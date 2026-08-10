path = r"D:\workspaces\website\shenzhen-beach\src\pages\beaches\[slug].astro"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

old = '{b.features.waterQuality.split("(")[0].trim()}'
new = '{b.features.waterQuality.split("(")[0].trim()}'
content = content.replace(old, new)
print("Replace count:", content.count(new))
with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
