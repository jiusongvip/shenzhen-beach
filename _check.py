import json
with open(r"D:\workspaces\website\shenzhen-beach\src\data\beaches.json", "r", encoding="utf-8") as f:
    beaches = json.load(f)
required = ["bestFor","tips","facilities","features","transport","food","clothing","accommodation","activities","safety","photoSpots"]
for b in beaches:
    missing = [k for k in required if k not in b or b[k] is None]
    if missing:
        print(b["name"] + ": MISSING " + ", ".join(missing))
    arrs = ["bestFor","tips","activities"]
    for a in arrs:
        if a in b and b[a] is not None and not isinstance(b[a], list):
            print(b["name"] + ": " + a + " is " + type(b[a]).__name__ + " not list")
print("Check done")
