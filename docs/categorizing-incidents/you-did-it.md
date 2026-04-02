# You did it!

!!! tip "Congratulations!"

    You've built a fully functional ServiceNow incident categorization agent — grounded in real data, connected to live systems, and capable of routing ambiguous cases to humans.

---

## What you built

Your agent takes an Incident Number, retrieves the full ticket from **ServiceNow**, categorizes it using a grounded context source, looks up the right assignee, and writes the result back — without a single line of code. When a ticket is too vague to classify, it escalates to a human in **Action Center** and resumes once the reviewer decides.

| Component | Role |
|-----------|------|
| **Agent** | Analyzes incident descriptions, categorizes them using context, and orchestrates the end-to-end workflow |
| **Context Grounding** | Anchors category and subcategory decisions to a valid data source, eliminating hallucinations |
| **Assignee Lookup tool** | RPA workflow that retrieves the on-duty expert email for a given category/subcategory pair |
| **Search Incidents tool** | Integration Service activity that fetches live incident details from **ServiceNow** by Incident Number |
| **Update Incident tool** | RPA workflow that writes categorization results back to the ServiceNow ticket |
| **Escalation** | Routes unclassifiable incidents to a human reviewer in **Action Center** and resumes on their decision |
| **Evaluations** | Regression tests that validate multiple categorization scenarios against expected outputs |

---

## Next steps

### 1. Run your agent on live incidents

Your agent is ready to run on demand. Publish the solution to your **Personal Workspace** and trigger it from **Orchestrator**, passing a real Incident Number as input.

- Open the solution in **Studio Web**
- Publish to your **Personal Workspace**
- Trigger a run from **Orchestrator** and pass a live incident number
- Review the Execution Trace in **Agent Builder** to verify every step — retrieval, categorization, lookup, and update

### 2. Connect to an automated trigger

Instead of running manually, wire your agent to a trigger so it fires whenever a new incident arrives.

- In **Orchestrator**, set up a time-based trigger or a queue
- Use the Incident Number as the queue item payload
- Watch the agent process tickets without manual input

---

## Keep iterating

**Tune the confidence threshold**

- Open the Context Grounding settings and lower the confidence threshold.
- Watch previously confident categorizations start escalating instead.
- Raise it and observe more aggressive auto-classification — sometimes at the cost of accuracy.
- Finding the right balance is a key part of production agent design.
- Refine the list of categories and descriptions to reduce ambiguity.

**Improve the system prompt**

- The current prompt escalates anything ambiguous. Try adding a fallback rule before escalation — for example, pick the closest category but flag it in `ExecutionDetails`.
- Add examples in the system prompt for categories that are easy to confuse (e.g., *Software / Email* vs *Network / DNS*).
- Re-run the Evaluation set after each change to measure the impact.

**Expand the agent**

- Add a second context source for a different ServiceNow table, such as Change Requests.
- Introduce priority routing: high-priority incidents skip normal categorization and escalate immediately.
- Add a post-escalation audit step that logs every human override — useful training data for future prompt improvements.

The skills you practiced here — context grounding, tool integration, escalation design, prompt iteration, and regression testing with Evaluations — are the core building blocks of production-ready agentic automation. Keep experimenting. Change the prompts. Break things. Fix them.

---

## Learn more

| Resource | Description |
|----------|-------------|
| [Building an agent in Studio Web](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/building-an-agent-in-studio-web) | Step-by-step reference for creating, configuring, and publishing agents |
| [Agent Tools](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/agent-tools) | How to connect Integration Service activities, RPA workflows, and other tools |
| [Agent Contexts](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/agent-contexts) | How Context Grounding works and how to configure data sources |
| [Agent Evaluations](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/agent-evaluations) | Running regression tests to validate agent performance across scenarios |
| [Agent Escalations and Memory](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/agent-escalations-and-agent-memory) | Configuring escalation paths and handling human-in-the-loop decisions |
| [Agent Prompts](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/agent-prompts) | System and user prompt structure, best practices, and prompt variables |
