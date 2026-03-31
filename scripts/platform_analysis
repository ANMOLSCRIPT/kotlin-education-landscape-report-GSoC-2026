import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

df = pd.read_csv("data/processed/kotlin_courses_dataset.csv")
os.makedirs("visuals", exist_ok=True)

plt.figure(figsize=(8,5))
sns.countplot(data=df, x='platform', order=df['platform'].value_counts().index)
plt.title("Platform-wise Distribution")
plt.xticks(rotation=40)
plt.tight_layout()
plt.savefig("visuals/platform_distribution.png")
plt.close()
