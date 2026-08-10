import json, os
base = r"D:\workspaces\website\shenzhen-beach\src"
with open(os.path.join(base, "data", "beaches.json"), "r", encoding="utf-8") as f:
    beaches = json.load(f)

b4 = {
    "id":"nanao","name":"Nanao Beach","nameCN":"\u5357\u6fb3\u6c99\u6ee9","distance":"60 min","fee":"Free","feeNum":0,
    "bestFor":["Local experience","Seafood","Casual visit"],"rating":3.8,"crowdLevel":"moderate","crowdLabel":"Moderate on weekends",
    "location":[22.5368,114.4982],"slug":"nanao",
    "description":"The main beach in Nanao town, a working fishing port. Local experience, excellent seafood.",
    "longDescription":"Nanao Beach is not a postcard beach. It is a working beach in a working fishing town, and that is exactly what makes it interesting. The sand is mixed with pebbles, the water is not as clear as the eastern beaches, and you will see fishing boats rather than surfboards. But you get an authentic slice of Shenzhen coastal life. In the morning, watch fishermen unload their catch. By lunchtime, that catch is on your plate at waterfront restaurants. Nanao is more of a lunch-and-stroll destination than a full beach day. Come for the seafood, walk along the waterfront, browse the morning fish market. The town is also the gateway to the eastern Dapeng Peninsula.",
    "openingHours":"Always accessible (public town beach). Restaurants: 10:00-22:00.",
    "familyFriendly":True,"accessibility":"Town beach accessible via paved road. Market has steps.",
    "transport":{"bus":"E11 express bus directly to Nanao terminus (~1 hour, ~10 RMB). Most convenient bus access.","taxiFromFutian":"~150 RMB (60 min)","taxiFromLuohu":"~110 RMB (45 min)","taxiFromNanshan":"~170 RMB (70 min)","driveTime":"45-60 min","parking":"Town parking, ~20 RMB/day."},
    "facilities":{"showers":"Basic public showers (cold, ~5 RMB)","lockers":"None","umbrellas":"None","lifeguards":"Seasonal, limited","food":"Excellent seafood restaurants throughout town","restrooms":"Public available","changingRooms":"None","firstAid":"Town clinic nearby"},
    "features":{"sandType":"Mixed sand, some rocky areas","waterQuality":"Grade II-III (varies)","waveType":"Calm, harbor-protected","bestSeason":"May-October","swimZone":"Limited areas"},
    "food":{"onSite":"Dozens of waterfront seafood restaurants with live tanks. Pick your fish, crab, shrimp, or shellfish and they cook it to order. Also noodle shops, breakfast spots, and casual eateries throughout town.","nearby":"Morning fish market (best before 9 AM) is worth visiting for the spectacle.","mustTry":"Steamed fish Cantonese style, salt and pepper mantis shrimp, stir-fried crab with ginger and scallion, cold Tsingtao beer","priceRange":"Seafood: 100-200 RMB per person. Noodle shop: 20-40 RMB."},
    "accommodation":{"nearby":"Hotels and guesthouses in Nanao (150-400 RMB/night). Nanao Hotel (~300 RMB/night). Some waterfront rooms.","camping":"Not suitable.","priceRange":"Budget: 150-250 RMB. Mid-range: 250-400 RMB."},
    "clothing":{"summer":"Casual beach wear. Swimsuit if swimming (check water quality). Sandals for waterfront and market walking.","winter":"Light jacket. Waterfront can be windy. Restaurants indoors.","essentials":["Cash (some restaurants prefer cash)","Appetite (main reason to come)","Camera (fish market is photogenic)","Towel if swimming","Sunscreen"]},
    "activities":[{"name":"Seafood Dining","desc":"The number one activity. Pick seafood from tanks, have it cooked to order. Go with a group to try more dishes. Lunch is best - fish is freshest."},{"name":"Morning Fish Market","desc":"Visit before 9 AM. Fishermen unloading catch, buyers haggling. A photographer dream and glimpse of disappearing Shenzhen."},{"name":"Waterfront Walk","desc":"Pleasant harborfront promenade for post-lunch stroll. Watch fishing boats, enjoy sea breeze."},{"name":"Island Boat Trips","desc":"Small boats to nearby islands from Nanao harbor. Sanmen Island popular for day trips with better beaches and snorkeling (~200-400 RMB half-day)."}],
    "safety":{"lifeguardHours":"Limited seasonal coverage.","hazards":"Water quality varies. Harbor has boat traffic - swim only in designated areas.","waterQualitySource":"Grade II-III. Less consistent due to harbor proximity.","emergencyContact":"Town clinic. Dapeng Hospital (30 min). Emergency: 110/120."},
    "photoSpots":"Morning fish market (7-9 AM) for documentary style. Harbor at sunset with boat silhouettes. Waterfront promenade. Restaurant seafood displays.",
    "bestTimeToVisit":"Weekday lunch for freshest seafood without crowds. Early morning for fish market. Avoid summer weekends.",
    "tips":["Best for seafood lunch plus a casual beach stroll","Check out the fish market in the morning","Nearby islands offer boat trips","Less swimming-focused than other beaches"]
}

