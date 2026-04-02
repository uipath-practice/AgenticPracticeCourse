# Categorizing Technical Support Incidents

**Build an intelligent ServiceNow incident triage agent for ticket routing**

---

## Overview

**UiPath Agent Builder** is a vital tool designed to empower users in the development of intelligent automation solutions with minimal coding experience. It facilitates the creation, design, and deployment of agents that can perform various tasks, such as invoking automations, utilizing APIs, and collaborating with other systems seamlessly. 

By offering a low-code environment, Agent Builder democratizes access to automation capabilities, enabling both technical and non-technical users to craft powerful, context-driven agents tailored to their unique operational needs. 

In this exercise you'll use **UiPath Agent Builder** to create an agent that automatically categorizes and routes ServiceNow incidents. You'll learn how to ground decisions in real data, validate performance with automated tests, and connect your agent to live systems.

The progression unfolds in a few steps:

- First, you'll teach the agent to categorize incidents based on static descriptions and test it with sample inputs to observe LLM behavior.

- Then, you'll use **Context Grounding** to refine results and validate performance with **Evaluations**.

- Next, you'll "grow the agent's hands" by connecting it to **ServiceNow** using **Integration Service** so it can retrieve incident details and update tickets based on its analysis.

- Finally, you'll configure **Escalations** so the agent can route uncertain cases to humans via **Action Center**.

By the end, you'll have a fully functional, production-ready triage agent. Let's get started!


## Steps

| Step | Focus |
| ---: | :--- |
| [**LLM with Context**](llm-with-context.md) | Ground your agent in real incident data to eliminate hallucinations. Create an agent that analyzes incident descriptions, anchors decisions to structured context, and validates performance with evaluation sets. |
| [**Tools and Escalations**](tools-and-escalations.md) | Connect your agent to ServiceNow's live API and implement escalation workflows. Retrieve incident details from real systems, update tickets with categorization decisions, and route ambiguous cases to human reviewers via Action Center. |

!!! tip "Training Environment"
    Log in at **[cloud.uipath.com/tpenlabs](https://cloud.uipath.com/tpenlabs)** and remember using tenant **AgenticPractice** for this exercise.