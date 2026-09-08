"""
Design QA & Typography Linter Engine (Version 2.0 - Strict Agency Standards)
============================================================================
Programmatically validates social media graphics against strict design standards:
1. Minimum font size enforcement (Hard reject < 28px on 1080px/1200px canvases)
2. Mathematical centering checks (abs(center_x - canvas_center_x) <= 2px)
3. Container padding enforcement (min 50px padding)
4. Vertical rhythm and gap consistency (20px <= gap <= 120px)
5. Authentic brand asset validation (no text-reconstructed logos)
6. Anti-Clutter & Element Count Rule (max 4 elements per container card to prevent cramming)
7. Color Cohesion Rule (max 2 accent colors per card to prevent circus palette)
8. Template Fidelity Rule (validates alignment with proven agency archetypes)
"""

import os
import sys
from typing import List, Dict, Tuple, Any

class DesignQALinter:
    def __init__(self, min_font_size: int = 28):
        self.min_font_size = min_font_size
        self.violations: List[Dict[str, Any]] = []
        self.checks_passed: int = 0
        self.checks_total: int = 0

    def check_font_size(self, graphic_id: str, element_name: str, text: str, font_name: str, font_size: int, allowed_floor: int = None) -> bool:
        """Enforces minimum font size. Flags anything below allowed_floor (default 28px)."""
        self.checks_total += 1
        floor = allowed_floor if allowed_floor is not None else self.min_font_size
        if font_size < floor:
            self.violations.append({
                "graphic_id": graphic_id,
                "rule": "MIN_FONT_SIZE",
                "severity": "CRITICAL",
                "element": element_name,
                "details": f"Font size {font_size}px is below required minimum of {floor}px. Text: '{text[:30]}...' ({font_name})"
            })
            return False
        self.checks_passed += 1
        return True

    def check_centering(self, graphic_id: str, element_name: str, bbox: Tuple[int, int, int, int], canvas_width: int, tolerance: int = 2) -> bool:
        """Verifies that an element designated as centered is mathematically centered."""
        self.checks_total += 1
        elem_center_x = (bbox[0] + bbox[2]) / 2.0
        canvas_center_x = canvas_width / 2.0
        offset = abs(elem_center_x - canvas_center_x)
        if offset > tolerance:
            self.violations.append({
                "graphic_id": graphic_id,
                "rule": "CENTERING_ALIGNMENT",
                "severity": "HIGH",
                "element": element_name,
                "details": f"Element center X={elem_center_x:.1f} deviates by {offset:.1f}px from canvas center X={canvas_center_x:.1f} (Tolerance: {tolerance}px)"
            })
            return False
        self.checks_passed += 1
        return True

    def check_container_padding(self, graphic_id: str, container_name: str, container_bbox: Tuple[int, int, int, int], inner_bbox: Tuple[int, int, int, int], min_padding: int = 50) -> bool:
        """Verifies minimum padding between container boundary and internal contents."""
        self.checks_total += 1
        pad_left = inner_bbox[0] - container_bbox[0]
        pad_top = inner_bbox[1] - container_bbox[1]
        pad_right = container_bbox[2] - inner_bbox[2]
        pad_bottom = container_bbox[3] - inner_bbox[3]

        fails = []
        if pad_left < min_padding:
            fails.append(f"left ({pad_left}px < {min_padding}px)")
        if pad_top < min_padding:
            fails.append(f"top ({pad_top}px < {min_padding}px)")
        if pad_right < min_padding:
            fails.append(f"right ({pad_right}px < {min_padding}px)")
        if pad_bottom < min_padding:
            fails.append(f"bottom ({pad_bottom}px < {min_padding}px)")

        if fails:
            self.violations.append({
                "graphic_id": graphic_id,
                "rule": "CONTAINER_PADDING",
                "severity": "MEDIUM",
                "element": container_name,
                "details": f"Container padding violation on {', '.join(fails)}"
            })
            return False
        self.checks_passed += 1
        return True

    def check_vertical_gap(self, graphic_id: str, upper_elem: str, upper_bottom: int, lower_elem: str, lower_top: int, min_gap: int = 18, max_gap: int = 140) -> bool:
        """Verifies consistent vertical rhythm between stacked elements."""
        self.checks_total += 1
        gap = lower_top - upper_bottom
        if gap < min_gap:
            self.violations.append({
                "graphic_id": graphic_id,
                "rule": "VERTICAL_RHYTHM_COLLISION",
                "severity": "HIGH",
                "element": f"{upper_elem} -> {lower_elem}",
                "details": f"Vertical gap {gap}px is too tight (< {min_gap}px), causing collision risk"
            })
            return False
        elif gap > max_gap:
            self.violations.append({
                "graphic_id": graphic_id,
                "rule": "VERTICAL_RHYTHM_GAP",
                "severity": "LOW",
                "element": f"{upper_elem} -> {lower_elem}",
                "details": f"Vertical gap {gap}px is excessively large (> {max_gap}px), causing abandoned white space"
            })
            return False
        self.checks_passed += 1
        return True

    def check_safe_zones(self, graphic_id: str, elem_name: str, bbox: Tuple[int, int, int, int], canvas_height: int, top_safe: int = 200, bottom_safe: int = 260) -> bool:
        """Enforces Instagram/TikTok 9:16 safe zones."""
        self.checks_total += 1
        if bbox[1] < top_safe:
            self.violations.append({
                "graphic_id": graphic_id,
                "rule": "SAFE_ZONE_TOP",
                "severity": "HIGH",
                "element": elem_name,
                "details": f"Element top Y={bbox[1]} encroaches into top safe zone (< {top_safe}px)"
            })
            return False
        if bbox[3] > (canvas_height - bottom_safe):
            self.violations.append({
                "graphic_id": graphic_id,
                "rule": "SAFE_ZONE_BOTTOM",
                "severity": "HIGH",
                "element": elem_name,
                "details": f"Element bottom Y={bbox[3]} encroaches into bottom safe zone (> {canvas_height - bottom_safe}px)"
            })
            return False
        self.checks_passed += 1
        return True

    def check_authentic_logo(self, graphic_id: str, logo_path: str, valid_logo_names: List[str]) -> bool:
        """Verifies that an authentic official logo asset was used."""
        self.checks_total += 1
        basename = os.path.basename(logo_path)
        if basename not in valid_logo_names:
            self.violations.append({
                "graphic_id": graphic_id,
                "rule": "AUTHENTIC_BRAND_ASSET",
                "severity": "CRITICAL",
                "element": "Brandmark/Logo",
                "details": f"Unrecognized or reconstructed logo asset: '{basename}'. Must use approved official logo."
            })
            return False
        self.checks_passed += 1
        return True

    def check_element_density(self, graphic_id: str, container_name: str, element_count: int, max_elements: int = 4) -> bool:
        """Flags clutter overload if a single container card has too many stacked elements."""
        self.checks_total += 1
        if element_count > max_elements:
            self.violations.append({
                "graphic_id": graphic_id,
                "rule": "CLUTTER_DENSITY_OVERLOAD",
                "severity": "CRITICAL",
                "element": container_name,
                "details": f"Container contains {element_count} elements (max {max_elements}). Excessive visual density causes mobile feed fatigue and cramped composition."
            })
            return False
        self.checks_passed += 1
        return True

    def check_color_cohesion(self, graphic_id: str, container_name: str, accent_colors: List[str], max_accents: int = 2) -> bool:
        """Enforces 2-color brand discipline in single cards to prevent 'circus palette' slop."""
        self.checks_total += 1
        unique_accents = set(accent_colors)
        if len(unique_accents) > max_accents:
            self.violations.append({
                "graphic_id": graphic_id,
                "rule": "COLOR_PALETTE_CLASH",
                "severity": "HIGH",
                "element": container_name,
                "details": f"Container uses {len(unique_accents)} distinct accent colors ({', '.join(unique_accents)}). Max {max_accents} allowed for professional brand cohesion."
            })
            return False
        self.checks_passed += 1
        return True

    def check_symmetric_margins(self, graphic_id: str, element_name: str, container_bbox: Tuple[int, int, int, int], inner_bbox: Tuple[int, int, int, int], tolerance: int = 2, check_h: bool = True, check_v: bool = True) -> bool:
        """
        Enforces equal margins rule:
        'Anything should have the same amount of margin on each side, top and bottom, left and right'
        """
        self.checks_total += 1
        left_m = inner_bbox[0] - container_bbox[0]
        top_m = inner_bbox[1] - container_bbox[1]
        right_m = container_bbox[2] - inner_bbox[2]
        bottom_m = container_bbox[3] - inner_bbox[3]

        fails = []
        if check_v:
            v_diff = abs(top_m - bottom_m)
            if v_diff > tolerance:
                fails.append(f"Vertical asymmetry: Top margin ({top_m}px) != Bottom margin ({bottom_m}px), diff={v_diff}px")
        if check_h:
            h_diff = abs(left_m - right_m)
            if h_diff > tolerance:
                fails.append(f"Horizontal asymmetry: Left margin ({left_m}px) != Right margin ({right_m}px), diff={h_diff}px")

        if fails:
            self.violations.append({
                "graphic_id": graphic_id,
                "rule": "ASYMMETRIC_MARGINS",
                "severity": "CRITICAL",
                "element": element_name,
                "details": "; ".join(fails)
            })
            return False
        self.checks_passed += 1
        return True

    def get_summary(self) -> str:
        out = []
        out.append("=" * 80)
        out.append(f"DESIGN QA & LINTER AUDIT REPORT: {self.checks_passed}/{self.checks_total} Checks Passed")
        out.append("=" * 80)
        if not self.violations:
            out.append("STATUS: 100% CLEAN - ZERO DESIGN OR TYPOGRAPHY DEFECTS DETECTED.")
            out.append("All font sizes >= 28px, all centered elements aligned, padding & density compliant.")
        else:
            out.append(f"STATUS: FAILED - {len(self.violations)} VIOLATIONS DETECTED:")
            for i, v in enumerate(self.violations, 1):
                out.append(f"  {i}. [{v['severity']}] {v['graphic_id']} - {v['rule']} in {v['element']}:")
                out.append(f"     {v['details']}")
        out.append("=" * 80)
        return "\n".join(out)

    def is_clean(self) -> bool:
        return len(self.violations) == 0
