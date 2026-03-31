---
description: "Task list for ShopSmart Sales Dashboard implementation"
---

# Tasks: ShopSmart Sales Dashboard

**Input**: Design documents from `prd/specs/001-ecommerce-analytics-dashboard/`
**Prerequisites**: plan.md ✅, spec.md ✅, data-model.md ✅, contracts/ui-contract.md ✅, quickstart.md ✅

## Format: `[ID] [P?] [Story?] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2, US3)

---

## Phase 1: Setup

**Purpose**: Project initialization — creates the two files everything else depends on.

- [x] T001 Create `requirements.txt` at repo root with dependencies: `streamlit`, `pandas`, `plotly`
- [x] T002 Create `app.py` at repo root with page config and title: `st.set_page_config(page_title="ShopSmart Sales Dashboard")` and `st.title("ShopSmart Sales Dashboard")` (FR-001)

---

## Phase 2: Foundational (Blocking Prerequisite)

**Purpose**: Data loading infrastructure that every user story depends on.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

- [x] T003 Implement `load_data()` in `app.py`: reads `data/sales-data.csv` with `pd.read_csv()`, parses `date` column via `pd.to_datetime(errors='coerce')`, drops rows where `total_amount` is null/NaN via `dropna()`, decorates with `@st.cache_data`, and wraps file read in try/except that calls `st.error("Unable to load data file. Please ensure 'data/sales-data.csv' exists in the repository root.")` then `st.stop()` on failure (FR-008, FR-009)

**Checkpoint**: Run `streamlit run app.py` from repo root — page title renders, no errors in terminal.

---

## Phase 3: User Story 1 — Executive KPI Overview (Priority: P1) 🎯 MVP

**Goal**: Display Total Sales, Total Orders, and Average Order Value as metric cards.

**Independent Test**: Load dashboard — three KPI cards appear with values: Total Sales ~$650K–$700K,
Total Orders = 482, Average Order Value = Total Sales ÷ 482. Values match manual CSV calculation
to within $1 (SC-007).

- [x] T004 [P] [US1] Compute KPI scalars in `app.py` after `load_data()` call: `total_sales = df['total_amount'].sum()`, `total_orders = len(df)`, `avg_order_value = total_sales / total_orders` (FR-002, FR-003, FR-004; data-model.md KPI Scalars)
- [x] T005 [US1] Render KPI row in `app.py` using `st.columns(3)` with `st.metric()` for each card: col[0] label `"Total Sales"` value formatted as `f"${total_sales:,.0f}"`, col[1] label `"Total Orders"` value formatted as `f"{total_orders:,}"`, col[2] label `"Average Order Value"` value formatted as `f"${avg_order_value:,.2f}"` (ui-contract.md KPI Row Contract)

**Checkpoint**: At this point, User Story 1 is fully functional and independently demonstrable.

---

## Phase 4: User Story 2 — Sales Trend Over Time (Priority: P2)

**Goal**: Display a monthly sales trend line chart with hover tooltips.

**Independent Test**: Trend chart shows exactly 12 data points labeled Jan 2024–Dec 2024.
Hovering each point reveals month name and exact sales value. Sum of all monthly values
equals the Total Sales KPI (SC-002, SC-004).

- [x] T006 [P] [US2] Compute `monthly_sales` DataFrame in `app.py`: `df.groupby(df['date'].dt.to_period('M'))['total_amount'].sum().reset_index()`, rename columns to `month` and `total_sales`, format `month` as string label `'Jan 2024'` via `month.dt.strftime('%b %Y')`, sort ascending by month (data-model.md Monthly Aggregate)
- [x] T007 [US2] Build Plotly Express line chart from `monthly_sales` in `app.py`: `px.line(monthly_sales, x='month', y='total_sales', title='Monthly Sales Trend', labels={'month': 'Month', 'total_sales': 'Sales ($)'})`, add `st.subheader("Monthly Sales Trend")` and render with `st.plotly_chart(fig_trend, use_container_width=True)` (ui-contract.md Sales Trend Chart Contract; FR-005)

**Checkpoint**: At this point, User Stories 1 and 2 both work independently.

---

## Phase 5: User Story 3 — Category & Regional Breakdowns (Priority: P3)

**Goal**: Display two horizontal bar charts (by category, by region) side by side.

**Independent Test**: Two horizontal bar charts appear side by side. Category chart shows all 5
categories sorted highest-to-lowest. Region chart shows all 4 regions sorted highest-to-lowest.
Hovering any bar shows exact name and sales value. Both charts visible without horizontal scroll
on desktop viewport (SC-003, SC-004).

