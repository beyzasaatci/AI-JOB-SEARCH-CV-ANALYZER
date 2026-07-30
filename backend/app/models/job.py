from pydantic import BaseModel
from typing import Optional, List


class JobPosting(BaseModel):
    title: str
    company: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None
    requirements: List[str] = []
    salary: Optional[str] = None
    posting_url: Optional[str] = None
    source: str