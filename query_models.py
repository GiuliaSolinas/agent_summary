#Simple script to test the API and query a model using the Google GenAI API

import os
from dotenv import load_dotenv
load_dotenv()

# Access the API key from the environment variable
api_key = os.getenv("GOOGLE_API_KEY")

# This script demonstrates how to query a model using the Google GenAI API.
from google import genai

client = genai.Client(api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)