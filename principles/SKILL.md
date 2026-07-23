---
name: jtbd-principles
description: Shared principles, terminology, evidence discipline, and core contracts for all Jobs-to-be-Done (JTBD) and Outcome-Driven Innovation (ODI) agent skills.
---

# JTBD Shared Principles & Core Contract

This document governs all skills in the `jtbd-skills` repository. It provides the cross-skill terminology, evidence discipline, and strict analytical boundaries required to execute Outcome-Driven Innovation (ODI) reliably.

## 1. Core Terminology Contract

Every JTBD skill must strictly maintain the following distinctions:

| Term | Definition | Key Characteristic | Example |
| :--- | :--- | :--- | :--- |
| **Core Functional Job** | The stable, functional progress a job executor is trying to accomplish. | Solution-free, outcome-free, emotionally neutral. | *Restore blood flow in a blocked artery* |
| **Job Executor** | The specific person performing the core functional job. | Not a buyer persona or demographic tag. | *Interventional cardiologist* |
| **Solution** | A specific product, feature, technology, supplier, algorithm, or channel used to get a job done. | Variable over time; interchangeable. | *Angioplasty balloon catheter, Stent* |
| **Desired Outcome** | A measurable success metric used by the executor to judge how well the job is completed. | Formulaic: Direction + Metric + Object + Clarifier. | *Minimize the likelihood of damaging the arterial wall during inflation* |
| **Emotional Job** | How the job executor wants to feel while executing the job. | Internal psychological state. | *Feel confident during high-risk procedures* |
| **Social Job** | How the job executor wants to be perceived by peers, patients, or superiors. | External perception / status. | *Be regarded as an expert practitioner* |
| **Consumption Chain Job** | A lifecycle support activity related to the product (install, setup, clean, maintain, dispose). | Executed by support roles or executor in support mode. | *Sterilize the catheter before procedure* |

---

## 2. Evidence Discipline & Source Tracing

When analyzing user prompts, research notes, product descriptions, or interview transcripts:

1. **Evidence vs. Inference Separation**:
   - **Direct Evidence**: Explicit statements provided in the source text. Must be cited or preserved.
   - **Inference / Hypothesis**: Logical deductions made by the agent. Must be explicitly flagged with `status: inferred` or `status: candidate`.
   - **Fabrication Ban**: Never invent customer interviews, survey scores, market satisfaction data, or quotes.

2. **Handling Missing Evidence**:
   - If the job executor is unknown, flag it as an `evidence_gap`.
   - If evidence is insufficient to define a confident functional job, state `status: insufficient_evidence` and specify the exact missing fact needed.

3. **No Solution-to-Job Tautology**:
   - Do NOT define a job by taking a solution name and appending a verb (e.g., "Use an AI tool" -> "Do AI tool usage"). A job exists independently of whether the solution exists.

---

## 3. Scope Boundaries across Skills

- **`jtbd-job-definer`**: Defines, audits, and rewrites the single **Core Functional Job Statement**.
- **`jtbd-job-mapper`**: Breaks down an established Job into sequential process steps (Universal Job Map).
- **`jtbd-outcome-uncoverer`**: Extracts quantitative Desired Outcome Statements per job map step.
- **`jtbd-opportunity-analyzer`**: Evaluates Opportunity Scores ($Importance + \max(Importance - Satisfaction, 0)$).
- **`jtbd-growth-strategist`**: Formulates business and product positioning strategy.

No skill should cross into the responsibility of another skill without explicit input data.
