# Step 4 — Configure Human Validation

**Handle low-confidence escalations**

---

## Goal

Configure the human validation step that activates when IXP extraction confidence falls below your defined threshold.

## When Humans Are Needed

In the IXP workflow, human validation covers two scenarios:

1. **Low-confidence extraction** — one or more fields were extracted with low confidence; a human verifies or corrects the extracted data before matching proceeds
2. **Matching exceptions** — after extraction, the agent cannot make a clear match/reject decision

## The Human Task

In Action Center, the reviewer sees:

- The original PDF invoice (for reference)
- The IXP-extracted values with confidence scores highlighted
- Fields flagged for review
- Form fields to confirm or correct each value

Once submitted, the corrected data flows back into the process and the agent proceeds with matching.

## Steps

<!-- Add step-by-step instructions here as you migrate from the original site -->

!!! note "Content migration in progress"
    Detailed steps and screenshots will be added here. In the meantime, refer to the [original training site](https://sites.google.com/uipath.com/tpenlabs/home).

[← Step 3: Configure an Agent](configure-agent.md) | [Next: Configure API Integration →](configure-api.md)
