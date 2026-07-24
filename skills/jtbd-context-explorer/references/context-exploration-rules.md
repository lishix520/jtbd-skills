# JTBD Context Exploration Rules & Guidelines

## Purpose

The **Context Explorer** investigates the qualitative circumstance and progress signals surrounding a customer's situation (Christensen's JTBD framework).

It extracts evidence about *why* and *under what conditions* a person seeks to make progress, without prematurely formulating a solution-free Core Functional Job or generating quantitative outcome metrics.

---

## Core Distinctions

### 1. Circumstance vs. Functional Job vs. Solution
- **Circumstance (Situation / Trigger / Constraint)**: The background context or pressure.
  * *Example*: "The weekly executive review is tomorrow, and three remote teams have not sent updates."
- **Candidate Functional Progress**: The underlying goal (to be evaluated by `jtbd-job-definer`).
  * *Example*: "Prepare a project status update."
- **Solution (Feature Request / Tool)**: A specific product or implementation.
  * *Example*: "Build a Jira button that auto-generates reports." (MUST be logged under `current_approaches` / `competing_alternatives` or feature requests, NOT as a job).

---

### 2. Non-Consumption Threshold Rules
Do NOT classify general product dissatisfaction as non-consumption.

- ❌ **Insufficient (Dissatisfaction)**: "I dislike updating spreadsheets." -> Log as `current_approaches` (`spreadsheets`), NOT non-consumption.
- ✅ **Sufficient (Non-Consumption)**: "We considered cloud reporting software, but security policy prohibits cloud tools, so we keep using spreadsheets."
  * `non_consumption`: "Cloud reporting software"
  * `barrier_type`: `security_or_privacy` (or `policy_or_regulation`)
  * `current_approaches`: "Spreadsheets"

---

### 3. Emotional vs. Social Signals
Keep psychological internal feelings distinct from external social perceptions:

- **Emotional Signal**: Internal psychological feeling (e.g., anxiety, confidence, frustration, peace of mind).
  * *Example*: "I feel anxious before presenting an update to leadership."
- **Social Signal**: Desired or avoided perception by others (e.g., colleagues, executives, clients, peers).
  * *Example*: "I do not want executives to think I have lost control of the project."
  * *Audience*: "Executives"

---

## Barrier Type Classifications for Non-Consumption

| Barrier Type | Definition & Trigger Excerpt |
| :--- | :--- |
| **`access`** | Physical, network, or permission lockout preventing usage. |
| **`affordability`** | Price exceeds budget or willingness to pay. |
| **`complexity`** | Skill, training, or usability barrier makes usage infeasible. |
| **`suitability`** | Solution does not match the specific physical/operational context. |
| **`availability`** | Solution is not available in the region or platform. |
| **`policy_or_regulation`** | Organizational policy, legal compliance, or government regulation prohibits usage. |
| **`security_or_privacy`** | Security requirements or privacy concerns prevent adoption. |
| **`perceived_value`** | Potential user believes the benefit is not worth the effort of switching. |
| **`unknown`** | Non-consumption is evident, but the specific barrier is unstated. |
