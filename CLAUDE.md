# CLAUDE.md — Agentic Practice Workshop Site

This file is read automatically on every Claude Code session in this project.
Apply all rules below to every task involving this site — no reminders needed.

---

## Project Purpose

A GitHub Pages–hosted MkDocs site that guides learners through hands-on UiPath agentic automation exercises. The primary audience is workshop participants who are practicing for the first time — not developers, not UiPath experts. Writing and structure should reflect that.

**Live site:** https://s-shumilov.github.io/AgenticPracticeCourse/
**Source repo:** https://github.com/s-shumilov/AgenticPracticeCourse
**Theme:** MkDocs Material (`mkdocs.yml`)
**Deploy:** GitHub Actions on every push to `main` (`.github/workflows/deploy.yml`)

---

## Site Structure

### Folder layout
```
docs/
  index.md                         ← Home page
  assets/
    images/                        ← Shared images used across multiple pages
  stylesheets/
    extra.css                      ← Custom image styles (do not modify)
  <exercise-slug>/
    index.md                       ← Exercise overview (always present)
    <step-slug>.md                 ← One file per step/sub-topic
    images/                        ← Screenshots for this exercise's pages
  next-steps.md                    ← Standalone page
```

### Naming conventions
- Exercise folder names: lowercase, hyphenated (`categorizing-incidents`, `invoice-matching-ixp`)
- Step file names: `verb-noun.md` — describes the action (`add-robot.md`, `configure-agent.md`, `create-bpmn.md`)
- No numeric prefixes in filenames; numbers appear in the nav label only

### Nav registration (mkdocs.yml)
**Always update `nav:` in `mkdocs.yml` when adding, removing, or renaming a page.**
Nav labels for steps are prefixed: `1. Create BPMN Diagram`, `2. Add a Robot`, etc.
Exercise overview pages use label: `Overview`.

---

## Page Structure

### Home page (`docs/index.md`)
1. `# H1 Title` — site/workshop name
2. `**Bold subtitle**` — one-line descriptor
3. `---`
4. `!!! info "Training Environment"` callout with platform URL, tenant, contact
5. `## What You'll Build` — 2–3 sentences framing the exercises
6. Core principle as blockquote (`> ...`)
7. `---`
8. One `###` section per exercise with a summary table and `[Start Exercise →](path)` link
9. `---`
10. `## Key Concepts` — glossary of platform terms used across the site

### Exercise overview page (`<exercise>/index.md`)
1. `# Exercise Name` — noun phrase, matches nav label
2. `**Bold subtitle**` — one line: what the learner builds
3. `---`
4. `## Overview` — 2–3 sentences; mention the key platform feature(s) used
5. Phase/component table if the exercise has multiple phases
6. Numbered list of steps, each linking to its page
7. `---`
8. `!!! tip "Training Environment"` callout at the bottom

### Step page (`<exercise>/<step>.md`)
1. `# Step N — Verb Noun` (or a descriptive title if not sequential)
2. `!!! tip "Let's start"` admonition — numbered list of 2–3 actions for this step (what the learner will do)
3. `## Goal` — one short paragraph: what the learner will have built by the end
4. Conceptual sections (one `##` per key concept or sub-task)
5. `## Steps` (or a descriptive heading) — numbered step-by-step instructions; use a placeholder comment if not yet written

---

## Language and Tone

- **Audience:** First-time workshop participants. Assume no prior UiPath knowledge.
- **Voice:** Second person, direct — "you'll configure", "your agent", "open the panel".
- **Tense:** Present for descriptions ("the robot retrieves invoices"); future for instructions ("you'll add a connection").
- **Register:** Professional but conversational. Not formal, not casual. No hype.
- **Sentence length:** Short. One idea per sentence. If a sentence runs more than two lines, split it.
- **Paragraphs:** Two to four sentences maximum.
- **Avoid:** "In this section we will", "Please note that", "It is important to", "feel free to", "leverage" (use "use"), "utilize" (use "use"), "robust", "seamlessly".
- **Platform names:** Bold on first appearance per page, plain text after. Always use exact names: **Agent Builder**, **Maestro**, **IXP**, **Action Center**, **ServiceNow**.
- **Acronyms:** Define on first use per page: `IXP (Intelligent eXtraction & Processing)`.

