# Build an Agent and add it to workflow

!!! tip "Here is our plan for this lesson:"

    1. Build the **2-Way Matching AI Agent** from scratch in **Studio Web**.
        - The agent will use Robot's JSON outputs as inputs, and output the validation result.
        - If there is a problem with the invoice, the agent will also prepare data for the human validation task.

    2. Configure testing and build an evaluations dataset to ensure quality of the Agent *(optional)*.

    3. Configure the Agent in the Maestro workflow.

    4. Configure Maestro Gateway based on Agent's outputs.

    5. Simulate to see if the decision goes the right direction.

## Goal

Create the **2-Way Matching Agent** with two tools: an IXP data extraction tool and an RPA workflow tool that queries the Purchase Order database. The agent receives a PDF invoice, extracts structured data, looks up the corresponding PO, and returns a matching decision with supporting outputs.

## Why Use an LLM for Matching

The next step in our process is to compare Purchase Order and Invoice.

You can write traditional code that would compare and analyze invoice data and line items, but it might be fairly challenging, since "rules" are usually flexible — for example, tables might include lines with semantically similar but not identical descriptions, or there may be some other acceptable variations. This increases code complexity and implementation time for every such edge case.

Also, if discrepancies are detected, the usual next step is to write to the sender and request to update the invoice.

LLMs are ideal for this job — they can analyze large amounts of text in any format, identify discrepancies and exceptions, then follow the instructions in prompts to generate a validation summary or email response in the required format and language.

Let's use Studio to create our "2-Way Matching Agent"!

## Steps

### Part 1: Create the agent and configure arguments

1. In **Studio Web**, add a new Agent to your solution. Remember that Solutions can have multiple components such as apps, automations, workflows and agents. Name it **2-Way Matching Agent**.

    ![New agent created in Studio Web](configure-agent.images/1-new-agent.png){ .screenshot }

    Dismiss the Autopilot screen when you see the prompt to generate a new agent. Feel free to play with Autopilot later, but here you'll configure prompts and settings manually — click **Start fresh**.

2. Open **Data Manager** from the left ribbon and add a new Input argument:

    | Field | Value |
    |-------|-------|
    | Name | `InvoicePDF` |
    | Type | File |
    | Description | Invoice File |

    ![Input argument InvoicePDF configured as File type](configure-agent.images/2-input-argument.png){ .screenshot }

3. For Output arguments, switch to editor mode.

    ![Switching to editor mode for output arguments](configure-agent.images/3-editor-mode.png){ .screenshot }

