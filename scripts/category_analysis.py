import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv("data/processed/kotlin_courses_dataset.csv")
os.makedirs("visuals", exist_ok=True)

plt.figure(figsize=(8,5))
sns.countplot(data=df, x='category', order=df['category'].value_counts().index)
plt.title("Category Distribution of Kotlin Courses")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("visuals/category_distribution.png")
plt.close()
