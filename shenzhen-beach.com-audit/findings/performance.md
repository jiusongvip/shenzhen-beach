
# Performance (Core Web Vitals) Findings

N.B. All measurements are lab estimates from static analysis and file sizes. Real CWV data requires deployment and monitoring.

## Estimated CWV

| Metric | Estimated | Status |
|--------|-----------|--------|
| LCP (Largest Contentful Paint) | 1.8-2.5s | Needs improvement |
| FCP (First Contentful Paint) | 1.2-1.8s | Needs improvement |
| CLS (Cumulative Layout Shift) | < 0.05 | Good |
| TBT (Total Blocking Time) | < 50ms | Good |

## Performance Issues

### Render-blocking CSS (~120 KB total)
- **Google Fonts** (Geist): loaded via `<link>` in `<head>`, no `display=swap`
- **Leaflet CSS**: 76 KB from unpkg CDN, loaded synchronously in `<head>`
- **Tailwind CSS bundle**: 42 KB, loaded via `<link>` in `<head>`
- Recommendation: Inline critical CSS, defer the rest. Add `&display=swap` to fonts URL.

### Hero Image (LCP)
- `hero-xichong.webp`: 142.5 KB — reasonable for a hero image
- Already has `loading="eager" fetchpriority="high" decoding="async"`
- Could add `<link rel="preload" as="image">` for the hero image
- Could serve a smaller variant for mobile via `<picture>` with `srcset`

### Image Sizes
- All served WebP images: 50-145 KB — good
- No `srcset` for responsive delivery — mobile downloads same as desktop
- Unused JPGs in dist (2-3 MB each, ~25 MB total) — should be removed

### JavaScript
- Minimal JS: inline menu toggle (~200 bytes), scroll-to-top (~200 bytes), QuickNav intersection observer (~500 bytes)
- No heavy frameworks — excellent for performance
- Google Analytics script adds ~1 KB inline + 1 network request (placeholder ID)
