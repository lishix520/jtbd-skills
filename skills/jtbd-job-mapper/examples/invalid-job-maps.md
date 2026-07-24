# Invalid Universal Job Map Examples & Corrections

This document details 4 major **map-level anti-patterns** when constructing Universal Job Maps. Each example illustrates an incorrect map structure, the specific rule violation, and how to correct or re-classify the stages.

---

## Anti-Pattern 1: Product Workflow Mistaken for Job Map

### Core Functional Job
`Prepare a project status update`

### Incorrect Map Attempt
```yaml
stages:
  - category: define
    steps:
      - statement: "Log into Jira account"
  - category: locate
    steps:
      - statement: "Open the sprint dashboard"
  - category: prepare
    steps:
      - statement: "Export data to Notion"
  - category: execute
    steps:
      - statement: "Click 'Share via Slack'"
```

### Rule Violation
- **Solution & Interface Contamination**: Maps specific software products (`Jira`, `Notion`, `Slack`) and UI interaction steps (`Log into`, `Click Share`).
- **User Journey Misalignment**: Describes a current product's user journey rather than a solution-agnostic functional job map.

### Correction Guidelines
- Strip all product names, interfaces, and UI button clicks.
- Re-map each step to its underlying functional action:
  - `Log into Jira account` & `Open sprint dashboard` -> **Locate**: `Identify relevant project status information`
  - `Export data to Notion` -> **Prepare**: `Organize status information`
  - `Click 'Share via Slack'` -> **Conclude**: `Deliver the status update`
- Exclude Jira, Notion, and Slack under `excluded_items` with classification `solution`.

---

## Anti-Pattern 2: Forced Eight-Stage Completion

### Core Functional Job
`Set a kitchen timer`

### Incorrect Map Attempt
```yaml
stages:
  - category: define
    steps:
      - statement: "Determine timer duration"
  - category: locate
    steps:
      - statement: "Locate the kitchen timer on the counter"
  - category: prepare
    steps:
      - statement: "Clean the kitchen timer buttons"
  - category: confirm
    steps:
      - statement: "Verify timer battery level"
  - category: execute
    steps:
      - statement: "Start the countdown"
  - category: monitor
    steps:
      - statement: "Observe the countdown display"
  - category: modify
    steps:
      - statement: "Adjust countdown speed"
  - category: conclude
    steps:
      - statement: "Store timer in drawer"
```

### Rule Violation
- **Inventing Steps Without Evidence**: Hardcoding steps across all 8 stages when evidence only describes determining a duration and starting the timer.
- **Consumption Chain / Fabrication Contamination**: Cleaning buttons and storing timers in drawers are maintenance or storage activities, not core job steps.

### Correction Guidelines
- Unsupported stages must be marked `not_applicable` or `unknown`; do NOT force steps for completeness.
- **Corrected Applicability**:
  - `define`: `present` (`Determine timer duration`)
  - `locate`: `not_applicable`
  - `prepare`: `not_applicable`
  - `confirm`: `not_applicable`
  - `execute`: `present` (`Start the countdown`)
  - `monitor`: `unknown`
  - `modify`: `not_applicable`
  - `conclude`: `present` (`Silence the timer alert`)

---

## Anti-Pattern 3: Compound-Step Map

### Core Functional Job
`Prepare a project status update`

### Incorrect Map Attempt
```yaml
stages:
  - category: execute
    steps:
      - statement: "Gather, organize, validate, and summarize project information"
```

### Rule Violation
- **Compounding Multiple Actions**: Combines 4 distinct functional actions (`Gather`, `Organize`, `Validate`, `Summarize`) spanning 4 separate Universal Job Map categories into a single statement.
- **Prevents Outcome Measurement**: Compound steps make it impossible to attach individual, unambiguous Desired Outcomes in downstream skills (`jtbd-outcome-engineer`).

### Correction Guidelines
- Decompound into single-action steps across their respective categories:
  - **Locate**: `Identify relevant project status information`
  - **Prepare**: `Organize status information`
  - **Confirm**: `Verify the completeness of status information`
  - **Execute**: `Compose the status update`

---

## Anti-Pattern 4: Linear Map Losing Corrective Loop

### Core Functional Job
`Cut wood`

### Incorrect Map Attempt
```yaml
stages:
  - category: execute
    steps:
      - statement: "Sever the wood along the marked path"
  - category: conclude
    steps:
      - statement: "Clear the cut wood"

flow:
  edges:
    - from: execute
      to: conclude
```

### Rule Violation
- **Omission of Corrective Loop**: Ignores the in-flight observation (`monitor`) and adjustment (`modify`) required when execution deviates.
- **Over-Simplification**: Forces a rigid linear flow when the functional reality requires checking, adjusting alignment, and re-executing.

### Correction Guidelines
- Include `monitor` and `modify` stages and model the feedback loop explicitly using `flow.edges`:
  ```yaml
  flow:
    edges:
      - from: execute
        to: monitor
      - from: monitor
        to: modify
        when: "the cut deviates from the intended line"
      - from: modify
        to: execute
        when: "a correction requires another cut"
      - from: monitor
        to: conclude
        when: "the required cut is complete"
  ```
