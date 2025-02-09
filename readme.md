# 🎥 Video-to-Text

![image](https://github.com/user-attachments/assets/6cb173af-dd3d-451b-9aec-64cd77af9171)


**Rendi i contenuti video accessibili a tutti.**

## 📖 Descrizione

**Video-to-Text** è un'applicazione progettata per abbattere le barriere uditive, linguistiche ed economiche, rendendo i contenuti video accessibili a un pubblico più ampio. Le principali funzionalità includono:

- **Conversione Video-Audio**: Estrai l'audio dai video.
- **Trascrizione Audio-Testo**: Converte l'audio in testo, utile per persone con difficoltà uditive.
- **Traduzione Testo**: Traduce il testo trascritto in diverse lingue (attualmente supporta l'inglese, con piani di espansione per altre lingue).

## ✨ Funzionalità

- **Estrazione Audio**: Converte video di YouTube in file audio.
- **Trascrizione del Testo**: Trasforma l’audio estratto in testo.
- **Traduzione del Testo**: Traduce il testo trascritto in una lingua di destinazione.
- **Interfaccia Intuitiva**: Visualizza lo stato di avanzamento delle operazioni in tempo reale.

## 🛠️ Tecnologie Utilizzate

### Backend

- **Flask**: Framework per creare l'API REST.
- **Whisper**: Modello di machine learning per trascrizione e traduzione multilingue.
- **yt-dlp**: Strumento per scaricare audio/video da YouTube.
- **Werkzeug**: Gestione sicura delle richieste e upload dei file.
- **CORS**: Configurazione delle policy di cross-origin.

### Frontend

- **React**: Libreria per la costruzione dell’interfaccia utente.
- **Componenti UI Personalizzati**: Per una migliore esperienza utente.
- **Fetch API**: Comunicazione asincrona tra frontend e backend.

### Altre Librerie

- **Python**: Linguaggio di programmazione per il backend.
- **JavaScript (ES6)**: Linguaggio di programmazione per il frontend.

## 📋 Requisiti

- **Python 3.x** (consigliata versione 3.8 o superiore)
- **Node.js** e **npm** (per eseguire il frontend React)
- **yt-dlp** (installabile tramite pip)

## 🚀 Installazione

### Backend (Flask)

1. **Clona il repository:**

   ```bash
   git clone https://github.com/fracabu/video-to-text.git
   cd video-to-text
   ```

2. **Crea e attiva un ambiente virtuale:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Su Windows: venv\Scripts\activate
   ```


3. **Installa le dipendenze richieste:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Avvia il server Flask:**

   ```bash
   python api.py
   ```

### Frontend (React)

1. **Naviga nella cartella `frontend` e installa le dipendenze:**

   ```bash
   cd frontend
   npm install
   ```

2. **Avvia l'applicazione React:**

   ```bash
   npm start
   ```

3. **Apri l'applicazione in un browser all'indirizzo:** `http://localhost:3000`

## 🚀 Avvio dell'Applicazione Completa

Per far funzionare l'applicazione completa, avrai bisogno di aprire due terminali:

1. **Primo terminale (Backend - Flask):**
   ```bash
   cd C:\Users\utente\video-to-text
   .\venv\Scripts\activate
   python api.py
   ```
   ![image](https://github.com/user-attachments/assets/0c13d6f6-21db-47b3-8098-d4f06d938715)
   
   Questo avvierà il server Flask su [http://localhost:5000](http://localhost:5000).

2. **Secondo terminale (Frontend - React):**
   ```bash
   cd C:\Users\utente\video-to-text\frontend
   npm run dev
   ```
   ![image](https://github.com/user-attachments/assets/33821deb-9d55-4d77-a204-419a7366edd1)

   Questo avvierà il server di sviluppo React su [http://localhost:5173](http://localhost:5173).

### Flusso di Lavoro dell'Applicazione

1. L'interfaccia React (frontend) mostra la UI dove puoi inserire l'URL di YouTube.
2. Quando fai una richiesta, il frontend comunica con il backend Flask.
3. Il backend processa la richiesta (download video, conversione, trascrizione).
4. Il risultato viene rimandato al frontend e mostrato nell'interfaccia.

**Consiglio:** Tieni aperti entrambi i terminali affiancati così puoi vedere i log sia del frontend che del backend mentre l'app è in esecuzione.

## 📝 Utilizzo

1. **Inserisci l'URL di un video di YouTube** nell'app per estrarre l'audio.
2. **Carica il file audio** per trascriverlo in testo.
3. **Seleziona la lingua** per tradurre il testo (al momento solo inglese).
4. **Visualizza e scarica** il testo trascritto o tradotto.

## 🔧 Prossimi Sviluppi

- Supporto per il caricamento di file video locali.
- Supporto per diversi formati video e audio (es. `.mp4`, `.wav`, `.ogg`).
- Estensione del supporto alla traduzione in più lingue.

## 🤝 Contributi

Contributi sono benvenuti! Per iniziare:

1. Fai un fork del progetto.
2. Crea un branch per la tua nuova feature (`git checkout -b feature/nuova-funzionalità`).
3. Effettua i tuoi cambiamenti e committali (`git commit -am 'Aggiunta nuova funzionalità'`).
4. Effettua un push del branch (`git push origin feature/nuova-funzionalità`).
5. Invia una pull request.

## 📄 Licenza

Questo progetto è distribuito sotto licenza MIT. Consulta il file [LICENSE](./LICENSE) per maggiori informazioni.

## 📬 Contatti

Per domande o suggerimenti:

- **Email**: fracabu@gmail.com
- **LinkedIn**: [Francesco Capurso](https://www.linkedin.com/in/francesco-~-capurso-5801031a9/)
