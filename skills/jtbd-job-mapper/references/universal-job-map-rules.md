# Universal Job Map Rules & Stage Boundaries

## Purpose

A Universal Job Map organizes the functional steps a job executor takes to complete a Core Functional Job. It is a functional dependency map, independent of any specific current solution.

It is NOT a user journey map, UI workflow, feature inventory, purchase funnel, service blueprint, or vendor sales process.

---

## Stage Meanings & Functional Questions

The 8 Universal Job Map categories answer specific functional questions:

| Stage | Category | Functional Question |
| :--- | :--- | :--- |
| 1 | **Define** | What must the executor determine, plan, or decide before acting? |
| 2 | **Locate** | What inputs, tools, data, or materials must the executor identify or obtain? |
| 3 | **Prepare** | What must be arranged, configured, or made ready prior to execution? |
| 4 | **Confirm** | What must be verified or checked to ensure readiness or appropriateness? |
| 5 | **Execute** | What action directly performs the core transformation or advances the job? |
| 6 | **Monitor** | What must be observed or tracked during or after execution? |
| 7 | **Modify** | What must be adjusted or corrected when conditions or results deviate? |
| 8 | **Conclude** | What completes, records, hands off, or closes the job? |

---

## Applicability Classifications

Do NOT force all 8 stages to contain steps. Mark each category accurately:

- **`present`**: Supported by direct evidence or an explicitly labeled domain rationale.
- **`conditional`**: Occurs only under specified circumstances or conditions.
- **`not_applicable`**: Genuinely irrelevant to this specific core functional job.
- **`unknown`**: Insufficient evidence to determine whether steps exist; do NOT invent steps.

---

## Functional Flow & Dependency Modeling

Use `flow.edges` to represent functional dependencies, conditions, and loops instead of a rigid linear 8-step list:

- **Forward Dependencies**: e.g., `from: define`, `to: execute`.
- **Conditional Branches**: e.g., `from: monitor`, `to: modify`, `when: "when a deviation is detected"`.
- **Loops & Re-execution**: e.g., `from: modify`, `to: execute`, `when: "when a correction requires another attempt"`.
- **Completion Edge**: e.g., `from: monitor`, `to: conclude`, `when: "when execution is verified complete"`.

---

## Correct Granularity Guidelines

A valid job map step:
- Is more specific than the Core Functional Job itself.
- Is broader than a mouse click, button press, API call, or UI interaction.
- Is distinct enough to have separate, measurable Desired Outcomes.
- Contains only **one primary action** per step statement (e.g., `Identify project status information`, NOT `Gather, organize, and validate project status information`).

---

## Category Boundary Rules

- **Define vs. Locate**: `Define` decides criteria, scope, or plan; `Locate` finds or accesses physical/digital inputs.
- **Locate vs. Prepare**: `Locate` accesses inputs; `Prepare` sets up or arranges them for execution.
- **Prepare vs. Confirm**: `Prepare` arranges inputs; `Confirm` checks their validity or readiness.
- **Confirm vs. Execute**: `Confirm` verifies readiness; `Execute` performs the central action.
- **Execute vs. Monitor**: `Execute` does the action; `Monitor` observes status or output.
- **Monitor vs. Modify**: `Monitor` observes deviations; `Modify` makes adjustments.
- **Modify vs. Conclude**: `Modify` adjusts in-flight work; `Conclude` wraps up and finishes the job.

---

## Anti-Patterns & Excluded Items

| Invalid Map Step | Primary Defect | Reason for Exclusion |
| :--- | :--- | :--- |
| *Open the Jira dashboard* | Solution / Tool | Names a specific brand and software interface. |
| *Quickly verify the data* | Outcome Contaminated | Includes performance metric (`Quickly`). |
| *Make stakeholders confident* | Emotional Objective | Describes emotional state, not functional progress. |
| *Sell the report to executives* | Vendor Activity | Internal commercial activity, not job executor progress. |
| *Buy and install the software* | Lifecycle / Purchase | Purchase decision and setup activity, not core job. |
| *Gather, clean, and analyze data* | Compound Step | Combines 3 distinct actions into one step. |
| *Use AI to summarize findings* | Technology Contaminated | Prescribes AI technology instead of functional action. |
