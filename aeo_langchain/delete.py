import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

print("\n=== AVAILABLE MODELS ===\n")

for m in client.models.list():
    print("MODEL:", m.name)

    # Heuristic capability detection
    if "embedding" in m.name:
        print("  Type: Embedding-only (embedContent)")
    elif "gemini" in m.name or "bison" in m.name:
        print("  Type: Text generation (generateContent)")
    else:
        print("  Type: Unknown / internal")

    print()
