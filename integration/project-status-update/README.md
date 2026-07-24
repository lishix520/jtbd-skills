# Integration Fixture: Prepare a project status update

This directory contains the **Golden Path Integration Fixture** for the `jtbd-skills` repository.

It demonstrates the complete, end-to-end data pipeline across all 5 atomic skills:

```text
00-research-input.md (Synthetic research quotes)
  └── 01-job-definition.yaml (jtbd-job-definer)
        └── 02-job-map.yaml (jtbd-job-mapper)
              └── 03-desired-outcomes.yaml (jtbd-outcome-engineer)
                    └── 04-survey-input.json (Quantitative survey data)
                          └── 05-opportunity-results.json (jtbd-opportunity-calculator script)
                                └── 06-strategy-assessment.yaml (jtbd-growth-strategist)
```

> **Notice**: This fixture uses synthetic test data to validate contract interfaces and schema traceability across skills. It is not customer research or proof of a commercial market.
