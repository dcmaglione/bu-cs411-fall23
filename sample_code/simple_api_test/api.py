import os
import requests
from dotenv import load_dotenv

load_dotenv()

NASA_API_KEY = os.getenv("NASA_API_KEY") # Remember .env file!

def get_apod(date, api_key):
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "date": date,
        "api_key": api_key
    }
    response = requests.get(url=url, params=params)
    return response.json()

apod = get_apod("2020-10-10", NASA_API_KEY)
print(apod["hdurl"])
