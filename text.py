import os
import yt_dlp
from datetime import datetime
import json
import whisper

def download_youtube_audio(url, folder_path):
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

def transcribe_audio(audio_path):
    try:
        model = whisper.load_model("base")
        result = model.transcribe(audio_path)
        return result
    except Exception as e:
        print(f"Errore durante la trascrizione: {str(e)}")
        raise

# Solo se il file viene eseguito direttamente
if __name__ == "__main__":
    folder_path = 'Transcriptions'
    os.makedirs(folder_path, exist_ok=True)

    # Richiedi l'URL del video
    video_input = input("Inserisci l'URL del video di YouTube: ")

    # Scarica solo l'audio dal video
    audio_filename = download_youtube_audio(video_input, folder_path)

    # Aggiorna la lista degli audio scaricati
    update_audio_list(folder_path, audio_filename)

    print(f"Download completato. Il file audio è stato salvato come: {audio_filename}")
    print("Il nome del file è stato aggiunto a 'audio_list.json' nella cartella Transcriptions.")