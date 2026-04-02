# HOWTO — Course Authoring Workflows

Step-by-step guides for every course authoring task. Covers both the assisted (Claude Code) and manual approaches.

---

## Workflow 1: Create a new exercise from scratch

### What you need before starting

- **Exercise name** — display name (e.g., "Expense Report Processing")
- **One-paragraph description** — what the learner will build and which platform features they'll use
- **List of lessons** — names with brief descriptions (e.g., "1. Upload Report — robot retrieves PDFs from a storage bucket")

### Using Claude Code

```
/new-exercise
Name: Expense Report Processing
Slug: expense-report-processing
Description: Automate expense report review using IXP extraction and human validation in Action Center.
Steps: 1. Upload Report — robot retrieves PDFs, 2. Extract Data — IXP reads fields, 3. Review Exceptions — Action Center task
```

The skill creates all folders, stub pages, updates `mkdocs.yml`, and adds a card to the home page. Review the generated content and adjust as needed.

### Manual approach

1. Create the exercise folder: `docs/<exercise-slug>/`
2. Create image folders for each lesson: `docs/<exercise-slug>/<step-slug>.images/.gitkeep`
3. Create `documentation.txt` with the standard header (see [Filesystem.md](Filesystem.md))
4. Write `index.md` following the overview template in [CourseStructure.md](CourseStructure.md)
5. Write stub lesson files (`1-verb-noun.md`, `2-verb-noun.md`, etc.) following the lesson template
6. Write `you-did-it.md` following the summary template
7. Register all pages in `mkdocs.yml` nav section
8. Add an exercise card to `docs/index.md`
9. Run `mkdocs build` to verify no errors

---

## Workflow 2: Generate a lesson from screenshots

This is the primary content generation workflow. You'll do this for each lesson after scaffolding the exercise.

### Prerequisites

- Exercise already scaffolded (Workflow 1 complete)
- Screenshots uploaded to the lesson's image folder: `docs/<exercise-slug>/<step-slug>.images/`
- `scripts/.env` configured with Azure OpenAI credentials
- Python dependencies installed: `pip install openai requests beautifulsoup4 numpy python-dotenv pillow`

### Steps

1. **Add documentation links** — Edit `docs/<exercise-slug>/documentation.txt` and add URLs to official UiPath docs relevant to this lesson's topic. The extraction script uses these as context.

2. **Run the lesson generation skill:**
   ```
   /new-lesson
   Exercise: expense-report-processing
   Step: 2
   Name: Extract Data
   Images: docs/expense-report-processing/extract-data.images/
   Context: IXP project reads line items from expense receipts. Outputs amount, category, date fields.
   ```

3. **What happens behind the scenes:**
   - Script fetches and embeds any new documentation URLs
   - Script analyzes each screenshot and writes `.metadata.json` files
   - Claude reads the metadata and builds the complete lesson page
   - Screenshots are placed in context with step-by-step instructions

4. **Review the generated page** — Check that:
   - Screenshots are in the right order and context
   - Code blocks contain exactly what the learner should copy
   - Platform names are bold on first use
   - Technical accuracy matches what the screenshots actually show

5. **Edit and finalize** — Add details the screenshots don't capture:
   - Business context and explanations
   - Tips and warnings from your domain expertise
   - Cross-references to other lessons or exercises

---

## Workflow 3: Review a lesson

After you've written and edited a lesson, run the review skill to check it against all formatting and language rules.

```
/review-lesson categorizing-incidents/llm-with-context
```

The skill reads the lesson page and checks it against:
- [CourseStructure.md](CourseStructure.md) — page structure rules
- [Formatting.md](Formatting.md) — all formatting patterns
- [Language.md](Language.md) — voice, tone, word choices

It reports issues organized by severity:
- **Must fix** — broken formatting, missing required sections, forbidden words
- **Recommend** — structure deviations, inconsistent patterns
- **Info** — minor style suggestions

Fix the must-fix items, consider the recommendations, and ignore the info items at your discretion.

---

## Workflow 4: Review an exercise

Once all lessons are reviewed individually, run the exercise-level review for cross-lesson coherence.

```
/review-exercise invoice-matching-ixp
```

