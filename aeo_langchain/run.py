import json
from aeo_pipeline import run_aeo_pipeline
import os

if __name__ == "__main__":
    url = "https://web-scraping.dev/"  # change to any URL you want

    print("GOOGLE_API_KEY exists:", bool(os.getenv("GOOGLE_API_KEY")))

    result = run_aeo_pipeline(
        url=url,
        llm_provider="openai-4.1-nano"  # use "gemini" if configured or "openai-4.1-nano"
    )

    print(json.dumps(result, indent=2, ensure_ascii=False))
