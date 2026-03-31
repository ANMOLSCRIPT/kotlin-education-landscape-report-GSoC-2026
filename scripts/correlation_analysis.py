import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

df = pd.read_csv("data/processed/kotlin_courses_dataset.csv")
os.makedirs("visuals", exist_ok=True)

# Encode categorical data
encoded_df = df.copy()
for col in ['country', 'platform', 'level', 'category']:
    encoded_df[col] = encoded_df[col].astype('category').cat.codes

# Correlation matrix
corr = encoded_df.corr()

plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap (Encoded Features)")
plt.tight_layout()
plt.savefig("visuals/correlation_heatmap.png")
plt.close()
