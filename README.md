# XPM_TechNebraska_SourceofTruth
**Organization:** Tech Nebraska (`https://technologynebraska.com/`)  
**Operating Agency:** XPM Agency (`https://xpm.agency`)  
**Account Lead & Strategist:** Hunter Bergman (`hunter@xpm.agency`)  
**Client Executive Director:** Emily Allen (`eallen@nechamber.com`)  
**Governance Partner:** Nebraska Chamber of Commerce & Industry  
**Repository Classification:** XPM Client Source of Truth Standard (Tier 1 Benchmark)

---

## Executive Overview

This repository is the single source of truth for **Tech Nebraska**'s brand identity, strategic positioning, StoryBrand messaging architecture, and verified digital assets.

It is designed for seamless consumption by:
1. **AI Agents & Operating Daemons** (Claude Code, Gemini/Antigravity, Codex, Cursor) via [`AGENTS.md`](./AGENTS.md) and [`tokens.json`](./tokens.json).
2. **Human Creative & Account Teams** at XPM for pitch development, campaign execution, and retainer operations.
3. **Client Leadership & Board Members** for executive presentations and brand governance.

---

## Repository Directory Structure

```
XPM_TechNebraska_SourceofTruth/
├── README.md                              # Human project overview and directory index
├── AGENTS.md                              # Master AI operating contract (Universal agent instructions)
├── CLAUDE.md                              # Agent compatibility entry point
├── GEMINI.md                              # Agent compatibility entry point
├── tokens.json                            # Machine-readable design tokens (Pantone, HEX, typography)
├── .gitignore                             # Git hygiene (Tier 3 asset exclusions)
│
├── docs/                                  # Strategic documentation & brand codex
│   ├── brand_strategy.md                  # 7-phase XPM brand strategy & 3 guiding pillars
│   ├── storybrand_framework.md            # Donald Miller SB7 framework & 3 hero archetypes
│   ├── brand_voice_and_tone.md            # Tone spectrum, voice rules, anti-slop dictionary
│   ├── visual_identity.md                 # Design system specifications & 80/20 ratio rule
│   ├── client_profile.md                  # Entity overview, Chamber alliance, Advisory Board
│   ├── content_and_blog_audit.md          # Complete 22-post editorial analysis & content strategy
│   ├── seo_and_aeo_intelligence_audit.md  # SE Ranking baseline audit, keywords & 4-month roadmap
│   ├── website_and_technical_seo_audit.md # ClickUp task 86bbv8jvv (54/100 baseline, schema defects, 15 member backlink targets)
│   ├── social_media_and_campaign_audit.md # ClickUp task 86bbv9ha8 (LinkedIn, FB, 74-post Instagram forensic crawl)
│   ├── competitive_intelligence_benchmark.md # ClickUp task 86bbva8yv (TAI, TechPoint, AIM, Bio NE, YouTube audit)
│   ├── clickup_comprehensive_strategy_and_brief.md # ClickUp doc 8cfvj6d-37514 (Master Content Strategy, Ideas & Summit Retainer Brief)
│   ├── six_month_content_strategy_core_document.md # Master 6-Month Content Strategy ($14,400 Core Engagement SOW & Editorial Architecture)
│   └── xpm_source_of_truth_standard.md    # Agency SOP for setting up future client repos
│
└── assets/                                # Verified Brand Assets
    ├── manifest.json                      # Machine-readable asset inventory with metadata
    ├── fonts/                             # Official TTF variable fonts (Space Grotesk, Work Sans)
    ├── logos/
    │   ├── svg/                           # Master Bézier vector source of truth (4 marks, 5 icons)
    │   ├── png_web/                       # Transparent web PNGs (3200px wordmarks / 1900px icons)
    │   └── png_hires/                     # 600 DPI print-ready PNGs (up to 12,800px)
    ├── backgrounds/
    │   ├── rendered_4k/                   # 8000x4500 PNG master grainy orb collisions
    │   ├── previews/                      # 1200x675 lightweight JPG previews
    │   └── production_pdfs/               # Vector background PDF artwork (Tier 3 on disk)
    ├── social_proof/                      # 19 authentic past campaign flyers & speaker quotes
    ├── generated_suite/                   # 6 production marketing graphics (1:1, 16:9, 4:5, 9:16)
    └── interactive/                       # Standalone offline HTML applications
        ├── tech_nebraska_brand_moodboard.html        # Living Strategy, Growth Engine & Brand Intelligence OS (Interactive)
        ├── tech_nebraska_sb7_journey_visualizer.html # Interactive SB7 3-Hero Archetype Journey Visualizer
        └── tech_nebraska_graphics_suite_viewer.html  # Production Graphics Suite Viewer & Export Console
```

---

## The Three-Tier Asset Standard

To keep the repository fast, lightweight, and agent-accessible while preserving total asset fidelity, assets follow the **XPM Three-Tier Asset Standard**:

* **Tier 1: Canonical Vectors & Digital Masters (Committed in Git)**
  - Vector SVGs, transparent PNGs, Favicons, typography references, and `tokens.json`.
* **Tier 2: Production Rendered Assets (Committed in Git)**
  - Rendered 4K backgrounds, social proof photos, verified event flyers, and interactive web tools.
* **Tier 3: Bulky Working Files (Excluded from Git, Cataloged in Cloud)**
  - Multi-gigabyte RAW camera footage, unedited b-roll, massive layered PSDs and InDesign working files are excluded via `.gitignore` and cataloged in [`assets/manifest.json`](./assets/manifest.json) with cloud storage links.

---

## Agent Usage Quickstart

For any AI agent operating in this repository or writing copy/code for Tech Nebraska:
1. Load [`AGENTS.md`](./AGENTS.md) as your primary operating contract.
2. Query [`tokens.json`](./tokens.json) for all color hex codes, font families, and radii.
3. Review [`docs/brand_voice_and_tone.md`](./docs/brand_voice_and_tone.md) to enforce zero AI slop.
4. Enforce strict **Hunter Bergman Exclusivity** (`AI-TASKOPS-001`) — all changes operate in Read-Only / Proposal mode.
