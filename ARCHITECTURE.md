# JTBD Skills Suite Architecture & Pipeline Contracts

This document details the architectural design, dual methodological pipelines, evidence discipline, and contract boundaries across the 7 atomic skills in the **JTBD Skills Suite**.

---

## 🏗️ Dual Methodological Pipelines Overview

The repository supports two distinct, complementary Jobs-to-be-Done methodological pipelines:

```text
                             [ Raw Customer Research Materials ]
                                    │               │
            ┌───────────────────────┘               └───────────────────────┐
            ▼                                                               ▼
   【 Christensen Qualitative Path 】                               【 Ulwick Quantitative ODI Path 】
            │                                                               │
   6. jtbd-context-explorer                                         1. jtbd-job-definer
     (Circumstance, Progress,                                         (Solution-Free Core Functional Job)
      Non-Consumption, Feature Requests)                                    │
            │                                                               ▼
            ▼                                                       2. jtbd-job-mapper
   7. jtbd-forces-analyzer                                            (Universal Job Map & Flow Edges)
     (Push, Pull, Habit, Anxiety,                                           │
      Big Hire / Little Hire Signals)                                        ▼
                                                                    3. jtbd-outcome-engineer
                                                                      (Formulaic Desired Outcomes)
                                                                            │
                                                                            ▼
                                                                    4. jtbd-opportunity-calculator
                                                                      (Opportunity Scores & Script)
                                                                            │
                                                                            ▼
                                                                    5. jtbd-growth-strategist
                                                                      (Evidence-Aligned Strategy Matrix)
```

---

## 📋 Skill Input/Output Contracts & Evidence Boundaries

| Skill Name | Pipeline | Expected Input Contract | Output Contract | Evidence Discipline & Stopping Rule |
| :--- | :--- | :--- | :--- | :--- |
| **`jtbd-job-definer`** | Ulwick ODI | Customer research quotes or candidate statements | Solution-free Core Functional Job | Rejects solutions, features, and outcomes. Marks unverified jobs as `candidate`. |
| **`jtbd-job-mapper`** | Ulwick ODI | Core Functional Job + Job Executor | Universal Job Map (8 categories) | Labels unverified steps as `hypothesis`/`domain_rationale`. Leaves unsupported stages as `unknown`. |
| **`jtbd-outcome-engineer`** | Ulwick ODI | Core Job + Job Executor + Single `job_map_step` | Formulaic Desired Outcomes | Bans abstract "error" targets and quality buzzwords. Binds metrics to specific step. |
| **`jtbd-opportunity-calculator`** | Ulwick ODI | Structured survey metadata ($1\_10$) + Numerical ratings | Quantitative Opportunity Scores | **Script-driven**. Rejects missing numbers; never invents ratings from qualitative text. |
| **`jtbd-growth-strategist`** | Ulwick ODI | Opportunity results + segment + price/cost/performance evidence | Growth Strategy Assessment | **Stops at `insufficient_evidence`** if price/cost/performance data is missing. Never forces a strategy. |
| **`jtbd-context-explorer`** | Christensen | Interview excerpts, reviews, support tickets, or feedback | Qualitative Context & Progress | Separates feature requests, policy constraints, and emotional/social signals. Never defines Core Job. |
| **`jtbd-forces-analyzer`** | Christensen | Context explorer output or switching interview excerpts | Four Forces (Push, Pull, Habit, Anxiety) | **Qualitative hypothesis only**. Never calculates purchase probability or numerical force formulas. |

---

## 🛡️ Evidence & Confidence Hierarchy

Every data object passed across skills MUST explicitly disclose its confidence level:

1. **`direct_evidence`**: Supported by an explicit customer quote or transcript (with `source_id`).
2. **`domain_rationale`**: Inferred from logical domain necessity. Must be marked `status: hypothesis` or `status: inferred`.
3. **`unverified_claim`**: Prospective product capability claim made by vendors; requires customer verification.
4. **`statistically_adequate`**: Quantitative survey sample size $N \ge 100$. ($N \ge 100$ is a sample-size heuristic, not a proof of statistical representativeness).
5. **`exploratory`**: Quantitative survey sample size $N < 100$. Output scores must be flagged as exploratory hypotheses.

---

## 🛑 Hard Stopping Rules

The architecture enforces strict stopping boundaries to prevent AI hallucination and premature strategic conclusions:

1. **Missing Job Executor**: `jtbd-job-definer` & `jtbd-job-mapper` return `insufficient_input` if the job executor is unknown.
2. **Missing Numerical Ratings**: `jtbd-opportunity-calculator` returns `calculation_status: blocked` if ratings are missing; it refuses to convert qualitative text into numeric ratings.
3. **Missing Market Evidence**: `jtbd-growth-strategist` returns `status: insufficient_evidence` if price, performance, or cost evidence for a candidate strategy is absent.
4. **Missing Switching Context**: `jtbd-forces-analyzer` returns `analysis_status: insufficient_switching_context` if a current approach or prospective alternative cannot be established.
