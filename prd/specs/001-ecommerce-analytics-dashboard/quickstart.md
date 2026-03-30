# Quickstart: ShopSmart Sales Dashboard

**Feature**: 001-ecommerce-analytics-dashboard
**Date**: 2026-03-30

---

## Prerequisites

- Python 3.11+
- [`uv`](https://docs.astral.sh/uv/) installed (`pip install uv` or `brew install uv`)
- Repository cloned locally

---

## Local Development

### 1. Install dependencies

```bash
uv sync
```

Or if using `requirements.txt` only:

```bash
pip install -r requirements.txt
```

### 2. Run the dashboard

From the **repository root** (so that the relative path `data/sales-data.csv` resolves correctly):

```bash
streamlit run app.py
```

The app opens at `http://localhost:8501`.

### 3. Verify expected values

Once loaded, confirm:

| KPI | Expected |
|-----|----------|
| Total Sales | $650,000–$700,000 |
| Total Orders | 482 |
| Average Order Value | Total Sales ÷ 482 |
| Trend chart data points | 12 (one per month, Jan–Dec 2024) |
| Category bars | 5 (Electronics, Accessories, Audio, Wearables, Smart Home) |
| Region bars | 4 (North, South, East, West) |

---

## Deployment to Streamlit Community Cloud

1. Push `app.py` and `requirements.txt` to GitHub (`main` branch).
2. Go to [share.streamlit.io](https://share.streamlit.io) → **New app**.
3. Select your repo, branch (`main`), and main file (`app.py`).
4. Click **Deploy** — Streamlit Cloud installs deps from `requirements.txt` and runs the app.
5. Copy the public URL and verify all KPIs and charts load correctly.

**Important**: The `data/` folder must be committed to the repo. Streamlit Cloud reads it
from the repo root, matching the relative path `data/sales-data.csv` used in `app.py`.

---

## Dependency File Reference

### `requirements.txt` (Streamlit Cloud)

```
streamlit
pandas
plotly
```

### `pyproject.toml` (local uv workflow)

```toml
[project]
name = "shopsmart-dashboard"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "streamlit",
    "pandas",
    "plotly",
]
```

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `FileNotFoundError: data/sales-data.csv` | Run `streamlit run app.py` from the repo root, not from a subdirectory |
| Charts not rendering | Ensure `plotly` is installed (`pip show plotly`) |
| Blank page / spinner stuck | Check the terminal for Python errors |
| Values don't match expected | Verify no rows are being unintentionally filtered before aggregation |
