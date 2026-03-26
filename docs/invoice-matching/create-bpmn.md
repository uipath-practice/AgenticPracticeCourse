# Step 1 — Create BPMN Diagram

**Model the invoice matching process before building it**

---

## Goal

Design the invoice matching workflow as a BPMN diagram. This diagram becomes the blueprint you'll import into **Maestro** in the next step.

## The Process You're Modeling

A supplier sends an invoice containing a header, line items, and footer. Your automation compares this invoice against the associated **Purchase Order (PO)**.

Three outcomes are possible:

| Outcome | Next Action |
|---------|-------------|
| **Full match** | Update UiPath Data Service and proceed to payment |
| **Partial match / mismatch** | Route to Accounting Team for manual review |
| **No match / rejected** | Send notification email to supplier |

## BPMN Diagramming Tool

Build your diagram at **[bpmn.uipath.com](https://bpmn.uipath.com/)**. When finished, export it as a `.bpmn` file — you'll import it into Maestro in Step 2.

## Steps

1. Open **[bpmn.uipath.com](https://bpmn.uipath.com/)** in your browser.

2. Create a new diagram and model the invoice matching process:
    - A **Start Event** triggers when a new invoice arrives
    - A **Robot task** retrieves the invoice and associated PO data
    - An **Agent task** compares invoice against PO
    - An **Exclusive Gateway** routes based on the comparison result:
        - Full match → update Data Service → End
        - Mismatch → Accounting Team review → End
        - Rejected → send supplier notification email → End

    ![Sample BPMN diagram for invoice matching process](images/bpmn-01.png){ .screenshot }

3. Review the process flow to make sure all paths have an End Event.

4. Export the diagram as a `.bpmn` file. Save it as **2-Way Matching Process.bpmn**.

    ![Completed BPMN diagram exported as .bpmn file](images/bpmn-02.png){ .screenshot }

You now have a complete process blueprint ready to import into Maestro.

[← Back to Overview](index.md) | [Next: Add a Robot →](add-robot.md)
