---
name: jtbd-forces-analyzer
description: Analyze Jobs-to-be-Done switching forces from interview excerpts, customer feedback, or structured context-explorer output. Use when asked to identify Push of the current situation, Pull of a prospective alternative, Habit of the current approach, Anxiety about switching, Big Hire or Little Hire signals, and evidence gaps in a possible customer switch. Do not use to define a Core Functional Job, predict purchase probability, score switching readiness, calculate opportunity, or recommend product strategy.
---

# JTBD Four Forces Analyzer

**Explain why customers want to change, yet still won't buy, switch, or renew.**

---

## Use this when
- You want to understand why prospects dislike their current tool but still hesitate to switch.
- You have customer interview notes or sales feedback containing current workarounds and prospective tools.
- You need to map Push, Pull, Habit, and Anxiety switching forces without making speculative purchase probability claims.

## Don't use this when
- You need to design a customer discovery interview or get immediate next questions (use `jtbd-switch-interview`).
- You need to formulate formulaic desired outcomes or calculate survey opportunity scores (use `jtbd-opportunity-calculator`).
- You need to audit strategic pricing or growth matrix positioning (use `jtbd-growth-strategist`).

## Minimum input
- **Minimum Input**: Raw interview quotes or structured context data containing both a **current approach** (status quo) and a **prospective alternative** (candidate solution). If either is missing, returns `analysis_status: insufficient_switching_context` with specific questions needed to complete the context.

## What you get
1. **Human Summary**: 5 key insights detailing reasons to change (Push), reasons to stay (Habit), reasons to choose you (Pull), reasons to hesitate (Anxiety), and the single most critical thing to validate next.
2. **Four Forces Arrays**: Source-linked excerpts for `push`, `pull`, `habit`, and `anxiety`.
3. **Switching Readiness Hypothesis**: A qualitative assessment (`hypothesis_available | insufficient_evidence`) stating supporting forces and missing evidence. (No numerical formulas or purchase probabilities).

## Quick prompt
> *"Analyze the switching forces (Push, Pull, Habit, Anxiety) from this interview excerpt: '[Paste interview text here]'."*

## What to do next
- Need to validate missing anxiety or friction points? Run **`jtbd-switch-interview`** to get targeted follow-up questions.
- Ready to formalize the customer's functional goal? Pass to **`jtbd-job-definer`**.

---

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

## Output Format

```yaml
human_summary:
  reason_to_change: ""
  reason_to_stay: ""
  reason_to_choose_you: ""
  reason_to_hesitate: ""
  most_important_thing_to_validate_next: ""

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
