
# Technical SEO Findings

## Crawlability

### robots.txt — PASS
- Wildcard `Allow: /` with specific AI bot directives
- Sitemap URL referenced correctly
- AI crawlers (GPTBot, Claude-Web, PerplexityBot) explicitly allowed

### Sitemap — PARTIAL PASS
- `sitemap-index.xml` references single `sitemap-0.xml` with 11 URLs
- Missing: image entries (`<image:image>`), video entries for YouTube embed
- Missing: 404 page (should not be in sitemap anyway — correct)

### Redirects — NEEDS IMPROVEMENT
- 17 redirect paths use `<meta http-equiv="refresh">` with `noindex`
- Should use HTTP 301 redirects at hosting level

## Indexability

### Canonical URLs — PASS
- All pages have proper `<link rel="canonical">` pointing to the correct URL
- Trailing slash handling: `trailingSlash: "never"` in astro config
- Redirect pages have canonicals pointing to hash-anchor targets

### noindex usage — PASS
- Only meta-refresh redirect pages use `noindex` (appropriate)
- 404 page is not in sitemap

## Security

### HTTPS — N/A (not deployed)
- Site URL configured as `https://shenzhen-beach.com`
- No security headers visible prior to deployment

## URL Structure

- Clean, descriptive paths: `/beaches/{slug}`
- Redirect paths preserved for legacy SEO URLs
- No `.html` extensions, no query parameters

## Internal Linking

- Beach cards link to detail pages
- "You Might Also Like" cross-links between beach pages
- Nav links use hash fragments (works on homepage, suboptimal elsewhere)
