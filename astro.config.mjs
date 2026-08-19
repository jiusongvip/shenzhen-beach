import { defineConfig } from "astro/config";
import tailwindcss from "@tailwindcss/vite";
import sitemap from "@astrojs/sitemap";

// Map beach slugs to their images for sitemap image entries
const beachImages = {
  dameisha: "/images/dameisha.webp",
  xichong: "/images/hero-xichong.webp",
  xiaomeisha: "/images/xiaomeisha.webp",
  dongchong: "/images/dongchong.webp",
  yangmeikeng: "/images/yangmeikeng.webp",
  jinshawan: "/images/jinshawan.webp",
  judiaosha: "/images/judiaosha.webp",
  nanao: "/images/nanao.webp",
  shuitousha: "/images/shuitousha.webp",
  shangdong: "/images/shangdong.webp",
};

// Single-page strategy with 10 beach detail pages.
// Legacy SEO URLs 301-redirect to the matching #section on the homepage,
// consolidating ranking authority into one page.
export default defineConfig({
  site: "https://www.shenzhen-beach.com",
  trailingSlash: "always",
  integrations: [sitemap({
    lastmod: new Date("2026-08-12"),
    serialize(item) {
      const site = "https://www.shenzhen-beach.com";
      let img = "";
      if (item.url === site) {
        img = site + "/images/hero-xichong.webp";
      } else {
        const m = item.url.match(/beaches\/(\w+)/);
        if (m && beachImages[m[1]]) img = site + beachImages[m[1]];
      }
      if (img) {
        return { ...item, img: [{ url: img }] };
      }
      return item;
    }
  })],
  vite: {
    plugins: [tailwindcss()],
  },
  redirects: {
    "/best-shenzhen-beach": "/#compare",
    "/shenzhen-beach-comparison": "/#compare",
    "/shenzhen-beach-transport": "/#transport",
    "/how-to-get-to-shenzhen-beaches": "/#transport",
    "/shenzhen-beach-faq": "/#faq",
    "/shenzhen-beach-guide": "/#beaches",
    "/shenzhen-beach-season": "/#seasons",
    "/best-time-to-visit-shenzhen-beaches": "/#seasons",
    "/shenzhen-beach-foreign": "/#foreign",
    "/shenzhen-beaches": "/",
    "/beaches": "/#beaches",
    "/compare": "/#compare",
    "/transport": "/#transport",
    "/seasons": "/#seasons",
    "/faq": "/#faq",
    "/foreign": "/#foreign",
  },
});
