# You did it!

!!! tip "Congratulations!"

    You've built a complete agentic invoice-matching process from scratch.

---

## What you built

Your process handles the full invoice lifecycle — from retrieving a PDF to routing the outcome — without any manual steps required for the happy path.

Summary:

| Component | Role |
|-----------|------|
| **Robot** | Retrieves an invoice PDF from the Storage Bucket |
| **AI Agent** | Extracts data with IXP, looks up the Purchase Order, and runs 2-way matching |
| **Human task** | Presents the mismatch summary in Action Center for review |
| **API connectors** | Sends the rejection email and stores approved records in Data Fabric |

This is a production-pattern process. The same design — Robot → Agent → Human → API — applies to a wide range of real-world document processing scenarios.

---

## Next steps

### 1. Publish and run your process from Maestro dashboard

Publish your completed process to your personal workspace, then run it as you would any other UiPath process.

- Open your solution in **Studio Web**
- Publish to your personal workspace
- Trigger a run from **Orchestrator** or **Maestro**
- Watch the execution trace end-to-end

### 2. Explore Maestro analytics

After a few runs, **Maestro → Analytics** shows:

- Transaction-level execution details
- End-to-end process flow visualization
- Exception and escalation rates

---

## Keep iterating

**Improve the agent prompt**
- The current prompt misses some edge cases — similar-but-not-identical line item descriptions, for example.
- Modify the system prompt and re-test with the same invoices.
- Measure how the matching decision changes.

**Test the boundaries**
- Set `in_FailureProbability` to different values and run multiple times.
- Deliberately submit an invoice with a missing PO ID and observe the escalation path.

**Expand the process**
- Add a second document type (e.g. credit notes).
- Introduce a new escalation path for high-value mismatches.
- Connect the approval path to an additional downstream system.

---

## Learn more

| Resource | Description |
|----------|-------------|
| UiPath Academy | Official learning paths for Agent Builder and Maestro |
| UiPath Documentation | API references, platform guides, release notes |
| UiPath Community | Forum for questions, shared automations, and tips |
