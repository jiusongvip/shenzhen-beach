import os
base = r"D:\workspaces\website\shenzhen-beach\src"

# ===== 1. Layout: Add global script for chevrons + mobile nav + scroll-to-top =====
layout = """---
export interface Props { title: string; description: string }
const { title, description } = Astro.props
---
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content={description} />
  <title>{title}</title>
  <meta property="og:title" content={title} />
  <meta property="og:description" content={description} />
  <meta property="og:type" content="website" />
  <meta name="twitter:card" content="summary_large_image" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
  <style is:global>
    @import "../styles/global.css";
  </style>
  <script is:inline>
    // Shared behaviors across all pages
    document.addEventListener('DOMContentLoaded', () => {
      // Accordion chevron rotation
      document.querySelectorAll('[aria-expanded]').forEach(btn => {
        btn.addEventListener('click', function() {
          const svg = this.querySelector('svg');
          if (svg) svg.classList.toggle('rotate-180');
        });
      });
      // Mobile menu
      const menuBtn = document.getElementById('mobile-menu-btn');
      const mobileMenu = document.getElementById('mobile-menu');
      if (menuBtn && mobileMenu) {
        menuBtn.addEventListener('click', () => mobileMenu.classList.toggle('hidden'));
        mobileMenu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => mobileMenu.classList.add('hidden')));
      }
      // Scroll-to-top
      const topBtn = document.getElementById('back-to-top');
      if (topBtn) {
        window.addEventListener('scroll', () => {
          topBtn.classList.toggle('opacity-0', window.scrollY < 500);
          topBtn.classList.toggle('pointer-events-none', window.scrollY < 500);
        });
        topBtn.addEventListener('click', () => window.scrollTo({top:0,behavior:'smooth'}));
      }
    });
  </script>
</head>
<body class="min-h-[100dvh]">
  <slot />
  <button id="back-to-top" class="fixed bottom-6 right-6 z-50 w-10 h-10 rounded-full bg-accent text-white shadow-lg flex items-center justify-center opacity-0 pointer-events-none transition-opacity duration-300 hover:bg-accent-dark" aria-label="Back to top">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="18 15 12 9 6 15"/></svg>
  </button>
</body>
</html>"""

with open(os.path.join(base, "layouts", "Layout.astro"), "w", encoding="utf-8") as f:
    f.write(layout)
print("  OK: Layout.astro")

# ===== 2. Nav: Add mobile menu dropdown =====
nav = """---
const links = [
  { href: "#compare", label: "Compare" },
  { href: "#beaches", label: "Beaches" },
  { href: "#transport", label: "Transport" },
  { href: "#seasons", label: "Seasons" },
  { href: "#foreign", label: "Visitors" },
  { href: "#faq", label: "FAQ" },
];
---
<nav class="sticky top-0 z-50 bg-white/80 backdrop-blur-md border-b border-gray-200/60">
  <div class="max-w-7xl mx-auto px-4 h-16 flex items-center justify-between">
    <a href="/" class="text-lg font-semibold tracking-tight">
      <span class="text-accent">Shenzhen</span>Beaches
    </a>
    <div class="hidden md:flex items-center gap-6 text-sm font-medium">
      {links.map(link => (
        <a href={link.href} class="text-gray-600 hover:text-accent transition-colors">{link.label}</a>
      ))}
    </div>
    <button class="md:hidden text-gray-600" id="mobile-menu-btn" aria-label="Menu">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="4" y1="6" x2="20" y2="6"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="18" x2="20" y2="18"/></svg>
    </button>
  </div>
  <div id="mobile-menu" class="hidden md:hidden border-t border-gray-100 bg-white">
    <div class="px-4 py-3 flex flex-col gap-2">
      {links.map(link => (
        <a href={link.href} class="text-sm font-medium text-gray-600 hover:text-accent py-2 transition-colors">{link.label}</a>
      ))}
    </div>
  </div>
</nav>"""

with open(os.path.join(base, "components", "Nav.astro"), "w", encoding="utf-8") as f:
    f.write(nav)
