from firecrawl_client import start_crawl, poll_crawl
from llm import get_llm
from models import TopicOutput, KeywordOutput, FAQOutput
from prompts.topics_prompt import TOPICS_PROMPT
from prompts.keywords_prompt import KEYWORDS_PROMPT
from prompts.faq_prompt import FAQ_PROMPT

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser


def run_aeo_pipeline(url: str, llm_provider="openai") -> dict:
    crawl = start_crawl(url)
    pages = poll_crawl(crawl["url"])

    page = next((p for p in pages if p.get("markdown")), None)
    if not page:
        raise RuntimeError("No markdown content found")

    markdown = page["markdown"]

    llm = get_llm(llm_provider)

    # ---------- Topics ----------
    topics_parser = PydanticOutputParser(pydantic_object=TopicOutput)

    topics_prompt = PromptTemplate(
        template=TOPICS_PROMPT,
        input_variables=["markdown"],
        partial_variables={
            "format_instructions": topics_parser.get_format_instructions()
        }
    )

    topics = (topics_prompt | llm | topics_parser).invoke(
        {"markdown": markdown}
    )

    # ---------- Keywords ----------
    keywords_parser = PydanticOutputParser(pydantic_object=KeywordOutput)

    keywords_prompt = PromptTemplate(
        template=KEYWORDS_PROMPT,
        input_variables=["markdown"],
        partial_variables={
            "format_instructions": keywords_parser.get_format_instructions()
        }
    )

    keywords = (keywords_prompt | llm | keywords_parser).invoke(
        {"markdown": markdown}
    )

    # ---------- FAQ ----------
    faq_parser = PydanticOutputParser(pydantic_object=FAQOutput)

    faq_prompt = PromptTemplate(
        template=FAQ_PROMPT,
        input_variables=["markdown"],
        partial_variables={
            "format_instructions": faq_parser.get_format_instructions()
        }
    )

    faq = (faq_prompt | llm | faq_parser).invoke(
        {"markdown": markdown}
    )

    return {
        "source_url": url,
        "topics": topics.topics,
        "meta_keywords": keywords.meta_keywords,
        "faq_schema": {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [item.model_dump() for item in faq.mainEntity]
        },
        "raw_markdown_excerpt": markdown[:1200]
    }
