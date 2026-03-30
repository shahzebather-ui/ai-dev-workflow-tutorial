# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

This is an **educational tutorial repository** — it contains no application code. It teaches participants to build a Streamlit e-commerce sales dashboard using a spec-driven, AI-assisted development workflow. The repo provides the tutorial documentation, a sample CSV dataset, and a PRD; participants fork it and build the actual code themselves.

## Repository Structure

- `prd/ecommerce-analytics.md` — The Product Requirements Document for the dashboard to be built. This is the source-of-truth spec for what participants will build.
- `data/sales-data.csv` — 1,000 transaction records (2024) used as the dashboard's data source. Columns: date, order_id, product, category, region, quantity, unit_price, total_amount.
- `v2/` — Current tutorial version: `pre-work-setup.md` (async tool/account setup) + `workshop-build-deploy.md` (3-hour live workshop guide).
- `v1/` — Original two-session version with more detailed reference materials (terminal basics, git concepts, troubleshooting, FAQ, glossary).

## Workflow the Tutorial Teaches

```
PRD → spec-kit → Jira → Code (Claude Code + Cursor) → Commit → Push → Deploy → Live
```

Key tools taught: GitHub, Atlassian Jira, Cursor, Claude Code, spec-kit, Python + Streamlit.

## Content Editing Guidelines

The tutorial documents are the primary artifact. When editing them:

- **v2 is canonical** — this is what active workshops use. Changes to setup flows, tool versions, or UI steps should go here first.
- **Version consistency** — if updating tool setup steps (e.g., Claude Code install, Streamlit Cloud onboarding), check both `v2/pre-work-setup.md` and `v2/workshop-build-deploy.md` for duplicate instructions that may also need updating.
- **UI caveats** — both v2 documents note that evolving UIs may not match screenshots/steps exactly. When instructions describe specific UI flows (e.g., Jira MCP setup, Streamlit deploy), note that steps may vary.
- **Jira MCP** — the workshop uses Jira via Claude Code's MCP integration. The relevant setup is in `v2/workshop-build-deploy.md` under the Jira connection section.

## The Dashboard Being Built (PRD Summary)

Participants build a Streamlit app with:
- KPI cards: Total Sales (~$650K–$700K), Total Orders (~482), Average Order Value
- Sales trend line chart (monthly)
- Category breakdown bar chart (Electronics, Accessories, Audio, Wearables, Smart Home)
- Regional breakdown bar chart (North, South, East, West)

Tech stack: Python 3.11+, Streamlit, Pandas, Plotly. Package manager: `uv`.
