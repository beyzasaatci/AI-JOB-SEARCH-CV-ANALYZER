from pydantic import BaseModel, Field
from typing import List, Dict


class CVvsJob(BaseModel):

    matched: List[str] = []

    missing: List[str] = []

    partial_match: List[str] = []



class Recommendation(BaseModel):

    # Güçlü taraflar
    strengths: List[str] = []


    # Skill eşleşmeleri
    matched_skills: List[str] = []


    # Eksikler
    missing_skills: List[str] = []


    # Skill açığı yüzdesi
    skill_gap: Dict[str, int] = {}



    # CV - Job karşılaştırması
    cv_vs_job: CVvsJob = Field(
        default_factory=CVvsJob
    )



    # Gereksiz içerikler
    redundant_content: List[str] = []



    # Geliştirme önerileri
    improvement_suggestions: List[str] = []



    # Mülakat hazırlığı
    interview_topics: List[str] = []



    # CV düzenleme önerileri
    cv_improvements: List[str] = []



    # Genel skor
    overall_fit_score: int = 0



    # Açıklama
    justification: str = ""