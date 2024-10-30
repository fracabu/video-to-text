import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path'; // Import necessario per risolvere i percorsi

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'), // Definisce '@' come alias per la cartella 'src'
    },
  },
  server: {
    watch: {
      usePolling: true,
    },
  },
});
