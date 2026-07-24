---
name: jtbd-opportunity-calculator
description: Calculate Opportunity Scores for Desired Outcome Statements using quantitative survey ratings (Importance and Satisfaction). Use when asked to compute ODI opportunity scores, classify outcomes into underserved, appropriately served, or overserved categories, audit survey scale compatibility, or report data quality and sample limitations.
---

# JTBD Opportunity Calculator

Calculate Outcome-Driven Innovation® (ODI) Opportunity Scores from quantitative customer survey data.

The Opportunity Score identifies where customers struggle to get a job done (underserved) vs. where they are receiving features they do not value (overserved).

## Scope

Input must include:
- `survey_metadata`: `importance_scale`, `satisfaction_scale`, `sample_size`, `population_definition`, `collection_method`
- `outcomes`: A list of Desired Outcome Statements with numerical `importance_mean` and `satisfaction_mean` ratings

Output:
- Calculated Opportunity Score per outcome statement
- Classification: `underserved` ($Opp \ge 10.0$), `appropriately_served` ($8.0 \le Opp < 10.0$), or `overserved` ($Opp < 8.0$ or $Satisfaction > Importance$)
- Assessment status: `statistically_valid` vs `exploratory`
- Identification of scale mismatches, missing ratings, or data quality limitations

Do not:
- Invent, estimate, or hallucinate numeric ratings from qualitative text or interviews
- Recalculate or redefine Core Functional Jobs, Job Maps, or Outcome Statements
- Apply the 10.0 threshold to non-10-point scales without scale normalization
- Formulate business growth strategies or product roadmaps (delegate to `jtbd-growth-strategist`)

## Mathematical Formula

For each outcome $i$, using identical 1-to-10 scales:

$$\text{Opportunity Score}_i = \text{Importance}_i + \max(\text{Importance}_i - \text{Satisfaction}_i, 0)$$

1. **Importance ($I_i$)**: Mean customer rating of outcome importance (1.0 to 10.0).
2. **Satisfaction ($S_i$)**: Mean customer rating of outcome satisfaction with current solutions (1.0 to 10.0).
3. **Satisfaction Gap**: If $I_i > S_i$, the gap is $(I_i - S_i)$. If $S_i \ge I_i$, the gap is $0$.
4. **Max Value**: On a 1-to-10 scale, maximum possible Opportunity Score is $10.0 + (10.0 - 1.0) = 19.0$.

## Scale & Data Quality Discipline

- **Identical Scale Requirement**: `importance_scale` and `satisfaction_scale` MUST be identical. If scales differ (e.g., 5-point vs 10-point), reject calculation or normalize scales before applying the formula.
- **Sample Validity Classification**:
  - `statistically_valid`: `sample_size` $\ge 100$, representative population definition, and collection method specified.
  - `exploratory`: `sample_size` $< 100$ or missing survey metadata. Scores must be flagged as exploratory hypotheses.
- **No Text Guessing**: If `importance_mean` or `satisfaction_mean` is null, state `status: insufficient_data`. Never guess numbers from phrases like "users really want this".

## Procedure

1. Audit `survey_metadata`. Check for scale consistency and sample size.
2. Validate that each outcome contains numerical `importance_mean` and `satisfaction_mean`.
3. Compute Satisfaction Gap: $\max(I_i - S_i, 0)$.
4. Compute Opportunity Score: $I_i + \text{Satisfaction Gap}$.
5. Classify opportunity landscape:
   - **`underserved`**: $Opp \ge 10.0$ (High priority for core innovation)
   - **`appropriately_served`**: $8.0 \le Opp < 10.0$
   - **`overserved`**: $Opp < 8.0$ or $S_i > I_i$ (Candidate for disruptive/low-cost innovation)
6. Sort outcomes by Opportunity Score descending.
7. Return calculation report and data limitation warnings.

## Validation Checklist

Reject calculation or return warnings if:

- `importance_mean` or `satisfaction_mean` is non-numeric, null, or out of scale bounds
- `importance_scale` and `satisfaction_scale` differ without explicit normalization
- Ratings are derived from text prompt speculation rather than survey data
- Opportunity threshold 10.0 is applied directly to a 5-point or 7-point scale without transformation

## Output Format

```yaml
survey_metadata:
  importance_scale: "1_to_10"
  satisfaction_scale: "1_to_10"
  sample_size: 0
  population_definition: ""
  collection_method: ""
  data_quality_status: statistically_valid | exploratory | invalid_metadata

calculation_summary:
  total_outcomes_evaluated: 0
  underserved_count: 0
  appropriately_served_count: 0
  overserved_count: 0

results:
  - id: ""
    statement: ""
    importance_mean: 0.0
    satisfaction_mean: 0.0
    satisfaction_gap: 0.0
    opportunity_score: 0.0
    classification: underserved | appropriately_served | overserved
    segment: ""

data_limitations: []
next_research_question: ""
```

## Reference Materials

Read `references/opportunity-algorithm-rules.md` before:
- Handling 5-point or 7-point survey scale normalization
- Interpreting opportunity landscapes ($Opp \ge 15.0$ extreme vs $10.0 \le Opp < 12.0$ moderate)
- Handling multi-segment survey results
