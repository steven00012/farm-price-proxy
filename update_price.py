import requests
import json

# ✅ 政府 API（改由 GitHub Actions 來抓，避開 Cloudflare 限制）
url = "https://raw.githubusercontent.com/openjson-tw/farm-price-daily/main/farm-price.json"

resp = requests.get(url)
data = resp.json()

# ✅ 想保留的作物
wanted_names = [
    "青江菜", "小白菜", "小松菜", "大陸妹", "油菜", "高麗菜",
    "大白菜", "紅蘿蔔(本產)", "番茄", "菜豆", "油麥菜"
]

result = []
for item in data:
    name = item.get("作物名稱")
    price = item.get("平均價")
    if name in wanted_names and price not in [None, "", "NA"]:
        result.append({
            "作物名稱": name,
            "平均價": price
        })

# ✅ 覆寫更新 JSON
with open("farm-price.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
