KEYWORDS_PROMPT = """
You are an AEO keyword engine.

From the markdown below, extract 8-15 meta keywords or short phrases representing:
- product capabilities
- domain terminology
- problem-solution concepts

Rules:
- Do NOT include URLs, UI labels, or images
- Do NOT repeat words
- These are AI-discovery keywords, not SEO spam

Markdown:
{markdown}

{format_instructions}
"""
