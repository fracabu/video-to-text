import React, { useState, useEffect } from 'react';
import { Youtube, FileAudio, Upload, Loader2, Volume2, FileText } from 'lucide-react';
import { Button } from './components/ui/button';
import { Tabs, TabsList, TabsTrigger, TabsContent } from './components/ui/tabs';
import { Progress } from './components/ui/progress';

function App() {
  const [inputType, setInputType] = useState('youtube');
  const [url, setUrl] = useState('');
  const [file, setFile] = useState(null); // Stato per il file caricato
  const [isConverting, setIsConverting] = useState(false);
  const [isTranscribing, setIsTranscribing] = useState(false);
  const [conversionProgress, setConversionProgress] = useState(0);
  const [transcriptionProgress, setTranscriptionProgress] = useState(0);
  const [audioFile, setAudioFile] = useState(null);
  const [error, setError] = useState(null);
  const [activeTab, setActiveTab] = useState('convert');
  const [files, setFiles] = useState({
    audio: [],
    transcriptions: [],
    translations: [],
  });

  const POLLING_INTERVAL = 1000; // 1 secondo

  // Funzione per caricare file lato frontend
  const handleFileUpload = (e) => {
    const uploadedFile = e.target.files[0];
    if (uploadedFile && uploadedFile.type.includes('video')) {
      setFile(uploadedFile);
      setUrl(''); // Resetta l'URL se si carica un file
    } else {
      setError('File non valido. Carica un file video.');
    }
  };

  // Funzione per aggiornare il progresso reale dal server
  const fetchProgress = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/progress');
      const data = await response.json();

      if (data) {
        setConversionProgress(data.conversion_progress || 0);
        setTranscriptionProgress(data.upload_progress || 0);
      }
    } catch (err) {
      console.error('Errore durante il polling del progresso:', err);
    }
  };

  // Funzione per gestire la conversione dei file caricati
  const handleFileConversion = async (e) => {
    e.preventDefault();
    setIsConverting(true);
    setConversionProgress(0);
    setError(null);

    try {
      const formData = new FormData();
      formData.append('file', file);

      const response = await fetch('http://localhost:5000/api/upload', {
        method: 'POST',
        body: formData,
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || 'Errore durante la conversione');
      }

      setAudioFile(data.audio_filename);
      await loadFiles(); // Ricarica la lista dei file
    } catch (err) {
      setError(err.message);
    } finally {
      setIsConverting(false);
    }
  };

  // Polling per il progresso durante la conversione
  useEffect(() => {
    let interval;
    if (isConverting) {
      interval = setInterval(() => {
        fetchProgress();
      }, POLLING_INTERVAL);
    }
    return () => clearInterval(interval);
  }, [isConverting]);

  // Polling per il progresso durante la trascrizione
  useEffect(() => {
    let interval;
    if (isTranscribing) {
      interval = setInterval(() => {
        fetchProgress();
      }, POLLING_INTERVAL);
    }
    return () => clearInterval(interval);
  }, [isTranscribing]);

  // Carica la lista dei file
  const loadFiles = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/files');
      const data = await response.json();
      setFiles(data);
    } catch (error) {
      console.error('Errore nel caricamento dei file:', error);
    }
  };

  useEffect(() => {
    loadFiles();
  }, []);

  const handleConversion = async (e) => {
    e.preventDefault();
    if (file) {
      handleFileConversion(e); // Se c'è un file, gestisci la conversione del file
      return;
    }
    setIsConverting(true);
    setConversionProgress(0);
    setError(null);

    try {
      const response = await fetch('http://localhost:5000/api/convert', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || 'Errore durante la conversione');
      }

      setAudioFile(data.audio_filename);
      await loadFiles(); // Ricarica la lista dei file
    } catch (err) {
      setError(err.message);
    } finally {
      setIsConverting(false);
    }
  };

  const handleTranscription = async () => {
    if (!audioFile) return;

    setIsTranscribing(true);
    setTranscriptionProgress(0);
    setError(null);

    try {
      const response = await fetch('http://localhost:5000/api/transcribe', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ filename: audioFile }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || 'Errore durante la trascrizione');
      }

      await loadFiles(); // Ricarica la lista dei file
    } catch (err) {
      setError(err.message);
    } finally {
      setIsTranscribing(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-50 to-gray-100 dark:from-gray-900 dark:to-gray-800 p-8">
      <div className="max-w-6xl mx-auto space-y-8">
        {/* Header */}
        <div className="text-center space-y-4">
          <h1 className="text-4xl font-bold text-gray-900 dark:text-white">Video to Text</h1>
          <p className="text-lg text-gray-600 dark:text-gray-300">Converti video in audio e trascrivi in testo</p>
        </div>

        <div className="grid gap-6">
          {/* Conversion/Transcription Panel */}
          <div>
            <div className="bg-white/90 dark:bg-gray-800/90 backdrop-blur-sm rounded-xl shadow-xl p-6">
              <Tabs defaultValue="convert" className="space-y-6">
                <TabsList className="grid grid-cols-2">
                  <TabsTrigger value="convert" onClick={() => setActiveTab('convert')}>
                    <Volume2 className="mr-2 h-5 w-5" />
                    Converti
                  </TabsTrigger>
                  <TabsTrigger value="transcribe" onClick={() => setActiveTab('transcribe')}>
                    <FileText className="mr-2 h-5 w-5" />
                    Trascrivi
                  </TabsTrigger>
                </TabsList>

                <TabsContent value="convert">
                  <form onSubmit={handleConversion} className="space-y-4">
                    <input
                      type="text"
                      placeholder="Incolla l'URL del video YouTube"
                      className="w-full p-3 border dark:border-gray-700 dark:bg-gray-800 dark:text-white rounded-md"
                      value={url}
                      onChange={(e) => setUrl(e.target.value)}
                      disabled={isConverting || !!file}
                    />
                    <input
                      type="file"
                      accept="video/*"
                      className="w-full p-3 border dark:border-gray-700 dark:bg-gray-800 dark:text-white rounded-md"
                      onChange={handleFileUpload}
                      disabled={isConverting || url}
                    />
                    {isConverting && (
                      <div className="space-y-2">
                        <Progress value={conversionProgress} />
                        <p className="text-sm text-gray-500 dark:text-gray-400">
                          Conversione in corso: {conversionProgress}%
                        </p>
                      </div>
                    )}
                    <Button type="submit" className="w-full py-6" disabled={isConverting || (!url && !file)}>
                      {isConverting ? (
                        <>
                          <Loader2 className="mr-2 h-5 w-5 animate-spin" />
                          Conversione in corso...
                        </>
                      ) : (
                        'Converti in Audio'
                      )}
                    </Button>
                  </form>
                </TabsContent>

                <TabsContent value="transcribe">
                  <div className="space-y-4">
                    {audioFile ? (
                      <>
                        <div className="p-4 bg-green-50 dark:bg-green-900/30 rounded-md">
                          <p className="text-green-600 dark:text-green-400">File audio pronto: {audioFile}</p>
                        </div>
                        {isTranscribing && (
                          <div className="space-y-2">
                            <Progress value={transcriptionProgress} />
                            <p className="text-sm text-gray-500 dark:text-gray-400">
                              Trascrizione in corso: {transcriptionProgress}%
                            </p>
                          </div>
                        )}
                        <Button onClick={handleTranscription} className="w-full py-6" disabled={isTranscribing}>
                          {isTranscribing ? (
                            <>
                              <Loader2 className="mr-2 h-5 w-5 animate-spin" />
                              Trascrizione in corso...
                            </>
                          ) : (
                            'Trascrivi in Testo'
                          )}
                        </Button>
                      </>
                    ) : (
                      <div className="text-center text-gray-500 dark:text-gray-400">Prima converti un video in audio</div>
                    )}
                  </div>
                </TabsContent>
              </Tabs>

              {error && (
                <div className="mt-4 p-4 bg-red-50 dark:bg-red-900/30 text-red-600 dark:text-red-400 rounded-md">
                  {error}
                </div>
              )}
            </div>
          </div>

          {/* File List Panel */}
          <div className="bg-white/90 dark:bg-gray-800/90 backdrop-blur-sm rounded-xl shadow-xl p-6">
            <h2 className="text-xl font-semibold mb-4 dark:text-white">File Generati</h2>
            <Tabs defaultValue="audio">
              <TabsList className="grid grid-cols-2 mb-4">
                <TabsTrigger value="audio">
                  <Volume2 className="mr-2 h-4 w-4" />
                  Audio
                </TabsTrigger>
                <TabsTrigger value="text">
                  <FileText className="mr-2 h-4 w-4" />
                  Testi
                </TabsTrigger>
              </TabsList>

              <TabsContent value="audio">
                <div className="space-y-2">
                  {files.audio.length > 0 ? (
                    files.audio.map((file, index) => (
                      <div key={index} className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded">
                        <p className="text-sm">{file}</p>
                      </div>
                    ))
                  ) : (
                    <p className="text-sm text-gray-500 dark:text-gray-400">Nessun file audio trovato.</p>
                  )}
                </div>
              </TabsContent>

              <TabsContent value="text">
                <div className="space-y-2">
                  {files.transcriptions.length > 0 ? (
                    files.transcriptions.map((file, index) => (
                      <div key={index} className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded">
                        <p className="text-sm">{file}</p>
                      </div>
                    ))
                  ) : (
                    <p className="text-sm text-gray-500 dark:text-gray-400">Nessun file di testo trovato.</p>
                  )}
                </div>
              </TabsContent>
            </Tabs>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
