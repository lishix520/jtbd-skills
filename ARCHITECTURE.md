# JTBD Skills Suite Architecture & Pipeline Contracts

This document details the architectural design, data pipelines, evidence discipline, and contract boundaries across the 5 atomic skills in the **JTBD Skills Suite**.

---

## 🏗️ Architectural Overview

The repository implements the Outcome-Driven Innovation® (ODI) methodology as a chain of 5 single-responsibility agent skills.

```text
[ Research Quotes / Feedback ]
              │
              ▼
    1. jtbd-job-definer  ───────►  Core Functional Job (Candidate / Accepted)
              │
              ▼
    2. jtbd-job-mapper   ───────►  Universal Job Map (8 Stages & Flow Edges)
              │
              ▼
 3. jtbd-outcome-engineer ─────►  Desired Outcome Statements (Direction + Metric + Target)
              │
              ▼
 4. jtbd-opportunity-calculator ►  Opportunity Scores & Classifications (Python Script)
              │
              ▼
   5. jtbd-growth-strategist ───►  Growth Strategy Assessment (Evidence Aligned / Insufficient)
```

---

## 📋 Skill Input/Output Contracts & Evidence Boundaries

| Skill Name | Expected Input Contract | Output Contract | Evidence Discipline & Stopping Rule |
| :--- | :--- | :--- | :--- |
| **`jtbd-job-definer`** | Customer research quotes, feedback, or candidate statements | Solution-free Core Functional Job | Rejects solutions, features, and outcomes. Marks unverified jobs as `candidate`. |
| **`jtbd-job-mapper`** | Core Functional Job + Job Executor | Universal Job Map (8 categories) | Labels unverified steps as `hypothesis`/`domain_rationale`. Leaves unsupported stages as `unknown`. |
| **`jtbd-outcome-engineer`** | Core Job + Job Executor + Single `job_map_step` | Formulaic Desired Outcomes | Bans abstract "error" targets and quality buzzwords. Binds metrics to specific step. |
| **`jtbd-opportunity-calculator`** | Structured survey metadata ($1\_10$) + Numerical ratings | Quantitative Opportunity Scores | **Script-driven**. Rejects missing numbers; never invents ratings from qualitative text. |
| **`jtbd-growth-strategist`** | Opportunity results + segment + price/cost/performance evidence | Growth Strategy Assessment | **Stops at `insufficient_evidence`** if price/cost/performance data is missing. Never forces a strategy. |

---

## 🛡️ Evidence & Confidence Hierarchy

Every data object passed across skills MUST explicitly disclose its confidence level:

1. **`direct_evidence`**: Supported by an explicit customer quote or transcript (with `source_id`).
2. **`domain_rationale`**: Inferred from logical domain necessity. Must be marked `status: hypothesis`.
3. **`statistically_adequate`**: Quantitative survey sample size $N \ge 100$. (Note: $N \ge 100$ is a sample-size heuristic, not a proof of statistical representativeness).
4. **`exploratory`**: Quantitative survey sample size $N < 100$. Output scores must be flagged as exploratory hypotheses.

---

## 🛑 Hard Stopping Rules

The architecture enforces strict stopping boundaries to prevent AI hallucination and premature strategic conclusions:

1. **Missing Job Executor**: `jtbd-job-definer` & `jtbd-job-mapper` return `insufficient_input` if the job executor is unknown.
2. **Missing Numerical Ratings**: `jtbd-opportunity-calculator` returns `calculation_status: blocked` if ratings are missing; it refuses to convert qualitative text into numeric ratings.
3. **Missing Market Evidence**: `jtbd-growth-strategist` returns `status: insufficient_evidence` if price, performance, or cost evidence for a candidate strategy is absent, even if Opportunity Scores are high ($Opp \ge 15.0$).
