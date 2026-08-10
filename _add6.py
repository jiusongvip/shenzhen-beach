import json, os
base = r"D:\workspaces\website\shenzhen-beach\src"
with open(os.path.join(base, "data", "beaches.json"), "r", encoding="utf-8") as f:
    beaches = json.load(f)
print(f"Current beach count: {len(beaches)}")
print(f"Beach IDs: {[b['id'] for b in beaches]}")
