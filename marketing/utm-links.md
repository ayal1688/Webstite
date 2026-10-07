# Links

One link per place. They all go to the Watts tee page.
Paste them exactly as written: lowercase, no link shortener, nothing added.
The first time you use one, open it yourself and check it lands on the Watts tee page.

## Every link

| Where | Exact link | Shows in the NEW SALE message as | Where you see clicks |
|---|---|---|---|
| TikTok bio (plain text, not clickable) | `wearoru.com` | `unknown` (a typed address carries no tag) | TikTok Analytics: profile views |
| TikTok pinned comment (plain text) | `wearoru.com` | `unknown` | none |
| TikTok Website field (only once it appears; reportedly after business verification or 1,000 followers — check in the app) | https://wearoru.com/product-watts?utm_source=tiktok&utm_medium=social&utm_campaign=launch | `tiktok` | TikTok Analytics: website clicks (check in the app) |
| Facebook Page "Shop now" button | https://wearoru.com/product-watts?utm_source=facebook&utm_medium=social&utm_campaign=launch | `facebook` | Page insights: action button clicks (check in the app) |
| Facebook Page posts and Reels (caption) | same Facebook link | `facebook` | Page insights: link clicks |
| Facebook group posts (only where the admins said yes and links are allowed) | same Facebook link | `facebook` | Not split from the Page. Note the date of each group post and watch for a jump. |
| Reddit: the one approved post only | https://wearoru.com/product-watts?utm_source=reddit&utm_medium=community&utm_campaign=launch | `reddit` | The post's view count and insights (check in the app) |
| Instagram bio (optional) | https://wearoru.com/product-watts?utm_source=instagram&utm_medium=social&utm_campaign=launch | `instagram` | Instagram insights |
| YouTube channel links (optional; check in the app whether links in Shorts descriptions are clickable) | https://wearoru.com/product-watts?utm_source=youtube&utm_medium=social&utm_campaign=launch | `youtube` | YouTube Studio |
| Strava profile (only if your profile is anonymous) | https://wearoru.com/product-watts?utm_source=strava&utm_medium=profile&utm_campaign=launch | `strava` | none that we know of (check in the app) |
| Google search (nothing to paste) | none | `unknown`, or the Google address | Search Console → Performance: clicks |

Where links never go:
- Reddit comments, ever. Nothing on Reddit during the warm-up (Days 1–14), and the profile stays clean too.
- Facebook groups in weeks 1–2. After that, only in groups whose admins said yes.
- If the Reddit mods want the link in a comment under your post instead of in the post, that comment starts with the disclosure line too:
  **Disclosure: this is my own small brand, ORU.**

## How you'll see results

### Sales: the NEW SALE message

Each paid order sends a NEW SALE message to the Discord channel behind `ALERT_WEBHOOK`, so it reaches your phone.
It shows the amount, the shirt, color and size, the source, and the PayPal order number. This comes with the site update; check it's live by Day 7.

It looks like this (four lines; the order number is made up here):

```
NEW SALE $56.00
1 × Watts tee Black L
source: reddit
PayPal order 1AB23456CD789012E
```

How to read the source:
- It's the first tagged link that visitor arrived on, remembered for that visit only.
- If they arrived without a tag, it shows the site they came from, or `unknown`.
- If they leave and come back later by typing the address, the source is `unknown`.
- If the server restarted between checkout and payment, the source is `unknown` too.
- An `unknown` source while TikTok is your busiest channel probably means TikTok, since the bio is plain text. Probably, not certainly.
- If you email a buyer anyway (about tracking, say), you can add one line: "Where did you hear about ORU?" Keep it to that one question.

### Visits: platform clicks

There's no visitor counter on the site. Google Analytics isn't installed.
So "visits" here means the clicks each platform reports.
Platforms count differently, so use these to compare channels, not as exact numbers.

### Weekly log

Fill this in every Wednesday (Days 7, 14, 21, 28) and on Day 30.

| Week ending | TikTok views (all posts) | TikTok US viewers % | TikTok profile views | Facebook link + button clicks | Reddit post views | Search Console clicks | Sales (source of each) |
|---|---|---|---|---|---|---|---|
| Wed Oct 14 (Day 7) | | | | | | | |
| Wed Oct 21 (Day 14) | | | | | | | |
| Wed Oct 28 (Day 21) | | | | | | | |
| Wed Nov 4 (Day 28) | | | | | | | |
| Fri Nov 6 (Day 30) | | | | | | | |

Rule of thumb, not verified: about 100–300 visits per sale. Add up the clicks before reading anything into zero sales.
