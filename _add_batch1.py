import json, os
base = r"D:\workspaces\website\shenzhen-beach\src"
with open(os.path.join(base, "data", "beaches.json"), "r", encoding="utf-8") as f:
    beaches = json.load(f)

b1 = {
    "id":"yangmeikeng","name":"Yangmeikeng","nameCN":"\u6768\u6885\u5751","distance":"70 min","fee":"Free","feeNum":0,
    "bestFor":["Scenery","Cycling","Photography"],"rating":4.4,"crowdLevel":"moderate","crowdLabel":"Busy on holidays",
    "location":[22.5423,114.5612],"slug":"yangmeikeng",
    "description":"Famous for its scenic coastal road. Popular with cyclists and photographers. The beach is small but the coastal views are unmatched.",
    "longDescription":"Yangmeikeng is not really a beach destination - it is a coastal scenery destination that happens to have a beach. The main draw is the spectacular car-free coastal road winding along the Dapeng Peninsula, offering dramatic ocean views. Bike rentals (30-50 RMB/day) are available at the entrance. The road is closed to private cars, making it a cyclist paradise. At the far end is Lujiazui, a dramatic headland with cliff-edge walkways and some of the most Instagrammed spots in Shenzhen.",
    "openingHours":"24 hours (public road). Beach: daylight hours only.",
    "familyFriendly":True,"accessibility":"Coastal road is paved. Beach has uneven paths.",
    "transport":{"bus":"E11 express to Nanao, then local minibus to Yangmeikeng entrance (15 min, ~20 RMB)","taxiFromFutian":"~170 RMB (70 min)","taxiFromLuohu":"~130 RMB (55 min)","taxiFromNanshan":"~190 RMB (80 min)","driveTime":"55-70 min","parking":"Near entrance gate, ~25 RMB/day. Park and bike or walk the coastal road."},
    "facilities":{"showers":"10 RMB (basic)","lockers":"None","umbrellas":"None","lifeguards":"Limited","food":"Seaside restaurants at entrance area","restrooms":"Near entrance","changingRooms":"None","firstAid":"None"},
    "features":{"sandType":"Mixed sand and pebbles, ~300m","waterQuality":"Grade I-II","waveType":"Calm, protected inlet","bestSeason":"March-November","swimZone":"Informal swimming areas"},
    "food":{"onSite":"Casual seafood restaurants near the entrance. Fresh, simple, affordable. Grilled fish, stir-fried clams, cold beer. No chain restaurants.","nearby":"Dapeng town (20 min drive) for more options. Nanao seafood market (25 min).","mustTry":"Grilled whole fish, garlic scallops, fresh coconut, cold beer on a seaside terrace","priceRange":"Entrance restaurants: 60-120 RMB per person."},
    "accommodation":{"nearby":"Small guesthouses and B&Bs near entrance (150-300 RMB/night). Yangmeikeng Boutique Hotel (~400 RMB/night).","camping":"Not officially permitted. Some visitors camp discreetly at own risk.","priceRange":"Guesthouse: 150-400 RMB."},
    "clothing":{"summer":"Cycling gear: comfortable shorts, breathable top, sports shoes. Swimsuit if swimming. Sunscreen essential - coastal road has no shade.","winter":"Light jacket or windbreaker for cycling. Long pants. Cycling still pleasant in winter.","essentials":["Sunscreen","Sunglasses","Water bottle","Cash (small vendors)","Camera","Power bank","Bike rental cash (30-50 RMB)"]},
    "activities":[{"name":"Coastal Cycling","desc":"The main event. Rent a bike (30-50 RMB/day) and ride 7 km of car-free coastal road. Stunning views. Allow 2-3 hours round trip with photo stops."},{"name":"Photography","desc":"Best coastal photography near Shenzhen. Golden hour on the coastal road is magical. Lujiazui headland for dramatic cliff-edge shots."},{"name":"Seaside Dining","desc":"Restaurant terraces at the entrance with ocean views. Perfect lunch before or after cycling."}],
    "safety":{"lifeguardHours":"Not reliable. Swim at own risk.","hazards":"Sun exposure on shadeless road. Slippery rocks near water. Cliff edges at Lujiazui. Limited mobile signal.","waterQualitySource":"Grade I-II. Good quality from open ocean exposure.","emergencyContact":"Nearest clinic in Dapeng (20 min). Emergency: 110/120."},
    "photoSpots":"Coastal road at golden hour for winding-road-with-ocean shots. Lujiazui headland for cliff-and-sea compositions. Sunrise at the small beach. Restaurant terraces for lifestyle shots.",
    "bestTimeToVisit":"Clear weekday for empty roads. March-April for wildflowers. October-November for crisp air and golden light. Avoid summer weekends.",
    "tips":["Rent a bicycle - the coastal road is the main reason to visit","Go on a clear day for the best photos","The beach area is small; focus on the coastal road experience","Combine with nearby Dapeng Fortress"]
}

