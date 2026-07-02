import os
import time
from dotenv import load_dotenv
from google import genai
from prompts import SYSTEM_PROMPT

# Load environment variables
load_dotenv()

# Get Gemini API Key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found. Please set it in your .env file or Streamlit Secrets."
    )

# Create Gemini client
client = genai.Client(api_key=api_key)


def generate_trip(destination, days, budget, interests):
    prompt = f"""
{SYSTEM_PROMPT}

Destination: {destination}
Days: {days}
Budget: {budget}
Interests: {interests}
"""

    max_retries = 3

    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )

            if response and response.text:
                return response.text

            return "⚠️ No response received from Gemini."

        except Exception as e:

            # Retry for temporary errors
            if attempt < max_retries - 1:
                time.sleep(3)
                continue

            # Show actual error after all retries fail
            return f"""
❌ Gemini API Error

{str(e)}

Possible reasons:
• API key is invalid
• API quota exceeded
• Gemini service is temporarily unavailable
• Network issue

Please try again later.
"""