# Categorizing Technical Support Incidents

**Build an intelligent ServiceNow incident triage agent for ticket routing**

## Overview

**UiPath Agent Builder** is a vital tool designed to empower users in the development of intelligent automation solutions with minimal coding experience. It facilitates the creation, design, and deployment of agents that can perform various tasks, such as invoking automations, utilizing APIs, and collaborating with other systems seamlessly. 

By offering a low-code environment, Agent Builder democratizes access to automation capabilities, enabling both technical and non-technical users to craft powerful, context-driven agents tailored to their unique operational needs. 

In this exercise you'll use **UiPath Agent Builder** to create an agent that automatically categorizes and routes ServiceNow incidents. You'll build a complete system that analyzes technical incidents, grounds decisions in real data, and routes ambiguous cases to human reviewers.

The progression looks like this:

- First, we will teach agent to categorize incidents based on static descriptions. We will play with sample inputs to better understand LLM interactions, use the **Context Grounding** to finetune the results, and give it a thorough testing using **Evaluations** feature.

- Once categorization itself is working well - we will "grow agent's hands" by connecting it to **ServiceNow** using **Integration Service** so that it can retrieve incident details and update incident back to ServiceNow based on Agent's analysis. 

- Finally, if Agent is unable to categorize the Incident, it should be able to reach out to **Humans** using **Escalations** capability.

By the end, you'll have a fully functional, production-ready triage agent. Let's get started!


## Steps

| Step | Focus |
| ---: | :--- |
| [**LLM with Context**](llm-with-context.md) | Ground your agent in real incident data to eliminate hallucinations. Create an agent that analyzes incident descriptions, anchors decisions to structured context, and validates performance with evaluation sets. |
| [**Tools and Escalations**](tools-and-escalations.md) | Connect your agent to ServiceNow's live API and implement escalation workflows. Retrieve incident details from real systems, update tickets with categorization decisions, and route ambiguous cases to human reviewers via Action Center. |

!!! tip "Training Environment"
    Log in at **[cloud.uipath.com/tpenlabs](https://cloud.uipath.com/tpenlabs)** and remember using tenant **AgenticPractice** for this exercise.