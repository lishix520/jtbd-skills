# JTBD Four Forces Analysis Rules & Guidelines

## Purpose

The **Four Forces Analyzer** organizes qualitative switching evidence into Bob Moesta & Bob Becker's Four Forces of Progress framework (further popularized by Bob Moesta and Alan Klement in JTBD literature).

It models the tension between staying with a status quo and adopting a prospective alternative.

---

## Core Distinctions & Classification Rules

### 1. Push vs. Generic Dissatisfaction
- ❌ **Generic Dissatisfaction (Not Push)**: "Spreadsheets are annoying."
  * *Rule*: Dislike without performance failure, missed deadlines, or risk does NOT constitute Push. Stop with `insufficient_switching_context` if no pressure to change exists.
- ✅ **Sufficient Push**: "I spend two hours each week combining spreadsheets manually. Now that the team has doubled, I miss review deadlines."
  * *Statement*: "Team scaling causes manual spreadsheet consolidation to miss review deadlines."

---

### 2. Pull vs. Feature Requests vs. Vendor Claims
- ❌ **Feature Request (Not Pull)**: "Please add a Jira button that creates a weekly report."
  * *Rule*: Feature requests express a solution preference, not evidence of an attractive prospective alternative. Record under `feature_requests` in `jtbd-context-explorer`; do NOT classify as Pull without evidence of desired progress.
- ⚠️ **Vendor Claim (`unverified_claim`)**: "Our dashboard cuts reporting time by 80%."
  * *Rule*: Product claims made by vendors represent prospective benefits, but must be tagged `status: unverified_claim` until verified by customer evidence.
- ✅ **Customer Pull**: "If a reporting service could automatically combine team updates, I would stop doing manual copy-paste."

---

### 3. Habit vs. Anxiety
- **Habit (Inertia of Status Quo)**: Existing routines, team familiarity, embedded workflows, or organizational muscle memory.
  * *Example*: "Everyone knows the spreadsheet template, so changing it would disrupt our weekly team routine."
- **Anxiety (Uncertainty of New Solution)**: Concern about switching, data loss, learning curve, audit failure, or compliance risks.
  * *Example*: "I worry a new reporting tool could lose our history or fail the internal audit."

---

### 4. Big Hire vs. Little Hire Signals
- **Big Hire Signal**: Evidence regarding the initial decision to buy, subscribe to, adopt, or switch to a new solution (e.g., getting budget approval, finishing a trial, signing a contract).
- **Little Hire Signal**: Evidence regarding repeated use, onboarding milestones, feature adoption, repurchase, or renewal after adoption.

---

## Non-Numerical Discipline

- 🚫 **Forbidden Formula**: Never calculate $Push + Pull > Habit + Anxiety$ or output a numerical purchase probability.
- **Switching Readiness**: Formulate as a qualitative hypothesis (`hypothesis_available`) ONLY when at least one push or pull signal AND one habit or anxiety signal are supported by source evidence. Otherwise, return `status: insufficient_evidence`.
