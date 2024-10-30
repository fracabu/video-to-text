# Video-to-Text

![image](https://github.com/user-attachments/assets/6c6ebd12-1fde-462a-b410-c21a2a977977)




**Una soluzione per rendere i contenuti video più accessibili per tutti.**

## Descrizione

Questa applicazione nasce dall’esigenza di rendere i contenuti video accessibili a un pubblico più ampio, superando le barriere uditive, linguistiche ed economiche. L'app consente di:

- **Convertire i video in audio**.
- **Trascrivere l’audio in testo** per chi ha difficoltà uditive.
- **Tradurre il testo** in diverse lingue (attualmente solo in inglese, con piani di espansione per altre lingue in futuro).

L'obiettivo è offrire uno strumento versatile e facilmente utilizzabile, che possa essere impiegato da chiunque per accedere a informazioni contenute in video, superando ostacoli uditivi o linguistici.

## Funzionalità

- **Estrazione Audio**: Converte video di YouTube in file audio.
- **Trascrizione del testo**: Trasforma l’audio estratto in testo, utile per persone con problemi di udito.
- **Traduzione del testo**: Traduce il testo trascritto in una lingua di destinazione (attualmente solo inglese).
- **Interfaccia intuitiva**: Visualizza lo stato di avanzamento delle operazioni in tempo reale.

## Tecnologie Utilizzate

### Backend
- **Flask**: Framework di microservizi per creare l'API REST.
- **Whisper**: Modello di machine learning per la trascrizione e traduzione multilingue.
- **yt-dlp**: Strumento per scaricare audio/video da YouTube.
- **Werkzeug**: Per la gestione sicura delle richieste e delle operazioni di upload dei file.
- **CORS**: Configurazione delle policy di cross-origin per una gestione sicura delle richieste.

### Frontend
- **React**: Libreria per la costruzione dell’interfaccia utente.
- **Componenti UI personalizzati**: Per una migliore esperienza utente.
- **Fetch API**: Per la comunicazione asincrona tra frontend e backend.

### Altre Librerie
- **Python**: Linguaggio di programmazione utilizzato per il backend.
- **JavaScript (ES6)**: Linguaggio di programmazione utilizzato per il frontend.

## Requisiti

- **Python 3.x** (consigliata versione 3.8 o superiore)
- **Node.js** e **npm** (per eseguire il frontend React)
- **yt-dlp** (può essere installato tramite pip)

## Installazione

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

## Utilizzo

1. **Inserisci l'URL di un video di YouTube** nell'app per estrarre l'audio.
2. **Carica il file audio** per trascriverlo in testo.
3. **Seleziona la lingua** per tradurre il testo (al momento solo inglese).
4. **Visualizza e scarica** il testo trascritto o tradotto.

## Prossimi Sviluppi

- Supporto per il caricamento di file video locali.
- Supporto per diversi formati video e audio (es. `.mp4`, `.wav`, `.ogg`).
- Estensione del supporto alla traduzione in più lingue.

## Contributi

Siete benvenuti a contribuire al progetto! Per iniziare:

1. Fai un fork del progetto.
2. Crea un branch per la tua nuova feature (`git checkout -b feature/nuova-funzionalità`).
3. Effettua i tuoi cambiamenti e committali (`git commit -am 'Aggiunta nuova funzionalità'`).
4. Effettua un push del branch (`git push origin feature/nuova-funzionalità`).
5. Invia una pull request.

## Licenza

Questo progetto è distribuito sotto licenza MIT. Consulta il file [LICENSE](./LICENSE) per maggiori informazioni.

