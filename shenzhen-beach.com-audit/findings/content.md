
# Content Quality Findings

## E-E-A-T Assessment

**Experience:** Good — TrustSignals section states "Built by Shenzhen locals who have visited every beach multiple times across all seasons." Photos appear to be real (not stock). Content includes specific, practical details (bus numbers, exact prices, walking times).

**Expertise:** Adequate — Water quality data cited from Shenzhen Ecology Bureau monthly reports. Transport routes verified against official sources. "Not AI-generated content — everything comes from firsthand visits."

**Authoritativeness:** Developing — Person schema exists but no visible author byline or credentials. No external citations or backlinks yet (site not deployed). The site is not affiliated with any tourism board.

**Trustworthiness:** Good — "Last verified: August 2026" visible. Disclaimers present. Prices in RMB clearly stated. "Always check official sources before traveling."

## Critical Issues

### Broken template on all 10 beach pages
- "Best Time to Visit" section renders: " offers ideal conditions for . "
- Caused by a broken template literal that references neither `b.name` nor `b.bestTimeToVisit`
- Location: `src/layouts/BeachLayout.astro`, approximately line 265

### Duplicate "Photo Spots" section
- Two identical `<section>` blocks render consecutively on all beach pages
- Both contain `<h2 class="text-2xl font-bold mb-4">Photo Spots</h2>`
- The first block is a stray conditional that was likely left behind during editing

## Other Issues

### Duplicate H1 on homepage
- Two `<h1>` tags: Hero (`Shenzhen Beach Guide`) + CheatSheet (`Shenzhen Beach Cheat Sheet`)
- The CheatSheet h1 should be h2

### No per-page "last updated" date
- TrustSignals says "Updated weekly" but no specific per-page date visible
- Schema has `dateModified: "2026-08-10"` which is good
