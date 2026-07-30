from app.ai.groq_agent import analyze_cv
from app.models.recommendation import Recommendation
import json

cv = """
Python
FastAPI
Docker
AWS
PostgreSQL
"""


job = """
Backend Developer

Requirements

Python
FastAPI
Docker
Redis
RabbitMQ
AWS
"""


result = analyze_cv(
    cv,
    job
)

recommendation = Recommendation.model_validate(result)



print(
    json.dumps(
        recommendation.model_dump(),
        indent=4,
        ensure_ascii=False
    )
)