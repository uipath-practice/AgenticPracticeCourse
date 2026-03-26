# UiPath Agentic Practice Workshop

**Learner's Handbook** — a practical guide for hands-on exercises

---

!!! info "Training Environment"
    - **Platform:** [cloud.uipath.com/tpenlabs](https://cloud.uipath.com/tpenlabs)
    - **Tenant:** AgenticPractice
    - **Contact:** sergey.shumilov@uipath.com

## What You'll Build

This workshop guides you through building real agentic automation solutions on the UiPath Platform. You'll work through two main use cases, each progressively adding intelligence and orchestration complexity.

### Core Principle

> Focused, domain-specific AI solutions consistently outperform general-purpose chatbots.

The exercises apply software engineering discipline — structured process design, systematic testing, and incremental iteration — to AI automation projects.

---

## Exercises

### 1. Categorizing Incidents
Build an intelligent ServiceNow incident triage agent, progressing through five phases:

| Phase | Focus |
|-------|-------|
| Basic agent | Foundational categorization using system prompts |
| LLM with Context | Ground the agent in real incident data to eliminate hallucinations |
| Evaluations | Test performance across standardized test cases |
| Live Integration | Connect to ServiceNow API — read and write real incidents |
| Tools & Escalations | Route complex cases to humans via Action Center |

[Start Exercise →](categorizing-incidents/index.md)

---

### 2. Invoice Matching Automation
Build a multi-component process combining AI agents, robots, human validation, and API integrations using **Maestro** orchestration.

[Start Exercise →](invoice-matching/index.md)

---

### 3. Invoice Matching with IXP
Extend the invoice matching workflow with **Intelligent eXtraction & Processing** for automated data extraction from PDF invoices with confidence-based escalation.

[Start Exercise →](invoice-matching-ixp/index.md)

---

## Key Concepts

**Agent Builder** — Low-code environment for creating, designing, and deploying agents.

**Maestro** — UiPath's orchestration platform for coordinating humans, robots, and AI agents across long-running enterprise processes.

**IXP (Intelligent eXtraction & Processing)** — Document processing technology with confidence scoring for automated data extraction from unstructured documents.

**Action Center** — UiPath interface for human escalation workflows, exception handling, and manual review.
