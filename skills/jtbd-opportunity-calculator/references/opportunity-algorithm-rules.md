# Opportunity Algorithm & Methodological Rules

## Purpose

The **Opportunity Algorithm** quantifies the degree to which a customer's desired outcome is underserved or overserved.

---

## Formula

$$Opp_i = I_i + \max(I_i - S_i, 0)$$

Where:
- $I_i$ = Mean Importance rating for outcome $i$
- $S_i$ = Mean Satisfaction rating for outcome $i$ with current solutions

### Key Mathematical Principles:
1. **Importance Foundation**: Importance is added directly ($I_i$). Low importance outcomes can never achieve a high Opportunity Score even if satisfaction is zero.
2. **One-Way Gap Add-on**: The gap $(I_i - S_i)$ adds to score only when $I_i > S_i$. When $S_i \ge I_i$, the gap is $0$.
3. **Upper Bound**: On a 1-to-10 scale, the maximum score is $10.0 + (10.0 - 1.0) = 19.0$.

---

## Opportunity Landscape Classifications (1-to-10 Scale)

Classification is determined strictly by the Opportunity Score bounds:

| Opportunity Score Range | Classification | Strategic Meaning |
| :--- | :--- | :--- |
| **$Opp \ge 15.0$** | `extreme_underserved` | Critical market pain point. Prime target for breakthrough innovation. |
| **$12.0 \le Opp < 15.0$** | `high_underserved` | Strong opportunity. High willingness to pay for better performance. |
| **$10.0 \le Opp < 12.0$** | `moderate_underserved` | Core product improvement opportunity. |
| **$8.0 \le Opp < 10.0$** | `appropriately_served` | Customer needs are satisfied. Sustaining innovations apply. |
| **$Opp < 8.0$** | `overserved_candidate` | Low overall opportunity score. Potential target for cost-reduction/disruption. |

### Satisfaction Relation & Overserved Signal:
- `satisfaction_relation`:
  - `below_importance`: $I_i > S_i$ (Unmet need gap exists)
  - `matches_importance`: $I_i = S_i$ (Perfect alignment)
  - `above_importance`: $S_i > I_i$ (Satisfaction exceeds importance)
- `overserved_signal`: `true` ONLY when $Opp < 8.0$ AND $S_i > I_i$.
- **CRITICAL**: Do NOT classify an outcome as `overserved_candidate` simply because $S_i > I_i$. If $I_i = 9.0$ and $S_i = 9.5$, $Opp = 9.0$, which is `appropriately_served`. High importance + high satisfaction is NOT overserved.

---

## Methodological Discipline & Representativeness

1. **Sample Size Heuristic**:
   - $N \ge 100$: `sample_size_status: adequate`
   - $N < 100$: `sample_size_status: small` (Flag limitation: "Sample size N < 100; scores are exploratory hypotheses.")
2. **Representativeness**:
   - Sample size alone does NOT prove representativeness. Always set `representativeness: unverified` unless formal sampling frame analysis is attached.
3. **Data Quality Status**:
   - `complete`: All required ratings and metadata are present.
   - `incomplete`: Numerical ratings or required fields are missing.
   - `invalid`: Out-of-bounds ratings or scale mismatches.

---

## Future Scope: Scale Normalization

Future versions may support caller-provided normalization for 5-point or 7-point scales using linear transformations:

$$Scale_{10} = 1.0 + \left( \frac{Rating - Min_{orig}}{Max_{orig} - Min_{orig}} \right) \times 9.0$$

- **v0.1 Rule**: v0.1 strictly requires matching `1_to_10` scales and does not normalize non-10 scales. Any non-10-point scale input is rejected as `data_quality_status: invalid`.