---

## Layout and Formatting

### Horizontal rules (`---`)
Use to separate the header block from the body, and between major top-level sections on overview/home pages. Do not use within step pages (use `##` headings instead).

### Tables
Use for:
- Phase/step summaries on overview pages (columns: Phase/Step | Focus/Description)
- Component role comparisons (columns: Component | Role)
- API or field references

Keep table rows short. If a cell would wrap awkwardly, convert to a description list instead.

### Admonitions
| Type | Use for |
|------|---------|
| `!!! info` | Training environment details (platform URL, tenant) |
| `!!! tip` | Helpful shortcuts, contextual advice |
| `!!! note` | Placeholder notice for content not yet migrated |
| `!!! warning` | Actions that could cause errors or data loss |

### Code blocks
**Every prompt, configuration snippet, or text the learner must copy gets a fenced code block — never inline text.**

MkDocs Material adds a copy-to-clipboard button automatically to every code block (configured via `content.code.copy` in `mkdocs.yml`). This means the code block IS the copy mechanism.

Rules:
- The code block must contain exactly what the learner pastes — no surrounding explanation, no placeholder comments inside the block, no extra blank lines at start/end.
- If a page shows a prompt that the learner enters into Agent Builder or any text field, that prompt goes in a code block. If the prompt is later updated on the page, update the code block too — they must always be identical.
- Use language identifiers: ` ```yaml `, ` ```json `, ` ```python `, ` ```text ` (for prompts and plain text). Never leave the opening fence bare unless the content is truly language-agnostic pseudocode.
- Pseudocode / logic flows use ` ```text `.

### Lists
- Numbered lists: sequential steps only.
- Bullet lists: non-sequential items, feature lists, "you'll learn" sections.
- Max two levels of nesting. If you need a third level, restructure as a new section.

### Images

**Where images live:**
- Screenshots specific to one exercise → `docs/<exercise-slug>/images/`
- Images shared across multiple pages → `docs/assets/images/`

**File naming:** lowercase, hyphenated, descriptive of what is shown:
`agent-builder-system-prompt.png`, `bpmn-overview-diagram.png`, `action-center-task.png`

**Supported formats:** PNG for screenshots (preferred), JPG for photos, SVG for diagrams.

**Referencing images in Markdown — three patterns:**

1. Plain image (no styling):
```markdown
![Alt text describing what the screenshot shows](images/filename.png)
```

2. Screenshot with border and shadow (use for all UI screenshots):
```markdown
![Alt text](images/filename.png){ .screenshot }
```

3. Screenshot with a visible caption:
```markdown
![Alt text](images/filename.png){ .screenshot }
*Caption text shown below the image*
```

Always use `.screenshot` for UiPath UI screenshots — it adds a subtle border and shadow that visually separates the screenshot from the page background.

**Sizing** — only add `width` when the image would otherwise render too large (full-page screenshots):
```markdown
![Alt text](images/filename.png){ .screenshot width="700" }
```

**Alt text rules:**
- Describe what is shown, not what to do: "Agent Builder system prompt configuration panel" not "Click here".
- Never leave alt text empty for informational screenshots.
- Decorative dividers or icons may use empty alt: `![](images/divider.svg)`.

**From a shared folder** (when the same image is used on multiple pages):
```markdown
![Alt text](../assets/images/filename.png){ .screenshot }
```

**Position in page:** Images appear inside the `## Steps` numbered list, directly after the step text they illustrate. One image per step is the default; use two only if a before/after comparison is genuinely needed.

Example step with image:
```markdown
1. Open **Agent Builder** and select **New Agent**.

    ![New Agent button in Agent Builder](images/new-agent-button.png){ .screenshot }

2. Enter a name for your agent and click **Create**.
```

Note the 4-space indent — this keeps the image inside the numbered list item so the list numbering doesn't reset.

