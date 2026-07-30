import json
from pathlib import Path

from app.models.job import JobPosting


BASE_DIR = Path(__file__).resolve().parents[2]

JOBS_FILE = BASE_DIR / "jobs.json"


def save_jobs(jobs):

    jobs_data = {}

    for index, job in enumerate(jobs):

        jobs_data[str(index + 1)] = job.model_dump()


    with open(
        JOBS_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            jobs_data,
            f,
            ensure_ascii=False,
            indent=4
        )


def get_job(job_id):

    print("READING:", JOBS_FILE)

    if not JOBS_FILE.exists():
        print("jobs.json bulunamadı")
        return None


    with open(
        JOBS_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        jobs = json.load(f)


    print("AVAILABLE IDS:", list(jobs.keys())[:10])


    job_data = jobs.get(
        str(job_id)
    )


    if job_data is None:
        print("JOB YOK:", job_id)
        return None


    return JobPosting(
        **job_data
    )