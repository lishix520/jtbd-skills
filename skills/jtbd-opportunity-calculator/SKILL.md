---
name: jtbd-opportunity-calculator
description: Calculate Outcome-Driven Innovation (ODI) Opportunity Scores from quantitative customer survey data. Use when asked to compute opportunity scores, classify outcomes into underserved or overserved categories, audit survey scale compatibility, report methodological limitations, or run deterministic calculations on survey datasets.
---

# JTBD Opportunity Calculator

Calculate Outcome-Driven Innovation® (ODI) Opportunity Scores from quantitative customer survey data.

The Opportunity Score identifies where customers struggle to get a job done (underserved) vs. where current solutions exceed customer value without adding utility (overserved).

## Scope

Input must include:
- `survey_metadata`: `importance_scale`, `satisfaction_scale`, `sample_size`, `population_definition`, `collection_method`
- `outcomes`: A list of Desired Outcome Statements with numerical `importance_mean` and `satisfaction_mean` ratings

Output:
- Calculated Opportunity Score per outcome statement
- Classification: `extreme_underserved` ($Opp \ge 15.0$), `high_underserved` ($12.0 \le Opp < 15.0$), `moderate_underserved` ($10.0 \le Opp < 12.0$), `appropriately_served` ($8.0 \le Opp < 10.0$), or `overserved_candidate` ($Opp < 8.0$)
- Satisfaction relation (`below_importance`, `matches_importance`, `above_importance`) and `overserved_signal` flag
- Methodological assessment (`sample_size_status`, `representativeness`, `collection_method_status`)
- Identification of missing ratings, scale mismatches, or data limitations

Do not:
- Claim sample size $\ge 100$ is proof of statistical validity or representativeness
- Classify high-importance outcomes ($I_i \ge 8.0$) as overserved simply because $S_i > I_i$
- Invent, estimate, or hallucinate numeric ratings from qualitative text or interview quotes
- Apply 10-point thresholds to any scale other than matching `1_to_10` inputs; v0.1 rejects non-10-point scales
- Formulate business growth strategies or product roadmaps (delegate to `jtbd-growth-strategist`)

## Mathematical Formula

For each outcome $i$, using 1-to-10 scales:

$$\text{Opportunity Score}_i = \text{Importance}_i + \max(\text{Importance}_i - \text{Satisfaction}_i, 0)$$

1. **Importance ($I_i$)**: Mean customer rating of outcome importance (1.0 to 10.0).
2. **Satisfaction ($S_i$)**: Mean customer rating of outcome satisfaction with current solutions (1.0 to 10.0).
3. **Satisfaction Gap**: If $I_i > S_i$, the gap is $(I_i - S_i)$. If $S_i \ge I_i$, the gap is $0$.
4. **Max Value**: On a 1-to-10 scale, maximum possible Opportunity Score is $10.0 + (10.0 - 1.0) = 19.0$.

## Opportunity Classification Rules

Opportunity classification is determined strictly by the Opportunity Score bounds:

- **`extreme_underserved`**: $Opp \ge 15.0$
- **`high_underserved`**: $12.0 \le Opp < 15.0$
- **`moderate_underserved`**: $10.0 \le Opp < 12.0$
- **`appropriately_served`**: $8.0 \le Opp < 10.0$
- **`overserved_candidate`**: $Opp < 8.0$

### Satisfaction Relation & Overserved Signal:
- `satisfaction_relation`:
  - `below_importance`: $I_i > S_i$
  - `matches_importance`: $I_i == S_i$
  - `above_importance`: $S_i > I_i$
- `overserved_signal`: Set to `true` ONLY when $Opp < 8.0$ AND $S_i > I_i$. High importance outcomes ($I_i \ge 8.0$) with $S_i > I_i$ have $Opp \ge 8.0$ and are classified as `appropriately_served`, NOT `overserved_candidate`.

## Scale & Data Quality Discipline

- **Data Quality Status**:
  - `complete`: Required metadata and numeric ratings are present.
  - `incomplete`: Missing values, missing metadata, or text input without ratings (`calculation_status: blocked`).
  - `invalid`: Scale mismatch, out-of-bounds ratings ($< 1.0$ or $> 10.0$), or non-numeric values.
- **Methodological Assessment**:
  - `sample_size_status`: `adequate` ($N \ge 100$), `small` ($N < 100$), or `unknown` ($N = 0$).
  - `representativeness`: `unverified` (sample size alone does not prove representativeness).
  - `collection_method_status`: `reported` vs `missing`.
- **Scale Handling**:
  - `calculation_scale`: "1_to_10"
  - `threshold_interpretation`: `standard` (for 1-10 scale) vs `heuristic_only` (for normalized non-10 scale).

## Procedure

1. Audit `survey_metadata`. Check for scale consistency and required fields. If numerical ratings are missing, return `data_quality_status: incomplete` and `calculation_status: blocked`.
2. Evaluate scale handling. If scales differ, reject calculation (`data_quality_status: invalid`).
3. For each outcome:
   a. Compute Satisfaction Gap: $\max(I_i - S_i, 0)$.
   b. Compute Opportunity Score: $I_i + \text{Satisfaction Gap}$.
   c. Determine `satisfaction_relation` (`below_importance`, `matches_importance`, `above_importance`).
   d. Set `overserved_signal: true` if $Opp < 8.0$ and $S_i > I_i$.
   e. Assign opportunity classification based on Opportunity Score.
4. Assess methodological limitations and populate `data_limitations`.
5. Return the calculation report.

## Output Format

```yaml
survey_metadata:
  importance_scale: "1_to_10"
  satisfaction_scale: "1_to_10"
  sample_size: 0
  population_definition: ""
  collection_method: ""

data_quality_status: complete | incomplete | invalid
calculation_status: completed | blocked

methodological_assessment:
  sample_size_status: adequate | small | unknown
  representativeness: unverified
  collection_method_status: reported | missing

scale_handling:
  calculation_scale: "1_to_10"
  normalization: none
  threshold_interpretation: standard

## Future Scope

Future versions may support caller-provided, documented normalization for non-10-point scales. v0.1 rejects all non-1_to_10 scales and does not apply normalization.

data_limitations: []

results:
  - id: ""
    statement: ""
    importance_mean: 0.0
    satisfaction_mean: 0.0
    satisfaction_gap: 0.0
    satisfaction_relation: below_importance | matches_importance | above_importance
    opportunity_score: 0.0
    classification: extreme_underserved | high_underserved | moderate_underserved | appropriately_served | overserved_candidate
    overserved_signal: true | false
    segment: ""

next_research_question: ""
```

## Reference Materials

Read `references/opportunity-algorithm-rules.md` before:
- Handling non-10-point scale normalization
- Analyzing opportunity landscapes and satisfaction relations
- Executing deterministic Python calculations using `scripts/calculate_opportunity.py`
