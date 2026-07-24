---
name: jtbd-growth-strategist
description: Evaluate market growth strategy candidates (Differentiated, Dominant, Disruptive, Discrete, Sustaining) using calculated ODI Opportunity Scores, segment definitions, price/performance evidence, and market constraints. Use when asked to map market opportunities to growth strategies, evaluate strategy feasibility against customer evidence, identify disconfirming evidence, or define next validation actions.
---

# JTBD Growth Strategist

Evaluate and map Outcome-Driven Innovation® (ODI) Opportunity landscapes into candidate market growth strategies.

The Growth Strategist acts as a decision support engine. It evaluates whether customer and market evidence aligns with specific growth strategies (Differentiated, Dominant, Disruptive, Discrete, or Sustaining) without forcing speculative strategic conclusions when critical evidence is missing.

## Scope

Input must include:
- `opportunity_analysis`: `data_quality_status`, `calculation_status`, `methodological_assessment`, and `results` from `jtbd-opportunity-calculator`
- `segment_definition`: Target segment name, evidence, and sample size
- `market_context`: Current alternatives, structured `price_evidence`, `performance_evidence`, and `nonconsumption_evidence`
- `strategy_constraints`: Target price position and target performance position

Output:
- `strategy_assessment`: `status` (`evidence_aligned`, `hypothesis_only`, `insufficient_evidence`)
- `candidate_strategies`: List of supported strategy options with rationale and required conditions
- `excluded_strategies`: Strategies rejected due to evidence contradictions or missing prerequisites
- `disconfirming_evidence`: Customer or market data contradicting specific strategy options
- `evidence_gaps`: Missing data preventing a conclusive strategy evaluation
- `next_validation_actions`: Smallest specific experiments or data collection steps needed

Do not:
- Force a single "winner" strategy when price/performance evidence is missing
- Claim `evidence_aligned` is a forecast of commercial success or market victory
- Recommend a Disruptive strategy without evidence of overserved outcomes ($Opp < 8.0$) or non-consumption
- Recommend a Differentiated strategy without high-value underserved outcomes ($Opp \ge 12.0$) and willingness-to-pay evidence
- Invent financial forecasts, ROI projections, or market size estimations

## Strategy Selection Prerequisites

### Performance / Price Strategies
| Strategy | Minimum Evidence Prerequisites |
| :--- | :--- |
| **`differentiated`** | Underserved outcomes ($Opp \ge 12.0$) AND structured price evidence showing willingness to pay a premium for superior performance. |
| **`dominant`** | Underserved outcomes ($Opp \ge 10.0$) AND performance + cost evidence showing the solution can deliver superior performance at lower or parity cost. |
| **`disruptive`** | Overserved outcomes ($Opp < 8.0$) OR non-consumption evidence; requires target low-cost position and sufficient performance. |
| **`sustaining`** | Appropriately served outcomes ($8.0 \le Opp < 10.0$) in core market; requires parity cost and incremental performance. |

### Context-Specific Strategy
| Strategy | Minimum Evidence Prerequisites |
| :--- | :--- |
| **`discrete`** | Triggered by distinct environmental, regulatory, workflow, or geographic constraints different from mainstream users; requires distinct outcome-priority evidence. Price/performance position is contextual. |

## Strategy Assessment Status Discipline

- **`evidence_aligned`**:
  - `opportunity_analysis.data_quality_status == "complete"`
  - `opportunity_analysis.calculation_status == "completed"`
  - `methodological_assessment.sample_size_status == "adequate"` ($N \ge 100$)
  - `price_evidence` and `performance_evidence` contain reported claims with source types
  - At least one strategy meets all prerequisites without unmitigated disconfirming evidence
- **`hypothesis_only`**:
  - `methodological_assessment.sample_size_status == "small"` ($N < 100$), OR price/performance evidence is based on domain rationale rather than market research. Candidate strategies are explicitly labeled as hypotheses.
- **`insufficient_evidence`**:
  - `opportunity_analysis.calculation_status != "completed"`, OR structured `price_evidence` / `performance_evidence` is completely missing.

## Procedure

1. Audit `opportunity_analysis` (`data_quality_status`, `calculation_status`, `sample_size_status`).
2. Evaluate `market_context` for structured price and performance evidence (checking `source_type` and claims).
3. Compare opportunity landscape against the Strategy Prerequisites Matrix.
4. Identify `disconfirming_evidence` for each strategy (e.g., attempting a premium price position when extreme underserved outcomes dominate).
5. Categorize candidate strategies into supported vs excluded.
6. Determine `strategy_assessment.status` (`evidence_aligned`, `hypothesis_only`, or `insufficient_evidence`).
7. Formulate `evidence_gaps` and `next_validation_actions`.

## Output Format

```yaml
job_context:
  core_functional_job: ""
  job_executor: ""
  segment_name: ""

strategy_assessment:
  status: evidence_aligned | hypothesis_only | insufficient_evidence
  primary_rationale: ""

candidate_strategies:
  - strategy: differentiated | dominant | disruptive | discrete | sustaining
    confidence: high | medium | low
    strategic_fit_rationale: ""
    supporting_outcomes: []
    prerequisite_conditions: []

excluded_strategies:
  - strategy: differentiated | dominant | disruptive | discrete | sustaining
    reason: ""
    contradicting_evidence: []

disconfirming_evidence: []
evidence_gaps: []
next_validation_actions: []
```

## Reference Materials

Read `references/growth-strategy-matrix-rules.md` before:
- Distinguishing between Performance/Price strategies vs Context-Specific (`discrete`) strategy
- Evaluating structured evidence source types (`stated_preference_survey`, `controlled_user_test`, etc.)
- Mapping disconfirming evidence to strategy exclusions
