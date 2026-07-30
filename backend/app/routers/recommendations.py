from fastapi import APIRouter, HTTPException
from app.data.cv_store import get_cv

from app.data.job_store import get_job
from app.ai.groq_agent import analyze_cv
from app.models.recommendation import Recommendation
from app.models.recommendation_request import RecommendationRequest


router = APIRouter()



@router.post(
    "/jobs/{job_id}/recommendations",
    response_model=Recommendation
)
def get_recommendation(
    job_id: int,
    request: RecommendationRequest
):


    job = get_job(job_id)


    if job is None:

        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )


    job_text = (
        f"{job.title}\n\n"
        f"{job.description}"
    )


    cv_text = get_cv(
        request.file_id
    )


    if cv_text is None:
        raise HTTPException(
            status_code=404,
            detail="CV not found"
        )


    return analyze_cv(
        cv_text,
        job_text
    )