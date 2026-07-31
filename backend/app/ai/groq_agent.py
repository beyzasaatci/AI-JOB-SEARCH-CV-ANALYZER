import json
import os

from dotenv import load_dotenv
from groq import Groq
import json
import os
import time

from dotenv import load_dotenv
from groq import Groq
from groq import RateLimitError
from groq import APIConnectionError
from groq import APITimeoutError

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def analyze_cv(cv_text: str, job_text: str):
    prompt = f"""
You are an expert recruiter.

Analyze the candidate CV against the job description deeply.
You can evaluate candidates from ANY profession.


Examples:

- Software Engineering
- Data Science
- Finance
- Accounting
- Healthcare
- Marketing
- Design
- Sales
- Human Resources
- Education
- Manufacturing

Always evaluate the CV according to the job description.
Return ONLY JSON.
No markdown.
No explanation outside JSON.

The JSON must follow exactly this structure:

{{
    "strengths": [],

    "matched_skills": [],

    "missing_skills": [],

    "skill_gap": {{

    }},

    "cv_vs_job": {{
        "matched": [],
        "missing": [],
        "partial_match": []
    }},

    "redundant_content": [],

    "improvement_suggestions": [],

    "interview_topics": [],

    "cv_improvements": [],

    "overall_fit_score": 0,

    "justification": ""
}}


Analysis rules:


strengths:
- Candidate's strongest technical abilities.
- Mention programming languages, frameworks, databases, cloud tools, projects.
- Only include real strengths from CV.


matched_skills:
- Technologies and skills appearing in both CV and job description.


missing_skills:
- Important requirements from job description that are missing in CV.


skill_gap:
- Create a dictionary.
- Key = missing skill.
- Value = percentage readiness gap between 0-100.

Example:

{{
"Docker":40,
"AWS":70,
"Kubernetes":90
}}


cv_vs_job:

matched:
- Skills where candidate fits the job.

missing:
- Requirements candidate does not have.

partial_match:
- Skills where candidate has similar experience but not exactly.


redundant_content:
- CV parts that are unnecessary for this job.
- Suggest removing unnecessary details.


improvement_suggestions:
- Give practical career improvement advice.
- Mention courses, projects, technologies.


interview_topics:
- Topics candidate should prepare before interview.


cv_improvements:
- Specific CV editing suggestions.


overall_fit_score:
- Integer between 0 and 100.
- Calculate based on:
  - Technical skills
  - Projects
  - Experience
  - Job requirements match


justification:
- Explain why this score was given.
- Mention strengths and weaknesses.

IMPORTANT:
- Write the recommendation in the same language as the CV.
- If CV is English, answer in English.
- If CV is Turkish, answer in Turkish.
- Do not translate names of companies, technologies, certificates or job titles.

Analyze:

1. Candidate background
2. Job compatibility
3. Strengths
4. Missing skills
5. Career advice


Return a professional recommendation.
Candidate CV:

{cv_text}


Job Description:

{job_text}

"""

    max_retries = 3

    for attempt in range(max_retries):

        try:

            response = client.chat.completions.create(

                model="llama-3.3-70b-versatile",

                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],

                response_format={
                    "type": "json_object"
                },

                temperature=0.2
            )

            content = response.choices[0].message.content

            return json.loads(content)

        except (
            RateLimitError,
            APIConnectionError,
            APITimeoutError
        ):

 
            if attempt == max_retries - 1:
                raise

            time.sleep(2 ** attempt)

        except Exception as e:
            raise RuntimeError(
                f"Groq API Error: {e}"
            )