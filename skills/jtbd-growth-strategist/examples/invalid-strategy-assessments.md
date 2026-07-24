# Invalid Growth Strategy Assessment Examples & Corrections

This document details 4 major **anti-patterns and invalid strategy evaluations** when evaluating market growth strategies. Each example illustrates an invalid assessment attempt, the specific rule violation, and how to correct or re-classify it.

---

## Anti-Pattern 1: Selecting Differentiated Strategy Based on High Score Alone (Missing WTP / Performance Evidence)

### Input Attempt
```yaml
opportunity_analysis:
  data_quality_status: complete
  calculation_status: completed
  results:
    - id: "O1"
      statement: "Minimize the time it takes to verify status information"
      opportunity_score: 15.5
      classification: extreme_underserved
market_context:
  price_evidence: []       # Missing willingness-to-pay evidence!
  performance_evidence: [] # Missing superior performance evidence!
strategy_constraints:
  target_price_position: premium
```

### Rule Violation
- **Missing Required Evidence**: A Differentiated strategy requires structured `price_evidence` demonstrating willingness to pay a premium AND structured `performance_evidence` demonstrating superior capability. High Opportunity Score alone does NOT justify a Differentiated strategy.

### Correct System Response
```yaml
strategy_assessment:
  status: insufficient_evidence
  primary_rationale: "Differentiated strategy requires structured price_evidence (willingness to pay premium) and performance_evidence (superior capability)."

evidence_gaps:
  - "Price evidence demonstrating customer willingness to pay premium pricing for speed."
  - "Performance evidence demonstrating that target solution achieves superior speed over incumbents."

next_validation_actions:
  - "Conduct a conjoint analysis survey to measure premium price willingness for 80% faster verification."
```

---

## Anti-Pattern 2: Claiming Dominant Strategy Without Cost Evidence

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

## Anti-Pattern 3: Selecting Discrete Strategy Based on Regulatory Constraint Alone (Missing Distinct Outcome Priority Evidence)

### Input Attempt
```yaml
segment_definition:
  name: "Healthcare Security PMs"
  evidence: ["HIPAA air-gapped security compliance constraint"]
opportunity_analysis:
  results:
    - id: "O1"
      statement: "Minimize the time it takes to format updates"
      opportunity_score: 8.5
      classification: appropriately_served
market_context:
  constraint_evidence:
    - claim: "Healthcare PMs require HIPAA air-gapped compliance."
      source_type: regulatory_document
```

### Rule Violation
- **Missing Distinct Outcome Priority Evidence**: A Discrete strategy cannot be triggered by a compliance tag or constraint evidence alone. It requires evidence that the niche segment prioritizes outcomes differently from mainstream users.

### Correct System Response
```yaml
strategy_assessment:
  status: insufficient_evidence
  primary_rationale: "Discrete strategy requires evidence that Healthcare PMs exhibit distinct outcome priorities compared to mainstream users."

excluded_strategies:
  - strategy: discrete
    reason: "Compliance constraint alone does not establish distinct outcome prioritization."

evidence_gaps:
  - "Segment evidence demonstrating that Healthcare PMs rank specific outcomes (e.g., data privacy) significantly higher than mainstream users."
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
