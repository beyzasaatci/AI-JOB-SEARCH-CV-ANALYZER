import re


EMAIL_REGEX = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

PHONE_REGEX = r"(?:\+90|0)?\s?\(?5\d{2}\)?\s?\d{3}\s?\d{2}\s?\d{2}"

LINKEDIN_REGEX = r"https?://(?:www\.)?linkedin\.com/[^\s]+"

GITHUB_REGEX = r"https?://(?:www\.)?github\.com/[^\s]+"


def extract_contacts(text):

    return {
        "email": (
            re.search(EMAIL_REGEX, text).group(0)
            if re.search(EMAIL_REGEX, text)
            else None
        ),

        "phone": (
            re.search(PHONE_REGEX, text).group(0)
            if re.search(PHONE_REGEX, text)
            else None
        ),

        "linkedin": (
            re.search(LINKEDIN_REGEX, text).group(0)
            if re.search(LINKEDIN_REGEX, text)
            else None
        ),

        "github": (
            re.search(GITHUB_REGEX, text).group(0)
            if re.search(GITHUB_REGEX, text)
            else None
        ),
    }