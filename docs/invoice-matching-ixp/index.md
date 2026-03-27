# Invoice Matching with IXP

---

**UiPath Maestro** helps transform workflow designs into scalable, production-ready solutions and enables agentic orchestration — coordinating long-running enterprise processes between humans, robots, and AI agents across different systems of record and systems of engagement. 

In addition to that, this exercise will use **IXP** (**I**ntelligent e**X**traction & **P**rocessing) for invoice data extraction from PDF documents. 

Here is the plan:

| Step | Focus |
| :---: | :--- | 
| [**Create BPMN Process**](create-bpmn.md) | Design the end-to-end workflow for the process |
| [**Configure a Robot**](configure-robot.md) | RPA job to retrieve the invoice PDF document |
| [**Configure an Agent**](configure-agent.md) | Extract data from Invoice using IXP, look up the Purchase Order, Perform Matching and help making decision |
| [**Configure Human Validation**](configure-human-validation.md) | Customized Action App designed to help Humans handling exceptions in Action Center |
| [**Configure API Integration**](configure-api.md) | Send notification emails and store approved invoices for further processing |

!!! tip "Training Environment"
    Log in at [cloud.uipath.com/tpenlabs](https://cloud.uipath.com/tpenlabs) and remember using tenant **AgenticPractice** for this exercise.
