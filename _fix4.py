path = r"D:\workspaces\website\shenzhen-beach\src\pages\beaches\[slug].astro"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace any waterQuality manipulation with just the raw value
import re
pattern = r'\{b\.features\.waterQuality[^}]*\}'
matches = re.findall(pattern, content)
print(f"Found waterQuality patterns: {matches}")

# Replace all variants with raw value
content = re.sub(r'\{b\.features\.waterQuality[^}]*\}', '{b.features.waterQuality}', content)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("All waterQuality expressions simplified to raw value")
