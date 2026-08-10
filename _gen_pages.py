import json, os
base = r"D:\workspaces\website\shenzhen-beach\src\pages\beaches"

with open(r"D:\workspaces\website\shenzhen-beach\src\data\beaches.json", "r", encoding="utf-8") as f:
    beaches = json.load(f)

template = """---
import Layout from "../../layouts/Layout.astro";
import Nav from "../../components/Nav.astro";
import Footer from "../../components/Footer.astro";
---

<Layout
  title="BEACH_NAME Beach (BEACH_CN) - Transport, Food, Hotels & Tips"
  description="Complete guide to BEACH_NAME Beach in Shenzhen: how to get there, entrance fee, opening hours, food & dining, nearby hotels, activities, safety tips, and what to wear. Updated August 2026."
>
  <Nav />
  <main class="max-w-4xl mx-auto px-4 py-8 md:py-12">
    <nav class="text-sm text-gray-400 mb-6">
      <a href="/" class="hover:text-ocean">Shenzhen Beaches</a>
      <span class="mx-2">/</span>
      <span class="text-gray-600">BEACH_NAME Beach</span>
    </nav>

    <div class="mb-10">
      <div class="flex flex-wrap items-baseline gap-3">
        <h1 class="text-3xl md:text-4xl font-bold tracking-tight text-gray-900">BEACH_NAME Beach</h1>
        <span class="text-xl text-gray-400">BEACH_CN</span>
      </div>
      <div class="flex flex-wrap items-center gap-4 mt-3 text-sm">
        <span class="flex items-center gap-1"><svg width="14" height="14" viewBox="0 0 24 24" fill="#e0683a"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>RATING</span>
        <span class="text-gray-600">DISTANCE from city</span>
        <span class="text-gray-600">FEE</span>
        <span class="text-gray-600">CROWD_LABEL</span>
      </div>
    </div>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 mb-10 p-5 bg-sand rounded-xl border border-gray-200">
      <div><span class="text-xs text-gray-400 uppercase block mb-1">Opening Hours</span><span class="text-sm font-semibold text-gray-800">HOURS</span></div>
      <div><span class="text-xs text-gray-400 uppercase block mb-1">Entry Fee</span><span class="text-sm font-semibold text-gray-800">FEE</span></div>
      <div><span class="text-xs text-gray-400 uppercase block mb-1">Water Quality</span><span class="text-sm font-semibold text-gray-800">WATER_QUALITY</span></div>
      <div><span class="text-xs text-gray-400 uppercase block mb-1">Family Friendly</span><span class="text-sm font-semibold text-gray-800">FAMILY</span></div>
    </div>

    LONG_DESCRIPTION

    DETAIL_TRANSPORT

    DETAIL_FOOD

    DETAIL_ACCOMMODATION

    DETAIL_CLOTHING

    DETAIL_FACILITIES

    DETAIL_ACTIVITIES

    DETAIL_SAFETY

    DETAIL_PHOTOS

    DETAIL_BEST_TIME

    DETAIL_TIPS

    DETAIL_SIMILAR

    <div class="mt-12 pt-8 border-t border-gray-200">
      <a href="/" class="text-sm text-ocean hover:underline inline-flex items-center gap-1">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"/></svg>
        Back to all Shenzhen beaches
      </a>
    </div>
  </main>
  <Footer />
</Layout>"""

def gen_transport(b):
    lines = ['<section class="mb-12"><h2 class="text-2xl font-bold mb-4">How to Get to ' + b["name"] + ' Beach</h2><div class="bg-white border border-gray-200 rounded-xl overflow-hidden"><dl class="divide-y divide-gray-100">']
    t = b.get("transport", {})
    for k, label in [("metro","Metro"),("metroExit",""),("metroWalk",""),("bus","Bus"),("taxiFromFutian","Taxi from Futian"),("taxiFromLuohu","Taxi from Luohu"),("taxiFromNanshan","Taxi from Nanshan"),("driveTime","Driving"),("parking","Parking")]:
        if k in t and t[k]:
            if k == "metro":
                lines.append('<div class="grid grid-cols-3 px-5 py-3"><dt class="text-sm font-medium text-gray-500">Metro</dt><dd class="col-span-2 text-sm text-gray-800">' + t["metro"] + ' (' + t.get("metroExit","") + ') - ' + t.get("metroWalk","") + '</dd></div>')
            elif k not in ["metroExit","metroWalk"]:
                lines.append('<div class="grid grid-cols-3 px-5 py-3"><dt class="text-sm font-medium text-gray-500">' + label + '</dt><dd class="col-span-2 text-sm text-gray-800">' + str(t[k]) + '</dd></div>')
    lines.append('</dl></div></section>')
    return "\n".join(lines)

