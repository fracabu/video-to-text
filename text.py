
import os
import whisper
import json
from datetime import datetime

def transcribe_audio(audio_path, model_name='base'):
    print(f"Caricamento del modello {model_name}...")
    model = whisper.load_model(model_name)
    
    print(f"Inizio trascrizione di {audio_path}...")
    result = model.transcribe(audio_path )
    # result = model.transcribe(audio_path, language='it')
    # result = model.transcribe(audio_path, task='translate')


    return result['text']

def save_transcription(transcription, folder_path, audio_filename):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    transcription_filename = f"trascrizione_{timestamp}_{audio_filename}.txt"
    file_path = os.path.join(folder_path, transcription_filename)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(transcription)
    return file_path

def get_audio_list(folder_path):
    list_file = os.path.join(folder_path, 'audio_list.json')
    if os.path.exists(list_file):
        with open(list_file, 'r') as f:
            return json.load(f)
    return []

# Percorso della cartella
folder_path = 'Transcriptions'

# Ottieni la lista degli audio disponibili
audio_list = get_audio_list(folder_path)

if not audio_list:
    print("Nessun file audio disponibile per la trascrizione.")
    exit()

# Mostra la lista degli audio disponibili
print("File audio disponibili:")
for i, audio in enumerate(audio_list, 1):
    print(f"{i}. {audio}")

# Chiedi all'utente di selezionare un file
selection = int(input("Seleziona il numero del file audio da trascrivere: ")) - 1

if 0 <= selection < len(audio_list):
    selected_audio = audio_list[selection]
    audio_path = os.path.join(folder_path, selected_audio)

    # Trascrivi l'audio
    transcription = transcribe_audio(audio_path)

    # Salva la trascrizione
    transcription_path = save_transcription(transcription, folder_path, selected_audio)

    print(f"Trascrizione completata e salvata in: {transcription_path}")
    print("Anteprima della trascrizione:")
    print(transcription[:100] + "...")
else:
    print("Selezione non valida.")