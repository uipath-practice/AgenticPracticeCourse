# Invoice Matching with IXP

**Build an end-to-end 2-way matching process using IXP, Robots, an AI Agent, and human review.**

## Overview

**UiPath Maestro** enables agentic orchestration — coordinating long-running enterprise processes between humans, robots, and AI agents across different systems of record and engagement. This exercise adds **IXP** (Intelligent eXtraction & Processing) to the mix, using it to extract structured invoice data from PDF documents.

| Step | Focus |
| ---: | :--- |
| [**Create BPMN Process**](1-create-bpmn.md) | Design the end-to-end workflow for the process |
| [**Configure a Robot**](2-configure-robot.md) | RPA job to retrieve the invoice PDF document |
| [**Configure an Agent**](3-configure-agent.md) | Extract invoice data using IXP, look up the Purchase Order, and run 2-way matching |
| [**Configure Human Validation**](4-configure-human-validation.md) | Action App in Action Center for human review of invoice exceptions |
| [**Configure API Integration**](5-configure-api.md) | Send rejection emails and store approved invoices for payment processing |

!!! tip "Training Environment"
    Log in at **[cloud.uipath.com/tpenlabs](https://cloud.uipath.com/tpenlabs)** and remember using tenant **AgenticPractice** for this exercise.
