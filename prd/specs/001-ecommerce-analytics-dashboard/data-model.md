# Data Model: ShopSmart Sales Dashboard

**Feature**: 001-ecommerce-analytics-dashboard
**Date**: 2026-03-30

---

## Source: Transaction

The raw unit of data. Each row in `data/sales-data.csv` is one Transaction.

| Field | Type | Constraints |
|-------|------|-------------|
| `date` | string → `datetime64` | Required; parseable as YYYY-MM-DD; used for monthly grouping |
| `order_id` | string | Required; unique per transaction; used for count |
| `product` | string | Informational; not aggregated in Phase 1 |
| `category` | string | Required; one of: Electronics, Accessories, Audio, Wearables, Smart Home (or any future value) |
| `region` | string | Required; one of: North, South, East, West (or any future value) |
| `quantity` | integer | Informational; not aggregated in Phase 1 |
| `unit_price` | float | Informational; not aggregated in Phase 1 |
| `total_amount` | float | Required; primary metric; rows with null/NaN excluded via `dropna()` before aggregation |

**Validation rules**:
- Rows where `total_amount` is null or NaN are dropped before any computation (edge case from spec).
- Date column is coerced with `pd.to_datetime(..., errors='coerce')` — unparseable dates become NaT and are excluded.
- No hardcoded category or region filtering — all values present in CSV appear in charts (spec edge case).

---

## Derived: Monthly Aggregate

Computed from Transaction via `groupby(date.dt.to_period('M'))`.

| Field | Type | Description |
|-------|------|-------------|
| `month_label` | string | `'Jan 2024'` format — x-axis label for trend chart |
| `total_sales` | float | Sum of `total_amount` for that month |

**Invariant**: Sum of all `total_sales` across months equals the Total Sales KPI.

---

## Derived: Category Aggregate

Computed from Transaction via `groupby('category')`.

| Field | Type | Description |
|-------|------|-------------|
| `category` | string | Category name as present in CSV |
| `total_sales` | float | Sum of `total_amount` for that category |

**Invariant**: All categories present in CSV appear. Sorted descending by `total_sales`.
Sum equals Total Sales KPI.

---

## Derived: Region Aggregate

Computed from Transaction via `groupby('region')`.

| Field | Type | Description |
|-------|------|-------------|
| `region` | string | Region name as present in CSV |
| `total_sales` | float | Sum of `total_amount` for that region |

**Invariant**: All regions present in CSV appear. Sorted descending by `total_sales`.
Sum equals Total Sales KPI.

---

## KPI Scalars

Computed once from the full Transaction DataFrame.

| KPI | Computation | Expected Value |
|-----|-------------|----------------|
| Total Sales | `df['total_amount'].sum()` | ~$650,000–$700,000 |
| Total Orders | `len(df)` | 482 |
| Average Order Value | Total Sales ÷ Total Orders | Total Sales / 482 |

**Tolerance**: All displayed values must match manual CSV calculation to within $1 (SC-007).

---

## State Transitions

Not applicable — the dashboard is stateless and read-only. Data loads once at page render
(or from Streamlit's cache if `@st.cache_data` is applied). No mutations occur.
