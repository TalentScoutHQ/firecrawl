FAQ_PROMPT = """
You are generating a basic Schema.org FAQPage.

Based on the content below:
- Create 3–6 FAQs
- Use What / How / Why questions
- Answers must be grounded in the content
- Short, factual, non-marketing

Markdown:
{markdown}

Return JSON:
{{
  "mainEntity": [
    {{
      "name": "Question?",
      "acceptedAnswer": {{
        "text": "Answer"
      }}
    }}
  ]
}}
"""
