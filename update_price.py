import requests
import json

# 抓取政府公開 API 資料
url = "https://raw.githubusercontent.com/hirocaster/farm-price-proxy/main/source.json"
resp = requests.get(url)
data = resp.json()

# 你想保留的菜名
wanted_names = [
    "青江菜", "小白菜", "小松菜", "大陸妹", "油菜", "高麗菜",
    "大白菜", "紅蘿蔔(本產)", "番茄", "菜豆", "油麥菜"
]

# 過濾並簡化資料
result = []
for item in data:
    name = item.get("作物名稱")
    price = item.get("平均價")
    if name in wanted_names and price not in [None, "", "NA"]:
        result.append({
            "作物名稱": name,
            "平均價": price
        })

# 寫入 JSON 檔案
with open("farm-price.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
