<!--
SYNC IMPACT REPORT
==================
Version change: N/A → 1.0.0 (initial ratification — all sections new)

Modified principles: N/A (first version)

Added sections:
  - Core Principles (I–V)
  - Tech Stack Constraints
  - Development Workflow
  - Governance

Removed sections: N/A

Templates reviewed:
  ✅ .specify/templates/plan-template.md — Constitution Check gate references this document; no changes needed
  ✅ .specify/templates/spec-template.md — Scope/requirements sections align with Principle I (Spec-Driven) and Principle II (YAGNI/Phase 1 only)
  ✅ .specify/templates/tasks-template.md — Task phases and parallelism markers align with Principle V (Workflow Fidelity); no changes needed
  ✅ .specify/templates/constitution-template.md — Source template; no update needed

Follow-up TODOs: None — no placeholders intentionally deferred.
-->

# ShopSmart Analytics Dashboard Constitution

## Core Principles

### I. Spec-Driven Development

All implementation MUST originate from a written specification derived from the PRD.
No feature, chart, KPI, or data transformation may be built without a corresponding
requirement in `prd/ecommerce-analytics.md` or an approved spec artifact.

**Rationale**: The project teaches the PRD → spec → code workflow as a professional
discipline. Skipping or bypassing the spec step contradicts the core learning objective.

**Constitution Check (for plan.md gate)**:
- Does the feature/task map to a numbered requirement (FR-1 through FR-5, NFR-1 through NFR-5)?
- Is there a spec.md before implementation begins?

### II. Simplicity First (YAGNI)

Only Phase 1 scope from the PRD MUST be implemented. Phase 2 items (authentication,
database integration, export, alerts, filtering, drill-down, mobile-responsive design)
are explicitly out of scope and MUST NOT be added speculatively.

Complexity requires justification. Every abstraction, helper, or utility MUST serve
a current, demonstrable requirement — not a hypothetical future one.

**Rationale**: The tutorial's dashboard is intentionally simple so participants can
complete it in a 3-hour workshop. Scope creep is a listed risk in the PRD.

**Constitution Check**:
- Is this feature listed in Phase 1 of the PRD?
- Can this be implemented without introducing new dependencies beyond the approved stack?

### III. Data Accuracy (NON-NEGOTIABLE)

All computed metrics displayed in the dashboard MUST match the expected values derived
from `data/sales-data.csv`:
- Total Sales: ~$650,000–$700,000
- Total Orders: 482
- All 5 categories (Electronics, Accessories, Audio, Wearables, Smart Home) MUST appear
- All 4 regions (North, South, East, West) MUST appear

Charts MUST use correct aggregations (sum for sales, count for orders). No rounding,
truncation, or approximation that changes displayed values by more than $1 is acceptable.

**Rationale**: Stakeholders rely on dashboard accuracy for business decisions. Incorrect
data undermines trust in the entire analytics platform.

**Constitution Check**:
- Have computed values been cross-checked against the CSV source?
- Are aggregation methods (sum vs. count vs. average) explicitly correct per FR?

### IV. Deployability

The dashboard MUST be deployable to Streamlit Community Cloud and publicly accessible
via a shareable URL. All dependencies MUST be declared in a `requirements.txt` or
`pyproject.toml` managed by `uv`. No local-only paths, hard-coded credentials, or
environment-specific configurations may be committed.

**Rationale**: Public deployment is an explicit acceptance criterion in the PRD and
the final milestone of the workshop workflow.

**Constitution Check**:
- Do all file references use relative paths?
- Are all dependencies pinned and resolvable by Streamlit Cloud's build environment?
- Does `data/sales-data.csv` load correctly from a relative path?

### V. Workflow Fidelity

The prescribed end-to-end workflow MUST be followed in order:

```
PRD → spec-kit → Jira → Code (Claude Code / Cursor) → Commit → Push → Deploy → Live
```

Each step in the workflow is a teaching checkpoint. Work MUST be tracked in Jira.
Code MUST be committed to GitHub with meaningful commit messages. Deployment MUST
go through Streamlit Community Cloud — not local-only demos.

**Rationale**: The workflow itself is the primary learning artifact, not the dashboard.
Skipping steps removes the instructional value of the exercise.

**Constitution Check**:
- Is there a corresponding Jira ticket for this implementation task?
- Will this work result in a commit pushed to GitHub?

## Tech Stack Constraints

The following stack is approved for Phase 1. Deviations require explicit justification
against Principle II (Simplicity First) before introduction.

| Component       | Approved Technology  | Version Constraint |
|-----------------|----------------------|--------------------|
| Language        | Python               | 3.11+              |
| Web Framework   | Streamlit            | Latest stable      |
| Visualization   | Plotly               | Latest stable      |
| Data Processing | Pandas               | Latest stable      |
| Package Manager | uv                   | Latest stable      |
| Data Source     | CSV file             | `data/sales-data.csv` |

No database, authentication library, or server-side framework may be introduced in
Phase 1. Streamlit's built-in session state is the only permitted stateful mechanism.

## Development Workflow

All contributors MUST follow this sequence for every change:

1. **Spec first**: Verify or create a spec referencing the PRD requirement.
2. **Jira ticket**: Create or update the Jira issue before writing code.
3. **Implement**: Use Claude Code or Cursor; follow spec.md acceptance criteria.
4. **Validate locally**: Run `streamlit run app.py` and verify metrics match expected values.
5. **Commit**: Meaningful commit message referencing the Jira ticket ID.
6. **Push**: Push to GitHub; confirm CI/build checks pass if configured.
7. **Deploy**: Verify Streamlit Community Cloud deployment reflects the update.

Code review is encouraged but not required for solo workshop participants. For instructor
review submissions, all 7 steps MUST be demonstrable.

## Governance

This constitution supersedes all other development guidelines for this project.
Amendments require:

1. A written rationale explaining why the change is necessary.
2. A version increment following semantic versioning:
   - **MAJOR**: Principle removal, redefinition, or backward-incompatible scope change.
   - **MINOR**: New principle, new mandatory section, or material expansion of guidance.
   - **PATCH**: Clarifications, wording fixes, non-semantic refinements.
3. Updated `LAST_AMENDED_DATE` and `CONSTITUTION_VERSION` in this document.
4. Propagation check across all `.specify/templates/` files for consistency.

All implementation plans (plan.md) MUST include a Constitution Check section that
validates compliance before Phase 0 research begins and again after Phase 1 design.

Non-compliance discovered during implementation MUST be flagged before merging, not
worked around. Use the Complexity Tracking table in plan.md to document and justify
any necessary violations.

**Version**: 1.0.0 | **Ratified**: 2026-03-30 | **Last Amended**: 2026-03-30
