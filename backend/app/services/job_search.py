import os
import requests

from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth


load_dotenv()


API_KEY = os.getenv(
    "CAREERJET_API_KEY"
)


if not API_KEY:
    raise ValueError(
        "CAREERJET_API_KEY not found"
    )


URL = "https://search.api.careerjet.net/v4/query"



# IP CACHE
USER_IP = None



def get_user_ip():

    global USER_IP


    if USER_IP:
        return USER_IP


    try:

        USER_IP = requests.get(
            "https://api.ipify.org",
            timeout=3
        ).text


    except:

        USER_IP="127.0.0.1"



    return USER_IP




def search_jobs(
    keyword:str,
    location:str="Turkey"
):


    user_ip=get_user_ip()



    params={

        "keywords":keyword,

        "location":location,

        "locale_code":"tr_TR",

        "page":1,

        "page_size":5,

        "user_ip":user_ip,

        "user_agent":
        "Mozilla/5.0"

    }



    print(
        "SEARCHING:",
        keyword,
        location
    )



    try:


        response=requests.get(

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


            timeout=10

        )



        response.raise_for_status()



        data=response.json()



        print(
            "FOUND JOBS:",
            len(
                data.get(
                    "jobs",
                    []
                )
            )
        )



        return data



    except Exception as e:


        print(
            "CAREERJET ERROR:",
            e
        )


        return {
            "jobs":[]
        }