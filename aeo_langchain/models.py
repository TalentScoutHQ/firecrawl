from pydantic import BaseModel
from typing import List


class TopicOutput(BaseModel):
    topics: List[str]


class KeywordOutput(BaseModel):
    meta_keywords: List[str]


class FAQItem(BaseModel):
    name: str
    acceptedAnswer: dict


class FAQOutput(BaseModel):
    mainEntity: List[FAQItem]
