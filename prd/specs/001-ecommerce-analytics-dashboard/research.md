# Research: ShopSmart Sales Dashboard

**Feature**: 001-ecommerce-analytics-dashboard
**Date**: 2026-03-30
**Status**: Complete — all NEEDS CLARIFICATION resolved

---

## Decision 1: Application Structure

**Decision**: Single `app.py` file; no package layout.

**Rationale**: The dashboard has one data source, three chart types, and no routing or
shared state between pages. Streamlit's own conventions favour a single entrypoint for
apps of this complexity. Splitting into modules prematurely adds indirection with no benefit.

**Alternatives considered**:
- `src/` package with `models.py`, `charts.py` helpers — rejected: over-engineered for
  a 150–200 line app; violates Principle II (Simplicity First).

---

## Decision 2: Dependency Management

**Decision**: `uv` with `pyproject.toml` (or `requirements.txt` as fallback for Streamlit Cloud).

**Rationale**: Constitution mandates `uv` as the package manager. Streamlit Community Cloud
reads `requirements.txt` from the repo root for its build environment. The recommended
approach is to maintain `requirements.txt` for Cloud compatibility, optionally alongside
`pyproject.toml` for local uv workflows.

**Alternatives considered**:
- `pyproject.toml` only — Streamlit Cloud may not read it; `requirements.txt` is the
  safe, documented path.
- `conda`/`pip` without lock — rejected: not reproducible.

**How to apply**: Include both `pyproject.toml` (for local `uv sync`) and `requirements.txt`
(for Streamlit Cloud deployment), with matching pinned versions.

---

## Decision 3: Plotly Chart Types

**Decision**:
- Monthly trend: `plotly.express.line` with `x=month_label`, `y=total_amount`
- Category breakdown: `plotly.express.bar` with `orientation='h'`, sorted descending
- Region breakdown: `plotly.express.bar` with `orientation='h'`, sorted descending

**Rationale**: Plotly Express is the simplest API surface for these chart types and is
already approved in the constitution stack. `st.plotly_chart(fig, use_container_width=True)`
renders full-width with interactive hover by default.

**Alternatives considered**:
- Streamlit native `st.line_chart` / `st.bar_chart` — rejected: no hover tooltips with
  custom labels; cannot control axis labels adequately.
- Matplotlib — rejected: static, no interactivity; heavier dependency.

---

## Decision 4: Pandas Aggregation Patterns

**Decision**:
- **Monthly**: `df['date'] = pd.to_datetime(df['date'])`, then
  `df.groupby(df['date'].dt.to_period('M'))['total_amount'].sum()`, converted to strings
  for x-axis labels (`'Jan 2024'` format).
- **Category**: `df.groupby('category')['total_amount'].sum().sort_values(ascending=False)`
- **Region**: `df.groupby('region')['total_amount'].sum().sort_values(ascending=False)`

**Rationale**: Standard Pandas patterns; no external libraries needed. `to_period('M')`
produces clean month grouping without day precision.

**Alternatives considered**:
- `resample('ME')` on a DatetimeIndex — equivalent but requires explicit index setting;
  `groupby` + `to_period` is more readable in a tutorial context.

---

## Decision 5: CSV Error Handling

**Decision**: Wrap `pd.read_csv()` in a `try/except` block; on failure call `st.error()`
and `st.stop()` to display a user-friendly message and halt rendering.

**Rationale**: FR-009 requires human-readable error over raw traceback. `st.stop()` prevents
further chart rendering attempts against a missing DataFrame.

**Alternatives considered**:
- `st.exception(e)` — exposes raw stack trace; violates FR-009.
- Returning `None` and checking downstream — more complex; `st.stop()` is cleaner.

---

## Decision 6: Layout for Breakdown Charts

**Decision**: Use `st.columns(2)` to place category and region charts side by side.

**Rationale**: Spec Assumption 5 explicitly calls for a two-column layout on desktop.
`st.columns(2)` is the canonical Streamlit approach; no CSS required.

**Alternatives considered**:
- Stacked vertically — rejected: contradicts explicit assumption in spec.
- CSS grid overrides — rejected: unnecessary complexity; Principle II violation.

---

## Resolution Summary

| Unknown | Resolution |
|---------|-----------|
| App structure | Single `app.py` |
| Dependency management | `requirements.txt` + optional `pyproject.toml` |
| Chart library API | Plotly Express (`px.line`, `px.bar`) |
| Monthly aggregation | `groupby(to_period('M'))` |
| Error handling | `try/except` → `st.error` + `st.stop` |
| Two-chart layout | `st.columns(2)` |
