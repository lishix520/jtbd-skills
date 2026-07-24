# Valid Growth Strategy Assessment Examples

> These are illustrative strategy assessments generated from structured ODI opportunity data and market context claims.
> The candidate strategy output represents **evidence-aligned decision support**, not a guaranteed commercial victory or automated consulting report.

---

## Example 1: Differentiated Strategy Assessment

- **Core Functional Job**: `Prepare a project status update`
- **Target Segment**: Enterprise Project Managers ($N = 250$)

```yaml
job_context:
  core_functional_job: "Prepare a project status update"
  job_executor: "Enterprise Project Manager"
  segment_name: "Enterprise PMs"

strategy_assessment:
  status: evidence_aligned
  primary_rationale: "Enterprise PMs exhibit extreme underserved outcomes (O1 Opp = 15.0). Stated preference surveys confirm premium willingness to pay ($50/user/mo), and controlled user tests demonstrate an 80% reduction in check time."

candidate_strategies:
  - strategy: differentiated
    confidence: high
    strategic_fit_rationale: "Aligns with premium price position and superior performance expectations for high-value underserved verification needs."
    supporting_outcomes:
      - "O1: Minimize the time it takes to verify the completeness of status information (Opp: 15.0)"
    prerequisite_conditions:
      - "Customer willingness to pay premium price position ($50/user/mo)."
      - "Demonstrated 80% reduction in status verification time."

excluded_strategies:
  - strategy: disruptive
    reason: "Overserved outcomes do not dominate the landscape, and customers actively seek superior performance rather than low-cost sufficient capability."
    contradicting_evidence:
      - "O1 Opp = 15.0 (Extreme Underserved)"
      - "Willingness to pay premium pricing ($50/user/mo)"

disconfirming_evidence: []
evidence_gaps:
  - "Actual transactional conversion data at the $50/user/mo price point."
next_validation_actions:
  - "Run a targeted landing page price-test with 50 enterprise PM leads to validate actual purchasing intent at $50/user/mo."
```

---

## Example 2: Discrete Strategy Assessment (Niche Context & Exploratory Observational Evidence)

- **Core Functional Job**: `Prepare a project status update`
- **Target Segment**: Defense & National Security Project Managers ($N = 110$)

```yaml
job_context:
  core_functional_job: "Prepare a project status update"
  job_executor: "Security Project Manager"
  segment_name: "Defense & National Security PMs"

strategy_assessment:
  status: hypothesis_only
  primary_rationale: "Defense PMs operate under classified air-gapped security compliance constraints and prioritize data leakage prevention (Opp = 15.0 vs mainstream Opp = 4.0). While candidate strategic fit is clear, operational feasibility relies on small-sample observational field data (N = 12)."

candidate_strategies:
  - strategy: discrete
    confidence: medium
    strategic_fit_rationale: "Solves a unique classified security constraint for a segment with distinct outcome priorities separate from the mainstream market."
    supporting_outcomes:
      - "O1: Minimize the likelihood of data leakage during status verification (Opp: 15.0 vs Mainstream Opp: 4.0)"
    prerequisite_conditions:
      - "Classified air-gapped security compliance constraint."
      - "Demonstrably higher prioritization of data leakage prevention compared to mainstream users."

excluded_strategies:
  - strategy: disruptive
    reason: "Discrete strategy does not rely on overserved mainstream outcomes or low-cost price positioning."
    contradicting_evidence: []

disconfirming_evidence: []
evidence_gaps:
  - "Independent feasibility evidence from controlled trials across defense server environments."
next_validation_actions:
  - "Deploy a zero-network pilot container in 2 isolated defense lab environments to gather controlled feasibility benchmarks."
```

---

## Example 3: Dominant Strategy Assessment (Performance + Unit Cost Evidence)

- **Core Functional Job**: `Prepare a project status update`
- **Target Segment**: Mid-Market PMs ($N = 180$)

```yaml
job_context:
  core_functional_job: "Prepare a project status update"
  job_executor: "Mid-Market Project Manager"
  segment_name: "Mid-Market PMs"

strategy_assessment:
  status: evidence_aligned
  primary_rationale: "Mid-market PMs experience high underserved outcome needs (O1 Opp = 13.5). Controlled benchmarks confirm 60% faster execution, while automated serverless unit economics achieve 40% lower cost-to-serve than legacy incumbents."

candidate_strategies:
  - strategy: dominant
    confidence: high
    strategic_fit_rationale: "Delivers superior performance on key underserved outcomes while matching or undercutting incumbent pricing due to cost-to-serve advantages."
    supporting_outcomes:
      - "O1: Minimize the time it takes to locate status information (Opp: 13.5)"
    prerequisite_conditions:
      - "Superior performance on status location (60% benchmark gain)."
      - "Lower unit cost-to-serve (40% cost reduction vs legacy architecture)."

excluded_strategies:
  - strategy: differentiated
    reason: "Mid-market PMs are cost-conscious and reject premium price surcharges despite high performance needs."
    contradicting_evidence:
      - "Stated preference survey indicates resistance to premium pricing over incumbent parity."

disconfirming_evidence: []
evidence_gaps:
  - "Long-term serverless scaling costs under high-volume status syncing."
next_validation_actions:
  - "Run a 30-day trial with 10 mid-market teams offering parity pricing to measure retention."
```
