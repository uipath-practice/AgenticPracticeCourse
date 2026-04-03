# You did it!

!!! tip "Congratulations!"

    You've built a conversational agent grounded in real documentation, extended it with live tools and an MCP server, and validated it with evaluations.

---

## What you built

You created a conversational agent in Agent Builder that answers UiPath Security questions using context grounding. You gave it access to Orchestrator job data and an external MCP server, then designed an evaluations dataset to validate its responses systematically.

| Component | Role |
|-----------|------|
| **Conversational Agent** | Answers questions in real time, scoped to grounded knowledge |
| **Context Grounding** | Anchors responses to UiPath Security documentation |
| **Orchestrator Tools** | Lets the agent retrieve live Job Details on demand |
| **MCP Server** | Provides external weather tools via the Model Context Protocol |
| **Evaluations** | Dataset-driven testing to validate agent response quality |

---

## Next steps

### 1. Deploy and share the agent

Publish your agent from Agent Builder and share the endpoint with a colleague. Try asking it questions outside the grounded scope — notice how it handles topics it shouldn't answer.

### 2. Review observability data

Open the agent's observability dashboard in Agent Builder. Check conversation logs and see which tools were called and how often.

---

## Keep iterating

**Broaden the knowledge base**

- Add more documentation indexes to the context grounding source and observe how the agent's coverage changes.

**Add more Orchestrator tools**

- Connect additional tools — like Get Process details or List Assets — and test whether the agent picks the right tool for each question.

**Design a tougher evaluations dataset**

- Include adversarial questions, edge cases, and ambiguous phrasing. See where the agent's score drops and use that to refine the system prompt.

---

## Learn more

| Resource | Description |
|----------|-------------|
| [Conversational Agents](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/conversational-agents) | Overview of conversational agents in UiPath Agent Builder |
| [Getting Started](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/conversational-agents-getting-started) | Step-by-step guide to creating your first conversational agent |
| [Agent Design](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/conversational-agents-design) | Prompt configuration, tools, and grounding options |
| [Deployment](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/conversational-agents-deployment) | How to publish and share a conversational agent |
| [Observability](https://docs.uipath.com/agents/automation-cloud/latest/user-guide/conversational-agents-observability) | Monitoring conversations and tool usage |
| [MCP Servers in Orchestrator](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/about-mcp-servers) | What MCP servers are and how they integrate with UiPath |
| [Managing MCP Servers](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-mcp-servers) | Register, configure, and govern MCP servers in Orchestrator |
| [Managing Indexes](https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/managing-indexes) | Setting up documentation indexes for context grounding |
