# ponytail: frontend build'i image icinde uretiliyor; backend/static elle kopyalanmiyor,
# boylece api.js degisip static/ eski kalma hatasi bir daha olmaz.
FROM node:22-slim AS frontend
WORKDIR /fe
COPY frontend/package*.json ./
RUN npm ci
COPY frontend/ ./
RUN npm run build

FROM python:3.11-slim
WORKDIR /app

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/app ./app
COPY backend/jobs.json ./jobs.json
COPY --from=frontend /fe/dist ./static

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
