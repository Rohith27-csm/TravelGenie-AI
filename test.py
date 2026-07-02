import os
from dotenv import load_dotenv
from google import genai

# Load the API key from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("API Key Found:", "Yes" if api_key else "No")

if not api_key:
    print("❌ No API key found in .env")
    exit()

try:
    # Create Gemini client
    client = genai.Client(api_key=api_key)

    # Test the API
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Say Hello!"
    )

    print("\n✅ API is working!")
    print("Response:")
    print(response.text)

except Exception as e:
    print("\n❌ Error:")
    print(e)