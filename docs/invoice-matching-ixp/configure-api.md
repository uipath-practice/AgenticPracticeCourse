# Step 5 — Configure API Integration

**Connect to external systems**

---

## Goal

Complete the IXP-enhanced process by adding API integrations that connect Maestro to the external systems needed to retrieve PO data and post matching results.

## API Connections in This Process

| Integration | Purpose |
|-------------|---------|
| ERP / PO system | Read Purchase Order details for matching |
| Invoice system | Post matching decisions (approved/rejected) |
| Notification system | (Optional) Alert stakeholders of exceptions |

## Steps

<!-- Add step-by-step instructions here as you migrate from the original site -->

!!! note "Content migration in progress"
    Detailed steps and screenshots will be added here. In the meantime, refer to the [original training site](https://sites.google.com/uipath.com/tpenlabs/home).

## What You've Built

After completing all five steps, your IXP-enhanced process:

- **Robot** retrieves invoice PDFs from source
- **Agent + IXP** extracts structured data with confidence scoring
- **Human validation** corrects low-confidence extractions
- **Agent** queries ERP, validates, and makes matching decisions
- **API calls** post results and trigger downstream actions

[← Step 4: Configure Human Validation](configure-human-validation.md) | [Back to Overview](index.md)
