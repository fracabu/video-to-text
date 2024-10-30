# Video to Text Transcriber

Trascrivi automaticamente file audio e video in testo utilizzando Python e Whisper di OpenAI. Questa soluzione è completamente gratuita e illimitata, senza dipendere da servizi cloud a pagamento. Tutto viene eseguito localmente sul tuo computer.

## 🚀 Caratteristiche

- **Trascrizione Locale**: Elaborazione completamente offline sul tuo PC
- **Supporto Multi-formato**: Compatibile con vari formati audio/video (mp3, wav, mp4, etc.)
- **Multi-lingua**: Riconoscimento automatico della lingua con alta precisione
- **Organizzazione Automatica**: Le trascrizioni vengono salvate con timestamp per facile riferimento
- **Gratuito e Illimitato**: Nessun costo o limite di utilizzo

## 📋 Requisiti di Sistema

- Python 3.7 o superiore
- FFmpeg installato sul sistema
- Spazio su disco per i modelli di Whisper
- RAM consigliata: minimo 8GB

## 🔧 Installazione

1. Clona il repository:
```bash
git clone [URL-del-tuo-repository]
cd video-to-text
```

2. Crea un ambiente virtuale:
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate # Linux/Mac
```

3. Installa le dipendenze:
```bash
pip install -r requirements.txt
```

## 📦 Struttura del Progetto

```
video-to-text/
│
├── Transcriptions/        # Cartella per file audio e trascrizioni
│   └── .gitkeep
├── script.py             # Script principale
├── text.py              # Funzioni di trascrizione
├── requirements.txt     # Dipendenze Python
└── README.md           # Documentazione
```

## 🎯 Utilizzo

1. Inserisci i tuoi file audio/video nella cartella `Transcriptions`
2. Aggiungi i nomi dei file al `audio_list.json`
3. Esegui lo script:
```bash
python text.py
```
4. Le trascrizioni verranno salvate nella cartella `Transcriptions` con timestamp

## ⚙️ Configurazione

Il programma supporta varie opzioni di Whisper:
- Modelli disponibili: tiny, base, small, medium, large
- Supporto per traduzione automatica
- Riconoscimento automatico della lingua

## 📝 Note

- La prima esecuzione scaricherà il modello Whisper selezionato
- Il tempo di elaborazione dipende dalla lunghezza del file e dalla potenza del PC
- È consigliato utilizzare file audio di buona qualità per risultati migliori

## 🤝 Contribuire

Sentiti libero di:
1. Fare fork del repository
2. Creare un branch per le tue modifiche
3. Inviare una Pull Request

## 📄 Licenza

Questo progetto è distribuito con licenza MIT. Vedi il file `LICENSE` per maggiori dettagli.
