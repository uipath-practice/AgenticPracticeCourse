# Tools and Escalations

**Route complex cases to humans via Action Center**

---

## What You'll Build

In this final phase you implement human escalation workflows. Not every incident can — or should — be handled automatically. This phase teaches you to recognize those cases and route them to the right people.

## Core Concept

Automation works best when it knows its own limits. An agent that escalates correctly is more valuable than one that confidently handles everything — including cases it shouldn't.

## Escalation Triggers

Configure your agent to escalate when:

- Categorization confidence is below a defined threshold
- The incident involves multiple potential categories with similar scores
- The incident description is ambiguous, incomplete, or contradictory
- Specific priority levels or impact categories require human review

## Action Center Integration

**Action Center** is the UiPath interface for human escalation. When your agent triggers an escalation:

1. A task is created in Action Center with the incident details
2. A human reviewer receives the task
3. The reviewer categorizes and resolves the task
4. The workflow continues with the human-provided decision

## Steps

<!-- Add step-by-step instructions here as you migrate from the original site -->

!!! note "Content migration in progress"
    Detailed steps and screenshots will be added here. In the meantime, refer to the [original training site](https://sites.google.com/uipath.com/tpenlabs/home).

## What to Expect

After completing this phase, your agent will:

- Automatically handle clear-cut incidents
- Escalate ambiguous or high-risk cases to humans
- Resume the workflow once human input is received

[← Back to Overview](index.md)
