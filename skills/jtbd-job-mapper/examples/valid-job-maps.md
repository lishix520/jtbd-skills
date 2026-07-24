# Valid Universal Job Map Examples

> These are illustrative, provisional maps.
> Their steps are hypotheses based on stated domain rationale, not verified
> findings from customer research.

---

## Example 1: Prepare a project status update

- **Core Functional Job**: `Prepare a project status update`
- **Job Executor**: Project Manager
- **Context**: For cross-functional review

```yaml
job:
  core_functional_job: "Prepare a project status update"
  status: accepted
  job_executor:
    value: "Project manager"
    status: confirmed

map_status: provisional

stages:
  - category: define
    applicability: present
    steps:
      - statement: "Determine the reporting scope"
        status: hypothesis
        basis: domain_rationale
        evidence: []
        assumptions: ["Reporting scope is required before identifying relevant information."]

  - category: locate
    applicability: present
    steps:
      - statement: "Identify relevant project status information"
        status: hypothesis
        basis: domain_rationale
        evidence: []
        assumptions: ["Status information must be located across project tracking sources."]

  - category: prepare
    applicability: present
    steps:
      - statement: "Organize status information"
        status: hypothesis
        basis: domain_rationale
        evidence: []
        assumptions: ["Information must be formatted/structured before drafting."]

  - category: confirm
    applicability: present
    steps:
      - statement: "Verify the completeness of status information"
        status: hypothesis
        basis: domain_rationale
        evidence: []
        assumptions: ["Completeness check is required prior to composing final update."]

  - category: execute
    applicability: present
    steps:
      - statement: "Compose the status update"
        status: hypothesis
        basis: domain_rationale
        evidence: []
        assumptions: ["Central action of preparing the status update."]

  - category: monitor
    applicability: conditional
    steps:
      - statement: "Track changes affecting reported project status"
        status: hypothesis
        basis: domain_rationale
        evidence: []
        assumptions: ["Applies when project status is actively changing before delivery."]
    notes: "Occurs while project status may change before delivery."

  - category: modify
    applicability: conditional
    steps:
      - statement: "Revise the status update"
        status: hypothesis
        basis: domain_rationale
        evidence: []
        assumptions: ["Applies when status changes require updating the composed text."]
    notes: "Occurs when new information invalidates current status draft."

  - category: conclude
    applicability: present
    steps:
      - statement: "Deliver the status update"
        status: hypothesis
        basis: domain_rationale
        evidence: []
        assumptions: ["Final step handing off the update to stakeholders."]

flow:
  edges:
    - from: define
      to: locate
    - from: locate
      to: prepare
    - from: prepare
      to: confirm
    - from: confirm
      to: execute
    - from: execute
      to: monitor
      when: "status changes occur before delivery"
    - from: monitor
      to: modify
      when: "status changes require revising the update"
    - from: modify
      to: execute
      when: "re-composing is required"
    - from: execute
      to: conclude
      when: "status update is ready for delivery"
  branches: []

excluded_items:
  - statement: "Open Jira dashboard"
    classification: solution
    reason: "Names a specific software tool and interface."
  - statement: "Quickly format the report"
    classification: desired_outcome
    reason: "Includes performance criterion (Quickly)."

evidence_gaps:
  - "Empirical validation with project managers to verify whether Locate and Prepare steps are performed sequentially or iteratively."
next_research_question: "How do project managers currently verify status completeness across distributed teams?"
```

---

## Example 2: Cut wood

- **Core Functional Job**: `Cut wood`
- **Job Executor**: Carpenter / Tradesperson

```yaml
job:
  core_functional_job: "Cut wood"
  status: accepted
  job_executor:
    value: "Carpenter"
    status: confirmed

map_status: provisional

stages:
  - category: define
    applicability: present
    steps:
      - statement: "Determine the desired dimensions for the cut"
        status: hypothesis
        basis: domain_rationale
        evidence: []
        assumptions: ["Dimensions must be specified prior to marking or cutting."]

  - category: locate
    applicability: present
    steps:
      - statement: "Identify the material to be cut"
        status: hypothesis
        basis: domain_rationale
        evidence: []
        assumptions: ["Wood stock must be selected and accessed."]

  - category: prepare
    applicability: present
    steps:
      - statement: "Mark the cutting line on the material"
        status: hypothesis
        basis: domain_rationale
        evidence: []
        assumptions: ["Material requires physical marking prior to cutting."]
      - statement: "Secure the material for cutting"
        status: hypothesis
        basis: domain_rationale
        evidence: []
        assumptions: ["Material must be stabilized."]

  - category: confirm
    applicability: present
    steps:
      - statement: "Verify alignment of the cutting tool with the marked line"
        status: hypothesis
        basis: domain_rationale
        evidence: []
        assumptions: ["Alignment must be checked prior to executing the cut."]

  - category: execute
    applicability: present
    steps:
      - statement: "Sever the wood along the marked path"
        status: hypothesis
        basis: domain_rationale
        evidence: []
        assumptions: ["Central execution action of cutting."]

  - category: monitor
    applicability: present
    steps:
      - statement: "Observe the path of the cut during execution"
        status: hypothesis
        basis: domain_rationale
        evidence: []
        assumptions: ["Carpenter monitors progress during and immediately after cutting."]

  - category: modify
    applicability: conditional
    steps:
      - statement: "Adjust the positioning of the material or cutting tool"
        status: hypothesis
        basis: domain_rationale
        evidence: []
        assumptions: ["Applies when the cut deviates from the intended line."]
    notes: "Occurs when deviation is detected during monitoring."

  - category: conclude
    applicability: present
    steps:
      - statement: "Clear the cut wood from the work area"
        status: hypothesis
        basis: domain_rationale
        evidence: []
        assumptions: ["Finishes the job and clears the workspace."]

flow:
  edges:
    - from: define
      to: locate
    - from: locate
      to: prepare
    - from: prepare
      to: confirm
    - from: confirm
      to: execute
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
  branches: []

excluded_items:
  - statement: "Cut wood in a straight line"
    classification: desired_outcome
    reason: "'In a straight line' is a quality criterion (Desired Outcome: Minimize the deviation from the intended cutting line)."
  - statement: "Use a Bosch circular saw"
    classification: solution
    reason: "Names a specific brand and tool."

evidence_gaps:
  - "Observation data on how carpenters handle material securement across different wood types."
next_research_question: "What conditions cause carpenters to pause execution and adjust alignment during a cut?"
```
