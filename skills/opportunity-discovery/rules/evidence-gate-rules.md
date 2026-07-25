# Opportunity Discovery Evidence Gate Rules

## Rule 1: Never Upgrade Pure Ideas to Proof of Demand
When an input contains only a product idea or feature suggestion (e.g., "I want to build an AI diary app"), the system MUST:
- Set `current_stage: idea_only`.
- Set `confidence: low`.
- State explicitly under `what_you_cannot_conclude_yet`: "Demand, willingness to pay, and switching motivation cannot be determined."
- Set `recommended_action`: "Do not start development yet; validate problem existence first."
- Set `smallest_next_validation_step`: Formulate an interview probe targeting past customer behavior.

## Rule 2: Redirect Feature Requests to Workflow Pain
When an input requests a specific button or feature (e.g., "Add a PDF export button"), the system MUST:
- Classify the button as a `hypothesis` solution design.
- Identify the underlying workflow step as `unknown`.
- Set `recommended_skill`: `jtbd-context-explorer` or `jtbd-switch-interview`.

## Rule 3: Opportunity Scores Measure Underserved Metrics, Not Business Success
When survey ratings ($1\text{--}10$) are provided:
- Use `jtbd-opportunity-calculator` to compute Opportunity Scores.
- Explicitly state under `what_you_cannot_conclude_yet`: "Scores rank unmet outcome metrics in this sample; they do not predict company success or prove willingness to pay."

## Rule 4: Always Output the Smallest Next Validation Step
Whenever evidence is insufficient to justify development or strategy execution, the system MUST provide a concrete, actionable next research step.
