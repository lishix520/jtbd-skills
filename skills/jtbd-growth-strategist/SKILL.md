---
name: jtbd-growth-strategist
description: Evaluate market growth strategy candidates (Differentiated, Dominant, Disruptive, Discrete, Sustaining) using calculated ODI Opportunity Scores, segment definitions, price/cost/performance evidence, and market constraints. Use when asked to map market opportunities to growth strategies, evaluate strategy feasibility against customer evidence, identify disconfirming evidence, or define next validation actions.
---

# JTBD Growth Strategist

Evaluate and map Outcome-Driven Innovation® (ODI) Opportunity landscapes into candidate market growth strategies.

The Growth Strategist acts as a decision support engine. It evaluates whether customer and market evidence aligns with specific growth strategies (Differentiated, Dominant, Disruptive, Discrete, or Sustaining) without forcing speculative strategic conclusions when critical evidence is missing.

## Scope

Input must include:
- `opportunity_analysis`: `data_quality_status`, `calculation_status`, `methodological_assessment`, and `results` from `jtbd-opportunity-calculator`
- `segment_definition`: Target segment name, evidence, and sample size
- `market_context`: Current alternatives, structured `price_evidence`, `cost_evidence`, `performance_evidence`, `constraint_evidence`, and `nonconsumption_evidence`
- `strategy_constraints`: Target price position and target performance position

Output:
- `strategy_assessment`: `status` (`evidence_aligned`, `hypothesis_only`, `insufficient_evidence`)
- `candidate_strategies`: List of supported strategy options with rationale and required conditions
- `excluded_strategies`: Strategies rejected due to evidence contradictions or missing prerequisites
- `disconfirming_evidence`: Customer or market data contradicting specific strategy options
- `evidence_gaps`: Missing data preventing a conclusive strategy evaluation
- `next_validation_actions`: Smallest specific experiments or data collection steps needed

Do not:
- Force a single "winner" strategy when price/cost/performance evidence is missing
- Claim `evidence_aligned` is a forecast of commercial success or market victory
- Recommend a Dominant strategy without structured `cost_evidence` demonstrating lower/parity cost-to-serve
- Recommend a Disruptive strategy without structured `cost_evidence` and overserved outcomes ($Opp < 8.0$) or non-consumption
- Recommend a Differentiated strategy without high-value underserved outcomes ($Opp \ge 12.0$) and willingness-to-pay evidence
- Recommend a Discrete strategy without explicit evidence of distinct outcome priorities
- Invent financial forecasts, ROI projections, or market size estimations

## Strategy Selection Prerequisites

### Performance / Price / Cost Strategies
| Strategy | Minimum Evidence Prerequisites |
| :--- | :--- |
| **`differentiated`** | Underserved outcomes ($Opp \ge 12.0$) AND structured `price_evidence` showing willingness to pay a premium AND structured `performance_evidence` showing superior capability. |
| **`dominant`** | Underserved outcomes ($Opp \ge 10.0$) AND structured `performance_evidence` showing superior performance AND `cost_evidence` showing lower or parity cost-to-serve. |
| **`disruptive`** | Overserved outcomes ($Opp < 8.0$) OR non-consumption evidence AND structured `cost_evidence` supporting low-cost position and sufficient performance. |
| **`sustaining`** | Appropriately served outcomes ($8.0 \le Opp < 10.0$) in core market; requires parity price and cost structure for incremental performance. |

### Context-Specific Strategy
| Strategy | Minimum Evidence Prerequisites |
| :--- | :--- |
| **`discrete`** | 1. Environmental, regulatory, security, geographic, or workflow constraint.<br>2. Segment outcome priorities demonstrably different from mainstream users.<br>3. Operational evidence supporting solution feasibility under the constraint. |

## Strategy Assessment Status Discipline

- **`evidence_aligned`**:
  - `opportunity_analysis.data_quality_status == "complete"`
  - `opportunity_analysis.calculation_status == "completed"`
  - `methodological_assessment.sample_size_status == "adequate"` ($N \ge 100$)
  - The selected candidate strategy meets EVERY prerequisite specified in its own rule with structured, sourced evidence
  - No unmitigated disconfirming evidence exists
- **`hypothesis_only`**:
  - `methodological_assessment.sample_size_status == "small"` ($N < 100$), OR evidence relies on unverified domain rationale. Candidate strategies are explicitly labeled as hypotheses.
- **`insufficient_evidence`**:
  - `opportunity_analysis.calculation_status != "completed"`, OR required evidence for the candidate strategy is missing.

## Procedure

1. Audit `opportunity_analysis` (`data_quality_status`, `calculation_status`, `sample_size_status`).
2. Evaluate `market_context` for structured price, cost, and performance evidence (checking `source_type` and claims).
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
- Evaluating structured evidence source types for `price_evidence`, `cost_evidence`, and `performance_evidence`
- Assessing prerequisites for `dominant` vs `differentiated` strategies
- Auditing `discrete` strategy prerequisites (constraints + distinct outcome priorities)