4. Paste the following JSON into the editor:

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
          "description": "HTML code containing side by side comparison of Purchase Order and Invoice"
        },
        "out_SuggestedResponse": {
          "type": "string",
          "description": "Suggested response to Invoice Supplier with description and request to mitigate issues"
        },
        "out_POID": {
          "type": "string",
          "description": "Purchase Order ID extracted from Invoice PDF"
        }
      },
      "title": "Outputs"
    }
    ```

    ![Output arguments JSON pasted into editor](configure-agent.images/4-output-json.png){ .screenshot }

5. Confirm all four output arguments are configured correctly.

    ![Output arguments configured](configure-agent.images/5-output-arguments.png){ .screenshot }

### Part 2: Configure the prompts

System prompt is like human's work instructions. Let's start with something like this:

> *"Precision in prompts, like in coding, leads to powerful and predictable results. If your prompt is messy, expect messy output. Treat it like code, and write every word with purpose!"* — another advice from gpt-4o

6. Enter the following **User Prompt**:

    ```text
    Analyze {{InvoicePDF}}.
    ```

    ![User Prompt with InvoicePDF variable](configure-agent.images/6-user-prompt.png){ .screenshot }

7. Enter the following **System Prompt**:

    ```text
    You are an AI agent specialized in comparing Invoice PDFs with Purchase Orders. Your primary responsibilities are:

    1. Analyze the contents of an Invoice PDF file using the InvoicesIXP tool. Extract all relevant information including company details, line items, totals, and tax information. Trigger Escalation if confidence falls beyond 60%.

    2. Use the Retrieve PO Data tool to fetch Purchase Order data from the Data Fabric. The Purchase Order ID should be extracted from the Invoice. If the PO data cannot be retrieved, use Escalation.

    3. Compare the Invoice details with the Purchase Order information. Identify and list any mismatches or discrepancies between the two documents. Pay special attention to:
       - Company names and details
       - Line items (product names, quantities, prices)
       - Totals and subtotals
       - Tax information
       - Dates (order date, delivery date, payment due date)

    4. Handle any unexpected data formats or missing information gracefully. If crucial information is missing from either document, note this in your analysis and use Escalation.

    5. Provide a clear, concise report of your findings, highlighting any issues that require attention.

    You should be thorough in your analysis, checking for discrepancies in items, quantities, prices, dates, and any other relevant fields. Always maintain a professional and objective tone in your reports.

    out_Status: Status of comparison should be:
    - "Full Match" - if Invoice and Purchase order match fully. Every line item in PO matched to Invoice line items, company name and details match, total and tax information matches.
    - "Failed Match" - if there are items that cannot be matched or other details do not align.

    out_DocumentsHTML: If match is not successful, generate HTML code containing side by side comparison of Purchase Order and Invoice, including Company details, document Line Items, Total and Tax information.
    - Use a table structure with three columns: Field, Purchase Order, Invoice.
    - Field titles should be placed in the leftmost column.
    - Tax value should include tax rate and tax name, if available.
    - Line items should be displayed as sub-tables inside the main table cell, aligned top.
    - Cells with discrepancies should have a light red background, both in the main table and in cells of line items sub-tables.
    - Set the table width property to 100%.
    - Use appropriate HTML tags for headers, rows, and data cells.

    out_SuggestedResponse: If match is not successful, draft the invoice rejection email to the supplier.
    - The email should have HTML formatting.
    - Start with "Dear Supplier" and do not include a Subject line or placeholders. Sign the email as "Payments Team".
    - Display product names, prices, and other data from documents in bold text.
    - Include a bullet list with reasons for rejection, i.e., discrepancies that can't be matched, and a request to adjust the invoice and resend.
    - In the bullet list, do not include items if that individual item is considered a match. Only list items that do not follow the rules.
    - Maintain a professional and courteous tone throughout the email.

    Always double-check your analysis and outputs for accuracy before finalizing your response.
    ```

    ![System Prompt configured](configure-agent.images/7-system-prompt.png){ .screenshot }

### Part 3: Add the IXP tool

Next, our agent will need tools that we mentioned in the system prompt:

- **InvoicesIXP** tool — uses the existing Invoice IXP project for data extraction
- **Retrieve PO Data** tool — looks up Purchase Order details using the extracted PO ID

8. In canvas mode, select your agent and add a new Tool.

    ![Tools section, adding a new tool](configure-agent.images/8-add-tool.png){ .screenshot }

9. Select **IXP** from the toolbox and choose the **InvoicesIXP** project.

    ![InvoicesIXP project selected](configure-agent.images/9-ixp-project.png){ .screenshot }

10. Add a meaningful description, for example: **Invoice Data extraction tool**.

    ![IXP tool description configured](configure-agent.images/10-ixp-description.png){ .screenshot }

    It's an out-of-the-box Invoice extraction model with standard taxonomy. You will not be able to see the tool configuration. It will return a JSON object containing extraction data. That's it!

11. Save the IXP tool configuration.

    ![IXP tool saved and visible in the tools list](configure-agent.images/11-ixp-tool-saved.png){ .screenshot }

### Part 4: Build and add the PO lookup tool

Next, let's build the **Retrieve PO Data** tool as a new RPA workflow. PO data is stored in Data Fabric and we can look up records using POID.

12. Add a new RPA workflow to your solution. Give it a meaningful name, like always.

    ![New RPA workflow added to solution](configure-agent.images/12-new-rpa-workflow.png){ .screenshot }

13. Configure the input and output variables for the workflow. Return the PODATA field from the entity.

    ![Input and output variables configured](configure-agent.images/13-workflow-variables.png){ .screenshot }

14. Add a **Query Entity Records** activity configured to query the **PurchaseOrdersDatabase** entity. Apply the filter: **POID equals in_POID**.

    ![Query Entity Records activity with POID filter](configure-agent.images/14-query-entity-records.png){ .screenshot }

15. Back in your agent's canvas, add this RPA workflow as a tool.

    ![RPA workflow added as a tool](configure-agent.images/15-rpa-tool-added.png){ .screenshot }

16. Configure the input hint for the **in_POID** argument so the agent knows the expected format:

    ```text
    Purchase Order ID. It starts with 'PO-' followed by a few digits, for example: 'PO-123456'.
    ```

    ![Both tools saved and visible in tools list](configure-agent.images/16-both-tools.png){ .screenshot }

Usually you would need to retrieve PO from a more complex environment like SAP or NetSuite, and also handle exceptions. But in this case you got away really easy — well done! ;)

### Part 5: Test the agent

17. Test the agent with a sample PDF invoice. Confirm the agent calls the IXP tool first.

    ![Agent test execution started with PDF input](configure-agent.images/17-agent-test.png){ .screenshot }

18. Review the IXP extraction results and verify the agent identified the PO ID correctly.

    ![IXP extraction results with PO ID identified](configure-agent.images/18-ixp-results.png){ .screenshot }

19. Confirm the agent called the PO lookup tool with the extracted PO ID.

    ![PO lookup tool called with extracted POID](configure-agent.images/19-po-lookup.png){ .screenshot }

20. Review the final output. Verify `out_Status`, `out_DocumentsHTML`, `out_SuggestedResponse`, and `out_POID` are all populated.

    ![Agent output variables fully populated](configure-agent.images/20-output-variables.png){ .screenshot }

    ![HTML comparison output preview](configure-agent.images/21-html-comparison.png){ .screenshot }

Investigate carefully — there are no errors here. It's just that the Vendor sent an Invoice that is differently formatted, and some descriptions are not identical but very similar. The Agent will only follow our specific instructions in the Prompt, and the current prompt doesn't mention anything about such "similar" items, or the possibility of splitting 1 PO line item into multiple Invoice line items.

As with any automation, our objective with the prompts is to cover as many cases as possible.

### Part 6: Connect the agent to Maestro

Let's get back to **Studio Web** and continue editing our Agentic Process.

21. Return to your **Maestro Agentic Process** and configure the second task. Set the action to **Start and wait for agent**, then search for the agent in your solution (Defined Resources) and select it.

    ![Agent task configured in Maestro](configure-agent.images/22-agent-task-maestro.png){ .screenshot }

22. Pick outputs from the previous RPA Task (Retrieve Invoice PDF) and add them as inputs to the Agent — here is how you do it in your Agent Task's Settings:

    | Robot output | Agent input |
    |-------------|-------------|
    | `out_FileName` | `InvoicePDF` |

    ![Input mapping from robot output to agent input](configure-agent.images/23-input-mapping.png){ .screenshot }

    Note that Agent's outputs were also automatically added to the workflow, so you can use them right away when configuring the Exclusive Gateway.

23. Let's look at Agent's Status (`out_Status`) and direct the process to the next step — either sending the invoice for payment, or towards manual review. Configure the **Exclusive Gateway** after the agent task.

    Set the expression for the **Full Match** path. Note that using `ToLower()` makes it a bit more reliable:

    ```text
    vars.outStatus.ToLower()=="full match"
    ```

    You can test various expected inputs right in the expression editor. Set **Failed Match** as the default path.

24. Click **Debug** and confirm the gateway routes correctly based on the agent's output. This time we want to see execution of the Agent and how Agent's output changes the direction of the execution flow from the default path.

    ![Process debug run showing correct gateway routing](configure-agent.images/24-gateway-routing.png){ .screenshot }

Your agent is ready. However, in most cases you will need to come back multiple times and improve the prompt in order for it to be more flexible — this way users need to perform less manual validation and it will work more reliably.

[← Configure a Robot](configure-robot.md) | [Next: Configure Human Validation →](configure-human-validation.md)
