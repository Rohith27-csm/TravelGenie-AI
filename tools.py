import os
import time
from dotenv import load_dotenv
from google import genai
from prompts import SYSTEM_PROMPT

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_trip(destination, days, budget, interests):

    prompt = f"""
{SYSTEM_PROMPT}

Destination: {destination}
Days: {days}
Budget: {budget}
Interests: {interests}
"""

    for _ in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt,
            )
            return response.text

        except Exception:
            time.sleep(3)

    return "⚠️ Gemini servers are currently busy. Please try again in a few minutes."