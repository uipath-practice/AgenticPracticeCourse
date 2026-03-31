Build a complete lesson page from screenshots for the Agentic Automation Workshop site.

## Collect inputs

If any of the following are missing from the user's message, ask before proceeding:

1. **Exercise slug** — folder name of the exercise (e.g., `expense-report-processing`)
2. **Step number** — the numeric prefix (e.g., `3`)
3. **Step name** — display name for the step (e.g., "Configure Agent")
4. **Images folder path** — path to the folder containing the screenshots (e.g., `docs/expense-report-processing/configure-agent.images/`)
5. **Context** (optional) — any additional details: platform features used, expected inputs/outputs, business logic, or special instructions

---

## Step 1: Check documentation references, then extract metadata

**Before running extraction**, check whether `docs/<exercise-slug>/documentation.md` exists. If it does, remind the user to add links for this lesson's topic before continuing. The extraction script reads this file and embeds any new URLs as documentation context — this improves metadata quality.

If the file exists but is missing relevant links, ask the user: *"Have you added the relevant documentation links to documentation.md for this step? The extraction script uses them as context."*

Once ready, run the extraction script:

```bash
python -m scripts.extract_metadata --folder <images-folder-path>
```

The script will:
1. Read `docs/<exercise-slug>/documentation.md` and embed any new URLs not yet cached (previously embedded links are skipped)
2. Use the embedded documentation as context when analyzing each screenshot

**Prerequisites:** `scripts/.env` must exist with Azure OpenAI credentials. See `scripts/.env.example` for the required keys. If the file is missing, stop and ask the user to set it up before continuing.

If some images already have `.metadata.json` files alongside them, the script skips those by default. Use `--force` only if explicitly requested.

After running, verify that `.metadata.json` files exist next to the images. If the script fails, report the error — do not proceed with placeholder content.

---

## Step 2: Read the metadata

Read every `.metadata.json` file in the images folder. Each file contains:
- `filename` — the image file it describes
- `ocr_text` — raw text visible in the screenshot
- `ui_description` — description of the UI state shown
- `step_instruction` — the action or concept the screenshot illustrates

Build a mental model of the full step: what the learner does first, what intermediate states look like, and what the final result is.

Also read the existing step `.md` file if it already exists (it may be a stub). Note any headings or partial content that should be preserved.

---

## Step 3: Build the lesson page

Write the complete lesson to `docs/<exercise-slug>/N-verb-noun.md`.

---

### Page structure

Every step page follows this structure in order:

**1. Title**

```markdown
# Step N — Verb Noun
```

The title is either `Step N — Verb Noun` for sequential steps, or a short descriptive phrase if the step is conceptual. Capitalisation and exact phrasing can vary.

**2. Opening tip admonition**

```markdown
!!! tip "Here is our plan:"

    1. First high-level action the learner will take
    2. Second high-level action
    3. Third action (if applicable)
```

The admonition title can vary: "Here is our plan:", "Let's start:", or similar. 2–3 items only — these are the high-level actions, not the detailed substeps. Infer from metadata and context.

**3. Goal section**

```markdown
## Goal

One paragraph (2–4 sentences). What the learner will have built or configured by the end of this step.
```

**4. Conceptual sections** (one `##` per key concept or rationale)

Add one or more `##` sections when a topic needs background before the hands-on steps. For example: why this approach was chosen, how a platform feature works, what inputs/outputs to expect. Infer from context and metadata. Keep each section short — 2–4 sentences per paragraph.

**5. Steps section**

```markdown
## Steps

### 1. Descriptive substep heading

[Action text.]

    ![Alt text describing the screenshot](images-folder/filename.png){ .screenshot }

### 2. Next substep

...
```

Use `### N. Descriptive Title` for sub-sections within Steps. Each substep has action text followed by its screenshot.

---

### Voice and tone

