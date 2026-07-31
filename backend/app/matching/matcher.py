from concurrent.futures import ThreadPoolExecutor

from app.matching.embedding import create_embedding
from app.matching.similarity import calculate_similarity
from app.ai.skill_matcher import ai_skill_match

from app.matching.embedding_cache import (
    embedding_cache,
    save_cache
)

from app.matching.job_filter import remove_duplicate_jobs



MAX_AI_JOBS = 6



def match_jobs(
    candidate_text,
    jobs,
    candidate_skills=None
):


    if candidate_skills is None:
        candidate_skills = []



    jobs = remove_duplicate_jobs(
        jobs
    )



    candidate_embedding = create_embedding(
        candidate_text
    )



    scored_jobs = []



    # ======================
    # SEMANTIC SEARCH
    # ======================


    for index, job in enumerate(jobs):


        job_text = f"""
Title:
{job.title}

Description:
{job.description[:1000]}
"""



        if job_text in embedding_cache:


            print(
                "EMBEDDING CACHE HIT"
            )


            job_embedding = embedding_cache[job_text]



        else:


            print(
                "CREATING EMBEDDING"
            )


            job_embedding = create_embedding(
                job_text
            )


            embedding_cache[job_text] = job_embedding




        semantic_score = calculate_similarity(

            candidate_embedding,

            job_embedding

        )



        scored_jobs.append(

            {

                "id": index,

                "job": job,

                "job_text": job_text,

                "semantic_score": semantic_score

            }

        )



    # cache tek sefer kaydet
    save_cache()



    scored_jobs.sort(

        key=lambda x:x["semantic_score"],

        reverse=True

    )



    # ======================
    # AI MATCH TOP 6
    # ======================


    top_jobs = scored_jobs[:MAX_AI_JOBS]



    def ai_call(item):


        return ai_skill_match(

            candidate_text[:2000],

            item["job_text"][:1000]

        )



    with ThreadPoolExecutor(

        max_workers=2

    ) as executor:


        ai_results = list(

            executor.map(

                ai_call,

                top_jobs

            )

        )



    results = []



    # ======================
    # RESULT CREATE
    # ======================


    for index,item in enumerate(scored_jobs):


        job = item["job"]



        if index < MAX_AI_JOBS:


            ai_result = ai_results[index]



        else:


            # AI bakmadıysa semantic sonucu kullan

            ai_result = {

                "profession_match": 50,

                "skill_score": 50,

                "matched_skills": [],

                "missing_skills": [],

                "reason":
                "Semantic similarity match"

            }




        profession_score = ai_result.get(

            "profession_match",

            0

        )


        skill_score = ai_result.get(

            "skill_score",

            0

        )



        if not isinstance(

            profession_score,

            (int,float)

        ):

            profession_score = 0



        if not isinstance(

            skill_score,

            (int,float)

        ):

            skill_score = 0




        # SADECE AI KONTROL ETTİKLERİNİ ELE

        if index < MAX_AI_JOBS:


            if profession_score < 30:

                continue




        final_score = (

            item["semantic_score"] * 0.30

            +

            skill_score * 0.50

            +

            profession_score * 0.20

        )




        results.append(

            {

                "id": item["id"],


                "title": job.title,


                "company": job.company,


                "location": job.location,



                "semantic_score":
                round(
                    item["semantic_score"],
                    2
                ),



                "skill_score":
                round(
                    skill_score,
                    2
                ),



                "profession_match":
                round(
                    profession_score,
                    2
                ),



                "match_score":
                round(
                    final_score,
                    2
                ),



                "matched_skills":
                ai_result.get(
                    "matched_skills",
                    []
                ),



                "missing_skills":
                ai_result.get(
                    "missing_skills",
                    []
                ),



                "reason":
                ai_result.get(
                    "reason",
                    ""
                ),



                "url":
                job.posting_url

            }

        )



    results.sort(

        key=lambda x:x["match_score"],

        reverse=True

    )



    return results