b2 = {
    "id":"jinshawan","name":"Jinshawan","nameCN":"\u91d1\u6c99\u6e7e","distance":"65 min","fee":"Free","feeNum":0,
    "bestFor":["Resort vibes","Sunbathing","Luxury"],"rating":4.3,"crowdLevel":"moderate","crowdLabel":"Mostly resort guests",
    "location":[22.5782,114.4658],"slug":"jinshawan",
    "description":"A newer, upscale beach area with international resort hotels. Cleaner and more curated than older beaches, with a relaxed atmosphere.",
    "longDescription":"Jinshawan (Golden Sand Bay) is Shenzhen newest and most upscale beach area. Unlike older beaches that grew organically, Jinshawan was developed as a planned resort zone with international hotel brands and manicured landscaping. The beach is about 1.5 km of fine golden sand, well-groomed and free of vendor clutter. The bay is protected, making for calm, safe swimming. Resort hotels offer day passes (200-400 RMB) for non-guests to access pools, loungers, and facilities. Beach bars serve proper cocktails, and restaurant quality is noticeably higher than at public beaches.",
    "openingHours":"24 hours (public beach). Resort facilities: check individual hours.",
    "familyFriendly":True,"accessibility":"Good. Resort-managed paths. Beach wheelchairs at Marriott.",
    "transport":{"bus":"E11 express to Dapeng center, then local bus or taxi (10 min) to Jinshawan","taxiFromFutian":"~160 RMB (65 min)","taxiFromLuohu":"~120 RMB (50 min)","taxiFromNanshan":"~180 RMB (75 min)","driveTime":"50-65 min","parking":"Resort parking, ~30-50 RMB/day."},
    "facilities":{"showers":"Free (resort-managed)","lockers":"At resorts","umbrellas":"Resort rental, ~100 RMB/day","lifeguards":"Yes, resort-managed year-round","food":"Resort restaurants, beach bars, cafes","restrooms":"Resort-standard","changingRooms":"Air-conditioned, resort-standard","firstAid":"Resort medical station"},
    "features":{"sandType":"Fine golden sand, well-groomed, ~1.5 km","waterQuality":"Grade II","waveType":"Gentle, protected bay","bestSeason":"Year-round, best April-October","swimZone":"Marked swimming areas"},
    "food":{"onSite":"Resort restaurants from casual poolside grills to fine dining. Beach bars with cocktails and light bites. Quality noticeably higher than public beaches.","nearby":"Dapeng town (10 min drive) has local restaurants. Dapeng Fortress area has courtyard restaurants in Ming Dynasty buildings.","mustTry":"Poolside cocktails at sunset. Resort dim sum brunch. Grilled seafood platter at beach bar.","priceRange":"Beach bar: 60-150 RMB. Resort restaurant: 150-400 RMB per person."},
    "accommodation":{"nearby":"Marriott Hotel Jinshawan (5-star, from ~900 RMB/night). Chinese luxury resorts (600-1200 RMB/night). Dapeng town guesthouses (150-300 RMB, 10 min drive).","camping":"Not permitted.","priceRange":"Budget: 150-300 RMB. Resort: 600-2000 RMB."},
    "clothing":{"summer":"Resort casual. Swimsuit, cover-up, sandals. Restaurants require cover-up and footwear. Nicer outfit for evening dining.","winter":"Light layers for beach walks. Resort pools may be heated.","essentials":["Sunscreen","Swimsuit","Cover-up","Resort day pass money (200-400 RMB)","Cash or card","Sunglasses and hat"]},
    "activities":[{"name":"Resort Pool Day","desc":"Day passes (200-400 RMB) for pools, loungers, towels, facilities. Best-value luxury beach experience near Shenzhen."},{"name":"Swimming","desc":"Clean, calm water with resort-managed lifeguards. Safer than public beaches."},{"name":"Sunbathing","desc":"Resort loungers and umbrellas. Well-maintained sand. Fewer people than public beaches."},{"name":"Beachside Dining","desc":"Proper restaurant dining with ocean views. Worth the premium for a special occasion."}],
    "safety":{"lifeguardHours":"Year-round, resort-managed. Most reliable lifeguard coverage.","hazards":"Very safe beach. Protected bay, minimal currents. Standard sun safety.","waterQualitySource":"Resort-managed testing + Ecology Bureau. Grade II.","emergencyContact":"Resort medical station on-site. Emergency: 110/120."},
    "photoSpots":"Resort pool deck for infinity-pool-meets-ocean. Western end of beach at sunset. Resort gardens. Beach bar at golden hour.",
    "bestTimeToVisit":"Weekdays for empty resort feel. May and October for perfect weather. Resort day pass on a Tuesday in shoulder season = peak Jinshawan.",
    "tips":["Stay at a resort hotel for the full experience","Public access is free but some facilities are resort-only","Best for a more polished beach experience","Less local character than Xichong or Dongchong"]
}

