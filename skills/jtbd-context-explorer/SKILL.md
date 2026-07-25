---
name: jtbd-context-explorer
description: Extract Jobs-to-be-Done context evidence from customer interviews, feedback, reviews, support tickets, or scenario descriptions. Use when asked to identify the circumstances that triggered a change, desired progress, current alternatives or workarounds, non-consumption, emotional or social signals, feature requests, constraints, competing solutions, and unanswered research questions. Do not use to define a Core Functional Job, calculate opportunity scores, or recommend product strategy.
---

# JTBD Context Explorer

**Turn messy customer feedback into "what happened, how they do it now, where they get stuck, and what to ask next."**

---

## Use this when
- You have customer interview transcripts, reviews, support tickets, or feedback notes and need to extract what actually happened.
- You want to separate real-world constraints and workarounds from feature requests.
- You need to identify non-consumption barriers or emotional/social context signals.

## Don't use this when
- You need to define a solution-free Core Functional Job statement (use `jtbd-job-definer`).
- You want to evaluate Push, Pull, Habit, and Anxiety switching tensions (use `jtbd-forces-analyzer`).
- You need quantitative market opportunity scores (use `jtbd-opportunity-calculator`).

## Minimum input
- **Minimum Input**: Raw customer text (interview notes, reviews, support tickets, or feedback quotes). If no source text is supplied, returns `analysis_status: insufficient_input`.

## What you get
1. **Human Summary**: A clear 5-point breakdown of what is happening, current workarounds, biggest constraints, likely problems, and next best questions.
2. **Structured Context Evidence**: Categorized arrays for `circumstances`, `desired_progress`, `current_approaches`, `non_consumption`, `feature_requests`, `constraints`, and `competing_alternatives`.
3. **Unresolved Evidence Gaps**: Key unanswered research questions.

## Quick prompt
> *"Extract the customer context, current workarounds, and key constraints from this feedback: '[Paste feedback here]'."*

## What to do next
- Want to analyze switching tensions? Pass extracted context to **`jtbd-forces-analyzer`**.
- Ready to formalize a solution-free customer goal? Pass to **`jtbd-job-definer`**.

---

## Scope

Extract evidence for:

- **Circumstance**: A concrete situation, trigger, constraint, event, or change that creates pressure to make progress.
- **Desired Progress**: A stated or strongly implied change from a current situation toward a better future situation.
- **Current Approach**: What the person currently does, including a product, manual process, workaround, delay, delegation, avoidance, or doing nothing.
- **Switching Trigger**: A reported event or threshold that made the current approach inadequate.
- **Non-Consumption**: Evidence that the person does not use an available solution because it is inaccessible, unaffordable, too complex, unsuitable, unavailable, prohibited by policy, security-restricted, or not worth adopting.
- **Feature Requests**: Statements proposing specific product capabilities, buttons, or tools.
- **Constraints**: Time, money, policy, environment, access, skill, compatibility, privacy, safety, or organizational restrictions.
- **Competing Alternatives**: Solutions, behaviors, workarounds, or "do nothing" approaches used to make progress.
- **Emotional Signal**: Evidence of a desired feeling or avoided feeling.
- **Social Signal**: Evidence about how the person wants to be perceived by another person or group.

## Evidence Rules

1. Preserve direct statements as excerpts with source IDs.
2. Label every interpretation as `inferred`; never present it as direct fact.
3. Strongly implied desired progress is ALWAYS `status: inferred`. Only explicit customer statements of intent are `direct_evidence`.
4. Do not infer causal relationships when the source only shows correlation.
5. Record proposed solution statements under `feature_requests`; do not convert a feature request into a validated Core Functional Job, current approach, or competing alternative without independent evidence.
6. Do not treat a complaint as proof of a broad market pattern or non-consumption.
7. Do not classify something as non-consumption unless the material shows absence, avoidance, inability, or refusal to use a relevant alternative.
8. Treat emotional and social language as separate signals, not as Core Functional Jobs or ODI desired outcomes.
9. Record contradictions rather than resolving them through guesswork.
10. Return the smallest next research question that would reduce the most consequential uncertainty.

## Output Format

```yaml
human_summary:
  what_is_happening: ""
  current_workaround: ""
  biggest_constraint: ""
  likely_problem_to_verify: ""
  next_best_question: ""

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
    constraint_ids: []

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

feature_requests:
  - id: ""
    statement: ""
    status: direct_evidence | inferred
    evidence: []
    assumptions: []

constraints:
  - id: ""
    statement: ""
    type: time | money | policy_or_regulation | security_or_privacy | environment | access | skill | compatibility | privacy | safety | organizational | unknown
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
- Categorizing proposed solutions into `feature_requests`
- Deciding whether a phrase proves non-consumption vs doing nothing
- Determining whether desired progress is `direct_evidence` or `inferred`
- Separating an emotional signal from a social signal
- Extracting top-level constraints
