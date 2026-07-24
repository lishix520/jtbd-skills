# Invalid Desired Outcome Examples & Corrections

This document details 5 major **anti-patterns** when formulating Desired Outcome Statements. Each example illustrates an invalid candidate statement, the specific rule violation, and how to correct or re-classify it.

---

## Anti-Pattern 1: Solution / Feature Contamination

### Candidate Statement
`Minimize the time it takes to click the Jira export button`

### Rule Violation
- **Names Specific Products & Features**: Mentions `Jira` (software product) and `export button` (UI interface feature).
- **Solution-Dependent Metric**: If the team stops using Jira, this outcome statement becomes obsolete.

### Correction / Handling
- **Exclude**: Place under `excluded_items` with classification `solution`.
- **Solution-Free Rewrite**:
  ```text
  Minimize the time it takes to access status information
  ```

---

## Anti-Pattern 2: Compound Outcome Metric

### Candidate Statement
`Minimize the time and likelihood of error when verifying completeness`

### Rule Violation
- **Combines Multiple Metrics**: Merges duration (`time`) and probability (`likelihood`) into a single statement.
- **Prevents Quantifiable Rating**: Customers cannot give a distinct Importance and Satisfaction rating to two different performance metrics simultaneously.

### Correction / Handling
- **Exclude**: Place under `excluded_items` with classification `compound_outcome`.
- **Split into Two Formulaic Outcomes**:
  1. `Minimize the time it takes to verify the completeness of status information` (Metric: `time`)
  2. `Minimize the likelihood of omitting required status information during verification` (Metric: `likelihood`)

---

## Anti-Pattern 3: Vague Quality Buzzwords

### Candidate Statement
`Make verification faster and more reliable`

### Rule Violation
- **Non-Formulaic Syntax**: Uses vague adjectives (`faster`, `more reliable`) instead of the required ODI formulaic structure (`Direction + Metric + Target + Clarifier`).
- **Unmeasurable Target**: "Reliable" is a subjective buzzword, not an explicit measurable target.

### Correction / Handling
- **Exclude**: Place under `excluded_items` with classification `vague_metric`.
- **Formulaic Conversion**:
  1. `Faster` -> **`Minimize the time it takes to verify the completeness of status information`**
  2. `More reliable` -> **`Minimize the likelihood of miscalculating status metrics during verification`**

---

## Anti-Pattern 4: Abstract Likelihood Target

### Candidate Statement
`Minimize the likelihood of error during verification`

### Rule Violation
- **Abstract Placeholder Target**: Uses the generic word `error` as the target rather than naming a concrete, observable undesired event or failure mode.

### Correction / Handling
- **Exclude**: Place under `excluded_items` with classification `vague_metric`.
- **Concrete Event Rewrite**:
  ```text
  Minimize the likelihood of omitting required status information during verification
  ```

---

## Anti-Pattern 5: Emotional or Social Outcome

### Candidate Statement
`Maximize confidence during executive reviews`

### Rule Violation
- **Emotional State Contamination**: `Confidence` describes an internal psychological feeling, not a functional performance metric of the job executor's task.
- **Wrong Classification**: Belongs in Emotional Job analysis, NOT in functional Outcome-Driven Innovation metrics.

### Correction / Handling
- **Exclude**: Place under `excluded_items` with classification `emotional_social`.
- **Do NOT Force-Rewrite into Functional Outcome**: Emotional goals must be re-routed to Emotional Job analysis. Do not force-convert feelings into functional metrics.
