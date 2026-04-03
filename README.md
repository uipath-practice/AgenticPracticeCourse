# Agentic Practice Workshop — Site Guide

How the site works, how to edit it, and what to ask Claude Code to do.

---

## How It Works

```
docs/*.md files
      ↓
  MkDocs builds HTML
      ↓
  GitHub Actions pushes to gh-pages branch
      ↓
  GitHub Pages serves the live site
```

| File / Folder | Purpose |
|---------------|---------|
| `docs/` | All page content — one `.md` file per page |
| `mkdocs.yml` | Site config: theme, navigation, plugins |
| `docs/stylesheets/extra.css` | Custom CSS (image styles, two-column layouts) |
| `docs/*/<step>.images/` | Screenshots per lesson (e.g., `configure-agent.images/`) |
| `docs/assets/images/` | Images shared across multiple pages |
| `.github/workflows/deploy.yml` | Auto-deploy on every push to `main` |
| `Master/` | Authoritative course rules, templates, and formatting reference |
| `CLAUDE.md` | Compact authoring rules Claude reads automatically; points to Master/ |
| `Archive/` | Archived exercises and lessons — gitignored, never deployed |

**Publishing is automatic.** Push to `main` → GitHub Actions runs → site updates in ~60 seconds. You never run a deploy command manually.

---

## Preview Locally

```bash
/Users/sergey/Library/Python/3.9/bin/mkdocs serve
```

Open `http://127.0.0.1:8000` in your browser. The site reloads live as you save files.

To check for broken links before pushing:

```bash
/Users/sergey/Library/Python/3.9/bin/mkdocs build
```

---

## Making Changes Manually

### Edit wording or a paragraph

Open the relevant `.md` file in any text editor, make the change, save, and push.

```
docs/categorizing-incidents/llm-with-context.md     ← Categorizing Incidents, lesson 1
docs/invoice-matching-ixp/3-configure-agent.md      ← IXP exercise, lesson 3
docs/next-steps.md                                  ← standalone page
```

The navigation order and labels are defined in `mkdocs.yml` under `nav:` — edit there to rename a menu item.

### Quick formatting reference

For full details with examples, see `Master/Formatting.md`. Here are the essentials:

**Add a screenshot:**
```markdown
![Description of what is shown](step-slug.images/filename.png){ .screenshot }
```

**Resize a screenshot** (wide images use `width="900"`, others `width="700"` or similar):
```markdown
![Description](step-slug.images/filename.png){ .screenshot width="700" }
```

**Two-column layout** (text next to screenshot):
```
[[[
Click on **Data Manager** and add a new argument.
|30|
![Data Manager panel](step-slug.images/4-data-manager.png){ .screenshot }
]]]
```

Supported ratios: `|30|` (30/70), `|50|` (50/50), `|70|` (70/30). Each delimiter on its own line.

**Add a callout box:**
```markdown
!!! tip "Title"
    Shortcut or helpful hint.

!!! warning "Title"
    Action that could cause an error.
```

Four types available: `tip`, `info`, `note`, `warning`.

**Image inside a numbered list** (4-space indent to preserve numbering):
```markdown
1. Open **Agent Builder** and select **New Agent**.

    ![New Agent button](step-slug.images/1-new-agent.png){ .screenshot }

2. Enter a name and click **Create**.
```

---

## Authoring Rules

All course authoring rules live in the `Master/` directory:

| File | Covers |
|------|--------|
| [Master/README.md](Master/README.md) | Entry point — what each file contains, exercise lifecycle |
| [Master/Filesystem.md](Master/Filesystem.md) | Directory structure, file/folder naming, Archive folder |
| [Master/CourseStructure.md](Master/CourseStructure.md) | Page templates (Overview, Lesson, Summary) |
| [Master/Formatting.md](Master/Formatting.md) | Images, code blocks, layouts, admonitions |
| [Master/Language.md](Master/Language.md) | Voice, tone, word choices |
| [Master/HOWTO.md](Master/HOWTO.md) | End-to-end workflows for creating, publishing, removing, and reviewing content |

`CLAUDE.md` at the project root has a compact summary and points to Master/ for details. Claude reads it automatically every session. To add or update a rule, edit the relevant Master file and commit.

---

## What to Ask Claude Code

Use Claude Code for anything that touches multiple files, requires consistency, or involves restructuring.

