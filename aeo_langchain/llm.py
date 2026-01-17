from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


def get_llm(provider="openai"):
    if provider == "gemini":
        return ChatGoogleGenerativeAI(
            model="models/gemini-pro-latest",
            temperature=0.2,
        )

    if provider == "openai-4.1-nano":
        return ChatOpenAI(
            model="gpt-4.1-nano",
            temperature=0.2,
        )

    if provider == "openai-3.5-16k":
        return ChatOpenAI(
            model="gpt-3.5-turbo-16k",
            temperature=0.2,
        )

    # default fallback
    return ChatOpenAI(
        model="gpt-4.1-nano",
        temperature=0.2,
    )
