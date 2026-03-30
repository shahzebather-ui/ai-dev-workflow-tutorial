# Implementation Plan: ShopSmart Sales Dashboard

**Branch**: `001-ecommerce-analytics-dashboard` | **Date**: 2026-03-30 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-ecommerce-analytics-dashboard/spec.md`

## Summary

Build a single-page Streamlit dashboard that reads `data/sales-data.csv` and displays three
KPI cards (Total Sales, Total Orders, Average Order Value), a monthly sales trend line chart,
and two horizontal bar charts (by category and by region). No authentication, filtering, or
database — pure CSV-driven read-only analytics deployable to Streamlit Community Cloud.

## Technical Context

**Language/Version**: Python 3.11+
**Primary Dependencies**: Streamlit (latest stable), Plotly (latest stable), Pandas (latest stable)
**Storage**: CSV file — `data/sales-data.csv` (relative path, ~1,000 rows)
**Testing**: Manual validation against expected CSV values (Total Sales ~$650K–$700K, Total Orders = 482)
**Target Platform**: Streamlit Community Cloud (public URL); local development via `streamlit run`
**Project Type**: Single-file web dashboard (data app)
**Performance Goals**: All KPIs and charts render within 5 seconds on standard broadband (SC-001)
**Constraints**: Relative file paths only; no hard-coded credentials; no Phase 2 features
**Scale/Scope**: ~1,000 CSV rows; single-user read-only; desktop viewport only

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Pre-Phase 0 Gate

| Principle | Check | Status |
|-----------|-------|--------|
| I. Spec-Driven | spec.md exists; all FRs (FR-001–FR-009) map to PRD Phase 1 requirements | ✅ PASS |
| II. Simplicity First | Phase 2 items (auth, filtering, export, drill-down) are explicitly excluded in spec Assumptions | ✅ PASS |
| III. Data Accuracy | FR-002, FR-003, FR-004 specify exact aggregation methods; SC-007 requires <$1 tolerance | ✅ PASS |
| IV. Deployability | FR-008 mandates relative path for CSV; approved stack fully declared in constitution | ✅ PASS |
| V. Workflow Fidelity | Jira ticket creation is a pre-implementation step (workshop workflow); spec and plan exist | ✅ PASS |

No violations. No Complexity Tracking entries required.

## Project Structure

### Documentation (this feature)

```text
prd/specs/001-ecommerce-analytics-dashboard/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output
│   └── ui-contract.md
└── tasks.md             # Phase 2 output (/speckit.tasks — NOT created by /speckit.plan)
```

### Source Code (repository root)

```text
app.py                   # Single Streamlit application entrypoint
data/
└── sales-data.csv       # Source data (already present)
pyproject.toml           # uv-managed dependencies (or requirements.txt)
```

**Structure Decision**: Single-file layout. A Streamlit dashboard of this scope (one data
source, three chart types, no routing) does not warrant a `src/` package layout. All logic
lives in `app.py`. If aggregation helpers grow complex they may be extracted to a single
`utils.py`, but that is deferred until needed.

## Complexity Tracking

> No violations to justify — all constitution gates pass.
