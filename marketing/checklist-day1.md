# Day 1 checklist · Thu Oct 8

About an hour in total.

- **A. The repo and the money path** (about 22 min). Do this first. A0 comes before anything else.
- **B. Accounts** (about 25 min, plus the Facebook group list).
- **C. Quick wins** (about 12 min). Can slip to Day 2.

A and B1–B3 are the core 47 minutes. The group list (B4) can finish by Day 3.

**Stop rule:**
- No posts anywhere and no Reddit account until the GitHub repo shows **Private** (A0).
- If anything else in section A fails, don't schedule a post yet. A post that sends people to a broken checkout is worse than no post.

"Check in the app" means the menu names may have moved. The goal stays the same.

---

## A. The repo and the money path

### A0. Make the GitHub repo private, before anything is posted (2 min)

- [ ] github.com → your **Webstite** repo → **Settings** → **General** → scroll to **Danger Zone** → **Change visibility** → **Private** → confirm.
- **Look for:** a "Private" badge next to the repo name.
- Why: this marketing folder, the anonymous-Reddit plan and the Israel-time schedule are already in that repo, and its history holds retired drafts and claims. The account name points to you. Deleting files doesn't remove them from history. Private does hide them.
- Until it shows Private: don't push anything more to that repo, don't post anywhere, and don't make the Reddit account.

If it fails:
- No Settings tab: you're not logged in as the owner. Log in as the account that owns the repo.
- If GitHub Pages was serving anything from this repo, that stops on a free plan. Nothing in this plan needs it.

### A1. Northflank boot line (3 min)

- [ ] Northflank → your project → service `oru-shop` → **Logs**. Search the log for `ORU running on`.
- **Look for exactly:** `ORU running on https://wearoru.com (paypal LIVE)`
- [ ] Also look for any line starting with `WARNING:`.

If it fails:
- It says `sandbox`: `oru-shop` → **Environment** → set `PAYPAL_ENV` to `live` (lowercase) → save. It redeploys. Check the log again.
- The address isn't `https://wearoru.com`: set `SITE_URL` to `https://wearoru.com` → save → check again.
- No boot line at all (old logs rolled off): restart the service once (check in the app where), then look again.
- You see a `WARNING:` line: copy it to Claude.

### A2. The alert reaches your phone (4 min)

- [ ] `oru-shop` → **Environment**: `ALERT_WEBHOOK` is set. It should be a Discord webhook address starting `https://discord.com/api/webhooks/`. Copy it.
- [ ] Send a test from your computer. Open Windows PowerShell and paste this, with your address in place of `PASTE_THE_URL`:

```
Invoke-RestMethod -Method Post -Uri "PASTE_THE_URL" -ContentType "application/json" -Body '{"content":"ORU alert test"}'
```

