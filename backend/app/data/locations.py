# ponytail: sadece Adzuna'nin destekledigi ulkeler. Turkey/Sweden/Japan Adzuna'da yok
# (/jobs/tr/ -> 404), Careerjet ise AWS IP'lerinden 403 verdigi icin kullanilamiyor.
locations = {
  "Germany": [
    "Berlin",
    "Munich",
    "Hamburg",
    "Frankfurt",
    "Cologne",
    "Stuttgart",
    "Dusseldorf",
    "Dortmund",
    "Leipzig",
    "Bremen"
  ],


  "United States": [
    "New York",
    "San Francisco",
    "Seattle",
    "Boston",
    "Austin",
    "Chicago",
    "Los Angeles",
    "Washington DC",
    "Denver",
    "Atlanta"
  ],


  "United Kingdom": [
    "London",
    "Manchester",
    "Birmingham",
    "Liverpool",
    "Edinburgh",
    "Leeds",
    "Bristol",
    "Cambridge",
    "Oxford"
  ],


  "Netherlands": [
    "Amsterdam",
    "Rotterdam",
    "Utrecht",
    "Eindhoven",
    "The Hague",
    "Groningen"
  ],


  "France": [
    "Paris",
    "Lyon",
    "Marseille",
    "Toulouse",
    "Nice",
    "Bordeaux"
  ],


  "Canada": [
    "Toronto",
    "Vancouver",
    "Montreal",
    "Ottawa",
    "Calgary"
  ],


  "Spain": [
    "Madrid",
    "Barcelona",
    "Valencia",
    "Seville",
    "Bilbao"
  ],


  "Italy": [
    "Rome",
    "Milan",
    "Turin",
    "Florence",
    "Bologna"
  ],


  "Poland": [
    "Warsaw",
    "Krakow",
    "Wroclaw",
    "Poznan"
  ],


  "Australia": [
    "Sydney",
    "Melbourne",
    "Brisbane",
    "Perth"
  ]
}


# Adzuna ulke kodlari (api.adzuna.com/v1/api/jobs/<kod>/search)
COUNTRY_CODES = {
  "Germany": "de",
  "United States": "us",
  "United Kingdom": "gb",
  "Netherlands": "nl",
  "France": "fr",
  "Canada": "ca",
  "Spain": "es",
  "Italy": "it",
  "Poland": "pl",
  "Australia": "au",
}

# ponytail: iki dict elle senkron tutuluyor; import'ta patlasin ki sessizce kaymasin
assert locations.keys() == COUNTRY_CODES.keys(), (
    "locations ve COUNTRY_CODES ayni ulkeleri icermeli"
)