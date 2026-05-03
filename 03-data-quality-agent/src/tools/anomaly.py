# tools/anomaly_detection.py

import numpy as np
import pandas as pd

def detect_anomalies(df: pd.DataFrame, profile: dict) -> list:
    anomalies = []

    for col in df.columns:
        col_data = df[col]
        col_profile = profile["columns"][col]

        # Missing values
        if col_profile["missing"] > 0:
            anomalies.append({
                "column": col,
                "issue": "Missing values detected",
                "count": col_profile["missing"]
            })

        # Numeric checks
        if pd.api.types.is_numeric_dtype(col_data):

            # Negative values
            if (col_data < 0).any():
                anomalies.append({
                    "column": col,
                    "issue": "Negative values detected"
                })

            # Outliers using z-score
            if col_data.std() != 0:
                z_scores = (col_data - col_data.mean()) / col_data.std()
                outliers = np.abs(z_scores) > 3

                if outliers.sum() > 0:
                    anomalies.append({
                        "column": col,
                        "issue": "Outliers detected",
                        "count": int(outliers.sum())
                    })

        # Low cardinality warning
        if col_profile["unique"] < 2:
            anomalies.append({
                "column": col,
                "issue": "Low variability (possible data issue)"
            })

    return anomalies