- **Look for:** "ORU alert test" in the Discord channel, and a notification on your phone.
- [ ] Second test, through the live site: on wearoru.com, join the email list with your own address.
- **Look for:** a `new subscriber: …` message in the same channel. (This uses `SUBSCRIBE_WEBHOOK`, or `ALERT_WEBHOOK` if that one isn't set.)

If it fails:
- Nothing in Discord: the address is wrong or the webhook was deleted. Discord → Server Settings → Integrations → Webhooks → New Webhook → pick the channel → Copy Webhook URL. Paste it into `ALERT_WEBHOOK` and `SUBSCRIBE_WEBHOOK` in Northflank → save → test again.
- Discord gets it but your phone stays quiet: in the Discord phone app, long-press the channel → Notifications → All Messages. Then check your phone allows Discord notifications.

Why it matters: this is where the NEW SALE message lands (with the source, once the site update is live), and the warning if a paid order doesn't reach production.

### A3. Printify: card on file, and the neck label (5 min)

- [ ] Printify → your account menu → **Billing** (or Payment methods): a card or a balance is there.
- If not: add one. Paid orders go to production straight away and Printify charges you then. With no card, a buyer pays and nothing gets made.
- [ ] Printify → **My products** → Watts tee. Note the print provider it uses (ID 217 in our setup).
- [ ] Open the same blank in the **Catalog**, with that provider selected. Read the product details for the neck label.
- **Look for:** "tear-away label", or a printed (tagless) label.
- [ ] Write down only one word: tear-away, printed, or can't tell. Don't copy the blank's name anywhere.

If it fails:
- Printed label: tell Claude. The product page says "Label: tear-away", which would then be wrong, and buyers would see the blank maker's name inside the collar. We fix the page. Don't promise a custom label; it may cost money.
- Can't tell: say so. The sample will settle it.

### A4. PayPal: "PayPal account optional" (4 min)

- [ ] paypal.com → log in to the business account → **Settings** (gear) → Account settings → **Website payments** → Website preferences → **Update**.
  PayPal moves these menus. If you can't find it, search PayPal Help for "PayPal account optional".
- [ ] Set **PayPal account optional** to **On** → Save.
- **Look for:** the setting still shows On after you reload the page.

If it fails:
- The option isn't there: write that down and tell Claude. Some accounts or regions don't get it. We'd then add one line near the Checkout button that says how payment works.

### A5. Free smoke test (4 min). Don't pay.

- [ ] Open a private or incognito window, so you're logged out of PayPal.
- [ ] Go to wearoru.com/product-watts → Black → M → **Add to bag** → open the bag → **Checkout**.
- **Look for:** a paypal.com page (not sandbox.paypal.com) that shows ORU, $56 and free shipping.
- **Look for:** a way to pay by card without logging in. The wording varies, for example "Pay with Debit or Credit Card".
- [ ] Click "Cancel and return to ORU", or close the tab. **Don't pay.** A completed payment goes straight to production, and Printify charges your card.

If it fails:
- You land on sandbox.paypal.com: `PAYPAL_ENV` isn't live. Go back to A1.
- The bag shows an error, or nothing happens: note the time, look at the Northflank log for that minute, and send both to Claude. Don't promote until this works.
- No card option: PayPal decides this per buyer and per country. Not seeing it from Israel doesn't prove US buyers won't see it. Note what you saw and tell Claude.

---

## B. Accounts

### B1. TikTok (7 min)

- [ ] TikTok app → **Profile** → ☰ (top right) → **Settings and privacy** → **Account** → **Switch to Business Account** → pick the closest category (clothing or apparel; check in the app) → done.
- [ ] Profile → **Edit profile** → is there a **Website** field?
  - Yes: paste the TikTok link from `utm-links.md` → save → tap it on your profile and check it opens the Watts tee page.
  - No: that's expected at 0 followers. Leave it.
- [ ] Bio: paste the bio from `captions.md`. It's plain text with `wearoru.com` at the end. Check the length limit in the app.
- [ ] Don't start "business verification" today. It needs a business registration document and may show a name in public. Decide later, with anonymity in mind.
- [ ] On the computer, open **TikTok Studio** (web) → **Upload**. Check three things and write yes or no:
  - Is there a **Schedule** option?
  - Is **Disclose commercial content** there before you schedule?
  - Is **AI-generated content** there before you schedule?
  If any answer is no, the phone fallback in `calendar.md` applies.

If it fails:
- The bio won't save the address: write down what happened and tell Claude. The end card and the pinned comment still carry it.

### B2. Reddit (15 min)

- [ ] reddit.com → **Sign up** with an email. Username: a neutral rider handle. Not "ORU", not your name or initials, not your town, not a handle you use anywhere else.
- [ ] Verify the email.
- [ ] Leave the profile plain: no bio link, no ORU, no photo of you.
- [ ] Join r/eMountainBike, r/ebikes, r/MTB and r/mountainbiking.
- [ ] Search for **r/emtb**. Write down: does it exist? If yes, how many members, and how recent are the newest posts? If it's active, join it too.
- [ ] In each sub, read the **Rules** (desktop: right sidebar; app: the About tab), the pinned posts, and the wiki if there is one. Fill in the table below.
- [ ] In each sub, open **Create post** but don't post. Note whether Reddit shows an eligibility notice or a "Post Check". Where these appear varies; check in the app. Close without posting.
- Never: mention ORU, link wearoru.com, or make a second account. Days 1–14 are warm-up only.

If it fails:
- Sign-up asks for something you can't give, or blocks you: stop and tell Claude. Don't borrow anyone else's account or number.

| Sub | Self-promo allowed? | "I made this" or merch posts? | Promo thread or day? | Flair needed? | Links allowed? | Eligibility notice? |
|---|---|---|---|---|---|---|
| r/eMountainBike | | | | | | |
| r/ebikes | | | | | | |
| r/MTB | | | | | | |
| r/mountainbiking | | | | | | |
| r/emtb (if it exists) | | | | | | |

### B3. Facebook Page "Shop now" button (4 min)

- [ ] Switch to the ORU Page: your profile picture (top right) → **See all profiles** → ORU.
- [ ] On the Page, under the cover photo: **Add action button** (or Edit action button) → **Shop now** → paste the Facebook link from `utm-links.md` → Save. The option may sit under "Shop" or similar; check in the app.
- **Look for:** tapping the button opens the Watts tee page.
- The rest of the Page setup (cover, Intro, About, link preview, pinned intro post) is `facebook.md` §1, on Day 2.

If it fails:
- "Shop now" isn't offered: use "Learn more" with the same link, and tell Claude.

### B4. Facebook group list (20 min; finish by Day 3)

Do all of this as the ORU Page. Never join a group as yourself.

- [ ] Search: "eMTB", "electric mountain bike", "Levo owners", "Trek Rail owners", "Orbea Rise", "Heckler", and "<US state> eMTB".
- [ ] Open each group's own page. The option to join as a Page only shows there, not in the search results (check in the app).
  - You can join as ORU: Pages are allowed. Note it.
  - Only your personal profile is offered: skip the group.
- [ ] Read each group's About → Rules. Note what they say about selling or promotion.
- [ ] List 8–12 groups that allow Pages. Join a few today and the rest over week 1.

Leads to check (names seen secondhand, not verified; some may lean UK): eMTB Enthusiasts, eMTB Riders Group, Electric Mountain Bike Group, Electric Bike Enthusiasts, E-Bikes of America, and owner groups for specific bikes. US groups first.

| Group | Link | Members | Posts a day | Pages allowed? | Promo rules | Joined? |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |

---

## C. Quick wins

### C1. Google Search Console (10 min, plus waiting)

- [ ] search.google.com/search-console → **Add property** → **Domain** → type `wearoru.com` → copy the TXT record it shows.
- [ ] Porkbun → Domain Management → wearoru.com → **DNS** → add a record: Type **TXT**, Host left empty, Answer = the `google-site-verification=…` text → Save.
- [ ] Back in Search Console → **Verify**.
- [ ] Once verified: **Sitemaps** → type `sitemap.xml` → **Submit**.
- **Look for:** Verified, then sitemap status "Success".
- [ ] Later, once Claude says the site fixes are live: **URL inspection** → `https://wearoru.com/product-watts.html` → **Request indexing**.
- Don't set up Merchant Center yet. It waits for real photos.

If it fails:
- "Not found" when you verify: wait 15–60 minutes and try again. DNS can take longer.
- Sitemap says "Couldn't fetch": common at first. Check again tomorrow.

### C2. Strava profile link (2 min), only if it keeps you anonymous

- [ ] First check: does your Strava profile show your real name, your face, or where you live? If yes, **skip this step.** Anonymity beats one link.
- [ ] If it's clean: Strava → your profile settings → the bio or website field (check in the app) → paste the Strava link from `utm-links.md` → Save.
- Don't post links in Strava clubs (regular members can't), and don't promote in the Strava Community Hub.

---

## D. Send Claude the results

Copy this, fill it in, send it:

```
A0 GitHub repo private: yes / no
A1 boot line: LIVE / sandbox / other: ___
A2 alert test reached phone: yes / no. Signup test: yes / no
A3 card on Printify: yes / no. Neck label: tear-away / printed / can't tell
A4 PayPal account optional: on / not found
A5 smoke test: reached PayPal page yes / no. Total shown: ___. Card option seen: yes / no
B1 TikTok business: yes. Website field: yes / no. Web scheduler: yes / no. Both toggles on web: yes / no
B2 Reddit account made: yes. r/emtb exists: yes / no. Rules table filled: yes / no
B3 Shop now button works: yes / no
B4 groups listed: ___. Pages allowed in: ___. Joined so far: ___
C1 Search Console verified: yes / no. Sitemap: success / couldn't fetch / not yet
C2 Strava: done / skipped (anonymity)
```
