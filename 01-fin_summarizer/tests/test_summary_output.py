import pytest

@pytest.fixture
def test_summarize_financial_data_mock(monkeypatch):
    import pandas as pd
    from unittest.mock import MagicMock
    from src import llm_integration

    df = pd.DataFrame({"Revenue": [100, 200, 300], "Profit": [20, 50, 80]})

    mock_invoke = MagicMock()
    mock_invoke.return_value.content = (
        "1️⃣ **Summary:** Revenue is increasing.\n"
        "2️⃣ **Trends:** Profit is stable."
    )

    monkeypatch.setattr(llm_integration.llm, "invoke", mock_invoke)

    summary = llm_integration.summarize_df(df)

    assert "Summary" in summary
    assert "Revenue" in summary