print("  OK: Nav.astro (mobile menu)")

# ===== 3. Hero: Fix filter JS (visibility:collapse for tr rows) + better hero =====
hero = """---
---
<section id="quiz" class="min-h-[100dvh] flex items-center pt-16">
  <div class="max-w-7xl mx-auto px-4 w-full grid lg:grid-cols-2 gap-12 items-center">
    <div>
      <h1 class="text-4xl md:text-5xl lg:text-6xl font-bold tracking-tighter leading-[1.05] mb-6">
        Which Shenzhen Beach Is Right for You?
      </h1>
      <p class="text-lg text-gray-600 max-w-[48ch] mb-8 leading-relaxed">
        Compare 10 beaches in one place. Real photos, honest advice,
        transport guides, and everything you need to plan your perfect beach day.
      </p>
      <div class="flex flex-wrap gap-3" id="quick-filter">
        <button data-filter="Swimming" class="px-4 py-2 rounded-full border border-gray-300 text-sm font-medium hover:border-accent hover:text-accent transition-colors">Swimming</button>
        <button data-filter="Surfing" class="px-4 py-2 rounded-full border border-gray-300 text-sm font-medium hover:border-accent hover:text-accent transition-colors">Surfing</button>
        <button data-filter="Family" class="px-4 py-2 rounded-full border border-gray-300 text-sm font-medium hover:border-accent hover:text-accent transition-colors">Family</button>
        <button data-filter="Camping" class="px-4 py-2 rounded-full border border-gray-300 text-sm font-medium hover:border-accent hover:text-accent transition-colors">Camping</button>
        <button data-filter="Photography" class="px-4 py-2 rounded-full border border-gray-300 text-sm font-medium hover:border-accent hover:text-accent transition-colors">Photography</button>
        <button data-filter="all" class="px-4 py-2 rounded-full bg-accent text-white text-sm font-medium hover:bg-accent-dark transition-colors">Show all</button>
      </div>
      <p class="text-xs text-gray-400 mt-4">Tap a beach to see transport, facilities, photos, and tips</p>
    </div>
    <div class="relative aspect-[4/3] rounded-2xl overflow-hidden bg-gradient-to-br from-ocean/30 via-ocean/15 to-accent/20 flex items-center justify-center">
      <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_70%_60%,rgba(224,104,58,0.15),transparent_60%),radial-gradient(ellipse_at_30%_20%,rgba(26,95,122,0.2),transparent_50%)]"></div>
      <div class="relative z-10 text-center px-6">
        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#1a5f7a" stroke-width="1.5" class="mx-auto mb-3 opacity-60"><path d="M2 20h20M4 12c0-4.4 3.6-8 8-8s8 3.6 8 8v8H4v-8z"/></svg>
        <p class="text-ocean/70 text-sm font-medium">10 beaches. One page.<br/>Find yours in 60 seconds.</p>
      </div>
    </div>
  </div>
</section>
<script>
  document.querySelectorAll('#quick-filter button[data-filter]').forEach(btn => {
    btn.addEventListener('click', () => {
      const filter = btn.dataset.filter;
      document.querySelectorAll('#quick-filter button').forEach(b => { b.classList.remove('bg-accent','text-white'); });
      btn.classList.add('bg-accent','text-white');
      document.querySelectorAll('.beach-card').forEach(card => {
        if (filter === 'all' || (card.dataset.tags || '').includes(filter)) {
          card.style.visibility = '';
        } else {
          card.style.visibility = 'collapse';
        }
      });
    });
  });
</script>"""

with open(os.path.join(base, "components", "Hero.astro"), "w", encoding="utf-8") as f:
    f.write(hero)
print("  OK: Hero.astro (visibility fix + gradient hero)")

