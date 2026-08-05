from app.models.job import JobPosting


def normalize_jobs(data):

    jobs = []

    for item in data.get("jobs", []):

        job = JobPosting(
            title=item.get("title", ""),
            company=item.get("company", ""),
            location=item.get("locations", ""),
            description=item.get("description", ""),
            posting_url=item.get("url", ""),
            source="Adzuna"
        )

        jobs.append(job)

    return jobs