from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(
        candidate_embedding,
        job_embedding
):

    score = cosine_similarity(
        [candidate_embedding],
        [job_embedding]
    )[0][0]


    return round(float(score) * 100, 2)