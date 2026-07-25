# Quantitative ODI Survey Question Template

When conducting an Outcome-Driven Innovation (ODI) survey, present each Desired Outcome Statement to respondents with two separate 1-to-10 scales:

---

## Question Format

### Outcome Statement:
> **"[Insert Desired Outcome Statement here]"**
> *(e.g., "Minimize the time it takes to verify the completeness of status information")*

#### 1. How important is this outcome to you when executing this job?
```text
[1] Not at all Important ───► [5] Moderately Important ───► [10] Extremely Important
```

#### 2. How satisfied are you with your current approach's ability to achieve this outcome?
```text
[1] Not at all Satisfied ───► [5] Moderately Satisfied ───► [10] Extremely Satisfied
```

---

## Instructions for Data Aggregation

1. Calculate the arithmetic mean for **Importance** ($I$) across all respondents ($N \ge 100$).
2. Calculate the arithmetic mean for **Satisfaction** ($S$) across all respondents.
3. Input the mean scores into `survey-input-template.json` or `survey-input-template.csv`.
4. Pass the JSON file to `calculate_opportunity.py` to obtain deterministic Opportunity Scores.
