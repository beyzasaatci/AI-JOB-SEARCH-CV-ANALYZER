import os
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
from pathlib import Path


load_dotenv(Path(__file__).resolve().parents[2] / ".env")


API_KEY = os.getenv("CAREERJET_API_KEY")

if not API_KEY:
    raise ValueError("CAREERJET_API_KEY not found")


URL = "https://search.api.careerjet.net/v4/query"



def search_jobs(keyword: str, location: str = "Turkey"):


    user_ip = requests.get(
        "https://api.ipify.org",
        timeout=10
    ).text



    search_locations = [
        location
    ]


    # Şehir fallback
    parts = location.split()

    if len(parts) > 1:

        city = parts[-1]

        search_locations.append(city)



    # Türkiye fallback

    search_locations.append(
        "Turkey"
    )



    # duplicate temizle

    search_locations = list(
        dict.fromkeys(search_locations)
    )




    for loc in search_locations:


        print(
            "SEARCHING LOCATION:",
            loc
        )


        params = {

            "keywords": keyword,

            "location": loc,

            "locale_code": "tr_TR",

            "page": 1,

            "page_size": 10,

            "user_ip": user_ip,

            "user_agent": "Mozilla/5.0"

        }



        response = requests.get(

            URL,

            params=params,

            headers={

                "Referer":
                "http://localhost:8000",

                "User-Agent":
                "Mozilla/5.0"

            },

            auth=HTTPBasicAuth(
                API_KEY,
                ""
            ),

            timeout=30

        )



        data = response.json()



        print(
            "FOUND JOBS:",
            len(data.get("jobs", []))
        )



        if data.get("jobs"):

            return data




    return {
        "jobs":[]
    }