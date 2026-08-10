---
title: "SEO Audit Report — shenzhen-beach.com"
date: "2026-08-10"
business_type: "Travel / Destination Guide (Content Site)"
pages_crawled: 22 (11 unique + 11 redirect pages)
health_score: 67/100
---

# SEO Audit Report: shenzhen-beach.com

## Executive Summary

**Overall SEO Health Score: 67/100**

shenzhen-beach.com is a well-structured single-page guide with 10 beach detail pages, built on Astro (static site). The site has strong fundamentals — excellent structured data, good content depth, proper canonical URLs, and AI crawler access. However, several bugs are actively degrading page quality (duplicate sections, broken templates) and a few high-impact gaps (missing OG images, no icon link, placeholder GA) need immediate attention.

**Business Type Detected:** Travel / Destination Guide — content-rich informational site targeting English-speaking visitors to Shenzhen beaches.

**Top Critical Issues:**
1. Broken "Best Time to Visit" template on all 10 beach pages (displays gibberish)
2. "Photo Spots" section duplicated on all 10 beach pages
3. FAQ structured data uses raw bus numbers instead of helpful sentences

**Top Quick Wins:**
1. Fix the two BeachLayout.astro template bugs (30 min)
2. Add `<link rel="icon">` to Layout.astro (2 min)
3. Pass `ogImage` prop from beach pages to BeachLayout (5 min)
4. Replace GA4 placeholder with real ID or remove the tag (5 min)
5. Fix the duplicate H1 in CheatSheet (1 min)

---

## Scoring Breakdown

| Category | Score | Weight | Weighted |
|----------|-------|--------|----------|
| Technical SEO | 72 | 22% | 15.8 |
| Content Quality | 65 | 23% | 15.0 |
| On-Page SEO | 70 | 20% | 14.0 |
| Schema / Structured Data | 78 | 10% | 7.8 |
| Performance (CWV) | 55 | 10% | 5.5 |
| AI Search Readiness | 72 | 10% | 7.2 |
| Images | 65 | 5% | 3.3 |
| **Total** | | | **67.4** |

---

## 1. Technical SEO (72/100)

### What Works
- Astro static site with clean HTML output and minimal JS
- Proper canonical URLs on all pages
- Sitemap generated via `@astrojs/sitemap`
- robots.txt allows all crawlers including AI bots (GPTBot, Claude-Web, PerplexityBot)
- Astro redirects configured for legacy URLs
- All internal links use clean paths (no `.html` extensions)
- `/beaches` index page exists as a landing page (redirects to `/#beaches`)

### Findings

**[Critical] Redirect pages use meta refresh, not HTTP 301**
- All redirect pages (e.g., `/best-shenzhen-beach`, `/shenzhen-beach-comparison`, etc.) use `<meta http-equiv="refresh">` with `noindex` instead of proper 301 HTTP redirects.
- Meta refresh passes minimal link equity; Google treats 301s as stronger signals.
- Static hosts (Cloudflare Pages, Netlify) support 301 redirect configs — use those instead.
- Files: [`dist/best-shenzhen-beach/index.html`](/D:/workspaces/website/shenzhen-beach/dist/best-shenzhen-beach/index.html) and 16 similar redirect pages.

**[High] No explicit favicon link in `<head>`**
- The site relies on `/favicon.ico` being served at the root, which browsers pick up by convention. An explicit `<link rel="icon">` ensures all crawlers and platforms pick it up.
- File: [`src/layouts/Layout.astro`](/D:/workspaces/website/shenzhen-beach/src/layouts/Layout.astro)

**[Medium] CSS is render-blocking**
- Leaflet CSS loaded synchronously in `<head>` via `<link>` (no `media="print" onload="this.media='all'"` trick)
- Tailwind CSS bundle at 42 KB is also render-blocking
- Impact: delays LCP and FCP on first visit
- File: [`src/layouts/Layout.astro`](/D:/workspaces/website/shenzhen-beach/src/layouts/Layout.astro)

