import pandas as pd
import numpy as np

# Load your dataset (make sure the path is correct)
df = pd.read_csv('dataset.csv')  # Adjust if file is in a different location

# First 5 rows
print("Head:\n", df.head())

# Data types, nulls, column names
print("\nInfo:")
print(df.info())

# Summary statistics for numerical columns
print("\nDescribe:")
print(df.describe())

# Check for missing/null values
print("\nMissing Values:")
print(df.isnull().sum())
