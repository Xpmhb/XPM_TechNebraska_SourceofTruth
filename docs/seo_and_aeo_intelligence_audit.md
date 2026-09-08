# Tech Nebraska: Search Engine (SEO) & Answer Engine (AEO) Intelligence Audit

**Domain:** `technologynebraska.com`  
**Operating Agency:** XPM Agency  
**Target Repository:** [`Xpmhb/XPM_TechNebraska_SourceofTruth`](https://github.com/Xpmhb/XPM_TechNebraska_SourceofTruth)  
**Data Sources:** SE Ranking Remote MCP API, WordPress Divi Site Crawl, Backlink Authority Graph  
**Audit Date:** September 8, 2026  
**Status:** Canonical Baseline Audit  

---

## 1. Executive Search Baseline & Authority Metrics

Tech Nebraska has established a solid baseline of digital authority since its 2023 founding in partnership with the Nebraska Chamber of Commerce & Industry, but its search presence is almost entirely **passive and brand-dependent**.

```
+-------------------------------------------------------------------------------------------------------------------------+
| TECH NEBRASKA HISTORICAL SEO BASELINE (SE RANKING BENCHMARKS)                                                           |
+-----------------------------------+--------------------+----------------------------------------------------------------+
| Metric                            | Value              | Diagnostic Meaning & Implication                               |
+-----------------------------------+--------------------+----------------------------------------------------------------+
| Domain Inlink Rank (Authority)    | 34 / 100           | High authority for a young association; strong trust ceiling.  |
| Total Backlinks                   | 431                | Healthy link profile anchored by Chamber and news mentions.   |
| Referring Domains (RefDomains)    | 59 domains         | 91% Dofollow (392 links across 30 dofollow root domains).      |
| Total Ranked Organic Keywords     | 125 worldwide      | 50 top US keywords tracked; heavily weighted to exact-match.   |
| Monthly Organic Traffic           | ~75 visits/mo      | Captures direct brand searchers; virtually zero non-brand.    |
| Paid Search (PPC / Google Ads)    | $0 (0 keywords)    | Zero paid search capture for "Nebraska tech summit" or grants. |
| CMS Platform                      | WordPress (Divi)   | Heavy CSS/JS bundle, unoptimized for Core Web Vitals.          |
| Schema Markup Coverage            | < 5% (Missing)     | Zero structured JSON-LD for Events, Articles, or Organization. |
+-----------------------------------+--------------------+----------------------------------------------------------------+
```

---

## 2. Organic Keyword Performance Triangulation

We extracted and classified all ranking organic keywords into three performance cohorts:

### A. The Monopoly Cohort: Top 3 Positions (Branded Exact-Match)
Tech Nebraska completely dominates queries containing their exact organization name, occupying Position #1 with sitelinks:
- **`nebraska tech`** — **Rank #1** | Volume: 170 | Difficulty: 18 | Sitelinks on SERP: Homepage, Team, Summit, Events, Membership, Policy.
- **`nebraska technology`** — **Rank #1** | Volume: 170 | Difficulty: 16 | Appears in Google AI Overviews (SGE).

### B. The Striking Distance Cohort: Positions 4–20 (High Opportunity)
Keywords that are currently on Page 2 or the lower half of Page 1 and can be pushed into the Top 3 with targeted on-page optimization:
- **`tech omaha`** — **Rank #5 & #18** | Volume: 50 | Difficulty: 10 | Homepage & Events page ranking; easily captured with dedicated Omaha hub content.
- **`christopher dill`** — **Rank #13** | Volume: 70 | Difficulty: 6 | Advisory Board Chair article.
- **`nebraska technology` (Subpages)** — **Rank #13** | Volume: 170 | Team page ranking.

### C. The Missed Opportunity Cohort: Positions 21+ & Missing Keywords
The website is currently invisible for the most lucrative commercial and high-intent industry queries in Nebraska:
- ❌ **`nebraska tech conference` / `omaha tech summit`** (Invisible)
- ❌ **`nebraska business innovation act` / `BIA prototype grant`** (Invisible despite leading the lobbying!)
- ❌ **`nebraska agtech startups` / `omaha fintech companies`** (Invisible)
- ❌ **`nebraska tech jobs` / `omaha software engineers`** (Invisible)
- ❌ **`nebraska CIO network` / `omaha IT executives`** (Invisible)

---

## 3. Organic Competitor Benchmarking

```
+-------------------------------------------------------------------------------------------------------------------------+
| SEARCH COMPETITOR BENCHMARKING (SE RANKING)                                                                             |
+----+----------------------------+-----------------+-------------------+-------------------------------------------------+
| #  | Competitor Domain          | Total Keywords  | Missing Keywords  | Competitive Gap Analysis                        |
+----+----------------------------+-----------------+-------------------+-------------------------------------------------+
| 01 | techomaha.com              | 84 keywords     | 72 missing        | Captures Omaha local developer & meetup queries |
| 02 | nebraskaitsymposium.com    | 20 keywords     | 11 missing        | Captures corporate enterprise IT summit traffic |
| 03 | nebraskaglobal.com         | 41 keywords     | 36 missing        | Captures software venture and startup queries   |
| 04 | aitpomaha.com              | 33 keywords     | 29 missing        | Captures IT professional association searches   |
| 05 | omahatech.ai               | 4 keywords      | 2 missing         | Early-stage local AI agency/community           |
+----+----------------------------+-----------------+-------------------+-------------------------------------------------+
```

> **Key Insight:** `techomaha.com` and `nebraskaitsymposium.com` currently outrank Tech Nebraska for non-branded tech event traffic despite Tech Nebraska having significantly higher brand prestige, Fortune 500 board members, and Chamber backing.

---

## 4. Technical SEO & Answer Engine Optimization (AEO) Deficiencies

### 1. Zero JSON-LD Structured Data Schema
- Google cannot programmatically understand Tech Nebraska's events, speakers, or board leadership.
- **Missing Schemas:**
  - `Event` schema on `/events/` and `/event/2025-tech-nebraska-summit/` (causing Google to exclude the Summit from rich event snippets and Google Events).
  - `Organization` & `GovernmentPermit` schema detailing their Chamber alliance and non-profit standing.
  - `Person` schema on `/meet-the-team/` for Emily Allen, Brody Deren (Union Pacific), and Chris Dill (Kiewit).
  - `Article` & `NewsArticle` schema on their 22 blog posts, preventing inclusion in Google Discover and News carousel.

### 2. Divi WordPress Bloat & Core Web Vitals
- Built on WordPress with Elegant Themes' **Divi Builder** (`et_blog`).
- Excessive inline styles, uncompressed assets, and heavy DOM depth throttle mobile Core Web Vitals (LCP > 3.8s), hurting mobile search rankings.

### 3. AEO (Answer Engine Optimization) Blindspots
- When users ask AI search engines (**Perplexity, ChatGPT Search, Claude, Google Gemini**) questions like:
  - *"What are the top tech events in Omaha for 2026?"*
  - *"How does the Nebraska Business Innovation Act work for startups?"*
  - *"Who are the leading enterprise CIOs in Nebraska?"*
- Tech Nebraska's site is rarely cited because content is locked inside unstructured WordPress containers without direct, schema-backed answer formatting.

---

## 5. The 4-Month Retainer Growth Roadmap for XPM Agency

This audit directly feeds our proposed **4-Month SEO & Content Retainer** for Executive Director Emily Allen:

```
+-------------------------------------------------------------------------------------------------------------------------+
| 4-MONTH SEO, AEO & CONTENT RETAINER ROADMAP                                                                             |
+-------+-----------------------------+-----------------------------------+-----------------------------------------------+
| Month | Strategic Objective         | Primary Deliverables              | Target KPI Impact                             |
+-------+-----------------------------+-----------------------------------+-----------------------------------------------+
| M01   | Technical SEO Foundation &  | • Inject full JSON-LD Schema suite| • Google Events Rich Snippet activation       |
|       | Summit Event Architecture   | • Optimize Summit 2026 landing pge| • Rank Top 3 for "Nebraska tech summit"       |
|       |                             | • Fix Divi mobile asset caching   | • Core Web Vitals mobile pass score           |
| M02   | BIA Policy & Grant Hub      | • Build "Nebraska BIA Grant Guide"| • Capture 100% of state startup grant queries |
|       | (High-Intent Pillar)        | • Schema-backed FAQ & prototype   | • +150 monthly high-intent founder visits     |
|       |                             |   grant application walkthrough   | • Direct lead pipeline for Startup Showcase   |
| M03   | Enterprise CIO Authority &  | • Launch "Silicon Prairie AI"     | • Citations in Perplexity & Google AI Overviews|
|       | AEO Answer Engine Optimization| interview series (UP, HDR, Kiewit)| • Rank Top 5 for "Nebraska AI adoption"       |
|       |                             | • Structured Q&A schema blocks    | • +200 monthly organic corporate visits       |
| M04   | Regional Hub Expansion &    | • Build Omaha, Lincoln, Norfolk & | • Capture regional search beyond Omaha        |
|       | Competitor Capture          |   Kearney regional ecosystem pages| • Surpass techomaha.com in organic keywords   |
|       |                             | • Capture techomaha keyword gap   | • +500 monthly recurring organic visits       |
+-------+-----------------------------+-----------------------------------+-----------------------------------------------+
```

---

## 6. Verification & Version Control
This SEO baseline document has been saved to the repository at `docs/seo_and_aeo_intelligence_audit.md` and committed to [`Xpmhb/XPM_TechNebraska_SourceofTruth`](https://github.com/Xpmhb/XPM_TechNebraska_SourceofTruth).
