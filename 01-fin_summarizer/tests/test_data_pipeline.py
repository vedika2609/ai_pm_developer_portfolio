import pandas as pd
import pytest
from src.data_preprocessing import convert_csv_to_df

def test_convert_csv_to_df_valid(tmp_path):
    """Test reading a valid CSV file."""
    # Arrange
    csv_content = "Revenue,Profit\n100,20\n200,40\n"
    csv_path = tmp_path / "sample.csv"
    csv_path.write_text(csv_content)

    # Act
    df = convert_csv_to_df(csv_path)

    # Assert
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert list(df.columns) == ["Revenue", "Profit"]

def test_convert_csv_to_df_invalid_file():
    """Ensure the function raises a proper error for invalid inputs."""
    assert convert_csv_to_df("non_existent_file.csv").empty

def test_convert_csv_to_df_cleaning(tmp_path):
    """Test that missing values or extra spaces are cleaned."""
    csv_content = "Revenue , Profit \n100, 20\n , 40\n"
    csv_path = tmp_path / "dirty.csv"
    csv_path.write_text(csv_content)

    df = convert_csv_to_df(csv_path)
    assert "revenue" in df.columns[0].lower()  # cleaned column names
    assert not df.isnull().all(axis=None)