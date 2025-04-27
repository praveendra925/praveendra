# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Load the dataset
df = pd.read_csv(r"C:\Users\PRAVEENDRA\Downloads\p.csv")  
print("Initial data:\n", df.head())

print("\nInfo:\n")
print(df.info())
print("\nMissing values:\n", df.isnull().sum())
print("\nStatistics:\n", df.describe())


for col in df.select_dtypes(include=['float64', 'int64']).columns:
    df[col].fillna(df[col].mean(), inplace=True)

for col in df.select_dtypes(include=['object']).columns:
    df[col].fillna(df[col].mode()[0], inplace=True)


df = df.drop_duplicates()
for col in df.select_dtypes(include=['float64', 'int64']).columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    df = df[(df[col] >= Q1 - 1.5 * IQR) & (df[col] <= Q3 + 1.5 * IQR)]

df = pd.get_dummies(df, drop_first=True)
scaling_method = "standardize"  
num_cols = df.select_dtypes(include=['int64', 'float64']).columns

if scaling_method == "standardize":
    scaler = StandardScaler()
else:
    scaler = MinMaxScaler()

df[num_cols] = scaler.fit_transform(df[num_cols])

plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

print("\nCleaned and Prepared Data:\n", df.head())
