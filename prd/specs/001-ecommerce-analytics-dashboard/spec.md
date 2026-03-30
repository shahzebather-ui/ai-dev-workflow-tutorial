# Feature Specification: ShopSmart Sales Dashboard

**Feature Branch**: `001-ecommerce-analytics-dashboard`
**Created**: 2026-03-30
**Status**: Draft
**Input**: User description: "E-Commerce Analytics Dashboard from PRD"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Executive KPI Overview (Priority: P1)

As a finance manager or executive, I want to see three key performance indicators —
Total Sales, Total Orders, and Average Order Value — displayed prominently at the top
of the dashboard so that I can assess business performance at a glance without
scrolling or clicking.

**Why this priority**: KPI cards are the first thing stakeholders look at; they
establish trust in the data and enable immediate decision-making. All other charts
depend on the same underlying data load.

**Independent Test**: Load the dashboard with `data/sales-data.csv`. Verify three
KPI cards appear with values matching manual CSV calculations: Total Sales ~$650K–$700K,
Total Orders = 482, Average Order Value = Total Sales ÷ 482.

**Acceptance Scenarios**:

1. **Given** the dashboard is open, **When** the page loads, **Then** three KPI cards
   are visible showing Total Sales (currency-formatted), Total Orders (integer), and
   Average Order Value (currency-formatted).
2. **Given** the CSV contains 1,000 rows, **When** totals are computed, **Then** Total
   Orders equals the count of transactions (482) and Total Sales equals the sum of
   `total_amount` across all rows.
3. **Given** a stakeholder views the dashboard, **When** they read the KPI cards,
   **Then** no calculation or navigation is required to find these three metrics.

---

### User Story 2 - Sales Trend Over Time (Priority: P2)

As the CEO, I want to see a line chart showing monthly sales totals across the full
year so that I can identify growth patterns, seasonal peaks, and business trajectory.

**Why this priority**: Trend visibility contextualises the KPI totals and answers
"are we improving?" It requires the same data load as Story 1 but adds aggregation.

**Independent Test**: Verify the line chart displays 12 monthly data points, x-axis
shows month labels (Jan–Dec 2024), and the sum of all monthly values equals the
Total Sales KPI.

**Acceptance Scenarios**:

1. **Given** the data spans 12 months of 2024, **When** the trend chart renders,
   **Then** exactly 12 data points appear on the x-axis, one per month.
2. **Given** a user hovers over a data point, **When** the tooltip appears, **Then**
   it shows the month name and exact sales amount for that month.
3. **Given** the chart is visible, **When** a stakeholder interprets the line,
   **Then** the y-axis scale makes trend changes visually apparent.

---

### User Story 3 - Category & Regional Breakdowns (Priority: P3)

As a marketing director or regional manager, I want to see horizontal bar charts
showing sales ranked by product category and by geographic region so that I can
identify top performers and underperforming segments.

**Why this priority**: Breakdowns answer "where is revenue coming from?" and enable
targeted decisions. They depend on the same data load as Stories 1 and 2.

**Independent Test**: Verify two horizontal bar charts appear, each sorted
highest-to-lowest. Confirm all 5 categories and all 4 regions appear. Confirm bar
lengths are proportional to sales values.

**Acceptance Scenarios**:

1. **Given** the dashboard loads, **When** the category chart renders, **Then** all
   5 categories (Electronics, Accessories, Audio, Wearables, Smart Home) appear as
   horizontal bars sorted from highest to lowest sales value.
2. **Given** the dashboard loads, **When** the regional chart renders, **Then** all
   4 regions (North, South, East, West) appear as horizontal bars sorted from highest
   to lowest sales value.
3. **Given** a user hovers over a bar, **When** the tooltip appears, **Then** it
   shows the category/region name and exact sales total.
4. **Given** the two charts are displayed, **When** a stakeholder views the page,
   **Then** both charts are visible without horizontal scrolling on a standard
   desktop browser viewport.

---

### Edge Cases

- What happens if a row in the CSV has a missing or null `total_amount`? The system
  must skip or exclude that row rather than crash or display NaN.
- What if the CSV file is not found at the expected path? The dashboard must display
  a clear, user-friendly error message rather than a raw Python traceback.
- What if a category or region appears in the data that is not in the expected lists?
  It must still be displayed — no hardcoded category or region filtering.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The dashboard MUST display the page title "ShopSmart Sales Dashboard".
- **FR-002**: The dashboard MUST show a "Total Sales" KPI card containing the sum of
  all `total_amount` values, formatted as currency (e.g., $672,345).
- **FR-003**: The dashboard MUST show a "Total Orders" KPI card containing the count
  of transaction rows, formatted as an integer with comma separator.
- **FR-004**: The dashboard MUST show an "Average Order Value" KPI card containing
  Total Sales ÷ Total Orders, formatted as currency.
- **FR-005**: The dashboard MUST display a line chart of monthly sales totals for the
  full date range in the CSV, with month on the x-axis and sales amount on the y-axis,
  with interactive hover tooltips showing month and exact value.
- **FR-006**: The dashboard MUST display a horizontal bar chart of total sales by
  product category, sorted highest-to-lowest, showing all categories present in the
  data, with interactive hover tooltips.
- **FR-007**: The dashboard MUST display a horizontal bar chart of total sales by
  geographic region, sorted highest-to-lowest, showing all regions present in the
  data, with interactive hover tooltips.
- **FR-008**: The dashboard MUST load its data from `data/sales-data.csv` using a
  relative file path so that it works both locally and on Streamlit Community Cloud.
- **FR-009**: If the CSV file cannot be loaded, the dashboard MUST display a
  human-readable error message rather than a raw exception traceback.

### Key Entities

- **Transaction**: A single sales record. Key attributes: date, order_id, product,
  category, region, quantity, unit_price, total_amount.
- **Monthly Aggregate**: Derived grouping — month label + sum of total_amount for
  that month. Used for the trend chart.
- **Category Aggregate**: Derived grouping — category name + sum of total_amount
  for that category. Used for the category bar chart.
- **Region Aggregate**: Derived grouping — region name + sum of total_amount for
  that region. Used for the region bar chart.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: All three KPI values load and display within 5 seconds of the page
  opening on a standard broadband connection.
- **SC-002**: The sales trend chart shows exactly one data point per calendar month
  present in the dataset (12 for a full-year dataset).
- **SC-003**: Every category and region present in the CSV appears in its respective
  chart — zero categories or regions are omitted.
- **SC-004**: Hovering over any chart element reveals a tooltip with the exact label
  and numeric value within 1 second of hover.
- **SC-005**: A non-technical stakeholder can read and interpret all KPIs and charts
  without any instructions or training.
- **SC-006**: The deployed dashboard is publicly accessible via a shareable
  Streamlit Community Cloud URL.
- **SC-007**: All KPI values match manual calculations from the CSV to within $1
  rounding tolerance.

## Assumptions

- The CSV file at `data/sales-data.csv` contains approximately 1,000 rows spanning
  12 months of 2024 with columns: date, order_id, product, category, region,
  quantity, unit_price, total_amount.
- The date column is parseable as a standard date format (YYYY-MM-DD or similar).
- Mobile-responsive design is out of scope (Phase 2 per PRD); the dashboard targets
  desktop browsers only.
- User authentication, filtering controls, and export functionality are out of scope
  (Phase 2 per PRD).
- The two breakdown charts (category and region) will be displayed side by side in
  a two-column layout on desktop viewports.
- Average Order Value is calculated as Total Sales ÷ Total Orders (not as a median
  or weighted average).
- The dashboard will be deployed to Streamlit Community Cloud as a public app with
  no access restrictions.
