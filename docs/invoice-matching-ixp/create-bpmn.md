# Step 1 — Create BPMN Process

**Design the IXP-enhanced workflow**

---

## Goal

Create the BPMN diagram for the IXP-based invoice matching process. This version differs from the standard process by including the IXP extraction step and the confidence-based branching logic.

## Key Differences from Standard Process

The IXP process adds:

- An explicit **extraction step** after the robot delivers the invoice PDF
- A **confidence gate**: high-confidence results flow to automated matching, low-confidence results route to human review
- A **human review task** specifically for validating extracted data (not just matching decisions)

## Steps

<!-- Add step-by-step instructions here as you migrate from the original site -->

!!! note "Content migration in progress"
    Detailed steps and screenshots will be added here. In the meantime, refer to the [original training site](https://sites.google.com/uipath.com/tpenlabs/home).

[← Back to Overview](index.md) | [Next: Configure a Robot →](configure-robot.md)