**Add a new exercise (draft — not visible to learners yet):**
```
/new-exercise
Name: Expense Report Processing
Description: Automate expense report review using IXP and human validation
Steps: 1. Upload Report — robot retrieves PDFs, 2. Extract Data — IXP reads fields, 3. Review Exceptions — Action Center task
```

**Generate a lesson from screenshots:**
```
/new-lesson
Exercise: expense-report-processing
Step: 2
Name: Extract Data
Images: docs/expense-report-processing/extract-data.images/
```

**Publish an exercise when it's ready for learners:**
```
/publish-exercise expense-report-processing
```

**Review a lesson or exercise:**
```
/review-lesson invoice-matching-ixp/3-configure-agent
/review-exercise invoice-matching-ixp
```

**Remove a lesson or an entire exercise:**
```
/remove-lesson invoice-matching-ixp/2-configure-robot
/remove-exercise invoice-matching-ixp
```

**Other common requests:**
- "Optimize the language in docs/categorizing-incidents/tools-and-escalations.md"
- "Update the system prompt code block on page X — the new version is: [paste]"
- "Add a 70/30 image split after step 3 on page X"

---

## Contributing with Claude Code Skills

This repo ships with Claude Code skills that automate course authoring. Any team member with Claude Code installed gets them automatically.

### Prerequisites

1. **Claude Code** — installed and authenticated ([claude.ai/code](https://claude.ai/code))
2. **Azure OpenAI credentials** — required for `/new-lesson`. Copy `scripts/.env.example` to `scripts/.env` and fill in your values. This file is gitignored.
3. **Python dependencies** — `pip install openai requests beautifulsoup4 numpy python-dotenv pillow`

### Available skills

| Skill | What it does | When to use |
|-------|-------------|-------------|
| `/new-exercise` | Scaffolds a new exercise: folders, stubs — **draft mode, not in nav** | Starting a new exercise from scratch |
| `/new-lesson` | Builds a lesson page from screenshots: extracts metadata, generates content | After uploading screenshots to a lesson's images folder |
| `/publish-exercise` | Adds a draft exercise to the navigation and home page | When the exercise is ready for learners |
| `/review-lesson` | Reviews a single lesson against Master/ rules | After editing or finalizing a lesson |
| `/review-exercise` | Reviews an entire exercise for per-page and cross-lesson coherence | After all lessons are reviewed individually |
| `/remove-lesson` | Archives a lesson and removes it from navigation — prompts for confirmation | Retiring a lesson or cleaning up after a test run |
| `/remove-exercise` | Archives an entire exercise and removes it from navigation — prompts for confirmation | Retiring an exercise or cleaning up after a test run |

### Draft and publish model

Exercises start in **draft mode** — files exist in `docs/` but are not visible in the navigation or on the home page. This lets you build and test content without exposing it to learners.

```
/new-exercise   →  creates files, not visible in nav
/new-lesson     →  adds lessons, still not visible in nav
/publish-exercise  →  adds nav entry and home page card — learners can see it
```

Archived content goes to `Archive/` at the project root. This folder is gitignored and never deployed.

### Documentation references

Each exercise folder contains a `documentation.txt` file. **Add a link every time you upload new screenshots.** The metadata extraction script reads this file and embeds each URL's content as context for screenshot analysis.

```
docs/<exercise-slug>/documentation.txt
```

### Typical workflow

```
1. /new-exercise          →  provide name, description, and step list (draft mode)
2. Upload screenshots to docs/<exercise-slug>/<step>.images/
3. Add relevant docs links to docs/<exercise-slug>/documentation.txt
4. /new-lesson            →  provide exercise slug, step number, images folder path
5. Review generated page, edit as needed
6. /review-lesson         →  check against Master/ rules
7. /review-exercise       →  cross-lesson coherence check
8. /publish-exercise      →  add to nav and home page
9. mkdocs build           →  verify no errors
10. git push              →  site deploys automatically
```

---

## Editing Tips

- **VS Code** with split pane: `Cmd+Shift+P` → "Markdown: Open Preview to the Side"
- **Best preview**: keep `mkdocs serve` running, open `http://127.0.0.1:8000` — it updates live as you save
- **For formatting hassles** (two-column layouts, admonitions, resizing): ask Claude Code
- Write content in VS Code, let Claude handle the markup
