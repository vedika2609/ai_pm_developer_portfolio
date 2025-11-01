import streamlit as st
from pandas import DataFrame
import src.data_preprocessing as dp
import src.llm_integration as llm

st.title("💹 FinSummarizer – AI-Powered Financial Report Summarizer")

uploaded_file = st.file_uploader("Upload your financial data CSV file", type=["csv"])

if uploaded_file:
    df: DataFrame = dp.convert_csv_to_df(uploaded_file)
    st.dataframe(df.head())

    # Initialize session state
    if "clicked" not in st.session_state:
        st.session_state["clicked"] = False

    # Button click handler
    if st.button("Generate Summary", on_click=lambda: st.session_state.update(clicked=True)) or st.session_state["clicked"]:
        st.subheader("📊 Summary Output")
        summary_placeholder = st.empty()
        full_summary = ""

        with st.spinner("Generating summary... please wait ⏳"):
            for token in llm.stream_financial_summary(df):
                full_summary += token
                summary_placeholder.markdown(full_summary)

        st.success("✅ Summary generation complete!")

        if full_summary:
            st.download_button(
                label="⬇️ Download Summary",
                data=full_summary,
                file_name="financial_summary.txt",
                mime="text/plain"
            )