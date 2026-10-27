import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

print("Key Found:", bool(os.getenv("GOOGLE_API_KEY")))

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

response = client.models.generate_content(
    model="gemini-flash-latest",
    contents="Say Hello"
)

print(response.text)