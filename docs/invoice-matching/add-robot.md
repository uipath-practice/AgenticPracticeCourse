# Step 2 — Add a Robot

**Import your BPMN diagram and connect it to an RPA process**

---

## Goal

Create an Agentic Process in **Maestro**, import the BPMN diagram you built in Step 1, and connect the first workflow task to the **Retrieve.Invoice** RPA process. By the end of this step, your process will retrieve simulated invoice and PO data and you'll be able to run it end to end in debug mode.

## Why a Robot Here

Hundreds of invoices arrive daily, extracted from ERP and billing systems via RPA — without API access. The **Retrieve.Invoice** process simulates this retrieval and generates sample Invoice and PO documents as JSON, providing structured input for the agent in the next step.

## Steps

### Create the Maestro Agentic Process

1. In **Studio Web**, create a new **Agentic Process**.

    ![New Agentic Process created in Studio Web](images/robot-01.png){ .screenshot }

2. Import your BPMN diagram. Select the **2-Way Matching Process.bpmn** file you exported in Step 1.

    ![BPMN diagram imported into Maestro](images/robot-02.png){ .screenshot }

3. Delete the auto-generated empty process placeholder that appears after import.

4. Rename the process to **2-Way Matching Process**.

5. Rename the project to **2-Way Matching Project**.

    ![Process and project renamed](images/robot-03.png){ .screenshot }

### Configure the robot task

6. Select the robot task node in your BPMN canvas.

7. Open the properties panel and select **Start and wait for RPA workflow** as the action type.

    ![Properties panel with Start and wait for RPA workflow selected](images/robot-04.png){ .screenshot }

8. Search for and select the **Retrieve.Invoice** process from the **2-Way Matching** folder.

    ![Retrieve.Invoice process selected from 2-Way Matching folder](images/robot-05.png){ .screenshot }

9. Set the `in_FailureProbability` input argument to **90** (percent). This simulates realistic retrieval conditions during testing.

    ![in_FailureProbability set to 90](images/robot-06.png){ .screenshot }

### Test the process

10. Click **Debug** to launch the process.

    ![Debug button in Maestro process editor](images/robot-07.png){ .screenshot }

11. Wait for the process to complete and review the output. The **Retrieve.Invoice** process produces JSON with the following structure:

    ```json
    {
      "Header": {
        "CompanyName": "...",
        "Address": "...",
        "RegistrationCode": "..."
      },
      "Lines": [
        {
          "ID": "1",
          "ProductName": "...",
          "UnitPrice": "...",
          "Quantity": "..."
        }
      ],
      "Details": {
        "Subtotal": "...",
        "Tax": "...",
        "Total": "..."
      }
    }
    ```

    ![Process execution output showing Invoice and PO JSON](images/robot-08.png){ .screenshot }

12. Confirm that both invoice and PO data were generated in the output.

    ![Output variables showing out_InvoiceData and out_PurchaseOrderData](images/robot-09.png){ .screenshot }

The robot is now connected and returning structured data. In the next step, you'll add an agent that compares the two documents.

[← Step 1: Create BPMN Diagram](create-bpmn.md) | [Next: Add an Agent →](add-agent.md)
