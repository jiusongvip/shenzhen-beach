import os, json
base = r"D:\workspaces\website\shenzhen-beach\src"

# ===== DYNAMIC DETAIL PAGE TEMPLATE =====
template = """---
import Layout from "../../layouts/Layout.astro";
import Nav from "../../components/Nav.astro";
import Footer from "../../components/Footer.astro";
import beaches from "../../data/beaches.json";

export function getStaticPaths() {
  return beaches.map(b => ({ params: { slug: b.slug } }));
}

const { slug } = Astro.params;
const b = beaches.find(x => x.slug === slug);
if (!b) throw new Error("Beach not found: " + slug);

const pageTitle = b.name + " Beach (" + b.nameCN + ") \\u2014 Transport, Food, Hotels & Tips";
const pageDesc = "Complete guide to " + b.name + " Beach in Shenzhen: how to get there, entrance fee, opening hours, food & dining, nearby hotels, activities, safety tips, and what to wear. Updated August 2026.";

const similar = beaches.filter(x => x.id !== b.id && x.bestFor.some(t => b.bestFor.includes(t))).slice(0, 3);
---

<Layout title={pageTitle} description={pageDesc}>
  <Nav />
  <main class="max-w-4xl mx-auto px-4 py-8 md:py-12">
    <!-- Breadcrumb -->
    <nav class="text-sm text-gray-400 mb-6" aria-label="Breadcrumb">
      <a href="/" class="hover:text-ocean transition-colors">Shenzhen Beaches</a>
      <span class="mx-2">/</span>
      <span class="text-gray-600">{b.name} Beach</span>
    </nav>

    <!-- Hero -->
    <div class="mb-10">
      <div class="flex flex-wrap items-baseline gap-3">
        <h1 class="text-3xl md:text-4xl font-bold tracking-tight text-gray-900">{b.name} Beach</h1>
        <span class="text-xl text-gray-400">{b.nameCN}</span>
      </div>
      <div class="flex flex-wrap items-center gap-4 mt-3 text-sm">
        <span class="inline-flex items-center gap-1"><svg width="14" height="14" viewBox="0 0 24 24" fill="#e0683a"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>{b.rating}</span>
        <span class="text-gray-600">{b.distance} from city</span>
        <span class="text-gray-600">{b.fee}</span>
        <span class="text-gray-600">{b.crowdLabel}</span>
      </div>
    </div>

    <!-- Quick Info Card -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 mb-10 p-5 bg-sand rounded-xl border border-gray-200">
      <div><span class="text-xs text-gray-400 uppercase tracking-wider block mb-1">Opening Hours</span><span class="text-sm font-semibold text-gray-800">{b.openingHours}</span></div>
      <div><span class="text-xs text-gray-400 uppercase tracking-wider block mb-1">Entry Fee</span><span class="text-sm font-semibold text-gray-800">{b.fee}</span></div>
      <div><span class="text-xs text-gray-400 uppercase tracking-wider block mb-1">Water Quality</span><span class="text-sm font-semibold text-gray-800">{b.features.waterQuality.split("(")[0].strip()}</span></div>
      <div><span class="text-xs text-gray-400 uppercase tracking-wider block mb-1">Family Friendly</span><span class="text-sm font-semibold text-gray-800">{b.familyFriendly ? "Yes" : "Not ideal"}</span></div>
    </div>

    <!-- Overview -->
    <section class="mb-12">
      <h2 class="text-2xl font-bold tracking-tight text-gray-900 mb-4">Overview</h2>
      <div class="prose max-w-none text-gray-600 leading-relaxed space-y-3">
        {b.longDescription.split("\\n\\n").map(p => <p>{p}</p>)}
      </div>
    </section>

    <!-- Transport (行) -->
    <section class="mb-12">
      <h2 class="text-2xl font-bold tracking-tight text-gray-900 mb-4">How to Get to {b.name} Beach</h2>
      <div class="bg-white border border-gray-200 rounded-xl overflow-hidden">
        <dl class="divide-y divide-gray-100">
          {b.transport.metro && <div class="grid grid-cols-3 px-5 py-3"><dt class="text-sm font-medium text-gray-500">Metro</dt><dd class="col-span-2 text-sm text-gray-800">{b.transport.metro} ({b.transport.metroExit}) \\u2014 {b.transport.metroWalk}</dd></div>}
          {b.transport.bus && <div class="grid grid-cols-3 px-5 py-3"><dt class="text-sm font-medium text-gray-500">Bus</dt><dd class="col-span-2 text-sm text-gray-800">{b.transport.bus}</dd></div>}
          {b.transport.taxiFromFutian && <div class="grid grid-cols-3 px-5 py-3"><dt class="text-sm font-medium text-gray-500">Taxi from Futian</dt><dd class="col-span-2 text-sm text-gray-800">{b.transport.taxiFromFutian}</dd></div>}
          {b.transport.taxiFromLuohu && <div class="grid grid-cols-3 px-5 py-3"><dt class="text-sm font-medium text-gray-500">Taxi from Luohu</dt><dd class="col-span-2 text-sm text-gray-800">{b.transport.taxiFromLuohu}</dd></div>}
          {b.transport.taxiFromNanshan && <div class="grid grid-cols-3 px-5 py-3"><dt class="text-sm font-medium text-gray-500">Taxi from Nanshan</dt><dd class="col-span-2 text-sm text-gray-800">{b.transport.taxiFromNanshan}</dd></div>}
          {b.transport.driveTime && <div class="grid grid-cols-3 px-5 py-3"><dt class="text-sm font-medium text-gray-500">Driving</dt><dd class="col-span-2 text-sm text-gray-800">{b.transport.driveTime}</dd></div>}
          {b.transport.parking && <div class="grid grid-cols-3 px-5 py-3"><dt class="text-sm font-medium text-gray-500">Parking</dt><dd class="col-span-2 text-sm text-gray-800">{b.transport.parking}</dd></div>}
        </dl>
      </div>
    </section>

    <!-- Food (食) -->
    <section class="mb-12">
      <h2 class="text-2xl font-bold tracking-tight text-gray-900 mb-4">Food & Dining</h2>
      <div class="grid md:grid-cols-2 gap-6">
        <div class="bg-white border border-gray-200 rounded-xl p-5">
          <h3 class="font-semibold text-ocean mb-2">At the Beach</h3>
          <p class="text-sm text-gray-600">{b.food.onSite}</p>
        </div>
        <div class="bg-white border border-gray-200 rounded-xl p-5">
          <h3 class="font-semibold text-ocean mb-2">Nearby</h3>
          <p class="text-sm text-gray-600">{b.food.nearby}</p>
        </div>
      </div>
      <div class="mt-4 bg-accent/5 border border-accent/20 rounded-xl p-5">
        <h3 class="font-semibold text-accent mb-1">What to Try</h3>
        <p class="text-sm text-gray-700">{b.food.mustTry}</p>
        <p class="text-xs text-gray-500 mt-2">Price range: {b.food.priceRange}</p>
      </div>
    </section>

    <!-- Accommodation (住) -->
    <section class="mb-12">
      <h2 class="text-2xl font-bold tracking-tight text-gray-900 mb-4">Where to Stay</h2>
      <div class="bg-white border border-gray-200 rounded-xl p-5">
        <p class="text-sm text-gray-600">{b.accommodation.nearby}</p>
      </div>
      {b.accommodation.camping !== "Not permitted" && b.accommodation.camping !== "Not permitted at Dameisha." && b.accommodation.camping !== "Not permitted at Xiaomeisha." && <div class="mt-3 bg-amber-50 border border-amber-200 rounded-xl p-5"><h3 class="font-semibold text-amber-700 mb-1">Camping</h3><p class="text-sm text-gray-700">{b.accommodation.camping}</p></div>}
      <p class="text-xs text-gray-400 mt-3">Price range: {b.accommodation.priceRange}</p>
    </section>

    <!-- Clothing (衣) -->
    <section class="mb-12">
      <h2 class="text-2xl font-bold tracking-tight text-gray-900 mb-4">What to Wear & Bring</h2>
      <div class="grid md:grid-cols-2 gap-6">
        <div class="bg-white border border-gray-200 rounded-xl p-5">
          <h3 class="font-semibold text-ocean mb-2">Summer (May-Oct)</h3>
          <p class="text-sm text-gray-600">{b.clothing.summer}</p>
        </div>
        <div class="bg-white border border-gray-200 rounded-xl p-5">
          <h3 class="font-semibold text-ocean mb-2">Winter (Nov-Apr)</h3>
          <p class="text-sm text-gray-600">{b.clothing.winter}</p>
        </div>
      </div>
      <div class="mt-4 bg-white border border-gray-200 rounded-xl p-5">
        <h3 class="font-semibold text-ocean mb-2">Packing Checklist</h3>
        <ul class="grid sm:grid-cols-2 gap-2 text-sm text-gray-600">
          {b.clothing.essentials.map(e => <li class="flex gap-2"><span class="text-accent">\\u2713</span> {e}</li>)}
        </ul>
      </div>
    </section>

    <!-- Facilities -->
    <section class="mb-12">
      <h2 class="text-2xl font-bold tracking-tight text-gray-900 mb-4">Facilities</h2>
      <div class="bg-white border border-gray-200 rounded-xl overflow-hidden">
        <dl class="divide-y divide-gray-100">
          {b.facilities.showers && b.facilities.showers !== "None" && <div class="grid grid-cols-3 px-5 py-3"><dt class="text-sm font-medium text-gray-500">Showers</dt><dd class="col-span-2 text-sm text-gray-800">{b.facilities.showers}</dd></div>}
          {b.facilities.lockers && b.facilities.lockers !== "None" && <div class="grid grid-cols-3 px-5 py-3"><dt class="text-sm font-medium text-gray-500">Lockers</dt><dd class="col-span-2 text-sm text-gray-800">{b.facilities.lockers}</dd></div>}
          {b.facilities.changingRooms && b.facilities.changingRooms !== "None" && <div class="grid grid-cols-3 px-5 py-3"><dt class="text-sm font-medium text-gray-500">Changing Rooms</dt><dd class="col-span-2 text-sm text-gray-800">{b.facilities.changingRooms}</dd></div>}
          {b.facilities.umbrellas && <div class="grid grid-cols-3 px-5 py-3"><dt class="text-sm font-medium text-gray-500">Umbrellas/Chairs</dt><dd class="col-span-2 text-sm text-gray-800">{b.facilities.umbrellas}</dd></div>}
          {b.facilities.lifeguards && b.facilities.lifeguards !== "No" && <div class="grid grid-cols-3 px-5 py-3"><dt class="text-sm font-medium text-gray-500">Lifeguards</dt><dd class="col-span-2 text-sm text-gray-800">{b.facilities.lifeguards}</dd></div>}
          {b.facilities.restrooms && b.facilities.restrooms !== "None" && b.facilities.restrooms !== "None on-site" && <div class="grid grid-cols-3 px-5 py-3"><dt class="text-sm font-medium text-gray-500">Restrooms</dt><dd class="col-span-2 text-sm text-gray-800">{b.facilities.restrooms}</dd></div>}
          {b.facilities.firstAid && <div class="grid grid-cols-3 px-5 py-3"><dt class="text-sm font-medium text-gray-500">First Aid</dt><dd class="col-span-2 text-sm text-gray-800">{b.facilities.firstAid}</dd></div>}
        </dl>
      </div>
    </section>

    <!-- Activities -->
    <section class="mb-12">
      <h2 class="text-2xl font-bold tracking-tight text-gray-900 mb-4">Things to Do</h2>
      <div class="space-y-4">
        {b.activities.map(a => (
          <div class="bg-white border border-gray-200 rounded-xl p-5">
            <h3 class="font-semibold text-gray-800 mb-1">{a.name}</h3>
            <p class="text-sm text-gray-600">{a.desc}</p>
          </div>
        ))}
      </div>
    </section>

    <!-- Safety -->
    <section class="mb-12">
      <h2 class="text-2xl font-bold tracking-tight text-gray-900 mb-4">Safety</h2>
      <div class="bg-white border border-gray-200 rounded-xl p-5 space-y-3">
        <div><span class="text-sm font-medium text-gray-500">Lifeguard Hours: </span><span class="text-sm text-gray-800">{b.safety.lifeguardHours}</span></div>
        <div><span class="text-sm font-medium text-gray-500">Hazards: </span><span class="text-sm text-gray-800">{b.safety.hazards}</span></div>
        <div><span class="text-sm font-medium text-gray-500">Water Quality: </span><span class="text-sm text-gray-800">{b.safety.waterQualitySource}</span></div>
        <div><span class="text-sm font-medium text-gray-500">Emergency: </span><span class="text-sm text-gray-800">{b.safety.emergencyContact}</span></div>
      </div>
    </section>

    <!-- Photo Spots -->
    <section class="mb-12">
      <h2 class="text-2xl font-bold tracking-tight text-gray-900 mb-4">Photo Spots</h2>
      <p class="text-gray-600 text-sm leading-relaxed">{b.photoSpots}</p>
    </section>

    <!-- Best Time -->
    <section class="mb-12">
      <h2 class="text-2xl font-bold tracking-tight text-gray-900 mb-4">Best Time to Visit</h2>
      <div class="bg-ocean/5 border border-ocean/20 rounded-xl p-5">
        <p class="text-sm text-gray-700">{b.bestTimeToVisit}</p>
      </div>
    </section>

    <!-- Tips -->
    <section class="mb-12">
      <h2 class="text-2xl font-bold tracking-tight text-gray-900 mb-4">Visitor Tips</h2>
      <ul class="space-y-2">
        {b.tips.map((t,i) => <li key={i} class="flex gap-2 text-sm text-gray-600"><span class="text-accent shrink-0 mt-0.5">\\u2022</span> {t}</li>)}
      </ul>
    </section>

    <!-- Similar Beaches -->
    {similar.length > 0 && (
      <section class="mb-12">
        <h2 class="text-2xl font-bold tracking-tight text-gray-900 mb-4">You Might Also Like</h2>
        <div class="grid sm:grid-cols-3 gap-4">
          {similar.map(s => (
            <a href={`/beaches/${s.slug}/`} class="block bg-white border border-gray-200 rounded-xl p-4 hover:border-accent hover:shadow-sm transition-all no-underline">
              <span class="font-semibold text-gray-800">{s.name}</span>
              <span class="text-xs text-gray-400 ml-1">{s.nameCN}</span>
              <p class="text-xs text-gray-500 mt-1">{s.bestFor.slice(0,2).join(", ")}</p>
              <p class="text-xs text-gray-400 mt-2">\\u2605 {s.rating} \\u00b7 {s.fee}</p>
            </a>
          ))}
        </div>
      </section>
    )}

    <div class="mt-12 pt-8 border-t border-gray-200">
      <a href="/" class="text-sm text-ocean hover:underline inline-flex items-center gap-1">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"/></svg>
        Back to all Shenzhen beaches
      </a>
    </div>
  </main>
  <Footer />
</Layout>
"""

# Write the template
with open(os.path.join(base, "pages", "beaches", "[slug].astro"), "w", encoding="utf-8") as f:
    f.write(template)
print("  OK: [slug].astro template (衣食住行 + safety + activities + photo spots)")

# Remove old individual detail pages
for old in ["dameisha.astro", "xichong.astro", "xiaomeisha.astro"]:
    p = os.path.join(base, "pages", "beaches", old)
    if os.path.exists(p): os.remove(p); print(f"  Removed old: {old}")

print("\\nDetail page template complete. All 10 beaches will be generated from [slug].astro")
