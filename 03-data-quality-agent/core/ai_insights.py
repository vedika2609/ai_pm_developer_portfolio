# core/ai_insights.py

import json
from openai import OpenAI

import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_ai_insights(findings: dict) -> dict:
    """
    Generate structured AI insights from data quality findings
    """

    prompt = f"""
You are an expert data quality analyst.

Given the following findings from a dataset:

{json.dumps(findings, indent=2)}

Your task:

1. Identify the most critical issues
2. Explain why they matter
3. Suggest actionable fixes

Return output in JSON format:

{{
  "summary": "...",
  "issues": [
    {{
      "column": "...",
      "problem": "...",
      "impact": "...",
      "recommendation": "..."
    }}
  ],
  "overall_assessment": "..."
}}

Be concise and practical.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a senior data platform engineer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except:
        return {
            "summary": content,
            "issues": [],
            "overall_assessment": "Parsing failed, raw output returned."
        }