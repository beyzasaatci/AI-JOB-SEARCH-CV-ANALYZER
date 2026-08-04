from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.routers.upload import router as upload_router
from app.routers.jobs import router as jobs_router
from app.routers import recommendations
from app.routers import locations

app = FastAPI(
    title="AI Job Search CV Analyzer",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Routers
app.include_router(upload_router, prefix="/api")
app.include_router(jobs_router, prefix="/api")
app.include_router(recommendations.router, prefix="/api")
app.include_router(locations.router, prefix="/api")

# React static files
app.mount("/assets", StaticFiles(directory="static/assets"), name="assets")


# React index
@app.get("/")
async def root():
    return FileResponse("static/index.html")


# React Router support
@app.get("/{full_path:path}")
async def spa(full_path: str):
    # API istekleri buraya düşmesin
    if full_path.startswith("api"):
        return {"detail": "Not Found"}

    return FileResponse("static/index.html")