This checks everything the lesson review checks, plus:
- Overview page links match actual lesson files
- Nav registration in `mkdocs.yml` is correct and complete
- Consistent terminology and platform name usage across all pages
- Step numbering is sequential with no gaps
- Summary page component table matches the actual exercise components
- All referenced images exist on disk
- No orphaned images (images that exist but aren't referenced)
- Cross-lesson links are valid

---

## Workflow 5: Edit and refine existing content

When making changes to an existing page:

1. **Read the page first** — understand the current structure before changing anything
2. **Match existing patterns** — don't introduce new section types or formatting
3. **Preserve content** — rephrase awkward sentences, don't delete explanatory paragraphs
4. **Update all occurrences** — if you change a prompt in a code block, search for the same text elsewhere on the page
5. **Run `mkdocs build`** — verify no broken links after editing

### Common editing tasks

| Task | What to do |
|------|-----------|
| Fix language/tone | Apply rules from [Language.md](Language.md). Rephrase, don't delete. |
| Add screenshot | Place in the lesson's image folder, reference with `.screenshot` class |
| Update a prompt | Use the diff + highlighted code block pattern from [Formatting.md](Formatting.md) |
| Add a tip/warning | Use one of the four admonition types (tip, info, note, warning) |
| Restructure a page | Only with explicit confirmation — human structure choices are intentional |

---

## Workflow 6: Start a new repository from scratch

For setting up a completely new course site (not adding to the existing one).

### What to copy from this repository

1. **Master/** — the entire directory (your authoritative rules)
2. **CLAUDE.md** — update the project-specific details (site URL, repo URL, tenant info)
3. **.claude/commands/** — all skills (new-exercise, new-lesson, review-lesson, review-exercise)
4. **mkdocs.yml** — use as a starting template, update `site_name`, `site_url`, `nav`
5. **hooks/split_cols.py** — the two-column layout hook
6. **docs/stylesheets/extra.css** — all CSS including image styles and two-column grid
7. **docs/javascripts/extra.js** — external links → new tab
8. **docs/assets/images/** — copy the logo and favicon, or replace with your own
9. **scripts/** — the metadata extraction pipeline (if you'll use `/new-lesson`)
10. **.github/workflows/deploy.yml** — GitHub Actions auto-deploy
11. **requirements.txt** — MkDocs dependencies

### What to create fresh

1. **docs/index.md** — new home page for the new course
2. **docs/next-steps.md** — new global outro
3. Exercise folders as needed

### Setup steps

1. Create a new GitHub repository
2. Copy the files listed above
3. Update `mkdocs.yml`: change `site_name`, `site_url`, `nav`, and author
4. Update `CLAUDE.md`: change project-specific URLs and paths
5. Update training environment callout text in Master/CourseStructure.md if the tenant differs
6. Set up GitHub Pages: enable Pages on the `gh-pages` branch
7. Set up `scripts/.env` if using the metadata extraction pipeline
8. Run `/new-exercise` to create your first exercise
9. Push to main — GitHub Actions deploys automatically

---

## Best practices for course design

### Planning an exercise

- **Start with the business case.** What real-world problem does the learner solve? Lead with that.
- **Identify 3–6 lessons.** Each lesson should take 15–30 minutes. If a lesson would take longer, split it.
- **Each lesson produces a visible result.** The learner should be able to test or see something working at the end of every lesson.
- **Progressive complexity.** Start with the simplest component and build toward the full solution.

### Writing lessons

- **Background before steps.** Don't assume the learner knows why they're doing something — explain briefly, then show how.
- **One screenshot per action.** Don't show 5 screenshots for a single click. Show the result that confirms they did it right.
- **Test every prompt and code block.** Copy-paste your own code blocks and verify they work exactly as written.
- **End with validation.** Every lesson should end with the learner confirming something works — a debug run, a test output, a visible result.

### Reviewing content

- **Read aloud.** If a sentence sounds awkward when spoken, rewrite it.
- **Check the learner's path.** Follow the steps as if you've never seen the platform. Would you know where to click?
- **Verify screenshots match instructions.** If the UI has changed since the screenshot was taken, update both.
- **Test cross-references.** Click every internal link. Run `mkdocs build` to catch broken ones automatically.
