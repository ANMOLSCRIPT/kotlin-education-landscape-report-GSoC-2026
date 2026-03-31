import pandas as pd

DATA_PATH = "data/processed/kotlin_courses_dataset.csv"

df = pd.read_csv(DATA_PATH)

print("\nDataset Overview\n")
print(df.head())

print("\nBasic Statistics\n")
print(df.describe(include='all'))

print("\nTotal Courses:", len(df))
print("Total Institutions:", df['institution'].nunique())
print("Total Countries:", df['country'].nunique())
