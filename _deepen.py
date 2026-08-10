import os, json, shutil
base = r"D:\workspaces\website\shenzhen-beach\src"

# ===== ENHANCED BEACH DATA with 衣食住行 =====
beaches = [
  {
    "id":"dameisha","name":"Dameisha","nameCN":"大梅沙","distance":"30 min","fee":"Free","feeNum":0,
    "bestFor":["Swimming","Family","First-timers"],"rating":4.2,"crowdLevel":"busy","crowdLabel":"Busy on weekends",
    "location":[22.5958,114.3121],"slug":"dameisha",
    "description":"Shenzhen most popular and accessible beach. Wide sandy shore with gentle waves, walking distance from Metro Line 8. Perfect for families and first-timers.",
    "longDescription":"Dameisha (大梅沙) is Shenzhen's most iconic public beach, stretching over 1.8 kilometers along the eastern coast. It's the first beach most Shenzhen residents ever visit, and for good reason: it's free, easy to reach via Metro Line 8, and has the best facilities of any public beach in the city.\n\nThe beach features fine yellow sand and a gentle slope into the water, making it ideal for casual swimming and families with children. A designated swimming area is marked by buoys and staffed by lifeguards during the summer season (typically 9:00 AM to 9:00 PM).\n\nThe beach underwent a major renovation in the late 2010s that added new showers, changing rooms, and a landscaped boardwalk. Behind the beach, a strip of convenience stores, snack stalls, and casual restaurants makes it easy to spend a full day here without packing a cooler.\n\nDameisha is also the gateway to the larger Dameisha resort area, which includes several hotels, a Sheraton resort, and the OCT East theme park complex just up the hill. If you're visiting Shenzhen for the first time and want the easiest possible beach experience, start here — but be prepared for crowds on summer weekends.",
    "openingHours":"06:00-22:00 (summer), 07:00-21:00 (winter)",
    "familyFriendly":True,
    "accessibility":"Wheelchair-accessible boardwalk and ramp to beach. Accessible restrooms available.",
    "transport":{
      "metro":"Line 8","metroExit":"Exit C","metroWalk":"10 min walk",
      "bus":"103, 387, M191, M362, M438, M465",
      "taxiFromFutian":"~80 RMB (40 min)","taxiFromLuohu":"~50 RMB (25 min)","taxiFromNanshan":"~110 RMB (50 min)",
      "driveTime":"30-45 min from city center","parking":"Paid lot, ~20 RMB/day, ~200 spots. Fills by 10 AM on summer weekends."
    },
    "facilities":{"showers":"10 RMB","lockers":"20 RMB","umbrellas":"50 RMB/day","lifeguards":"09:00-21:00 (summer)","food":"Convenience stores, snack stalls, BBQ pits","restrooms":"Free, multiple locations","changingRooms":"Free","firstAid":"On-site during summer"},
    "features":{"sandType":"Fine yellow sand, 1.8 km long, 50-80m wide","waterQuality":"Grade II (swimmable, tested monthly by Shenzhen Ecology Bureau)","waveType":"Gentle, protected bay, safe for casual swimming","bestSeason":"May-October","swimZone":"Designated swimming area with lifeguards, marked by red/yellow buoys"},
    "food":{
      "onSite":"Convenience stores (7-Eleven, Meiyijia) selling drinks, ice cream, and basic snacks. Several beachside snack stalls selling grilled squid, corn, sausages, and cold noodles (10-30 RMB each). BBQ pits available for rent in the designated area behind the beach.",
      "nearby":"Dameisha Village (5 min walk) has dozens of seafood restaurants. Recommended: Dameisha Seafood Street (大梅沙海鲜街) for fresh catch. Western options: McDonald's, Starbucks within 10 min walk. OCT East resort area (10 min taxi) has upscale dining.",
      "mustTry":"Grilled oysters (烤生蚝, ~15 RMB each), fresh coconut (椰子, ~10 RMB), seafood hotpot at village restaurants",
      "priceRange":"On-beach snacks: 10-50 RMB. Restaurant meal: 80-200 RMB per person. Seafood dinner: 150-400 RMB per person."
    },
    "accommodation":{
      "nearby":"Sheraton Dameisha Resort (5-star, from ~800 RMB/night, direct beach access). Vienna Hotel Dameisha (3-star, from ~300 RMB/night, 5 min walk). Dameisha Inn (budget guesthouse, from ~150 RMB/night). Several Airbnb apartments in nearby complexes.",
      "camping":"Not permitted at Dameisha.",
      "priceRange":"Budget guesthouse: 150-300 RMB. Mid-range hotel: 300-600 RMB. Resort: 800-1500 RMB."
    },
    "clothing":{
      "summer":"Swimsuit, rash guard (sun protection), flip-flops, wide-brimmed hat, sunglasses. Bring a light cover-up for walking to restaurants. Sunscreen is essential — the Shenzhen sun is strong even on cloudy days.",
      "winter":"Light jacket or hoodie (temps 15-20°C). Long pants recommended. Water is too cold for swimming without a wetsuit. Good season for beach walks and photography.",
      "essentials":["Sunscreen (SPF 50+)","Towel","Water bottle (refill stations available)","Waterproof phone pouch","Cash (some vendors don't accept mobile payment for small purchases)","Insect repellent (summer evenings)"]
    },
    "activities":[
      {"name":"Swimming","desc":"Designated swim zone with lifeguards. Gentle waves, suitable for casual and family swimming. Water depth increases gradually — safe for children near shore."},
      {"name":"Beach Volleyball","desc":"Public nets available near the center of the beach. First come, first served. Bring your own ball or rent from nearby shops."},
      {"name":"Sandcastle Building","desc":"Fine, packable sand is perfect for sandcastles. Popular with families. Shovels and buckets sold at beach shops (~20 RMB)."},
      {"name":"BBQ","desc":"Designated BBQ pits behind the beach. Bring your own food or buy from nearby supermarkets. Charcoal and grills available for rent (~50 RMB). Popular evening activity."},
      {"name":"Sunbathing","desc":"Wide sandy area with plenty of space to lay a towel. Umbrella and chair rentals available (50 RMB/day). Best before 11 AM or after 3 PM to avoid peak sun."}
    ],
    "safety":{
      "lifeguardHours":"09:00-21:00 (May-October). No lifeguards in winter.",
      "hazards":"Rip currents are rare due to the protected bay shape. Main risks: sunburn, dehydration on hot days, jellyfish during late summer (August-September).",
      "waterQualitySource":"Shenzhen Ecology Bureau monthly swimming-grade report. Grade II = safe for swimming. Check latest report before swimming.",
      "emergencyContact":"Shenzhen beach emergency: 110 (police), 120 (ambulance). On-site first aid station available during summer."
    },
    "photoSpots":"The eastern end of the beach (toward Xiaomeisha) offers the best sunrise views. The boardwalk above the beach is ideal for wide panorama shots. The rock formations at the far east end make for dramatic foreground elements at golden hour.",
    "bestTimeToVisit":"Weekday mornings (any season) for empty beach. May and October for warm water + manageable crowds. September weekday mornings are the absolute sweet spot."
  },
  {
    "id":"xichong","name":"Xichong","nameCN":"西涌","distance":"75 min","fee":"30 RMB","feeNum":30,
    "bestFor":["Surfing","Camping","Photography"],"rating":4.5,"crowdLevel":"quiet","crowdLabel":"Quiet on weekdays",
    "location":[22.4857,114.5595],"slug":"xichong",
    "description":"Shenzhen longest beach at 4km, and its best surf spot. Untamed, scenic, and worth the extra travel time. Backed by green hills and home to a growing surf community.",
    "longDescription":"Xichong (西涌, also written as Xichong) is Shenzhen's crown jewel for anyone who wants more than a quick dip. At 4 kilometers long, it's by far the longest beach in the city, and its exposed position facing the South China Sea means it catches the best waves in the region.\n\nThis is where Shenzhen's surf culture lives. A dozen surf shops line the road behind the beach, offering board rentals (around 100 RMB per hour) and lessons for beginners. The best surf is during typhoon season (July through October), when distant storms send clean swells into the bay. On a good day, you'll see 20-30 surfers in the water.\n\nThe beach itself is wilder than Dameisha or Xiaomeisha — coarser golden sand, fewer facilities, and a more natural feel. The hills behind the beach are covered in subtropical forest, and the lack of high-rise development means the night sky here is actually dark enough for stargazing.\n\nCamping is one of Xichong's biggest draws. Designated camping areas near the beach allow tents, and several local operators rent gear if you don't have your own. Falling asleep to the sound of waves and waking up to an empty beach before the day-trippers arrive is worth the extra effort to get here.\n\nXichong is also the starting (or ending) point for the famous Dongchong-Xichong coastal hiking trail, a stunning 8 km clifftop path that ranks among the best day hikes near Shenzhen.",
    "openingHours":"24 hours (beach area). Swimming recommended during daylight only.",
    "familyFriendly":False,
    "accessibility":"Limited. Sand is softer and harder to navigate. No wheelchair ramps. Not recommended for visitors with mobility challenges.",
    "transport":{
      "bus":"E11 express bus from downtown to Nanao (南澳) terminus (~1 hour, ~10 RMB), then transfer to M232 local bus to Xichong (~30 min, ~3 RMB)",
      "taxiFromFutian":"~180 RMB (75 min)","taxiFromLuohu":"~140 RMB (60 min)","taxiFromNanshan":"~200 RMB (90 min)",
      "driveTime":"60-75 min from city center","parking":"Several lots near the beach entrances (there are 4 entrance points). ~30 RMB/day. Fills on summer weekends by 10:30 AM."
    },
    "facilities":{"showers":"15 RMB","lockers":"20 RMB","umbrellas":"60 RMB/day","lifeguards":"Seasonal, limited coverage. Flag system used.","food":"Beachside BBQ restaurants, local seafood. Small shops selling drinks and snacks.","restrooms":"Available near each entrance","changingRooms":"Basic, near shower areas","firstAid":"Limited. Nearest clinic in Xichong village (5 min drive)."},
    "features":{"sandType":"Coarse golden sand, 4 km long stretch","waterQuality":"Grade I-II (generally very good, tested monthly)","waveType":"Moderate, suitable for surfing and bodyboarding. Best surf during typhoon season (Jul-Oct).","bestSeason":"May-October for swimming, July-October for surfing","swimZone":"Designated swimming areas marked by flags. Swim between the red and yellow flags."},
    "food":{
      "onSite":"A strip of casual beachside restaurants and BBQ joints behind the beach. Fresh seafood is the specialty — most places have tanks where you pick your fish/crab/shrimp. Grilled skewers, fried rice, and cold beer are staples. Expect 80-150 RMB per person for a solid meal.",
      "nearby":"Xichong village (5 min walk from the beach) has more local restaurants, noodle shops, and convenience stores. No Western chain restaurants in the area.",
      "mustTry":"BBQ seafood platter (海鲜烧烤拼盘), salt and pepper squid (椒盐鱿鱼), cold Tsingtao beer watching the sunset",
      "priceRange":"Beachside meal: 80-150 RMB per person. Seafood dinner: 150-300 RMB. Snacks and drinks: 10-40 RMB."
    },
    "accommodation":{
      "nearby":"Xichong Surf Club guesthouse (from ~250 RMB/night, surf-themed, board storage). Several family-run guesthouses and B&Bs in the village (150-400 RMB/night). No international chain hotels.",
      "camping":"Yes! Designated camping areas near the beach. Bring your own tent (~20 RMB camping fee) or rent from local operators (~80-150 RMB for tent + sleeping bag). Campfires generally not permitted. Book ahead on summer weekends.",
      "priceRange":"Camping: 20-150 RMB. Guesthouse: 150-400 RMB. No luxury options in immediate area."
    },
    "clothing":{
      "summer":"Surf gear if you're surfing (rash guard, board shorts). Otherwise: swimsuit, flip-flops, sun hat, sunglasses. Bring a light jacket for evening — it gets breezy. Reef-safe sunscreen recommended.",
      "winter":"Warmer layers needed than city beaches. Coastal wind can be strong. Hoodie, windbreaker, long pants. Water temperature drops to 16-18°C — wetsuit needed for surfing.",
      "essentials":["Sunscreen (SPF 50+, reef-safe)","Insect repellent (mosquitoes at dusk)","Cash (limited mobile payment in some shops)","Power bank (limited charging options)","Headlamp or flashlight (for camping and evening walks)","Water shoes (some rocky sections)","Tent if camping","Towel and change of clothes"]
    },
    "activities":[
      {"name":"Surfing","desc":"The best surf in Shenzhen. Multiple surf shops offering board rental (~100 RMB/hr) and lessons (~300-400 RMB for 2 hours). Best waves July-October. Beginner-friendly sections near beach entrances 1-2."},
      {"name":"Camping","desc":"Designated camping zones with basic facilities. Wake up to an empty beach and morning surf. Bring your own gear or rent locally."},
      {"name":"Coastal Hiking","desc":"The Dongchong-Xichong trail starts/ends here. 8 km, 3-4 hours one way. Stunning cliff views. Moderately challenging — good shoes essential. Carry water."},
      {"name":"Photography","desc":"Long beach + hills behind = incredible golden hour light. Best spots: the rocky outcrop at the eastern end, the hillside trail for elevated beach panoramas, and the surf break for action shots."},
      {"name":"Stargazing","desc":"Far from city lights, Xichong has the darkest skies near Shenzhen. Bring a blanket and lie on the beach after dark. Milky Way visible on clear nights."}
    ],
    "safety":{
      "lifeguardHours":"Seasonal, typically 09:00-18:00 during summer. Flag system: swim between red and yellow flags only.",
      "hazards":"Rip currents can occur, especially near the rocky ends of the beach. Jellyfish in late summer. Strong UV exposure — the open beach has no natural shade. Typhoons can create dangerous conditions — check weather before going.",
      "waterQualitySource":"Shenzhen Ecology Bureau monthly report. Grade I-II = among the cleanest in Shenzhen. Water quality generally better than city beaches due to less runoff.",
      "emergencyContact":"Nearest hospital: Dapeng New District People's Hospital (~30 min drive). Beach emergency: 110."
    },
    "photoSpots":"Eastern end of the beach (near entrance 4) for sunrise and empty sand. The rocky headland at the far east for dramatic foreground. The hillside trail looking back at the beach for the classic 4 km panorama. Late afternoon light on the surf break near entrance 2.",
    "bestTimeToVisit":"Weekdays for empty beach. September-October for best combo of warm water + clean waves + manageable crowds. July-August for best surf. Avoid summer weekends and all national holidays."
  },
  {
    "id":"xiaomeisha","name":"Xiaomeisha","nameCN":"小梅沙","distance":"40 min","fee":"50 RMB","feeNum":50,
    "bestFor":["Resort day","Families","Water activities"],"rating":4.1,"crowdLevel":"moderate","crowdLabel":"Moderate year-round",
    "location":[22.6035,114.3247],"slug":"xiaomeisha",
    "description":"A redeveloped resort beach next to Dameisha, with upgraded facilities and a more managed experience. Home to Xiaomeisha Sea World and several resort hotels.",
    "longDescription":"Xiaomeisha (小梅沙) is Dameisha's more polished sibling — smaller, cleaner, and managed as part of a resort complex. After a major redevelopment completed in recent years, the beach now offers higher-quality facilities than any other public beach in Shenzhen.\n\nThe beach is about 800 meters long with fine, well-maintained white sand. The bay is more protected than Dameisha's, so the water is calmer — great for families with small children. The entry fee (50 RMB) keeps the crowds slightly more manageable than Dameisha's free-for-all, though it still gets busy on summer weekends.\n\nXiaomeisha's biggest advantage is its integration with the surrounding resort area. The Xiaomeisha Sea World (小梅沙海洋世界) is right next door — a large aquarium and marine park that makes a great combo with a beach day. Several resort hotels, including an InterContinental, line the waterfront, and day passes with pool access are available even if you're not staying overnight.\n\nThe beach offers more structured activities than the wilder eastern beaches: jet ski rentals, banana boat rides, and organized beach games are common. If you want a beach day with resort-level comfort and zero hassle, Xiaomeisha delivers.",
    "openingHours":"08:00-21:00 (summer), 08:30-18:00 (winter). Last entry 1 hour before closing.",
    "familyFriendly":True,
    "accessibility":"Good. Paved paths to the beach. Accessible restrooms. Beach wheelchairs available at resort reception.",
    "transport":{
      "metro":"Line 8","metroExit":"Exit B","metroWalk":"15 min walk or short taxi (starting fare)",
      "bus":"103, 387, M362, M438",
      "taxiFromFutian":"~90 RMB (45 min)","taxiFromLuohu":"~60 RMB (30 min)","taxiFromNanshan":"~120 RMB (55 min)",
      "driveTime":"35-45 min from city center","parking":"Resort parking, ~30 RMB/day. More spaces than Dameisha. Underground parking available at InterContinental."
    },
    "facilities":{"showers":"Included with entry fee","lockers":"30 RMB","umbrellas":"80 RMB/day (resort quality)","lifeguards":"09:00-21:00 (summer), well-staffed","food":"Resort restaurants, cafes, snack bars. Higher quality than Dameisha.","restrooms":"Clean, well-maintained, resort-standard","changingRooms":"Air-conditioned, included with entry","firstAid":"On-site medical station"},
    "features":{"sandType":"Fine white sand, well-maintained and raked daily, ~800m long","waterQuality":"Grade II (regularly tested, good consistency)","waveType":"Gentle, very protected bay. Calmest of all Shenzhen beaches.","bestSeason":"Year-round, best May-October for swimming","swimZone":"Well-marked swimming areas. Multiple lifeguard stations."},
    "food":{
      "onSite":"Resort cafes and beach bars serving Western and Chinese food. InterContinental resort has multiple restaurants (Chinese, international buffet, poolside grill). Beach vendors sell drinks, ice cream, and light snacks.",
      "nearby":"Xiaomeisha commercial area (5 min walk) has more restaurants. Sea World complex has food courts and cafes. Dameisha's restaurant strip is 10 min walk away.",
      "mustTry":"Poolside cocktails at the InterContinental. Resort dim sum brunch on weekends. Fresh coconut by the beach.",
      "priceRange":"Beach snacks: 20-60 RMB. Resort restaurant: 150-400 RMB per person. InterContinental buffet: ~300 RMB per person."
    },
    "accommodation":{
      "nearby":"InterContinental Shenzhen Dameisha Resort (5-star, from ~1000 RMB/night, direct beach access, pool). Several mid-range resort hotels (400-800 RMB/night). Holiday Inn Express Dameisha (from ~350 RMB/night).",
      "camping":"Not permitted at Xiaomeisha.",
      "priceRange":"Mid-range: 350-600 RMB. Resort: 800-2000 RMB."
    },
    "clothing":{
      "summer":"Swimsuit, cover-up for walking between beach and resort. Resort dress code is casual but not beachwear in restaurants. Flip-flops fine for beach, sandals or casual shoes for resort areas.",
      "winter":"Light layers. Resort areas are well-sheltered from wind. Heated pools at some resorts extend the swimming season.",
      "essentials":["Sunscreen","Swimsuit","Cover-up or light dress for resort areas","Phone/camera (safe environment for valuables)","Cash or mobile payment for beach vendors","Resort day pass if not staying overnight"]
    },
    "activities":[
      {"name":"Swimming","desc":"Calm, protected water. Ideal for casual swimming and families with young children. Multiple lifeguard stations."},
      {"name":"Water Sports","desc":"Jet ski rentals (~200 RMB/15 min). Banana boat rides (~100 RMB/person). Parasailing available seasonally."},
      {"name":"Sea World Visit","desc":"Xiaomeisha Sea World next door. Aquarium, dolphin shows, underwater tunnel. ~200 RMB entry. Great rainy day backup plan."},
      {"name":"Resort Pool Day","desc":"Resort day passes (200-400 RMB) give access to pools, loungers, and facilities without staying overnight. Best value for a luxury beach day."},
      {"name":"Beach Yoga","desc":"Resorts occasionally offer morning beach yoga. Check with concierge. Alternatively, the wide smooth sand at low tide is perfect for DIY practice."}
    ],
    "safety":{
      "lifeguardHours":"09:00-21:00 (year-round, reduced hours in winter)",
      "hazards":"Very safe beach overall. Protected bay means minimal currents. Main risk is sun exposure — bring shade. Jellyfish rare but possible in late summer.",
      "waterQualitySource":"Resort-managed water quality testing in addition to Shenzhen Ecology Bureau monitoring. Consistently Grade II.",
      "emergencyContact":"On-site medical station. InterContinental has 24-hour doctor on call. Emergency: 110/120."
    },
    "photoSpots":"The western end of the beach looking toward Dameisha for sunset. The resort pool deck for infinity-pool-meets-ocean shots. Sea World's outdoor plaza for family photos. The jetty at the eastern end for fishing-boat-backdrop photos.",
    "bestTimeToVisit":"Weekdays year-round for uncrowded resort feel. May and October for perfect weather. Avoid summer weekends and Chinese holidays. Resort day pass on a Tuesday in September is peak Xiaomeisha experience."
  },
  {
    "id":"dongchong","name":"Dongchong","nameCN":"东涌","distance":"80 min","fee":"20 RMB","feeNum":20,
    "bestFor":["Hiking","Quiet escape","Nature"],"rating":4.3,"crowdLevel":"quiet","crowdLabel":"Usually quiet",
    "location":[22.4972,114.5806],"slug":"dongchong",
    "description":"A secluded gem next to Xichong, connected by a beautiful coastal hiking trail. Smaller and less developed, ideal for those who want peace and natural scenery.",
    "longDescription":"Dongchong (东涌, also Dong Chong) is Xichong's quieter neighbor — a smaller, more intimate beach that feels a world away from the city. If Xichong is where surfers go, Dongchong is where people go to escape the surfers.\n\nThe beach is about 1 kilometer long with coarser sand and a more rugged feel. The water quality here is among the best in Shenzhen (Grade I), thanks to minimal development and less runoff. On a weekday, you might share the entire beach with just a handful of other visitors.\n\nDongchong's real claim to fame is the Dongchong-Xichong coastal hiking trail. This 8 km path traces the coastline between the two beaches, climbing over headlands and dipping into hidden coves. The views are spectacular — turquoise water, dramatic cliffs, and in spring, wildflowers covering the hillsides. The hike takes 3-4 hours and is moderately challenging with some steep sections.\n\nThe village behind the beach is small and traditional — a few family-run restaurants, basic guesthouses, and not much else. This is not a place for resort amenities. It's a place for sitting on the sand with a book, hiking until your legs are tired, and eating fresh seafood that was swimming an hour ago.",
    "openingHours":"Daylight hours. No formal closing time but facilities close by 18:00.",
    "familyFriendly":False,
    "accessibility":"Not accessible. Uneven paths, no ramps, basic facilities.",
    "transport":{
      "bus":"E11 express to Nanao (南澳) terminus, then M231 local bus to Dongchong (~40 min). Buses run less frequently than to Xichong.",
      "taxiFromFutian":"~190 RMB (80 min)","taxiFromLuohu":"~150 RMB (65 min)","taxiFromNanshan":"~210 RMB (95 min)",
      "driveTime":"65-80 min from city center","parking":"Small lot near beach, ~20 RMB/day. Very limited — maybe 30 spots. Park in the village and walk if full."
    },
    "facilities":{"showers":"10 RMB (basic)","lockers":"Limited availability","lifeguards":"Seasonal, limited","food":"A few local seafood restaurants, basic snack shop","restrooms":"Basic, near entrance","changingRooms":"None","firstAid":"None on-site"},
    "features":{"sandType":"Coarse sand with pebbles in some areas, ~1 km long","waterQuality":"Grade I (excellent, less runoff than other beaches)","waveType":"Moderate, less protected than Xichong","bestSeason":"April-November","swimZone":"Limited marked area"},
    "food":{"onSite":"A handful of family-run seafood restaurants (3-4 options). Fresh catch of the day, simple preparation. A small shop selling drinks, instant noodles, and basic snacks.","nearby":"More restaurant options in Dongchong village (10 min walk). Nanao town (20 min drive) has the best seafood market and restaurants in the area.","mustTry":"Steamed fish with ginger and scallion (清蒸鱼), stir-fried clams with chili (辣炒花蛤), cold beer on the beach","priceRange":"Beach restaurant: 60-120 RMB per person. Very affordable compared to city beaches."},
    "accommodation":{"nearby":"A few basic guesthouses in Dongchong village (100-250 RMB/night). No chain hotels. Some rooms in private homes available on Chinese booking platforms.","camping":"Possible but less organized than Xichong. Ask local guesthouse owners. Bring all gear.","priceRange":"Guesthouse: 100-250 RMB. Very budget-friendly."},
    "clothing":{"summer":"Swimsuit, hiking shoes or sturdy sandals for the trail, sun hat, sunscreen. Quick-dry clothing if doing the hike. Bring a light jacket for the evening coastal breeze.","winter":"Windbreaker essential — exposed location. Layers for hiking. Water too cold for swimming without wetsuit. Great hiking weather.","essentials":["Sunscreen","Insect repellent","Cash (no ATMs, limited mobile payment)","Water (2L minimum for hiking)","Hiking shoes","Power bank","Snacks (limited purchase options)","First aid kit for hiking"]},
    "activities":[{"name":"Coastal Hiking","desc":"The main reason to visit. Dongchong-Xichong trail: 8 km, 3-4 hours, moderate difficulty. Stunning clifftop ocean views. Start early to avoid midday heat. Download offline maps."},{"name":"Swimming","desc":"Clean water, but limited lifeguard coverage. Swim with caution. The water is clearer than city beaches."},{"name":"Photography","desc":"The coastal trail offers the best photo opportunities. Dramatic cliffs, turquoise water, wild coastline. The beach itself is photogenic at sunrise when the light hits the eastern hills."},{"name":"Quiet Relaxation","desc":"This is the best beach near Shenzhen for doing absolutely nothing. Bring a book, find a spot, and enjoy the sound of waves without crowds."}],
    "safety":{"lifeguardHours":"Limited and seasonal. Do not rely on lifeguard presence.","hazards":"Rip currents possible. Slippery rocks. Trail sections can be dangerous in wet weather. No mobile signal on some trail sections.","waterQualitySource":"Grade I = excellent. Best water quality among Shenzhen beaches.","emergencyContact":"Nearest medical help in Nanao (20 min drive). Carry a first aid kit. Emergency: 110/120."},
    "photoSpots":"The trail overlook looking back at Dongchong beach — the classic shot. Sunrise from the eastern headland. The rocky shoreline at the western end. The trail itself with ocean backdrop.",
    "bestTimeToVisit":"Weekdays for solitude. April-May and October-November for best hiking weather. Avoid summer weekends. Winter weekdays for empty beach walks."
  }
]

# Write enhanced data
with open(os.path.join(base, "data", "beaches.json"), "w", encoding="utf-8") as f:
    json.dump(beaches, f, ensure_ascii=False, indent=2)
print("  Enhanced beaches.json with 衣食住行 data")
print(f"  Beaches with full data: {', '.join(b['name'] for b in beaches)}")
print(f"  Beaches need full 衣食住行: yangmeikeng, jinshawan, judiaosha, nanao, shuitousha, shangdong")
