# Invoice Matching with IXP

**2-Way matching with Intelligent eXtraction & Processing**

---

## Overview

This exercise builds on the standard invoice matching process by adding **IXP (Intelligent eXtraction & Processing)** for automated data extraction from PDF invoices. IXP handles unstructured documents and provides confidence scores that drive automated escalation decisions.

## What IXP Adds

| Capability | Description |
|------------|-------------|
| **PDF extraction** | Reads and extracts data from unstructured invoice PDFs |
| **Confidence scoring** | Each extracted field gets a confidence score |
| **Automated escalation** | Low-confidence results automatically route to human review |

## How It Fits the Process

The full workflow:

```
Robot retrieves PDFs
  → Agent extracts data using IXP
      → High confidence: Agent queries ERP for PO data
          → Agent validates and decides (match/reject)
      → Low confidence: Escalate to human for review
  → API calls complete the process
```

## Five-Step Implementation

1. [**Create BPMN Process**](create-bpmn.md) — Design the IXP-enhanced workflow
2. [**Configure a Robot**](configure-robot.md) — Set up invoice PDF retrieval
3. [**Configure an Agent**](configure-agent.md) — Extract data, query ERP, validate, decide
4. [**Configure Human Validation**](configure-human-validation.md) — Handle low-confidence escalations
5. [**Configure API Integration**](configure-api.md) — Connect to external systems

---

!!! tip "Training Environment"
    Log in at [cloud.uipath.com/tpenlabs](https://cloud.uipath.com/tpenlabs) using tenant **AgenticPractice**.
