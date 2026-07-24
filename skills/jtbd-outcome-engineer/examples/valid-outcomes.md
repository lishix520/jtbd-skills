# Valid Desired Outcome Statement Examples

> These are illustrative, provisional desired outcome statements.
> Their metrics are hypotheses based on stated domain rationale, not verified
> findings from customer research interviews.

---

## Target Job Map Step 1: Locate: Identify relevant project status information

- **Core Functional Job**: `Prepare a project status update`
- **Job Executor**: Project Manager
- **Job Map Step**: Category: `locate` | Statement: `Identify relevant project status information`

```yaml
job_context:
  core_functional_job: "Prepare a project status update"
  job_executor: "Project manager"
  job_map_step:
    category: locate
    statement: "Identify relevant project status information"

outcomes_status: provisional

desired_outcomes:
  - statement: "Minimize the time it takes to identify relevant project status information"
    direction: minimize
    metric_type: time
    measurement_target: "identify relevant project status information"
    contextual_clarifier: ""
    status: hypothesis
    basis: domain_rationale
    evidence: []
    assumptions: ["Delay in finding status information causes overall report preparation delay."]

  - statement: "Minimize the likelihood of missing critical status changes across active workstreams"
    direction: minimize
    metric_type: likelihood
    measurement_target: "missing critical status changes across active workstreams"
    contextual_clarifier: ""
    status: hypothesis
    basis: domain_rationale
    evidence: []
    assumptions: ["Overlooking active status changes leads to inaccurate updates."]

  - statement: "Minimize the effort required to locate status updates from distributed team members"
    direction: minimize
    metric_type: effort
    measurement_target: "locate status updates from distributed team members"
    contextual_clarifier: "from distributed team members"
    status: hypothesis
    basis: domain_rationale
    evidence: []
    assumptions: ["Manual check-ins across multiple channels increase PM cognitive load."]

excluded_items:
  - statement: "Minimize the time it takes to click the Jira export button"
    classification: solution
    reason: "Names a specific software product (Jira) and interface element (button)."

evidence_gaps:
  - "Direct customer quotes detailing specific failure modes when locating status information across remote teams."
next_research_question: "Which specific sources of project status information cause the highest delay for project managers?"
```

---

## Target Job Map Step 2: Confirm: Verify the completeness of status information

- **Core Functional Job**: `Prepare a project status update`
- **Job Executor**: Project Manager
- **Job Map Step**: Category: `confirm` | Statement: `Verify the completeness of status information`

```yaml
job_context:
  core_functional_job: "Prepare a project status update"
  job_executor: "Project manager"
  job_map_step:
    category: confirm
    statement: "Verify the completeness of status information"

outcomes_status: provisional

desired_outcomes:
  - statement: "Minimize the time it takes to verify the completeness of status information"
    direction: minimize
    metric_type: time
    measurement_target: "verify the completeness of status information"
    contextual_clarifier: ""
    status: hypothesis
    basis: domain_rationale
    evidence: []
    assumptions: ["Checking information completeness consumes non-trivial time."]

  - statement: "Minimize the likelihood of omitting required status details prior to draft composition"
    direction: minimize
    metric_type: likelihood
    measurement_target: "omitting required status details prior to draft composition"
    contextual_clarifier: "prior to draft composition"
    status: hypothesis
    basis: domain_rationale
    evidence: []
    assumptions: ["Incomplete verification leads to inaccurate status reporting."]

  - statement: "Minimize the effort required to confirm the accuracy of reported metrics"
    direction: minimize
    metric_type: effort
    measurement_target: "confirm the accuracy of reported metrics"
    contextual_clarifier: ""
    status: hypothesis
    basis: domain_rationale
    evidence: []
    assumptions: ["Cross-checking reported numbers against source systems requires manual labor."]

excluded_items:
  - statement: "Minimize the likelihood of error during verification"
    classification: vague_metric
    reason: "Uses abstract likelihood target ('error') instead of naming a concrete undesired event."
  - statement: "Maximize confidence during executive reviews"
    classification: emotional_social
    reason: "Describes emotional/social feeling of confidence rather than a functional performance metric."

evidence_gaps:
  - "Customer verification quotes regarding specific completeness criteria expected by executive reviewers."
next_research_question: "What specific status details are most frequently omitted during verification?"
```
