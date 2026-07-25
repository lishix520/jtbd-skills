# Find opportunities people will pay for.

JTBD Skills helps you find market opportunities, build products and services that sell better, and make more money.

Use it to:
- Find unmet needs
- Decide whether an idea is worth pursuing
- Improve an existing product or service
- Understand why customers choose, switch, or stay
- Find what customers will pay more for
- Decide what to do next

[中文说明 / Chinese Section](#-找到人们愿意付钱的机会中文说明)

---

## 🎯 When You Can Use It

- **New Idea**: You have a new product idea, but aren't sure if anyone truly needs it
- **Feature Overload**: Users request many features, but you don't know which to build first
- **Sales Friction**: Products aren't selling well, and you need to understand why prospects aren't buying
- **Customer Churn**: Customers are leaving or not renewing, and you need to uncover why
- **Pricing Strategy**: You want to raise prices or launch a premium tier, but don't know if customers will pay
- **Growth Directions**: You're looking for new growth opportunities without relying on guesswork

---

## 💡 See How It Helps You

**Someone tells you:**

> "I spend two hours every Friday manually copying updates into spreadsheets. I really wish Jira had a button to auto-generate weekly reports."

**Don't build the Jira feature right away. Ask first:**

> "Tell me about the last time that became a major pain—what was happening right before you started, and what took place between starting the report and sending it?"

**This helps you see clearly:**

- Where they actually get stuck in their workflow
- Why their current approach is no longer sufficient
- Whether this is a minor complaint or a problem worth solving
- What specific improvement they would actually pay for or switch solutions to adopt

---

## 🚀 Start Here

Paste any of the following into an AI tool supporting Agent Skills:

- A customer quote or feedback statement
- An interview transcript or discovery notes
- A negative or positive review
- A sales or customer support conversation
- A product, service, or feature idea you're evaluating

**Say directly to the AI:**

> *"Help me understand the underlying need behind this, and tell me what I should ask next."*

**Or:**

> *"I want to know if this idea is worth building. Tell me what evidence is missing, who to talk to, and how to validate it next."*

See full use cases and real-world demos: [examples/business-use-cases.md](./examples/business-use-cases.md) | [01-idea-only-ai-diary.md](./examples/01-idea-only-ai-diary.md) | [02-feature-request-pdf-export.md](./examples/02-feature-request-pdf-export.md) | [03-survey-opportunity-ranking.md](./examples/03-survey-opportunity-ranking.md)

---

## 🔍 Choose Based On Your Need

| What You Want To Do | What You Get | Underlying Skill |
| :--- | :--- | :--- |
| **I have a new idea or quote and need to decide what to validate next** | An Opportunity Decision Brief (stage, direct evidence, hypotheses, what CAN/CANNOT be concluded, smallest next step) | **`opportunity-discovery`** |
| **I don't know what to ask next** | One natural, non-leading follow-up question; why it matters; how to probe vague answers; what NOT to ask yet | `jtbd-switch-interview` |
| **I have customer feedback, but don't know what it means** | Distinction between current approaches, real-world circumstances, constraints, feature requests, and unverified assumptions | `jtbd-context-explorer` |
| **Users are unhappy, but still won't buy, switch, or renew** | Triggers causing change, inertia keeping them, anxiety about new solutions, and next validation steps | `jtbd-forces-analyzer` |

### 🛠️ Need something more specific?

- **Turn a feature request into a solution-free customer job** → `jtbd-job-definer`
- **Map a customer task from start to finish** → `jtbd-job-mapper`
- **Turn a pain point into measurable research questions** → `jtbd-outcome-engineer`
- **Rank needs using quantitative survey data** → `jtbd-opportunity-calculator`
- **Check whether you have enough evidence for a growth decision** → `jtbd-growth-strategist`

---

## 🛡️ Not Another Product-Analysis Prompt

JTBD Skills separates evidence, hypotheses, and unknowns.
When the evidence is not enough, it does not pretend to know the answer.
It tells you the smallest next step needed to make a better decision.

---

## 🌐 找到人们愿意付钱的机会。（中文说明）

JTBD Skills 帮你发现市场机会、做出更好卖的产品和服务，并赚到更多钱。

你可以用它来：
- 找到还没有被满足的需求
- 判断一个想法值不值得做
- 改进已有产品或服务
- 理解用户为什么选择、切换或留下来
- 找出客户愿意多付钱的价值
- 决定下一步该做什么

<details>
<summary><b>展开阅读中文详细指南与场景</b></summary>

### 🎯 你可以在这些时候用它

- **有新想法**：你有一个新想法，但不确定有没有人真的需要
- **功能繁杂**：用户提了很多功能需求，但你不知道该做哪个
- **销售受阻**：产品卖得不够好，想知道用户到底为什么不买
- **客户流失**：已有客户在流失，想知道他们为什么离开或不续费
- **尝试提价**：想提高价格、做新套餐或新服务，但不知道用户愿不愿意多付钱
- **寻找增长**：想找一个新的增长方向，却不想只凭感觉下注

### 💡 看看它怎么帮你

**有人对你说：**

> “我每周五都要花两小时把各团队的更新拼到表格里。真希望 Jira 能自动生成周报。”

**不要马上做 Jira 功能。先问：**

> “上一次你觉得这件事特别麻烦是什么时候？从开始整理到发出周报，中间发生了什么？”

**这能帮你看清：**

- 对方真正卡住的是哪一步
- 现在的做法为什么不够用
- 这是偶发抱怨，还是值得投入解决的问题
- 对方到底会为怎样的改进付钱或切换

</details>

---

## ⚙️ How It Works (Methodology Engine)

JTBD Skills combines two complementary research and innovation methodologies:

1. **Qualitative Context & Switching Forces (Christensen & Moesta Path)**:
   `opportunity-discovery` ──► `Context Explorer` ──► `Four Forces Analyzer` ──► `Switch Interview Guide`
   *Understand why people adopt, switch, stay, or leave.*

2. **Quantitative Underserved Needs & Strategy Matrix (Ulwick ODI Path)**:
   `opportunity-discovery` ──► `Job Definer` ──► `Job Mapper` ──► `Outcome Engineer` ──► `Opportunity Calculator` ──► `Growth Strategist`
   *Calculate Opportunity Scores and evaluate evidence-backed product and business strategy options.*

For complete architecture details, dual methodology pipelines, and stopping rules, see [ARCHITECTURE.md](./ARCHITECTURE.md).

---

## 🛠️ For Builders & AI-Agent Users

Browse the repository structure in the [GitHub file tree](./skills/).

---

### 📋 Skills Overview

| Skill Name | Scope | Status |
| :--- | :--- | :--- |
| **`principles`** | Cross-skill contract, terminology & evidence rules | `v0.5` |
| **`opportunity-discovery`** | Evidence-aware opportunity discovery & decision brief generator (Top-level Orchestrator) | `v0.5` |
| **`jtbd-switch-interview`** | Turn customer conversations into better business questions | `v0.5` |
| **`jtbd-context-explorer`** | Extract qualitative circumstances, progress, and non-consumption evidence | `v0.5` |
| **`jtbd-forces-analyzer`** | Organize switching evidence into Push, Pull, Habit, and Anxiety forces | `v0.5` |
| **`jtbd-job-definer`** | Extract, audit, and rewrite solution-free Core Functional Jobs | `v0.5` |
| **`jtbd-job-mapper`** | Deconstruct defined jobs into solution-free Universal Job Maps | `v0.5` |
| **`jtbd-outcome-engineer`** | Formulate formulaic Desired Outcome Statements for a job map step | `v0.5` |
| **`jtbd-opportunity-calculator`** | Compute quantitative ODI Opportunity Scores from survey ratings | `v0.5` |
| **`jtbd-growth-strategist`** | Map opportunity landscapes and market evidence to growth strategies | `v0.5` |

---

### 🧪 Verify the Repository

Clone the repository:

```bash
git clone https://github.com/lishix520/jtbd-skills.git
cd jtbd-skills
```

Run deterministic Opportunity Calculator calculation:

```bash
python3 skills/jtbd-opportunity-calculator/scripts/calculate_opportunity.py \
  integration/project-status-update/04-survey-input.json \
  > /tmp/calculated_out.json
```

Verify output against quantitative golden fixture:

```bash
diff -u /tmp/calculated_out.json \
  integration/project-status-update/05-opportunity-results.json
```

---

## 📄 License

MIT License. See [LICENSE](./LICENSE) for details.
