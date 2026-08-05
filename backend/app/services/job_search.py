import os

import requests
from dotenv import load_dotenv

from app.data.locations import COUNTRY_CODES


load_dotenv()


APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")


if not APP_ID or not APP_KEY:
    raise ValueError("ADZUNA_APP_ID / ADZUNA_APP_KEY not found")


URL = "https://api.adzuna.com/v1/api/jobs/{country}/search/1"

PAGE_SIZE = 5


def split_location(location):
    """'United States New York' -> ('us', 'New York'). Bilinmeyen ulke -> (None, ...)."""

    for name, code in COUNTRY_CODES.items():

        if location == name:
            return code, ""

        if location.startswith(name + " "):
            return code, location[len(name) + 1:]

    return None, location


def search_jobs(keyword: str, location: str = "Germany"):

    country, city = split_location(location)

    if not country:
        print("UNSUPPORTED LOCATION:", location)
        return {"jobs": []}

    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "what": keyword,
        "results_per_page": PAGE_SIZE,
        "content-type": "application/json",
    }

    if city:
        params["where"] = city

    print("SEARCHING:", keyword, "|", country, city)

    try:

        response = requests.get(
            URL.format(country=country),
            params=params,
            timeout=10,
        )

        response.raise_for_status()

        results = response.json().get("results", [])

        print("FOUND JOBS:", len(results))

        # normalize_jobs'in bekledigi anahtarlara cevir
        return {
            "jobs": [
                {
                    "title": item.get("title", ""),
                    "company": item.get("company", {}).get("display_name", ""),
                    "locations": item.get("location", {}).get("display_name", ""),
                    "description": item.get("description", ""),
                    "url": item.get("redirect_url", ""),
                }
                for item in results
            ]
        }

    except Exception as e:

        print("ADZUNA ERROR:", e)

        return {"jobs": []}


if __name__ == "__main__":
    # ponytail: tek kontrol - cok kelimeli ulke adi dogru ayrisiyor mu
    assert split_location("United States New York") == ("us", "New York")
    assert split_location("Germany Berlin") == ("de", "Berlin")
    assert split_location("Netherlands The Hague") == ("nl", "The Hague")
    assert split_location("Germany") == ("de", "")
    assert split_location("Turkey Istanbul") == (None, "Turkey Istanbul")
    print("ok")
