# Valid Opportunity Score Calculation Examples

> These are illustrative calculations generated from a sample survey dataset.
> The calculated scores represent **sample-level calculated signals**, not definitive, unassailable market truths.

---

## Example 1: Project Management Status Update Survey Dataset

- **Core Functional Job**: `Prepare a project status update`
- **Job Executor**: Project Manager
- **Survey Metadata**: $N = 250$ US Project Managers (Online Quantitative Survey, 1-to-10 scales)

```yaml
survey_metadata:
  importance_scale: "1_to_10"
  satisfaction_scale: "1_to_10"
  sample_size: 250
  population_definition: "US Project Managers"
  collection_method: "Online quantitative survey"

data_quality_status: complete
calculation_status: completed

methodological_assessment:
  sample_size_status: adequate
  representativeness: unverified
  collection_method_status: reported

scale_handling:
  calculation_scale: "1_to_10"
  normalization: none
  threshold_interpretation: standard

calculation_summary:
  total_outcomes_evaluated: 3
  underserved_count: 1
  appropriately_served_count: 1
  overserved_count: 1

data_limitations: []

results:
  - id: "O1"
    statement: "Minimize the time it takes to verify the completeness of status information"
    importance_mean: 9.2
    satisfaction_mean: 3.4
    satisfaction_gap: 5.8
    satisfaction_relation: below_importance
    opportunity_score: 15.0
    classification: extreme_underserved
    overserved_signal: false
    segment: "All"

  - id: "O2"
    statement: "Minimize the effort required to format status updates"
    importance_mean: 6.0
    satisfaction_mean: 7.5
    satisfaction_gap: 0.0
    satisfaction_relation: above_importance
    opportunity_score: 6.0
    classification: overserved_candidate
    overserved_signal: true
    segment: "All"

  - id: "O3"
    statement: "Minimize the likelihood of omitting required status details"
    importance_mean: 9.0
    satisfaction_mean: 9.5
    satisfaction_gap: 0.0
    satisfaction_relation: above_importance
    opportunity_score: 9.0
    classification: appropriately_served
    overserved_signal: false
    segment: "All"

next_research_question: "Which specific team structures experience the highest friction when verifying information completeness (O1)?"
```
