# Step 3 — Configure an Agent

**Extract, query, validate, and decide**

---

## Goal

Configure the agent to perform three critical functions using IXP:

1. **Extract** invoice data from PDFs using IXP with confidence-based escalation
2. **Query** the ERP system for the corresponding Purchase Order data
3. **Validate** and **decide** — match, reject, or escalate

## IXP Extraction

When the agent receives a PDF invoice, it uses IXP to extract structured data:

- Vendor name and ID
- Invoice number and date
- Line items (description, quantity, unit price)
- Total amount
- Referenced PO number

Each extracted field includes a **confidence score** (0–100%). You'll configure a threshold — fields below the threshold trigger escalation.

## Confidence-Based Logic

```
For each extracted field:
  IF confidence >= threshold:
    → Proceed with extracted value
  ELSE:
    → Flag for human review
```

## ERP Query

Once extraction is complete (or after human correction of low-confidence fields), the agent queries the ERP for the Purchase Order referenced on the invoice.

## Matching Decision

The agent compares:
- Invoice vendor → PO vendor
- Invoice line items → PO line items
- Invoice total → PO total (within tolerance)

Result: **Match**, **Reject**, or **Escalate for review**

## Steps

<!-- Add step-by-step instructions here as you migrate from the original site -->

!!! note "Content migration in progress"
    Detailed steps and screenshots will be added here. In the meantime, refer to the [original training site](https://sites.google.com/uipath.com/tpenlabs/home).

[← Step 2: Configure a Robot](configure-robot.md) | [Next: Configure Human Validation →](configure-human-validation.md)
