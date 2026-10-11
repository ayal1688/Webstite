# wearoru.com blog

Free replacement for an autoblog tool. Posts are plain JS files in `posts/`.
`build.mjs` turns them into finished pages inside the oru-store checkout.

```
node marketing/blog-src/build.mjs            # defaults to C:\Users\ayal1\ORU-store
node marketing/blog-src/build.mjs D:\other\oru-store
```

Each run writes:
- `blog/index.html`
- `blog/<slug>.html`
- `sitemap.xml` (fixed pages plus every post, with lastmod)
- `llms.txt`

Each post page has BlogPosting, FAQPage and BreadcrumbList structured data.

oru-store `main` deploys live, so review the diff there before pushing.

## Adding a post

1. Copy a file in `posts/` and give it the next number.
2. Fill in its fields:
   - `slug`, `title`, `short` (breadcrumb), `description` (≤155 chars), `keyword`, `date` (YYYY-MM-DD), `lede`.
   - `body`: HTML using h2, p, ul and ol.
   - `faq`: [question, answer] pairs.
3. Link the product page once, `/product-watts.html`, where it fits naturally.
4. Open with a two- or three-sentence "short answer". It is what chatbots and featured snippets quote.
5. Run the build and read the page.

House rules (same as the rest of the marketing kit):
- No invented reviews or customers.
- No claims about the shirt beyond the product page: it wicks, it does not stop sweat, and the print patch breathes less. Product images are illustrations.
- Never name the blank's maker.
- Cite real sources for facts, and leave out a fact you cannot back up.

The 30-post calendar is in `calendar.md`.
