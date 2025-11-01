from unittest.mock import patch
import pandas as pd
from src.llm_integration import summarize_df


@patch("src.llm_integration.summarize_df")
def test_summarize_financial_data_mock(mock_summarize_df):
    """Simulate LLM response to test summarization pipeline."""
    # Arrange
    df = pd.DataFrame({
        "Revenue": [100, 200, 300],
        "Profit": [20, 50, 80]
    })
    mock_summarize_df.return_value = (
        "1️⃣ **Summary:** Revenue is increasing.\n"
        "2️⃣ **Trends:** Profit is stable."
    )

    # Act
    summary = summarize_df(df)

    # Assert
    assert isinstance(summary, str)
    assert "Summary" in summary
    assert "Revenue" in summary
