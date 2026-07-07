# Creating a Conversational Agent with Autopilot

!!! tip "Here is our plan for this lesson:"

    1. Create a new conversational agent in **Studio Web**
    2. Let **Autopilot** generate a system prompt from your agent's purpose description
    3. Review the tools and context that Autopilot discovered
    4. Connect a **Context Grounding index** to ground the agent's responses

## Goal

You'll create a working conversational agent that answers questions about invoices and ServiceNow tickets from previous exercises. **Autopilot** will analyze your description, automatically wire up available tools, and generate a system prompt that guides the agent's behavior. By the end, your chatbot-agent will be grounded in real data and documentation, preventing hallucinated answers.

## Why Autopilot Matters

Configuring an agent from scratch can feel overwhelming. You need to choose the right tools, write clear instructions, and ensure everything works together. **Autopilot** handles the heavy lifting: it reads your natural-language description, scans **Orchestrator** for available tools and context sources, and generates a system prompt that brings it all together. Review the result and adjust — manually or via the Autopilot chat.

## Steps

### 1. Open Studio Web and create a new agent


[[[
In **Studio Web**, click the blue **Create New** button in the top-right corner. From the dropdown, select **Agent** to create a new solution.
|30|
![Studio Web Create New menu with Agent option highlighted](1-create-agent.images/1-create-new-menu.png){ .screenshot }
]]]

### 2. Select the Conversational agent type

A wizard appears asking what kind of agent you want to build. 

[[[
![Agent type selection showing Conversational option with description field](1-create-agent.images/2-select-conversational-type.png){ .screenshot }
|70|

Choose **Conversational** — this type is designed for interactive dialogue where the agent answers user questions via continuous dialogue.

In the description field, tell **Autopilot** what your agent should do:

```text
This conversational agent that will use available tools from UiPath Orchestrator and context grounding indexes to answer various questions about: Invoice processing documents, ServiceNow incidents and associated Orchestrator Jobs.
```
]]]

This description guides **Autopilot** when generating your system prompt. Be specific: mention the domain (invoices, jobs), and hint at the tools or context you expect. It's also practical to define which areas the agent should not focus on and mention other constraints.

Click **Generate Agent** to let **Autopilot** analyze your setup.

!!! tip "Best practice"
    Delegate tasks to the most qualified entity. For prompt writing, that entity is… the thing that reads prompts all day.  

### 3. Watch Autopilot discover tools and context

While **Autopilot** runs, it:

- Scans your **Orchestrator** for available tools
- Identifies context sources (like **Context Grounding indexes**)
- Analyzes your description to decide what's relevant

![Autopilot analysis in progress, showing successful discovery of tools and context](1-create-agent.images/3-autopilot-analyzing.png){ .screenshot width="800" }

**Autopilot** displays a list of tools it found in your **Orchestrator**. Review the list carefully. Each tool represents an RPA process, API, or other automation your agent can invoke.

![List of available tools discovered by Autopilot, with Accept button highlighted](1-create-agent.images/4-available-tools.png){ .screenshot width="800" }

Click **Accept** to confirm these tools will be available to your agent. Notice that you can only see tools you have permission to use, based on Orchestrator's role-based access controls (RBAC). When you publish and run this automation, the robot user needs those same permissions — otherwise tool calls will fail.

### 4. Review the generated system prompt

**Autopilot** has now created a complete system prompt. This prompt defines:

- **Role** — what the agent is (e.g., "You are an invoice and job query specialist")
- **Tool Rules** — when and how to use each available tool
- **Domain constraints** — what the agent should and shouldn't do

!!! tip 
    The system prompt is the agent's functional guide and job description. A well-written prompt is the difference between helpful and hallucinating.


![System prompt editor on the left, Autopilot Preview on the right showing the generated prompt](1-create-agent.images/5-review-system-prompt-W.png){ .screenshot width="900" }

[[[
If the prompt looks good, click **Accept** to confirm. 

You will be able to edit it later.
|50|
![Final confirmation dialog with agent behavior guidelines](1-create-agent.images/6-confirm-behavior.png){ .screenshot }
]]]

### 5. Add Context Grounding indexes

Just to make it complete, let's add data from some existing indexes. With context, conversational agents will be able to cite sources, which is very useful for a chatbot automation reading long complex documents.

On the **agent canvas** click the **+** icon under **Context** on the Agent node to add a knowledge source.

![Agent canvas showing Context connection point with the add button highlighted](1-create-agent.images/7-add-context.png){ .screenshot width="800" }

A right-side panel opens showing available context sources. Search for "security" to find the **UiPath Security data** index containing very comprehensive documentation about UiPath platform. A few topics you could inquire about will include: **data encryption, role based access controls, agentic security, data residency**.

- Download the source file if you want to keep it: [UiPath Security Whitepaper.pdf](../assets/UiPath Security Whitepaper.pdf)
- Explore more interesting whitepapers and learn about UiPath platform security in [UiPath Trust Portal](https://trust.uipath.com/) and [UiPath Security page](https://www.uipath.com/legal/trust-and-security/security)

### 6. Configure how the agent retrieves from the index

[[[
After selecting the index, a configuration form appears. 

These settings control how the agent searches and retrieves information. 

Use simple semantic search. You can increase the relevance threshold to 0.3–0.5 to narrow down results — useful for large documents like this one.

Your agent is now fully configured.
|50|
![Index configuration form showing all retrieval settings](1-create-agent.images/8-configure-context-W.png){ .screenshot width="900" }
]]]

### 7. Review the complete agent configuration

Your agent is now wired with tools and context, it's ready to answer questions. You can see the full picture on the canvas.

![Complete agent configuration showing context and tools connected to the central Agent node](1-create-agent.images/9-complete-agent-W.png){ .screenshot width="900" }


[[[
Don't forget to give it a meaningful name, as usually:
|50|
![Conversational Agent component expanded in the solution Explorer](1-create-agent.images/10-agent-in-explorer.png){ .screenshot }
]]]


!!! tip "Tip of the day"
    It’s important to arrange all tools like tentacles, as shown. This allows the agent to multitask efficiently - and just like a real octopus, it can regrow any tentacle when a tool call fails. Even better, this **agentic octopus** can grow new tentacles over time, continuously expanding its reach. And yes, this is just an attention check which means you can pick any other animal to mimic its natural benefits with the agent!

Your agent is now ready to test. But let's not rush - in the next lesson, you'll explore the tools it can use and understand how they work.