b5 = {
    "id":"shuitousha","name":"Shuitousha","nameCN":"\u6c34\u5934\u6c99","distance":"65 min","fee":"Free","feeNum":0,
    "bestFor":["Quiet beach day","Local vibe"],"rating":3.7,"crowdLevel":"quiet","crowdLabel":"Usually quiet",
    "location":[22.5268,114.5156],"slug":"shuitousha",
    "description":"A small, lesser-known beach near Nanao. Quiet and unpretentious. Zero facilities but total tranquility.",
    "longDescription":"Shuitousha is Shenzhen hidden beach. Small, unremarkable in photos, but beloved by locals who know about it. At maybe 300 meters long with mixed sand and rocky patches, it will not win beauty contests. But on a weekday, you might be one of only 10 people on the entire beach. There are zero facilities: no showers, lockers, food, or lifeguards. Bring everything, take everything back. The trade-off is tranquility hard to find anywhere else near a major city. Best combined with a Nanao seafood lunch - only 10 minutes away.",
    "openingHours":"Always accessible. No formal hours or facilities.",
    "familyFriendly":False,"accessibility":"Not accessible. Uneven ground, no paved paths.",
    "transport":{"bus":"E11 to Nanao, then short walk (15 min) or taxi (starting fare)","taxiFromFutian":"~155 RMB (65 min)","taxiFromLuohu":"~115 RMB (50 min)","taxiFromNanshan":"~175 RMB (75 min)","driveTime":"50-65 min","parking":"Informal roadside. Free but limited."},
    "facilities":{"showers":"None","lockers":"None","umbrellas":"None","lifeguards":"No","food":"None","restrooms":"None on-site","changingRooms":"None","firstAid":"None"},
    "features":{"sandType":"Mixed sand, natural state","waterQuality":"Grade II","waveType":"Calm","bestSeason":"May-September","swimZone":"No formal zone"},
    "food":{"onSite":"Nothing. Zero facilities.","nearby":"Walk to Nanao town (10-15 min) for all dining.","mustTry":"Pack a picnic. Buy supplies in Nanao.","priceRange":"BYO everything."},
    "accommodation":{"nearby":"Guesthouses in Nanao (10-15 min walk, 150-300 RMB/night).","camping":"Possible but not officially supported. Bring all gear.","priceRange":"Guesthouse: 150-300 RMB."},
    "clothing":{"summer":"Swimsuit, full sun protection (zero shade), water shoes for rocks. Bring own umbrella or beach tent.","winter":"Light jacket for beach walks. Pleasant solitude but too cold for swimming.","essentials":["Everything for a beach day (zero facilities)","Water (2L+ per person)","Food/picnic","Sunscreen + hat","Umbrella or beach tent","Trash bag","Toilet paper","First aid kit"]},
    "activities":[{"name":"Quiet Relaxation","desc":"The main activity. Read, nap, listen to waves. A beach for doing nothing and doing it well."},{"name":"Picnic","desc":"With no vendors, a picnic is mandatory. Buy supplies in Nanao, find your spot."},{"name":"Casual Swimming","desc":"Calm water but no lifeguards. Swim with caution, not alone."}],
    "safety":{"lifeguardHours":"No lifeguards. Ever.","hazards":"Zero facilities. No shade, no water source. Swim at own risk.","waterQualitySource":"Grade II. Decent quality.","emergencyContact":"Nearest help in Nanao (10-15 min). Emergency: 110/120."},
    "photoSpots":"The quiet empty beach itself. Sunrise. Rocky sections at low tide for texture.",
    "bestTimeToVisit":"Weekday mornings for guaranteed solitude. Sep-Oct for pleasant weather. Combine with Nanao lunch.",
    "tips":["Come prepared with everything","Swim at your own risk","Great spot for a quiet picnic","Parking is informal; arrive early"]
}

