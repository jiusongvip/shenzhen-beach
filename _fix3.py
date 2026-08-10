path = r"D:\workspaces\website\shenzhen-beach\src\pages\beaches\[slug].astro"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the inline expression with a pre-computed variable approach
# Option 1: Just use the raw waterQuality string directly (no split/trim needed)
old_expr = '{b.features.waterQuality.split("(")[0].trim()}'
new_expr = '{b.features.waterQuality.replace(/\(.*/, "").trim()}'
if old_expr in content:
    content = content.replace(old_expr, new_expr)
    print("Replaced with .replace()")
else:
    print("Old expr not found in content")
    # Try searching for partial
    for line in content.split("\n"):
        if "waterQuality" in line and "trim" in line:
            print("Found:", line.strip()[:120])

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
