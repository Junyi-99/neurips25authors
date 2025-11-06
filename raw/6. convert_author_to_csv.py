import pandas as pd
import json
from tqdm import tqdm
import os


def load_author_map():
    author_map = {}
    author_ids = json.load(open("data/neurips2025_author_ids.json"))
    for author_id in tqdm(author_ids):
        try:
            author = json.load(open(f"data/authors/{author_id}.json"))
            if "error" in author:
                continue
            author_map[author_id] = author['content']

        except Exception as e:
            print(f"Error loading author {author_id}: {e}")
            continue
    return author_map


# load "data/author_map.json"
if os.path.exists("data/author_map.json"):
    print("Loading author map from data/author_map.json")
    author_map = json.load(open("data/author_map.json"))
else:
    print("Loading author map from data/authors/")
    author_map = load_author_map()
    print("Saving author map to data/author_map.json")
    json.dump(author_map, open("data/author_map.json", "w"), indent=2)


df = pd.DataFrame(author_map.items(), columns=['author_id', 'author_content'])
df.set_index('author_id', inplace=True)

# 把 author_content 展开成 column
for key, value in author_map.items():
    for k, v in value.items():
        # Convert complex types (list, dict) to JSON strings
        if isinstance(v, (list, dict)):
            df.loc[key, k] = json.dumps(v)
        else:
            df.loc[key, k] = v

df.drop(columns=['author_content'], inplace=True)
df.to_csv("data/neurips25_author_profiles.csv")
print(f"Saved {len(df)} authors to data/neurips25_author_profiles.csv")
