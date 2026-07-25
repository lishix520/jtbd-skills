# Changelog

All notable changes to the **JTBD Skills Suite** project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.5.4] - 2026-07-25

### Fixed
- **Clean Raw Markdown Format Cleanup**: Re-created `README.md` cleanly without string escaping, removing all accidental backslash escapes (`\#`, `\*\*`, `\[`), and verified zero escaped backslashes (`grep -nE '\\\\[#*\[\]`]' README.md`). Single-line commands provided for Verify section.

---

## [0.5.3] - 2026-07-25

### Fixed
- **Clean Verbatim Verification Code Blocks**: Replaced `README.md` repository verification section with exact, unescaped raw Markdown Bash code blocks (`git clone/cd`, `calculate_opportunity.py`, `diff`).

---

## [0.5.2] - 2026-07-25

### Fixed
- **Verification Code Blocks Split**: Formatted `README.md` repository verification into 3 distinct clean fenced Bash code blocks (`clone/cd`, `calculate_opportunity.py`, `diff`) without line wrapping or redirection escaping errors.
- **Unified Readiness Stage & Decision Scope Enums**: Unified `readiness_stage` (`idea_only`, `anecdotal_signal`, `evidence_emerging`, `ready_for_outcome_ranking`, `ready_for_strategy_assessment`, `not_decision_ready`) and added explicit `decision_scope` metadata field in `skills/opportunity-discovery/SKILL.md` and `tests/cases.yaml`.

---

## [0.5.1] - 2026-07-25

### Fixed
- **Single Authoritative Evidence Protocol Path**: Consolidated and verified `principles/evidence-model.md` as the single authoritative protocol path across `opportunity-discovery/SKILL.md`, `README.md`, and `ARCHITECTURE.md`.
- **Refined Quantitative Routing Matrix**: Split broad quantitative routing in `opportunity-discovery` into 3 precise rows: `ready_for_outcome_ranking` (`jtbd-opportunity-calculator`), `ready_for_strategy_assessment` (`jtbd-growth-strategist`), and `partial_market_evidence` (requires outcome survey & segment evidence).
- **Added 5-Dimension Confidence Criteria**: Updated `principles/evidence-model.md` with explicit confidence evaluation criteria (Traceability, Relevance, Coverage, Consistency, Decision Alignment) to ensure quantitative data is not automatically assumed to be high confidence.
- **GitHub About Alignment**: Updated GitHub repository About description to `Find opportunities people will pay for with evidence-aware product discovery skills for AI agents.`.

---

## [0.5.0] - 2026-07-25

### Added
- **`opportunity-discovery` Orchestrator Skill**: Top-level Evidence Gate orchestrator and router (`skills/opportunity-discovery/`) that classifies input into 4 tiers (`idea_only`, `customer_signal`, `research_evidence`, `quantitative_evidence`), routes to downstream skills, and outputs an Opportunity Decision Brief.
- **Shared Evidence Gate Protocol (`principles/evidence-model.md`)**: Shared protocol defining 4 evidence tiers (`direct_evidence`, `inference`, `hypothesis`, `unknown`) and 5 readiness statuses (`Idea only`, `Anecdotal signal`, `Evidence emerging`, `Decision-ready for next step`, `Not decision-ready`).
- **3 Real-World Demos**:
  - `examples/01-idea-only-ai-diary.md` (Idea Only -> Do not build yet; interview 5 target users)
  - `examples/02-feature-request-pdf-export.md` (Feature Request -> Validate executive report workflow pain first)
  - `examples/03-survey-opportunity-ranking.md` (Quantitative Survey -> Opportunity Scores rank outcomes, do not predict company success)
- **Architecture Diagram Update**: Updated `ARCHITECTURE.md` to cover `opportunity-discovery` as the 9th skill orchestrating both Christensen and Ulwick ODI pipelines.

---

## [0.4.4] - 2026-07-25

### Fixed
- **Clean Repository Structure Link**: Replaced bulky ASCII tree block in `README.md` with a concise link (`Browse the repository structure in the GitHub file tree.`).
- **Robust Verification Commands**: Split `README.md` repository verification into two bullet-proof, easy-to-copy Bash code blocks.
- **GitHub About & Submission Alignment**: Updated `docs/awesome-agent-skills-submission.md` with official GitHub About description ("Find opportunities people will pay for with evidence-aware customer research skills for AI agents.") and search intent Topics.

---

## [0.4.3] - 2026-07-25

### Added
- **Market Signal Entrances & Directory Submission Copy (`docs/awesome-agent-skills-submission.md`)**: Added standardized discoverability keywords and pre-formatted user-outcome submission text for external Agent Skills directories (e.g. `VoltAgent/awesome-agent-skills`).

---

## [0.4.2] - 2026-07-25

### Fixed
- **Repository Tree Folding**: Folded the README repository tree under `<details><summary><b>📁 Repository Structure</b></summary></details>` by removing a stray orphan tag.
- **Architecture Synchronization**: Updated `ARCHITECTURE.md` to cover all 8 atomic skills and included `jtbd-switch-interview` in the dual methodology pipelines overview diagram and contract matrix.
- **Cleaned Internal Skill Numbering**: Removed internal `Skill 8` and `Atomic Skill 1–7` labels from `README.md` and updated Overview status badges to `v0.4` baseline.

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
