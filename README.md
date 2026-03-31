# Agentic Practice Workshop — Site Guide

How the site works, how to edit it manually, and what to ask Claude Code to do.

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
| `docs/*/images/` | Screenshots for each exercise |
| `docs/assets/images/` | Images shared across multiple pages |
| `.github/workflows/deploy.yml` | Auto-deploy on every push to `main` |
| `CLAUDE.md` | Authoring rules Claude reads automatically |

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
docs/categorizing-incidents/llm-with-context.md  ← Categorizing Incidents, step 1
docs/invoice-matching/add-agent.md               ← Invoice Matching, step 3
docs/invoice-matching-ixp/configure-agent.md     ← IXP exercise, step 3
docs/next-steps.md                               ← standalone page
```

The navigation order and labels are defined in `mkdocs.yml` under `nav:` — edit there to rename a menu item.

### Add a plain image

1. Save the image to the page's `images/` folder (e.g. `docs/invoice-matching/images/my-screenshot.png`).
2. Reference it in the `.md` file:

```markdown
![Description of what is shown](images/my-screenshot.png){ .screenshot }
```

Always use `.{ .screenshot }` for UI screenshots — it adds the border and shadow. Omit it for diagrams or decorative images.

### Resize an image

Add a `width` attribute:

```markdown
![Description](images/my-screenshot.png){ .screenshot width="600" }
```

Width is in pixels. Use this when a full-page screenshot renders too large. Common values: `500`–`800`.

### Add a caption below an image

Place italic text on the line immediately after the image tag:

```markdown
![Description](images/my-screenshot.png){ .screenshot }
*This caption appears centered below the image.*
```

### Two-column image layout

Three split ratios are available: `50/50`, `30/70`, and `70/30`.

**50 / 50 split:**

```html
<div class="img-cols img-cols-50" markdown>
<div markdown>
![Left image description](images/left.png){ .screenshot }
*Optional caption*
</div>
<div markdown>
![Right image description](images/right.png){ .screenshot }
*Optional caption*
</div>
</div>
```

**70 / 30 split** (wide left, narrow right):

```html
<div class="img-cols img-cols-70-30" markdown>
<div markdown>
![Main image](images/main.png){ .screenshot }
</div>
<div markdown>
![Detail](images/detail.png){ .screenshot }
</div>
</div>
```

**30 / 70 split** (narrow left, wide right): use `img-cols-30-70` instead.

> **Note:** These blocks require blank lines between the HTML and surrounding Markdown content — leave an empty line before and after the `<div>` block.

### Add a step to an existing page

Find the numbered list under `## Steps` in the relevant `.md` file and insert your step. Keep the indent consistent — images inside a numbered list need 4 spaces of indent to stay attached to the list item:

```markdown
3. Open the **Configuration** panel and click **Add**.

    ![Configuration panel open](images/config-panel.png){ .screenshot }

4. Enter a name and click **Save**.
```

### Add a callout box

Four types are available:

```markdown
!!! tip
    Shortcut or helpful hint.

!!! note
    Neutral information.

!!! info "Training Environment"
    Log in at [cloud.uipath.com/tpenlabs](https://cloud.uipath.com/tpenlabs) using tenant **AgenticPractice**.

!!! warning
    Action that could cause an error.
```

---

## What to Ask Claude Code

Use Claude Code (this tool) for anything that touches multiple files, requires consistency across the site, or involves restructuring.

### Add a new exercise

```
Add a new exercise called "Automating Email Triage". It should have an overview page
and 3 steps: "Configure the Agent", "Add Email Connector", "Test and Deploy".
Follow the existing exercise structure.
```

Claude will create the folder, all `.md` files, image folders, register everything in `mkdocs.yml`, and link the exercise from the home page.

### Migrate content from an external source

```
Migrate the content from [URL] into the page docs/invoice-matching/add-robot.md.
Replace the placeholder with real step-by-step instructions.
```

### Rewrite / optimize language on a page

```
Optimize the language in docs/categorizing-incidents/tools-and-escalations.md
following the tone rules in CLAUDE.md.
```

### Rename or restructure an exercise

```
Rename "Invoice Matching" to "2-Way Matching" everywhere — page titles, nav labels,
internal links, and the home page summary card.
```

### Update a prompt or code block across the site

```
The system prompt in docs/categorizing-incidents/llm-with-context.md has been updated.
The new version is: [paste prompt]. Update the code block on that page
and any other place the same prompt appears.
```

### Add images once you have the files

```
I've added images bpmn-01.png through bpmn-04.png to docs/invoice-matching/images/.
There are now 4 images — update create-bpmn.md to reference all of them
in the Steps section.
```

---

## Navigation Structure

The navigation is defined in `mkdocs.yml`:

```yaml
nav:
  - Home: index.md
  - Categorizing Incidents:
    - Overview: categorizing-incidents/index.md
    - LLM with Context: categorizing-incidents/llm-with-context.md
    - Tools and Escalations: categorizing-incidents/tools-and-escalations.md
  - Invoice Matching:
    - Overview: invoice-matching/index.md
    - 1. Create BPMN Diagram: invoice-matching/create-bpmn.md
    ...
```

To add a page to the nav, add a line here. To rename a menu item, change the label before the colon. The `.md` filename stays the same.

---

## Authoring Rules

`CLAUDE.md` at the project root contains the full set of writing and formatting rules. Claude reads this automatically every session. The key rules:

