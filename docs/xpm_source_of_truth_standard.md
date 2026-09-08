# XPM Standard Operating Procedure: Client Source of Truth Repository Standard (`XPM-SOP-SOT-001`)

**Version:** 1.0  
**Authority:** XPM Agency Engineering & Brand Strategy  
**Reference Benchmark:** `XPM_TechNebraska_SourceofTruth`  

---

## 1. Purpose & Scope

Every XPM client requires a standardized, version-controlled **Source of Truth (SoT)** repository. The goal is to provide a single, canonical interface that equips human team members and autonomous AI agents (Claude, Gemini, Codex, Cursor) to execute marketing, SEO, design, and software engineering with zero hallucination and 100% brand fidelity.

---

## 2. Mandatory Repository Directory Hierarchy

Every client repository must strictly follow this structure:

```
XPM_[ClientName]_SourceofTruth/
├── README.md                              # Human executive brief & repo index
├── AGENTS.md                              # Master AI operating contract (Universal agent instructions)
├── CLAUDE.md / GEMINI.md                  # Compatibility entry points pointing to AGENTS.md
├── tokens.json                            # Machine-readable design tokens (HEX, RGB, fonts, radii)
├── .gitignore                             # Git hygiene (Tier 3 exclusions)
│
├── docs/                                  # Strategic Documentation
│   ├── brand_strategy.md                  # 7-phase brand strategy, pillars, positioning
│   ├── storybrand_framework.md            # Donald Miller SB7 framework & personas
│   ├── brand_voice_and_tone.md            # Tone spectrum, voice rules, anti-slop dictionary
│   ├── visual_identity.md                 # Design system specifications & layout rules
│   ├── client_profile.md                  # Stakeholder roster, business details, history
│   └── xpm_source_of_truth_standard.md    # This SOP document
│
└── assets/                                # Brand Assets (Three-Tier Standard)
    ├── manifest.json                      # Machine-readable asset index
    ├── logos/                             # SVGs, web PNGs, hi-res 600 DPI masters
    ├── backgrounds/                       # Master 4K backgrounds and previews
    ├── social_proof/                      # Real past flyers, speaker quotes, proof photos
    └── interactive/                       # Standalone offline HTML mood boards & visualizers
```

---

## 3. The Three-Tier Asset Management Standard

1. **Tier 1 (Canonical Digital Masters - Git):** SVGs, transparent PNGs, Favicons, typography references, and `tokens.json`.
2. **Tier 2 (Rendered Production Assets - Git):** Rendered 4K backgrounds, social proof photos, verified event flyers, and standalone HTML tools (<50MB).
3. **Tier 3 (Bulky Working Files - Cloud):** RAW video, multi-GB video footage, PSDs, and InDesign files. Excluded via `.gitignore` and cataloged in `assets/manifest.json` with cloud storage links.

---

## 4. Mandatory Agent Operating Protocols

1. **Read-Only / Proposal Mode:** Zero automated live mutations to production campaigns, CMS, or budgets without explicit human approval.
2. **Hunter Bergman Exclusivity (`AI-TASKOPS-001`):** All sign-offs and notifications must route exclusively to Hunter Bergman (`hunter@xpm.agency` / User ID `84261539`).
3. **Anti-Slop Copywriting Guarantee:** Strict enforcement of client-specific voice and banned AI words list.
