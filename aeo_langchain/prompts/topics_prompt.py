TOPICS_PROMPT = """
You are an AEO content analyzer.

From the following website markdown, extract 8–15 AEO topics or phrases that represent:
- product concepts
- problem statements
- domain-specific capabilities

Rules:
- No fluff
- No testimonials
- No brand slogans
- Use short phrases
- AI-discovery oriented

Markdown:
{markdown}

{format_instructions}
"""