- All prompt text the learner copies goes in a fenced code block (` ```text `)
- Every step page ends with a navigation footer: `[← Previous](prev.md) | [Next →](next.md)`
- Platform names bold on first use per page: **Agent Builder**, **Maestro**, **IXP**, **Action Center**
- Avoid: "leverage", "utilize", "robust", "seamlessly", "In this section we will"
- Sentences: one idea per sentence, max two lines

---

## File Naming Conventions

| Thing | Convention | Example |
|-------|-----------|---------|
| Exercise folder | lowercase, hyphenated | `invoice-matching-ixp/` |
| Step page | `verb-noun.md` | `add-robot.md`, `configure-agent.md` |
| Image file | lowercase, hyphenated | `agent-builder-prompt-panel.png` |
| Shared image | lives in `docs/assets/images/` | `../assets/images/maestro-overview.png` |

---

## Contributing with Claude Code Skills

This repo ships with two Claude Code skills that automate the most repetitive authoring tasks. Any team member with Claude Code installed gets them automatically — no setup needed beyond cloning the repo.

### Prerequisites

1. **Claude Code** — installed and authenticated ([claude.ai/code](https://claude.ai/code))
2. **Azure OpenAI credentials** — required only for the `/new-lesson` skill. Copy `scripts/.env.example` to `scripts/.env` and fill in your own values. This file is gitignored and must never be committed.
3. **Python dependencies** — `pip install openai requests beautifulsoup4 numpy python-dotenv pillow` (required for the metadata extraction script)

### Available skills

| Skill | What it does | When to use |
|-------|-------------|-------------|
| `/new-exercise` | Scaffolds a new exercise: creates folders, overview page, step stubs, updates `mkdocs.yml` nav, and adds an index card to the home page | Starting a new exercise from scratch |
| `/new-lesson` | Builds a complete lesson page from screenshots: runs metadata extraction, reads the results, and generates step-by-step content with images and code blocks | After uploading screenshots to an exercise's images folder |

### Documentation references

Each exercise folder contains a `documentation.md` file. **Add a link to this file every time you upload new screenshots.** The links point to official product documentation relevant to what those screenshots show.

```
docs/<exercise-slug>/documentation.md
```

Example entry:
```
- https://docs.uipath.com/agents/automation-cloud/latest/user-guide/building-an-agent-in-studio-web
```

The metadata extraction script reads this file before processing images. It fetches and embeds each URL's text content (text only, no images) using Azure OpenAI embeddings, then uses this as context when analyzing screenshots. URLs already embedded in a previous run are skipped automatically — only new links are fetched. The embedded cache (`documentation.cache.json`) is gitignored.

The same links appear in a **Learn more** table at the end of each generated lesson page.

### Typical workflow

```
1. /new-exercise     →  provide name, description, and step list
2. Upload screenshots to docs/<exercise-slug>/<step>.images/
3. Add relevant docs links to docs/<exercise-slug>/documentation.md
4. /new-lesson       →  provide exercise slug, step number, images folder path
5. Review generated page, edit as needed
6. mkdocs build      →  verify no errors
7. git push          →  site deploys automatically
```

### Example invocations

```
/new-exercise
Name: Expense Report Processing
Slug: expense-report-processing
Description: Automate expense report review using IXP and human validation
Steps: 1. Upload Report — robot retrieves PDFs, 2. Extract Data — IXP reads fields, 3. Review Exceptions — Action Center task
```

```
/new-lesson
Exercise: expense-report-processing
Step: 2
Name: Extract Data
Images: docs/expense-report-processing/extract-data.images/
Context: IXP project reads line items from expense receipts. Outputs amount, category, date fields.
```

### Authoring conventions

All content rules are in `CLAUDE.md` at the project root. Claude reads it automatically every session. When you encounter a pattern question (how to structure a page, how to format a code block, what tone to use), check CLAUDE.md first.

To add a new rule or update an existing one, edit `CLAUDE.md` directly and commit. This keeps conventions versioned and visible to all contributors.



There's no perfect WYSIWYG editor for MkDocs specifically, because MkDocs uses custom syntax (admonitions, image attributes) that no generic editor understands. But here's the practical breakdown:                    
  ---                                                       
  For live preview while editing 
                                                                                                                                      
  VS Code (what you already have) + split pane
                                                                                                                                    
  You're already using VS Code. Press Cmd+Shift+P → "Markdown: Open Preview to the Side" — you get the .md file on the left and a rendered preview on the right as you type.                                                                                                                                                        
                                                                                                                           
  Even better: keep mkdocs serve running in Terminal, open http://127.0.0.1:8000 in your browser — the actual styled site updates every time you save a file.      
  That's your real preview with the correct theme, images, and formatting.
                                                                                                                                                                   
  ---                                                                                                                                                              
  For the painful parts — just ask Claude Code
                                                                                                                                                                   
  The things that are genuinely painful to write manually:  
                                                                                                                                                                   
  - Two-column image layouts → "Add a 70/30 image split after step 3 on page X, left image is robot.png, right is output.png"                                      
  - Admonition boxes → "Add a tip box after step 5 saying..."                                                                                                      
  - Resizing images → "Resize all images on the configure-agent page to width 700"                                                                                 
  - Reorganizing a page → "Move the Context Grounding section before the Prompts section"                                                                          
                                                                                                                                                                   
  You write the content in Typora or directly in VS Code, Claude handles the formatting markup.                                                                    
                                                                                                                                                                   
  ---                                                                                                                                                              
  The practical workflow                                    
                        
  Write/edit text   →  Typora or VS Code
  Preview           →  browser at localhost:8000 (mkdocs serve running)                                                                                            
  Formatting/CSS    →  ask Claude Code                                                                                                                             
  Publish           →  git push (automatic)                                                                                                                        
                                                                                                                                                                   
  The only command you ever need to remember:               
                                                                                                                                                                   
  /Users/sergey/Library/Python/3.9/bin/mkdocs serve         
                                                                                                                                                                   
  Run it once in Terminal, leave it open, and your browser becomes a live preview of the site as you edit.