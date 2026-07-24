# JTBD Skills Suite (Outcome-Driven Innovation & Jobs-to-be-Done)

A modular open-source Agent Skills repository for applying
Jobs-to-be-Done (JTBD) and Outcome-Driven Innovation (ODI)
methods to product research, market strategy, and requirement definition.

Designed according to the [Agent Skills Specification](https://github.com/agentskills/agentskills).

---

## 📁 Repository Structure (v0.1 Baseline)

```text
jtbd-skills/
├── README.md
├── LICENSE
├── principles/
│   └── SKILL.md                 # Shared contracts, evidence rules, and cross-skill terminology
└── skills/
    ├── jtbd-job-definer/        # Core Functional Job Definer (Atomic Skill 1)
    │   ├── SKILL.md             # Main skill definition & frontmatter
    │   ├── references/
    │   │   └── job-statement-rules.md   # Detailed syntax, scope, and resolution rules
    │   ├── examples/
    │   │   ├── valid-examples.md        # Valid core functional job statements
    │   │   └── invalid-examples.md      # Anti-pattern examples & rewrites
    │   └── tests/
    │       └── cases.yaml               # Test suite for agent validation & auditing
    ├── jtbd-job-mapper/         # Universal Job Mapper (Atomic Skill 2)
    │   ├── SKILL.md             # Main skill definition & frontmatter
    │   ├── references/
    │   │   └── universal-job-map-rules.md # Stage boundaries & mapping rules
    │   ├── examples/
    │   │   ├── valid-job-maps.md        # Provisional valid job map examples
    │   │   └── invalid-job-maps.md      # Map-level anti-pattern examples
    │   └── tests/
    │       └── cases.yaml               # Test suite for job mapping validation
    └── jtbd-outcome-engineer/   # Desired Outcome Engineer (Atomic Skill 3)
        ├── SKILL.md             # Main skill definition & frontmatter
        ├── references/
        │   └── outcome-statement-rules.md # Syntax & metric rules
        └── tests/
            └── cases.yaml               # Test suite for outcome validation
```

---

## 🎯 Principles

All skills in this repository strictly adhere to core ODI principles:
1. **Solution-Free**: A job is independent of technology, products, features, or suppliers.
2. **Outcome-Free**: Performance criteria (speed, cost, accuracy) are outcomes, not the job.
3. **Evidence-Driven**: Distinguish between direct evidence and inferences. Never fabricate research data.
4. **Job Executor Perspective**: Always define the job from the person executing it, not the vendor.

---

## 🚀 Skills Overview

| Skill Name | Scope | Status |
| :--- | :--- | :--- |
| **`principles`** | Cross-skill contract, terminology & evidence rules | `v0.1` |
| **`jtbd-job-definer`** | Extract, audit, and rewrite solution-free Core Functional Jobs | `v0.1` |
| **`jtbd-job-mapper`** | Deconstruct defined jobs into solution-free Universal Job Maps | `v0.1` |
| **`jtbd-outcome-engineer`** | Formulate formulaic Desired Outcome Statements for a job map step | `v0.1 (Draft)` |

---

## 📄 License

MIT License. See [LICENSE](./LICENSE) for details.
