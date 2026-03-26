# Categorizing Incidents

**Build an intelligent ServiceNow incident triage agent**

---

## Overview

In this exercise you'll use **UiPath Agent Builder** to create an agent that automatically categorizes and routes ServiceNow incidents. You'll progress through five phases, each adding a new capability layer.

## Five-Phase Learning Path

### Phase 1 — Basic Agent
Create a foundational categorization agent using system prompts. The agent analyzes incident descriptions and assigns categories without any external data sources.

**You'll learn:**
- Agent Builder basics
- Writing effective system prompts for categorization
- Testing agent responses

---

### Phase 2 — LLM with Context
[Ground your agent](llm-with-context.md) in real incident data to eliminate hallucinations. Instead of relying solely on the LLM's general knowledge, you'll provide structured context from your incident database.

**You'll learn:**
- Data-anchoring techniques
- Preventing AI-generated assumptions
- Feeding structured data into prompts

---

### Phase 3 — Evaluations
Deploy an evaluation framework to systematically test your agent's performance across a standardized collection of test cases.

**You'll learn:**
- Building test case collections
- Running batch evaluations
- Measuring and improving categorization accuracy

---

### Phase 4 — Live System Integration
Connect the agent to ServiceNow's live API — retrieve incident details from real systems and post categorization decisions back.

**You'll learn:**
- API integration in Agent Builder
- Reading from and writing to ServiceNow
- Working with real operational data

---

### Phase 5 — Tools and Escalations
[Implement escalation workflows](tools-and-escalations.md) via Action Center. Route complex or ambiguous incidents to human reviewers when automated handling isn't appropriate.

**You'll learn:**
- Configuring Action Center escalations
- Designing human-in-the-loop decision points
- When (and how) to hand off to humans

---

## Platform

All exercises run in **UiPath Agent Builder**, a low-code environment that lets you create, design, and deploy agents without deep coding experience.

!!! tip "Training Environment"
    Log in at [cloud.uipath.com/tpenlabs](https://cloud.uipath.com/tpenlabs) using tenant **AgenticPractice**.
