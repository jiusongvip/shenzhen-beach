
# Action Plan — shenzhen-beach.com

## Phase 1: Critical Fixes (Week 1)

### Fix BeachLayout.astro template bugs
**Effort:** 30 min | **Impact:** High (10 pages)

1. **Fix broken "Best Time to Visit" section** — Replace the empty template literal with `${b.name} Beach offers ideal conditions for ${b.features?.bestSeason}.` or use `b.bestTimeToVisit` data if available.
2. **Remove duplicate "Photo Spots" section** — Delete the first (incomplete) conditional block; keep only the correct one.

### Fix FAQ structured data answers
**Effort:** 20 min | **Impact:** High (10 pages, voice search)

Rewrite the FAQ schema generation in BeachLayout.astro so the "How do I get to" answer is a full sentence incorporating metro, bus, and walking directions, not raw bus numbers.

### Fix duplicate H1 on homepage
**Effort:** 1 min | **Impact:** Low

Change the `<h1>` in CheatSheet.astro to `<h2>`.

---

## Phase 2: High-Impact Improvements (Weeks 2-3)

### Add OG images to beach detail pages
**Effort:** 10 min | **Impact:** Medium (social sharing)

Pass `ogImage` prop from each `src/pages/beaches/*.astro` file to BeachLayout. Map available images by beach ID.

### Add explicit favicon link
**Effort:** 2 min | **Impact:** Low

Add `<link rel="icon" type="image/svg+xml" href="/favicon.svg">` and `<link rel="icon" type="image/x-icon" href="/favicon.ico">` to Layout.astro `<head>`.

### Replace or remove GA4 placeholder
**Effort:** 5 min | **Impact:** Low (until deployed)

Replace `G-XXXXXXXXXX` with a real GA4 measurement ID. If no tracking is needed, remove both `<script>` blocks entirely.

### Convert redirects to proper 301s
**Effort:** 30 min | **Impact:** Medium (link equity)

Use hosting platform's redirect config (Cloudflare Pages `_redirects`, Netlify `_redirects`, or Nginx config) instead of Astro's HTML meta-refresh redirect pages.

### Add `font-display: swap`
**Effort:** 1 min | **Impact:** Medium (CWV)

Add `&display=swap` to the Google Fonts URL in Layout.astro.

---

## Phase 3: Content & Authority (Month 2)

### Optimize render-blocking CSS
**Effort:** 1 hour | **Impact:** Medium (CWV)

- Inline critical CSS (above-fold styles) and defer the rest
- Load Leaflet CSS with `media="print" onload="this.media='all'"`
- Consider self-hosting Leaflet CSS instead of loading from unpkg CDN

### Complete llms.txt with all 10 beaches
**Effort:** 15 min | **Impact:** Medium (AI discoverability)

Add all 10 beach detail pages with descriptions to `public/llms.txt`.

### Add image sitemap entries
**Effort:** 30 min | **Impact:** Medium (Google Image Search)

Extend the sitemap config or add a custom sitemap with `<image:image>` entries for all beach photos.

### Add responsive images
**Effort:** 2 hours | **Impact:** Medium (CWV, mobile UX)

Use `<picture>` with `srcset` to serve smaller WebP variants on mobile viewports. Generate 400w and 800w variants alongside the current full-size images.

### Remove unused JPGs from dist
**Effort:** 5 min | **Impact:** Low (hosting cost)

Add a build cleanup step to remove `.jpg` files from `dist/images/`. Astro already copies only referenced files, but ensure the `.jpg` files aren't being copied from `public/images/`.

---

## Phase 4: Monitoring & Iteration (Ongoing)

- Set up Google Search Console once deployed (verify ownership)
- Monitor Core Web Vitals via CrUX once the site gets traffic
- Add more AI crawler bots to robots.txt as new ones emerge
- Consider adding `hreflang` tags if Chinese-language pages are added
- Track SEO drift: re-run this audit after deployment to compare baselines

---

## Priority Summary

| # | Action | Severity | Effort |
|---|--------|----------|--------|
| 1 | Fix broken "Best Time to Visit" template | Critical | 15 min |
| 2 | Remove duplicate "Photo Spots" section | Critical | 15 min |
| 3 | Fix FAQ structured data answers | Critical | 20 min |
| 4 | Fix duplicate H1 (CheatSheet) | Low | 1 min |
| 5 | Add OG images to beach pages | High | 10 min |
| 6 | Add favicon link | High | 2 min |
| 7 | Replace/remove GA4 placeholder | High | 5 min |
| 8 | 301 redirects instead of meta refresh | High | 30 min |
| 9 | Add font-display: swap | Medium | 1 min |
| 10 | Optimize render-blocking CSS | Medium | 1 hr |
| 11 | Complete llms.txt | Medium | 15 min |
| 12 | Add image sitemap entries | Medium | 30 min |
| 13 | Add responsive images (srcset) | Medium | 2 hrs |
| 14 | Remove unused JPGs from dist | Low | 5 min |
| **Total** | | | **~6 hours** |
