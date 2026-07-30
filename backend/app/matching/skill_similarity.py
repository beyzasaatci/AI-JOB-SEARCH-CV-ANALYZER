from app.matching.embedding import create_embedding
from app.matching.similarity import calculate_similarity


def calculate_skill_similarity(
        cv_skills,
        job_skills
):

    if not cv_skills or not job_skills:
        return 0


    total_score = 0


    for cv_skill in cv_skills:

        best_match = 0


        cv_embedding = create_embedding(
            cv_skill
        )


        for job_skill in job_skills:

            job_embedding = create_embedding(
                job_skill
            )


            similarity = calculate_similarity(
                cv_embedding,
                job_embedding
            )


            if similarity > best_match:
                best_match = similarity


        total_score += best_match


    average = total_score / len(cv_skills)


    return round(
        average * 100,
        2
    )