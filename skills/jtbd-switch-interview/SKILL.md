---
name: jtbd-switch-interview
description: Interactive interview guide and question generator for understanding why customers change behaviors, buy products, or switch solutions. Use when asked to design a customer interview, formulate non-leading follow-up questions, reconstruct a decision timeline, or avoid leading feature questions during customer discovery. Do not use to define a Core Functional Job, calculate opportunity scores, or recommend product strategy.
---

# JTBD Switch Interview Guide

**Turn customer feedback into a discovery conversation that uncovers real reasons for buying, switching, or churning.**

---

## Use this when
- You have a customer quote, review, feedback fragment, or sales note and need to know what to ask next.
- You are planning a customer discovery interview and want to avoid asking leading questions.
- You want to uncover why a customer switched solutions, bought a competitor, or hesitated to sign up.

## Don't use this when
- You need to map a complete 8-stage functional workflow (use `jtbd-job-mapper`).
- You have quantitative survey rating data and need Opportunity Scores (use `jtbd-opportunity-calculator`).
- You need to audit strategic pricing or growth positioning (use `jtbd-growth-strategist`).

## Minimum input
- **Minimum Input**: A single customer quote, a feedback statement, an interview transcript fragment, or a target customer behavior you want to investigate. (Can also run with zero input to generate an initial interview plan).

## What you get
1. **One primary non-leading question** to speak out loud.
2. **Why it matters** in 2 simple sentences.
3. **A follow-up probe** if the customer's answer is vague.
4. **⚠️ What NOT to ask right now** (avoiding feature traps and speculative questions).
5. **📌 Current Understanding Summary** (What is Known, What is Assumed, What is Missing).
6. **Structured Metadata** for downstream methodology agents.

## Quick prompt
> *"Help me choose the next interview question for this customer quote: '[Paste customer statement here]'."*

## What to do next
- Have customer notes/transcripts? Pass them to **`jtbd-context-explorer`** to extract structured circumstances and constraints.
- Want to analyze switching inertia vs push forces? Pass excerpts to **`jtbd-forces-analyzer`**.

---

## Scope & Three Interactive Modes

### 1. Starting Mode (No Input Provided)
- Identify target interviewee persona criteria.
- Formulate the first neutral, event-based opening question.

### 2. Single Quote Mode (Fragment / Feedback Input)
- Identify which phase of the decision timeline is missing (`first_thought`, `passive_looking`, `active_looking`, `decision`, `first_use`, `ongoing_use`).
- Output **1 Main Question**, **1 Follow-up Probe**, **1 Forbidden Question (What NOT to Ask)**, and a **Known / Assumed / Missing Summary**.

### 3. Transcript Mode (Partial Transcript Input)
- Extract a chronological timeline summary.
- Identify unverified hypotheses and major evidence gaps.
- Output the single most critical next question for the subsequent interview round.

---

## Core Interviewing Discipline

1. **Ask About Past Behavior, Not Future Speculation**: Ask "When was the last time you..." rather than "Would you buy...".
2. **One Question at a Time**: Never overload the interviewer with long lists of questions. Output exactly ONE primary question.
3. **Never Lead With Solution Features**: If a customer mentions a feature request (e.g., "I want a Jira button"), redirect to the triggering event and current approach.
4. **Isolate Specific Events**: Focus on concrete, anchored moments in time (who was there, what happened, when it failed).
5. **Human-First Conversational Output**: Always render a clean, human-readable interview guide first, followed by structured metadata for downstream agents.

---

## Default Output Format (Human-First UX)

```markdown
## 💬 What to Ask Next

"[Primary non-leading question to speak out loud]"

### Why This Question Matters
[Brief 2-sentence explanation of what timeline gap or hypothesis this question investigates.]

### If the Answer Is Vague
"[Concrete follow-up probe asking for specific past details or events]"

### ⚠️ What NOT to Ask Right Now
"[Explicit warning against a specific leading question, feature discussion, or speculative query]"

### 📌 Current Understanding Summary
- **What is Known**: [Direct evidence extracted from input]
- **What is Assumed**: [Interpretation or logical hypothesis]
- **What is Missing**: [Key evidence gap to investigate next]

---

### 📊 Structured Metadata (Agent Mode)

```yaml
analysis_status: plan_generated | evidence_extracted | insufficient_input

interview_focus: first_thought | passive_looking | active_looking | decision | first_use | ongoing_use | unknown

timeline_summary:
  first_thought: ""
  passive_looking: ""
  active_looking: ""
  decision: ""
  first_use: ""
  ongoing_use: ""

current_hypotheses:
  - id: "HYP-001"
    statement: ""
    status: unverified

evidence_gaps:
  - ""

next_question_type: event_anchor | push_trigger | current_workaround | alternative_evaluation | anxiety_probe | outcome_clarification
```
```

---

## Reference

Read `references/switch-interview-rules.md` before:
- Redirecting a feature request into a timeline event
- Formulating non-leading timeline questions
- Identifying the 6 phases of the decision timeline
- Distinguishing behavioral evidence from customer speculation
