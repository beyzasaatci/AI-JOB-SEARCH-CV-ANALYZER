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
    You are a senior technical recruiter.

    Read the following job description.

    Extract ONLY the technical skills that are explicitly mentioned.

    Rules:
    - Return ONLY valid JSON.
    - Do NOT guess missing technologies.
    - Do NOT invent skills.
    - Do NOT include soft skills.
    - Do NOT include job titles.
    - Preserve original technology names.

    Format:

    {{
        "skills": [
            "Java",
            "Spring Boot",
            "Docker"
        ]
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

        print("GROQ ERROR:", e)

        return []

    data = json.loads(
        response.choices[0].message.content
    )

    skills = []

    for x in data.get("skills", []):

        if isinstance(x, str):

            skills.append(
                x.lower().strip()
            )

        elif isinstance(x, dict):

            skill = (
                x.get("skill")
                or x.get("name")
                or x.get("technology")
            )

            if skill:

                skills.append(
                    skill.lower().strip()
                )

    skill_cache[key] = skills

    print("AI SKILLS:", skills)

    return skills