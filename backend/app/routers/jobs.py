from fastapi import APIRouter, HTTPException

from app.services.job_search import search_jobs
from app.services.job_normalizer import normalize_jobs

from app.matching.matcher import match_jobs
from app.data.job_store import get_job


router = APIRouter()



# =================================
# JOB SEARCH
# =================================

@router.get("/jobs")
def get_jobs(
    keyword: str,
    location: str = "Turkey"
):

    # CareerJet API'den ilanları çek

    raw_jobs = search_jobs(
        keyword,
        location
    )


    # CareerJet formatını kendi modelimize çevir

    jobs = normalize_jobs(
        raw_jobs
    )


    return {

        "count": len(jobs),

        "jobs": [
            job.model_dump()
            for job in jobs
        ]

    }




# =================================
# JOB MATCHING
# =================================

@router.post("/jobs/match")
def match_job_list(
    candidate_text: str,
    candidate_skills: list[str]
):


    # Daha önce upload-cv sırasında
    # save_jobs() ile kaydedilen ilanları alıyoruz

    jobs = [

        get_job(i)

        for i in range(1, 100)

        if get_job(i) is not None

    ]



    if not jobs:

        raise HTTPException(

            status_code=404,

            detail="No jobs found"

        )



    # Embedding + skill matching

    matches = match_jobs(

        candidate_text,

        jobs,

        candidate_skills

    )



    return {

        "count": len(matches),

        "matches": matches

    }