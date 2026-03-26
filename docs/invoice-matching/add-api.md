# Step 5 — Add API Calls

**Send rejection emails and store approved invoices via Integration Service**

---

## Goal

Complete the process by connecting two external systems: **Gmail** (to send rejection emails to suppliers) and **Data Fabric** (to store approved invoice data for payment processing). Both use **UiPath Integration Service**, which handles authentication so you don't have to configure credentials manually.

## Integration Service

**Integration Service** manages authorization and authentication for SaaS platforms. You select a connector and a shared connection, and Maestro handles the rest. No API keys embedded in your process.

## Steps

### Part 1: Configure the rejection email

1. In your **2-Way Matching Process** in Maestro, select the task on the **Reject** path.

2. Set the action type to **Execute Connector Activity**.

    ![Execute Connector Activity selected for reject task](images/api-01.png){ .screenshot }

3. Select the **Gmail Connector** and then the shared Gmail connection.

    ![Gmail Connector and shared connection selected](images/api-02.png){ .screenshot }

4. Configure the **Send Email** activity:
    - **To:** the supplier's email address (from the invoice data)
    - **Subject:** Invoice rejection notification
    - **Body:** use `out_SuggestedResponse` from the agent output — it contains a formatted rejection email with specific discrepancy reasons

    ![Send Email configured with dynamic supplier email and rejection body](images/api-03.png){ .screenshot }

5. Save the task.

### Part 2: Store approved invoice data in Data Fabric

6. Select the task on the **Approve** path (after the human approves or after a direct Full Match).

7. Set the action type to **Execute Connector Activity**.

    ![Execute Connector Activity selected for approve task](images/api-04.png){ .screenshot }

8. Select the **Data Fabric connector** and configure it to write the approved invoice record to the database. This data becomes available to the finance team for payment processing.

    ![Data Fabric connector configured](images/api-05.png){ .screenshot }

9. Map the relevant invoice fields as the record payload.

### Part 3: Test the complete process

10. Run the process several times with different invoice scenarios. After a few runs:
    - Check the **Data Fabric** database — approved invoices accumulate as records
    - Check the supplier email inbox — rejection emails with formatted discrepancy lists arrive automatically

    ![Data Fabric records showing approved invoices from multiple runs](images/api-06.png){ .screenshot }

Your process is complete. It retrieves invoices via robot, matches them using an AI agent, routes exceptions to human reviewers, sends rejection emails via Gmail, and stores approved records in Data Fabric — all orchestrated by Maestro.

[← Step 4: Add a Human](add-human.md) | [Back to Overview](index.md)
