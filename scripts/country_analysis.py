import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("data/processed/kotlin_courses_dataset.csv")
os.makedirs("visuals", exist_ok=True)

country_counts = df['country'].value_counts()

plt.figure(figsize=(8,5))
country_counts.plot(kind='bar')
plt.title("Country-wise Kotlin Course Distribution")
plt.xlabel("Country")
plt.ylabel("Number of Courses")
plt.tight_layout()
plt.savefig("visuals/country_distribution.png")
plt.close()
