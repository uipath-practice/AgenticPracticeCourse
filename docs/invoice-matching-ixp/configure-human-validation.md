# Step 4 — Configure Human Validation

**Add an Action App for human review when the agent can't match documents**

---

## Goal

Add a human validation step on the **Failed Match** path. When the agent flags a mismatch, a reviewer in **Action Center** sees a summary with both documents and chooses to approve or reject the invoice. The workflow resumes based on their decision.

## Humans in the Loop

When an agent can't determine the correct course of action, human involvement is required. Reviewers process tasks in **Action Center** using inputs prepared by robots and agents:

- All inputs needed to make a decision should be on one screen. Reviewers shouldn't need to open other applications or check execution logs.
- The agent's job is to prepare all inputs in the right format before the human task is triggered.
- Once the decision is made, the process continues to the next step.

Here's what the validation form needs:
- Both documents presented side by side, with discrepancies highlighted in red.
- A brief description of the problem.
- A pre-drafted rejection email — the agent already generated this in the previous step.

!!! note "Note on approvals"
    In practice, approving a mismatched invoice for payment can be a serious compliance issue — in some countries it's illegal. For this exercise, assume the reviewer can make any decision with no consequences.

## Steps

### Part 1: Import the validation app

1. Import the **2WM Validation App IXP Template** from the shared templates into your solution. Find it and click **Add**.

    ![2WM Validation App IXP Template selected](images/ixp-human-01.png){ .screenshot }

2. After the app appears in your solution, review its structure:
   - UI elements — how the validation task appears to the reviewer.
   - App Actions and Action Schema — the possible outcomes of the reviewer's decision.
   - App Inputs and Outputs — where data comes from and what comes out.

    ![2WM Validation App IXP interface](images/ixp-human-02.png){ .screenshot }

### Part 2: Configure the human task in Maestro

3. In your **Maestro Agentic Process**, select the human task node on the **Failed Match** path.

4. Set the action type to **Action App Task**.

    ![Action App Task selected](images/ixp-human-03.png){ .screenshot }

5. Select the **2WM Validation App IXP** you imported.

6. Customize the task title so it's easy to identify in Action Center, for example: **Invoice Review Required**.

7. In **Advanced Options**, assign the task to yourself. Otherwise you'll need to locate your task among all unassigned tasks in Action Center.

    ![Task configured with title and assignee](images/ixp-human-04.png){ .screenshot }

8. Map the agent outputs to the app inputs:

    | Agent output | App input |
    |-------------|-----------|
    | `out_DocumentsHTML` | Comparison display field |
    | `out_SuggestedResponse` | Suggested rejection email field |

    ![Agent outputs mapped to app inputs](images/ixp-human-05.png){ .screenshot }

9. Save the task configuration.

    ![Completed task configuration](images/ixp-human-06.png){ .screenshot }

### Part 3: Configure the gateway decision

10. Configure the **Exclusive Gateway** downstream from the human task.

    ![Exclusive Gateway configured](images/ixp-human-07.png){ .screenshot }

11. Set **Reject** as the default path.

12. In the Expression Editor, pick the **Action** output (which per the app settings can be `"Approve"` or `"Reject"`). Configure the **Approve** path condition:

    ```text
    vars.actionOutput == "Approve"
    ```

    ![Expression Editor with Approve condition](images/ixp-human-08.png){ .screenshot }

### Part 4: Test the human validation flow

13. Click **Debug**. With `in_FailureProbability` set to 90, the invoice will frequently fail to match, triggering the human task.

    ![Process debug with human task triggered](images/ixp-human-09.png){ .screenshot }

14. When the process pauses, click **Open app task** or find it in **Action Center**. Review the comparison and click **Approve** or **Reject**.

    ![Action Center showing invoice review task](images/ixp-human-10.png){ .screenshot }

15. Confirm the process resumed and routed correctly after your decision.

    ![Process resumed after human decision](images/ixp-human-11.png){ .screenshot }

16. Review the execution trace in Maestro to verify the correct path was taken.

    ![Execution trace showing the path taken](images/ixp-human-12.png){ .screenshot }

17. Run a few more tests — try both Approve and Reject — to confirm both paths work.

    ![Second test run with different decision outcome](images/ixp-human-13.png){ .screenshot }

    ![Process execution summary after multiple test runs](images/ixp-human-14.png){ .screenshot }

18. Review the end-to-end process execution.

    ![End-to-end process flow](images/ixp-human-15.gif){ .screenshot }

[← Step 3: Configure an Agent](configure-agent.md) | [Next: Configure API Integration →](configure-api.md)
