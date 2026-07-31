from fastapi import FastAPI
from app.routers.upload import router as upload_router
from app.routers.jobs import router as jobs_router
from app.routers import recommendations
from fastapi.middleware.cors import CORSMiddleware
from app.routers import locations

app = FastAPI(
    title="AI Job Search CV Analyzer",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def root():
    return {"message": "Backend is running"}

app.include_router(upload_router)
app.include_router(jobs_router)

app.include_router(
    recommendations.router
)
app.include_router(
    locations.router
)