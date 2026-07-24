# JTBD Growth Strategy Matrix & Decision Rules

## Purpose

The **JTBD Growth Strategy Matrix** maps Outcome-Driven Innovation (ODI) Opportunity landscapes and market evidence to candidate growth strategies.

Rather than generating speculative consulting advice, this reference defines explicit prerequisite rules and disconfirming evidence for 5 core growth strategies.

---

## Strategy Families

Growth strategies are categorized into two distinct families:

### 1. Performance / Price / Cost Strategies (Mainstream Market Alignment)

These 4 strategies depend on position along the Performance, Price, and Cost-to-Serve continuum relative to incumbents:

- **`differentiated`**: High performance at a premium price. Target underserved outcomes ($Opp \ge 12.0$) for customers willing to pay more.
- **`dominant`**: Superior performance at a lower or parity price. Target underserved outcomes ($Opp \ge 10.0$) while maintaining lower/parity cost-to-serve.
- **`disruptive`**: Sufficient performance at a significantly lower price. Target overserved outcomes ($Opp < 8.0$) or non-consumers with a low cost-to-serve.
- **`sustaining`**: Incremental performance improvements at parity price. Target appropriately served outcomes ($8.0 \le Opp < 10.0$) to defend core market share.

### 2. Context-Specific Strategy (Niche / Environment Alignment)

- **`discrete`**: Target customers operating in a distinct physical environment, security regime, regulatory framework, or specialized workflow.
  - **Prerequisites**:
    1. Environmental, regulatory, security, geographic, or workflow constraint.
    2. Segment outcome priorities demonstrably different from mainstream users.
    3. Operational evidence supporting solution feasibility under the constraint.
  - **Price / Performance Position**: Contextual (can be premium or low-cost depending on niche constraints). Does NOT require overserved outcome scores.

---

## Structured Market Evidence Discipline

To achieve `status: evidence_aligned`, market context claims MUST use structured evidence objects with stated source types:

### Price Evidence Schema:
- `claim`: Statement of price position or willingness-to-pay.
- `source_type`: `stated_preference_survey` | `transactional_data` | `conjoint_analysis` | `customer_interview`
- `sample_size`: Numeric sample count ($N$) or `null`.
- `limitations`: List of known caveats.

### Cost Evidence Schema:
- `claim`: Statement of unit economics, production cost, or cost-to-serve.
- `source_type`: `unit_economics_model` | `operational_data` | `supplier_quote` | `cost_benchmark`
- `sample_size`: Numeric sample count ($N$) or `null`.
- `baseline`: Benchmark cost comparison (e.g., "incumbent cloud infrastructure cost").
- `limitations`: List of known caveats.

### Constraint Evidence Schema (for Discrete Strategies):
- `claim`: Statement of specific environmental, security, regulatory, or workflow constraint.
- `source_type`: `regulatory_document` | `security_audit` | `field_observation` | `customer_interview`
- `sample_size`: Numeric sample count ($N$) or `null`.
- `limitations`: List of known caveats.

### Performance Evidence Schema:
- `claim`: Statement of performance improvement.
- `source_type`: `controlled_user_test` | `internal_benchmark` | `field_observation` | `customer_interview`
- `sample_size`: Numeric sample count ($N$) or `null`.
- `baseline`: Specific incumbent solution benchmarked against (e.g., "manual spreadsheet verification").
- `limitations`: List of known caveats.

---

## Detailed Strategy Prerequisites & Disconfirming Evidence

### 1. Differentiated Strategy
- **Prerequisites**:
  - Underserved outcomes ($Opp \ge 12.0$).
  - Structured `price_evidence` demonstrating willingness to pay a premium.
  - Structured `performance_evidence` demonstrating superior capability.
- **Disconfirming Evidence**:
  - Mainstream satisfaction is high ($S_i \ge 8.0$).
  - Customers are price-sensitive or reject premium pricing.

### 2. Dominant Strategy
- **Prerequisites**:
  - Underserved outcomes ($Opp \ge 10.0$).
  - Structured `performance_evidence` showing superior performance.
  - Structured `cost_evidence` demonstrating equal or lower cost-to-serve than incumbents.
- **Disconfirming Evidence**:
  - High unit economics require a premium price position (`cost_evidence` missing or unviable).

### 3. Disruptive Strategy
- **Prerequisites**:
  - Overserved outcomes ($Opp < 8.0$) OR non-consumption evidence.
  - Low-cost target price position relative to incumbents.
  - Structured `cost_evidence` supporting low-cost unit economics.
  - Sufficient performance on core functional outcomes.
- **Disconfirming Evidence**:
  - Extreme underserved outcomes ($Opp \ge 15.0$) dominate the market landscape.

### 4. Discrete Strategy
- **Prerequisites**:
  - Segment evidence identifies a distinct environmental, regulatory, security, geographic, or workflow constraint.
  - Segment outcome priorities are demonstrably different from mainstream users.
  - Operational evidence supports the feasibility of addressing the constraint.
- **Disconfirming Evidence**:
  - Segment outcome priorities match mainstream users.

### 5. Sustaining Strategy
- **Prerequisites**:
  - Outcomes are appropriately served ($8.0 \le Opp < 10.0$).
  - Parity price position and cost structure.
- **Disconfirming Evidence**:
  - Extreme underserved outcomes ($Opp \ge 15.0$) are left unaddressed.

---

## Assessment Status Rules

- **`evidence_aligned`**:
  - `opportunity_analysis.data_quality_status == "complete"`
  - `opportunity_analysis.calculation_status == "completed"`
  - `methodological_assessment.sample_size_status == "adequate"` ($N \ge 100$)
  - The selected candidate strategy meets EVERY prerequisite specified in its own rule with structured, sourced evidence.
- **`hypothesis_only`**:
  - `methodological_assessment.sample_size_status == "small"` ($N < 100$), OR evidence relies on unverified domain rationale.
- **`insufficient_evidence`**:
  - `opportunity_analysis.calculation_status != "completed"`, OR required evidence for the candidate strategy is missing.
