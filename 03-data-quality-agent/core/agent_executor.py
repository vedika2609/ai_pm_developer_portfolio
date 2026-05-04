from core.anomaly_detection import detect_anomalies
from core.profiling import profile_dataframe
from core.schema import validate_schema
from core.ai_insights import generate_ai_insights

class DataQualityAgent:

    def __init__(self, expected_schema=None):
        self.expected_schema = expected_schema

    def run(self, df):
        """
        Main execution pipeline
        """

        # Step 1: Profiling
        print("Running profiling...")
        profile = profile_dataframe(df)

        # Step 2: Anomaly Detection
        print("Detecting anomalies...")
        anomalies = detect_anomalies(df, profile)

        # Step 3: Schema Validation (optional)
        print("Validating schema...")
        schema_issues = []
        if self.expected_schema:
            schema_issues = validate_schema(df, self.expected_schema)

        # Step 4: Combine findings
        findings = {
            "profile": profile,
            "anomalies": anomalies,
            "schema_issues": schema_issues
        }

        # Step 5: AI Insights
        print("Generating AI insights...")
        ai_output = generate_ai_insights(findings)

        return {
            "findings": findings,
            "ai_insights": ai_output
        }