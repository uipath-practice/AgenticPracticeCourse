# Step 4 — Add a Human

**Configure validation and escalation checkpoints**

---

## Goal

Add human intervention points to handle cases the agent flags as exceptions — invoices where automatic matching confidence is low, amounts exceed approval thresholds, or discrepancies require review.

## When Humans Are Needed

Automate the routine; escalate the exceptions. Humans are brought in when:

- Invoice and PO data don't match cleanly
- The agent's confidence in a decision is below threshold
- Invoice amounts exceed an automatic approval limit
- The invoice references a PO that can't be found

## Action Center Integration

Human tasks appear in **Action Center**, where reviewers can:

- See the invoice and matched PO data side-by-side
- Approve or reject the match
- Add notes explaining the decision
- Route to additional approvers if needed

The workflow resumes automatically once the human task is completed.

## Steps

<!-- Add step-by-step instructions here as you migrate from the original site -->

!!! note "Content migration in progress"
    Detailed steps and screenshots will be added here. In the meantime, refer to the [original training site](https://sites.google.com/uipath.com/tpenlabs/home).

[← Step 3: Add an Agent](add-agent.md) | [Next: Add API Calls →](add-api.md)
