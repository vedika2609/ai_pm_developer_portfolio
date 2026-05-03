# tools/profiling.py

import pandas as pd

def profile_dataframe(df: pd.DataFrame) -> dict:
    profile = {"columns": {}}

    for col in df.columns:
        column_data = df[col]

        profile["columns"][col] = {
            "dtype": str(column_data.dtype),
            "missing": int(column_data.isna().sum()),
            "unique": int(column_data.nunique())
        }

        if pd.api.types.is_numeric_dtype(column_data):
            profile["columns"][col].update({
                "mean": float(column_data.mean()),
                "std": float(column_data.std()),
                "min": float(column_data.min()),
                "max": float(column_data.max())
            })

        elif pd.api.types.is_string_dtype(column_data):
            profile["columns"][col].update({
                "sample_values": column_data.dropna().unique()[:5].tolist()
            })

    return profile