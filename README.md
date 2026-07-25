# JTBD Skills Suite (Outcome-Driven Innovation & Jobs-to-be-Done)

A modular open-source Agent Skills repository for applying
Jobs-to-be-Done (JTBD) and Outcome-Driven Innovation (ODI)
methods to product research, market strategy, and requirement definition.

Designed according to the [Agent Skills Specification](https://github.com/agentskills/agentskills).

---

## 🎯 What Do You Want To Do?

Paste any customer quote, transcript, or feedback into your AI Agent:

### 💬 "I have a customer quote — what should I ask next?"
> Calls **`jtbd-switch-interview`** (Skill 8).  
> Immediately gives you **1 non-leading question** to speak out loud, **why it matters**, a **vague-answer probe**, and **what NOT to ask yet** (avoiding feature traps).

### 🔍 "I have interview notes — what did I actually learn?"
> Calls **`jtbd-context-explorer`** (Skill 6).  
> Extracts real circumstances, desired progress, workarounds, feature requests, and policy constraints without inventing customer facts.

### ⚡ "I want to understand why users do not switch."
> Calls **`jtbd-forces-analyzer`** (Skill 7).  
> Maps customer evidence into Push, Pull, Habit, and Anxiety forces to uncover why users remain stuck with legacy tools.

---

### ⚙️ Behind the Scenes: The Methodology Engine

Behind these natural conversational entry points, 8 modular single-responsibility skills (`job-definer`, `job-mapper`, `outcome-engineer`, `opportunity-calculator`, `growth-strategist`, `context-explorer`, `forces-analyzer`, `switch-interview`) enforce strict evidence contracts, anti-hallucination rules, and deterministic calculation tools.

---

## 📁 Repository Structure (v0.2 Baseline)

```text
jtbd-skills/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
├── ARCHITECTURE.md
├── principles/
│   └── SKILL.md                 # Shared contracts, evidence rules, and cross-skill terminology
├── skills/
│   ├── jtbd-switch-interview/   # Interview Guide for Why People Change (Skill 8 - Interactive UX)
│   │   ├── SKILL.md             # Main skill definition & frontmatter
│   │   ├── references/
│   │   │   └── switch-interview-rules.md # Non-leading interview rules & cheat sheet
│   │   ├── examples/
│   │   │   ├── valid-interview-guides.md   # Dual-output valid interview guides
│   │   │   └── invalid-interview-guides.md # Anti-pattern interview guidance examples
│   │   └── tests/
│   │       └── cases.yaml               # Test suite for conversational interview validation
│   ├── jtbd-job-definer/        # Core Functional Job Definer (Atomic Skill 1)
│   │   ├── SKILL.md             # Main skill definition & frontmatter
│   │   ├── references/
│   │   │   └── job-statement-rules.md   # Detailed syntax, scope, and resolution rules
│   │   ├── examples/
│   │   │   ├── valid-examples.md        # Valid core functional job statements
│   │   │   └── invalid-examples.md      # Anti-pattern examples & rewrites
│   │   └── tests/
│   │       └── cases.yaml               # Test suite for agent validation & auditing
│   ├── jtbd-job-mapper/         # Universal Job Mapper (Atomic Skill 2)
│   │   ├── SKILL.md             # Main skill definition & frontmatter
│   │   ├── references/
│   │   │   └── universal-job-map-rules.md # Stage boundaries & mapping rules
│   │   ├── examples/
│   │   │   ├── valid-job-maps.md        # Provisional valid job map examples
│   │   │   └── invalid-job-maps.md      # Map-level anti-pattern examples
│   │   └── tests/
│   │       └── cases.yaml               # Test suite for job mapping validation
│   ├── jtbd-outcome-engineer/   # Desired Outcome Engineer (Atomic Skill 3)
│   │   ├── SKILL.md             # Main skill definition & frontmatter
│   │   ├── references/
│   │   │   └── outcome-statement-rules.md # Syntax & metric rules
│   │   ├── examples/
│   │   │   ├── valid-outcomes.md        # Provisional desired outcome examples
│   │   │   └── invalid-outcomes.md      # Anti-pattern outcome examples
│   │   └── tests/
│   │       └── cases.yaml               # Test suite for outcome validation
│   ├── jtbd-opportunity-calculator/ # Opportunity Calculator (Atomic Skill 4)
│   │   ├── SKILL.md             # Main skill definition & frontmatter
│   │   ├── references/
│   │   │   └── opportunity-algorithm-rules.md # Mathematical formula & scale rules
│   │   ├── scripts/
│   │   │   └── calculate_opportunity.py       # Deterministic calculation script
│   │   ├── examples/
│   │   │   ├── valid-calculations.md          # Valid calculation examples
│   │   │   └── invalid-calculations.md        # Calculation anti-pattern examples
│   │   └── tests/
│   │       └── cases.yaml               # Test suite for score calculation validation
│   ├── jtbd-growth-strategist/   # Growth Strategist (Atomic Skill 5)
│   │   ├── SKILL.md             # Main skill definition & frontmatter
│   │   ├── references/
│   │   │   └── growth-strategy-matrix-rules.md # Matrix prerequisites & evidence rules
│   │   ├── examples/
│   │   │   ├── valid-strategy-assessments.md   # Valid strategy evaluation examples
│   │   │   └── invalid-strategy-assessments.md # Strategy evaluation anti-pattern examples
│   │   └── tests/
│   │       └── cases.yaml               # Test suite for strategy assessment validation
│   ├── jtbd-context-explorer/   # Context Explorer (Atomic Skill 6)
│   │   ├── SKILL.md             # Main skill definition & frontmatter
│   │   ├── references/
│   │   │   └── context-exploration-rules.md # Circumstance & progress extraction rules
│   │   ├── examples/
│   │   │   ├── valid-context-analyses.md      # Valid context extraction examples
│   │   │   └── invalid-context-analyses.md    # Context extraction anti-pattern examples
│   │   └── tests/
│   │       └── cases.yaml               # Test suite for context extraction validation
│   └── jtbd-forces-analyzer/    # Four Forces Analyzer (Atomic Skill 7)
│       ├── SKILL.md             # Main skill definition & frontmatter
│       ├── references/
│       │   └── four-forces-rules.md     # Push, Pull, Habit, and Anxiety rules
│       ├── examples/
│       │   ├── valid-four-forces-analyses.md   # Valid Four Forces analysis examples
│       │   └── invalid-four-forces-analyses.md # Four Forces analysis anti-pattern examples
│       └── tests/
│           └── cases.yaml               # Test suite for Four Forces analysis validation
└── integration/
    ├── project-status-update/              # Quantitative ODI Golden Path Fixture (Skill 1-5)
    │   ├── README.md                      # Fixture architecture & pipeline documentation
    │   ├── 00-research-input.md           # Synthetic research statements
    │   ├── 01-job-definition.yaml         # Skill 1 Output
    │   ├── 02-job-map.yaml                # Skill 2 Output
    │   ├── 03-desired-outcomes.yaml       # Skill 3 Output
    │   ├── 04-survey-input.json           # Quantitative survey input
    │   ├── 05-opportunity-results.json   # Skill 4 Output (Script-generated)
    │   ├── 06-strategy-assessment.yaml   # Skill 5 Output (Insufficient evidence stopping)
    │   └── validation.md                  # Traceability & hash validation report
    └── spreadsheet-to-reporting-service/   # Qualitative Christensen Golden Path Fixture (Skill 6-7)
        ├── README.md                      # Qualitative fixture architecture & pipeline documentation
        ├── 00-research-input.md           # Synthetic qualitative research quotes
        ├── 01-context-analysis.yaml       # Skill 6 Output (Context & progress extraction)
        ├── 02-four-forces-analysis.yaml   # Skill 7 Output (Push, Pull, Habit, Anxiety)
        └── validation.md                  # ID traceability & evidence linkage report
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
| **`jtbd-switch-interview`** | Interactive Interview Guide: "Why People Change" (Conversational UX) | `v0.2 (Draft)` |
| **`jtbd-job-definer`** | Extract, audit, and rewrite solution-free Core Functional Jobs | `v0.1` |
| **`jtbd-job-mapper`** | Deconstruct defined jobs into solution-free Universal Job Maps | `v0.1` |
| **`jtbd-outcome-engineer`** | Formulate formulaic Desired Outcome Statements for a job map step | `v0.1` |
| **`jtbd-opportunity-calculator`** | Compute quantitative ODI Opportunity Scores from survey ratings | `v0.1` |
| **`jtbd-growth-strategist`** | Map opportunity landscapes and market evidence to growth strategies | `v0.1` |
| **`jtbd-context-explorer`** | Extract qualitative circumstances, progress, and non-consumption evidence | `v0.2` |
| **`jtbd-forces-analyzer`** | Organize switching evidence into Push, Pull, Habit, and Anxiety forces | `v0.2` |

---

## ⚡ Quick Start

Validate the repository and run the end-to-end integration pipeline in 3 commands:

```bash
# 1. Clone the repository
git clone https://github.com/lishix520/jtbd-skills.git && cd jtbd-skills

# 2. Run deterministic Opportunity Calculator script against the Quantitative Golden Path Fixture
python3 skills/jtbd-opportunity-calculator/scripts/calculate_opportunity.py \
  integration/project-status-update/04-survey-input.json \
  > /tmp/calculated_out.json

# 3. Verify script calculation against golden output
diff -u /tmp/calculated_out.json integration/project-status-update/05-opportunity-results.json
```

For complete architecture details, dual methodology pipelines, and evidence hierarchies, see [ARCHITECTURE.md](./ARCHITECTURE.md).

---

## 📄 License

MIT License. See [LICENSE](./LICENSE) for details.
