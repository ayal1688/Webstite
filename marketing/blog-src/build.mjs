// Builds the wearoru.com blog into the oru-store checkout:
//   blog/index.html, blog/<slug>.html, sitemap.xml and llms.txt.
// Posts live in ./posts/*.mjs (one default export each). Add a file, run
//   node marketing/blog-src/build.mjs [path-to-oru-store]
// then review the diff in oru-store before anything is pushed (main deploys live).
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const STORE = path.resolve(process.argv[2] || process.env.ORU_STORE || path.join(here, '../../../ORU-store'));
const SITE = 'https://wearoru.com';
if (!fs.existsSync(path.join(STORE, 'server', 'index.js'))) {
  console.error('Not an oru-store checkout: ' + STORE);
  process.exit(1);
}

const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const strip = (html) => html.replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim();
const human = (d) => new Date(d + 'T12:00:00Z').toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric', timeZone: 'UTC' });
const ld = (obj) => `<script type="application/ld+json">${JSON.stringify(obj).replace(/</g, '\\u003c')}</script>`;

const ORG = { '@type': 'Organization', name: 'ORU', url: SITE + '/', logo: SITE + '/assets/icon-512.png' };

const posts = [];
for (const f of fs.readdirSync(path.join(here, 'posts')).filter((f) => f.endsWith('.mjs')).sort()) {
  const p = (await import(pathToFileURL(path.join(here, 'posts', f)).href)).default;
  for (const k of ['slug', 'title', 'short', 'description', 'date', 'lede', 'body']) {
    if (!p[k]) throw new Error(`${f}: missing ${k}`);
  }
  if (p.description.length > 160) console.warn(`${f}: description is ${p.description.length} chars (Google shows ~155)`);
  p.words = strip(p.lede + ' ' + p.body + ' ' + (p.faq || []).flat().join(' ')).split(' ').length;
  p.url = `${SITE}/blog/${p.slug}.html`;
  p.file = f;
  posts.push(p);
}
// Newest first; posts published the same day keep the later-numbered file on top.
posts.sort((a, b) => (a.date !== b.date ? (a.date < b.date ? 1 : -1) : (a.file < b.file ? 1 : -1)));