- [ ] T008 [P] [US3] Compute `category_sales` DataFrame in `app.py`: `df.groupby('category')['total_amount'].sum().reset_index()`, rename to `category` and `total_sales`, sort descending by `total_sales` (data-model.md Category Aggregate; FR-006)
- [ ] T009 [P] [US3] Compute `region_sales` DataFrame in `app.py`: `df.groupby('region')['total_amount'].sum().reset_index()`, rename to `region` and `total_sales`, sort descending by `total_sales` (data-model.md Region Aggregate; FR-007)
- [ ] T010 [US3] Build Plotly Express horizontal bar chart for `category_sales` in `app.py`: `px.bar(category_sales, x='total_sales', y='category', orientation='h', title='Sales by Category', labels={'total_sales': 'Sales ($)', 'category': 'Category'})` — y-axis already sorted descending from T008 (ui-contract.md Category Chart Contract; FR-006)
- [ ] T011 [US3] Build Plotly Express horizontal bar chart for `region_sales` in `app.py`: `px.bar(region_sales, x='total_sales', y='region', orientation='h', title='Sales by Region', labels={'total_sales': 'Sales ($)', 'region': 'Region'})` — y-axis already sorted descending from T009 (ui-contract.md Region Chart Contract; FR-007)
- [ ] T012 [US3] Render both breakdown charts side by side in `app.py` using `st.columns(2)`: col[0] renders `st.subheader("Sales by Category")` + `st.plotly_chart(fig_category, use_container_width=True)`, col[1] renders `st.subheader("Sales by Region")` + `st.plotly_chart(fig_region, use_container_width=True)` (ui-contract.md Breakdown Charts Contract)

**Checkpoint**: All three user stories are independently functional.

---

## Phase 6: Polish & Validation

**Purpose**: End-to-end validation and deployment.

- [ ] T013 [P] Validate all dashboard values against `quickstart.md` expected values: confirm Total Sales $650K–$700K, Total Orders = 482, trend chart has 12 data points, category chart has 5 bars, region chart has 4 bars; all within $1 tolerance (SC-007; quickstart.md Verify Expected Values)
- [ ] T014 Deploy to Streamlit Community Cloud: commit `app.py`, `requirements.txt`, and `data/sales-data.csv` to `main` branch on GitHub; create new app at share.streamlit.io pointing to `main`/`app.py`; verify public URL loads correctly with all KPIs and charts (SC-006; quickstart.md Deployment section)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately
- **Foundational (Phase 2)**: Depends on Phase 1 — BLOCKS all user stories
- **US1 (Phase 3)**: Depends on Phase 2 completion — no other story dependencies
- **US2 (Phase 4)**: Depends on Phase 2 completion — no dependency on US1
- **US3 (Phase 5)**: Depends on Phase 2 completion — no dependency on US1 or US2
- **Polish (Phase 6)**: Depends on all desired user stories being complete

### User Story Dependencies

- **US1 (P1)**: T003 → T004 → T005
- **US2 (P2)**: T003 → T006 → T007
- **US3 (P3)**: T003 → T008+T009 → T010+T011 → T012

### Within Each Phase

- T004 and T005 are sequential (scalars must exist before rendering)
- T006 and T007 are sequential (aggregate must exist before chart)
- T008 and T009 are parallel (independent DataFrames)
- T010 and T011 are parallel after T008/T009 (independent charts)
- T012 depends on T010 and T011 (renders both charts)

### Parallel Opportunities

```bash
# Phase 5 parallel launch — after T003 is done:
Task: "T008 — Compute category_sales aggregate"
Task: "T009 — Compute region_sales aggregate"

# Then parallel:
Task: "T010 — Build category horizontal bar chart"
Task: "T011 — Build region horizontal bar chart"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001–T002)
2. Complete Phase 2: Foundational (T003) — CRITICAL
3. Complete Phase 3: User Story 1 (T004–T005)
4. **STOP and VALIDATE**: Confirm three KPI cards show correct values
5. Demo to stakeholders if ready

### Incremental Delivery

1. Setup + Foundational → data loads cleanly
2. Add US1 (T004–T005) → KPI cards visible → MVP demo ready
3. Add US2 (T006–T007) → trend chart visible → second demo
4. Add US3 (T008–T012) → breakdown charts visible → full dashboard
5. Polish + Deploy (T013–T014) → public URL → stakeholder sign-off

---

## Notes

- All tasks write to `app.py` — execute sequentially unless marked [P] within the same phase
- Run `streamlit run app.py` from repo root after each checkpoint (not from a subdirectory)
- T008 and T009 are parallel because they compute independent DataFrames with no shared writes
- T010 and T011 are parallel because they build independent Plotly figures
- Commit after each phase checkpoint to preserve progress
