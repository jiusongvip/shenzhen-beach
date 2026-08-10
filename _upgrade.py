import os, json
base = r"D:\workspaces\website\shenzhen-beach\src"

# ===== 1. RICH LAYOUT =====
# Smart title (avoid duplicate "Shenzhen"), rich structured data, GA, canonical
layout = """---
import "../styles/global.css";
export interface Props { title: string; description: string; ogImage?: string; jsonLd?: Record<string, unknown> | Record<string, unknown>[]; }
const { title, description, ogImage, jsonLd } = Astro.props;

// Smart title: avoid duplicating "Shenzhen" in page title
const baseName = "Shenzhen Beaches";
const fullTitle = title.includes("Shenzhen") ? title : `${title} | ${baseName}`;

// Canonical URL
const canonicalUrl = new URL(Astro.url.pathname, Astro.site).href.replace(/\\/$/, "");

// Default structured data for homepage
const isHome = Astro.url.pathname === "/" || Astro.url.pathname === "";
const defaultJsonLd = isHome ? [
  {
    "@context": "https://schema.org",
    "@type": "TouristDestination",
    "name": "Shenzhen Beaches",
    "description": "A comprehensive guide to all 10 beaches in Shenzhen, China. Interactive map, comparison tool, transport guides, entrance fees, and honest reviews to help you find your perfect beach day.",
    "url": new URL("/", Astro.site).href,
    "containsPlace": [
      {"@type": "TouristAttraction", "name": "Dameisha Beach", "alternateName": "大梅沙", "publicAccess": true},
      {"@type": "TouristAttraction", "name": "Xichong Beach", "alternateName": "西涌", "publicAccess": true},
      {"@type": "TouristAttraction", "name": "Xiaomeisha Beach", "alternateName": "小梅沙", "publicAccess": true},
      {"@type": "TouristAttraction", "name": "Dongchong Beach", "alternateName": "东涌", "publicAccess": true},
      {"@type": "TouristAttraction", "name": "Yangmeikeng Beach", "alternateName": "杨梅坑", "publicAccess": true},
      {"@type": "TouristAttraction", "name": "Jinshawan Beach", "alternateName": "金沙湾", "publicAccess": true},
      {"@type": "TouristAttraction", "name": "Judiaosha Beach", "alternateName": "桔钓沙", "publicAccess": true},
      {"@type": "TouristAttraction", "name": "Nanao Beach", "alternateName": "南澳沙滩", "publicAccess": true},
      {"@type": "TouristAttraction", "name": "Shuitousha Beach", "alternateName": "水头沙", "publicAccess": true},
      {"@type": "TouristAttraction", "name": "Shangdong Beach", "alternateName": "上洞", "publicAccess": true}
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "Shenzhen Beaches",
    "url": new URL("/", Astro.site).href,
    "description": "Complete guide to beaches in Shenzhen, China. Interactive map, comparison, transport info, and real tips for visitors."
  }
] : null;

const finalJsonLd = jsonLd || defaultJsonLd;
---

<!doctype html>
<html lang="en">
<head>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-XXXXXXXXXX');
  </script>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{fullTitle}</title>
  <meta name="description" content={description} />
  <meta property="og:title" content={fullTitle} />
  <meta property="og:description" content={description} />
  <meta property="og:type" content="website" />
  <meta property="og:url" content={canonicalUrl} />
  {ogImage && <meta property="og:image" content={ogImage} />}
  <meta name="twitter:card" content="summary_large_image" />
  <link rel="canonical" href={canonicalUrl} />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
  {finalJsonLd && <script type="application/ld+json" set:html={JSON.stringify(Array.isArray(finalJsonLd) ? {"@graph": finalJsonLd} : finalJsonLd)}></script>}
  <script is:inline>
    document.addEventListener('DOMContentLoaded', () => {
      // Accordion: toggle content + rotate chevron
      document.querySelectorAll('[aria-expanded]').forEach(btn => {
        btn.addEventListener('click', function() {
          const targetId = this.dataset.target;
          const content = targetId ? document.getElementById(targetId) : null;
          const expanded = this.getAttribute('aria-expanded') === 'true';
          this.setAttribute('aria-expanded', String(!expanded));
          if (content) content.classList.toggle('open');
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
print("  OK: Layout.astro (rich schema + GA + smart title + canonical)")

# ===== 2. ENHANCED FAQ with inline section links =====
faq = """---
const faqs = [
  {q:"Which Shenzhen beach is the best?",a:'Depends on what you want. Xichong for surfing and scenery, Dameisha for convenience and families, Yangmeikeng for photography and cycling, Xiaomeisha for a resort experience. Use the <a href="#compare" class="text-accent hover:underline">comparison table</a> above to find your match.'},
  {q:"Are Shenzhen beaches free?",a:'Most are free, including Dameisha, Yangmeikeng, Jinshawan, Judiaosha, Nanao, Shuitousha, and Shangdong. Xichong charges 30 RMB, Dongchong 20 RMB, and Xiaomeisha 50 RMB (includes facilities). See the <a href="#beaches" class="text-accent hover:underline">beach details</a> for full pricing.'},
  {q:"Can you swim at Shenzhen beaches?",a:'Yes. May through October is the main swimming season. Water quality varies and is published monthly by the Shenzhen Ecology Bureau. Xichong and Dongchong generally have the cleanest water. Check the <a href="#seasons" class="text-accent hover:underline">seasonal guide</a> for the best times.'},
  {q:"How to get to Shenzhen beaches from Hong Kong?",a:'Take MTR East Rail to Lo Wu or Lok Ma Chau, cross the border, then metro Line 8 (for Dameisha/Xiaomeisha) or taxi (for eastern beaches). Total: 1.5-2.5 hours. See the <a href="#transport" class="text-accent hover:underline">transport section</a> for all four options.'},
  {q:"When is the best time to visit Shenzhen beaches?",a:'September through November offers the best combination of warm water, clear skies, and manageable crowds. July and August are hottest but most crowded. See the <a href="#seasons" class="text-accent hover:underline">season-by-season breakdown</a>.'},
  {q:"Are Shenzhen beaches clean?",a:'Water quality varies. Eastern beaches (Xichong, Dongchong, Judiaosha) generally have Grade I. City beaches (Dameisha, Xiaomeisha) are regularly tested and usually Grade II, safe for swimming. Each <a href="#beaches" class="text-accent hover:underline">beach card</a> lists current water quality.'},
  {q:"Do I need to speak Chinese?",a:'At popular beaches like Dameisha, you can get by with English. At remote beaches, basic Chinese or a translation app helps. Use the <a href="#foreign" class="text-accent hover:underline">language cards</a> in the International Visitors section for taxi drivers.'},
  {q:"Is there surfing in Shenzhen?",a:'Yes. Xichong Beach is the main surf spot with consistent waves during typhoon season (Jul-Oct). Board rentals and lessons available from beachside shops. Dongchong also has surfable waves. See the <a href="#beaches" class="text-accent hover:underline">beach details</a> for surf conditions.'}
];

