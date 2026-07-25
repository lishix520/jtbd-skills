---
name: opportunity-discovery
description: Top-level evidence-aware orchestrator and router for product discovery. Classifies user input (product ideas, feedback, interview notes, or survey data), evaluates evidence readiness, routes to downstream skills, and outputs a Decision Brief detailing what can be concluded, what is only a hypothesis, and the smallest next validation step. Use as the primary entry point when given a new product idea, customer quote, or discovery material and asked what to validate next.
---

# Opportunity Discovery & Decision Brief Generator

**Determine what you can and cannot conclude before building or investing, and get the smallest next validation step.**

---

## Use this when
- You have a new product idea, feature suggestion, customer quote, interview transcript, or survey dataset and want an evidence-aware decision brief.
- You don't know which specific downstream JTBD skill (`switch-interview`, `context-explorer`, `forces-analyzer`, `job-definer`, `opportunity-calculator`, `growth-strategist`) to start with.
- You want to avoid spending time or money building an idea before verifying whether real customer evidence exists.

## Don't use this when
- You already know you need a specific downstream skill (e.g., you explicitly want an 8-stage job map -> use `jtbd-job-mapper`).
- You want an AI to make a speculative binary investment prediction ("Build it" or "Don't build it") without customer data.

## Minimum input
- **Minimum Input**: Any text input—from a raw 1-sentence product idea ("I want to build an AI diary app") to a full interview transcript or quantitative survey file. Supports 6 input modes:
  1. **`idea_only`**: Raw product/feature idea with zero customer facts.
  2. **`customer_signal`**: Raw customer quotes, support tickets, reviews, or sales feedback.
  3. **`research_evidence`**: Interview transcripts or structured research notes.
  4. **`ready_for_outcome_ranking`**: Outcome survey ratings (1-10).
  5. **`ready_for_strategy_assessment`**: Ranked outcomes + segment + price/cost/performance data.
  6. **`partial_market_evidence`**: Price/cost materials without outcome survey ratings.

## What you get
1. **Decision Brief**: A clear 5-part summary of current readiness stage, direct evidence vs hypotheses, what can and cannot be concluded, and the recommended action.
2. **Smallest Next Validation Step**: A concrete, actionable research task (e.g., "Interview 5 target users who faced this problem in the last 30 days").
3. **Skill Routing Recommendation**: Identification of the exact downstream skill to execute next.

## Quick prompt
> *"I have this product idea/feedback: '[Paste idea or quote]'. Evaluate evidence readiness, tell me what I can conclude, and give me the smallest next validation step."*

## What to do next
- Output recommends an interview? Run **`jtbd-switch-interview`**.
- Output recommends context extraction? Run **`jtbd-context-explorer`**.
- Output recommends analyzing switching inertia? Run **`jtbd-forces-analyzer`**.
- Output recommends calculating scores? Run **`jtbd-opportunity-calculator`**.

---

## 🚦 Input Classification & Routing Matrix

| Input Tier | Source Characteristics | System Assessment & Readiness Stage | Downstream Skill Routing |
| :--- | :--- | :--- | :--- |
| **`idea_only`** | Solution idea or feature proposal; no customer facts. | `idea_only` (Do not build yet; validate problem existence). | **`jtbd-switch-interview`** (Formulate interview questions for target users). |
| **`customer_signal`** | Reviews, support tickets, complaints, or feature requests. | `anecdotal_signal` (Extract real-world context & workarounds). | **`jtbd-context-explorer`** (Extract context, constraints, and workarounds). |
| **`research_evidence`** | Interview transcripts containing current tool & prospective tool. | `evidence_emerging` (Map customer switching forces or functional jobs). | **`jtbd-forces-analyzer`** or **`jtbd-job-definer`**. |
| **`ready_for_outcome_ranking`** | Structured 1-10 Importance & Satisfaction outcome survey ratings. | `ready_for_outcome_ranking` (Compute opportunity rankings). | **`jtbd-opportunity-calculator`** (Compute mathematical Opportunity Scores). |
| **`ready_for_strategy_assessment`** | Ranked outcomes + target segment + price/cost/performance evidence. | `ready_for_strategy_assessment` (Evaluate growth strategy matrix). | **`jtbd-growth-strategist`** (Evaluate growth strategy prerequisites). |
| **`partial_market_evidence`** | Price, cost, or competitor materials without outcome survey ratings or target segment. | `not_decision_ready` (Cannot conclude strategy; missing survey/segment). | State missing outcome survey & segment evidence; route to **`jtbd-outcome-engineer`**. |

---

## Output Format (Decision Brief)

```markdown
## 📋 Opportunity Decision Brief

### 🚦 Current Assessment
- **Readiness Stage**: [idea_only | anecdotal_signal | evidence_emerging | ready_for_outcome_ranking | ready_for_strategy_assessment | not_decision_ready]
- **Current Assessment**: [Actionable assessment statement, e.g., "Do not start development yet; validate problem frequency and current workarounds."]
- **Confidence Rating**: [low | medium | high] (Evaluated across Traceability, Relevance, Coverage, Consistency, Decision Alignment)

### ✅ What is Known (Direct Evidence)
- [Source-linked customer quote or verified fact]

### 💡 What is Only a Hypothesis
- [Unverified assumption or solution proposal]

### 🔍 What You CAN and CANNOT Conclude Right Now
- **CAN Conclude**: [Explicit valid conclusion based on current data]
- **CANNOT Conclude**: [Explicit boundary warning of unverified aspects]

### 🚀 Recommended Smallest Next Validation Step
"[Concrete, actionable validation task, e.g., 'Interview 5 target users who encountered this situation in the past 30 days.']"

---

### 📊 Structured Decision Brief Metadata

```yaml
decision_brief:
  current_stage: idea_only | anecdotal_signal | evidence_emerging | ready_for_outcome_ranking | ready_for_strategy_assessment | not_decision_ready
  decision_scope: switch_interview | context_exploration | switching_forces | job_definition | outcome_ranking | strategy_assessment | none
  evidence:
    direct: []
    inferred: []
  hypotheses: []
  unknowns: []
  current_assessment: ""
  confidence: low | medium | high
  what_you_can_conclude_now: []
  what_you_cannot_conclude_yet: []
  recommended_action: ""
  smallest_next_validation_step: ""
  recommended_skill: "jtbd-switch-interview | jtbd-context-explorer | jtbd-forces-analyzer | jtbd-job-definer | jtbd-opportunity-calculator | jtbd-growth-strategist"
```
```

---

## Reference

Read `principles/evidence-model.md` before:
- Classifying an input into an evidence tier
- Formulating a `decision_brief`
- Blocking premature strategic or build verdicts when evidence is insufficient
