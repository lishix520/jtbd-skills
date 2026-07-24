# Invalid Growth Strategy Assessment Examples & Corrections

This document details 4 major **anti-patterns and invalid strategy evaluations** when evaluating market growth strategies. Each example illustrates an invalid assessment attempt, the specific rule violation, and how to correct or re-classify it.

---

## Anti-Pattern 1: Attempting Dominant Strategy Without Cost Evidence

### Input Attempt
```yaml
opportunity_analysis:
  data_quality_status: complete
  calculation_status: completed
  results:
    - id: "O1"
      statement: "Minimize the time it takes to verify status information"
      opportunity_score: 13.5
      classification: high_underserved
market_context:
  performance_evidence:
    - claim: "Solution reduces check time by 50%."
      source_type: internal_benchmark
  cost_evidence: []  # Missing cost evidence!
strategy_constraints:
  target_price_position: low_cost
```

### Rule Violation
- **Missing Cost Evidence**: A Dominant strategy requires structured `cost_evidence` proving lower or parity cost-to-serve. Claiming a Dominant strategy without cost-structure data is unverified speculation.

### Correct System Response
```yaml
strategy_assessment:
  status: insufficient_evidence
  primary_rationale: "Dominant strategy requires structured cost_evidence to verify lower or parity cost-to-serve."

evidence_gaps:
  - "Unit economics model or operational cost data comparing cost-to-serve against legacy incumbents."

next_validation_actions:
  - "Construct a unit-cost benchmark comparing infrastructure and support costs against incumbent alternatives."
```

---

## Anti-Pattern 2: Attempting Discrete Strategy Without Distinct Outcome Priorities

### Input Attempt
```yaml
segment_definition:
  name: "Healthcare PMs"
  evidence: ["HIPAA compliance tag"]
opportunity_analysis:
  results:
    - id: "O1"
      statement: "Minimize the time it takes to format updates"
      opportunity_score: 8.5
      classification: appropriately_served
```

### Rule Violation
- **Missing Distinct Outcome Priority Evidence**: A Discrete strategy cannot be triggered by a segment name or compliance tag alone. It requires evidence that the niche segment prioritizes outcomes differently from mainstream users.

### Correct System Response
```yaml
strategy_assessment:
  status: insufficient_evidence
  primary_rationale: "Discrete strategy requires evidence that Healthcare PMs exhibit distinct outcome priorities compared to mainstream users."

excluded_strategies:
  - strategy: discrete
    reason: "Compliance tag alone does not establish distinct outcome prioritization."

evidence_gaps:
  - "Quantitative or qualitative evidence demonstrating that Healthcare PMs rank specific outcomes (e.g., data privacy) significantly higher than mainstream users."
```

---

## Anti-Pattern 3: Upgrading Small Sample Data to `evidence_aligned`

### Input Attempt
```yaml
opportunity_analysis:
  data_quality_status: complete
  calculation_status: completed
  methodological_assessment:
    sample_size_status: small  # N = 15 (< 100)
    representativeness: unverified
results:
  - id: "O1"
    statement: "Minimize status check delay"
    opportunity_score: 14.0
```

### Rule Violation
- **Over-Asserting Confidence**: Small sample size ($N < 100$) cannot support `status: evidence_aligned`. Strategy outputs must be downgraded to `hypothesis_only`.

### Correct System Response
```yaml
strategy_assessment:
  status: hypothesis_only
  primary_rationale: "Opportunity Scores are based on a small sample (N = 15 < 100). Candidate strategies represent exploratory hypotheses."

candidate_strategies:
  - strategy: differentiated
    confidence: low
    strategic_fit_rationale: "Exploratory hypothesis based on small sample data (N = 15)."

evidence_gaps:
  - "Statistically adequate quantitative survey sample (N >= 100)."
```

---

## Anti-Pattern 4: Forcing Disruptive Strategy When Extreme Underserved Outcomes Dominate

### Input Attempt
```yaml
opportunity_analysis:
  results:
    - id: "O1"
      statement: "Minimize the time it takes to verify information"
      opportunity_score: 16.5  # Extreme Underserved!
      classification: extreme_underserved
strategy_constraints:
  target_price_position: low_cost
```

### Rule Violation
- **Contradicting Opportunity Landscape**: Disruptive strategies apply when outcomes are overserved ($Opp < 8.0$) or non-consumption is present. Forcing a low-cost, low-performance Disruptive product into a market dominated by extreme underserved needs ($Opp = 16.5$) violates ODI strategy selection rules.

### Correct System Response
```yaml
strategy_assessment:
  status: evidence_aligned
  primary_rationale: "Disruptive strategy is excluded because the market landscape is dominated by extreme underserved needs."

excluded_strategies:
  - strategy: disruptive
    reason: "Disruptive low-cost strategy is contradicted when extreme underserved outcomes (O1 Opp = 16.5) dominate the market."
    contradicting_evidence:
      - "O1 Opp = 16.5 (Extreme Underserved)"
```
