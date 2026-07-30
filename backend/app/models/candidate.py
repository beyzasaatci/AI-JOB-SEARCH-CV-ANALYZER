from pydantic import BaseModel
from typing import List, Optional


class WorkExperience(BaseModel):
    company: Optional[str] = None
    position: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    description: Optional[str] = None


class Education(BaseModel):
    school: Optional[str] = None
    degree: Optional[str] = None
    field: Optional[str] = None
    graduation_year: Optional[str] = None


class CandidateProfile(BaseModel):
    name: Optional[str] = None
    title: Optional[str] = None

    email: Optional[str] = None
    phone: Optional[str] = None
    linkedin: Optional[str] = None
    github: Optional[str] = None

    skills: List[str] = []

    years_of_experience: Optional[int] = None

    work_history: List[WorkExperience] = []

    education: List[Education] = []

    certifications: List[str] = []

    languages: List[str] = []