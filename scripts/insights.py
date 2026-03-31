import pandas as pd

df = pd.read_csv("data/processed/kotlin_courses_dataset.csv")

print("\nKey Insights:\n")

# Most common category
print("Most Common Category:", df['category'].value_counts().idxmax())

# Most active country
print("Most Active Country:", df['country'].value_counts().idxmax())

# Platform dominance
print("Top Platform:", df['platform'].value_counts().idxmax())

# Level distribution
print("\nLevel Distribution:\n", df['level'].value_counts())
