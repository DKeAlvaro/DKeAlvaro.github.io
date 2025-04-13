import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// vite.config.ts
export default defineConfig({
    plugins: [react()],
    server: {
      watch: {
        usePolling: true,
      },
      fs: {
        allow: ['src']
      }
    },
  });
  