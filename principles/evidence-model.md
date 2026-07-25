# Evidence Gate & Confidence Model Protocol

This document defines the shared **Evidence Gate Protocol** across all skills in the **JTBD Skills Suite**.

It ensures that AI agents strictly separate direct facts from hypotheses and unknowns, and refuse to fabricate business conclusions when evidence is missing.

---

## 🛡️ The 4 Evidence Tiers

| Evidence Tier | Definition | Example | Allowed Upgrades & Rules |
| :--- | :--- | :--- | :--- |
| **`direct_evidence`** | Verifiable, source-linked customer quotes, observable behaviors, or raw dataset facts. | *"I spend two hours every Friday manually copying status updates."* | Must include a `source_id` or quote snippet. |
| **`inference`** | A logical interpretation derived from direct evidence. | *"Manual consolidation creates time pressure prior to Friday reviews."* | Must explicitly state the underlying `direct_evidence` source. |
| **`hypothesis`** | An unverified statement, assumption, or proposed solution without customer facts. | *"Teams will pay $50/month for automated report generation."* | **MUST NOT** be presented as a customer fact or market demand. |
| **`unknown`** | Critical research questions that current material cannot answer. | *"Whether users are willing to switch from spreadsheets."* | Triggers the **smallest next validation step**. |

---

## 🎯 The 5 Confidence Evaluation Dimensions

Confidence reflects **evidence quality, relevance, traceability, coverage, and consistency**—not merely whether the input is quantitative. (A small N=6 unverified survey does NOT equal high confidence).

| Dimension | Key Evaluation Question |
| :--- | :--- |
| **1. Traceability** | Are direct quotes, raw survey data, or observable behaviors attached with source IDs? |
| **2. Relevance** | Does the evidence come directly from target users operating in the target real-world circumstance? |
| **3. Coverage** | Is this a single isolated incident (N=1), or a repeated pattern across multiple users? |
| **4. Consistency** | Do multiple sources align without unmitigated contradictions? |
| **5. Decision Alignment** | Does the evidence directly address the specific commercial decision under review? |

### Confidence Rating Guide:
- **`low`**: Pure product ideas, isolated feedback quotes (N=1-2), unverified vendor claims, or small unrepresentative surveys.
- **`medium`**: Multiple traceable customer interview quotes demonstrating repeated workarounds and friction patterns.
- **`high`**: Verified quantitative survey datasets (N >= 100) combined with qualitative interview evidence and market price/cost benchmarks.

---

## 🛑 The 5 Evidence Gate Readiness Statuses

| Readiness Status | Meaning | System Behavior & Action |
| :--- | :--- | :--- |
| **`Idea only`** | Input contains only a product idea or feature suggestion; no customer facts. | **Do not build.** Formulate initial hypotheses and output an interview plan. |
| **`Anecdotal signal`** | Input contains isolated quotes, complaints, or feedback from 1-2 users. | **Do not build.** Extract context & workarounds; find repeated behavior patterns. |
| **`Evidence emerging`** | Multiple traceable customer quotes demonstrate repeated friction & workarounds. | Map customer jobs, forces, or outcomes. Design targeted quantitative research. |
| **`Decision-ready for next step`** | Sufficient evidence exists to justify a specific experiment, survey, or research step. | Recommend the smallest next validation experiment or survey. |
| **`Not decision-ready`** | Input lacks critical price, cost, performance, or switching context evidence. | **Block strategy recommendation.** Output the specific evidence gap to fill. |

---

## ❌ Hard Evidence Violation Rules

1. **Pure Ideas Must Not Be Upgraded**: A product idea or feature request MUST NOT be classified as proof of market demand or willingness to pay.
2. **Qualitative Text Cannot Compute Opportunity Scores**: Qualitative interview quotes MUST NOT be converted into fake 1-10 numerical ratings.
3. **Opportunity Scores Do Not Predict Success**: An Opportunity Score (Opp >= 10.0) ranks underserved outcomes; it DOES NOT prove willingness to pay or business success.
4. **Quantitative Data Does Not Automatically Mean High Confidence**: Survey data with small samples (N < 100) or unverified sampling methodology MUST be tagged as `exploratory` with `low` or `medium` confidence.
5. **No Strategy Without Market Evidence**: Strategic recommendations (`growth-strategist`) MUST stop at `insufficient_evidence` if price WTP, cost-to-serve, or performance data is absent.
6. **Every Missing Evidence State Must Include a Next Step**: Whenever evidence is insufficient, the skill MUST output a concrete **smallest next validation step**.
