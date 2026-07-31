import json
import os

from dotenv import load_dotenv
from groq import Groq


load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)



def ai_skill_match(cv_text: str, job_text: str):


    prompt = f"""

You are a professional recruiter.

Compare CV and JOB.

First identify:

Candidate profession:
Job profession:


Rules:

- Same career field required.
- Do not match unrelated jobs.
- Lawyer != Manager
- Doctor != Engineer
- Developer != HR

Evaluate:

profession_match 0-100

skill_score 0-100


Return JSON only:

{{
"candidate_profession":"",
"job_profession":"",
"profession_match":0,
"matched_skills":[],
"missing_skills":[],
"skill_score":0,
"reason":""
}}




CV:

{cv_text[:3000]}


JOB:

{job_text[:1500]}

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


        result = json.loads(
            response.choices[0].message.content
        )


        print(
            "AI MATCH RESULT:",
            result
        )


        return result


    except Exception as e:

        print(
            "AI MATCH ERROR:",
            e
        )


        return {
            "matched_skills": [],
            "missing_skills": [],
            "skill_score": 0
        }