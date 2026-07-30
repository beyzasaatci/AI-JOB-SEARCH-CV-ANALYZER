from app.models.job import JobPosting
from app.matching.matcher import match_jobs


jobs = [
    JobPosting(
        title="Backend Developer",
        company="Test Company",
        location="Istanbul",
        description="""
        Python FastAPI Docker AWS PostgreSQL developer
        """,
        posting_url="test",
        source="careerjet"
    )
]


candidate_text = """
Python developer with FastAPI Docker AWS experience
"""


candidate_skills = [
    "python",
    "fastapi",
    "docker",
    "aws",
    "developer"
]


results = match_jobs(
    candidate_text,
    jobs,
    candidate_skills=candidate_skills
)


print(results)