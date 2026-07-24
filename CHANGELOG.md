# Changelog

All notable changes to the **JTBD Skills Suite** project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
