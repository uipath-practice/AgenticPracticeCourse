# LLM with Context

**Ground your agent in real data to eliminate hallucinations**

---

## What You'll Build

In this phase you extend the basic categorization agent by anchoring its responses to actual incident information. Without grounding, the LLM may generate plausible-sounding but incorrect category assignments. With context, the agent's decisions are traceable to real data.

## Key Concept: Data Anchoring

Data anchoring means providing the LLM with structured, factual context before asking it to make a decision. Instead of:

> "Here is an incident description. Categorize it."

You send:

> "Here is an incident description. Here is the relevant data from our incident history and category definitions. Based only on this data, categorize the incident."

This constrains the model's output space to what is factually supported.

## Steps

<!-- Add step-by-step instructions here as you migrate from the original site -->

!!! note "Content migration in progress"
    Detailed steps and screenshots will be added here. In the meantime, refer to the [original training site](https://sites.google.com/uipath.com/tpenlabs/home).

## What to Expect

After completing this phase, your agent will:

- Pull incident context before generating a response
- Base categorization decisions on actual data rather than inference
- Produce more consistent, auditable results

[← Back to Overview](index.md) | [Next: Tools and Escalations →](tools-and-escalations.md)
