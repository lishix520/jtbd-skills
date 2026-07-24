# Invalid Context Analysis Examples & Corrections

This document details 4 major **anti-patterns and invalid context evaluations** when extracting qualitative JTBD context evidence. Each example illustrates an invalid analysis attempt, the specific rule violation, and how to correct or re-classify it.

---

## Anti-Pattern 1: Misclassifying a Feature Request as a Core Functional Job

### Source Excerpt
> "I really need a Jira button that automatically creates my weekly status report."

### Invalid Analysis Attempt
```yaml
# ❌ INCORRECT OUTPUT
core_functional_job:
  statement: "Automatically create weekly status reports using a Jira button"
  status: validated_core_job
```

### Rule Violation
- **Feature Request Contamination**: Proposing a product capability ("Jira button") is a solution request, NOT a Core Functional Job. Recording a solution feature request as a validated Core Job violates solution-free JTBD principles.

### Correct Context Analysis
```yaml
# ✅ CORRECT OUTPUT
feature_requests:
  - id: FR-001
    statement: "Jira button that automatically creates weekly status reports"
    status: direct_evidence
    evidence:
      - source_id: interview-01
        excerpt: "I really need a Jira button that automatically creates my weekly status report."

evidence_gaps:
  - "The underlying solution-free functional progress the user attempts to make when updating status."
```

---

## Anti-Pattern 2: Misclassifying General Dissatisfaction as Non-Consumption

### Source Excerpt
> "I really dislike updating spreadsheets every Thursday afternoon."

### Invalid Analysis Attempt
```yaml
# ❌ INCORRECT OUTPUT
non_consumption:
  - id: NC-001
    statement: "Spreadsheets"
    barrier_type: complexity
```

### Rule Violation
- **Insufficient Evidence for Non-Consumption**: Complaining about an active tool ("dislike spreadsheets") proves dissatisfaction with a `current_approach`. It does NOT prove non-consumption unless the source demonstrates absence, avoidance, inability, or refusal to adopt an available alternative due to an explicit barrier.

### Correct Context Analysis
```yaml
# ✅ CORRECT OUTPUT
current_approaches:
  - id: CA-001
    statement: "Updating spreadsheets on Thursday afternoons"
    type: workaround
    status: direct_evidence
    evidence:
      - source_id: interview-01
        excerpt: "I really dislike updating spreadsheets every Thursday afternoon."

# non_consumption is empty because no alternative evaluation or barrier is stated!
non_consumption: []

evidence_gaps:
  - "Whether alternative status tools were evaluated or blocked by organizational constraints."
```

---

## Anti-Pattern 3: Promoting a Deadline Circumstance into a "Fast & Reliable" Outcome

### Source Excerpt
> "The weekly review is tomorrow morning, and three team leads have not submitted their updates yet."

### Invalid Analysis Attempt
```yaml
# ❌ INCORRECT OUTPUT
desired_outcomes:
  - statement: "Minimize the time it takes to quickly and reliably generate project status reports before deadlines"
    status: direct_evidence
```

### Rule Violation
- **Premature Outcome Speculation & Buzzword Injection**: A deadline circumstance ("review is tomorrow") provides direct evidence of situational pressure. It does NOT justify fabricating a formulaic ODI Desired Outcome statement with quality adjectives ("quickly and reliably"). Outcomes belong in `jtbd-outcome-engineer`, not context exploration.

### Correct Context Analysis
```yaml
# ✅ CORRECT OUTPUT
circumstances:
  - id: CIR-001
    statement: "Imminent review deadline tomorrow morning with three missing team updates."
    status: direct_evidence
    evidence:
      - source_id: interview-01
        excerpt: "The weekly review is tomorrow morning, and three team leads have not submitted their updates yet."

desired_progress:
  - id: DP-001
    statement: "Obtain missing team updates prior to the review deadline."
    status: inferred
    evidence:
      - source_id: interview-01
        excerpt: "The weekly review is tomorrow morning, and three team leads have not submitted their updates yet."
```

---

## Anti-Pattern 4: Promoting Executive Social Anxiety into a Functional Outcome

### Source Excerpt
> "I feel anxious before the review because I do not want executive leadership to think I have lost control of the project."

### Invalid Analysis Attempt
```yaml
# ❌ INCORRECT OUTPUT
core_functional_job: "Prevent executives from thinking I lost control of the project"
# OR
desired_outcomes:
  - statement: "Minimize the likelihood of appearing out of control to executive leadership"
```

### Rule Violation
- **Conflating Social Perception with Functional Progress**: Wanting to avoid negative executive perception ("lost control") is a **Social Signal**. It is NOT a Core Functional Job or a functional ODI outcome statement. Conflating social anxiety with functional jobs contaminates downstream job mapping.

### Correct Context Analysis
```yaml
# ✅ CORRECT OUTPUT
emotional_signals:
  - id: EM-001
    statement: "Anxiety prior to project review"
    status: direct_evidence
    evidence:
      - source_id: interview-01
        excerpt: "I feel anxious before the review"

social_signals:
  - id: SOC-001
    statement: "Avoid being perceived by executive leadership as having lost control of the project"
    audience: "Executive leadership"
    status: direct_evidence
    evidence:
      - source_id: interview-01
        excerpt: "because I do not want executive leadership to think I have lost control of the project."
```