- **Person:** Second person — "you'll configure", "your agent", "open the panel"
- **Tense:** Present for descriptions ("the robot retrieves invoices"); future for instructions ("you'll add a connection")
- **Register:** Professional but conversational. Not formal, not casual. No hype.
- **Sentence length:** Short. One idea per sentence. Split anything over two lines.
- **Paragraphs:** 2–4 sentences maximum.
- **Avoid:** "In this section we will", "Please note that", "It is important to", "feel free to", "leverage" (use "use"), "utilize" (use "use"), "robust", "seamlessly"

---

### Platform names

- Bold on first appearance **per page**, plain text after.
- Always use exact names: **Agent Builder**, **Maestro**, **IXP**, **Action Center**, **ServiceNow**.
- Define acronyms on first use: `IXP (Intelligent eXtraction & Processing)`.
- UI labels match the platform exactly — copy them from the OCR text in metadata.

---

### Images

Reference every screenshot with the `.screenshot` class:

```markdown
![Alt text describing what is shown](images-folder/filename.png){ .screenshot }
```

**Alt text rules:**
- Describe what is shown, not what to do: "Agent Builder system prompt panel" not "Click here"
- Never leave alt text empty for informational screenshots

**Placement in numbered lists** — indent 4 spaces to keep the image inside the list item:

```markdown
1. Open **Agent Builder** and select **New Agent**.

    ![New Agent button in Agent Builder](images-folder/new-agent.png){ .screenshot }

2. Enter a name and click **Create**.
```

**Two-column layout** — use when a screenshot and its description should sit side by side:

```
[[[
Left column content (markdown)
|N|
Right column content (markdown)
]]]
```

Where N is the left-column width as a percentage. Three values supported:

| Value | Split |
|-------|-------|
| `\|30\|` | 30% left / 70% right |
| `\|50\|` | 50% left / 50% right |
| `\|70\|` | 70% left / 30% right |

Each delimiter (`[[[`, `|N|`, `]]]`) must be on its own line with no trailing spaces.

Typical pattern — text left, screenshot right (`|30|`):

```
[[[
Click on **Data Manager** in the left ribbon, then click "**+**" to add a new argument.
|30|
![Data Manager panel with add button highlighted](images-folder/data-manager.png){ .screenshot }
]]]
```

Typical pattern — screenshot left, text right (`|70|`):

```
[[[
![New agent created in Studio Web](images-folder/create-agent.png){ .screenshot }
|70|
In **Studio Web**, add a new Agent to your solution and name it:
```text
2-Way Matching Agent
` ` `
]]]
```

Default to one image per step. Use two only if a genuine before/after comparison adds value.

---

### Code blocks

Every prompt, configuration value, field text, or any text the learner must copy goes in a fenced code block — never inline code. MkDocs Material adds a copy button automatically.

Rules:
- The block must contain exactly what the learner pastes — no surrounding explanation, no placeholder comments, no extra blank lines at start/end
- Always include a language identifier for readable syntax highlighting: ` ```yaml `, ` ```json `, ` ```python `, ` ```text `
- Plain prose with no keywords uses ` ```text `
- Use the OCR text from metadata as the source of truth for prompts and config values

Example:

```markdown
Configure the system prompt:

` ` `text
You are an invoice matching agent. Your job is to compare the invoice data
against the corresponding Purchase Order and return a validation decision.
` ` `
```

---

### Admonitions

| Type | Use for |
|------|---------|
| `!!! tip` | Helpful shortcuts, plan for the lesson, contextual advice |
| `!!! info "Training Environment"` | Platform URL and tenant details |
| `!!! note` | Placeholder for content not yet migrated |
| `!!! warning` | Actions that could cause errors or data loss |

---

### Navigation

Do **not** add manual navigation links at the bottom of the page. Navigation is handled automatically by the MkDocs sidebar. Never add patterns like `[← Previous](prev.md) | [Next →](next.md)`.

---

## Step 4: Verify

After writing the file, read it back and check:
- Every image referenced exists in the images folder
- All copyable text (prompts, field values, config) is in fenced code blocks
- Platform names are bold on first appearance, plain after
- No manual navigation links at the bottom
- All two-column blocks have each delimiter on its own line
- Voice matches the rules above: second person, short sentences, no forbidden words

Report what was created and flag any screenshots that had low-confidence metadata so the user knows which sections to review manually.
