<!-- ┌─────────────────────────────────────────────────────────────────────┐ -->
<!-- │ THECC INSTITUTIONAL TRADER ACADEMY™ — STANDARD DOCUMENT FRONT-MATTER │ -->
<!-- └─────────────────────────────────────────────────────────────────────┘ -->

# THECC Fair Value Gaps PRO — Maintenance Checklist

### THECC Institutional Trader Academy™

#### 📘 Course Metadata

| Field | Value |
|---|---|
| **Academy** | THECC Institutional Trader Academy™ |
| **Course** | Fair Value Gaps PRO |
| **Module** | Operations |
| **Lesson** | Maintenance |
| **Difficulty** | Instructor / Engineering |
| **Estimated Time** | 45 minutes per release |
| **Prerequisites** | Developer Guide `THECC-DOC-FVGPRO-DG` |
| **Indicator Version** | v2.1 |
| **Document Version** | v2.1.0 |
| **Last Updated** | 2026-09-20 |
| **Instructor** | Dale Batise |
| **Status** | Content Complete — Certification Pending |

**Document control:**

| Field | Value |
|---|---|
| Document ID | THECC-DOC-FVGPRO-MC |
| Document type | Maintenance Checklist |
| Indicator | THECC Fair Value Gaps PRO · **Registry ID pending** |
| Version | v2.1.0 |
| Build | 2.1.0+2026-09-20 |
| Release date | 2026-09-20 |
| Compatible indicator versions | FVG PRO v2.1.x |
| Academy Doc Standard | v1.0 |
| Edition | Internal Master |
| Platform | TradingView · Pine Script v6 |
| Copyright | © THE CONSISTENCY COLLECTIVE |

**Consistency Creates Freedom.**

---

## A · Outstanding for this product — do these first

- [ ] **Assign the registry ID**, or rule the product an ancestor of THECC-0008. The registry raises the question under that entry and IDs are permanent, so this blocks everything else.
- [ ] Create `_SOURCE_OF_TRUTH.json` per Academy Documentation Standard §2.
- [ ] Replace **Registry ID pending** in all 16 documents and in the metadata JSON.
- [ ] Move the Drive folder out of `_unregistered` to `THECC-NNNN <CODE>`.
- [ ] Add the product to `_THECC_PRODUCT_CATALOG.md` with its doc-suite status.
- [ ] Run the TradingView compile green-check; record the date.
- [ ] Capture real screenshots for the 📸 placeholders and the 📊 diagram.
- [ ] Issue the portal URL and replace the QR placeholders.
- [ ] Render DOCX for every document (PDF is produced by `make_pdf.py`).
- [ ] Decide whether the untagged pre-2.0 baseline gets a retrospective version number.

---

## B · Every release

### Source

- [ ] Version bumped in the file header and the `indicator()` title if shown
- [ ] Change history comment updated at the top of the source
- [ ] Compile: 0 errors — record the date
- [ ] Third-party licence attribution still present in the `.pine` comments, and still absent from the UI and the docs
- [ ] No new third-party name introduced anywhere student-facing

### Behaviour

- [ ] Every new input defaults to existing behavior, or the change is declared breaking in the Release Notes
- [ ] Auto / Fix / Multi-Fix tested at 1, 3 and 5 active slots
- [ ] Drawing cost per zone re-counted if any drawing was added — the 125-zone capacity moves with it
- [ ] Both invalidation methods re-checked against a wick-pierced zone
- [ ] Sensitivity steps produce monotonically increasing zone counts
- [ ] Every alert fired once, both routes, gating on and off
- [ ] Bar Replay: zones still appear only on confirmed bars

### Documentation

- [ ] Knowledge Base `KB-03` defaults table updated first — it is the source every other document quotes
- [ ] Student Guide, Cheat Sheet, Quick Start regenerated against it
- [ ] Release Notes and Change Log written before publication, not after
- [ ] Exam and both answer keys re-checked if any documented number changed
- [ ] Documentation Index updated with delivered and outstanding documents
- [ ] `python3 make_pdf.py` run so every `.md` has a current `.html` and `.pdf` at the same version
- [ ] Consistency audit run; 0 fails

### Status

- [ ] Status line correct in every document: `Content Complete — Certification Pending` until green-checked **and** owner-signed
- [ ] No document, page or message describes the course as certified before that

---

## C · Quarterly

- [ ] Re-read the fault tables against real support questions from the quarter; add any new signature
- [ ] Confirm the drawing-budget guidance still matches TradingView's published limits
- [ ] Confirm Pine v6 behaviour has not changed for `request.security`, pivots or `alert()`
- [ ] Spot-check three student journals: are invalidations being written before entries?
- [ ] Review the roadmap; move or drop anything that has sat untouched for two quarters

---

## D · Sign-off record

| Release | Compile green-check | Owner sign-off | Docs regenerated | Audit clean | Notes |
|---|---|---|---|---|---|
| v2.1 | ☐ | ☐ | ☐ | ☐ | Registry ID outstanding |
| | | | | | |

---

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v2.1.0 | 2026-09-20 | Dale Batise | First Maintenance Checklist for Fair Value Gaps PRO v2.1: outstanding product actions, per-release source, behaviour, documentation and status checks, quarterly review and sign-off record. |

**Educational material only. Not financial advice, not a signal service, and not a claim about future results.**

---

*© THE CONSISTENCY COLLECTIVE — THECC Institutional Trader Academy™ · Consistency Creates Freedom. · Academy Documentation Standard v1.0.*
