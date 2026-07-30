from app.matching.embedding import create_embedding
from app.matching.similarity import calculate_similarity
from app.matching.skill_match import calculate_skill_overlap
from app.matching.job_skill_extractor import extract_job_skills
from app.ai.job_skill_inference import infer_job_skills
from app.data.skills import normalize_skill
from app.matching.embedding_cache import embedding_cache
from app.matching.job_filter import remove_duplicate_jobs


def normalize_skill_list(skills):

    normalized = []

    for skill in skills:
        normalized.append(
            normalize_skill(skill)
        )

    return list(dict.fromkeys(normalized))


def match_jobs(
        candidate_text,
        jobs,
        candidate_skills=None
):

    if candidate_skills is None:
        candidate_skills = []


    jobs = remove_duplicate_jobs(jobs)


    candidate_embedding = create_embedding(
        candidate_text
    )


    candidate_skills = normalize_skill_list(
        candidate_skills
    )


    results = []


    MAX_AI_JOBS = 10
    ai_count = 0


    for index, job in enumerate(jobs):


        job_text = (
            f"{job.title} {job.description}"
        )


        # =========================
        # EMBEDDING
        # =========================

        if job_text in embedding_cache:

            print("EMBEDDING CACHE HIT")

            job_embedding = embedding_cache[job_text]


        else:

            print("CREATING EMBEDDING")

            job_embedding = create_embedding(
                job_text
            )

            embedding_cache[job_text] = job_embedding



        semantic_score = calculate_similarity(
            candidate_embedding,
            job_embedding
        )


        # =========================
        # SKILLS
        # =========================

        explicit_skills = extract_job_skills(
            job_text
        )

        print("REGEX:", explicit_skills)



        # Regex yeterliyse AI çağırma
        if len(explicit_skills) >= 2:


            job_skills = normalize_skill_list(
                explicit_skills
            )


        else:

            ai_skills = []


            if ai_count < MAX_AI_JOBS:


                ai_skills = infer_job_skills(
                    job_text
                )


                ai_count += 1



            job_skills = normalize_skill_list(
                explicit_skills + ai_skills
            )



        # =========================
        # SKILL SCORE
        # =========================

        skill_score = calculate_skill_overlap(
            candidate_skills,
            job_skills
        )



        # =========================
        # FINAL SCORE
        # =========================

        final_score = (

            semantic_score * 0.45

            +

            skill_score * 0.55

        )



        results.append(
            {

                # YENİ EKLENDİ
                "id": index + 1,


                "title": job.title,


                "company": job.company,


                "location": job.location,


                "semantic_score": round(
                    semantic_score,
                    2
                ),


                "skill_score": round(
                    skill_score,
                    2
                ),


                "match_score": round(
                    final_score,
                    2
                ),


                "skills_found": job_skills,


                "url": job.posting_url

            }
        )



    results.sort(
        key=lambda x: x["match_score"],
        reverse=True
    )


    return results