import rss from '@astrojs/rss';

export async function GET(context) {
  return rss({
    title: 'Shenzhen Beaches',
    description: 'Independent travel guide to the best beaches in Shenzhen, China. Compare all 10 beaches with real photos, transport guides, and honest reviews.',
    site: context.site,
    items: [
      { title: 'Shenzhen Beach Guide — Compare All 10 Beaches', description: 'Interactive map, comparison tool, transport guides, entrance fees, seasonal guide and honest reviews for every beach.', link: '/', pubDate: new Date('2026-08-10') },
      { title: 'Dameisha Beach (\u5927\u6885\u6c99) — Transport, Food & Tips', description: 'Shenzhen\'s most popular public beach. Free entry, Metro Line 8 access, 1.8 km of sand.', link: '/beaches/dameisha', pubDate: new Date('2026-08-10') },
      { title: 'Xichong Beach (\u897f\u6d8c) — Best Surfing in Shenzhen', description: 'Shenzhen\'s longest beach, cleanest water, best surf. 30 RMB entry.', link: '/beaches/xichong', pubDate: new Date('2026-08-10') },
      { title: 'Xiaomeisha Beach (\u5c0f\u6885\u6c99) — Resort Beach Guide', description: 'Upscale resort beach experience. 50 RMB entry includes facilities.', link: '/beaches/xiaomeisha', pubDate: new Date('2026-08-10') },
      { title: 'Dongchong Beach (\u4e1c\u6d8c) — Quiet Hiking & Surfing', description: 'Quiet beach with the famous Dongchong-to-Xichong hiking trail. 20 RMB entry.', link: '/beaches/dongchong', pubDate: new Date('2026-08-10') },
      { title: 'Yangmeikeng Beach (\u6768\u6885\u5751) — Cycling & Photography', description: 'Free beach with a scenic coastal cycling path and stunning photo spots.', link: '/beaches/yangmeikeng', pubDate: new Date('2026-08-10') },
      { title: 'Jinshawan Beach (\u91d1\u6c99\u6e7e) — Luxury Resort Escape', description: 'Quiet luxury resort beach with free entry and golden sand.', link: '/beaches/jinshawan', pubDate: new Date('2026-08-10') },
      { title: 'Judiaosha Beach (\u6854\u9493\u6c99) — Best Hidden Gem', description: 'Crescent-shaped bay with white sand, rated 4.6/5. Free entry.', link: '/beaches/judiaosha', pubDate: new Date('2026-08-10') },
      { title: 'Nanao Beach (\u5357\u6fb3) — Local Fishing Town Beach', description: 'Authentic local beach experience with fresh seafood dining nearby.', link: '/beaches/nanao', pubDate: new Date('2026-08-10') },
      { title: 'Shuitousha Beach (\u6c34\u5934\u6c99) — Secluded Peace', description: 'Small, secluded beach for those who want quiet and solitude.', link: '/beaches/shuitousha', pubDate: new Date('2026-08-10') },
      { title: 'Shangdong Beach (\u4e0a\u6d1e) — Off-Path Local Beach', description: 'Undeveloped, quiet local beach for adventurous visitors.', link: '/beaches/shangdong', pubDate: new Date('2026-08-10') },
      { title: 'Best Time to Visit Shenzhen Beaches', description: 'Season-by-season guide: May-October for swimming, November for uncrowded beach walks.', link: '/#seasons', pubDate: new Date('2026-08-10') },
      { title: 'How to Get to Shenzhen Beaches', description: 'Complete transport guide: Metro Line 8, bus routes, taxi fares, and driving directions.', link: '/#transport', pubDate: new Date('2026-08-10') },
    ],
    customData: '<language>en</language>',
  });
}
