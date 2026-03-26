# Step 3 — Add an Agent

**Build a 2-way matching agent and connect it to your Maestro workflow**

---

## Goal

Create the **2-Way Matching Agent** in Agent Builder, configure its inputs, outputs, and prompts, then connect it to your Maestro process. The agent compares invoices against purchase orders and returns a matching decision.

## What the Agent Does

The agent receives two JSON documents — an Invoice and a Purchase Order — and:

1. Compares them line by line, including header, line items, and totals
2. Identifies discrepancies
3. Returns a status (`Full Match` or `Failed Match`), an HTML comparison table, and a suggested rejection email if needed

## Steps

### Part 1: Create the agent

1. In **Studio Web**, create a new Agent. Name it **2-Way Matching Agent**.

2. When prompted, dismiss **Autopilot** and select **Start fresh**.

    ![New agent created with Start fresh option](images/agent-01.png){ .screenshot }

3. Configure the **Input Arguments** using this JSON schema (import via the schema editor):

    ```json
    {
      "type": "object",
      "required": ["in_PurchaseOrderData", "in_InvoiceData"],
      "properties": {
        "in_InvoiceData": {
          "type": "string",
          "description": "JSON object containing Invoice data and line items"
        },
        "in_PurchaseOrderData": {
          "type": "string",
          "description": "JSON object containing Purchase Order data and line items"
        }
      }
    }
    ```

    ![Input arguments configured via JSON schema import](images/agent-02.png){ .screenshot }

4. Configure the **Output Arguments** using this JSON schema:

    ```json
    {
      "type": "object",
      "required": ["out_Status"],
      "properties": {
        "out_Status": {
          "type": "string",
          "description": "Status of matching - either 'Full Match' or 'Failed Match'"
        },
        "out_DocumentsHTML": {
          "type": "string",
          "description": "HTML code containing side by side comparison"
        },
        "out_SuggestedResponse": {
          "type": "string",
          "description": "Suggested response to Supplier"
        }
      }
    }
    ```

    ![Output arguments configured](images/agent-03.png){ .screenshot }

### Part 2: Configure prompts

5. Enter the following **System Prompt**:

    ```text
    You are accounting automation agent who is performing 2 way matching of external supplier Invoice against Purchase Order issued by our company against each other. Your objective is to detect and list discrepancies between documents, including line item level comparison, which would allow for more accurate record keeping.
    ```

6. Enter the following **User Prompt**:

    ```text
    Compare these documents:
    Invoice: {{in_InvoiceData}}
    Purchase Order: {{in_PurchaseOrderData}}
    ```

    ![System and User Prompt configured](images/agent-04.png){ .screenshot }

### Part 3: Test the agent

7. Run a simple match test using these sample values:

    **Invoice:**
    ```json
    {
      "Header": {
        "CompanyName": "Lion City Tech Pte Ltd",
        "Company Address": "10 Anson Road, #15-01, Singapore 079903",
        "Company Registration Code": "SG202312345N"
      },
      "Lines": [
        {"ID": "1", "Product Name": "Correction Tape", "Unit Price": "0.30", "Quantity": "30"}
      ],
      "Details": {"Subtotal": "9.00", "Tax (GST 9%)": "0.81", "Total": "9.81"}
    }
    ```

    Provide the matching PO data as the second input. The agent should return `Full Match`.

    ![Agent test with simple matching documents](images/agent-05.png){ .screenshot }

8. Test with a more complex invoice — one with multiple line items where some have slight description variations (e.g., `Tape Dispenser` appears twice, or a descriptor like `(USB-charging)` is appended). Note how the agent handles these.

    ![Agent test with complex documents showing discrepancy detection](images/agent-06.png){ .screenshot }

9. Add the following **matching rules** to your System Prompt to make the agent's behavior explicit:

    **Acceptable variations (count as Full Match):**
    - Identical prices and quantities, with non-exact descriptions
    - One PO line matching multiple invoice lines if quantities sum correctly
    - Semantically similar descriptions (e.g., `Pen` vs `Red pen`, `Phone` vs `Conference Phone`)

    **Discrepancies requiring supplier clarification (Failed Match):**
    - Items in the invoice with no matching PO line
    - Price or quantity differences
    - Semantically different descriptions
    - Multiple invoice lines mapping to a single PO line with different prices

    ![Updated System Prompt with matching rules](images/agent-07.png){ .screenshot }

### Part 4: Configure the agent in Maestro

10. Return to your **2-Way Matching Process** in Maestro. Select the agent task node in the BPMN canvas.

11. Set the action to **Start and wait for agent**. Select **2-Way Matching Agent**.

12. Map the robot outputs to the agent inputs:

    | Robot Output | Agent Input |
    |-------------|-------------|
    | `out_PurchaseOrderData` | `in_PurchaseOrderData` |
    | `out_InvoiceData` | `in_InvoiceData` |

    ![Agent task configured with input mappings](images/agent-08.png){ .screenshot }

13. Add an **Exclusive Gateway** after the agent task. Connect it to:
    - Payment path (Full Match)
    - Manual review path (Failed Match)

14. Set the gateway expression for the **Full Match** path:

    ```text
    vars.outStatus.ToLower()=="full match"
    ```

    ![Gateway expression for Full Match path](images/agent-09.png){ .screenshot }

15. Run the process in debug mode and confirm the gateway routes correctly based on the agent's decision.

    ![Process debug run showing gateway routing](images/agent-10.png){ .screenshot }

[← Step 2: Add a Robot](add-robot.md) | [Next: Add a Human →](add-human.md)
