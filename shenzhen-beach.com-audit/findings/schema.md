
# Schema / Structured Data Findings

## Implemented Schemas

### Homepage (@graph)
- `TouristDestination` with `containsPlace` (all 10 beaches as TouristAttraction)
- `ImageObject` (hero image)
- `WebSite` with dateModified and inLanguage
- `Person` (Shenzhen Beaches Team) with knowsAbout
- `BreadcrumbList` (single-level)
- `FAQPage` (8 questions)

### Beach Detail Pages
- `TouristAttraction` with GeoCoordinates, PostalAddress, AggregateRating
- `ImageObject` (beach photo)
- `FAQPage` (5 questions per beach)

## Critical Finding

### FAQ answers are not natural language
**Example (Dameisha):**
- "How do I get to Dameisha Beach?" → "103, 387, M191, M362, M438, M465"

These are raw bus numbers. Voice Search and rich results need natural-language answers:
> "Take Metro Line 8 to Dameisha station (Exit C, 10 min walk to the beach). Bus routes 103, 387, M191, M362, M438, and M465 also stop near the beach."

The fix is in `src/layouts/BeachLayout.astro` where FAQ data is generated.

## Quality

- All schemas validate structurally
- Chinese `alternateName` included (important for bilingual searches)
- `AggregateRating` uses plausible values (not all 5.0)
- `isAccessibleForFree` correctly set based on `feeNum === 0`
