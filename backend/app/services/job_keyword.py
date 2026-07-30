def generate_job_keywords(skills):

    keywords = []


    skill_map = {

        "python": [
            "Python Developer",
            "Backend Developer"
        ],

        "java": [
            "Java Developer",
            "Software Developer"
        ],

        "sql": [
            "Backend Developer",
            "Database Developer"
        ],

        "react": [
            "Frontend Developer"
        ],

        "docker": [
            "DevOps Engineer",
            "Backend Developer"
        ],

        "aws": [
            "Cloud Engineer",
            "Backend Developer"
        ]

    }


    for skill in skills:

        skill_lower = skill.lower()


        for key, jobs in skill_map.items():

            if key in skill_lower:

                keywords.extend(jobs)



    # duplicate temizle

    keywords = list(
        dict.fromkeys(keywords)
    )


    return keywords[:5]