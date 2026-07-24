---
name: jtbd-growth-strategist
description: Evaluate market growth strategy candidates (Differentiated, Dominant, Disruptive, Discrete, Sustaining) using calculated ODI Opportunity Scores, segment definitions, price/performance evidence, and market constraints. Use when asked to map market opportunities to growth strategies, evaluate strategy feasibility against customer evidence, identify disconfirming evidence, or define next validation actions.
---

# JTBD Growth Strategist

Evaluate and map Outcome-Driven Innovation® (ODI) Opportunity landscapes into candidate market growth strategies.

The Growth Strategist acts as a decision support engine. It evaluates whether customer evidence supports specific growth strategies (Differentiated, Dominant, Disruptive, Discrete, or Sustaining) without forcing speculative strategic recommendations when critical evidence is missing.

## Scope

Input must include:
- `opportunity_analysis`: Opportunity Scores, classifications, and data limitations from `jtbd-opportunity-calculator`
- `segment_definition`: Target segment definition, evidence, and sample size
- `market_context`: Current alternatives, price evidence, performance evidence, and nonconsumption evidence
- `strategy_constraints`: Target price position and target performance position

Output:
- `strategy_assessment`: `status` (`recommendation_ready`, `hypothesis_only`, `insufficient_evidence`)
- `candidate_strategies`: List of supported strategy options with rationale and required conditions
- `excluded_strategies`: Strategies rejected due to evidence contradictions or missing prerequisites
- `disconfirming_evidence`: Customer or market data contradicting specific strategy options
- `evidence_gaps`: Missing data preventing a conclusive strategy recommendation
- `next_validation_actions`: Smallest specific experiments or data collection steps needed

Do not:
- Force a single "winner" strategy when price/performance evidence is missing
- Recommend a Disruptive strategy without evidence of overserved outcomes or non-consumption
- Recommend a Differentiated strategy without high-value underserved outcomes ($Opp \ge 12.0$) and willingness-to-pay evidence
- Invent financial forecasts, ROI projections, or market size estimations
- Treat `exploratory` survey data as conclusive proof of market opportunity

## Strategy Selection Prerequisites

| Strategy | Minimum Evidence Prerequisites |
| :--- | :--- |
| **`differentiated`** | Underserved outcomes ($Opp \ge 12.0$) AND evidence that customers will pay a premium for superior performance. |
| **`dominant`** | Underserved outcomes ($Opp \ge 10.0$) AND evidence that the solution can simultaneously deliver superior performance at lower or parity cost. |
| **`disruptive`** | Overserved outcomes ($Opp < 8.0$) OR non-consumption evidence; requires target low-cost position and sufficient performance. |
| **`discrete`** | Unique environmental, regulatory, workflow, or geographic constraints distinct from mainstream market, with separate outcome prioritization. |
| **`sustaining`** | Appropriately served outcomes ($8.0 \le Opp < 10.0$) in core market; requires parity cost and incremental performance. |

## Strategy Assessment Status Discipline

- **`recommendation_ready`**: Calculated opportunity scores are `complete`, sample size is adequate, price/performance evidence is present, and at least one strategy meets all prerequisites without unmitigated disconfirming evidence.
- **`hypothesis_only`**: Opportunity scores are `exploratory` ($N < 100$), OR price/performance evidence is based on domain rationale rather than market data. Candidate strategies must be explicitly labeled as hypotheses.
- **`insufficient_evidence`**: `opportunity_analysis` is incomplete/blocked, or price/performance evidence is entirely absent.

## Procedure

1. Audit `opportunity_analysis` status (`complete` vs `exploratory` vs `incomplete`).
2. Evaluate `market_context` and `strategy_constraints` for price and performance evidence.
3. Compare opportunity landscape against the Strategy Prerequisites Matrix.
4. Identify `disconfirming_evidence` for each strategy (e.g., attempting a premium price position for overserved outcomes).
5. Categorize candidate strategies into supported vs excluded.
6. Determine `strategy_assessment.status` (`recommendation_ready`, `hypothesis_only`, or `insufficient_evidence`).
7. Formulate `evidence_gaps` and `next_validation_actions`.

## Output Format

```yaml
job_context:
  core_functional_job: ""
  job_executor: ""
  segment_name: ""

strategy_assessment:
  status: recommendation_ready | hypothesis_only | insufficient_evidence
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
- Distinguishing between Differentiated and Dominant strategy prerequisites
- Identifying disconfirming evidence for Disruptive strategies
- Mapping non-consumption evidence to Discrete vs Disruptive strategies
