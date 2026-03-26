# Step 5 — Configure API Integration

**Connect Gmail and Data Fabric to complete the IXP process**

---

## Goal

Add the same two API integrations as the standard exercise: **Gmail** for rejection emails and **Data Fabric** for storing approved invoice records. Both use **Integration Service** connectors already configured in your tenant.

## Steps

### Part 1: Configure the rejection email

1. In your **2-Way Matching IXP Process** in Maestro, select the task on the **Reject** path.

2. Set the action type to **Execute Connector Activity**.

    ![Execute Connector Activity selected](images/ixp-api-01.png){ .screenshot }

3. Select the **Gmail Connector** and the shared Gmail connection.

    ![Gmail Connector and shared connection selected](images/ixp-api-02.png){ .screenshot }

4. Configure the **Send Email** activity:
    - **To:** the supplier's email address from the extracted invoice data
    - **Body:** use `out_SuggestedResponse` — the agent's formatted rejection email with specific discrepancy reasons

    ![Email configured with supplier address and rejection body](images/ixp-api-03.png){ .screenshot }

5. Save the task.

### Part 2: Store approved invoice data in Data Fabric

6. Select the task on the **Approve** path.

7. Set the action type to **Execute Connector Activity**.

    ![Execute Connector Activity on Approve path](images/ixp-api-04.png){ .screenshot }

8. Select the **Data Fabric connector** and configure it to write the approved invoice record for payment processing.

    ![Data Fabric connector configured](images/ixp-api-05.png){ .screenshot }

### Part 3: Test the complete process

9. Run the process several times. After a few runs:
    - Check **Data Fabric** — approved invoices accumulate as records
    - Check the supplier inbox — formatted rejection emails arrive automatically

    ![Data Fabric records from multiple process runs](images/ixp-api-06.png){ .screenshot }

Your IXP-enhanced process is complete. It retrieves invoice PDFs via robot, extracts and validates data using IXP, queries the PO database, routes exceptions to human review, sends rejection emails, and stores approved records — all orchestrated by Maestro.

[← Step 4: Configure Human Validation](configure-human-validation.md) | [Back to Overview](index.md)
