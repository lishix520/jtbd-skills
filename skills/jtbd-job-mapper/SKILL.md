---
name: jtbd-job-mapper
description: Build or audit a solution-free Universal Job Map for a defined Core Functional Job. Use when asked to decompose a customer's functional job into Define, Locate, Prepare, Confirm, Execute, Monitor, Modify, and Conclude steps; identify missing, misordered, solution-specific, or vendor-centric job-map steps; or prepare a validated job map for ODI desired-outcome research.
---

# JTBD Universal Job Mapper

Map how a job executor completes an already-defined Core Functional Job.

A job map describes the customer's functional process, not a product workflow,
feature list, purchase journey, vendor process, or current solution.

## Scope

Input must include:
- A Core Functional Job statement
- A job executor, confirmed or explicitly marked as a hypothesis
- Evidence, a domain description, or an explicit request to produce a provisional map

Output:
- A sequence of job steps using the Universal Job Map categories
- Evidence and confidence for each step
- Explicit gaps, alternative paths, and non-applicable stages
- A map suitable as input to `jtbd-outcome-engineer`

Do not:
- Redefine the Core Functional Job
- Add desired outcomes, features, products, technologies, or performance claims
- Treat the current workflow as the ideal job map
- Force all eight stages to contain a step
- Infer missing steps as facts without evidence
- Calculate opportunities or recommend product strategy

## Universal Job Map categories

Use these categories as an organizing framework:

1. Define — determine objectives, constraints, criteria, or plan
2. Locate — identify, gather, access, or obtain required inputs
3. Prepare — arrange, configure, organize, or make inputs ready
4. Confirm — verify readiness, validity, completeness, or appropriateness
5. Execute — perform the central action that advances the job
6. Monitor — observe progress, status, output, or changing conditions
7. Modify — correct, adjust, adapt, or refine when required
8. Conclude — finalize, preserve, communicate, hand off, or close the job

A category may be:
- `present`: supported by direct evidence or an explicitly labeled domain rationale
- `conditional`: occurs only in stated circumstances
- `not_applicable`: genuinely irrelevant to this job
- `unknown`: insufficient evidence; do not invent a step

## Step rules

Every step must:

1. Use the job executor's perspective.
2. State a functional action, not a product feature, channel, technology, vendor activity, or internal company process.
3. Be solution-free and outcome-free.
4. Represent an observable part of completing the core job, not a separate independent job.
5. Be mutually distinguishable from adjacent steps.
6. Be ordered by functional dependency, not necessarily by current product workflow.
7. Be concise: one primary action per step.
8. Preserve loops and branches when evidence requires them; do not force a linear path.

## Procedure

1. Validate that the input Core Functional Job is present and solution-free.
2. Confirm the job executor. If unknown, return `insufficient_input`.
3. Extract direct evidence and label assumptions separately.
4. For each Universal Job Map category, identify supported candidate actions.
5. Mark unsupported categories as `unknown` or `not_applicable`; never fill them merely for completeness.
6. Check that each step advances the specified Core Functional Job.
7. Identify loops, branches, and conditional steps using `flow.edges`.
8. Audit for solution, outcome, vendor, purchase, and lifecycle contamination.
9. Return the map and the smallest next research question needed to resolve the highest-impact uncertainty.

## Validation checklist

Reject, remove, or rewrite any step that:

- Names a brand, product, feature, technology, interface, channel, or implementation
- Includes performance criteria such as fast, accurate, safe, cheap, easy, reliable, or seamless
- Describes the vendor's internal process
- Describes buying, receiving, installing, learning, maintaining, repairing, or disposing of a solution
- Is an emotional or social objective
- Repeats another step without a distinct functional role
- Is a different independent job
- Exists only because the eight-step template demands it

## Output format

```yaml
job:
  core_functional_job: ""
  status: accepted | candidate | rejected
  job_executor:
    value: ""
    status: confirmed | inferred | unknown

map_status: provisional | evidence_supported | insufficient_input

stages:
  - category: define | locate | prepare | confirm | execute | monitor | modify | conclude
    applicability: present | conditional | not_applicable | unknown
    steps:
      - statement: ""
        status: evidence_supported | hypothesis
        basis: direct_evidence | domain_rationale | explicit_request
        evidence: []
        assumptions: []
    notes: ""

flow:
  edges:
    - from: define | locate | prepare | confirm | execute | monitor | modify | conclude
      to: define | locate | prepare | confirm | execute | monitor | modify | conclude
      when: "" # optional condition for loops or branches
  branches: []

excluded_items:
  - statement: ""
    classification: solution | desired_outcome | vendor_activity | lifecycle_activity | emotional_job | social_job | separate_job
    reason: ""

evidence_gaps: []
next_research_question: ""
```

## Reference materials

Read `references/universal-job-map-rules.md` before:
- Mapping a job with ambiguous stage boundaries
- Auditing an existing job map
- Deciding whether a category is conditional or not applicable
- Handling loops, repeated execution, or non-linear workflows

Read `examples/valid-job-maps.md` for expected scope and granularity.
Read `examples/invalid-job-maps.md` when correcting common errors.
