import json
import pandas as pd

FILES = [
    "data/neurips2025_oral.json",
    "data/neurips2025_spotlight.json",
    "data/neurips2025_poster.json",
]

all_author_ids = []

for path in FILES:
    try:
        df = pd.read_json(path)
    except ValueError:
        # Fallback for line-delimited JSON, if any
        df = pd.read_json(path, lines=True)

    # Prefer nested content.authorids if present
    if "content" in df.columns:
        for content in df["content"]:
            if isinstance(content, dict):
                authorids = content.get("authorids", [])
                if isinstance(authorids['value'], list):
                    all_author_ids.extend(authorids['value'])
    # Some exports might have top-level authorids
    if "authorids" in df.columns:
        for authorids in df["authorids"]:
            if isinstance(authorids, list):
                all_author_ids.extend(authorids)

unique_author_ids = sorted(set(all_author_ids))

json.dump(unique_author_ids, open("data/neurips2025_author_ids.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"Saved {len(unique_author_ids)} author ids to neurips2025_author_ids.json")