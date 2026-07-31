import json
import os

from dotenv import load_dotenv
from groq import Groq


load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def extract_cv_profile(cv_text: str):

    prompt = f"""

You are an expert career advisor.

Analyze this CV.

Return ONLY JSON.

Do not assume the person is only a software developer.

Identify:
- career category
- professional skills
- tools
- technologies
- industries
- experience areas


Format:

{{
    "category": "",
    "skills": [],
    "experience_areas": []
}}


CV:

{cv_text}

"""


    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        temperature=0,

        response_format={
            "type":"json_object"
        },

        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )


    return json.loads(
        response.choices[0].message.content
    )