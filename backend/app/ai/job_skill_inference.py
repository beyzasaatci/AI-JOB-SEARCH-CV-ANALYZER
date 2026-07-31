import json
import os
import hashlib

from pathlib import Path
from dotenv import load_dotenv
from groq import Groq


load_dotenv(
    Path(__file__).resolve().parents[2] / ".env"
)


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


skill_cache = {}



def infer_job_skills(job_text: str):


    key = hashlib.md5(
        job_text.encode()
    ).hexdigest()



    if key in skill_cache:

        print("SKILL CACHE HIT")

        return skill_cache[key]



    print("GROQ SKILL EXTRACTION")



    prompt = f"""

You are an expert recruiter and career analyst.

Analyze this job description.

This system supports ALL professions:

- Software
- Engineering
- Finance
- Marketing
- Sales
- Human Resources
- Design
- Healthcare
- Operations
- Other professional fields


Extract:

1. category:
Main job field.


2. skills:
Required professional skills.


3. tools:
Software, platforms, systems, equipment or methods.


4. domain_knowledge:
Industry knowledge or expertise areas.



Rules:

- Return ONLY valid JSON.
- Do not invent unrelated skills.
- Do not focus only on technology.
- Do not include job titles as skills.
- Include only relevant professional skills.



Format:


{{
    "category": "",
    "skills": [],
    "tools": [],
    "domain_knowledge": []
}}



Job Description:


{job_text}

"""



    try:


        response = client.chat.completions.create(


            model="llama-3.1-8b-instant",


            temperature=0,


            response_format={
                "type": "json_object"
            },


            messages=[

                {
                    "role": "user",
                    "content": prompt
                }

            ]

        )



    except Exception as e:


        print(
            "GROQ ERROR:",
            e
        )


        return []



    try:


        data = json.loads(
            response.choices[0].message.content
        )


    except Exception as e:


        print(
            "JSON ERROR:",
            e
        )


        return []




    skills = []



    all_skills = (

        data.get(
            "skills",
            []
        )

        +

        data.get(
            "tools",
            []
        )

        +

        data.get(
            "domain_knowledge",
            []
        )

    )



    for x in all_skills:



        if isinstance(x, str):


            skills.append(
                x.lower().strip()
            )



        elif isinstance(x, dict):


            skill = (

                x.get("skill")

                or

                x.get("name")

                or

                x.get("technology")

            )



            if skill:


                skills.append(
                    skill.lower().strip()
                )




    skills = list(
        dict.fromkeys(skills)
    )



    skill_cache[key] = skills



    print(
        "AI SKILLS:",
        skills
    )



    return skills