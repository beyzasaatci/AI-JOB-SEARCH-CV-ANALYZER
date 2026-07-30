import json
import os
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq


# backend/.env dosyasını yükle
load_dotenv(Path(__file__).resolve().parents[2] / ".env")

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY not found. Please create backend/.env and add your API key."
    )

client = Groq(api_key=api_key)


def parse_cv(cv_text: str):

    prompt = f"""
You are an expert resume parser.

Extract the resume into JSON.

Return ONLY valid JSON.

Schema:
{{
    "name": "",
    "title": "",
    "skills": [],
    "years_of_experience": 0,
    "work_history": [
        {{
            "company": "",
            "position": "",
            "start_date": "",
            "end_date": "",
            "description": ""
        }}
    ],
    "education": [
        {{
            "school": "",
            "degree": "",
            "field": "",
            "graduation_year": ""
        }}
    ],
    "certifications": [],
    "languages": []
}}

Resume:

{cv_text}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response.choices[0].message.content.strip()

    print("========== GROQ RESPONSE ==========")
    print(content)
    print("===================================")

    if content.startswith("```json"):
        content = content.replace("```json", "").replace("```", "").strip()

    elif content.startswith("```"):
        content = content.replace("```", "").strip()

    profile = json.loads(content)

    profile["text"] = cv_text

    return profile