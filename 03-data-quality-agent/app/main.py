import sys
import os

# Fix import path for Streamlit
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
from core.agent_executor import DataQualityAgent

# -----------------------------
# 🔹 Page Config
# -----------------------------
st.set_page_config(
    page_title="AI Data Quality Copilot",
    layout="wide"
)

st.title("🧠 AI Data Quality Copilot")
st.caption("Analyze datasets and get AI-powered data quality insights")

# -----------------------------
# 🔹 File Upload
# -----------------------------
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.success("Dataset uploaded successfully")

    # -----------------------------
    # 🔹 Dataset Overview
    # -----------------------------
    col1, col2, col3 = st.columns(3)
    col1.metric("Rows", len(df))
    col2.metric("Columns", len(df.columns))
    col3.metric("Missing Values", int(df.isna().sum().sum()))

    # -----------------------------
    # 🔹 Run Agent with Loader
    # -----------------------------
    progress = st.progress(0)

    with st.spinner("🧠 Analyzing dataset..."):
        progress.progress(20, "Profiling data...")
        agent = DataQualityAgent()

        result = agent.run(df)

        progress.progress(100, "Analysis complete")

    progress.empty()

    ai = result.get("ai_insights", {})
    findings = result.get("findings", {})

    # -----------------------------
    # 🔹 Summary
    # -----------------------------
    st.markdown("## 🔍 Summary")

    summary = ai.get("summary", "No summary available")
    st.success(summary)

    # -----------------------------
    # 🔹 Issues Section
    # -----------------------------
    st.markdown("## ⚠️ Detected Issues")

    issues = ai.get("issues", [])

    if not issues:
        st.success("No major issues detected 🎉")

    else:
        for issue in issues:
            with st.container():
                col1, col2 = st.columns([1, 3])

                with col1:
                    st.markdown(f"### `{issue.get('column', 'Unknown')}`")

                with col2:
                    st.error(issue.get("problem", "Unknown issue"))
                    st.write(f"**Impact:** {issue.get('impact', '-')}")
                    st.write(f"**Recommendation:** {issue.get('recommendation', '-')}")

                st.divider()

    # -----------------------------
    # 🔹 Overall Assessment
    # -----------------------------
    st.markdown("## 📊 Overall Assessment")

    assessment = ai.get("overall_assessment", "No assessment available")
    st.info(assessment)

    # -----------------------------
    # 🔹 Parsing Failure Fallback
    # -----------------------------
    if not issues and "Parsing failed" in summary:
        st.warning("⚠️ AI response could not be parsed properly. Showing raw output below.")

        with st.expander("View Raw AI Output"):
            st.write(assessment)

    # -----------------------------
    # 🔹 Raw Findings (Debug View)
    # -----------------------------
    with st.expander("🔬 View Raw Findings"):
        st.json(findings)