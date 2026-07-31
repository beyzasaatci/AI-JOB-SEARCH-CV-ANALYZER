import json
import os

from dotenv import load_dotenv
from groq import Groq


load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)



def generate_job_keywords(profile):


    prompt = f"""

You are a strict professional job recommendation system.

Your task:
Generate job search keywords ONLY based on the candidate's MAIN PROFESSION.

IMPORTANT RULES:

1. First identify:
- Main profession
- Industry
- Career field
- Seniority

2. Job keywords MUST stay in the same professional field.

3. Never recommend another profession because of transferable skills.

Examples:


LAW PROFILE:

Allowed:

Lawyer
Legal Counsel
Corporate Lawyer
Compliance Specialist
Contract Specialist
Legal Consultant


Forbidden:

Project Manager
Operations Manager
Business Analyst
Accounting Clerk
Restaurant Manager
Night Manager


SOFTWARE PROFILE:

Allowed:

Software Engineer
Backend Developer
Frontend Developer
DevOps Engineer
Cloud Engineer


Forbidden:

HR Specialist
Sales Manager
Accountant


BUSINESS PROFILE:

Allowed:

Business Analyst
Project Manager
Operations Analyst
Consultant


Forbidden:

Lawyer
Doctor
Engineer


FINANCE PROFILE:

Allowed:

Financial Analyst
Accountant
Auditor
Finance Specialist


Forbidden:

Software Engineer
Lawyer


Generate maximum 5 keywords.

If uncertain, prefer fewer keywords.

Return ONLY JSON:

{{
    "keywords":[]
}}


Candidate Profile:

{json.dumps(profile, ensure_ascii=False)}

"""


    try:

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


        result = json.loads(
            response.choices[0].message.content
        )


        keywords = result.get(
            "keywords",
            []
        )


        return keywords[:5]


    except Exception as e:

        print(
            "KEYWORD ERROR:",
            e
        )

        return []