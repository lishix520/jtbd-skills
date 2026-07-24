# Valid Four Forces Analysis Examples

> These are synthetic examples for interface and classification illustration.
> They are not customer research or evidence of a market pattern.

---

## Example 1: Full Four Forces Analysis (Spreadsheet -> Reporting Service)

### Source Input
```yaml
sources:
  - id: interview-01
    type: interview
    text: "I spend two hours every Thursday manually combining spreadsheets from 4 team leads. Now that our department has doubled, I missed two executive deadlines last month. We are evaluating an automated team reporting service. If it auto-consolidates updates, I won't have to copy-paste. However, everyone knows the spreadsheet template, so changing it will disrupt our weekly team routine. Also, I worry the new tool could lose historical data during migration or fail internal IT compliance."
```

### Extracted Four Forces Analysis
```yaml
analysis_status: evidence_extracted

switching_context:
  actor:
    value: "Department Project Manager"
    status: inferred
  circumstance:
    statement: "Department size doubled, causing manual spreadsheet consolidation to miss executive review deadlines."
    status: direct_evidence
    evidence:
      - source_id: interview-01
        excerpt: "Now that our department has doubled, I missed two executive deadlines last month."
  current_approach:
    statement: "Manual spreadsheet consolidation"
    status: direct_evidence
    evidence:
      - source_id: interview-01
        excerpt: "manually combining spreadsheets from 4 team leads."
  prospective_alternative:
    statement: "Automated team reporting service"
    status: direct_evidence
    evidence:
      - source_id: interview-01
        excerpt: "We are evaluating an automated team reporting service."

forces:
  push:
    - id: PUSH-001
      statement: "Manual spreadsheet consolidation cannot scale with team growth, causing missed executive review deadlines."
      status: direct_evidence
      evidence:
        - source_id: interview-01
          excerpt: "I missed two executive deadlines last month."
      assumptions: []

  pull:
    - id: PULL-001
      statement: "Automated aggregation eliminates manual copy-pasting of status updates."
      status: direct_evidence
      evidence:
        - source_id: interview-01
          excerpt: "If it auto-consolidates updates, I won't have to copy-paste."
      assumptions: []

  habit:
    - id: HABIT-001
      statement: "Team familiarity with existing spreadsheet templates creates inertia against changing weekly routines."
      status: direct_evidence
      evidence:
        - source_id: interview-01
          excerpt: "everyone knows the spreadsheet template, so changing it will disrupt our weekly team routine."
      assumptions: []

  anxiety:
    - id: ANX-001
      statement: "Concern that data migration might lose historical records."
      status: direct_evidence
      evidence:
        - source_id: interview-01
          excerpt: "I worry the new tool could lose historical data during migration"
      assumptions: []
    - id: ANX-002
      statement: "Concern that prospective alternative might fail internal IT compliance."
      status: direct_evidence
      evidence:
        - source_id: interview-01
          excerpt: "or fail internal IT compliance."
      assumptions: []

hire_signals:
  big_hire:
    status: unknown
    signals: []
  little_hire:
    status: unknown
    signals: []

switching_readiness:
  status: hypothesis_available
  statement: "Switching pressure (PUSH-001) and attraction (PULL-001) favor adopting an automated reporting service, but switching inertia (HABIT-001) and compliance/data-loss anxiety (ANX-001, ANX-002) must be addressed through a migration trial."
  supporting_force_ids:
    - PUSH-001
    - PULL-001
    - HABIT-001
    - ANX-001
    - ANX-002
  missing_evidence:
    - "Budget approval and official IT security clearance."

contradictions: []
evidence_gaps:
  - "Whether IT compliance review has officially begun for the reporting service."
next_research_question: "What specific IT compliance standards must the prospective reporting service satisfy to resolve ANX-002?"
```

---

## Example 2: Big Hire Evidence Only (Incomplete Forces Data)

### Source Input
```yaml
sources:
  - id: interview-02
    type: interview
    text: "After completing a 14-day trial of the SaaS reporting service, I secured executive budget approval to replace our manual spreadsheet workflow next month."
```

### Extracted Four Forces Analysis
```yaml
analysis_status: evidence_extracted

switching_context:
  actor:
    value: "Project Manager / Department Lead"
    status: inferred
  circumstance:
    statement: "Executive budget approval secured to replace manual spreadsheet workflow."
    status: direct_evidence
    evidence:
      - source_id: interview-02
        excerpt: "secured executive budget approval to replace our manual spreadsheet workflow next month."
  current_approach:
    statement: "Manual spreadsheet workflow"
    status: direct_evidence
    evidence:
      - source_id: interview-02
        excerpt: "replace our manual spreadsheet workflow"
  prospective_alternative:
    statement: "SaaS reporting service"
    status: direct_evidence
    evidence:
      - source_id: interview-02
        excerpt: "trial of the SaaS reporting service"

forces:
  push: []
  pull: []
  habit: []
  anxiety: []

hire_signals:
  big_hire:
    status: present
    signals:
      - id: BH-001
        statement: "Completed 14-day trial and secured executive budget approval to adopt SaaS reporting service."
        status: direct_evidence
        evidence:
          - source_id: interview-02
            excerpt: "After completing a 14-day trial of the SaaS reporting service, I secured executive budget approval"
  little_hire:
    status: unknown
    signals: []

switching_readiness:
  status: insufficient_evidence
  statement: "Big Hire signal (BH-001) confirms budget approval, but qualitative Four Forces evidence (Push, Pull, Habit, Anxiety) was not collected in this excerpt."
  supporting_force_ids: []
  missing_evidence:
    - "Specific Push friction and Anxiety concerns experienced during adoption."

contradictions: []
evidence_gaps:
  - "Qualitative switching forces that drove the initial decision prior to budget approval."
next_research_question: "What primary friction in the spreadsheet process drove the manager to initiate the 14-day trial?"
```
