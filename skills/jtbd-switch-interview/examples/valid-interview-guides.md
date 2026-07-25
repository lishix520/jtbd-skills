# Valid Switch Interview Guide Examples

> These are synthetic examples for interface and conversational guidance illustration.
> They demonstrate the dual-layer output format: a clean human conversational guide first, followed by structured metadata for downstream methodology skills.

---

## Example 1: Redirecting a Feature Request ("Jira Button")

### Source Input
```yaml
sources:
  - id: feedback-01
    type: feedback
    text: "I really need a Jira button that automatically creates my weekly status report."
```

### Generated Interview Guide Output

## 💬 What to Ask Next

"Tell me about the last time you needed to create your weekly status report—what was happening right before you started, and how did you compile it?"

### Why This Question Matters
The customer is asking for a specific solution feature ("Jira button"). Asking about the most recent real-world event uncovers the underlying workflow friction and trigger without validating an unproven solution design.

### If the Answer Is Vague
"Can you walk me through step-by-step what you did last Thursday when you made the report? What tools were open, and where did the data come from?"

### ⚠️ What NOT to Ask Right Now
"What fields or options would you like us to put on the Jira button?" *(Avoid discussing feature specifications or solution mechanics during discovery!)*

---

### 📊 Structured Metadata

```yaml
analysis_status: evidence_extracted

interview_focus: first_thought

timeline_summary:
  first_thought: "Customer desires automatic weekly report creation."
  passive_looking: ""
  active_looking: ""
  decision: ""
  first_use: ""
  ongoing_use: ""

current_hypotheses:
  - id: HYP-001
    statement: "Manual status report compilation creates time pressure or friction prior to weekly reviews."
    status: unverified

evidence_gaps:
  - "Current manual workaround and specific friction event that triggered the feature request."

next_question_type: current_workaround
```

---

## Example 2: Probing Anxiety on Switching Hesitation

### Source Input
```yaml
sources:
  - id: interview-01
    type: interview
    text: "We evaluated a SaaS reporting service last month and liked the demo, but we hesitated to sign up and stayed with our spreadsheets."
```

### Generated Interview Guide Output

## 💬 What to Ask Next

"What were you or your team most worried about on the day you decided not to sign up for the SaaS reporting service?"

### Why This Question Matters
The customer reached the active evaluation stage (`decision`), but an unmitigated anxiety or constraint blocked adoption. Identifying the specific risk (e.g., security, compliance, data loss, cost) reveals the real adoption barrier.

### If the Answer Is Vague
"Was there a specific person who raised a concern, or a policy requirement that came up during the evaluation?"

### ⚠️ What NOT to Ask Right Now
"Don't you think the automated features are worth the small monthly subscription cost?" *(Avoid defending the solution or arguing value with the interviewee!)*

---

### 📊 Structured Metadata

```yaml
analysis_status: evidence_extracted

interview_focus: decision

timeline_summary:
  first_thought: "Evaluated SaaS reporting service last month."
  passive_looking: "Liked the demo."
  active_looking: "Evaluated service."
  decision: "Hesitated and chose to stay with spreadsheets."
  first_use: ""
  ongoing_use: ""

current_hypotheses:
  - id: HYP-002
    statement: "Unmitigated anxiety or security policy constraint blocked the final purchasing decision."
    status: unverified

evidence_gaps:
  - "Specific risk, compliance policy, or stakeholder concern that caused hesitation."

next_question_type: anxiety_probe
```
