from fastapi import APIRouter

from app.matching.matcher import match_jobs
from app.services.job_search import search_jobs
from app.services.job_normalizer import normalize_jobs

router = APIRouter()


@router.get("/jobs/match")
def get_matching_jobs(
    keyword: str,
    location: str = "Turkey"
):

    # 1- Jobları getir
    raw_jobs = search_jobs(
        keyword,
        location
    )


    # 2- Normalize et
    jobs = normalize_jobs(raw_jobs)


    # 3- Örnek CV bilgisi
    candidate_text = """
    Python developer with FastAPI,
    Docker, AWS, PostgreSQL experience.
    Building REST APIs and backend systems.
    """


    candidate_skills = [
        "python",
        "fastapi",
        "docker",
        "aws",
        "postgresql",
        "developer"
    ]


    # 4- Matching
    results = match_jobs(
        candidate_text,
        jobs,
        candidate_skills
    )


    return {
        "count": len(results),
        "matches": results
    }