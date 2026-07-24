# Invalid Universal Job Map Examples & Corrections

This document categorizes common anti-patterns and errors when constructing **Universal Job Maps**, providing detailed audit rationale and solution-free rewrites.

---

## Anti-Pattern 1: Mechanical Template Filling (Forcing All 8 Stages)

### Example 1.1
- **Core Functional Job**: `Set a kitchen timer`
- **Job Executor**: Home Cook
- **Invalid Map Attempt**:
  - *Define*: Determine timer duration
  - *Locate*: Find the kitchen timer on the counter *(Forced step without evidence)*
  - *Prepare*: Clean the kitchen timer buttons *(Forced step)*
  - *Confirm*: Check timer battery status *(Forced step)*
  - *Execute*: Start the timer
  - *Monitor*: Watch the countdown display *(Forced step)*
  - *Modify*: Adjust countdown speed *(Invalid/Forced)*
  - *Conclude*: Store timer in drawer *(Forced step)*

- **Audit Rationale**:
  Forcing every single category to contain a step when the evidence only describes setting a duration and starting a timer violates the evidence-driven principle. Categories without supported evidence or functional necessity must be marked `not_applicable` or `unknown`.

- **Corrected Applicability Mapping**:
  - `define`: present (`Determine timer duration`)
  - `locate`: not_applicable
  - `prepare`: not_applicable
  - `confirm`: not_applicable
  - `execute`: present (`Start the timer`)
  - `monitor`: unknown
  - `modify`: unknown
  - `conclude`: present (`Silence the timer alert`)

---

## Anti-Pattern 2: Solution & Tool Contamination in Map Steps

### Example 2.1
- **Core Functional Job**: `Prepare a project status update`
- **Invalid Map Steps**:
  - `Open the Jira dashboard`
  - `Export data into an Excel spreadsheet`
  - `Format slides in PowerPoint`
  - `Post the update on Slack`

- **Audit Rationale**:
  `Jira`, `Excel`, `PowerPoint`, and `Slack` are specific software tools, platforms, and interfaces. If the organization switches from Jira to GitHub Issues, or from Slack to Email, the functional steps of the job do not change.

- **Solution-Free Rewrites**:
  - `Open the Jira dashboard` -> **`Identify relevant project status information`**
  - `Export data into an Excel spreadsheet` -> **`Organize status information`**
  - `Format slides in PowerPoint` -> **`Compose the status update`**
  - `Post the update on Slack` -> **`Deliver the status update`**

---

## Anti-Pattern 3: Outcome & Performance Metric Contamination

### Example 3.1
- **Core Functional Job**: `Prepare a project status update`
- **Invalid Map Steps**:
  - `Quickly gather project information`
  - `Accurately verify data completeness`
  - `Seamlessly send update to stakeholders`

- **Audit Rationale**:
  `Quickly`, `Accurately`, and `Seamlessly` are performance outcomes (speed, accuracy, ease). They belong in Desired Outcome Statements (*Minimize the time it takes to gather information*), not in job map steps.

- **Outcome-Free Rewrites**:
  - `Quickly gather project information` -> **`Identify relevant project status information`**
  - `Accurately verify data completeness` -> **`Verify the completeness of status information`**
  - `Seamlessly send update to stakeholders` -> **`Deliver the status update`**

---

## Anti-Pattern 4: Lifecycle & Purchasing Activity Contamination

### Example 4.1
- **Core Functional Job**: `Prepare a project status update`
- **Invalid Map Steps**:
  - `Buy a project management software subscription`
  - `Install reporting software on the laptop`
  - `Upgrade software to premium plan`

- **Audit Rationale**:
  Buying, installing, and upgrading software are purchase decisions and consumption chain support tasks. They are NOT steps in executing the core functional job of preparing a status update.

- **Action**: Exclude these steps and place them under `excluded_items` with classification `lifecycle_activity` or `purchase_activity`.

---

## Anti-Pattern 5: UI Click Workflow / User Journey Misalignment

### Example 5.1
- **Core Functional Job**: `Transfer funds between accounts`
- **Invalid Map Steps**:
  - `Click on the 'Login' button`
  - `Type username and password`
  - `Select dropdown option 'Checking'`
  - `Press 'Submit' button`

- **Audit Rationale**:
  Describing UI clicks, button presses, and form fields maps a current web application's interaction design, not the customer's functional job. A solution-free job map remains valid whether funds are transferred via mobile app, ATM, phone banking, or smart contract.

- **Functional Job Map Rewrites**:
  - `Define`: **`Determine the transfer amount and destination`**
  - `Confirm`: **`Verify account balance availability`**
  - `Execute`: **`Authorize the transfer of funds`**
  - `Conclude`: **`Obtain confirmation of completed transfer`**

---

## Anti-Pattern 6: Multi-Action Compounding per Step

### Example 6.1
- **Core Functional Job**: `Prepare a project status update`
- **Invalid Map Step**:
  - `Gather, organize, and verify project status information`

- **Audit Rationale**:
  Combines 3 distinct actions (`Gather` = Locate, `Organize` = Prepare, `Verify` = Confirm) across 3 different Universal Job Map categories into a single sentence. Compound steps prevent independent measurement of desired outcomes.

- **Decompounding Correction**:
  - *Locate*: **`Identify relevant project status information`**
  - *Prepare*: **`Organize status information`**
  - *Confirm*: **`Verify the completeness of status information`**
