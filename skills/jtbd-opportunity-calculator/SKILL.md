---
name: jtbd-opportunity-calculator
description: Compute quantitative Outcome-Driven Innovation (ODI) Opportunity Scores from customer importance and satisfaction survey ratings. Use when given numerical survey data (1-10 scale), mean importance and satisfaction scores, or survey JSON/CSV files, and asked to compute opportunity scores, classify outcomes into opportunity tiers, or run the deterministic calculation script. Do not use to invent survey scores from qualitative text or recommend product strategy.
---

# JTBD Opportunity Calculator

**Use customer importance and satisfaction ratings to pinpoint the most valuable unaddressed needs.**

---

## Use this when
- You have quantitative survey rating data ($1\text{--}10$ scale) for customer desired outcomes.
- You need to compute mathematical ODI Opportunity Scores ($Opp = Importance + \max(Importance - Satisfaction, 0)$).
- You want to classify outcome metrics into `extreme_underserved`, `high_underserved`, `moderate_underserved`, `appropriately_served`, or `overserved_candidate`.

## Don't use this when
- You do not have numerical survey data (never convert qualitative interview text into fake numbers!).
- You need to formulate outcome metric statements from scratch (use `jtbd-outcome-engineer`).
- You need to evaluate market growth strategies (use `jtbd-growth-strategist`).

## Minimum input
- **Minimum Input**: Numerical importance and satisfaction mean ratings on a matching $1\text{--}10$ scale, sample size $N$, and outcome statements.
- **Templates Available**: Use templates under `skills/jtbd-opportunity-calculator/templates/`:
  - `survey-input-template.json`
  - `survey-input-template.csv`
  - `survey-question-template.md`

If ratings are missing or scales are non-10-point, returns `calculation_status: blocked`.

## What you get
1. **Executive Summary**: Top underserved outcomes, outcomes not to prioritize, data strength rating, and recommended next steps.
2. **Mathematical Opportunity Scores**: Exact deterministic score calculations ($Opp$ range $1.0\text{--}20.0$).
3. **Outcome Classifications**: Objective categorization based on mathematical thresholds.

## Quick prompt
> *"Compute Opportunity Scores for this survey data: '[Paste JSON/CSV ratings or run calculate_opportunity.py]'."*

## What to do next
- High underserved outcomes ($Opp \ge 10.0$)? Collect market price/cost/performance evidence and pass to **`jtbd-growth-strategist`** to evaluate candidate growth strategies.

---

## Mathematical Formula

$$\text{Opportunity Score (Opp)} = \text{Importance} + \max(\text{Importance} - \text{Satisfaction}, 0)$$

- **Scale Requirement**: Importance and Satisfaction MUST be on matching $1.0\text{--}10.0$ scales.
- **Threshold Classifications**:
  - `extreme_underserved`: $Opp \ge 15.0$
  - `high_underserved`: $12.0 \le Opp < 15.0$
  - `moderate_underserved`: $10.0 \le Opp < 12.0$
  - `appropriately_served`: $8.0 \le Opp < 10.0$
  - `overserved_candidate`: $Opp < 8.0$ (Requires $S > I$)

## Deterministic Script Execution

Run the bundled Python calculation script directly against a survey JSON file:

```bash
python3 skills/jtbd-opportunity-calculator/scripts/calculate_opportunity.py \
  path/to/survey_input.json > opportunity_results.json
```

## Output Format

```yaml
executive_summary:
  top_underserved_outcomes: []
  outcomes_not_to_prioritize: []
  data_strength: exploratory | adequate_but_not_representative | unverified
  recommended_next_step: ""

survey_metadata:
  importance_scale: "1_to_10"
  satisfaction_scale: "1_to_10"
  sample_size: 0
  population_definition: ""
  collection_method: ""

data_quality_status: complete | incomplete | invalid
calculation_status: completed | blocked

methodological_assessment:
  sample_size_status: adequate | small
  representativeness: unverified
  collection_method_status: reported | missing

scale_handling:
  calculation_scale: "1_to_10"
  normalization: "none"
  threshold_interpretation: "standard"

results:
  - id: ""
    statement: ""
    importance_mean: 0.0
    satisfaction_mean: 0.0
    satisfaction_gap: 0.0
    satisfaction_relation: below_importance | equal | above_importance
    opportunity_score: 0.0
    classification: extreme_underserved | high_underserved | moderate_underserved | appropriately_served | overserved_candidate
    overserved_signal: true | false
    segment: ""

data_limitations: []
```

## Reference

Read `references/opportunity-algorithm-rules.md` before:
- Handling small sample sizes ($N < 100$)
- Evaluating satisfaction relations ($S > I$)
- Rejecting non-10-point scales
