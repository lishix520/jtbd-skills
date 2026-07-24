---
name: jtbd-outcome-engineer
description: Formulate, audit, or rewrite solution-free Desired Outcome Statements for a specific step in a JTBD Universal Job Map. Use when asked to extract customer performance metrics, remove solution or feature bias from outcome statements, deduplicate outcome metrics, structure customer success criteria for Outcome-Driven Innovation (ODI) research, or prepare desired outcomes for a job-map step.
---

# JTBD Desired Outcome Engineer

Formulate how a job executor measures success when executing a specific step in a Universal Job Map.

A Desired Outcome Statement defines a customer's metric of value and performance. It does not describe a product feature, technology capability, job map step, emotional aspiration, or commercial goal.

## Scope

Input must include:
- A Core Functional Job statement
- A job executor, confirmed or explicitly marked as a hypothesis
- A specific `job_map_step` (Category and Statement)

Output:
- A set of formulaic Desired Outcome Statements linked to the target `job_map_step`
- Evidence, status, and classification for each statement
- Identification of solution-contaminated, outcome-compound, or invalid candidate metrics
- Smallest next research question required for empirical validation

Do not:
- Redefine the Core Functional Job or rewrite the input `job_map_step`
- Generate outcomes without an explicit `job_map_step` input
- Include products, features, technologies, channels, or implementation methods in outcome statements
- Calculate Importance, Satisfaction, or Opportunity Scores
- Design survey rating scales or market segmentation strategy
- Fabricate customer research scores or claim unverified statements are customer-validated facts

## Formulaic Syntax Rules

Every valid Desired Outcome Statement MUST follow this structure:

$$\text{Desired Outcome} = \text{Direction} + \text{Performance Metric} + \text{Object of Control} + [\text{Optional Contextual Clarifier}]$$

1. **Direction**: Must be `Minimize` (preferred for 95%+ of ODI metrics: time, likelihood of error, effort, cost) or `Maximize` (when increasing output/yield without trade-offs).
2. **Performance Metric**: The unit of measurement, usually `the time it takes to...` or `the likelihood of...`.
3. **Object of Control**: The precise physical, digital, or informational entity being controlled or acted upon during the step.
4. **Optional Contextual Clarifier**: Added ONLY to specify the condition under which the outcome is desired.

## Classification Distinctions

Classify each candidate metric before finalizing:

| Type | Definition | Example |
|---|---|---|
| Desired Outcome | A valid solution-free performance metric for the step | *Minimize the likelihood of omitting required status information* |
| Solution / Feature | A product capability, technology, or interface tool | *Fast Jira export button* |
| Compound Outcome | Multiple metrics combined in a single statement | *Minimize time and likelihood of error* |
| Job Map Step | A functional action rather than a performance metric | *Verify completeness of information* |
| Emotional / Social Outcome | Internal psychological feeling or social status | *Maximize feeling of confidence* |
| Business / Vendor Metric | Internal company revenue or operational goal | *Maximize subscription renewals* |

## Procedure

1. Validate that `core_functional_job`, `job_executor`, and `job_map_step` are provided. If missing, return `insufficient_input`.
2. Extract direct customer statements or domain rationale related to the step.
3. Label candidate metrics using the classification distinctions.
4. Filter out solutions, feature requests, compound metrics, and emotional goals.
5. Format valid metrics into formulaic Desired Outcome Statements (`Direction + Metric + Object + Clarifier`).
6. Audit each outcome using the Validation Checklist.
7. Return the structured output with `status: hypothesis` (unless direct research evidence is attached).

## Validation Checklist

Reject, remove, or rewrite any outcome statement that:

- Names a brand, product, software, feature, technology, interface, or channel
- Uses vague buzzwords such as fast, easy, seamless, reliable, convenient, or user-friendly instead of a formulaic metric
- Combines multiple metrics (e.g., combining time AND likelihood in one statement)
- Describes a job step (action) rather than a performance metric (result)
- Describes an emotional state (confidence, pride) or social perception
- Describes vendor profit, sales, or business goals
- Lacks a link to a specific `job_map_step`

## Output Format

```yaml
job_context:
  core_functional_job: ""
  job_executor: ""
  job_map_step:
    category: define | locate | prepare | confirm | execute | monitor | modify | conclude
    statement: ""

outcomes_status: provisional | evidence_supported | insufficient_input

desired_outcomes:
  - statement: ""
    direction: minimize | maximize
    metric_type: time | likelihood | output
    object_of_control: ""
    contextual_clarifier: ""
    status: hypothesis | evidence_supported
    basis: direct_evidence | domain_rationale | explicit_request
    evidence: []
    assumptions: []

excluded_items:
  - statement: ""
    classification: solution | compound_outcome | job_step | emotional_social | vendor_metric
    reason: ""

evidence_gaps: []
next_research_question: ""
```

## Reference Materials

Read `references/outcome-statement-rules.md` before:
- Formatting complex desired outcome statements
- Auditing candidate customer metrics for solution contamination
- Deciding whether to use `time` vs `likelihood`
- Splitting compound outcome statements