def gen_food(b):
    f = b.get("food", {})
    return '<section class="mb-12"><h2 class="text-2xl font-bold mb-4">Food & Dining</h2><div class="grid md:grid-cols-2 gap-6"><div class="bg-white border border-gray-200 rounded-xl p-5"><h3 class="font-semibold text-ocean mb-2">At the Beach</h3><p class="text-sm text-gray-600">' + f.get("onSite","") + '</p></div><div class="bg-white border border-gray-200 rounded-xl p-5"><h3 class="font-semibold text-ocean mb-2">Nearby</h3><p class="text-sm text-gray-600">' + f.get("nearby","") + '</p></div></div><div class="mt-4 bg-accent/5 border border-accent/20 rounded-xl p-5"><h3 class="font-semibold text-accent mb-1">What to Try</h3><p class="text-sm text-gray-700">' + f.get("mustTry","") + '</p><p class="text-xs text-gray-500 mt-2">Price range: ' + f.get("priceRange","") + '</p></div></section>'

def gen_accommodation(b):
    a = b.get("accommodation", {})
    camp = a.get("camping","")
    camping_html = ""
    if camp and "Not permitted" not in camp:
        camping_html = '<div class="mt-3 bg-amber-50 border border-amber-200 rounded-xl p-5"><h3 class="font-semibold text-amber-700 mb-1">Camping</h3><p class="text-sm text-gray-700">' + camp + '</p></div>'
    return '<section class="mb-12"><h2 class="text-2xl font-bold mb-4">Where to Stay</h2><div class="bg-white border border-gray-200 rounded-xl p-5"><p class="text-sm text-gray-600">' + a.get("nearby","") + '</p></div>' + camping_html + '<p class="text-xs text-gray-400 mt-3">Price range: ' + a.get("priceRange","") + '</p></section>'

def gen_clothing(b):
    c = b.get("clothing", {})
    ess = c.get("essentials", [])
    ess_html = "".join(['<li class="flex gap-2"><span class="text-accent">&#10003;</span> ' + e + '</li>' for e in ess])
    return '<section class="mb-12"><h2 class="text-2xl font-bold mb-4">What to Wear & Bring</h2><div class="grid md:grid-cols-2 gap-6"><div class="bg-white border border-gray-200 rounded-xl p-5"><h3 class="font-semibold text-ocean mb-2">Summer (May-Oct)</h3><p class="text-sm text-gray-600">' + c.get("summer","") + '</p></div><div class="bg-white border border-gray-200 rounded-xl p-5"><h3 class="font-semibold text-ocean mb-2">Winter (Nov-Apr)</h3><p class="text-sm text-gray-600">' + c.get("winter","") + '</p></div></div><div class="mt-4 bg-white border border-gray-200 rounded-xl p-5"><h3 class="font-semibold text-ocean mb-2">Packing Checklist</h3><ul class="grid sm:grid-cols-2 gap-2 text-sm text-gray-600">' + ess_html + '</ul></div></section>'

def gen_activities(b):
    acts = b.get("activities", [])
    items = "".join(['<div class="bg-white border border-gray-200 rounded-xl p-5"><h3 class="font-semibold text-gray-800 mb-1">' + a["name"] + '</h3><p class="text-sm text-gray-600">' + a["desc"] + '</p></div>' for a in acts])
    return '<section class="mb-12"><h2 class="text-2xl font-bold mb-4">Things to Do</h2><div class="space-y-4">' + items + '</div></section>'

def gen_safety(b):
    s = b.get("safety", {})
    return '<section class="mb-12"><h2 class="text-2xl font-bold mb-4">Safety</h2><div class="bg-white border border-gray-200 rounded-xl p-5 space-y-3"><div><span class="text-sm font-medium text-gray-500">Lifeguard Hours: </span><span class="text-sm text-gray-800">' + s.get("lifeguardHours","") + '</span></div><div><span class="text-sm font-medium text-gray-500">Hazards: </span><span class="text-sm text-gray-800">' + s.get("hazards","") + '</span></div><div><span class="text-sm font-medium text-gray-500">Water Quality: </span><span class="text-sm text-gray-800">' + s.get("waterQualitySource","") + '</span></div><div><span class="text-sm font-medium text-gray-500">Emergency: </span><span class="text-sm text-gray-800">' + s.get("emergencyContact","") + '</span></div></div></section>'