b6 = {
    "id":"shangdong","name":"Shangdong","nameCN":"\u4e0a\u6d1e","distance":"60 min","fee":"Free","feeNum":0,
    "bestFor":["Exploration","Solitude"],"rating":3.5,"crowdLevel":"quiet","crowdLabel":"Almost always empty",
    "location":[22.5643,114.4876],"slug":"shangdong",
    "description":"An off-the-radar beach most Shenzhen residents have never heard of. Rocky coastline, total solitude.",
    "longDescription":"Shangdong is for people who say I want to go somewhere I will not see another human being. A rough, natural stretch of coast with more rocks than sand. The beach is small (maybe 200 meters), with mixed sand and pebbles between rocky headlands. Zero facilities of any kind. No road directly to the beach. Minimal signage. Navigate by GPS, be comfortable with informal parking and unmarked paths. Water quality is excellent (Grade I) because nothing is upstream. The coastline is untouched and raw. For experienced beach-goers who value solitude above all else and are prepared to be entirely self-sufficient. This is the most extreme beach option near Shenzhen.",
    "openingHours":"Always accessible. No gate, no hours.",
    "familyFriendly":False,"accessibility":"Not accessible at all. Rough terrain, no paths, no facilities.",
    "transport":{"bus":"Limited. Best by car or taxi. Nearest bus stop requires 20+ min walk.","taxiFromFutian":"~155 RMB (60 min)","taxiFromLuohu":"~115 RMB (50 min)","taxiFromNanshan":"~175 RMB (70 min)","driveTime":"50-60 min","parking":"Informal roadside. No designated lot."},
    "facilities":{"showers":"None","lockers":"None","umbrellas":"None","lifeguards":"No","food":"None","restrooms":"None","changingRooms":"None","firstAid":"None"},
    "features":{"sandType":"Mixed sand and rock, ~200m","waterQuality":"Grade I (untouched)","waveType":"Varies, exposed coastline","bestSeason":"May-September","swimZone":"None"},
    "food":{"onSite":"Nothing for kilometers.","nearby":"Nearest food in Dapeng town (20 min drive).","mustTry":"Epic DIY picnic. Camping-level self-sufficiency for a beach day.","priceRange":"BYO everything."},
    "accommodation":{"nearby":"Guesthouses in Dapeng (20 min drive). No accommodation near beach.","camping":"Possible for experienced campers with all gear. No facilities. Leave no trace.","priceRange":"Guesthouse: 150-300 RMB in Dapeng."},
    "clothing":{"summer":"Full beach survival kit. Swimwear, sturdy shoes for rocks, full sun protection (zero shade), water shoes. Pack as if going into wilderness.","winter":"Hiking gear more than beach gear. Dramatic scenery but dangerous for swimming.","essentials":["Everything. Seriously.","Water (3L+ per person)","Full meal/picnic","Sunscreen + hat + UV protection","Sturdy shoes (rocks are sharp)","Comprehensive first aid kit","Phone + power bank + offline maps","Tell someone your plans","Trash bags","Toilet paper + hand sanitizer"]},
    "activities":[{"name":"Exploration","desc":"Not a swimming beach. An exploration destination. Scramble over rocks, discover tide pools, find private patches of sand. The adventure is the point."},{"name":"Photography","desc":"Raw coastline for dramatic photos. Turquoise water against dark rocks. Zero people in shots."},{"name":"Solitude","desc":"Almost guaranteed to be alone. Most private beach experience near Shenzhen."}],
    "safety":{"lifeguardHours":"No lifeguards. Ever.","hazards":"MOST HAZARDOUS beach near Shenzhen. Sharp rocks, slippery surfaces, zero facilities, no shade, no water, limited signal, no easy emergency access. Swimming extremely dangerous - exposed coastline with unpredictable currents.","waterQualitySource":"Grade I. Water is clean but conditions are dangerous.","emergencyContact":"Difficult emergency access. Help in Dapeng (20+ min). Carry comprehensive first aid. Tell someone plans. Emergency: 110/120."},
    "photoSpots":"Rocky coastline at low tide. Turquoise water against dark rocks. Sunrise on eastern shore. Tide pools with marine life.",
    "bestTimeToVisit":"Weekdays for guaranteed solitude. Oct-Nov for best light. Only go in good weather.",
    "tips":["Off-grid experience; bring everything","Swim with extreme caution","Check tide times","Tell someone where you are going"]
}

beaches.extend([b4, b5, b6])
with open(os.path.join(base, "data", "beaches.json"), "w", encoding="utf-8") as f:
    json.dump(beaches, f, ensure_ascii=False, indent=2)
print(f"Added 3 beaches. Total: {len(beaches)}")
for b in beaches:
    has = all(k in b for k in ["clothing","food","accommodation","activities","safety","photoSpots","longDescription","openingHours","familyFriendly","accessibility"])
    print(f"  {b['name']}: {'OK' if has else 'MISSING'}")