b3 = {
    "id":"judiaosha","name":"Judiaosha","nameCN":"\u6854\u9493\u6c99","distance":"70 min","fee":"Free","feeNum":0,
    "bestFor":["Romantic","Photography","Quiet retreat"],"rating":4.0,"crowdLevel":"quiet","crowdLabel":"Usually quiet",
    "location":[22.5567,114.5438],"slug":"judiaosha",
    "description":"A crescent-shaped beach with fine white sand, surrounded by lush hills. One of the most aesthetically beautiful beaches near Shenzhen.",
    "longDescription":"Judiaosha is a perfect crescent of fine white sand tucked between two green headlands. It looks more like a Thai island beach than something near Shenzhen. The sand is genuinely white (rare for Shenzhen), the water is crystal clear (Grade I), and the surrounding hills create genuine seclusion. Facilities are minimal: basic showers, a simple restroom, nothing else. No restaurants, no vendors, no jet skis. This is the beach for disconnecting. Bring everything, stay for golden hour, leave before dark.",
    "openingHours":"Daylight hours. No lighting or facilities after dark.",
    "familyFriendly":False,"accessibility":"Not accessible. Uneven path. No ramps.",
    "transport":{"bus":"E11 to Nanao, then local bus or taxi (15 min). Buses infrequent.","taxiFromFutian":"~175 RMB (70 min)","taxiFromLuohu":"~135 RMB (55 min)","taxiFromNanshan":"~195 RMB (80 min)","driveTime":"55-70 min","parking":"Limited roadside parking. Free but fills on weekends."},
    "facilities":{"showers":"Limited, basic (cold water only)","lockers":"None","umbrellas":"None","lifeguards":"Not always present","food":"None on the beach","restrooms":"Basic, one facility","changingRooms":"None","firstAid":"None"},
    "features":{"sandType":"Fine white sand, crescent shape, ~400m","waterQuality":"Grade I (excellent)","waveType":"Calm, shallow entry","bestSeason":"April-October","swimZone":"No formal swim zone"},
    "food":{"onSite":"Nothing. Zero food vendors. This is the most important thing to know.","nearby":"Nanao town (15 min drive) has excellent seafood. Pack a picnic.","mustTry":"DIY beach picnic. Stop at a market on the way. Fresh fruit, sandwiches, cold drinks eaten with feet in the sand.","priceRange":"BYO food. Nanao restaurant: 80-150 RMB per person."},
    "accommodation":{"nearby":"Nearest guesthouses in Nanao (15 min drive, 150-300 RMB/night). No hotels near the beach.","camping":"Not officially permitted. Some camp discreetly with zero facilities.","priceRange":"Guesthouse: 150-300 RMB."},
    "clothing":{"summer":"Swimsuit, full sun protection (no shade), water shoes for rocky edges. Bring umbrella or beach tent - no rentals.","winter":"Light layers for beach walks. Beautiful for photography and solitude.","essentials":["Everything. Seriously.","Water (2L+ per person)","Food (full picnic)","Sunscreen","Umbrella or beach tent","Trash bag","Cash","Camera","Towel"]},
    "activities":[{"name":"Swimming","desc":"Crystal clear water, gentle waves. Shallow entry. No lifeguards - swim with caution."},{"name":"Photography","desc":"One of the most photogenic beaches near Shenzhen. Crescent shape, white sand, green headlands. Golden hour is magical."},{"name":"Beach Picnic","desc":"Zero facilities means your picnic is the main event. Spread a blanket and enjoy one of Shenzhen most beautiful beaches almost alone."},{"name":"Sunbathing & Reading","desc":"The best beach for simply lying on the sand with a book. No vendors, no music, no announcements."}],
    "safety":{"lifeguardHours":"Not guaranteed. Assume no lifeguards.","hazards":"No shade. No facilities. Swim with caution. Limited mobile signal.","waterQualitySource":"Grade I = cleanest rating. Excellent water quality.","emergencyContact":"Nearest help in Nanao (15 min). Carry first aid kit. Emergency: 110/120."},
    "photoSpots":"Eastern headland looking back at crescent - classic shot. Golden hour (5-7 PM summer). Rocky sections at ends for foreground. Sunrise on empty beach.",
    "bestTimeToVisit":"Weekdays for solitude. October-November for best light + comfortable temp. Golden hour (4-7 PM) for photography. Avoid all summer weekends.",
    "tips":["Go during golden hour for stunning photos","Pack food, water, and shade - facilities are minimal","Swim with caution; lifeguards may not be on duty","One of the cleanest beaches in the area"]
}

beaches.extend([b1, b2, b3])
with open(os.path.join(base, "data", "beaches.json"), "w", encoding="utf-8") as f:
    json.dump(beaches, f, ensure_ascii=False, indent=2)
print(f"Added 3 beaches. Total: {len(beaches)}")
