import io
import pandas as pd
import pytest
from unittest.mock import patch
import asyncio


import src.data_preprocessing as dp
import src.llm_integration as llm

# --------------------------------------------------------------------
# 1️⃣ Helper: fake CSV upload simulation
# --------------------------------------------------------------------
@pytest.fixture
def sample_csv_bytes():
    csv_str = "Revenue,Profit\n100,20\n200,50\n300,80\n"
    return io.BytesIO(csv_str.encode("utf-8"))

# --------------------------------------------------------------------
# 2️⃣ Test: Full pipeline integration (mocked LLM)
# --------------------------------------------------------------------
@patch("src.llm_integration.stream_financial_summary")
def test_full_pipeline_integration(mock_stream, sample_csv_bytes):
    """Simulate the end-to-end FinSummarizer flow."""
    # Arrange
    df = dp.convert_csv_to_df(sample_csv_bytes)

    # Simulate the streaming generator output
    mock_stream.return_value = iter([
        "Revenue is increasing. ",
        "Profit margins remain stable."
    ])

    # Act
    output_text = "".join(list(mock_stream.return_value))

    # Assert
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert "Revenue" in df.columns
    assert "Revenue" in output_text
    assert "Profit" in output_text


# --------------------------------------------------------------------
# 3️⃣ Test: Stream summarization generator
# --------------------------------------------------------------------
@patch("src.llm_integration.stream_financial_summary")
def test_stream_pipeline(mock_stream, sample_csv_bytes):
    """Verify the streaming generator works token by token."""
    df = dp.convert_csv_to_df(sample_csv_bytes)

    # Mock the stream_financial_summary generator output
    mock_stream.return_value = iter([
        "Revenue is increasing. ",
        "Profit margins remain stable."
    ])

    # Act
    tokens = list(mock_stream.return_value)
    output_text = "".join(tokens)

    # Assert
    assert "Revenue" in output_text
    assert "Profit" in output_text
