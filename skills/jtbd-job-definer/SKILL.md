---
name: jtbd-job-definer
description: Define, rewrite, or audit a Jobs-to-be-Done Core Functional Job from customer research, product descriptions, feedback, or candidate job statements. Use when asked to identify a customer's core functional job, separate a job from a solution or outcome, validate a JTBD job statement, or rewrite a feature-oriented request as a solution-free functional job.
---

# JTBD Core Functional Job Definer

Define the stable functional progress the job executor is trying to make.
Do not define a product, feature, purchase decision, emotional outcome, social outcome,
performance metric, or implementation method.

## Scope

Produce one Core Functional Job hypothesis at a time.

Use this skill to:
- Extract a candidate core functional job from supplied evidence
- Audit whether a candidate statement is a valid core functional job
- Rewrite an invalid statement into a candidate job statement
- Identify missing evidence that prevents a confident definition

Do not:
- Infer market size, opportunity, satisfaction, or customer segments
- Create a job map or desired outcomes
- Treat a proposed product or feature as the job
- Present an inference as a verified customer fact

## Required distinctions

Classify each relevant statement before defining the job:

| Type | Definition |
|---|---|
| Core functional job | The functional progress the job executor seeks, independent of a solution |
| Solution | A product, feature, technology, channel, brand, or implementation |
| Desired outcome | A measurable success criterion, such as less time, lower likelihood, or reduced effort |
| Emotional job | How the executor wants to feel |
| Social job | How the executor wants to be perceived |
| Context | A circumstance that disambiguates the job without prescribing a solution |
| Evidence gap | Information required to define the job reliably |

## Definition rules

A valid Core Functional Job:

1. Uses the job executor's perspective.
2. States a functional objective using `Verb + Object`.
3. May include a contextual clarifier only when it distinguishes this job from another.
4. Is solution-free: exclude products, features, brands, channels, technologies, and implementation methods.
5. Is outcome-free: exclude speed, cost, accuracy, safety, ease, quality, and other performance criteria.
6. Is emotionally and socially neutral.
7. Is neither so broad that it contains multiple independent jobs nor so narrow that it describes one workflow step or one product use.
8. Describes the job being done, not the vendor's internal activity, buying process, or a proposed intervention.

## Procedure

1. Identify the likely job executor. If unknown, state it as an evidence gap.
2. Extract direct evidence, preserving quotations or source references where available.
3. Label supplied statements using the required distinctions.
4. Identify candidate functional verbs and objects.
5. Draft one solution-free Core Functional Job statement.
6. Run the validation checklist.
7. If the evidence supports multiple independent jobs, return separate hypotheses; do not merge them.
8. If evidence is insufficient, return no definitive job. State the smallest missing fact needed.

## Validation checklist

Reject or rewrite a candidate if it:
- Names a product, feature, technology, platform, supplier, or channel
- Includes a performance outcome such as quickly, safely, accurately, cheaply, easily, or reliably
- Includes emotional or social language such as confidently, professionally, or without embarrassment
- Describes a purchase, adoption, installation, configuration, maintenance, or disposal activity rather than the core functional objective
- Contains multiple independent verbs or objectives that should be separate jobs
- Is merely a single step within a larger job
- Cannot be attributed to a specific job executor

## Output format

Return this structure:

```yaml
job_executor:
  value: ""
  status: confirmed | inferred | unknown

core_functional_job:
  statement: ""
  status: candidate | validated_from_evidence | insufficient_evidence
  rationale: ""

classification:
  solution_or_feature: []
  desired_outcomes: []
  emotional_jobs: []
  social_jobs: []
  context: []

evidence:
  direct: []
  inferred: []
  contradictions: []

quality_check:
  customer_perspective: pass | fail | unknown
  functional_only: pass | fail | unknown
  solution_free: pass | fail | unknown
  outcome_free: pass | fail | unknown
  appropriately_scoped: pass | fail | unknown

missing_evidence: []
next_research_question: ""
```

## Examples

Read `references/job-statement-rules.md` before resolving ambiguous cases.
Read `examples/valid-examples.md` and `examples/invalid-examples.md` when asked to audit or rewrite a statement.
