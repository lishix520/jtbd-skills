# Real-World Demo 2: Feature Request Redirect ("PDF Export Button")

This demo illustrates how **`opportunity-discovery`** handles a recurring customer feature request. Rather than treating the feature request as proof of a validated product requirement, the system isolates the feature proposal, identifies the underlying workflow uncertainty, and routes to context exploration.

---

## 📥 User Input (Customer Support Tickets & Feedback Quotes)
> 1. "Please add a PDF export button to the project dashboard so I can share updates."
> 2. "I spend 45 minutes every Thursday taking screenshots of project widgets to paste into PowerPoint for our executive review."
> 3. "We really need a 1-click PDF download for weekly status reports."

---

## 📋 Generated Opportunity Decision Brief

## 📋 Opportunity Decision Brief

### 🚦 Current Assessment
- **Readiness Stage**: `Anecdotal signal`
- **Current Assessment**: Do not commit to engineering a custom PDF export button yet. Customers are experiencing real time pressure compiling status information for executive reviews, but PDF export is only one possible solution design.
- **Confidence Rating**: `medium`

### ✅ What is Known (Direct Evidence)
- Customers spend up to 45 minutes every Thursday manually taking screenshots of dashboard widgets and pasting them into PowerPoint (Source: Quote 2).
- The activity is triggered by a recurring weekly executive status review.

### 💡 What is Only a Hypothesis
- A static PDF download button is the optimal or acceptable solution for executive reporting.
- Executive recipients will accept a raw dashboard PDF export without custom commentary or metric framing.

### 🔍 What You CAN and CANNOT Conclude Right Now
- **CAN Conclude**: Manual screenshotting and PowerPoint assembly creates recurring weekly workflow friction prior to executive reviews.
- **CANNOT Conclude**: Whether a PDF button solves the executive's needs, or if interactive link sharing / automated email summaries are superior.

### 🚀 Recommended Smallest Next Validation Step
"Interview 3 recent requesters. Ask: 'The last time you created a PowerPoint report for executive review, who received it, what specific metrics did they look at, and why wasn't a dashboard link sufficient?'"

---

### 📊 Structured Decision Brief Metadata

```yaml
decision_brief:
  current_stage: anecdotal_signal
  evidence:
    direct:
      - "Users spend 45 minutes every Thursday manually taking screenshots for PowerPoint status reports."
    inferred:
      - "Manual status reporting creates time pressure prior to Thursday executive meetings."
  hypotheses:
    - "A PDF export button is the required solution."
  unknowns:
    - "Executive recipient reporting requirements"
    - "Acceptable report formats"
  current_assessment: "Validate executive reporting requirements before building a PDF export feature."
  confidence: medium
  what_you_can_conclude_now:
    - "Weekly status compilation creates significant manual effort."
  what_you_cannot_conclude_yet:
    - "Whether a PDF button satisfies executive report recipients."
  recommended_action: "Pass customer quotes to jtbd-context-explorer to extract full workflow constraints."
  smallest_next_validation_step: "Interview 3 report creators to understand executive recipient metric requirements."
  recommended_skill: "jtbd-context-explorer"
```
