# Step 3 — Configure an Agent

**Extract invoice data using IXP, look up the PO, and perform matching**

---

## Goal

Configure the **2-Way Matching Agent** with two tools: an IXP extraction tool and an RPA workflow tool that queries the Purchase Order database. The agent receives a PDF invoice, extracts structured data from it, looks up the corresponding PO, and returns a matching decision.

## How the Agent Works

The agent follows this sequence:

1. Receives the invoice PDF filename
2. Calls the **IXP tool** to extract structured invoice data (header, line items, totals, PO ID)
3. Uses the extracted **PO ID** to call the **RPA workflow tool** and retrieve the matching Purchase Order from the database
4. Compares invoice against PO and returns: `Full Match` or `Failed Match`

## PO ID Format

PO IDs in this exercise follow the format **PO-** followed by digits — for example, `PO-123456`. The agent uses this format when filtering the database query.

## Steps

### Part 1: Create the agent

1. In **Studio Web**, create a new Agent (or reuse the 2-Way Matching Agent from the standard exercise). Name it **2-Way Matching Agent**.

2. Configure the **Input Argument**:

    | Argument | Type | Description |
    |----------|------|-------------|
    | `InvoicePDF` | File | The PDF invoice file retrieved from Storage Bucket |

    ![Input argument InvoicePDF configured as File type](images/ixp-agent-01.png){ .screenshot }

3. Configure the **Output Arguments**:

    | Argument | Type | Description |
    |----------|------|-------------|
    | `out_Status` | String | `Full Match` or `Failed Match` |
    | `out_DocumentsHTML` | String | Side-by-side HTML comparison |
    | `out_SuggestedResponse` | String | Suggested rejection email to supplier |
    | `out_POID` | String | The PO ID extracted from the invoice |

    ![Output arguments configured including out_POID](images/ixp-agent-02.png){ .screenshot }

### Part 2: Configure the User Prompt

4. Enter the following **User Prompt**:

    ```text
    Analyze {{InvoicePDF}}
    ```

    ![User Prompt with InvoicePDF variable](images/ixp-agent-03.png){ .screenshot }

5. Configure the **System Prompt** with matching rules and instructions for tool use (similar to the standard exercise, adapted for PDF extraction via IXP).

### Part 3: Add the IXP tool

6. Go to the **Tools** tab and add the **IXP tool**.

7. Select the **InvoicesIXP** project as the IXP extraction source.

    ![IXP tool added with InvoicesIXP project selected](images/ixp-agent-04.png){ .screenshot }

8. Configure the tool description to tell the agent when to use it:

    ```text
    Use this tool to extract structured data from the invoice PDF, including header information, line items, totals, and the Purchase Order ID.
    ```

    ![IXP tool description configured](images/ixp-agent-05.png){ .screenshot }

### Part 4: Add the PO lookup tool

9. Add a second tool: an **RPA Workflow** tool.

10. Select **Query Entity Records** from the **PurchaseOrdersDatabase** source.

    ![Query Entity Records tool selected](images/ixp-agent-06.png){ .screenshot }

11. Configure the filter: **POID equals in_POID**.

    This tells the tool to find the Purchase Order whose ID matches what the agent extracted from the invoice.

    ![Filter configured as POID equals in_POID](images/ixp-agent-07.png){ .screenshot }

12. Configure the tool description:

    ```text
    Use this tool to retrieve Purchase Order data from the database. Filter by POID using the PO ID extracted from the invoice. PO IDs start with "PO-" followed by digits.
    ```

    ![PO lookup tool description](images/ixp-agent-08.png){ .screenshot }

### Part 5: Test the agent

13. Test the agent with a sample PDF invoice from the Storage Bucket. Confirm the agent:
    - Calls the IXP tool to extract data
    - Identifies the PO ID from the extracted data
    - Calls the PO lookup tool with the correct PO ID
    - Returns a matching decision

    ![Agent test execution with PDF invoice](images/ixp-agent-09.png){ .screenshot }

    ![Agent output showing Status, HTML comparison, and POID](images/ixp-agent-10.png){ .screenshot }

### Part 6: Connect the agent to Maestro

14. Return to your **2-Way Matching IXP Process** in Maestro. Select the agent task node.

15. Set the action to **Start and wait for agent**. Select **2-Way Matching Agent**.

16. Map the robot output to the agent input:

    | Robot Output | Agent Input |
    |-------------|-------------|
    | `out_FileName` | `InvoicePDF` |

    ![Agent task configured with PDF file mapping](images/ixp-agent-11.png){ .screenshot }

17. Add an **Exclusive Gateway** after the agent task. Configure the expression for the **Full Match** path:

    ```text
    vars.outStatus.ToLower()=="full match"
    ```

    ![Gateway expression for Full Match path](images/ixp-agent-12.png){ .screenshot }

18. Run the process in debug mode and confirm the gateway routes correctly.

    ![Process debug showing correct gateway routing](images/ixp-agent-13.png){ .screenshot }

[← Step 2: Configure a Robot](configure-robot.md) | [Next: Configure Human Validation →](configure-human-validation.md)
