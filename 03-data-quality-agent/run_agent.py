# run_agent.py

import pandas as pd
from core.agent_executor import DataQualityAgent

# Load dataset
df = pd.read_csv("data/customer_data_with_issues.csv")

# Optional schema
expected_schema = {
    "age": "int",
    "customer_id": "str",
    "email": "str",
    "signup_date": "date",
    "country": "str",
    "monthly_spend": "float"
}

# Initialize agent
agent = DataQualityAgent(expected_schema=expected_schema)

# Run agent
result = agent.run(df)

# Print results
print("\n=== AI INSIGHTS ===\n")
print(result["ai_insights"])

print("\n=== RAW FINDINGS ===\n")
print(result["findings"])