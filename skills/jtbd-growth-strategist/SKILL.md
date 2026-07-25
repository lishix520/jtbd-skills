---
name: jtbd-growth-strategist
description: Map quantitative Opportunity Scores and market evidence to candidate growth strategies (differentiated, dominant, disruptive, discrete, sustaining). Use when given opportunity calculation results, segment metadata, and structured price/cost/performance evidence, and asked to evaluate strategic positioning or disconfirming evidence. Do not use to invent market evidence or recommend product strategy without required prerequisites.
---

# JTBD Growth Strategist

**Audit your market evidence before deciding to raise prices, differentiate, cut costs, or target a niche.**

---

## Use this when
- You have quantitative Opportunity Scores ($Opp \ge 10.0$) AND structured market evidence (price willingness-to-pay, unit cost, performance benchmarks, or environmental constraints).
- You want to evaluate whether a proposed strategy (differentiated, dominant, disruptive, discrete, sustaining) has sufficient prerequisite evidence.
- You want to identify disconfirming evidence that contradicts a proposed strategy.

## Don't use this when
- You only have qualitative interview notes or complaints without market evidence (use `jtbd-context-explorer` or `jtbd-forces-analyzer`).
- You have not yet computed quantitative Opportunity Scores (use `jtbd-opportunity-calculator`).
- You want to invent pricing or strategy recommendations without data.

## Minimum input
- **Minimum Input**: `opportunity_analysis` results from `jtbd-opportunity-calculator`, target `segment_definition`, and structured market evidence (`price_evidence`, `cost_evidence`, `performance_evidence`, `constraint_evidence`). If required evidence is missing, returns `status: insufficient_evidence`.

## What you get
1. **Decision Readiness Summary**: Decision under review, present evidence, missing evidence, what cannot be decided yet, and the smallest next research step.
2. **Strategy Assessment Status**: `evidence_aligned` (all prerequisites met), `hypothesis_only` ($N < 100$), or `insufficient_evidence` (missing evidence).
3. **Excluded Strategies**: Explicit reasons and contradicting evidence for excluded strategies.

## Quick prompt
> *"Audit market evidence and evaluate candidate growth strategies for this opportunity dataset: '[Paste opportunity results and market evidence]'."*

## What to do next
- Status is `insufficient_evidence`? Use `decision_readiness.smallest_next_research_step` to gather missing price WTP, cost-to-serve, or performance benchmark evidence via **`jtbd-switch-interview`** or user surveys.

---

## Strategy Matrix Prerequisites

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

## Output Format

```yaml
decision_readiness:
  decision_under_review: ""
  evidence_present: []
  evidence_missing: []
  what_cannot_be_decided_yet: []
  smallest_next_research_step: ""

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

## Reference

Read `references/growth-strategy-matrix-rules.md` before:
- Checking price, cost, and performance evidence schemas
- Verifying discrete strategy prerequisite constraints
- Identifying disconfirming market evidence
