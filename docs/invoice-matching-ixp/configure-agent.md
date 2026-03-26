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

1. In **Studio Web**, create a new Agent. Name it **2-Way Matching Agent**.

    ![New agent created in Studio Web](images/ixp-agent-01.png){ .screenshot }

2. Configure the **Input Argument**:

    | Argument | Type | Description |
    |----------|------|-------------|
    | `InvoicePDF` | File | The PDF invoice file retrieved from Storage Bucket |

    ![Input argument InvoicePDF configured as File type](images/ixp-agent-02.png){ .screenshot }

3. Configure the **Output Arguments**:

    | Argument | Type | Description |
    |----------|------|-------------|
    | `out_Status` | String | `Full Match` or `Failed Match` |
    | `out_DocumentsHTML` | String | Side-by-side HTML comparison |
    | `out_SuggestedResponse` | String | Suggested rejection email to supplier |
    | `out_POID` | String | The PO ID extracted from the invoice |

    ![Output arguments panel](images/ixp-agent-03.png){ .screenshot }

    ![Output arguments configured including out_POID](images/ixp-agent-04.png){ .screenshot }

4. Save the argument configuration.

    ![Saved argument configuration overview](images/ixp-agent-05.png){ .screenshot }

### Part 2: Configure the prompts

5. Enter the following **User Prompt**:

    ```text
    Analyze {{InvoicePDF}}
    ```

    ![User Prompt with InvoicePDF variable](images/ixp-agent-06.png){ .screenshot }

6. Configure the **System Prompt** with matching rules and tool instructions. Include instructions for calling the IXP tool first, extracting the PO ID, then calling the PO lookup tool.

    ![System Prompt configured](images/ixp-agent-07.png){ .screenshot }

### Part 3: Add the IXP tool

7. Go to the **Tools** tab and add the **IXP tool**.

    ![Tools tab open, IXP tool being added](images/ixp-agent-08.png){ .screenshot }

8. Select the **InvoicesIXP** project as the IXP extraction source.

    ![InvoicesIXP project selected](images/ixp-agent-09.png){ .screenshot }

9. Configure the tool description:

    ```text
    Use this tool to extract structured data from the invoice PDF, including header information, line items, totals, and the Purchase Order ID.
    ```

    ![IXP tool description configured](images/ixp-agent-10.png){ .screenshot }

10. Save the IXP tool configuration.

    ![IXP tool saved and visible in the tools list](images/ixp-agent-11.png){ .screenshot }

### Part 4: Add the PO lookup tool

11. Add a second tool: an **RPA Workflow** tool.

    ![RPA Workflow tool being added](images/ixp-agent-12.png){ .screenshot }

12. Select **Query Entity Records** from the **PurchaseOrdersDatabase** source.

    ![Query Entity Records selected from PurchaseOrdersDatabase](images/ixp-agent-13.png){ .screenshot }

13. Configure the filter: **POID equals in_POID**.

    ![Filter configured as POID equals in_POID](images/ixp-agent-14.png){ .screenshot }

14. Configure the tool description:

    ```text
    Use this tool to retrieve Purchase Order data from the database. Filter by POID using the PO ID extracted from the invoice. PO IDs start with "PO-" followed by digits.
    ```

    ![PO lookup tool description configured](images/ixp-agent-15.png){ .screenshot }

15. Save the PO lookup tool configuration.

    ![Both tools saved and visible in tools list](images/ixp-agent-16.png){ .screenshot }

### Part 5: Test the agent

16. Test the agent with a sample PDF invoice from the Storage Bucket. Confirm the agent calls the IXP tool to extract data.

    ![Agent test execution started with PDF input](images/ixp-agent-17.png){ .screenshot }

17. Review the IXP extraction results — verify the agent identified the PO ID correctly.

    ![IXP extraction results with PO ID identified](images/ixp-agent-18.png){ .screenshot }

18. Confirm the agent called the PO lookup tool with the extracted PO ID.

    ![PO lookup tool called with extracted POID](images/ixp-agent-19.png){ .screenshot }

19. Review the final agent output — verify `out_Status`, `out_DocumentsHTML`, `out_SuggestedResponse`, and `out_POID` are all populated.

    ![Agent output variables fully populated](images/ixp-agent-20.png){ .screenshot }

    ![HTML comparison output preview](images/ixp-agent-21.png){ .screenshot }

### Part 6: Connect the agent to Maestro

20. Return to your **2-Way Matching IXP Process** in Maestro. Select the agent task node.

21. Set the action to **Start and wait for agent**. Select **2-Way Matching Agent**.

    ![Agent task configured in Maestro](images/ixp-agent-22.png){ .screenshot }

22. Map the robot output to the agent input:

    | Robot Output | Agent Input |
    |-------------|-------------|
    | `out_FileName` | `InvoicePDF` |

    ![Input mapping from robot output to agent input](images/ixp-agent-23.png){ .screenshot }

23. Add an **Exclusive Gateway** after the agent task. Configure the expression for the **Full Match** path:

    ```text
    vars.outStatus.ToLower()=="full match"
    ```

24. Run the process in debug mode and confirm the gateway routes correctly.

    ![Process debug run showing correct gateway routing](images/ixp-agent-24.png){ .screenshot }

[← Step 2: Configure a Robot](configure-robot.md) | [Next: Configure Human Validation →](configure-human-validation.md)
