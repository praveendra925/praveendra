import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'name': ['John', 'Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Henry', 'Ivy'],
    'age': [25, 30, None, 35, 28, 22, 40, 29, None, 26],
    'gender': ['Male', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'income': [50000, 60000, 55000, 70000, 65000, None, 75000, 68000, 58000, 62000],
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']
}

# Create the DataFrame
df = pd.DataFrame(data)

df.fillna({'age': df['age'].mean(), 'income': df['income'].mean()}, inplace=True) 
df['income'].fillna(df['income'].mean(), inplace=True)  


df['gender'].fillna(df['gender'].mode()[0], inplace=True)  
print("Cleaned Dataset with Imputed Values:")
print(df)

label_encoder = LabelEncoder()
df['gender'] = label_encoder.fit_transform(df['gender'])  

df = pd.get_dummies(df, columns=['city'], drop_first=True)  

print("\nDataset After Encoding Categorical Features:")
print(df)

df.to_csv('cleaned_and_encoded_dataset.csv', index=False)
