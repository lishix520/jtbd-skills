---
name: jtbd-outcome-engineer
description: Formulate formulaic Desired Outcome Statements for a specific job map step using ODI metrics (time, likelihood, effort, cost, output). Use when given a job map step, qualitative pain point, or survey question and asked to express performance metrics, audit outcome statements, or prepare survey items for quantitative research. Do not use to calculate opportunity scores or recommend product strategy.
---

# JTBD Desired Outcome Engineer

**Turn "users want it faster and easier" into measurable, survey-ready research metrics.**

---

## Use this when
- You have a specific job map step and want to engineer precise performance metric statements.
- You have vague customer complaints ("too slow", "hard to use") and want to rewrite them into formulaic metrics.
- You are preparing an ODI quantitative survey and need standardized outcome statements.

## Don't use this when
- You need to extract switching forces or non-consumption barriers (use `jtbd-context-explorer` or `jtbd-forces-analyzer`).
- You need to calculate mathematical Opportunity Scores from survey ratings (use `jtbd-opportunity-calculator`).
- You need to evaluate market growth strategies (use `jtbd-growth-strategist`).

## Minimum input
- **Minimum Input**: Core Functional Job, Job Executor, and a single `job_map_step` (or a qualitative pain point statement). Supports three modes:
  1. **Step-to-Outcome Mode**: Generate outcomes for a job map step.
  2. **Audit Mode**: Audit an existing survey question for formulaic precision.
  3. **Pain-Point Mode**: Convert a broad complaint into candidate outcome statements.

## What you get
1. **Next Use Handoff**: Qualitative questions for interview probes AND survey-ready questions for quantitative surveys.
2. **Formulaic Desired Outcome Statements**: Statements following `[Direction] + [Metric] + [Target] + [Contextual Clarifier]`.
3. **Metric Classification**: Metric type tag (`time`, `likelihood`, `effort`, `cost`, `output`).

## Quick prompt
> *"Formulate desired outcome metrics for this job step: '[Paste job map step statement]'."*

## What to do next
- Need qualitative interview probes? Use the `next_use.qualitative` questions in **`jtbd-switch-interview`**.
- Ready to collect quantitative data? Export `next_use.quantitative` items into an ODI survey, then pass ratings to **`jtbd-opportunity-calculator`**.

---

## Outcome Statement Formula

Every Desired Outcome Statement MUST follow this exact structure:

$$\text{Desired Outcome} = \text{Direction} + \text{Metric Type} + \text{Measurement Target} + [\text{Contextual Clarifier}]$$

- **Direction**: `Minimize` (or `Maximize` when increasing capacity/yield).
- **Metric Type**: `time` | `likelihood` | `effort` | `cost` | `output`.
- **Measurement Target**: The precise action, event, error, or state being controlled. (Must be concrete and observable; avoid vague words like "error", "failure", "problem").
- **Contextual Clarifier**: Optional phrase specifying environmental or conditional boundaries.

## Output Format

```yaml
next_use:
  qualitative:
    - "Interview probe question for qualitative discovery"
  quantitative:
    - "Survey question item for 1-10 Importance/Satisfaction rating"

job_context:
  core_functional_job: ""
  job_executor: ""
  job_map_step:
    category: define | locate | prepare | confirm | execute | monitor | modify | conclude
    statement: ""

outcomes_status: provisional | validated

desired_outcomes:
  - id: ""
    statement: ""
    direction: minimize | maximize
    metric_type: time | likelihood | effort | cost | output
    measurement_target: ""
    contextual_clarifier: ""
    source_step:
      category: ""
      statement: ""
    status: evidence_supported | hypothesis
    basis: direct_evidence | domain_rationale
    evidence: []
    assumptions: []

excluded_items: []
evidence_gaps: []
next_research_question: ""
```

## Reference

Read `references/outcome-statement-rules.md` before:
- Distinguishing metric types (`time`, `likelihood`, `effort`, `cost`, `output`)
- Enforcing concrete specificity on likelihood targets
- Stripping quality buzzwords ("easily", "reliably", "accurately")
