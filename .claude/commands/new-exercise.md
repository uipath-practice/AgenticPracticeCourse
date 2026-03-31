Scaffold a new exercise for the Agentic Automation Workshop site.

## Collect inputs

If any of the following are missing from the user's message, ask for them before proceeding:

1. **Exercise slug** — lowercase, hyphenated folder name (e.g., `expense-report-processing`). Infer from the display name if not provided.
2. **Display name** — title as it appears in the nav (e.g., "Expense Report Processing")
3. **One-paragraph description** — what the learner will build and which platform products they'll use
4. **Steps** — list of step names with brief descriptions (e.g., "1. Upload Report — robot retrieves PDFs from a storage bucket")

---

## What to create

### 1. Folder structure

- `docs/<exercise-slug>/` — exercise folder (create by adding files into it)
- `docs/<exercise-slug>/images/.gitkeep` — empty file so git tracks the images folder
- `docs/<exercise-slug>/documentation.md` — documentation reference file (see template below)

**`documentation.md` template:**

```markdown
# Documentation References — <Display Name>

Add a link here for each new set of screenshots you upload to this exercise.
The metadata extraction script reads this file and embeds the linked documentation
as context for image analysis. New links are fetched and embedded automatically
on the next run; previously embedded links are not re-fetched.

## Links

<!-- Add URLs below, one per line, prefixed with - -->
```

---

### 2. Exercise overview page — `docs/<exercise-slug>/index.md`

Use this exact structure:

```markdown
# Display Name

**Bold subtitle — one line describing what the learner builds.**

---

## Overview

2–3 sentences. Name the key platform features used. Explain what the learner will have
automated or built by the end.

1. [Step One Name](1-verb-noun.md) — brief description of what happens in this step
2. [Step Two Name](2-verb-noun.md) — brief description
3. [Step Three Name](3-verb-noun.md) — brief description

---

!!! tip "Training Environment"
    Log in at [cloud.uipath.com/tpenlabs](https://cloud.uipath.com/tpenlabs) using tenant **AgenticPractice**.
```

**Writing rules for the overview page:**
- `# Title` is a noun phrase — the exercise name, not a verb phrase
- The bold subtitle is one sentence: what the learner builds
- `## Overview` names the platform products (bold on first use: **Agent Builder**, **Maestro**, **IXP**, **Action Center**)
- Each step in the numbered list links to its file and has a plain-English description
- No extra sections — the overview page is intentionally short

---

### 3. Step pages — `docs/<exercise-slug>/N-verb-noun.md`

File names: `N-verb-noun.md` — numeric prefix followed by a verb-noun slug.  
Examples: `1-create-bpmn.md`, `2-configure-robot.md`, `3-configure-agent.md`

Use this stub structure for each step page:

```markdown
# Step N — Verb Noun

!!! tip "Here is our plan:"

    1. [First action the learner will take — infer from the step description]
    2. [Second action]
    3. [Third action if applicable]

## Goal

One short paragraph: what the learner will have built or configured by the end of this step.

## Steps

<!-- Add step-by-step instructions with screenshots here -->

!!! note "Content migration in progress"
    Detailed steps and screenshots will be added here.
```

**Writing rules for the tip admonition:**
- The title ("Here is our plan:", "Let's start:", etc.) can vary — keep it natural
- 2–3 bullet points only — the high-level actions, not the detailed substeps
- Infer from the step description the user provided

**Writing rules for `## Goal`:**
- One paragraph, 2–4 sentences maximum
- What the learner will have *built*, not what they will *do*
- Second person: "you'll have configured", "your agent will be able to"

---

### 4. Outro page — `docs/<exercise-slug>/you-did-it.md`

Every exercise ends with a `you-did-it.md` page. Use this structure:

```markdown
# You did it!

!!! tip "Congratulations!"

    You've built a complete [one-line description of what they built].

---

## What you built

[2–3 sentences summarising the end-to-end process.]

| Component | Role |
|-----------|------|
| **[Component 1]** | [What it does in this exercise] |
| **[Component 2]** | [What it does] |
| **[Component 3]** | [What it does] |

---

## Next steps

### 1. Publish and run your process

[Brief instructions on publishing and triggering a run.]

### 2. Explore the results

[What to look at after a successful run — dashboards, logs, outputs.]

---

## Keep iterating

[2–3 short suggestions for how the learner could extend or improve what they built.]

---

## Learn more

| Resource | Description |
|----------|-------------|
| [Resource name](URL) | One-sentence description |
```

**For the Learn more table:**
Read `docs/<exercise-slug>/documentation.md` and extract all URLs. For each URL, derive a human-readable name from the URL slug (e.g., `building-an-agent-in-studio-web` → "Building an Agent in Studio Web"). Write a one-sentence description based on the URL slug and page topic. If `documentation.md` has no URLs yet, leave a placeholder row.

---

### 5. Update `mkdocs.yml` nav

Add the exercise before `- Next Steps: next-steps.md` (or at the end of the exercise list if Next Steps doesn't exist). Follow the existing indentation and pattern:

```yaml
- Display Name:
  - Overview: exercise-slug/index.md
  - 1. Step One Name: exercise-slug/1-verb-noun.md
  - 2. Step Two Name: exercise-slug/2-verb-noun.md
  - 3. Step Three Name: exercise-slug/3-verb-noun.md
  - You did it!: exercise-slug/you-did-it.md
```

Nav labels for steps are prefixed with their number: `1. Create BPMN Process`, `2. Configure a Robot`.

---

### 6. Update `docs/index.md`

Add a summary card for the new exercise under `## Exercises` (or wherever the other exercise cards are). Read the home page first and match the format of the existing cards exactly — same heading level, same table structure, same `[Start Exercise →](path)` link pattern.

---

## Voice and tone for generated content

These rules apply to all text you write — overview page, step stubs, and any prose:

- **Person:** Second person — "you'll configure", "your agent", "open the panel"
- **Tense:** Present for descriptions ("the robot retrieves invoices"); future for instructions ("you'll add a connection")
- **Register:** Professional but conversational. Not formal, not casual. No hype.
- **Sentence length:** Short. One idea per sentence. Split anything over two lines.
- **Paragraphs:** 2–4 sentences maximum.
- **Avoid:** "In this section we will", "Please note that", "It is important to", "feel free to", "leverage" (use "use"), "utilize" (use "use"), "robust", "seamlessly"
- **Platform names:** Bold on first appearance per page, plain text after. Always use exact names: **Agent Builder**, **Maestro**, **IXP**, **Action Center**, **ServiceNow**. Define acronyms on first use: `IXP (Intelligent eXtraction & Processing)`

---

## Verify

After creating all files, run `mkdocs build` to check for broken links and nav errors:

```bash
mkdocs build
```

If mkdocs is not on your PATH, use the full installation path (on macOS with Python 3.9: `~/Library/Python/3.9/bin/mkdocs build`).

Report any build errors. If the build passes, summarize what was created: files, nav entries, and index card.
