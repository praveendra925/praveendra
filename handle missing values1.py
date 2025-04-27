import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'name': ['John', 'Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Henry', 'Ivy'],
    'age': [25, 30, None, 35, 28, 22, 40, 29, None, 26],
    'gender': ['Male', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'income': [50000, 60000, 55000, 70000, 65000, None, 75000, 68000, 58000, 62000]
}

df = pd.DataFrame(data)


df.to_csv(r"C:\Users\PRAVEENDRA\Downloads\p.csv", index=False)

print("Original Dataset:")
print(df)


missing_values = df.isnull().sum()
print("\nMissing Values in Dataset:")
print(missing_values)


sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title('Missing Values Heatmap')
plt.show()

df['age'].fillna(df['age'].mean(), inplace=True)  
df['income'].fillna(df['income'].mean(), inplace=True)  

df['gender'].fillna(df['gender'].mode()[0], inplace=True)  


missing_values_after = df.isnull().sum()
print("\nMissing Values After Imputation:")
print(missing_values_after)


sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title('Missing Values After Imputation Heatmap')
plt.show()


print("\nCleaned Dataset:")
print(df)


df.to_csv(r"C:\Users\PRAVEENDRA\Downloads\p.csv", index=False)