# ===== 4. FAQ: Fix JSON-LD schema with set:html =====
faq = """---
const faqs = [
  {q:"Which Shenzhen beach is the best?",a:"Depends on what you want. Xichong for surfing and scenery, Dameisha for convenience and families, Yangmeikeng for photography and cycling, Xiaomeisha for a resort experience. Use the comparison table above to find your match."},
  {q:"Are Shenzhen beaches free?",a:"Most are free, including Dameisha, Yangmeikeng, Jinshawan, Judiaosha, Nanao, Shuitousha, and Shangdong. Xichong charges 30 RMB, Dongchong 20 RMB, and Xiaomeisha 50 RMB (includes facilities)."},
  {q:"Can you swim at Shenzhen beaches?",a:"Yes. May through October is the main swimming season. Water quality varies and is published monthly by the Shenzhen Ecology Bureau. Xichong and Dongchong generally have the cleanest water."},
  {q:"How to get to Shenzhen beaches from Hong Kong?",a:"Take MTR East Rail to Lo Wu or Lok Ma Chau, cross the border, then metro Line 8 (for Dameisha/Xiaomeisha) or taxi (for eastern beaches). Total: 1.5-2.5 hours depending on destination."},
  {q:"When is the best time to visit Shenzhen beaches?",a:"September through November offers the best combination of warm water, clear skies, and manageable crowds. July and August are hottest but most crowded, especially weekends."},
  {q:"Are Shenzhen beaches clean?",a:"Water quality varies. Eastern beaches (Xichong, Dongchong, Judiaosha) generally have Grade I. City beaches (Dameisha, Xiaomeisha) are regularly tested and usually Grade II, safe for swimming."},
  {q:"Do I need to speak Chinese?",a:"At popular beaches like Dameisha, you can get by with English. At remote beaches, basic Chinese or a translation app helps. Use the language cards above for taxi drivers."},
  {q:"Is there surfing in Shenzhen?",a:"Yes. Xichong Beach is the main surf spot with consistent waves during typhoon season (Jul-Oct). Board rentals and lessons available from beachside shops. Dongchong also has surfable waves."}
];

const schemaObj = {
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": faqs.map(item => ({
    "@type": "Question",
    "name": item.q,
    "acceptedAnswer": { "@type": "Answer", "text": item.a }
  }))
};
const schemaJson = JSON.stringify(schemaObj);
---
<section id="faq" class="py-16 bg-white">
  <div class="max-w-3xl mx-auto px-4">
    <h2 class="text-2xl md:text-3xl font-bold tracking-tight mb-8 text-center">Frequently Asked Questions</h2>
    <div class="space-y-3">
      {faqs.map((item, i) => (
        <div class="border border-gray-200 rounded-xl overflow-hidden">
          <button class="w-full px-5 py-4 text-left flex items-center justify-between gap-4" data-target={`faq-${i}`} aria-expanded="false">
            <span class="font-medium text-gray-800">{item.q}</span>
            <svg class="w-5 h-5 text-gray-400 flex-shrink-0 transition-transform duration-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div id={`faq-${i}`} class="accordion-content">
            <div class="accordion-inner px-5 pb-4 text-gray-600 text-sm">{item.a}</div>
          </div>
        </div>
      ))}
    </div>
    <script type="application/ld+json" set:html={schemaJson}></script>
  </div>
</section>
"""

with open(os.path.join(base, "components", "FAQ.astro"), "w", encoding="utf-8") as f:
    f.write(faq)
print("  OK: FAQ.astro (JSON-LD schema + chevron rotation)")

