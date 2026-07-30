import requests
from bs4 import BeautifulSoup

url = "https://jobviewtrack.com/v2/UzZCoBqFuU8FB5t69hnw1wDFKvHoWqtVJhBqWIETFnYZ-NA60u6s6IEbnBwz4hVa1mU4s6msMUOTnWkfCjBPV7rdhxj8vjMHGoN0nfMAoMAPbEZ70fIiXzKPDhyqridjpDFI4A6C0eNH3RfQt8a2gKmQ1N9aXV-famA4kGZn8MCZgokYJae98wnTjLjxtO3GU8uejH40aMeKoVL3oJTqGSt01LjRfMHzkOv7XiGEuKQ"

response = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    allow_redirects=True,
    timeout=30
)

print("STATUS:", response.status_code)
print("FINAL URL:", response.url)

soup = BeautifulSoup(response.text, "html.parser")

text = soup.get_text(" ", strip=True)

print(text[:5000])