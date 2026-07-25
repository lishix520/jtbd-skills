# Real-World Demo 1: Evaluating a Pure Product Idea ("AI Diary App")

This demo illustrates how **`opportunity-discovery`** handles a raw product idea with zero customer facts. Instead of making a speculative binary prediction or validating the idea blindly, the system identifies evidence gaps and provides a non-leading interview plan.

---

## 📥 User Input
> "I want to build an AI diary app that automatically transcribes and organizes my daily thoughts."

---

## 📋 Generated Opportunity Decision Brief

## 📋 Opportunity Decision Brief

### 🚦 Current Assessment
- **Readiness Stage**: `Idea only`
- **Current Assessment**: Do not start product development yet. The proposal is an unverified solution idea with zero direct customer facts. Validate whether a real, recurring journaling friction exists.
- **Confidence Rating**: `low`

### ✅ What is Known (Direct Evidence)
- **Direct Evidence**: None. No customer quotes, observed workarounds, or behavior logs have been provided.

### 💡 What is Only a Hypothesis
- Users experience significant friction manually keeping a diary.
- An AI transcription and auto-organization feature is the preferred solution.
- Users are willing to switch solutions or pay for an AI diary application.

### 🔍 What You CAN and CANNOT Conclude Right Now
- **CAN Conclude**: You have formulated a clear product vision to test.
- **CANNOT Conclude**: Market demand, willingness to pay, switching motivation, or current workaround pain cannot be determined.

### 🚀 Recommended Smallest Next Validation Step
"Interview 5 target users who actively kept a journal or diary in the past 30 days. Ask about the last time they wrote or recorded a entry, what tools they used, and where they got stuck."

---

### 📊 Structured Decision Brief Metadata

```yaml
decision_brief:
  current_stage: idea_only
  evidence:
    direct: []
    inferred: []
  hypotheses:
    - "Users experience friction keeping a manual diary."
    - "AI auto-organization is the desired solution."
  unknowns:
    - "Target user segment"
    - "Current journaling workarounds"
    - "Willingness to pay or switch"
  current_assessment: "Do not start development yet; validate problem existence and current workarounds."
  confidence: low
  what_you_can_conclude_now:
    - "Product hypothesis statement formulated."
  what_you_cannot_conclude_yet:
    - "Market demand, willingness to pay, or switching motivation."
  recommended_action: "Conduct 5 qualitative discovery interviews using non-leading past-behavior probes."
  smallest_next_validation_step: "Interview 5 people who actively kept a diary in the past 30 days."
  recommended_skill: "jtbd-switch-interview"
```
