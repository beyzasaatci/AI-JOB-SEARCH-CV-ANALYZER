# 🚀 AI Job Search CV Analyzer

An AI-powered cloud-native web application that analyzes resumes, extracts candidate skills using Large Language Models (LLMs), searches live job opportunities, and generates personalized career recommendations.

The application is fully containerized with Docker and deployed on **AWS ECS Fargate**.

---

# ✨ Features

- 📄 Upload CV (PDF / DOCX)
- 🤖 AI-powered CV analysis using Groq LLM
- 🧠 Automatic skill extraction
- 🔍 Live job search
  - Adzuna API
  - RapidAPI Jobs API
- 🎯 AI-powered job matching
- 📊 Match score calculation
- 💬 Personalized career recommendations
- 🌍 Country & city selection
- ☁️ AWS Cloud deployment
- 📦 Dockerized frontend & backend

---

# 🏗 Architecture

```
                   +----------------------+
                   |      React + Vite    |
                   |      Frontend        |
                   +----------+-----------+
                              |
                          REST API
                              |
                              ▼
                    +--------------------+
                    |      FastAPI       |
                    |      Backend       |
                    +----------+---------+
                               |
         +---------------------+-----------------------+
         |                     |                       |
         ▼                     ▼                       ▼
     Groq API            Adzuna API           RapidAPI Jobs
         |
         ▼
 AI Skill Extraction & Recommendations
```

---

# 🛠 Tech Stack

## Frontend

- React
- Vite
- Axios
- TailwindCSS

## Backend

- FastAPI
- Python
- Uvicorn
- Pydantic
- Boto3

## AI

- Groq LLM

## APIs

- Adzuna API
- RapidAPI Jobs API

## Cloud

- AWS ECS Fargate
- Amazon ECR
- Amazon S3
- AWS Secrets Manager
- Docker

---

# 📁 Project Structure

```
AI-JOB-SEARCH-CV-ANALYZER
│
├── app/
│   ├── routers/
│   ├── services/
│   ├── data/
│   └── main.py
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── vite.config.js
│
├── Dockerfile
├── requirements.txt
├── ecs-task-definition.json
└── README.md
```

---

# ⚙️ Local Installation

## Clone Repository

```bash
git clone https://github.com/beyzasaatci/AI-JOB-SEARCH-CV-ANALYZER.git

cd AI-JOB-SEARCH-CV-ANALYZER
```

---

## Backend

Create virtual environment

```bash
python -m venv venv
```

Activate

Mac/Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install packages

```bash
pip install -r requirements.txt
```

Run backend

```bash
uvicorn app.main:app --reload
```

Backend

```
http://localhost:8000
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend

```
http://localhost:5173
```

---

# 🐳 Docker

Build backend image

```bash
docker build \
--platform linux/amd64 \
-t ai-job-backend .
```

Run

```bash
docker run -p 8000:8000 ai-job-backend
```

---

# ☁ AWS Deployment

The application is deployed on **Amazon Web Services** using:

- Amazon ECS Fargate
- Amazon ECR
- Amazon S3
- AWS Secrets Manager

Deployment workflow:

1. Build Docker images
2. Push images to Amazon ECR
3. Register ECS Task Definition
4. Deploy containers on ECS Fargate


---

# 🔐 Environment Variables

The backend requires:

```
GROQ_API_KEY
RAPIDAPI_KEY
ADZUNA_APP_ID
ADZUNA_APP_KEY
AWS_REGION
AWS_BUCKET_NAME
```



---

# 👩‍💻 Author

**Beyza Saatci**

Computer Engineering Student

GitHub:

https://github.com/beyzasaatci

LinkedIn:

(Add your LinkedIn profile here)

---

# 📄 Note

This project was developed for educational and portfolio purposes.
