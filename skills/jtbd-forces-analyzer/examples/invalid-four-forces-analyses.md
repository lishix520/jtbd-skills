# Invalid Four Forces Analysis Examples & Corrections

This document details 4 major **anti-patterns and invalid Four Forces evaluations**. Each example illustrates an invalid analysis attempt, the specific rule violation, and how to correct or re-classify it.

---

## Anti-Pattern 1: Manufacturing Pull from a Solution Feature Request

### Source Excerpt
> "Please add a Jira button that automatically creates a weekly report."

### Invalid Analysis Attempt
```yaml
# ❌ INCORRECT OUTPUT
analysis_status: evidence_extracted
forces:
  pull:
    - statement: "Jira button that automatically creates weekly reports"
      status: direct_evidence
```

### Rule Violation
- **Feature Request Contamination**: Proposing a product button is a `feature_request` (solution preference), NOT evidence of Pull for an evaluated prospective alternative. Creating a Pull force without customer evidence of an evaluated alternative violates JTBD rules.

### Correct System Response
```yaml
# ✅ CORRECT OUTPUT
analysis_status: insufficient_switching_context

# Stops because no prospective alternative or current approach context is established by a single feature request statement!
switching_context:
  current_approach:
    status: unknown
  prospective_alternative:
    status: unknown

evidence_gaps:
  - "Current reporting approach and candidate alternative solution under evaluation."
```

---

## Anti-Pattern 2: Treating Vendor Marketing Claims as Customer-Verified Pull

### Source Excerpt
> Vendor Brochure: "Our Acme Dashboard cuts reporting time by 80%."
> Customer Quote: "We currently compile reports in spreadsheets and are evaluating the Acme Dashboard."

### Invalid Analysis Attempt
```yaml
# ❌ INCORRECT OUTPUT
forces:
  pull:
    - statement: "Cuts reporting time by 80%"
      status: direct_evidence # ❌ WRONG: Claiming customer-verified performance!
```

### Rule Violation
- **Unverified Vendor Claim Over-Assertion**: Marketing claims made by vendors represent prospective benefits, but MUST be tagged `status: unverified_claim` until verified by actual customer research or benchmark testing.

### Correct Four Forces Analysis
```yaml
# ✅ CORRECT OUTPUT
forces:
  pull:
    - id: PULL-001
      statement: "Acme Dashboard promises an 80% reduction in reporting time."
      status: unverified_claim # ✅ CORRECT: Tagged as unverified vendor claim
      evidence:
        - source_id: vendor-01
          excerpt: "Our Acme Dashboard cuts reporting time by 80%."

switching_context:
  current_approach:
    statement: "Spreadsheets"
    status: direct_evidence
  prospective_alternative:
    statement: "Acme Dashboard"
    status: direct_evidence
```

---

## Anti-Pattern 3: Classifying Generic Spreadsheet Dislike as Push

### Source Excerpt
> "I really dislike updating spreadsheets every Thursday."

### Invalid Analysis Attempt
```yaml
# ❌ INCORRECT OUTPUT
forces:
  push:
    - statement: "User dislikes updating spreadsheets"
      status: direct_evidence
```

### Rule Violation
- **Conflating Generic Dislike with Change Pressure**: Disliking a tool proves mild dissatisfaction. It does NOT constitute a Push force unless the material demonstrates performance failure, missed deadlines, unacceptable risk, or operational pressure to change.

### Correct System Response
```yaml
# ✅ CORRECT OUTPUT
analysis_status: insufficient_switching_context

# Stops because minor dissatisfaction does not establish pressure to switch or a prospective alternative!
evidence_gaps:
  - "Specific operational friction or deadline failures creating pressure to replace spreadsheets."
```

---

## Anti-Pattern 4: Calculating Numerical Four Forces Scores or Purchase Probability

### Source Excerpt
> "Push: Missed deadlines (1). Pull: Automated aggregation (1). Habit: Routine templates (1). Anxiety: Data loss concern (1)."

### Invalid Analysis Attempt
```yaml
# ❌ INCORRECT OUTPUT
four_forces_calculation:
  push_score: 8.0
  pull_score: 9.0
  habit_score: 5.0
  anxiety_score: 4.0
  formula: "(Push + Pull) - (Habit + Anxiety)"
  net_switching_force: 8.0
  purchase_probability: "85%" # ❌ WRONG: Inventing numerical scoring formulas!
```

### Rule Violation
- **Numerical Scoring & Probability Hallucination**: The Four Forces framework is a qualitative tension model. Adding, weighting, totaling, or calculating mathematical formulas ($Push + Pull > Habit + Anxiety$) or predicting purchase probability is strictly prohibited in v0.1.

### Correct Four Forces Analysis
```yaml
# ✅ CORRECT OUTPUT
switching_readiness:
  status: hypothesis_available
  statement: "Switching pressure (PUSH) and attraction (PULL) suggest interest in changing, but inertia (HABIT) and data loss concerns (ANXIETY) represent unmitigated adoption barriers."
  supporting_force_ids:
    - PUSH-001
    - PULL-001
    - HABIT-001
    - ANX-001
  missing_evidence:
    - "Empirical trial data verifying data loss mitigation."
```
