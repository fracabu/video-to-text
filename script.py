import os
import yt_dlp
from datetime import datetime
import json
import shutil
import whisper
from pathlib import Path

def process_input_source(folder_path):
    print("\nScegli la sorgente dell'audio:")
    print("1. Video YouTube (URL)")
    print("2. File locale (video o audio)")
    choice = input("Inserisci il numero della tua scelta (1 o 2): ")

    if choice == "1":
        url = input("\nInserisci l'URL del video di YouTube: ")
        audio_filename = download_youtube_audio(url, folder_path)
    elif choice == "2":
        file_path = input("\nInserisci il percorso completo del file: ")
        audio_filename = process_local_file(file_path, folder_path)
    else:
        raise ValueError("Scelta non valida. Seleziona 1 o 2.")
    
    # Dopo aver ottenuto il file audio, procedi con la trascrizione
    audio_path = os.path.join(folder_path, audio_filename)
    transcribe_audio(audio_path, folder_path)
    
    return audio_filename

def download_youtube_audio(url, folder_path):
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"audio_{timestamp}.mp3"
        output_path = os.path.join(folder_path, output_filename)
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_path,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        if not os.path.exists(output_path) and os.path.exists(output_path + ".mp3"):
            os.rename(output_path + ".mp3", output_path)
        
        print(f"Audio scaricato in: {output_path}")
        return output_filename
    except Exception as e:
        print(f"Errore durante il download da YouTube: {str(e)}")
        raise

def process_local_file(file_path, folder_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File non trovato: {file_path}")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"audio_{timestamp}.mp3"
        output_path = os.path.join(folder_path, output_filename)

        if file_path.lower().endswith('.mp3'):
            shutil.copy2(file_path, output_path)
            print(f"File MP3 copiato in: {output_path}")
        else:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': output_path,
                'enable_file_urls': True,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([f"file:{file_path}"])

            print(f"File convertito in MP3 e salvato in: {output_path}")

        return output_filename
    except Exception as e:
        print(f"Errore durante l'elaborazione del file locale: {str(e)}")
        raise

def transcribe_audio(audio_path, folder_path):
    try:
        print("\nInizio trascrizione del file audio...")
        print("Caricamento del modello Whisper...")
        
        # Carica il modello Whisper
        model = whisper.load_model("base")
        
        print("Trascrizione in corso...")
        # Esegue la trascrizione
        result = model.transcribe(audio_path)
        
        # Salva la trascrizione
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_filename = os.path.splitext(os.path.basename(audio_path))[0]
        transcript_filename = f"trascrizione_{base_filename}_{timestamp}.txt"
        transcript_path = os.path.join(folder_path, transcript_filename)
        
        with open(transcript_path, 'w', encoding='utf-8') as f:
            f.write(result["text"])
        
        print(f"\nTrascrizione completata e salvata in: {transcript_path}")
        print("\nAnteprima della trascrizione:")
        print("-" * 50)
        preview = result["text"][:200] + "..." if len(result["text"]) > 200 else result["text"]
        print(preview)
        print("-" * 50)

    except Exception as e:
        print(f"Errore durante la trascrizione: {str(e)}")
        raise

def update_audio_list(folder_path, audio_filename):
    list_file = os.path.join(folder_path, 'audio_list.json')
    try:
        if os.path.exists(list_file):
            with open(list_file, 'r') as f:
                audio_list = json.load(f)
        else:
            audio_list = []
        
        audio_list.append(audio_filename)
        
        with open(list_file, 'w') as f:
            json.dump(audio_list, f, indent=4)
    except Exception as e:
        print(f"Errore durante l'aggiornamento di audio_list.json: {str(e)}")
        raise

def main():
    # Creazione della cartella per le trascrizioni
    folder_path = 'Transcriptions'
    os.makedirs(folder_path, exist_ok=True)

    try:
        # Processo di input, conversione e trascrizione
        audio_filename = process_input_source(folder_path)

        # Aggiorna la lista degli audio
        update_audio_list(folder_path, audio_filename)

        print("\nProcesso completato con successo!")
        print(f"File audio salvato come: {audio_filename}")
        print("Il nome del file è stato aggiunto a 'audio_list.json' nella cartella Transcriptions.")

    except Exception as e:
        print(f"\nErrore durante l'esecuzione del programma: {str(e)}")
        print("Il programma è stato interrotto a causa di un errore.")

if __name__ == "__main__":
    main()