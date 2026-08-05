import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  plugins: [
    react(),
    tailwindcss(),
  ],
  // ponytail: baseURL "/api" relative; dev'de backend'e proxy'le, prod'da FastAPI zaten servis ediyor
  server: {
    proxy: {
      "/api": "http://localhost:8000",
    },
  },
});