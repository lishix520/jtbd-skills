# Invalid Core Functional Job Examples & Rewrites

This document categorizes common anti-patterns and errors when formulating **Core Functional Job** statements, providing detailed audit rationale and solution-free rewrites.

---

## Error Category 1: Solution / Feature Contamination

### Example 1.1
- **Invalid Statement**: `Use an AI assistant to organize project information`
- **Error Type**: Solution Contamination
- **Violation**: `AI assistant` is a solution/technology.
- **Audit Rationale**: If AI assistants disappear tomorrow, the user still needs to organize project information. The tool must be removed.
- **Solution-Free Rewrite**: `Organize project information`

### Example 1.2
- **Invalid Statement**: `Send Slack messages to keep the team updated`
- **Error Type**: Solution & Channel Contamination
- **Violation**: `Slack` (brand/product) and `messages` (format/channel).
- **Solution-Free Rewrite**: `Inform team members of project updates`

### Example 1.3
- **Invalid Statement**: `Boil water using a smart stovetop kettle`
- **Error Type**: Solution & Narrow Scope Contamination
- **Violation**: `smart stovetop kettle` is a solution; boiling water is only a step.
- **Solution-Free Rewrite**: `Prepare a hot beverage for consumption`

---

## Error Category 2: Outcome / Performance Metric Contamination

### Example 2.1
- **Invalid Statement**: `Cut wood in a straight line`
- **Error Type**: Outcome Contamination
- **Violation**: `in a straight line` is a performance quality criterion (Desired Outcome).
- **Audit Rationale**: "In a straight line" measures the quality/precision of execution (*Minimize the deviation from the intended cutting line*), not the core functional job.
- **Outcome-Free Rewrite**: `Cut wood`

### Example 2.2
- **Invalid Statement**: `Quickly and reliably share documents with external clients`
- **Error Type**: Outcome Contamination
- **Violation**: `Quickly` (speed outcome) and `reliably` (reliability outcome).
- **Audit Rationale**: Speed and reliability are Desired Outcomes used to evaluate performance, not the job itself.
- **Outcome-Free Rewrite**: `Share documents with external clients`

### Example 2.3
- **Invalid Statement**: `Safely restore blood flow in a blocked artery without damaging tissue`
- **Error Type**: Outcome & Constraint Contamination
- **Violation**: `Safely` and `without damaging tissue` are desired outcomes/constraints.
- **Outcome-Free Rewrite**: `Restore blood flow in a blocked artery`

### Example 2.4
- **Invalid Statement**: `Easily and cheaply commute to work`
- **Error Type**: Outcome Contamination
- **Violation**: `Easily` and `cheaply` are performance criteria.
- **Outcome-Free Rewrite**: `Commute to work`

---

## Error Category 3: Emotional / Social Job Contamination

### Example 3.1
- **Invalid Statement**: `Confidently present project status to executives`
- **Error Type**: Emotional Contamination
- **Violation**: `Confidently` describes how the presenter wants to feel (Emotional Job).
- **Rewrite & Separation**:
  - **Core Functional Job**: `Present project status for executive review`
  - **Emotional Job (Separate)**: *Feel confident during executive presentations*

### Example 3.2
- **Invalid Statement**: `Look like an expert home chef when serving dinner`
- **Error Type**: Social Contamination
- **Violation**: `Look like an expert home chef` describes social perception (Social Job).
- **Rewrite & Separation**:
  - **Core Functional Job**: `Prepare a meal for dinner guests`
  - **Social Job (Separate)**: *Be perceived as a skilled home cook*

---

## Error Category 4: Multi-Job Merging (Compounded Objectives)

### Example 4.1
- **Invalid Statement**: `Collect, analyze, and report project metrics to stakeholders`
- **Error Type**: Multi-Job / Process Step Compound
- **Violation**: `Collect`, `analyze`, and `report` are separate functional process steps in a broader job map, or three distinct jobs.
- **Audit Rationale**: Merging multiple verbs makes it impossible to define clean desired outcomes.
- **Rewrite**: Split into separate process steps within the job `Manage project performance`, or evaluate if the core job is `Report project metrics to stakeholders`.

---

## Error Category 5: Vendor Activity / Purchasing Misalignment

### Example 5.1
- **Invalid Statement**: `Market and sell angioplasty catheters to hospital buyers`
- **Error Type**: Vendor Perspective
- **Violation**: Describes what the vendor does, not what the customer (surgeon/patient) is trying to achieve.
- **Rewrite**: Focus on the customer: `Restore blood flow in a blocked artery`

### Example 5.2
- **Invalid Statement**: `Buy a home thermostat at Home Depot`
- **Error Type**: Purchasing Activity / Consumption Chain
- **Violation**: Buying a product is a purchase decision, not the core functional job.
- **Rewrite**: Core Functional Job: `Control indoor temperature in a residence`

---

## Quick Reference Audit Summary

| Candidate Input | Primary Defect | Corrected Core Functional Job Statement |
| :--- | :--- | :--- |
| *Use Zoom to hold virtual meetings* | Solution (Zoom, virtual) | **Conduct a team meeting** |
| *Accurately and easily track personal expenses* | Outcome (Accurately, easily) | **Track personal expenses** |
| *Feel secure when storing confidential files in the cloud* | Emotional + Solution (Feel secure, cloud) | **Store confidential files** |
| *Build an AI app that automatically generates code* | Solution + Feature (AI app, automatically) | **Generate source code for a software application** |
