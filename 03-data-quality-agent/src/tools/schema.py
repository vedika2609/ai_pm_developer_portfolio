# core/schema.py

def validate_schema(df, expected_schema: dict) -> list:
    issues = []

    # Check missing columns
    for col in expected_schema:
        if col not in df.columns:
            issues.append({
                "column": col,
                "issue": "Missing column"
            })

    # Check data types
    for col, expected_type in expected_schema.items():
        if col in df.columns:
            actual_type = str(df[col].dtype)

            if expected_type not in actual_type:
                issues.append({
                    "column": col,
                    "issue": f"Type mismatch (expected {expected_type}, got {actual_type})"
                })

    return issues