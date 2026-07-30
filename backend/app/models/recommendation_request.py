from pydantic import BaseModel


class RecommendationRequest(BaseModel):
    file_id: str