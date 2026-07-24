# Invalid Opportunity Score Calculation Examples & Corrections

This document details 4 major **anti-patterns and invalid calculations** when evaluating survey data. Each example illustrates an invalid or limited input, the specific rule violation, and the expected system output.

---

## Anti-Pattern 1: Out-of-Bounds Ratings

### Input Attempt
```yaml
survey_metadata:
  importance_scale: "1_to_10"
  satisfaction_scale: "1_to_10"
  sample_size: 100
outcomes:
  - id: "O1"
    statement: "Minimize the time it takes to verify information"
    importance_mean: 11.0  # Invalid out-of-bounds rating
    satisfaction_mean: 4.0
```

### Rule Violation
- Rating $11.0$ exceeds the maximum bound of the 1-to-10 scale ($1.0 \le Rating \le 10.0$).
- Accepting out-of-bounds numbers produces nonsensical Opportunity Scores ($> 19.0$).

### Correct System Response
```yaml
data_quality_status: invalid
calculation_status: blocked
data_limitations:
  - "Out-of-bounds rating: importance_mean and satisfaction_mean must be within 1.0 to 10.0."
results: []
```

---

## Anti-Pattern 2: Scale Mismatch / Unsupported Scale (v0.1)

### Input Attempt
```yaml
survey_metadata:
  importance_scale: "1_to_5"  # Unsupported scale in v0.1
  satisfaction_scale: "1_to_10"
  sample_size: 150
outcomes:
  - id: "O1"
    statement: "Minimize the time it takes to locate status information"
    importance_mean: 4.5
    satisfaction_mean: 5.0
```

### Rule Violation
- **Scale Mismatch**: `importance_scale` and `satisfaction_scale` differ.
- **Unsupported Scale**: v0.1 strictly requires matching 1-to-10 scales to apply standard ODI opportunity cutoffs.

### Correct System Response
```yaml
data_quality_status: invalid
calculation_status: blocked
data_limitations:
  - "Unsupported scale: v0.1 requires matching 1_to_10 importance and satisfaction scales."
results: []
```

---

## Anti-Pattern 3: Text Prompt Guessing (No Numerical Ratings)

### Input Attempt
```yaml
survey_metadata:
  importance_scale: "1_to_10"
  satisfaction_scale: "1_to_10"
  sample_size: 0
text_feedback: "Project managers hate waiting for status info and feel it's extremely important."
```

### Rule Violation
- **Anti-Fabrication Principle**: Never invent or hallucinate numerical ratings ($I=9.5, S=2.0$) from qualitative text or customer interview quotes.
- Quantitative calculation requires explicit numerical survey ratings.

### Correct System Response
```yaml
data_quality_status: incomplete
calculation_status: blocked
data_limitations:
  - "Missing numerical data: No outcome ratings provided."
  - "Qualitative text feedback was not converted into numerical ratings."
results: []
```

---

## Anti-Pattern 4: Small Sample Size (Exploratory Data Limitation)

### Input Attempt
```yaml
survey_metadata:
  importance_scale: "1_to_10"
  satisfaction_scale: "1_to_10"
  sample_size: 15  # Small sample size
  population_definition: "Internal PM team"
  collection_method: ""  # Missing collection method
outcomes:
  - id: "O1"
    statement: "Minimize the time it takes to locate status information"
    importance_mean: 8.0
    satisfaction_mean: 5.0
```

### Methodological Rule Handling
- Small sample size ($N < 100$) does NOT block calculation, but MUST be explicitly flagged as an exploratory hypothesis.
- `representativeness` remains `unverified`.

### Correct System Response
```yaml
data_quality_status: complete
calculation_status: completed

methodological_assessment:
  sample_size_status: small
  representativeness: unverified
  collection_method_status: missing

data_limitations:
  - "Sample size N = 15 (< 100); results represent exploratory hypotheses."
  - "Collection method missing."

results:
  - id: "O1"
    statement: "Minimize the time it takes to locate status information"
    importance_mean: 8.0
    satisfaction_mean: 5.0
    satisfaction_gap: 3.0
    satisfaction_relation: below_importance
    opportunity_score: 11.0
    classification: moderate_underserved
    overserved_signal: false
```
