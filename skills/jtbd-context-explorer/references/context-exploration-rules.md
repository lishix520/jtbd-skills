# JTBD Context Exploration Rules & Guidelines

## Purpose

The **Context Explorer** investigates the qualitative circumstance and progress signals surrounding a customer's situation (Christensen's JTBD framework).

It extracts evidence about *why* and *under what conditions* a person seeks to make progress, without prematurely formulating a solution-free Core Functional Job or generating quantitative outcome metrics.

---

## Core Distinctions & Rules

### 1. Feature Requests vs. Current Approaches / Jobs
- **Feature Requests**: A statement proposing a specific product capability, interface element, or tool (e.g., "Build a Jira button that auto-generates reports").
  * **Rule**: Record under `feature_requests`. Do NOT log under `current_approaches` or `competing_alternatives` unless independent source material proves the product is already being used or actively evaluated. Do NOT treat a feature request as a validated Core Functional Job.

---

### 2. Direct vs. Imferred Desired Progress
- **Direct Evidence**: Explicit customer statements of intent or desire (e.g., "I want to finish status reporting before Friday").
- **Inferred Progress**: Strongly implied progress extracted from circumstances or complaints.
  * **Rule**: Strongly implied desired progress is ALWAYS `status: inferred`, even when the supporting source excerpt is direct evidence.

---

### 3. Non-Consumption vs. Dissatisfaction vs. Do Nothing
- ❌ **Dissatisfaction (Not Non-Consumption)**: "I dislike updating spreadsheets." -> Log as `current_approaches` (`spreadsheets`), NOT non-consumption.
- ❌ **Do Nothing / Low Perceived Value (Requires classification discipline)**: "I know there are reporting tools, but the weekly update is not important enough for me to change anything."
  * `current_approaches`: "Do nothing"
  * `competing_alternatives`: "Reporting tools"
  * **Rule**: Do not classify "do nothing" as non-consumption from a single statement alone. Record the behavior and the available alternative, then investigate whether low perceived value, switching effort, habit, risk, or lack of access prevents adoption. Log an `evidence_gap`.
- ✅ **Sufficient Non-Consumption**: "We considered cloud reporting software, but security policy prohibits cloud tools, so we keep using spreadsheets."
  * `non_consumption`: "Cloud reporting software"
  * `barrier_type`: `policy_or_regulation` (or `security_or_privacy`)
  * `constraints`: "Policy prohibits cloud tools"
  * `current_approaches`: "Spreadsheets"

---

### 4. Emotional vs. Social Signals
Keep psychological internal feelings distinct from external social perceptions:

- **Emotional Signal**: Internal psychological feeling (e.g., anxiety, confidence, frustration, peace of mind).
  * *Example*: "I feel anxious before presenting an update to leadership."
- **Social Signal**: Desired or avoided perception by others (e.g., colleagues, executives, clients, peers).
  * *Example*: "I do not want executives to think I have lost control of the project."
  * *Audience*: "Executives"

---

## Top-Level Constraints Schema

Extract top-level organizational, security, regulatory, environmental, time, or money restrictions into `constraints`:

- **Type Classifications**: `policy_or_regulation`, `security_or_privacy`, `environment`, `access`, `skill`, `time`, `money`, `compatibility`, `privacy`, `safety`, `organizational`, `unknown`.