def gen_facilities(b):
    f = b.get("facilities", {})
    items = ""
    for k, label in [("showers","Showers"),("lockers","Lockers"),("changingRooms","Changing Rooms"),("umbrellas","Umbrellas/Chairs"),("lifeguards","Lifeguards"),("restrooms","Restrooms"),("firstAid","First Aid")]:
        v = f.get(k, "")
        if v and v not in ["None", "None on-site"]:
            items += '<div class="grid grid-cols-3 px-5 py-3"><dt class="text-sm font-medium text-gray-500">' + label + '</dt><dd class="col-span-2 text-sm text-gray-800">' + v + '</dd></div>'
    return '<section class="mb-12"><h2 class="text-2xl font-bold mb-4">Facilities</h2><div class="bg-white border border-gray-200 rounded-xl overflow-hidden"><dl class="divide-y divide-gray-100">' + items + '</dl></div></section>'

def gen_similar(b):
    similar = [x for x in beaches if x["id"] != b["id"] and any(t in b["bestFor"] for t in x["bestFor"])][:3]
    if not similar: return ""
    cards = "".join(['<a href="/beaches/' + s["slug"] + '/" class="block bg-white border border-gray-200 rounded-xl p-4 hover:border-accent hover:shadow-sm transition-all"><span class="font-semibold text-gray-800">' + s["name"] + '</span><span class="text-xs text-gray-400 ml-1">' + s["nameCN"] + '</span><p class="text-xs text-gray-500 mt-1">' + ", ".join(s["bestFor"][:2]) + '</p><p class="text-xs text-gray-400 mt-2">&#9733; ' + str(s["rating"]) + ' &middot; ' + s["fee"] + '</p></a>' for s in similar])
    return '<section class="mb-12"><h2 class="text-2xl font-bold mb-4">You Might Also Like</h2><div class="grid sm:grid-cols-3 gap-4">' + cards + '</div></section>'

def gen_tips(b):
    tips = b.get("tips", [])
    items = "".join(['<li class="flex gap-2 text-sm text-gray-600"><span class="text-accent shrink-0 mt-0.5">&#8226;</span> ' + t + '</li>' for t in tips])
    return '<section class="mb-12"><h2 class="text-2xl font-bold mb-4">Visitor Tips</h2><ul class="space-y-2">' + items + '</ul></section>'

for b in beaches:
    page = template
    page = page.replace("BEACH_NAME", b["name"])
    page = page.replace("BEACH_CN", b["nameCN"])
    page = page.replace("DISTANCE", b["distance"])
    page = page.replace("FEE", b["fee"])
    page = page.replace("RATING", str(b["rating"]))
    page = page.replace("CROWD_LABEL", b["crowdLabel"])
    page = page.replace("HOURS", b.get("openingHours", ""))
    page = page.replace("WATER_QUALITY", b["features"]["waterQuality"].split("(")[0].strip())
    page = page.replace("FAMILY", "Yes" if b.get("familyFriendly") else "Not ideal")

    page = page.replace("LONG_DESCRIPTION", '<section class="mb-12"><h2 class="text-2xl font-bold mb-4">Overview</h2><div class="text-gray-600 leading-relaxed space-y-3">' + "".join(['<p>' + p + '</p>' for p in b.get("longDescription","").split("\\n\\n")]) + '</div></section>')
    page = page.replace("DETAIL_TRANSPORT", gen_transport(b))
    page = page.replace("DETAIL_FOOD", gen_food(b))
    page = page.replace("DETAIL_ACCOMMODATION", gen_accommodation(b))
    page = page.replace("DETAIL_CLOTHING", gen_clothing(b))
    page = page.replace("DETAIL_FACILITIES", gen_facilities(b))
    page = page.replace("DETAIL_ACTIVITIES", gen_activities(b))
    page = page.replace("DETAIL_SAFETY", gen_safety(b))
    page = page.replace("DETAIL_PHOTOS", '<section class="mb-12"><h2 class="text-2xl font-bold mb-4">Photo Spots</h2><p class="text-gray-600 text-sm leading-relaxed">' + b.get("photoSpots","") + '</p></section>')
    page = page.replace("DETAIL_BEST_TIME", '<section class="mb-12"><h2 class="text-2xl font-bold mb-4">Best Time to Visit</h2><div class="bg-ocean/5 border border-ocean/20 rounded-xl p-5"><p class="text-sm text-gray-700">' + b.get("bestTimeToVisit","") + '</p></div></section>')
    page = page.replace("DETAIL_TIPS", gen_tips(b))
    page = page.replace("DETAIL_SIMILAR", gen_similar(b))

    filepath = os.path.join(base, b["slug"] + ".astro")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"  OK: {b['slug']}.astro")

print(f"\\nGenerated {len(beaches)} detail pages with full content")
