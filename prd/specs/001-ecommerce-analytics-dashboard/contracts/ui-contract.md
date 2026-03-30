# UI Contract: ShopSmart Sales Dashboard

**Feature**: 001-ecommerce-analytics-dashboard
**Date**: 2026-03-30
**Type**: Streamlit application — user-facing interface contract

---

## Page Contract

### Page Title

```
st.title("ShopSmart Sales Dashboard")
```

- Requirement: FR-001
- Must appear at the top of the page, before any KPI or chart.

---

## KPI Row Contract

Three metric cards displayed horizontally via `st.columns(3)`.

| Column | Label | Value Format | Source |
|--------|-------|--------------|--------|
| col[0] | `"Total Sales"` | `"$672,345"` (currency, commas, no decimals or 2dp) | `df['total_amount'].sum()` |
| col[1] | `"Total Orders"` | `"482"` (integer, comma separator if ≥1000) | `len(df)` |
| col[2] | `"Average Order Value"` | `"$1,394.90"` (currency, 2dp) | Total Sales ÷ Total Orders |

- Requirement: FR-002, FR-003, FR-004
- Rendered via `st.metric(label=..., value=...)`.
- No delta values or arrows — Phase 1 only.

---

## Sales Trend Chart Contract

```
st.subheader("Monthly Sales Trend")
st.plotly_chart(fig_trend, use_container_width=True)
```

| Property | Value |
|----------|-------|
| Chart type | Plotly Express line chart |
| X-axis | Month label (`'Jan 2024'` … `'Dec 2024'`) |
| Y-axis | Sales amount (float, Plotly auto-formats) |
| Data points | One per calendar month present in CSV (12 for full-year data) |
| Hover tooltip | Month label + exact sales value |
| Interactivity | Zoom, pan, hover (Plotly default) |

- Requirement: FR-005, SC-002, SC-004

---

## Breakdown Charts Contract

Two charts displayed side by side via `st.columns(2)`.

### Category Chart (col[0])

```
st.subheader("Sales by Category")
st.plotly_chart(fig_category, use_container_width=True)
```

| Property | Value |
|----------|-------|
| Chart type | Plotly Express horizontal bar chart |
| Y-axis | Category name |
| X-axis | Total sales (float) |
| Sort order | Descending by total sales (highest at top) |
| Categories shown | All categories present in CSV — no hardcoded filter |
| Hover tooltip | Category name + exact sales total |

- Requirement: FR-006, SC-003, SC-004

### Region Chart (col[1])

```
st.subheader("Sales by Region")
st.plotly_chart(fig_region, use_container_width=True)
```

| Property | Value |
|----------|-------|
| Chart type | Plotly Express horizontal bar chart |
| Y-axis | Region name |
| X-axis | Total sales (float) |
| Sort order | Descending by total sales (highest at top) |
| Regions shown | All regions present in CSV — no hardcoded filter |
| Hover tooltip | Region name + exact sales total |

- Requirement: FR-007, SC-003, SC-004

---

## Error State Contract

If `data/sales-data.csv` cannot be loaded:

```python
st.error("Unable to load data file. Please ensure 'data/sales-data.csv' exists in the repository root.")
st.stop()
```

- Requirement: FR-009
- No Python traceback visible to the user.
- Page rendering halts — no blank/broken charts below the error.

---

## Out of Scope (Phase 2)

The following UI elements MUST NOT appear in Phase 1:
- Date range filters or dropdowns
- Category/region filter widgets
- Export buttons (CSV download, PDF)
- Authentication prompts or login screens
- Mobile-specific layout adjustments
- Drill-down views or detail pages