# ===== 5. BeachCard: Fix accordion script to use the shared global one =====
beachcard = """---
import beaches from "../data/beaches.json";
---
<section id="beaches" class="py-16 bg-white">
  <div class="max-w-7xl mx-auto px-4">
    <h2 class="text-2xl md:text-3xl font-bold tracking-tight mb-8">Beach Details</h2>
    <div class="space-y-4">
      {beaches.map(b => (
        <div id={`card-${b.id}`} class="border border-gray-200 rounded-xl overflow-hidden transition-shadow hover:shadow-md">
          <button class="w-full px-5 py-4 flex items-start gap-4 text-left" data-target={`content-${b.id}`} aria-expanded="false">
            <div class="flex-1 min-w-0">
              <div class="flex items-center gap-2 flex-wrap">
                <h3 class="text-lg font-semibold">{b.name}</h3>
                <span class="text-sm text-gray-400">{b.nameCN}</span>
                <span class={`w-2 h-2 rounded-full ${b.crowdLevel==='busy'?'bg-accent':b.crowdLevel==='moderate'?'bg-amber-400':'bg-ocean'}`}></span>
              </div>
              <div class="flex items-center gap-4 mt-1 text-sm text-gray-600 flex-wrap">
                <span>{b.distance} from city</span>
                <span>{b.fee}</span>
                <span class="flex items-center gap-1"><svg width="12" height="12" viewBox="0 0 24 24" fill="#e0683a"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>{b.rating}</span>
                <span>{b.crowdLabel}</span>
              </div>
              <p class="text-gray-600 text-sm mt-2 line-clamp-2">{b.description}</p>
            </div>
            <svg class="w-5 h-5 text-gray-400 transition-transform duration-300 flex-shrink-0 mt-1" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div id={`content-${b.id}`} class="accordion-content">
            <div class="accordion-inner px-5 pb-5 border-t border-gray-100">
              <div class="grid md:grid-cols-3 gap-4 mt-4">
                <div>
                  <h4 class="font-semibold text-sm text-ocean mb-2">How to Get There</h4>
                  <ul class="text-sm text-gray-600 space-y-1">
                    {b.transport.metro && <li>Metro: {b.transport.metro} ({b.transport.metroExit}) - {b.transport.metroWalk}</li>}
                    {b.transport.bus && <li>Bus: {b.transport.bus}</li>}
                    {b.transport.taxiFromFutian && <li>Taxi from Futian: {b.transport.taxiFromFutian}</li>}
                    {b.transport.taxiFromLuohu && <li>Taxi from Luohu: {b.transport.taxiFromLuohu}</li>}
                    {b.transport.driveTime && <li>Drive: {b.transport.driveTime}</li>}
                    {b.transport.parking && <li>Parking: {b.transport.parking}</li>}
                  </ul>
                </div>
                <div>
                  <h4 class="font-semibold text-sm text-ocean mb-2">Facilities</h4>
                  <ul class="text-sm text-gray-600 space-y-1">
                    {b.facilities.showers && <li>Showers: {b.facilities.showers}</li>}
                    {b.facilities.lockers && <li>Lockers: {b.facilities.lockers}</li>}
                    {b.facilities.umbrellas && <li>Umbrellas/Chairs: {b.facilities.umbrellas}</li>}
                    {b.facilities.lifeguards && <li>Lifeguards: {b.facilities.lifeguards}</li>}
                    {b.facilities.food && <li>Food: {b.facilities.food}</li>}
                    {b.facilities.restrooms && <li>Restrooms: {b.facilities.restrooms}</li>}
                  </ul>
                </div>
                <div>
                  <h4 class="font-semibold text-sm text-ocean mb-2">Beach Features</h4>
                  <ul class="text-sm text-gray-600 space-y-1">
                    <li>Sand: {b.features.sandType}</li>
                    <li>Water: {b.features.waterQuality}</li>
                    <li>Waves: {b.features.waveType}</li>
                    <li>Best: {b.features.bestSeason}</li>
                    <li>Swim: {b.features.swimZone}</li>
                  </ul>
                  <div class="mt-3">
                    <h4 class="font-semibold text-sm text-ocean mb-1">Tips</h4>
                    <ul class="text-sm text-gray-600 space-y-1">
                      {b.tips.map((t,i) => <li key={i}>{t}</li>)}
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      ))}
    </div>
  </div>
</section>
"""

with open(os.path.join(base, "components", "BeachCard.astro"), "w", encoding="utf-8") as f:
    f.write(beachcard)
print("  OK: BeachCard.astro (aria-expanded + shared chevron script)")

print("\\nAll fixes applied.")
