# Real-World Demo 3: Quantitative Survey Opportunity Ranking

This demo illustrates how **`opportunity-discovery`** handles quantitative survey ratings ($1\text{--}10$). It routes data to **`jtbd-opportunity-calculator`** to compute deterministic Opportunity Scores, while enforcing the rule that opportunity scores rank underserved outcome metrics but **do not** predict business success or prove willingness to pay.

---

## 📥 User Input (Quantitative Survey Dataset)
```json
{
  "survey_metadata": {
    "importance_scale": "1_to_10",
    "satisfaction_scale": "1_to_10",
    "sample_size": 120,
    "population_definition": "Enterprise Project Managers"
  },
  "outcomes": [
    {
      "id": "O-001",
      "statement": "Minimize the time it takes to verify the completeness of status information",
      "importance_mean": 9.2,
      "satisfaction_mean": 3.8
    },
    {
      "id": "O-002",
      "statement": "Minimize the likelihood of omitting required status information during verification",
      "importance_mean": 8.5,
      "satisfaction_mean": 6.1
    }
  ]
}
```

---

## 📋 Generated Opportunity Decision Brief

## 📋 Opportunity Decision Brief

### 🚦 Current Assessment
- **Readiness Stage**: `Decision-ready for next step`
- **Current Assessment**: Quantitative survey ratings ($N=120$) are complete. Outcome O-001 ranks as an **Extreme Underserved Outcome** ($Opp = 14.6$). Proceed to validate solution feasibility for O-001.
- **Confidence Rating**: `high`

### ✅ What is Known (Direct Evidence)
- Survey dataset ($N=120$ Enterprise PMs) demonstrates high importance ($I=9.2$) and low satisfaction ($S=3.8$) for verifying status information completeness.
- Mathematical Opportunity Score for O-001 is $14.6$ ($9.2 + (9.2 - 3.8)$).

### 💡 What is Only a Hypothesis
- Enterprise PMs are willing to pay a premium subscription price for a tool that addresses O-001.
- Unit cost-to-serve will allow a profitable margin for a solution targeting O-001.

### 🔍 What You CAN and CANNOT Conclude Right Now
- **CAN Conclude**: Verifying status completeness (O-001) is the top-ranked underserved outcome metric in this sample.
- **CANNOT Conclude**: This score does NOT predict overall company financial success, nor does it prove willingness to pay without price WTP testing.

### 🚀 Recommended Smallest Next Validation Step
"Gather pricing willingness-to-pay (WTP) and cost-to-serve evidence for O-001 solution concepts before committing to a commercial product roadmap."

---

### 📊 Structured Decision Brief Metadata

```yaml
decision_brief:
  current_stage: decision_ready_for_next_step
  evidence:
    direct:
      - "N=120 Enterprise PM survey dataset complete."
      - "Outcome O-001 Opportunity Score = 14.6 (Extreme Underserved)."
  hypotheses:
    - "Target segment will pay a premium for solutions addressing O-001."
  unknowns:
    - "Willingness to pay (WTP) price threshold"
    - "Unit cost-to-serve"
  current_assessment: "Opportunity ranking complete. Validate pricing willingness to pay and unit cost before strategic investment."
  confidence: high
  what_you_can_conclude_now:
    - "O-001 is the primary underserved outcome metric in this sample."
  what_you_cannot_conclude_yet:
    - "Commercial business success or pricing willingness to pay."
  recommended_action: "Pass ratings to jtbd-opportunity-calculator for score exports, then collect price/cost evidence for jtbd-growth-strategist."
  smallest_next_validation_step: "Conduct 5 pricing willingness-to-pay interviews with target Enterprise PMs."
  recommended_skill: "jtbd-opportunity-calculator"
```
