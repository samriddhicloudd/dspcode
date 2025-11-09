import pandas as pd

# Load your dataset
data = pd.read_csv("health_data.csv")

print("Data Type: Structured (CSV file)")
print("Data State: At-Rest (stored in file)\n")

# Simple PII check
for column in data.columns:
    if any(word in column.lower() for word in ["name", "email", "phone", "aadhar"]):
        print(f"Column '{column}' may contain PII data.")