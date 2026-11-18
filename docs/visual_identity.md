# Tech Nebraska — Visual Identity & Design Standards

**Status:** Corebook-aligned reference, updated 2026-11-18 from client-provided official Corebook excerpts, screenshots, and downloaded asset files.  
**Authority:** [Official Tech Nebraska Corebook](https://my.corebook.io/tech-nebraska).  
**Scope:** This document records rules evidenced in the supplied sections. Where a rule is not in Corebook, it is identified as XPM editorial guidance rather than an official requirement.

## 1. Official brand palette

| Corebook color | HEX | RGB |
|---|---|---|
| Light blue / off-white | `#D2E4F2` | 210, 228, 242 |
| Orange | `#FF4C00` | 255, 76, 0 |
| True blue | `#0080C7` | 0, 128, 199 |
| Green | `#00BA6F` | 0, 186, 111 |
| Yellow / goldenrod | `#FFB900` | 255, 185, 0 |
| Grey-black / obsidian | `#241F20` | 36, 31, 32 |
| Pink | `#FC9FC9` | 252, 159, 201 |
| Purple | `#9877BE` | 152, 119, 190 |
| Light teal / cyan | `#67D2DF` | 103, 210, 223 |

The Corebook supplies Pantone, CMYK and RGB values as well. Use the official guide or the supplied Adobe swatches for print output. Preserve the original swatches rather than estimating color conversions.

## 2. Color gradients and grainy graphic elements

The official Corebook illustrates nine gradient combinations:
1. `#FFB900` → `#FF4C00`
2. `#0080C7` → `#D2E4F2`
3. `#FC9FC9` → `#D2E4F2`
4. `#FFB900` → `#FC9FC9`
5. `#0080C7` → `#FC9FC9`
6. `#FC9FC9` → `#FF4C00`
7. `#FFB900` → `#67D2DF`
8. `#0080C7` → `#00BA6F`
9. `#FC9FC9` → `#9877BE`

These are color-pair references, not a claim that every gradient angle, midpoint, blending algorithm or background is prescribed.

**Official graphic-elements rationale (provided Corebook):** Grainy, orb-like elements are used at a large scale. Blending methods let brand colors interact and create new colors where they meet, expressing community within the technology sector. For production, use approved source assets, including rendered backgrounds in `assets/backgrounds/rendered_4k/` when accessible.

## 3. Official typography

- **Primary:** **Gilgan Regular** and **Work Sans** family (all weights shown in the type specimen).
- **Secondary:** **Space Grotesk**, for **bug type, buttons and other small details**; it is **not** the preferred headline font.
- **Fallback when Gilgan Regular is unavailable:** **Helvetica Neue, Nimbus Sans, Arial** type families.
- **Example text hierarchy:** Subhead, headline, body, and small emphasis, as illustrated by Corebook. These examples are guides for cross-channel consistency and not rigid mandatory size rules.

Do not redistribute proprietary font files outside permitted workflows.

## 4. Logo, brandmark and correct usage

- **Preferred:** Full-color brandmark with the Tech Nebraska wordmark.
- **Approved alternatives:** Off-white and black versions where a single-color treatment is needed.
- **Clear space:** Cushion space around the logo **equal to the width/diameter of one of the three circles within the brandmark**, as illustrated in Corebook. Do not use the previous instruction referring to the height of the entire state/brand icon.
- **Prohibited:** Warping/distorting the logo; recoloring it; changing the brandmark's position relative to the wordmark. Consult official 'Do not' examples before applying any other treatment.
- The brandmark represents knowledge transfer, new professional connection and the collective power of people working together.

Source logo variants are in `assets/logos/` and the official client download packages. Preserve their proportions.

## 5. Contrast and accessibility

Corebook includes example ratios for **text on White** and **text on Grey Black**; examples shown in the supplied screenshots:

| Text color | White background | Grey Black background |
|---|---:|---:|
| Off White | 16.26:1 shown for dark/off-white reference in chart* | 12.49:1 shown for off-white on dark |
| Purple | 4.54:1 | 3.54:1 |
| True Blue | 4.25:1 | 3.8:1 |
| Orange | 3.34:1 | 4.87:1 |
| Green | 2.54:1 | 6.39:1 |
| Light Teal | 2.05:1 | 7.94:1 |
| Pink | 1.92:1 | 8.47:1 |
| Yellow | 1.72:1 | 9.44:1 |

*Note: The first 16.26:1 light-chart column is visually labeled 'Off White' against 'White' in a compact screenshot, but such a ratio is not plausible for two light colors; it likely represents dark grey-black text and must **not** be used as a machine-readable WCAG determination. Rely on official screenshot and independently measured pairings for compliance.*

**Practical rule:** Evaluate the actual text/background pairing at the actual type size. The screenshots illustrate regular text, large text and decorative graphic components as distinct applications; do not infer blanket approval for all uses of an accent. When accessibility matters, independently check WCAG contrast using final pixel colors and display sizes. The background chart is labeled **White** and **Grey Black**, not the surrounding blue page background.

## 6. Photography and content-creative distinction

**Corebook status:** The user confirmed that the Corebook has **no separate photography or design section** beyond the logo, palette, typography, gradients and graphic elements reviewed. Do not present unverified photography preferences as formal Corebook requirements.

**Separate editorial direction, sourced from Emily's communications (not Corebook):** Prefer real people, meaningful moments and authentic/candid community photography when appropriate. Client approval still applies to final image selection, particularly event and Thanksgiving posts. See [Decisions & Feedback Ledger](./decisions_feedback_ledger.md).

## 7. Historical XPM interpretations (retained; superseded where inconsistent)

The repository's prior visual identity file contained these working interpretations:
- An **80/20 neutral canvas versus vibrant accent** ratio, describing only black/off-white and blue/yellow/cyan. This is **historical XPM design guidance**, **not confirmed as a Corebook mandate** from the supplied material. Do not require 80/20 or restrict colors to those five without further explicit authority.
- Gradient backgrounds described primarily as electric blue/goldenrod/cyan on black. Superseded as a complete inventory by the nine Corebook gradients and all nine colors.
- **Space Grotesk for display headings and technical metrics** and Work Sans for body/interface text. **Superseded** by Corebook's Gilgan Regular + Work Sans primary and Space Grotesk secondary hierarchy.
- Logo clear space described as equal to the **height of the state icon**. **Superseded** by Corebook's **circle-width** clear-space reference.

**Change record:** TN-01 approved by Hunter on 2026-11-18. No production assets or publishing calendars were altered by this documentation revision.