### Links
- Internal links: relative paths (`../invoice-matching/index.md`).
- External URLs: always use Markdown link syntax, never bare URLs. Display text should be the domain or a descriptive label, not the raw URL.
- Platform URL: always `[cloud.uipath.com/tpenlabs](https://cloud.uipath.com/tpenlabs)`.

---

## Content Conventions

### Steps section placeholder
When detailed steps haven't been written yet, use exactly this pattern:

```markdown
## Steps

<!-- Add step-by-step instructions with screenshots here -->

!!! note "Content migration in progress"
    Detailed steps and screenshots will be added here. In the meantime, refer to the [original training site](https://sites.google.com/uipath.com/tpenlabs/home).
```

Remove this block entirely when real steps are added. Never leave both the placeholder and real steps on the same page.

### "You'll learn" lists
Used in exercise overview pages to summarize learning outcomes per phase. Format:

```markdown
**You'll learn:**
- Item one
- Item two
- Item three
```

Never use "You will learn:" (contractions preferred) or nested bullets here.

### Glossary terms (Key Concepts)
Each entry on the home page follows this format — bold term, em-dash, definition:

```markdown
**Term** — One-sentence definition that connects to what the learner will do with it.
```

No period at end. No paragraph spacing between entries.

### Training environment callout
Standard text — use exactly this in exercise overview pages:

```markdown
!!! tip "Training Environment"
    Log in at [cloud.uipath.com/tpenlabs](https://cloud.uipath.com/tpenlabs) using tenant **AgenticPractice**.
```

---

## When Adding a New Exercise

1. Create `docs/<exercise-slug>/` folder.
2. Create `docs/<exercise-slug>/images/` folder (add `.gitkeep` so git tracks it).
3. Create `index.md` following the exercise overview structure above.
4. Create one `.md` file per step following the step page structure above.
5. Add all new pages to `nav:` in `mkdocs.yml` in the correct position.
6. Add a summary card for the exercise to `docs/index.md` under `## Exercises`.
7. Run `mkdocs build` locally to verify no broken links or build errors before committing.

## When Editing an Existing Page

- Match the existing page's structure exactly. Don't introduce new section patterns.
- **Never remove sections, paragraphs, or explanatory text when migrating or editing content.** Migrate all text from the source; only adjust wording to fit the voice and tone rules. If a paragraph feels informal or wordy, rephrase it — don't delete it.
- If a page has a `!!! note "Content migration in progress"` block and you're adding real content to `## Steps`, remove the placeholder block entirely.
- If you edit a prompt displayed in a code block, check the rest of the page — if the same prompt text appears anywhere else (description, table, inline), update all occurrences to match.
- Do not add new admonition types not listed in this file without a clear reason.

## When Optimizing Language

- Apply all language rules in this file.
- **Never remove sections, paragraphs, or blocks of text.** Every block exists for a reason. Work within each sentence or paragraph — adjust wording, not scope.
- Preserve technical accuracy — do not reword platform names, step names, or process descriptions without understanding the content.
- Adjust phrasing to match the voice and tone rules, but keep all explanatory content intact. Explanatory paragraphs that give context or motivation are not "filler" — do not cut them.
- **Capitalised mid-sentence nouns are acceptable.** Do not change capitalisation of domain concepts such as "Invoice", "Purchase Order", "Supplier", "Storage Bucket" — the author may capitalise these intentionally for emphasis or consistency with UI labels.
- **Describing the same scenario in more than one section is acceptable.** Only flag duplication when the exact same paragraph appears verbatim in two places.
- After editing, re-read the page aloud in your head. If a sentence sounds awkward or would confuse a first-time learner, rewrite it.

---

## mkdocs.yml — Do Not Change Without Reason

The following settings are intentional — do not modify them unless explicitly asked:
- Theme: `material`, palette: deep orange / slate
- Features: `navigation.tabs`, `navigation.sections`, `navigation.top`, `navigation.footer`, `content.code.copy`
- Extensions: all currently listed — they are used across the site
- `site_url`: must match the GitHub Pages URL exactly

---

## Local Preview

```bash
/Users/sergey/Library/Python/3.9/bin/mkdocs serve
```

Build check before committing:
```bash
/Users/sergey/Library/Python/3.9/bin/mkdocs build
```
