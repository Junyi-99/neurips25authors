import pandas as pd

df_o = pd.read_json("data/neurips2025_oral.json")
df_s = pd.read_json("data/neurips2025_spotlight.json")
df_p = pd.read_json("data/neurips2025_poster.json")
df_a = pd.read_json("data/neurips2025_author_ids.json")

print(f"There are {len(df_o)} oral papers")
print(f"There are {len(df_s)} spotlight papers")
print(f"There are {len(df_p)} poster papers")
print(f"There are {len(df_a)} author ids")
