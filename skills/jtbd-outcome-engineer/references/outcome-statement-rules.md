# Desired Outcome Statement Rules & Guidelines

## Purpose

A Desired Outcome Statement defines the metric customer (job executor) uses to measure value and success when executing a specific step in a Universal Job Map.

In Outcome-Driven Innovation (ODI), desired outcomes are the measurable criteria against which solutions are designed, evaluated, and prioritized.

---

## Formulaic Syntax Rules

Every Desired Outcome Statement MUST follow this rigid formulaic syntax:

$$\text{Desired Outcome} = \text{Direction} + \text{Performance Metric} + \text{Measurement Target} + [\text{Optional Contextual Clarifier}]$$

### 1. Direction
- **`Minimize`**: Used for 95%+ of ODI outcome statements. Customers almost always seek to reduce waste, delay, risk, error, cost, or physical/mental effort.
- **`Maximize`**: Used ONLY when describing an increase in yield, throughput, or capacity without negative trade-offs.

### 2. Performance Metric
- **Time**: `the time it takes to...` (measures duration/delay).
- **Likelihood**: `the likelihood of...` or `the likelihood that...` (measures probability of error, failure, or undesired event).
- **Effort**: `the effort required to...` (measures manual, physical, or mental labor).
- **Cost**: `the cost required to...` (measures financial expenditure).
- **Output / Yield**: `the...` (measures throughput without trade-offs).

### 3. Measurement Target
- The specific action, object, event, state, or result whose performance is being measured during the job-map step.

### 4. Optional Contextual Clarifier
- Added to restrict the metric to specific environmental or operational conditions (e.g., `when project status is changing rapidly`).

---

## Metric Type Guidelines

| Desired Metric Type | Standard Formula | Example |
| :--- | :--- | :--- |
| **Time (Duration)** | `Minimize the time it takes to [action/verb] [object]` | *Minimize the time it takes to identify relevant status information* |
| **Likelihood (Error/Risk)** | `Minimize the likelihood of [concrete undesired event]` | *Minimize the likelihood of omitting required status information* |
| **Effort (Labor)** | `Minimize the effort required to [action/verb] [object]` | *Minimize the effort required to organize status information* |
| **Cost (Expense)** | `Minimize the cost required to [action/verb] [object]` | *Minimize the cost required to obtain status information* |
| **Output / Yield** | `Maximize the [output/yield]` | *Maximize the percentage of valid records processed* |

> **Output / Yield Strictness Rule**: For output/yield metrics, name a concrete count, proportion, volume, coverage, or throughput measure. Do NOT use abstract terms such as productivity, quality, or value.

---

## Likelihood Target Specificity Rule

A likelihood outcome statement MUST name a concrete undesired event, failure mode, or specific deviation. Do NOT use abstract placeholders such as "error", "inaccuracy", or "failure" unless the specific event is explicitly defined.

- ❌ **Invalid Abstract Likelihood Target**: *Minimize the likelihood of error during verification*
- ✅ **Valid Concrete Likelihood Target**: *Minimize the likelihood of omitting required status information during verification*

---

## Anti-Patterns & Blacklist Words

### 1. Vague Quality Buzzwords (REJECT)
Do NOT use non-metric buzzwords as unqualified outcome adjectives. Convert them to formulaic metrics:

| Vague Buzzword | Error Reason | Formulaic Metric Conversion |
| :--- | :--- | :--- |
| *Fast* | Vague quality term | **Minimize the time it takes to...** |
| *Accurate* | Unqualified outcome adjective | **Minimize the likelihood of omitting/miscalculating...** (Do not use "accurate" as an unqualified adjective. Concrete verification targets like *confirm the accuracy of reported metrics* are acceptable). |
| *Safe* | Vague quality term | **Minimize the likelihood of injury/damage during...** |
| *Easy / Seamless* | Vague quality term | **Minimize the effort required to...** |
| *Cheap / Affordable* | Vague quality term | **Minimize the cost required to...** |

### 2. Solution & Feature Contamination (REJECT)
Outcome statements must NEVER name a tool, software, technology, UI element, or channel.

| Invalid (Solution-Contaminated) | Valid (Solution-Free Desired Outcome) |
| :--- | :--- |
| *Minimize the time it takes to click the Jira export button* | **Minimize the time it takes to access status information** |
| *Minimize the likelihood of an AI summary error* | **Minimize the likelihood of inaccuracies in the status update** |

### 3. Compound Metric Statements (SPLIT)
A single outcome statement must contain ONLY ONE metric. Never combine time and likelihood, or multiple objects into one statement.

- ❌ **Invalid Compound**: `Minimize the time and likelihood of error when verifying completeness`
- ✅ **Correct Split**:
  1. *Minimize the time it takes to verify the completeness of status information*
  2. *Minimize the likelihood of omitting required status information during verification*

### 4. Job Step vs. Outcome Confusion (REJECT)
A job step is an ACTION (`Verify completeness`). An outcome is a METRIC OF SUCCESS (`Minimize the likelihood of omitting information during verification`).
