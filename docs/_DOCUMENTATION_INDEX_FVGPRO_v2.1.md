# THECC Fair Value Gaps PRO — Documentation Index

### THECC Institutional Trader Academy™ · Document ID `THECC-DOC-FVGPRO-IX`

| Field | Value |
|---|---|
| Indicator | THECC Fair Value Gaps PRO v2.1 |
| Registry ID | **PENDING — owner decision required** |
| Academy Doc Standard | v1.0 |
| Documents delivered | 2 of 20 |
| Last updated | 2026-09-20 |
| Status | Content Complete — Certification Pending |
| Copyright | © THE CONSISTENCY COLLECTIVE |

---

## ⚠️ Why the Drive folder sits in `_unregistered`

`THECC_INDICATOR_REGISTRY.json` has no entry for this product. It carries an open question under **THECC-0008 (FVG Return Filter)**:

> *"FVGBPR_v1.7.pine sits in the same folder — unclear whether it is a separate product (FVG+BPR) or an ancestor. Resolve before retrofit; may warrant its own ID."*

The registry's ID policy is that `THECC-NNNN` is assigned once and never changes, so no ID was invented for these documents. Two related builds exist and the relationship between them needs an owner decision:

| Build | What it is |
|---|---|
| **FVG PRO v2.1** | Multi-timeframe FVG engine with volume profiling and Skull Mode, plus market structure, equal highs/lows and liquidity sweeps. The subject of these documents. |
| **SMC FVG/BPR v1.7** | Separate script: FVG, weak FVG, Balance Price Range, market structure, liquidity sweeps, equal highs/lows. |

They share concepts but are different products with different engines.

## Required sequence before publication

1. **Owner assigns the registry ID** (or rules the product an ancestor of THECC-0008).
2. Create `_SOURCE_OF_TRUTH.json` for the product, per Academy Documentation Standard §2.
3. Update the ID in every document: front matter, Document Control, and the metadata `.json`.
4. Move the Drive folder to `THECC-NNNN <CODE>` beside the other product folders.
5. Add the product to `_THECC_PRODUCT_CATALOG.md`.
6. Green-check the build on TradingView, then the owner may flip Status to `Production Certified` (§2a).

## Delivered documents

| Document | ID | Formats |
|---|---|---|
| Student Guide | `THECC-DOC-FVGPRO-SG` | `.md` (master) · `.html` · `.json` metadata · slide outline · video outline |
| Cheat Sheet | `THECC-DOC-FVGPRO-CS` | `.md` (master) · `.html` |

**DOCX and PDF are not present.** They were not rendered in the authoring session because the authoring container's LibreOffice could not load documents. Produce them by either route:

- Open the `.md` in Google Docs (right-click → Open with → Google Docs), then **File → Download → .docx / .pdf**; or
- Run the sanctioned `_render/` pipeline, which also runs `audit.py` for the 0-fail consistency gate.

`render.py` in this folder regenerates the `.html` from the `.md` using the Academy brand CSS.

## Outstanding documents (18 of the 20-document suite)

Instructor Guide (IG) · Developer Guide (DG) · Quick Start (QS) · FAQ Book (FAQ) · Troubleshooting Manual (TS) · Release Notes (RN) · Change Log (CL) · Knowledge Base (KB) · Video Scripts (VS, full scripts — only the outline exists) · PowerPoint (PPT, deck — only the outline exists) · Certification Exam (EX) · Instructor Answer Key (AK) · Student Workbook (WB) · Practical Exercises (PE) · Live Trading Lab Manual (LM) · Maintenance Checklist (MC) · Feature Roadmap (RM) · Documentation Index (IX — this file covers it for now)

## Standard compliance notes

| Requirement | Status |
|---|---|
| Course Metadata block | ✅ |
| Document Control front matter | ✅ (Indicator ID pending) |
| QR code placeholder | ✅ placeholder only — portal URL not yet issued |
| Table of Contents | ✅ |
| Callout legend | ✅ |
| Exercises + Review Questions per chapter | ✅ |
| Certification Quiz, 80% pass mark | ✅ (answers belong in the AK document) |
| Revision History · Compatibility · Copyright · footer convention | ✅ |
| Screenshots and diagrams | ⛔ placeholders — real captures required |
| No third-party names in student-facing docs (§7) | ✅ verified |
| Source-code attribution kept in `.pine` only (§6a) | ✅ |
| Reading level, Grade 11–12 (§6) | ✅ authored to target |
| Terminology lock (§8) | ✅ *confirmed* and *repaint* used per the standard |

## Source build

The documented build is `pine/thecc-fvg-pro-v2.pine` in this repository. Compile status: **not green-checked**. Keep the canonical `.pine` wherever the registry's `canonical_source` points once the ID is assigned.

---

*© THE CONSISTENCY COLLECTIVE — THECC Institutional Trader Academy™ · Consistency Creates Freedom. · Academy Documentation Standard v1.0.*
