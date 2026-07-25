---
name: jtbd-job-mapper
description: Deconstruct a defined Core Functional Job into a chronological Universal Job Map across standard stages (define, locate, prepare, confirm, execute, monitor, modify, conclude). Use when asked to map the steps of a customer job, identify functional dependencies between steps, or uncover missing execution steps in a workflow. Do not use to write desired outcome statements, calculate opportunity scores, or recommend product strategy.
---

# JTBD Job Mapper

**Deconstruct a customer job from start to finish to find where the journey gets stuck.**

---

## Use this when
- You have a defined Core Functional Job and want to break it down into an 8-stage universal execution map.
- You want to identify functional step dependencies, conditional loops, or missing preparation/monitoring steps.
- You want to pinpoint which specific execution stage has the highest uncertainty or friction for research.

## Don't use this when
- You need to extract qualitative switching forces or non-consumption barriers (use `jtbd-context-explorer` or `jtbd-forces-analyzer`).
- You need to write formulaic outcome metrics for a specific step (use `jtbd-outcome-engineer`).
- You have survey ratings and need Opportunity Scores (use `jtbd-opportunity-calculator`).

## Minimum input
- **Minimum Input**: A Core Functional Job statement and Job Executor. Supports two starting points:
  1. **Validated Job**: Maps an accepted Core Functional Job.
  2. **Candidate Job**: Maps a `candidate` job hypothesis, explicitly marking unverified steps as `hypothesis` or `domain_rationale`.

## What you get
1. **Human Summary**: Journey summary in one sentence, likely pain points to test, and unknown steps to validate.
2. **Universal Job Map**: Step statements organized across up to 8 universal stages (`define`, `locate`, `prepare`, `confirm`, `execute`, `monitor`, `modify`, `conclude`).
3. **Flow Dependency Graph**: Functional dependencies (`flow.edges`) between stages.

## Quick prompt
> *"Break down the execution steps for this job statement: '[Paste job statement]'."*

## What to do next
- Select a specific job map step with high friction or uncertainty -> Pass to **`jtbd-outcome-engineer`** to formulate Desired Outcome Statements.

---

## Universal Job Map Stages

1. **Define**: Determine objectives and plan execution.
2. **Locate**: Gather necessary information, inputs, or materials.
3. **Prepare**: Set up the environment, format inputs, or configure tools.
4. **Confirm**: Verify readiness, completeness, or safety before execution.
5. **Execute**: Perform the core functional action of the job.
6. **Monitor**: Track execution progress, status, or environmental changes.
7. **Modify**: Adjust or revise execution when monitoring reveals variance.
8. **Conclude**: Finish, store, hand off, or clean up after execution.

## Output Format

```yaml
human_summary:
  job: ""
  journey_in_one_sentence: ""
  likely_pain_points_to_test: []
  unknown_steps_to_validate: []

job:
  core_functional_job: ""
  status: candidate | accepted
  job_executor:
    value: ""
    status: direct_evidence | inferred | unknown

map_status: provisional | validated

stages:
  - category: define | locate | prepare | confirm | execute | monitor | modify | conclude
    applicability: present | conditional | unknown
    steps:
      - statement: ""
        status: evidence_supported | hypothesis
        basis: direct_evidence | domain_rationale
        evidence: []
        assumptions: []

flow:
  edges:
    - from: ""
      to: ""
      when: ""
  branches: []

excluded_items: []
evidence_gaps: []
next_research_question: ""
```

## Reference

Read `references/universal-job-map-rules.md` before:
- Distinguishing job steps from solution features
- Mapping conditional loops (`monitor` -> `modify` -> `execute`)
- Assigning step basis (`direct_evidence` vs `domain_rationale`)
