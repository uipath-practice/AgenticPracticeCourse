# Step 2 — Configure a Robot

**Add an RPA automation to your Maestro workflow**

---

## Goal

Create a Maestro Agentic Process, import your BPMN diagram, and connect the first task to the **RetrieveInvoiceDocument** RPA process. The robot simulates retrieving an invoice PDF and outputs the file name stored in a Storage Bucket. The agent in the next step will extract structured data from that PDF using IXP.

## About the Robot Process

In this scenario, the company processes hundreds of invoices per day. Data is stored in ERP and Accounts Payable systems that don't always have APIs or direct database access. RPA automation using UI interaction is often the only way to extract that data.

The **RetrieveInvoiceDocument** process simulates this: it retrieves a sample invoice and outputs the PDF file name from a Storage Bucket. The process has already been configured in Orchestrator in the **2-Way Matching IXP** folder.

## Steps

### Create the Agentic Process

1. In **Studio Web**, click **Create New** and select **Agentic Process**.

    ![New Agentic Process in Studio Web](images/ixp-robot-01.png){ .screenshot }

2. Open **Project Explorer**, right-click on the Agentic Process, and select **Import BPMN**. Select the `.bpmn` file you exported in the previous step.

    ![BPMN diagram imported into Studio Web](images/ixp-robot-02.png){ .screenshot }

3. Delete the auto-generated empty process placeholder.

4. Rename the solution to **2-Way Matching Solution** and the process to **2-Way Matching Process**.

    ![Solution and process renamed](images/ixp-robot-03.png){ .screenshot }

5. Click **Debug** to run the imported diagram. Unlike a static BPMN tool, Maestro can actually execute the model — observe how it follows connections and decision paths.

    ![Debug run on the imported BPMN diagram](images/ixp-robot-04.png){ .screenshot }

### Configure the robot task

6. Select the robot task node in the BPMN canvas.

7. In the properties panel, set the action to **Start and wait for RPA workflow**.

    ![Start and wait for RPA workflow selected](images/ixp-robot-05.png){ .screenshot }

8. Search for and select **RetrieveInvoiceDocument** from the **2-Way Matching IXP** folder.

    ![RetrieveInvoiceDocument selected from 2-Way Matching IXP folder](images/ixp-robot-06.png){ .screenshot }

9. Set a value for **in_FailureProbability**. This controls the probability (in percent) that the invoice won't match the PO. Set it to **90** so the validation path triggers frequently during testing. You can adjust it at any time.

    ![in_FailureProbability input set](images/ixp-robot-07.png){ .screenshot }

### Test the process

10. Click **Debug** to run the process.

    ![Debug mode launch](images/ixp-robot-08.png){ .screenshot }

11. Check the execution details. If you see a file name in the output variables, the robot retrieved the invoice PDF successfully.

    ![Debug output showing PDF filename returned by robot](images/ixp-robot-09.png){ .screenshot }

At this step, don't worry about manually configuring input/output parameters — variables are automatically created for subsequent steps.

12. Close debug mode and save the process.

    ![Process saved and ready for agent configuration](images/ixp-robot-10.png){ .screenshot }

[← Step 1: Create BPMN Process](create-bpmn.md) | [Next: Configure an Agent →](configure-agent.md)
