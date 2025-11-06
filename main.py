import pandas as pd

df = pd.read_csv("neurips25_author_profiles.csv")

print(df.info())
print(df.shape)
print(df.columns)
