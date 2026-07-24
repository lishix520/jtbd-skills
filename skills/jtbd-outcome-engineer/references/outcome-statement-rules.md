# Desired Outcome Statement Rules & Guidelines

## Purpose

A Desired Outcome Statement defines the metric customer (job executor) uses to measure value and success when executing a specific step in a Universal Job Map.

In Outcome-Driven Innovation (ODI), desired outcomes are the measurable criteria against which solutions are designed, evaluated, and prioritized.

---

## Formulaic Syntax Rules

Every Desired Outcome Statement MUST follow this rigid formulaic syntax:

$$\text{Desired Outcome} = \text{Direction} + \text{Performance Metric} + \text{Object of Control} + [\text{Optional Contextual Clarifier}]$$

### 1. Direction
- **`Minimize`**: Used for 95%+ of ODI outcome statements. Customers almost always seek to reduce waste, delay, risk, error, or physical/mental effort.
- **`Maximize`**: Used ONLY when describing an increase in yield, throughput, or capacity without negative trade-offs.

### 2. Performance Metric
- **Time**: `the time it takes to...` (measures duration/delay).
- **Likelihood**: `the likelihood of...` or `the likelihood that...` (measures probability of error, failure, or undesired event).

### 3. Object of Control
- The specific noun phrase representing the physical, digital, or informational asset being acted upon or monitored during the job map step.

### 4. Optional Contextual Clarifier
- Added to restrict the metric to specific environmental or operational conditions (e.g., `when project status is changing rapidly`).

---

## Metric Type Guidelines

| Desired Metric Type | Standard Formula | Example |
| :--- | :--- | :--- |
| **Time (Duration)** | `Minimize the time it takes to [action/verb] [object]` | *Minimize the time it takes to identify relevant status information* |
| **Likelihood (Error/Risk)** | `Minimize the likelihood that/of [undesired event]` | *Minimize the likelihood of omitting required status details* |
| **Likelihood (Delay)** | `Minimize the likelihood of experiencing a delay in [action]` | *Minimize the likelihood of experiencing a delay in verifying completeness* |

---

## Anti-Patterns & Blacklist Words

### 1. Vague Quality Buzzwords (REJECT)
Do NOT use non-metric buzzwords in outcome statements. Convert them to formulaic metrics:

| Vague Buzzword | Error Reason | Formulaic Metric Conversion |
| :--- | :--- | :--- |
| *Fast* | Vague quality term | **Minimize the time it takes to...** |
| *Accurate* | Vague quality term | **Minimize the likelihood of error in...** |
| *Safe* | Vague quality term | **Minimize the likelihood of injury/damage during...** |
| *Easy / Seamless* | Vague quality term | **Minimize the effort required to...** |
| *Reliable* | Vague quality term | **Minimize the likelihood of malfunction during...** |

### 2. Solution & Feature Contamination (REJECT)
Outcome statements must NEVER name a tool, software, technology, UI element, or channel.

| Invalid (Solution-Contaminated) | Valid (Solution-Free Desired Outcome) |
| :--- | :--- |
| *Minimize the time it takes to click the Jira export button* | **Minimize the time it takes to access status information** |
| *Minimize the likelihood of an AI summary error* | **Minimize the likelihood of inaccuracies in the status update** |

### 3. Compound Metric Statements (SPLIT)
A single outcome statement must contain ONLY ONE metric. Never combine time and likelihood, or multiple objects of control into one statement.

- **Invalid Compound**: `Minimize the time and likelihood of error when verifying completeness`
- **Correct Split**:
  1. *Minimize the time it takes to verify the completeness of status information*
  2. *Minimize the likelihood of error when verifying the completeness of status information*

### 4. Job Step vs. Outcome Confusion (REJECT)
A job step is an ACTION (`Verify completeness`). An outcome is a METRIC OF SUCCESS (`Minimize the likelihood of omitting information during verification`).
