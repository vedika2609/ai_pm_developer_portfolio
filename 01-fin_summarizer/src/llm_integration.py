import os

import pandas as pd

from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
from src import data_preprocessing as data

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")
if api_key is None:
    print("⚠️ Warning: Anthropic API key not found, skipping LLM initialization.")
    llm = None
else:
    llm = ChatAnthropic(model_name="claude-3-7-sonnet-20250219",
                    temperature=0.1,
                    timeout=None,
                    max_retries=10,
                    verbose=True
                    )

SUMMARY_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "You are an expert Financial Analyst that generates clear, factual summaries of financial datasets."),
    ("user", """Summarize the following dataset into key trends, anomalies, and recommendations.

    Dataset sample:
    {data}

    Please structure your response as:
    1️⃣ **Summary**
    2️⃣ **Trends & Insights**
    3️⃣ **Anomalies or Red Flags**
    4️⃣ **Recommended Next Steps**
    """)
])

def summarize_df(financial_df: pd.DataFrame) -> str:
    """Summarize financial data using Anthropic Claude with structured chat prompt."""
    data_preview = financial_df.head(20).to_string(index=False)
    messages = SUMMARY_PROMPT.format_messages(data=data_preview)

    if llm is None:
        return "⚠️ No LLM available in test mode."

    llm_response = llm.invoke(messages)
    return llm_response.content if isinstance(llm_response.content, str ) else llm_response.content[0].text

def stream_financial_summary(financial_df: pd.DataFrame):
    """Stream summary from LLM"""
    data_preview = financial_df.head(20).to_string(index=False)
    messages = SUMMARY_PROMPT.format_messages(data=data_preview)

    for chunk in llm.stream(messages):
        if chunk.content:
            yield chunk.content

if __name__ == "__main__":
    df = data.convert_csv_to_df('../data/financial_sample_data.csv')
    response = summarize_df(df)
    print(response)
