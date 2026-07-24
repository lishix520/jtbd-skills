---
name: jtbd-forces-analyzer
description: Analyze Jobs-to-be-Done switching forces from interview excerpts, customer feedback, or structured context-explorer output. Use when asked to identify Push of the current situation, Pull of a prospective alternative, Habit of the current approach, Anxiety about switching, Big Hire or Little Hire signals, and evidence gaps in a possible customer switch. Do not use to define a Core Functional Job, predict purchase probability, score switching readiness, calculate opportunity, or recommend product strategy.
---

# JTBD Four Forces Analyzer

Organize evidence about a possible change from a current approach to a new approach using the Four Forces framework:

- **Push**: Dissatisfaction, friction, risk, or pressure in the current situation.
- **Pull**: An attractive promised progress, benefit, or attribute of a prospective alternative.
- **Habit**: Familiarity, routines, switching inertia, or embedded dependencies supporting the current approach.
- **Anxiety**: Uncertainty, perceived risk, effort, cost, or concern about adopting a prospective alternative.

The Four Forces are a qualitative evidence framework, not a scoring model or a purchase-probability calculator.

## Required Input

Accept either:
- Source excerpts from interviews, reviews, feedback, or support material; or
- A structured output from `jtbd-context-explorer`, including source excerpts.

The input must establish, or explicitly leave unknown:
- A job executor or decision actor
- A current approach, behavior, or status quo
- A possible alternative, proposed change, or prospective new approach

If source material is absent, return `analysis_status: insufficient_input`.
If no current approach or prospective alternative is established, return `analysis_status: insufficient_switching_context`; do not invent one.

## Analysis Status Discipline

- **`analysis_status: evidence_extracted`**: A valid switching context exists (both current approach and prospective alternative are established) AND at least one supported item is extracted from either the Four Forces or hire signals.
- **`analysis_status: insufficient_switching_context`**: Material fails to establish either a current approach or a prospective alternative.
- **`analysis_status: insufficient_input`**: No source material is provided.

## Scope

Extract and classify evidence for:

- **`push`**: Pressure or dissatisfaction making the current approach less acceptable.
- **`pull`**: An explicitly stated or evidenced attractive property of a possible alternative; do not infer pull from the mere existence of a feature request.
- **`habit`**: Routine, familiarity, integration, learned behavior, or dependency maintaining the status quo.
- **`anxiety`**: Concern about uncertainty, migration, reliability, learning, privacy, cost, approval, or operational risk of changing approaches.
- **`big_hire_signal`**: Evidence about deciding to adopt, buy, switch to, or first use a new approach.
- **`little_hire_signal`**: Evidence about continued use, repurchase, renewal, or repeated selection after adoption.
- **`switching_context`**: The current approach, prospective alternative, actor, and circumstance framing a possible switch.

## Evidence Rules

1. Preserve direct evidence as source-linked excerpts.
2. Label interpretations as `inferred`; do not upgrade them to direct facts.
3. Do not create a pull merely because a requested feature exists.
4. Do not classify generic dislike as push unless it creates pressure to change.
5. Do not classify an existing workflow as habit unless the material indicates familiarity, inertia, embeddedness, or a reason it persists.
6. Do not classify general fear as anxiety unless it concerns a prospective switch or alternative.
7. Keep vendor product claims separate from customer evidence; label unsupported claims as `unverified_claim`.
8. Do not add, total, weight, or compare forces numerically (e.g., do not calculate Push + Pull > Habit + Anxiety).
9. A switching-readiness statement must remain a hypothesis and must identify supporting and missing evidence.
10. Big Hire and Little Hire are signals, not mandatory stages; mark them `unknown` when evidence is absent.

## Procedure

1. Validate that the material establishes a current approach and possible alternative; otherwise stop with `analysis_status: insufficient_switching_context`.
2. Identify the actor making or influencing the possible switch.
3. Extract source-linked evidence for each force (`push`, `pull`, `habit`, `anxiety`).
4. Separate direct evidence, inference, vendor claims, and unknowns.
5. Identify Big Hire and Little Hire signals only where the material supports them.
6. Record contradictions, including evidence that favors retaining the status quo.
7. Produce an optional switching-readiness hypothesis only when at least one push or pull signal and one habit or anxiety signal are evidenced.
8. State research questions that would most reduce switching uncertainty.

## Output Format

```yaml
analysis_status: evidence_extracted | insufficient_input | insufficient_switching_context

switching_context:
  actor:
    value: ""
    status: direct_evidence | inferred | unknown
  circumstance:
    statement: ""
    status: direct_evidence | inferred | unknown
    evidence: []
  current_approach:
    statement: ""
    status: direct_evidence | inferred | unknown
    evidence: []
  prospective_alternative:
    statement: ""
    status: direct_evidence | inferred | unknown
    evidence: []

forces:
  push:
    - id: ""
      statement: ""
      status: direct_evidence | inferred
      evidence: []
      assumptions: []
  pull:
    - id: ""
      statement: ""
      status: direct_evidence | inferred | unverified_claim
      evidence: []
      assumptions: []
  habit:
    - id: ""
      statement: ""
      status: direct_evidence | inferred
      evidence: []
      assumptions: []
  anxiety:
    - id: ""
      statement: ""
      status: direct_evidence | inferred
      evidence: []
      assumptions: []

hire_signals:
  big_hire:
    status: present | unknown
    signals: []
  little_hire:
    status: present | unknown
    signals: []

switching_readiness:
  status: hypothesis_available | insufficient_evidence
  statement: ""
  supporting_force_ids: []
  missing_evidence: []

contradictions: []
evidence_gaps: []
next_research_question: ""
```

## Reference

Read `references/four-forces-rules.md` before:
- Distinguishing Push from Habit or generic dissatisfaction
- Distinguishing Pull from a product feature request or vendor claim
- Distinguishing Anxiety from general emotional discomfort
- Identifying Big Hire versus Little Hire signals
- Writing a switching-readiness hypothesis
