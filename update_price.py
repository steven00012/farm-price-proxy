import requests
import json

# 政府 API 透過 Cloudflare Worker 中繼代理
url = "https://veg-price.kai0932516360.workers.dev/"

resp = requests.get(url)

try:
    data = resp.json()
except Exception:
    print("❌ 抓到的不是 JSON，請確認 Worker 是否啟用")
    print(resp.text)
    exit(1)

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

with open("farm-price.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
