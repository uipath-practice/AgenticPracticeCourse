# Modeling Business Processes using BPMN canvas

!!! tip "Let's start"
    
    **1. Review the business process that we will implement**

    **2. Prepare a BPMN diagram reflecting process steps**
   
## Goal

In this step, you'll design the process flow diagram for the invoice matching automation. You'll review the business process, build it in the UiPath BPMN designer, and export the file for import into Maestro.

## The 2-Way Matching Process

2-way matching is one of the most common processes in finance — validating a supplier invoice against the original Purchase Order.

Here are the common steps:

1. **Purchase Order creation** — the purchasing department creates a formal PO with item descriptions, quantities, unit prices, and agreed payment terms.
2. **Invoice receipt and data entry** — after the vendor delivers goods or services, they submit an invoice. The Accounts Payable team receives it and enters the data into the accounting system, often via automated extraction (OCR + IXP).
3. **Document validation** — the AP team retrieves the original PO and compares it against the invoice, checking for consistency in key fields: PO number, total amount, price, and line items.
      - Companies often set tolerance levels (e.g., a 5% price variance) to determine if minor differences are acceptable. If within tolerance, the invoice moves to approval; otherwise, it is flagged.
      - A single PO may be covered by multiple invoices (partial delivery).
4. **Approval or exception handling** — a matching invoice is approved for payment. If a discrepancy exists, the invoice is placed on hold and sent for investigation.
5. **Payment processing and documentation** — the approved invoice is scheduled for payment. All records are stored together for audit purposes.

### Matching Variants

| Variant | Documents compared |
|---------|--------------------|
| **2-way** | Invoice + Purchase Order |
| **3-way** | Invoice + PO + Goods Receipt Note |
| **4-way** | Invoice + PO + Goods Receipt Note + Inspection Report |

Every company has customizations depending on their ERP and industry. This exercise focuses on 2-way matching.

### What You'll Build

For this exercise, focus on steps 2–4. The simplified process:

1. Supplier sends an invoice containing:
      - **Header** (company name, addresses, dates, Invoice ID, PO ID, Company registration ID, etc - the usual fields).
      - **Line items** in a table (Product, Quantity, Price)
      - **Footer** (Subtotals, Totals, Tax information)
2. **Invoice data is compared** against the linked Purchase Order. Possible outcomes:
      - **Full match:** names, quantities, and prices match across all line items, company details, totals, and tax information align.
      - **Failed match:** discrepancies found: wrong company entity, missing line items, unmatched descriptions, or nothing in common at all.
3. **If the invoice and PO match** (or if a human reviewed and approved it): invoice details are updated in **Data Fabric** and sent for payment.
4. **If they don't match** — a validation task is created in **Action Center** for the Accounts Payable team to review and then approve or reject.
5. **If rejected** — an email is generated and sent to the supplier with reasons and a request to fix and resubmit the invoice. The resubmitted invoice is processed following the same steps.

## Build the diagram

1. Open **[bpmn.uipath.com](https://bpmn.uipath.com/)** in your browser.

2. Build a BPMN diagram based on the process description above. It should look similar to this:

    ![BPMN diagram for IXP invoice matching process](create-bpmn.images/1-bpmn-diagram.png){ .screenshot }

3. Export the diagram as a `.bpmn` file. You'll import it into Maestro in the next step. Alternatively, download and use this **[sample BPMN file](dependencies/2-Way%20Matching%20Process.bpmn)**.


[[[
![Wise robot](create-bpmn.images/2-wise-robot.png){ .screenshot }
|30|
In later steps, you'll connect each task in this diagram to UiPath platform components. When the process runs, Orchestrator will trigger robotic and agentic jobs — or route tasks to humans. Let's add some action into this diagram by **[adding a Robot](2-configure-robot.md)**!
]]]