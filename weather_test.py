import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("WEATHER_API_KEY")

print("API Key:", api_key)

url = f"https://api.openweathermap.org/data/2.5/weather?q=Goa&appid={api_key}&units=metric"

response = requests.get(url)

print("Status Code:", response.status_code)
print("Response:")
print(response.text)