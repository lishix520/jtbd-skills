# Contributing to JTBD Skills Suite

Thank you for contributing to the open-source **JTBD Skills Suite**!

This project provides modular, agentic skills implementing **Jobs-to-be-Done (JTBD)** and **Outcome-Driven Innovation® (ODI)** principles based on the [Agent Skills Specification](https://github.com/agentskills/agentskills).

---

## 🎯 Core Engineering Principles

When adding or modifying skills in this repository, strictly maintain:

1. **Solution-Free & Outcome-Free Core Jobs**: Core Functional Jobs must not contain product features, technologies, or quality adjectives.
2. **One Skill, One Scope**: Each skill has a narrow, atomic responsibility. Never merge job definition, job mapping, rating generation, or strategy evaluation into a single prompt.
3. **Evidence Discipline**: Never hallucinate research data, quotes, or numerical ratings. Label unverified statements as `hypothesis` or `domain_rationale`.
4. **Deterministic Script Verification**: Quantitative calculation tools must produce deterministic, reproducible outputs from JSON/YAML inputs.

---

## 📁 Skill Directory Structure

Every skill under `skills/` must follow this structure:

```text
skills/my-skill-name/
├── SKILL.md                          # Frontmatter, scope, syntax rules, & Output YAML Schema
├── references/                       # Detailed reference rules & guidelines
│   └── my-skill-rules.md
├── examples/                         # Valid & invalid examples with audit explanations
│   ├── valid-examples.md
│   └── invalid-examples.md
└── tests/                            # Test cases for agent auditing
    └── cases.yaml
```

---

## 🧪 Local Testing & CI Validation

To validate the repository locally before submitting a pull request:

```bash
# 1. Run Python Opportunity Calculator script against integration fixture
python3 skills/jtbd-opportunity-calculator/scripts/calculate_opportunity.py \
  integration/project-status-update/04-survey-input.json \
  > /tmp/test_out.json

# 2. Compare against golden output
diff -u /tmp/test_out.json integration/project-status-update/05-opportunity-results.json
```

All Pull Requests must pass GitHub Actions CI checks (`.github/workflows/validate.yml`).