const strip = (s) => s.replace(/<[^>]*>/g, "").replace(/\\s+/g, " ").trim();

const schemaObj = {
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": faqs.map(item => ({
    "@type": "Question",
    "name": item.q,
    "acceptedAnswer": { "@type": "Answer", "text": strip(item.a) }
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
            <div class="accordion-inner px-5 pb-4 text-gray-600 text-sm" set:html={item.a}></div>
          </div>
        </div>
      ))}
    </div>
    <script type="application/ld+json" set:html={schemaJson}></script>
  </div>
</section>"""

with open(os.path.join(base, "components", "FAQ.astro"), "w", encoding="utf-8") as f:
    f.write(faq)
print("  OK: FAQ.astro (inline section links + set:html for answers)")

# ===== 3. 404 PAGE =====
os.makedirs(os.path.join(base, "pages", "404"), exist_ok=True)
with open(os.path.join(base, "pages", "404", "index.astro"), "w", encoding="utf-8") as f:
    f.write("""---
import Layout from "../../layouts/Layout.astro";
---
<Layout title="Page not found">
  <div class="min-h-[60vh] flex items-center justify-center px-4">
    <div class="text-center">
      <h1 class="text-4xl font-bold tracking-tighter mb-4">Page not found</h1>
      <p class="text-gray-600 mb-8">The page you are looking for does not exist. No worries.</p>
      <a href="/" class="inline-block px-6 py-3 rounded-full bg-accent text-white font-medium hover:bg-accent-dark transition-colors">Back to the beaches</a>
    </div>
  </div>
</Layout>""")
print("  OK: pages/404/index.astro")

# ===== 4. PUBLIC FILES =====
pub = r"D:\workspaces\website\shenzhen-beach\public"

# llms.txt
with open(os.path.join(pub, "llms.txt"), "w", encoding="utf-8") as f:
    f.write("# shenzhenbeaches.com\n")
    f.write("> A comprehensive single-page guide to all 10 beaches in Shenzhen, China. Interactive map, comparison tool, transport guides, real photos, honest reviews. Everything you need to find your perfect Shenzhen beach day.\n\n")
    f.write("## Main Page\n")
    f.write("- [Complete Guide](https://shenzhenbeaches.com/): One page that covers every Shenzhen beach.\n")
    f.write("  - #quiz — Hero + quick filter: find your beach match by activity (Swimming, Surfing, Family, Camping, Photography)\n")
    f.write("  - #map — Interactive Leaflet map with all 10 beaches color-coded by crowd level\n")
    f.write("  - #compare — Side-by-side comparison table of all beaches (distance, fee, rating, crowds)\n")
    f.write("  - #beaches — Accordion cards for each beach: transport, facilities, features, visitor tips\n")
    f.write("  - #transport — Metro, bus, taxi, and driving options to reach the beaches\n")
    f.write("  - #seasons — Spring/summer/autumn/winter guide with temperatures and best activities\n")
    f.write("  - #foreign — International visitor info: payment, visa, language cards, beach etiquette\n")
    f.write("  - #faq — 8 frequently asked questions with inline links to relevant sections\n\n")
    f.write("## Beach Detail Pages\n")
    for b in ["dameisha","xichong","xiaomeisha"]:
        f.write(f"- [{b.title()} Beach Guide](https://shenzhenbeaches.com/beaches/{b}/): Detailed guide with transport, facilities, features, and tips.\n")
print("  OK: public/llms.txt")

# robots.txt with AI crawler rules (like zhangjiajie)
with open(os.path.join(pub, "robots.txt"), "w", encoding="utf-8") as f:
    f.write("User-agent: *\n")
    f.write("Allow: /\n\n")
    f.write("Sitemap: https://shenzhenbeaches.com/sitemap-index.xml\n\n")
    f.write("User-agent: GPTBot\n")
    f.write("Allow: /\n\n")
    f.write("User-agent: Claude-Web\n")
    f.write("Allow: /\n\n")
    f.write("User-agent: PerplexityBot\n")
    f.write("Allow: /\n")
print("  OK: public/robots.txt")

print("\\nAll upgrades applied!")
