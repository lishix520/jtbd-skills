# Changelog

All notable changes to the **JTBD Skills Suite** project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.4.1] - 2026-07-25

### Fixed
- **Verbatim English Hero Copy Restored**: Restored verbatim locked English Hero text in `README.md` ("Find opportunities people will pay for.").
- **Removed Over-Promising Wording**: Replaced "dictate product/business strategy" with "evaluate evidence-backed product and business strategy options" to align with stopping rule evidence discipline.
- **Repository Tree Folding**: Verified rendering of `<details><summary><b>📁 Repository Structure</b></summary>` to prevent page cluttering.

---

## [0.4.0] - 2026-07-25

### Added
- **Standardized Human-First Headers Across All 8 Skills**: Updated all 8 `SKILL.md` files with standard `Use this when`, `Don't use this when`, `Minimum input`, `What you get`, `Quick prompt`, and `What to do next` sections.
- **Human-Readable Summaries**: Integrated plain-language summary outputs (`human_summary`, `plain_language`, `next_use`, `executive_summary`, `decision_readiness`) across all 8 skills.
- **Survey Templates for Opportunity Calculator (`skills/jtbd-opportunity-calculator/templates/`)**: Added `survey-input-template.json`, `survey-input-template.csv`, and `survey-question-template.md`.
- **Handoff & Next Step Guidance**: Added explicit `What to do next` cross-skill handoff links across all 8 skills.

---

## [0.3.1] - 2026-07-25

### Fixed
- **Bilingual Readme Optimization**: Set English as the primary default presentation in `README.md` ("Find Opportunities People Will Pay For") with the Chinese translation ("找到人们愿意付钱的机会") integrated directly below as an optional section.

---

## [0.3.0] - 2026-07-25

### Added
- **`jtbd-switch-interview` (Skill 8)**: Conversational interview guide providing 30-second natural-language next questions, follow-up probes, and forbidden leading question warnings for non-expert users. Promoted to `v0.3`.
- **User-Centric Hero & Product Positioning**: Updated `README.md` with locked hero copy ("找到人们愿意付钱的机会") and 6 business scenario entry points.
- **Business Use Cases Guide (`examples/business-use-cases.md`)**: Comprehensive practical guide mapping 6 core business scenarios to customer quotes and actionable insights.

---

## [0.2.1] - 2026-07-25

### Fixed
- **Quick Start Formatting**: Formatted multi-line Bash continuation commands in `README.md` to prevent double-backslash copy-paste errors.

---

## [0.2.0] - 2026-07-25

### Added
- **`jtbd-context-explorer` (Skill 6)**: Qualitative context extraction skill extracting circumstance, desired progress, current approaches, feature requests, policy/security constraints, and non-consumption barriers.
- **`jtbd-forces-analyzer` (Skill 7)**: Qualitative switching tension analysis skill organizing customer switching evidence into Push, Pull, Habit, Anxiety, and Big Hire / Little Hire signals.
- **Qualitative Golden Path Integration Fixture (`integration/spreadsheet-to-reporting-service/`)**: End-to-end integration test suite for Christensen's qualitative path demonstrating ID linkage and evidence traceability across Skills 6 and 7.
- **Dual Methodological Pipelines Architecture**: Updated `ARCHITECTURE.md` to document both Christensen's qualitative path and Ulwick's quantitative ODI path.
- **CI Validation Expansion**: Updated `.github/workflows/validate.yml` to automatically validate qualitative fixture ID traceability alongside YAML/JSON syntax and script execution.

---

## [0.1.1] - 2026-07-24

### Fixed
- **CI Workflow Formatting**: Fixed YAML multi-line shell command syntax in `.github/workflows/validate.yml` to prevent shell continuation escaping errors.

### Added
- **Quick Start Section**: Added 3-command Quick Start guide to `README.md`.
- **`ARCHITECTURE.md`**: Architectural design documentation detailing data pipeline contracts, confidence hierarchy, and hard stopping rules across all 5 skills.
- **GitHub Issue Templates**: Added `bug_report.md`, `skill_proposal.md`, and `methodology_correction.md` under `.github/ISSUE_TEMPLATE/`.

---

## [0.1.0] - 2026-07-24

### Added
- **`principles`**: Shared JTBD/ODI contracts, terminology, evidence discipline rules, and anti-patterns.
- **`jtbd-job-definer`**: Core Functional Job definer skill with solution-free, outcome-free statement rules and test cases.
- **`jtbd-job-mapper`**: Universal Job Mapper skill using 8-stage categorization (`define` through `conclude`) and `flow.edges` functional dependency graph.
- **`jtbd-outcome-engineer`**: Formulaic Desired Outcome statement engineer skill (`Direction + Metric + Target + Clarifier`).
- **`jtbd-opportunity-calculator`**: Quantitative ODI Opportunity Score calculator skill with deterministic Python script (`calculate_opportunity.py`) and survey validation.
- **`jtbd-growth-strategist`**: Market growth strategy decision-support skill evaluating Differentiated, Dominant, Disruptive, Discrete, and Sustaining strategies with strict evidence prerequisite rules.
- **Golden Path Integration Fixture (`integration/project-status-update/`)**: End-to-end integration test suite demonstrating data pipeline traceability across all 5 skills (`00` through `06` + `validation.md`).
- **CI Automation (`.github/workflows/validate.yml`)**: GitHub Actions workflow validating YAML/JSON syntax and verifying deterministic script output against the integration fixture.
- **Project Documentation**: `README.md`, `LICENSE`, and `CONTRIBUTING.md`.
