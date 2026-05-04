import streamlit as st
import pandas as pd

from agent.agent_executor import DataQualityAgent

st.title("AI Data Quality Agent")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    agent = DataQualityAgent()

    result = agent.run(df)

    st.subheader("AI Insights")
    st.json(result["ai_insights"])

    st.subheader("Findings")
    st.json(result["findings"])