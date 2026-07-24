---
name: jtbd-context-explorer
description: Extract Jobs-to-be-Done context evidence from customer interviews, feedback, reviews, support tickets, or scenario descriptions. Use when asked to identify the circumstances that triggered a change, desired progress, current alternatives or workarounds, non-consumption, emotional or social signals, competing solutions, and unanswered research questions. Do not use to define a Core Functional Job, calculate opportunity scores, or recommend product strategy.
---

# JTBD Context Explorer

Extract and organize evidence about the circumstances in which a person seeks to make progress. Preserve the difference between direct evidence, inference, and unresolved uncertainty.

This skill investigates context around a possible job. It does not define or validate a Core Functional Job, map a workflow, generate desired outcomes, compute market opportunity, or select a strategy.

## Required Input

Accept one or more of:
- Interview excerpts or transcripts
- Customer feedback, reviews, support tickets, or open-text survey responses
- A scenario description with clearly identified source and limitations

If no source material is supplied, return `analysis_status: insufficient_input`.
Do not invent a customer circumstance, motivation, competing alternative, or non-consumption behavior.

## Scope

Extract evidence for:

- **Circumstance**: A concrete situation, trigger, constraint, event, or change that creates pressure to make progress.
- **Desired Progress**: A stated or strongly implied change from a current situation toward a better future situation.
- **Current Approach**: What the person currently does, including a product, manual process, workaround, delay, delegation, avoidance, or doing nothing.
- **Switching Trigger**: A reported event or threshold that made the current approach inadequate.
- **Non-Consumption**: Evidence that the person does not use an available solution because it is inaccessible, unaffordable, too complex, unsuitable, unavailable, prohibited by policy, security-restricted, or not worth adopting.
- **Competing Alternatives**: Solutions, behaviors, workarounds, or "do nothing" approaches used to make progress.
- **Emotional Signal**: Evidence of a desired feeling or avoided feeling.
- **Social Signal**: Evidence about how the person wants to be perceived by another person or group.
- **Constraints**: Time, money, policy, environment, access, skill, compatibility, privacy, safety, or organizational restrictions.

## Evidence Rules

1. Preserve direct statements as excerpts with source IDs.
2. Label every interpretation as `inferred`; never present it as direct fact.
3. Do not infer causal relationships when the source only shows correlation.
4. Do not convert a product feature request into a customer's underlying job.
5. Do not treat a complaint as proof of a broad market pattern.
6. Do not classify something as non-consumption unless the material shows absence, avoidance, inability, or refusal to use a relevant alternative.
7. Treat emotional and social language as separate signals, not as Core Functional Jobs or ODI desired outcomes.
8. Record contradictions rather than resolving them through guesswork.
9. Return the smallest next research question that would reduce the most consequential uncertainty.

## Procedure

1. Assign stable source IDs to supplied material.
2. Extract direct excerpts without paraphrasing their evidentiary meaning.
3. Classify each excerpt into one or more evidence categories.
4. Build a circumstance record only when source material identifies a concrete situation, trigger, constraint, or change.
5. Identify current approaches and alternatives, including delay and avoidance.
6. Mark non-consumption only when the required evidence threshold is met.
7. Separate emotional and social signals from functional progress.
8. List contradictions, unsupported hypotheses, and evidence gaps.
9. Produce research questions; do not turn gaps into conclusions.

## Output Format

```yaml
analysis_status: evidence_extracted | insufficient_input

sources:
  - id: ""
    type: interview | review | feedback | support_ticket | scenario
    limitations: []

circumstances:
  - id: ""
    statement: ""
    status: direct_evidence | inferred
    evidence:
      - source_id: ""
        excerpt: ""
    assumptions: []
    constraints: []

desired_progress:
  - id: ""
    statement: ""
    status: direct_evidence | inferred
    evidence: []
    assumptions: []

current_approaches:
  - id: ""
    statement: ""
    type: product | manual_process | workaround | delegation | delay | avoidance | do_nothing | unknown
    status: direct_evidence | inferred
    evidence: []
    assumptions: []

switching_triggers:
  - id: ""
    statement: ""
    status: direct_evidence | inferred
    evidence: []
    assumptions: []

non_consumption:
  - id: ""
    statement: ""
    barrier_type: access | affordability | complexity | suitability | availability | policy_or_regulation | security_or_privacy | perceived_value | unknown
    status: direct_evidence | inferred
    evidence: []
    assumptions: []

competing_alternatives:
  - id: ""
    statement: ""
    type: product | manual_process | workaround | delegation | delay | avoidance | do_nothing | unknown
    status: direct_evidence | inferred
    evidence: []
    assumptions: []

emotional_signals:
  - id: ""
    statement: ""
    status: direct_evidence | inferred
    evidence: []
    assumptions: []

social_signals:
  - id: ""
    statement: ""
    audience: ""
    status: direct_evidence | inferred
    evidence: []
    assumptions: []

contradictions: []
evidence_gaps: []
next_research_question: ""
```

## Reference

Read `references/context-exploration-rules.md` before:
- Deciding whether a phrase proves non-consumption
- Separating a circumstance from a functional job
- Separating an emotional signal from a social signal
- Inferring a switching trigger or competing alternative
- Resolving ambiguous source material
