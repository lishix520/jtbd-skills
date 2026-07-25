# Invalid Switch Interview Guide Examples & Corrections

This document details 4 major **anti-patterns and invalid interview guidance attempts**. Each example illustrates an invalid interview output, the specific rule violation, and how to correct it.

---

## Anti-Pattern 1: Asking Leading Feature Specification Questions

### Source Excerpt
> "I really need a Jira button that automatically creates my weekly status report."

### Invalid Interview Guidance Attempt
```markdown
# ❌ INCORRECT GUIDANCE
## What to Ask Next
"Great! What fields would you like on the Jira button, and what format should the generated report be in?"
```

### Rule Violation
- **Leading Feature Design Discussion**: Discussing feature mechanics ("What fields would you like?") validates an unproven solution design and fails to uncover the customer's actual situational trigger or current workaround.

### Correct Interview Guidance
```markdown
# ✅ CORRECT GUIDANCE
## 💬 What to Ask Next
"Tell me about the last time you needed to create your weekly status report—what was happening right before you started, and how did you compile it?"

### ⚠️ What NOT to Ask Right Now
"What fields or options would you like us to put on the Jira button?"
```

---

## Anti-Pattern 2: Asking Speculative Future Purchasing Questions

### Source Excerpt
> "I spend two hours every Thursday combining spreadsheets from my team."

### Invalid Interview Guidance Attempt
```markdown
# ❌ INCORRECT GUIDANCE
## What to Ask Next
"If we built an automated reporting tool that saved you those two hours, would you buy it for $50/month?"
```

### Rule Violation
- **Speculative Future Bias**: Customers are notoriously inaccurate when predicting future purchasing behavior ("Would you buy..."). Interviews must anchor on past behavior ("When was the last time you searched for a tool?").

### Correct Interview Guidance
```markdown
# ✅ CORRECT GUIDANCE
## 💬 What to Ask Next
"The last time spreadsheet compilation took two hours, did you look for another way or tool to speed it up?"

### ⚠️ What NOT to Ask Right Now
"Would you pay $50/month for an automated reporting tool?"
```

---

## Anti-Pattern 3: Overloading the User with a Wall of Questions

### Source Excerpt
> "We are looking for a better way to handle status updates."

### Invalid Interview Guidance Attempt
```markdown
# ❌ INCORRECT GUIDANCE
## Questions to Ask
1. What tool do you use?
2. How many people are on your team?
3. Who approves the budget?
4. How long have you used spreadsheets?
5. What features do you need?
6. When is your next deadline?
7. Have you tried Jira?
... (15 questions in a wall of text)
```

### Rule Violation
- **Interviewer Overload**: Dumping 15 questions forces the user to mechanically read a questionnaire, ruining natural discovery. Provide **ONE primary question** to speak out loud.

### Correct Interview Guidance
```markdown
# ✅ CORRECT GUIDANCE
## 💬 What to Ask Next
"What was the specific event that made your team decide it was time to look for a better way to handle status updates?"
```

---

## Anti-Pattern 4: Arguing Solution Value with the Customer

### Source Excerpt
> "We looked at a cloud reporting tool last month, but we hesitated to sign up because of security concerns."

### Invalid Interview Guidance Attempt
```markdown
# ❌ INCORRECT GUIDANCE
## What to Ask Next
"Don't you think the automated time savings outweigh the small security risk?"
```

### Rule Violation
- **Defending the Product / Arguing Value**: Trying to convince or debate the interviewee destroys neutral discovery and masks real adoption barriers (security policy).

### Correct Interview Guidance
```markdown
# ✅ CORRECT GUIDANCE
## 💬 What to Ask Next
"What specific security concern or policy requirement came up that caused the team to hesitate?"

### ⚠️ What NOT to Ask Right Now
"Don't you think the automated time savings outweigh the security risk?"
```
