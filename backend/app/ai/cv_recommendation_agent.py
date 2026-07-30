import json
import os

from pathlib import Path
from dotenv import load_dotenv
from groq import Groq


load_dotenv(
    Path(__file__).resolve().parents[2] / ".env"
)


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_recommendations(
    cv_text: str,
    job_text: str
):

    prompt = f"""
You are an expert technical recruiter.

Compare the candidate CV with the job description.

Return ONLY valid JSON.

Format:

{{
  "missing_skills": [],
  "redundant_content": [],
  "improvement_suggestions": [],
  "overall_fit_score": 0,
  "justification": ""
}}

Candidate CV:

{cv_text}

Job Description:

{job_text}
"""

    try:

        response = client.chat.completions.create(

            model="llama-3.1-8b-instant",

            temperature=0.2,

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

        return json.loads(
            response.choices[0].message.content
        )

    except Exception as e:

        print("Recommendation Error:", e)

        return {
            "missing_skills": [],
            "redundant_content": [],
            "improvement_suggestions": [],
            "overall_fit_score": 0,
            "justification": "Recommendation could not be generated."
        }