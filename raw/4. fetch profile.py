import os
import json
import openreview
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

# 初始化 client
client = openreview.api.OpenReviewClient(baseurl='https://api2.openreview.net')

# 加载作者 ID 列表
authors = json.load(open("data/neurips2025_author_ids.json"))
os.makedirs("data/authors", exist_ok=True)

def fetch_and_save_profile(author_id):
    """获取单个作者 profile 并保存到文件"""
    path = f"data/authors/{author_id}.json"
    if os.path.exists(path):
        return None  # 已存在则跳过
    try:
        profile = client.get_profile(author_id)
        with open(path, "w") as f:
            json.dump(profile.to_json(), f, indent=2)
        return author_id
    except openreview.openreview.OpenReviewException as e:
        if "Not Found" in str(e):
            with open(path, "w") as f:
                json.dump({"error": str(e)}, f, indent=2)
        return f"Error: {author_id} -> {e}"
    except Exception as e:
        return f"Unexpected: {author_id} -> {e}"


MAX_WORKERS = 1
results = []

with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    futures = {executor.submit(fetch_and_save_profile, author): author for author in authors}

    for future in tqdm(as_completed(futures), total=len(futures), desc="Fetching profiles"):
        result = future.result()
        if isinstance(result, str) and result.startswith("Error"):
            print(result)
        elif isinstance(result, str) and result.startswith("Unexpected"):
            print(result)
        else:
            print(result)
            results.append(result)

print(f"\n✅ Done. {len(results)} profiles fetched successfully.")
