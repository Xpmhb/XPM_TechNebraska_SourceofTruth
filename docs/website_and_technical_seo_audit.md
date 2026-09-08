# Website & Technical SEO Audit

> **ClickUp Task:** [`86bbv8jvv`](https://app.clickup.com/t/86bbv8jvv)
> **Parent Initiative:** [Tech Nebraska: Summit Proposal](https://app.clickup.com/t/86bbv8jum)
> **Status:** `executed`
> **Synced:** September 8, 2026

---

🏆 Master Website & Technical SEO Audit: Tech Nebraska

Target Organization: Tech Nebraska (https://technologynebraska.com/)
Institutional Classification: Independent 501(c)(6) Statewide Technology Trade Association (formerly under Nebraska Chamber of Commerce)
Executive Lead: Emily Allen, Executive Director
Internal Account Approver: Hunter Bergman (hunter@xpm.agency / User ID: 84261539)
Audit Conducted By: XPM Agency Growth Engineering & Technical SEO Team
Evaluation Date: September 4, 2026
Data Sources: Live Site Crawl & DOM Extraction, SE Ranking Remote MCP API, DataForSEO Labs, Google AI Grounding Telemetry, and Regional Association Benchmarking

1. Executive Summary & Composite Health Score

Overall Website Score: 54 / 100 (Grade: D+)
Current Status: Foundationally functional, but critically under-indexed and disconnected from search engines, event carousels, and inbound conversion funnels.
Target Score Post-Management (60 Days): 92 / 100 (Grade: A)

Category Breakdown
Structured Data & Schema: 32 / 100 (F) - Broken Event JSON-LD, 0 calendar schema
On-Page SEO & Metadata: 40 / 100 (F) - 100% missing meta descriptions on core navigation
CRO & Conversion Funnel: 52 / 100 (D) - Raw mailto: button & broken Circle.so tokens
Technical & Crawlability: 58 / 100 (D+) - Crawl-delay: 10, legacy 404 routes
Content Authority & E-E-A-T: 68 / 100 (C+) - Strong blog topics, but missing policy pillar & member directory
Speed, Security & Mobile: 76 / 100 (C) - Secure SSL, but heavy Divi CSS bloat & uncompressed sitemap images

2. Institutional Heritage & The Spin-Off Disconnect

Tech Nebraska was originally incubated in 2023 under the Nebraska Chamber of Commerce & Industry (nechamber.com) and recently transitioned into an independent 501(c)(6) trade association.

Forensic Link Findings (SE Ranking MCP)
Total Inbound Backlinks: 431
Total Referring Domains: 59 (Only 30 DoFollow)
Single-Source Dependency: 307 of 431 backlinks (71.2%) come from nechamber.com
Academic & Governmental Gap: 0 .edu backlinks and 0 .gov backlinks
Authority Comparison: Tech Nebraska holds Domain Rank 34, compared to Bio Nebraska (59), Nebraska Chamber (67), and TechPoint Indiana (84).

3. High-Priority Technical & Schema Vulnerabilities

A. Broken 2026 Tech Summit Event Schema
On /event/2026-tech-summit-what-we-build-next/, native JSON-LD has fatal defects:
Organizer.name is empty ("").
Location.address is a plain string, NOT a Google-required structured PostalAddress.
Missing offers (pricing, availability, registration URL).
Missing description and non-ISO timezone offsets.
Result: The Summit is completely disqualified from the Google Events Rich Carousel.

B. 100% Missing Meta Descriptions
Core pages (Home, /membership/, /events/, /contact/, /meet-the-team/) have zero meta descriptions entered in Yoast SEO. Google generates arbitrary, low-CTR text snippets.

C. The Broken Membership Conversion Flow
On /membership/, the primary "Become a Member" button is a raw mailto: link (mailto:emily@technologynebraska.com?subject=...), which fails on webmail and mobile devices.
On /memberships/submission-form/, the CTA links out to an external Circle.so invitation token, forcing enterprise executives into a community forum login before applying.
4 Conflicting URLs: /membership/, /memberships/, /membership-levels/, and /memberships/submission-form/ create internal cannibalization.

D. Crawl Throttling & 404 Hygiene
robots.txt contains Crawl-delay: 10, unnecessarily throttling search engine indexation.
/about, /join, and /news return hard 404 errors instead of 301 redirects.

4. Statewide Keyword Opportunity Matrix (Top 10 Terms)

Keyword Monthly Vol KD% Current Rank Target Landing Page Strategic Opportunity
nebraska conferences 720 0% Pos 18 /events/ Striking Distance:  Push into Top 3 with H2 optimization
technology companies in omaha 90 0% Pos 21 /  (New Directory) Build Member Directory to capture B2B searches
omaha tech companies 90 0% Pos 23 /  (New Directory) High conversion potential for enterprise recruitment
nebraska tech summit 50 0% Pos 1 /summit/ Dominate SERP with Event Schema rich snippets
tech companies in lincoln ne 60 0% Pos 20 /  (New Directory) Target Lincoln / Silicon Prairie startup leaders
cio nebraska / nebraska cio 100 0% Pos 23-27 /meet-the-team/ Optimize Advisory Board page for CIO queries
omaha conferences 70 3% Pos 35 /events/ Aggregate tech talks and regional summits
nebraska cyber security conference 30 0% Pos 41 /events/ Highlight cybersecurity summit tracks
join nebraska tech council 20 0% Unranked /membership/ High-intent corporate member acquisition
tech workforce development nebraska 30 0% Unranked /policy/  (New) Key term for state grants & STEM advocacy
5. Corporate Member Backlink Acquisition Matrix (Top 15 Targets)

Despite representing over $100B in combined corporate value, only 1 member (IP Pathways) currently links to Tech Nebraska. The remaining 15 premier members provide zero domain authority:

Kiewit (kiewit.com | DR 78) - Advisory Board Chair Chris Dill announcement page
Mutual of Omaha (mutualofomaha.com | DR 82) - Fintech Innovation Partner spotlight
Union Pacific (up.com | DR 85) - Digital Transformation Partner feature
Google (about.google | DR 98) - Midwest Regional Impact / Data Centers community link
Verizon (verizon.com | DR 92) - State & Local Government Affairs / 5G working group link
FNBO (fnbo.com | DR 74) - Community Partnerships / Newsroom
Nelnet (nelnet.com | DR 76) - Innovation Hub / Danielle Egr Tech Talk recap
Werner Enterprises (werner.com | DR 69) - Logistics Innovation Summit partner badge
Farm Credit Services (fcsamerica.com | DR 64) - AgTech Autonomy Session spotlight
Scott Data Center (scottdatacenter.com | DR 52) - Partner Ecosystem directory link
GyanSys (gyansys.com | DR 58) - Gold Sponsor event announcement blog post
McGrath North (mcgrathnorth.com | DR 54) - Advisory Board appointment press release
Hawkins Construction (hawkins1.com | DR 48) - Infrastructure Technology partnership badge
Farmers Mutual of NE (fmne.com | DR 51) - InsurTech Working Group affiliation
Gradera (gradera.com | DR 42) - Founder Lightning Talks recap link

6. The Proposed Solution: Monthly Website Management Retainer

Retainer Scope of Work (4 Core Pillars)

Pillar 1: Full-Stack WordPress & Divi CMS Governance
Weekly staging-first updates (Core, Divi, DiviFlash, Yoast, WP Event Manager).
Continuous 404 monitoring and 301 redirect maintenance.
Core Web Vitals maintenance (LCP < 2.2s, CLS < 0.05).
24/7 security scanning, firewall monitoring, and daily off-site cloud backups.

Pillar 2: Event Discoverability & Schema Automation Engine
Google-compliant Event JSON-LD injection for all Summits & Tech Talks.
Migration to an evergreen summit architecture (/summit/) preserving 100% of historical backlinks.
Regional event syndication to Midwest tech calendars.

Pillar 3: Corporate Member Acquisition & Directory Engine
Build and curate an interactive Nebraska Tech Company Directory indexing corporate partners.
Distribution of the "Proud Member of Tech Nebraska" digital badge kit to capture high-authority backlinks.
Complete overhaul of /membership/ to eliminate mailto: links and launch a streamlined 4-step application form.

Pillar 4: Policy Thought Leadership & AI Search (AEO) Optimization
Structure Nebraska AI and workforce policy reports into search-optimized pillar hubs.
Implement FAQPage and entity schema to win citations in Google AI Overviews and ChatGPT Search.
Monthly Looker Studio growth telemetry tracking keyword ranks, member inquiries, and ticket sales.

Retainer Pricing Options
Growth Retainer (Recommended): 20 Hours / month - $3,250 / month (CMS Governance, Event Schema, Membership CRO, Member Link Engine)
Enterprise Ecosystem Retainer: 35 Hours / month - $5,500 / month (Includes Full Interactive Member Directory, Monthly Policy Pillar Publishing, and Custom Event Design Sprints)

7. 30-Day Quick-Win Roadmap

Week 1: Deploy validated Google Event Schema on 2026 Tech Summit; remove Crawl-delay: 10; resolve 404 redirects.
Week 2: Replace raw mailto: link on /membership/ with clean lead form; populate 100% missing meta descriptions; update Homepage H1.
Week 3: Distribute Member Badge Kit to top 15 corporate members; optimize /events/ for nebraska conferences.
Week 4: Launch live Looker Studio executive telemetry dashboard; deliver Month 1 report to Emily Allen and Board.