function page({ title, description, canonical, type = 'website', crumbs, jsonld = [], main }) {
  const crumbHtml = crumbs.map((c, i) => i === crumbs.length - 1
    ? `<span aria-current="page">${esc(c[0])}</span>`
    : `<a href="${c[1]}">${esc(c[0])}</a>`).join(' &nbsp;/&nbsp; ');
  const crumbLd = {
    '@context': 'https://schema.org', '@type': 'BreadcrumbList',
    itemListElement: crumbs.map((c, i) => ({ '@type': 'ListItem', position: i + 1, name: c[0], item: SITE + c[1] }))
  };
  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${esc(title)}</title>
<meta name="description" content="${esc(description)}">
<link rel="canonical" href="${canonical}">
<meta property="og:site_name" content="ORU">
<meta property="og:title" content="${esc(title)}">
<meta property="og:description" content="${esc(description)}">
<meta property="og:url" content="${canonical}">
<meta property="og:image" content="${SITE}/assets/og.png">
<meta property="og:type" content="${type}">
<meta name="twitter:card" content="summary_large_image">
${[crumbLd, ...jsonld].map(ld).join('\n')}
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/assets/icon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#0F1011">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
<script>if(!matchMedia('(prefers-reduced-motion: reduce)').matches)document.documentElement.classList.add('m')</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<header class="wrap site-head">
  <a class="brand" href="/">
    <svg viewBox="0 0 120 120" role="img" aria-label="ORU"><circle cx="60" cy="60" r="47.38" fill="none" stroke="#E8E6E1" stroke-width="17.23"/><rect x="37.60" y="51.21" width="44.80" height="17.58" fill="#D1442B"/></svg>
    ORU
  </a>
  <nav class="site-nav" aria-label="Main">
    <a href="/#kit">Kit</a>
    <a href="/blog/" class="hide-xs">Blog</a>
    <a href="/#questions" class="hide-xs">Help</a>
    <a href="/cart.html">Bag (<span data-cart-count>0</span>)</a>
  </nav>
</header>

<main id="main">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb">
      ${crumbHtml}
    </nav>
${main}
  </div>
</main>

<footer class="site-foot">
  <div class="wrap">
    <svg class="mark-lg" viewBox="0 0 120 120" role="img" aria-label="ORU"><circle cx="60" cy="60" r="47.38" fill="none" stroke="#8B8A85" stroke-width="17.23"/><rect x="37.60" y="51.21" width="44.80" height="17.58" fill="#D1442B"/></svg>
    <div class="foot-cols">
      <div>
        <h2>Kit</h2>
        <ul>
          <li><a href="/product-watts.html">Watts tee</a></li>
          <li><a href="/#honest">What it is</a></li>
          <li><a href="/blog/">Blog</a></li>
        </ul>
      </div>
      <div>
        <h2>Help</h2>
        <ul>
          <li><a href="/about.html">Who makes it</a></li>
          <li><a href="/track.html">Track an order</a></li>
          <li><a href="/#questions">Sizing and shipping</a></li>
          <li><a href="/refunds.html">Returns</a></li>
          <li><a href="mailto:support@wearoru.com">support@wearoru.com</a></li>
        </ul>
      </div>
      <div>
        <h2>Legal</h2>
        <ul>
          <li><a href="/privacy.html">Privacy</a></li>
          <li><a href="/cookies.html">Cookies</a></li>
          <li><a href="/terms.html">Terms</a></li>
        </ul>
      </div>
      <div>
        <h2>ORU</h2>
        <ul>
          <li>14 Ben Gurion Boulevard</li>
          <li>Haifa 3502318, Israel</li>
          <li>Business no. 25672138</li>
        </ul>
      </div>
    </div>
    <p class="legal-line">&copy; 2026 ORU. Every message answered within one business day.</p>
  </div>
</footer>

<div class="sticky-cta">
  <span>From $56</span>
  <a class="btn" href="/product-watts.html">See the tee</a>
</div>

<div class="cookie" id="cookie-banner" role="dialog" aria-live="polite" aria-label="Cookie choice" hidden>
  <p>Analytics load only if you allow them. Nothing else here follows you. <a class="link-under" href="/cookies.html">What we store</a>.</p>
  <div class="cookie-row">
    <button class="btn" id="cookie-yes" type="button">Allow analytics</button>
    <button class="btn btn-quiet" id="cookie-no" type="button">Essential only</button>
  </div>
</div>

<script src="/assets/vendor/gsap.min.js"></script>
<script src="/assets/vendor/ScrollTrigger.min.js"></script>
<script src="/assets/vendor/lenis.min.js"></script>
<script src="/assets/site.js"></script>
</body>
</html>
`;
}

const outDir = path.join(STORE, 'blog');
fs.mkdirSync(outDir, { recursive: true });

for (const p of posts) {
  const faq = p.faq || [];
  const faqHtml = faq.length ? `
    <section class="article-faq">
      <h2>Questions people ask</h2>
      <div class="faq">
${faq.map(([q, a]) => `        <details open>
          <summary>${esc(q)}</summary>
          <p>${esc(a)}</p>
        </details>`).join('\n')}
      </div>
    </section>` : '';
  const jsonld = [{
    '@context': 'https://schema.org', '@type': 'BlogPosting',
    headline: p.title, description: p.description, datePublished: p.date, dateModified: p.updated || p.date,
    mainEntityOfPage: p.url, image: SITE + '/assets/og.png', inLanguage: 'en',
    author: ORG, publisher: ORG, keywords: p.keyword, wordCount: p.words
  }];
  if (faq.length) jsonld.push({
    '@context': 'https://schema.org', '@type': 'FAQPage',
    mainEntity: faq.map(([q, a]) => ({ '@type': 'Question', name: q, acceptedAnswer: { '@type': 'Answer', text: a } }))
  });
  const main = `
    <article class="article">
      <header class="article-head">
        <p class="eyebrow">Blog &middot; <time datetime="${p.date}">${human(p.date)}</time> &middot; ${Math.max(1, Math.round(p.words / 220))} min read</p>
        <h1>${esc(p.title)}</h1>
        <p class="lede">${esc(p.lede)}</p>
      </header>
      <div class="article-body">
${p.body.trim()}
      </div>
${faqHtml}
      <aside class="note article-cta">
        <p>Written by the one person behind ORU, who rides e-enduro and makes
        one shirt about it. <a class="link-under" href="/product-watts.html">See the Watts tee</a>
        or <a class="link-under" href="/blog/">read the other posts</a>.</p>
      </aside>
    </article>`;
  fs.writeFileSync(path.join(outDir, p.slug + '.html'), page({
    title: `${p.title} — ORU`, description: p.description, canonical: p.url, type: 'article',
    crumbs: [['Home', '/'], ['Blog', '/blog/'], [p.short, `/blog/${p.slug}.html`]], jsonld, main
  }));
}

const indexMain = `
    <section class="intro" style="padding-block:4vh 6vh">
      <p class="eyebrow">Blog</p>
      <h1 style="font-size:clamp(2.4rem,7vw,4.6rem)">Notes from<br>the trailhead.</h1>
      <p class="lede" style="max-width:56ch">E-MTB riding, what to wear for it, and the
      arguments that come with it. Written by the one person behind ORU. No
      sponsored posts.</p>
    </section>
    <ul class="post-list">
${posts.map((p) => `      <li>
        <a href="/blog/${p.slug}.html">
          <span class="post-date"><time datetime="${p.date}">${human(p.date)}</time></span>
          <span class="post-title">${esc(p.title)}</span>
          <span class="post-desc">${esc(p.description)}</span>
        </a>
      </li>`).join('\n')}
    </ul>`;
fs.writeFileSync(path.join(outDir, 'index.html'), page({
  title: 'Blog — e-MTB riding, kit and arguments — ORU',
  description: 'Honest posts about e-MTB riding: what to wear, whether it is cheating, gifts for riders. From the one person behind ORU.',
  canonical: SITE + '/blog/',
  crumbs: [['Home', '/'], ['Blog', '/blog/']],
  jsonld: [{ '@context': 'https://schema.org', '@type': 'Blog', name: 'ORU blog', url: SITE + '/blog/', publisher: ORG,
    blogPost: posts.map((p) => ({ '@type': 'BlogPosting', headline: p.title, url: p.url, datePublished: p.date })) }],
  main: indexMain
}));

// sitemap.xml: fixed pages plus every post. lastmod only where we know it.
const fixed = [
  ['/', '1.0'], ['/product-watts.html', '0.9'], ['/blog/', '0.8'], ['/about.html', '0.7'],
  ['/refunds.html', '0.4'], ['/privacy.html', '0.3'], ['/cookies.html', '0.3'], ['/terms.html', '0.3']
];
const latest = posts.length ? posts.map((p) => p.updated || p.date).sort().pop() : null;
const sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'];
for (const [u, pr] of fixed) {
  sm.push(`  <url><loc>${SITE}${u}</loc>${u === '/blog/' && latest ? `<lastmod>${latest}</lastmod>` : ''}<priority>${pr}</priority></url>`);
}
for (const p of posts) sm.push(`  <url><loc>${p.url}</loc><lastmod>${p.updated || p.date}</lastmod><priority>0.6</priority></url>`);
sm.push('</urlset>', '');
fs.writeFileSync(path.join(STORE, 'sitemap.xml'), sm.join('\n'));

// llms.txt (llmstxt.org format): a plain map of the site for AI assistants.
const llms = `# ORU

> ORU is a one-person e-MTB apparel brand based in Haifa, Israel. It sells one product, the Watts tee: a funny e-bike t-shirt for e-MTB riders, printed to order in the United States and shipped free.

Key facts:
- Product: Watts tee. Light (4 oz/yd²) 100% polyester, sweat-wicking, classic unisex fit, black or athletic navy, sizes S–3XL.
- Print: DTF back print of a rising chart that becomes the word WATTS above "ARE OVERRATED", plus a small ORU chest mark.
- Price: $56 (S–XL), $60 (2XL), $62 (3XL). Never discounted. Free shipping.
- Production: made to order; up to 10 days to print, then 2–5 days in transit to US addresses, 10–20 days to other countries.
- Ships to: US, Canada, UK, Ireland, Germany, France, Spain, Italy, Netherlands, Belgium, Austria, Sweden, Denmark, Finland, Norway, Poland, Portugal, Czechia, Israel, Australia, New Zealand, Japan, Singapore.
- Wrong size within 30 days: the right size is printed free and the customer keeps the first shirt.
- Honest limits: it wicks and dries fast but does not stop sweat; the printed patch breathes less than the rest of the shirt; product images are illustrations, not photos.
- Contact: support@wearoru.com, answered within one business day.

## Shop

- [Watts tee](${SITE}/product-watts.html): product page with sizes, prices, fabric, care and shipping.
- [Home and FAQ](${SITE}/): what the shirt is, how made-to-order works, buying questions.
- [Returns and refunds](${SITE}/refunds.html): wrong-size replacement, faulty items, statutory rights.
- [About](${SITE}/about.html): who makes ORU.

## Blog

${posts.map((p) => `- [${p.title}](${p.url}): ${p.description}`).join('\n')}

## Optional

- [Privacy](${SITE}/privacy.html)
- [Terms](${SITE}/terms.html)
`;
fs.writeFileSync(path.join(STORE, 'llms.txt'), llms);

for (const p of posts) console.log(`${p.slug}: ${p.words} words`);
console.log(`Wrote ${posts.length} posts, blog index, sitemap.xml and llms.txt into ${STORE}`);
