import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv("data/processed/kotlin_courses_dataset.csv")
os.makedirs("visuals", exist_ok=True)

plt.figure(figsize=(6,4))
sns.countplot(data=df, x='level', order=['Beginner','Intermediate','Advanced'])
plt.title("Course Level Distribution")
plt.tight_layout()
plt.savefig("visuals/level_distribution.png")
plt.close()
