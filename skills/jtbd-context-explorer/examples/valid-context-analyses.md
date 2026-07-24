# Valid Context Analysis Examples

> These are synthetic examples for interface and classification illustration.
> They are not customer research or evidence of a market pattern.

---

## Example 1: Project Status Update Context Analysis

### Source Input
```yaml
sources:
  - id: interview-01
    type: interview
    text: "The weekly review is tomorrow, and three teams have not sent updates. I currently copy-paste data into spreadsheets. I feel anxious before the executive review because I do not want them to think I have lost control. I really need a Jira button that automatically creates my weekly report."
  - id: interview-02
    type: interview
    text: "We tried using third-party web reporting tools last month, but corporate IT policy strictly prohibits sending internal project status outside our firewall."
```

### Extracted Context Analysis
```yaml
analysis_status: evidence_extracted

sources:
  - id: interview-01
    type: interview
    limitations: ["Single PM perspective"]
  - id: interview-02
    type: interview
    limitations: ["Corporate IT policy restriction stated verbally"]

circumstances:
  - id: CIR-001
    statement: "Weekly executive review is scheduled for tomorrow, but updates from three remote teams are missing."
    status: direct_evidence
    evidence:
      - source_id: interview-01
        excerpt: "The weekly review is tomorrow, and three teams have not sent updates."
    assumptions: []
    constraint_ids:
      - CON-001

desired_progress:
  - id: DP-001
    statement: "Obtain complete and accurate project status information prior to the executive review."
    status: inferred
    evidence:
      - source_id: interview-01
        excerpt: "The weekly review is tomorrow, and three teams have not sent updates."
    assumptions:
      - "Project manager requires complete team status to present during reviews."

current_approaches:
  - id: CA-001
    statement: "Copy-pasting data manually into spreadsheets"
    type: workaround
    status: direct_evidence
    evidence:
      - source_id: interview-01
        excerpt: "I currently copy-paste data into spreadsheets."
    assumptions: []

switching_triggers:
  - id: ST-001
    statement: "Imminent review deadline with missing team inputs renders manual copy-pasting insufficient."
    status: inferred
    evidence:
      - source_id: interview-01
        excerpt: "The weekly review is tomorrow, and three teams have not sent updates."
    assumptions: []

non_consumption:
  - id: NC-001
    statement: "Third-party web reporting tools"
    barrier_type: policy_or_regulation
    status: direct_evidence
    evidence:
      - source_id: interview-02
        excerpt: "We tried using third-party web reporting tools last month, but corporate IT policy strictly prohibits sending internal project status outside our firewall."
    assumptions: []

feature_requests:
  - id: FR-001
    statement: "Jira button that automatically creates weekly reports"
    status: direct_evidence
    evidence:
      - source_id: interview-01
        excerpt: "I really need a Jira button that automatically creates my weekly report."
    assumptions: []

constraints:
  - id: CON-001
    statement: "Corporate IT policy strictly prohibits transmitting internal project status data outside the company firewall."
    type: policy_or_regulation
    status: direct_evidence
    evidence:
      - source_id: interview-02
        excerpt: "corporate IT policy strictly prohibits sending internal project status outside our firewall."
    assumptions: []

competing_alternatives:
  - id: ALT-001
    statement: "Third-party web reporting tools"
    type: product
    status: direct_evidence
    evidence:
      - source_id: interview-02
        excerpt: "We tried using third-party web reporting tools last month"
    assumptions: []

emotional_signals:
  - id: EM-001
    statement: "Feeling anxious before the executive review"
    status: direct_evidence
    evidence:
      - source_id: interview-01
        excerpt: "I feel anxious before the executive review"
    assumptions: []

social_signals:
  - id: SOC-001
    statement: "Avoid being perceived by executives as having lost control of the project"
    audience: "Executive leadership"
    status: direct_evidence
    evidence:
      - source_id: interview-01
        excerpt: "because I do not want them to think I have lost control."
    assumptions: []

contradictions: []
evidence_gaps:
  - "Whether on-premise or self-hosted reporting alternatives were evaluated to comply with IT policy."
next_research_question: "Do other project managers in this organization use approved on-premise tools to aggregate team status?"
```

---

## Example 2: Restricted Air-Gapped Security Non-Consumption

### Source Input
```yaml
sources:
  - id: interview-03
    type: interview
    text: "We evaluated several commercial cloud-based status dashboards for our defense software project. However, our defense security mandate requires an air-gapped environment with zero outbound network traffic. Because none of the cloud tools support offline self-hosted deployment, we continue to maintain paper sign-off binders."
```

### Extracted Context Analysis
```yaml
analysis_status: evidence_extracted

sources:
  - id: interview-03
    type: interview
    limitations: ["Defense industry specific context"]

circumstances:
  - id: CIR-002
    statement: "Managing project status for defense software under air-gapped security compliance requirements."
    status: direct_evidence
    evidence:
      - source_id: interview-03
        excerpt: "our defense security mandate requires an air-gapped environment with zero outbound network traffic."
    assumptions: []
    constraint_ids:
      - CON-002

desired_progress:
  - id: DP-002
    statement: "Streamline project status verification while strictly complying with air-gapped security mandates."
    status: inferred
    evidence:
      - source_id: interview-03
        excerpt: "We evaluated several commercial cloud-based status dashboards for our defense software project."
    assumptions: []

current_approaches:
  - id: CA-002
    statement: "Maintaining paper sign-off binders"
    type: manual_process
    status: direct_evidence
    evidence:
      - source_id: interview-03
        excerpt: "we continue to maintain paper sign-off binders."
    assumptions: []

switching_triggers: []

non_consumption:
  - id: NC-002
    statement: "Commercial cloud-based status dashboards"
    barrier_type: security_or_privacy
    status: direct_evidence
    evidence:
      - source_id: interview-03
        excerpt: "We evaluated several commercial cloud-based status dashboards... However, our defense security mandate requires an air-gapped environment... Because none of the cloud tools support offline self-hosted deployment, we continue to maintain paper sign-off binders."
    assumptions: []

feature_requests: []

constraints:
  - id: CON-002
    statement: "Defense security mandate requiring zero outbound network traffic and air-gapped isolation."
    type: security_or_privacy
    status: direct_evidence
    evidence:
      - source_id: interview-03
        excerpt: "our defense security mandate requires an air-gapped environment with zero outbound network traffic."
    assumptions: []

competing_alternatives:
  - id: ALT-002
    statement: "Commercial cloud-based status dashboards"
    type: product
    status: direct_evidence
    evidence:
      - source_id: interview-03
        excerpt: "We evaluated several commercial cloud-based status dashboards"
    assumptions: []

emotional_signals: []
social_signals: []

contradictions: []
evidence_gaps:
  - "Whether custom internal scripts are used alongside paper binders to log status updates."
next_research_question: "Are defense teams permitted to run containerized self-hosted status software on internal air-gapped servers?"
```
