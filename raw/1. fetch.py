import requests
import json
import time

# Change the venue here


# VENUE = "oral"
# VENUE = "spotlight"
VENUE = "poster"


BASE_URL = "https://api2.openreview.net/notes"
PARAMS = {
    "content.venue": "NeurIPS 2025 " + VENUE,
    "details": "replyCount,presentation,writable",
    "domain": "NeurIPS.cc/2025/Conference",
    "invitation": "NeurIPS.cc/2025/Conference/-/Submission",
    "limit": 100,
    "offset": 0,
}
HEADERS = {
    "accept": "application/json,text/*;q=0.99",
    "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "dnt": "1",
    "origin": "https://openreview.net",
    "referer": "https://openreview.net/",
    "sec-ch-ua": '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
}

# 可选：你的 cookie（用于访问完整数据）
COOKIES = {
    "_ga": "GA1.1.79774197.1756700559",
    "GCILB": "b83e141730cb4b3a",
    "_ga_GTB25PBMVL": "GS2.1.s1762439962$o41$g1$t1762440627$j59$l0$h0",
}

def fetch_all_notes():
    all_notes = []
    offset = 0
    limit = PARAMS["limit"]

    while True:
        PARAMS["offset"] = offset
        response = requests.get(BASE_URL, headers=HEADERS, cookies=COOKIES, params=PARAMS)
        if response.status_code != 200:
            print(f"Request failed at offset {offset}: {response.status_code}")
            break

        data = response.json()
        notes = data.get("notes", [])
        if not notes:
            print("No more notes found.")
            break

        all_notes.extend(notes)
        print(f"Fetched {len(notes)} notes (total {len(all_notes)})")

        # 如果数量少于 limit，说明已到末尾
        if len(notes) < limit:
            break

        offset += limit
        time.sleep(0.3)  # 防止触发速率限制

    return all_notes


if __name__ == "__main__":
    notes = fetch_all_notes()

    # 保存结果
    with open(f"neurips2025_{VENUE}.json", "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=2, ensure_ascii=False)

    print(f"Saved {len(notes)} notes to neurips2025_{VENUE}.json")
