# Integration Fixture Validation Report

This document records the validation audit, script execution commands, and file hashes for the `project-status-update` Golden Path integration fixture.

---

## Data Pipeline Traceability Audit

| Step File | Skill Source | Input Provenance & ID Linkage | Output Integrity |
| :--- | :--- | :--- | :--- |
| **`00-research-input.md`** | Synthetic Input | Direct quotes labeled `research-01`, `research-02`, `research-03` | Base synthetic research |
| **`01-job-definition.yaml`** | `jtbd-job-definer` | Links direct evidence to `research-01` to `03` | Core Job: `candidate` |
| **`02-job-map.yaml`** | `jtbd-job-mapper` | Maps `locate`, `confirm`, `execute`, `monitor`, `modify` stages | Map: `provisional` |
| **`03-desired-outcomes.yaml`** | `jtbd-outcome-engineer` | Formulates `O-001` (linked to `locate`) & `O-002` (linked to `confirm`) | Outcomes: `provisional` |
| **`04-survey-input.json`** | Synthetic Input | Ratings for `O-001` ($I=9, S=4$) & `O-002` ($I=8, S=6$) | Quantitative input |
| **`05-opportunity-results.json`** | `jtbd-opportunity-calculator` | Deterministically calculated via `calculate_opportunity.py` | `O-001` Opp: 14.0, `O-002` Opp: 10.0 |
| **`06-strategy-assessment.yaml`** | `jtbd-growth-strategist` | Evaluates $Opp=14.0$; stops at `insufficient_evidence` due to missing price/performance/cost evidence | Assessment: `insufficient_evidence` |

---

## Deterministic Script Execution

The opportunity calculation results file `05-opportunity-results.json` was generated directly by running:

```bash
python3 skills/jtbd-opportunity-calculator/scripts/calculate_opportunity.py \
  integration/project-status-update/04-survey-input.json \
  > integration/project-status-update/05-opportunity-results.json
```

---

## Validation Assertions Verified

1. **Schema Parsing**: All YAML and JSON files conform to their respective skill Output schemas.
2. **Upstream Traceability**: Every outcome ID (`O-001`, `O-002`) and statement traces directly back to a job map step and synthetic research excerpt.
3. **Evidence Discipline**: All non-direct inferences are explicitly marked as `hypothesis` or `domain_rationale`.
4. **Calculated Determinism**: Opportunity scores match formula ($I + \max(I-S, 0)$).
5. **Stopping Discipline**: `jtbd-growth-strategist` correctly returns `insufficient_evidence` when price/cost/performance evidence is absent.
