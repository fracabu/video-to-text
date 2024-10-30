from flask import Flask, request, jsonify, session
from flask_cors import CORS
import whisper
import os
from werkzeug.utils import secure_filename
import yt_dlp  # Per il download dinamico da YouTube

app = Flask(__name__)
CORS(app)
app.secret_key = "una_chiave_segreta"

# Cartella per salvare i file caricati
UPLOAD_FOLDER = 'uploads'
TRANSCRIPTION_FOLDER = 'Transcriptions'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Crea le cartelle di upload e trascrizione se non esistono
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(TRANSCRIPTION_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return jsonify({"message": "API is working!"})

def download_progress_hook(d):
    if d['status'] == 'downloading':
        session['conversion_progress'] = float(d['downloaded_bytes']) / float(d['total_bytes']) * 100
    elif d['status'] == 'finished':
        session['conversion_progress'] = 100

@app.route('/api/convert', methods=['POST'])
def convert():
    try:
        session['conversion_progress'] = 0
        data = request.json
        url = data.get('url')
        
        if not url:
            return jsonify({'error': 'URL non fornito'}), 400

        print(f"Ricevuta richiesta di conversione per URL: {url}")
        
        folder_path = TRANSCRIPTION_FOLDER
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(folder_path, 'audio_%(id)s.%(ext)s'),
            'progress_hooks': [download_progress_hook]
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        audio_filename = os.path.basename(ydl.prepare_filename(ydl.extract_info(url, download=False)))

        return jsonify({
            'success': True,
            'message': 'Video convertito in audio con successo',
            'audio_filename': audio_filename
        })

    except Exception as e:
        print(f"Errore durante la conversione: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/upload', methods=['POST'])
def upload():
    try:
        session['upload_progress'] = 0

        if 'file' not in request.files:
            return jsonify({'error': 'Nessun file fornito'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'Nome del file non valido'}), 400

        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        file.save(file_path)
        session['upload_progress'] = 100  # Completa l'upload

        audio_filename = text.convert_video_to_audio(file_path, TRANSCRIPTION_FOLDER)

        return jsonify({
            'success': True,
            'message': 'File convertito in audio con successo',
            'audio_filename': audio_filename
        })

    except Exception as e:
        print(f"Errore durante il caricamento del file: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/progress', methods=['GET'])
def get_progress():
    conversion_progress = session.get('conversion_progress', 0)
    upload_progress = session.get('upload_progress', 0)
    return jsonify({
        'conversion_progress': conversion_progress,
        'upload_progress': upload_progress
    })

@app.route('/api/transcribe', methods=['POST'])
def transcribe():
    try:
        data = request.json
        filename = data.get('filename')
        
        if not filename:
            return jsonify({'error': 'Nome file non fornito'}), 400

        folder_path = TRANSCRIPTION_FOLDER
        file_path = os.path.join(folder_path, filename)

        if not os.path.exists(file_path):
            return jsonify({'error': 'File audio non trovato'}), 404

        print(f"Inizio trascrizione del file: {filename}")
        
        print("Caricamento del modello Whisper...")
        model = whisper.load_model("base")
        
        print("Trascrizione in corso...")
        result = model.transcribe(file_path)
        
        transcript_filename = f"trascrizione_{os.path.splitext(filename)[0]}.txt"
        transcript_path = os.path.join(folder_path, transcript_filename)
        
        with open(transcript_path, 'w', encoding='utf-8') as f:
            f.write(result["text"])

        return jsonify({
            'success': True,
            'message': 'Audio trascritto con successo',
            'text': result["text"],
            'transcript_file': transcript_filename
        })

    except Exception as e:
        print(f"Errore durante la trascrizione: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/files', methods=['GET'])
def get_files():
    try:
        audio_files = [f for f in os.listdir(TRANSCRIPTION_FOLDER) if f.endswith(('.mp3', '.wav'))]
        transcription_files = [f for f in os.listdir(TRANSCRIPTION_FOLDER) if f.endswith('.txt')]

        return jsonify({
            'audio': audio_files,
            'transcriptions': transcription_files
        })

    except Exception as e:
        print(f"Errore nel recupero dei file: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    print("Starting Flask server...")
    print("Available endpoints:")
    print("  GET  / - Test API connection")
    print("  POST /api/convert - Convert YouTube video to audio")
    print("  POST /api/upload - Upload and convert a file to audio")
    print("  GET  /api/progress - Get progress of ongoing conversion or upload")
    print("  POST /api/transcribe - Transcribe audio to text")
    print("  GET  /api/files - Get the list of generated files")
    print("\nServer running on http://localhost:5000")
    app.run(debug=True, port=5000)
