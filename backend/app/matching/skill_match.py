def calculate_skill_overlap(
        candidate_skills,
        job_skills
):


    if not job_skills:
        return 0



    candidate_set = set(
        candidate_skills
    )


    job_set = set(
        job_skills
    )


    matched = (
        candidate_set &
        job_set
    )


    score = (
        len(matched)
        /
        len(job_set)
    ) * 100


    return round(score,2)