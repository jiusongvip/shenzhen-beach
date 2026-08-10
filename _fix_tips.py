import json
with open(r"D:\workspaces\website\shenzhen-beach\src\data\beaches.json", "r", encoding="utf-8") as f:
    beaches = json.load(f)

tips_map = {
    "dameisha": ["Arrive before 9 AM on weekends to avoid crowds and secure parking","Bring your own towels and snacks; beachside prices are marked up","Night swimming not permitted; beach closes at 22:00","Free entry but registration via WeChat mini-program may be required during peak season","The eastern end of the beach is quieter; walk 5-10 minutes past the main entrance"],
    "xichong": ["Best visited on weekdays; summer weekends can be crowded despite the distance","Surfboard rentals available at beachside shops (~100 RMB/hr)","Camping allowed in designated areas; bring your own gear or rent locally","Cell signal can be weak in some sections; download maps beforehand","The western end (entrance 4) is the quietest area with the best swimming"],
    "xiaomeisha": ["Entry fee includes basic facilities; worth it for the cleaner experience","Combine with a visit to Xiaomeisha Sea World next door","Resort hotels offer day passes with pool access (200-400 RMB)","Less crowded than Dameisha on weekends","The resort beach bar serves the best cocktails in Shenzhen"],
    "dongchong": ["Hike the Dongchong-Xichong coastal trail (3-4 hours, stunning views)","Facilities are basic; bring everything you need","Better water quality than the city beaches","No ATMs nearby; bring cash","Start the coastal hike before 9 AM to avoid midday heat"]
}

for b in beaches:
    if b["id"] in tips_map:
        b["tips"] = tips_map[b["id"]]

with open(r"D:\workspaces\website\shenzhen-beach\src\data\beaches.json", "w", encoding="utf-8") as f:
    json.dump(beaches, f, ensure_ascii=False, indent=2)
print("Tips added to first 4 beaches")
