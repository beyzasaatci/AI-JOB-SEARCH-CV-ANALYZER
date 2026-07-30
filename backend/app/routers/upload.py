from fastapi import APIRouter, UploadFile, File, HTTPException, Form
import uuid
from app.data.cv_store import save_cv
from app.data.job_store import save_jobs
from app.services.s3_service import (
    upload_cv_to_s3,
    generate_presigned_url
)
from app.services.extractor import (
    extract_pdf_text,
    extract_docx_text
)
from app.services.s3_service import (
    upload_cv_to_s3,
    generate_presigned_url
)
from app.services.parser import parse_cv
from app.services.contact import extract_contacts

from app.data.skills import normalize_skill
from app.models.candidate import CandidateProfile

from app.services.job_keyword import generate_job_keywords
from app.services.job_search import search_jobs
from app.services.job_normalizer import normalize_jobs

from app.matching.matcher import match_jobs


router = APIRouter()


@router.post("/upload-cv")
async def upload_cv(
    file: UploadFile = File(...),
    location: str = Form("Turkey")
):


    allowed_extensions = [
        ".pdf",
        ".docx"
    ]


    if not any(
        file.filename.lower().endswith(ext)
        for ext in allowed_extensions
    ):

        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are allowed."
        )



    content = await file.read()



    if len(content) > 5 * 1024 * 1024:

        raise HTTPException(
            status_code=400,
            detail="Maximum file size is 5 MB."
        )



    if len(content) == 0:

        raise HTTPException(
            status_code=400,
            detail="Uploaded file is empty."
        )



    


    s3_key = upload_cv_to_s3(
        content,
        file.filename
)
    download_url = generate_presigned_url(
        s3_key
    )
    print("====================")
    print("S3 UPLOADED")
    print(s3_key)
    print("====================")


    try:

        if file.filename.lower().endswith(".pdf"):

            text = extract_pdf_text(
                file.file
            )

        else:

            text = extract_docx_text(
                file.file
            )


    except Exception:

        raise HTTPException(
            status_code=400,
            detail="The uploaded file is corrupted or cannot be processed."
        )



    # =========================
    # CONTACT EXTRACTION
    # =========================

    contacts = extract_contacts(
        text
    )



    # =========================
    # CV PARSING
    # =========================

    profile = parse_cv(
        text
    )


    profile.update(
        contacts
    )



    # =========================
    # SKILL NORMALIZATION
    # =========================

    profile["skills"] = [

        normalize_skill(skill)

        for skill in profile.get(
            "skills",
            []
        )

    ]


    profile["skills"] = list(
        dict.fromkeys(
            profile["skills"]
        )
    )



    # =========================
    # PYDANTIC VALIDATION
    # =========================

    candidate = CandidateProfile(
        **profile
    )



    candidate_text = text

    candidate_skills = profile["skills"]



    # =========================
    # JOB KEYWORD GENERATION
    # =========================

    job_keywords = generate_job_keywords(
        candidate_skills
    )


    print("===================")
    print("JOB KEYWORDS")
    print(job_keywords)
    print("===================")



    # =========================
    # JOB SEARCH
    # =========================

    all_jobs = []


    for keyword in job_keywords:


        print(
            "SEARCHING:",
            keyword
        )


        raw_jobs = search_jobs(
            keyword,
            location
        )


        normalized_jobs = normalize_jobs(
            raw_jobs
        )


        all_jobs.extend(
            normalized_jobs
        )



    # duplicate temizleme

    unique_jobs = []

    seen_urls = set()


    for job in all_jobs:


        if job.posting_url not in seen_urls:


            unique_jobs.append(
                job
            )


            seen_urls.add(
                job.posting_url
            )



    jobs = unique_jobs



    print("===================")
    print(
        "TOTAL JOBS:",
        len(jobs)
    )
    print("===================")



    # =========================
    # MATCHING
    # =========================

    matches = match_jobs(
        candidate_text,
        jobs,
        candidate_skills
    )



    # =========================
    # SAVE JOBS FOR RECOMMENDATION
    # =========================

    save_jobs(
        jobs
    )


    print("===================")
    print(
        "SAVED JOBS:",
        len(jobs)
    )
    print("===================")



    file_id = str(
        uuid.uuid4()
    )
    save_cv(
        file_id,
        text
    )


    ocr_required = (
        len(text.strip()) == 0
    )



    return {


        "status": "success",


        "file_id": file_id,
        "s3_key": s3_key,
        "download_url": download_url,

        "filename": file.filename,


        "file_size": len(content),


        "text_length": len(text),


        "ocr_required": ocr_required,


        "job_keywords": job_keywords,


        "candidate": candidate.model_dump(),


        "job_count": len(jobs),


        "matches": matches

    }