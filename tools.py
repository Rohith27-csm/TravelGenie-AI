import os
import time
from dotenv import load_dotenv
from google import genai
from prompts import SYSTEM_PROMPT

# ---------------- Load Environment ----------------
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("API Key Loaded:", "Yes" if api_key else "No")

if api_key:
    print("Key starts with:", api_key[:8] + "...")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found. Please add it to your .env file or Streamlit Secrets."
    )

# ---------------- Gemini Client ----------------
client = genai.Client(api_key=api_key)


def generate_trip(destination, days, budget, interests):

    prompt = f"""
{SYSTEM_PROMPT}

Destination: {destination}
Days: {days}
Budget: {budget}
Interests: {interests}
"""

    retries = 3

    for attempt in range(retries):

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            if response and response.text:
                return response.text

            return "⚠️ Gemini returned an empty response."

        except Exception as e:

            error = str(e)

            print(f"Attempt {attempt + 1} failed:")
            print(error)

            # Retry temporary errors
            if (
                "503" in error
                or "SERVICE_UNAVAILABLE" in error
                or "timeout" in error.lower()
            ):
                if attempt < retries - 1:
                    time.sleep(3)
                    continue

            # Quota exceeded
            if "429" in error or "RESOURCE_EXHAUSTED" in error:
                return """
# ⚠️ Gemini API Quota Reached

The Gemini API project has reached its current usage limit.

Please wait for the quota to reset or use another API key/project.

Your application is working correctly.
"""

            # Invalid API Key
            if "401" in error or "UNAUTHENTICATED" in error:
                return """
# ❌ Invalid Gemini API Key

Please verify:

• API key is correct
• API key is active
• Streamlit Secrets / .env contains the latest key
"""

            return f"""
# ❌ Gemini API Error

{error}
"""