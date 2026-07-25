---
name: jtbd-job-definer
description: Extract, audit, or rewrite a solution-free and outcome-free Core Functional Job statement from customer quotes or candidate sentences. Use when given a proposed product feature or customer statement and asked to express the underlying functional job, audit a job statement for solution contamination, or determine if enough evidence exists to validate a job statement. Do not use to map job steps, write desired outcomes, calculate opportunity scores, or recommend product strategy.
---

# JTBD Job Definer

**Rewrite "I want this feature" into a solution-free customer job statement.**

---

## Use this when
- A user asks for a specific product feature or button, and you need to uncover the underlying solution-free goal.
- You have a proposed Core Job statement and need to audit it for embedded technologies, products, quality adjectives, or outcome metrics.
- You want to establish a clean Core Functional Job statement before mapping workflow steps.

## Don't use this when
- You want to extract raw circumstances, non-consumption barriers, or feature requests without defining a job (use `jtbd-context-explorer`).
- You need to map the step-by-step execution journey (use `jtbd-job-mapper`).
- You need to engineer quantitative metric statements (use `jtbd-outcome-engineer`).

## Minimum input
- **Minimum Input**: A customer statement, feedback quote, feature request, or candidate job statement. Includes two operating modes:
  1. **Audit Mode**: Provide a job statement -> audits for embedded solutions, features, or outcomes.
  2. **Rewrite Mode**: Provide a feature request or quote -> formulates a candidate solution-free job statement.

## What you get
1. **Plain Language Explanation**: A 3-part summary explaining what the customer is trying to do, what was removed (and why), and what evidence is still missing.
2. **Core Functional Job Statement**: A single solution-free, outcome-free functional statement (`[Verb] + [Object of Control] + [Contextual Clarifier]`).
3. **Quality Check Audit**: Boolean checks verifying customer perspective, solution-free, outcome-free, and appropriate scope.

## Quick prompt
> *"Rewrite this feature request into a solution-free Core Functional Job: '[Paste feature request or quote]'."*

## What to do next
- Core job accepted or candidate defined? Pass to **`jtbd-job-mapper`** to break it down into an 8-stage functional workflow map.

---

## Operating Rules

1. **Solution-Free Rule**: A Core Functional Job MUST NOT mention any technology, product, feature, tool, or vendor name.
2. **Outcome-Free Rule**: A Core Functional Job MUST NOT contain quality adjectives or performance metrics (e.g., "fast", "reliable", "cheap", "easily"). Performance criteria belong in Desired Outcome Statements (`jtbd-outcome-engineer`).
3. **Single Job Focus**: Output exactly ONE Core Functional Job statement per request.
4. **Status Discipline**: Mark unverified inferences as `status: candidate`. Only mark `status: accepted` when direct source evidence proves the job executor's primary functional goal.

## Output Format

```yaml
plain_language:
  customer_is_trying_to: ""
  this_is_not_the_job_because: []
  what_we_still_need_to_know: ""

job:
  statement: ""
  status: candidate | accepted | insufficient_evidence
  executor: ""

evidence:
  direct: []
  inferred: []
  contradictions: []

quality_check:
  customer_perspective: pass | fail
  functional_only: pass | fail
  solution_free: pass | fail
  outcome_free: pass | fail
  appropriately_scoped: pass | fail

missing_evidence: []
next_research_question: ""
```

## Reference

Read `references/job-statement-rules.md` before:
- Stripping embedded technologies or features from candidate statements
- Resolving whether a job is micro-scoped (step) or macro-scoped (life goal)
- Auditing quality buzzwords and performance criteria
