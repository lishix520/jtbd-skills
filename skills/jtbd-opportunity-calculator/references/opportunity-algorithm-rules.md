# Opportunity Algorithm & Data Discipline Rules

## Purpose

The **Opportunity Algorithm** is the mathematical core of Outcome-Driven Innovation (ODI). It quantifies the degree to which a customer's desired outcome is underserved or overserved.

---

## The Formula

$$Opp_i = I_i + \max(I_i - S_i, 0)$$

Where:
- $I_i$ = Mean Importance rating for outcome $i$
- $S_i$ = Mean Satisfaction rating for outcome $i$ with current solutions

### Mathematical Properties:
1. **Focus on Importance**: Importance is added directly ($I_i$). An outcome with low importance can never achieve a high Opportunity Score, even if satisfaction is zero.
2. **One-Way Gap Penalty**: The gap $(I_i - S_i)$ only adds value when $I_i > S_i$. If $S_i > I_i$, $\max(I_i - S_i, 0) = 0$, meaning high satisfaction does not penalize basic importance.
3. **Upper Bound**: On a standard 1-to-10 scale, the theoretical maximum score is $10.0 + (10.0 - 1.0) = 19.0$.

---

## Opportunity Landscape Thresholds (1-to-10 Scale)

In standard Strategyn / ODI methodology using 1-to-10 scales:

| Opportunity Score Range | Classification | Market & Innovation Meaning |
| :--- | :--- | :--- |
| **$Opp \ge 15.0$** | Extreme Underserved | Critical market pain point. Exceptional opportunity for breakthrough/differentiated product. |
| **$12.0 \le Opp < 15.0$** | High Underserved | Strong opportunity. High customer willingness to pay for better solutions. |
| **$10.0 \le Opp < 12.0$** | Moderate Underserved | Worth addressing in core product updates. |
| **$8.0 \le Opp < 10.0$** | Appropriately Served | Customer needs are satisfied. Sustaining innovations apply. |
| **$Opp < 8.0$ (or $S_i > I_i$)** | Overserved | Features/perks exceed customer value. prime target for Disruptive (cheaper) innovation. |

---

## Scale Normalization Rules

If survey data uses a 5-point or 7-point Likert scale, it MUST be normalized to a 10-point scale before applying the 10.0 threshold:

### Linear Transformation Formula (Min-Max):

$$Scale_{10} = 1.0 + \left( \frac{Rating - Min_{orig}}{Max_{orig} - Min_{orig}} \right) \times 9.0$$

- **5-point scale (1 to 5)**: $Rating_{10} = 1.0 + (Rating_5 - 1) \times 2.25$
- **7-point scale (1 to 7)**: $Rating_{10} = 1.0 + (Rating_7 - 1) \times 1.5$

---

## Data Quality & Anti-Fabrication Rules

1. **No Text Guessing**: Never infer $I_i = 8.5$ or $S_i = 2.1$ from customer quotes or text descriptions. If numeric means are missing, set `data_quality_status: invalid_metadata` or `status: insufficient_data`.
2. **Sample Size Thresholds**:
   - `sample_size \ge 100`: `statistically_valid`
   - `sample_size < 100`: `exploratory` (Report data limitation: "Sample size N < 100; scores represent exploratory hypotheses.")
3. **Out-of-Bounds Check**: Any rating $< 1.0$ or $> 10.0$ (on a 1-to-10 scale) must be rejected as invalid data.