**[Medium] GA4 uses placeholder ID `G-XXXXXXXXXX`**
- All pages include the Google Analytics snippet but with a dummy ID
- Either add a real tracking ID or remove the script entirely (it's dead weight: ~1 KB inline JS + an extra network request)
- File: [`src/layouts/Layout.astro`](/D:/workspaces/website/shenzhen-beach/src/layouts/Layout.astro)

**[Low] Sitemap lacks image and video entries**
- The sitemap only lists page URLs with `lastmod`. No `<image:image>` entries despite 10 high-quality beach photos on detail pages.
- The embedded YouTube video could also use a `<video:video>` entry.
- File: [`dist/sitemap-0.xml`](/D:/workspaces/website/shenzhen-beach/dist/sitemap-0.xml)

**[Low] No `lastmod` on HTML pages themselves**
- Sitemap has `lastmod` dates but no `<meta>` tags in the HTML indicating content freshness
- File: [`src/layouts/Layout.astro`](/D:/workspaces/website/shenzhen-beach/src/layouts/Layout.astro)

---

## 2. Content Quality (65/100)

### What Works
- Deep, original content on all 10 beach detail pages
- Well-structured sections: Transport, Food, Stay, Clothing, Facilities, Safety, Tips
- Includes Chinese names for practical use
- Seasonal guide covers all four seasons
- International visitor section with payment, visa, etiquette info
- Vs Hong Kong comparison adds authority

### Findings

**[Critical] "Best Time to Visit" section displays gibberish on all 10 beach pages**
- Template outputs: " offers ideal conditions for . " (no beach name, no content)
- Broken template literal in BeachLayout.astro line ~265
- User-facing and harms credibility
- File: [`src/layouts/BeachLayout.astro`](/D:/workspaces/website/shenzhen-beach/src/layouts/BeachLayout.astro)

**[Critical] "Photo Spots" rendered twice on all 10 beach pages**
- Template has duplicate conditional blocks rendering the same section twice
- Causes duplicate content ID issues and wastes vertical space
- File: [`src/layouts/BeachLayout.astro`](/D:/workspaces/website/shenzhen-beach/src/layouts/BeachLayout.astro)

**[High] Duplicate H1 on homepage**
- Two `<h1>` tags found: Hero (`Shenzhen Beach Guide`) and CheatSheet (`Shenzhen Beach Cheat Sheet`)
- The CheatSheet should use an H2; this is semantically incorrect
- File: [`src/components/CheatSheet.astro`](/D:/workspaces/website/shenzhen-beach/src/components/CheatSheet.astro)

**[Medium] llms.txt only lists 3 of 10 beaches**
- The llms.txt file describes Dameisha, Xichong, and Xiaomeisha but omits the other 7 beaches
- Reduces AI discoverability for the full content inventory
- File: [`public/llms.txt`](/D:/workspaces/website/shenzhen-beach/public/llms.txt)

**[Low] No visible "last updated" date on pages**
- The TrustSignals section says "All information verified August 2026" but no per-page or section-level last-updated metadata visible to users
- File: [`src/components/TrustSignals.astro`](/D:/workspaces/website/shenzhen-beach/src/components/TrustSignals.astro)

**[Low] No author/authority meta tag**
- The Person schema exists in JSON-LD but no `<meta name="author">` tag
- File: [`src/layouts/Layout.astro`](/D:/workspaces/website/shenzhen-beach/src/layouts/Layout.astro)

---

## 3. On-Page SEO (70/100)

### What Works
- Clean, keyword-rich `<title>` tags (e.g., "Dameisha Beach (大梅沙) - Transport, Food, Hotels & Tips | Shenzhen Beaches")
- Descriptive meta descriptions on all pages
- Proper heading hierarchy (mostly H1 → H2 → H3) on detail pages
- Breadcrumb navigation on detail pages with `aria-label`
- Clean URL structure: `/beaches/{slug}`
- Internal linking between beach pages via "You Might Also Like" and hero quick picks

### Findings

**[High] OG images missing on all 10 beach detail pages**
- BeachLayout accepts an `ogImage` prop but the beach page files never pass it
- Each beach has a dedicated WebP image that could be used for social sharing
- Without OG images, social shares look generic/bland
- Files: [`src/pages/beaches/*.astro`](/D:/workspaces/website/shenzhen-beach/src/pages/beaches/) (all 10 files)

**[Medium] Nav uses hash links even on non-homepage pages**
- Nav `<a href="/#compare">` etc. — on a beach detail page, clicking this jumps to the homepage + hash
- Could use conditional logic: on homepage use `#section`, on other pages use `/#section`
- File: [`src/components/Nav.astro`](/D:/workspaces/website/shenzhen-beach/src/components/Nav.astro)

**[Low] No `hreflang` tags**
- Content is English-only targeting international visitors. No `hreflang` is acceptable for a single-language site targeting English speakers worldwide, but could be added later for Chinese-language expansion.

---

## 4. Schema / Structured Data (78/100)

### What Works
- Homepage: `TouristDestination`, `ImageObject`, `WebSite`, `Person`, `BreadcrumbList`, `FAQPage` (via `@graph`)
- Beach Pages: `TouristAttraction`, `ImageObject`, `FAQPage` per beach
- Proper use of `GeoCoordinates`, `PostalAddress`, `AggregateRating`
- Chinese `alternateName` included in all beach schemas

### Findings

**[Critical] FAQ structured data uses raw bus numbers as answer text**
- "How do I get to Dameisha Beach?" → answer: "103, 387, M191, M362, M438, M465"
- These are raw bus route numbers with no context — not helpful for Voice Search or rich results
- Should be: "Take Metro Line 8 to Dameisha station (Exit C, 10 min walk) or bus routes 103, 387, M191, M362, M438, M465."
- File: [`src/layouts/BeachLayout.astro`](/D:/workspaces/website/shenzhen-beach/src/layouts/BeachLayout.astro) (FAQ data generation section)

**[Low] FAQ JSON-LD text differs from visible HTML**
- The JSON-LD FAQ data is generated from data field values which may differ from the H2-section content users actually see. Google may flag mismatch.
- Low impact but worth aligning in a future sweep.

---

## 5. Performance / CWV (55/100)

### Findings

**[High] Largest Contentful Paint (LCP) impacted by hero image**
- Hero image on homepage: `hero-xichong.webp` at ~143 KB with `loading="eager" fetchpriority="high"` — acceptable size but still the LCP bottleneck
- Hero image on detail pages: 85-145 KB WebP, `loading="eager"` — reasonable
- Further optimization: serve multiple resolutions via `<picture>` with `srcset` for different viewport widths

**[High] Render-blocking CSS**
- Google Fonts (Geist) loaded synchronously via `<link>` in head
- Leaflet CSS (76 KB from unpkg CDN) loaded synchronously
- Tailwind CSS bundle (42 KB) loaded synchronously
- Combined render-blocking CSS: ~120 KB
- Use `media="print" onload="this.media='all'"` for non-critical stylesheets

**[Medium] No font-display strategy**
- Google Fonts link doesn't specify `&display=swap`, meaning text remains invisible during font load (FOIT)
- Add `&display=swap` to the Google Fonts URL

**[Medium] Largest `.jpg` files wasting disk/hosting space in dist/**
- The `dist/images/` directory contains both `.jpg` (2-3 MB each) and `.webp` (50-145 KB) versions
- Only `.webp` is actually referenced in HTML
- Total wasted space: ~25 MB (remove these from the build output or add a cleanup step)
- Files: [`dist/images/*.jpg`](/D:/workspaces/website/shenzhen-beach/dist/images/)

**[Low] No `preload` for hero image**
- The hero image could use `<link rel="preload" as="image">` for faster LCP
- Currently relies on browser discovering it from the `<img>` tag

---

## 6. AI Search Readiness (72/100)

### What Works
- llms.txt file present at root
- robots.txt explicitly allows all major AI crawlers (GPTBot, Claude-Web, PerplexityBot)
- Good content depth with factual, citation-worthy claims
- JSON-LD structured data makes content machine-readable
- Chinese + English content (bilingual entity references) helps AI understanding

### Findings

**[Medium] Missing AI bot crawlers in robots.txt**
- Brave (Bravebot), You.com, Grok, Einstein, and others are not explicitly allowed
- Currently the wildcard `Allow: /` for `*` covers them, but explicit directives are more robust

**[Medium] llms.txt incomplete**
- Only lists 3 of 10 beaches and only the main page sections
- Should list all beach detail pages with descriptions

**[Low] No citation-friendly anchor IDs**
- Section IDs exist (`#transport`, `#seasons`, etc.) but individual facts/claims lack `id` attributes
- Adding IDs to key claims would improve passage-level citability for AI search

---

## 7. Images (65/100)

### What Works
- All images have `alt` text (e.g., "Dameisha Beach (大梅沙)" with both EN and CN names)
- WebP format used throughout for served images
- `loading="lazy"` on below-fold images
- `width` and `height` attributes on all `<img>` tags (prevents CLS)
- `fetchpriority="high"` on hero image

### Findings

**[High] No responsive images (`srcset` / `<picture>`)**
- All beach and hero images serve a single resolution regardless of viewport
- Desktop users download the same image as mobile users
- Use `<picture>` with `srcset` to serve smaller WebP variants for mobile

**[Medium] No image sitemap entries**
- Google Image Search can't easily discover the 10 beach photos without image sitemap entries

---

## Appendix: Page Inventory

| URL | Type | Status |
|-----|------|--------|
| `/` | Homepage | OK |
| `/beaches/dameisha` | Beach Detail | Template bugs |
| `/beaches/xichong` | Beach Detail | Template bugs |
| `/beaches/xiaomeisha` | Beach Detail | Template bugs |
| `/beaches/dongchong` | Beach Detail | Template bugs |
| `/beaches/yangmeikeng` | Beach Detail | Template bugs |
| `/beaches/jinshawan` | Beach Detail | Template bugs |
| `/beaches/judiaosha` | Beach Detail | Template bugs |
| `/beaches/nanao` | Beach Detail | Template bugs |
| `/beaches/shuitousha` | Beach Detail | Template bugs |
| `/beaches/shangdong` | Beach Detail | Template bugs |
| 17 redirect paths | Redirect | Meta refresh, not 301 |
| `/404` | 404 Page | OK |
