# JTBD Growth Strategy Matrix & Decision Rules

## Purpose

The **JTBD Growth Strategy Matrix** maps Outcome-Driven Innovation (ODI) Opportunity landscapes and market evidence to candidate growth strategies.

Rather than generating speculative consulting advice, this reference defines explicit prerequisite rules and disconfirming evidence for 5 core growth strategies.

---

## Growth Strategy Classification Matrix

```text
                  High Customer Satisfaction / Overserved
                                    │
                                    │   DISRUPTIVE
        DISCRETE                    │   Low price,
        Niche environment,          │   sufficient performance
        distinct workflow           │
                                    │
Low Performance ────────────────────┼──────────────────── High Performance
                                    │
                                    │   DOMINANT / DIFFERENTIATED
        SUSTAINING                  │   High performance,
        Incremental improvement,    │   underserved outcomes
        parity price                │
                                    │
                  Low Customer Satisfaction / Underserved
```

---

## Detailed Strategy Prerequisites & Disconfirming Evidence

### 1. Differentiated Strategy
Target customers are willing to pay a premium price for a solution that solves significantly underserved outcomes.

- **Required Prerequisites**:
  - Opportunity Score $\ge 12.0$ (High or Extreme Underserved) on key functional outcomes.
  - Price evidence demonstrating customer willingness to pay a premium.
  - Performance evidence showing target solution can achieve superior performance on target outcomes.
- **Disconfirming Evidence**:
  - Customer satisfaction with existing solutions is high ($S_i \ge 8.0$).
  - Target customers are price-sensitive or unwilling to pay extra for performance gains.

### 2. Dominant Strategy
Target customers seek significantly better performance AND lower or parity cost simultaneously.

- **Required Prerequisites**:
  - Opportunity Score $\ge 10.0$ (Moderate, High, or Extreme Underserved).
  - Cost evidence demonstrating the solution can be delivered at equal or lower cost than incumbents.
  - Performance evidence showing superior performance on key outcomes.
- **Disconfirming Evidence**:
  - High unit economics or high cost structure requiring a premium price position.

### 3. Disruptive Strategy
Target customers are overserved by existing solutions, or are non-consumers locked out of the market by cost/complexity.

- **Required Prerequisites**:
  - Opportunity Score $< 8.0$ (Overserved outcomes) OR explicit non-consumption evidence.
  - Target price position is low-cost relative to current market alternatives.
  - Solution provides "sufficient" performance on core outcomes while removing unnecessary features.
- **Disconfirming Evidence**:
  - Mainstream customers demand higher performance and reject simpler, low-cost alternatives.
  - Underserved outcomes ($Opp \ge 12.0$) dominate the market landscape.

### 4. Discrete Strategy
Target customers execute the job in a unique context, environment, regulatory regime, or workflow that requires a specialized solution.

- **Required Prerequisites**:
  - Segment definition evidence showing distinct outcome prioritization compared to mainstream users.
  - Specific environmental, security, regulatory, or workflow constraints.
- **Disconfirming Evidence**:
  - Segment outcome priorities are identical to the mainstream market.

### 5. Sustaining Strategy
Incumbent market with satisfied customers ($8.0 \le Opp < 10.0$) requiring continuous incremental improvements to maintain market share.

- **Required Prerequisites**:
  - Outcomes are appropriately served ($8.0 \le Opp < 10.0$).
  - Parity price and incremental performance improvements.
- **Disconfirming Evidence**:
  - Extreme underserved outcomes ($Opp \ge 15.0$) exist and are left unaddressed.

---

## Assessment Status Rules

1. **`recommendation_ready`**:
   - `data_quality_status == "complete"`
   - `sample_size_status == "adequate"` ($N \ge 100$)
   - Both price evidence and performance evidence are reported.
2. **`hypothesis_only`**:
   - Data is `exploratory` ($N < 100$), OR price/performance evidence is based on domain rationale.
3. **`insufficient_evidence`**:
   - `data_quality_status != "complete"`, OR price/performance evidence is completely missing.
