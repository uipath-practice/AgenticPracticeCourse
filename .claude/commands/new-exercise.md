Scaffold a new exercise for the Agentic Automation Workshop site.

**Before proceeding, read:** `Master/Filesystem.md`, `Master/CourseStructure.md`, `Master/Language.md`, and the sample templates in `Master/Templates/` (overview, lesson, summary).

## Collect inputs

If any of the following are missing from the user's message, ask for them before proceeding:

1. **Exercise slug** — lowercase, hyphenated folder name (e.g., `expense-report-processing`). Infer from the display name if not provided.
2. **Display name** — title as it appears in the nav (e.g., "Expense Report Processing")
3. **One-paragraph description** — what the learner will build and which platform products they'll use
4. **Steps** — list of step names with brief descriptions (e.g., "1. Upload Report — robot retrieves PDFs from a storage bucket")

---

## What to create

### 1. Folder structure

Follow the conventions in `Master/Filesystem.md`:

- `docs/<exercise-slug>/` — exercise folder
- `docs/<exercise-slug>/<step-slug>.images/.gitkeep` — one image folder per lesson (named after the lesson file without numeric prefix)
- `docs/<exercise-slug>/documentation.txt` — documentation reference file

**`documentation.txt` template:**

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

Follow the **Overview Page** template in `Master/CourseStructure.md`. Key points:

- `# Title` is a noun phrase — the exercise name
- Bold headline: one sentence describing what the learner builds
- `## Overview` names platform products (bold on first use)
- Step table with links to lesson files
- Training environment callout at the bottom

---

### 3. Lesson stub pages — `docs/<exercise-slug>/N-verb-noun.md`

File names follow the pattern in `Master/Filesystem.md`: numeric prefix + verb-noun slug.

Use this stub structure for each lesson page:

```markdown
# Descriptive Lesson Title

!!! tip "Here is our plan:"

    1. [First action — infer from the step description]
    2. [Second action]
    3. [Third action if applicable]

## Goal

One short paragraph: what the learner will have built or configured by the end of this step.

## Steps

<!-- Add step-by-step instructions with screenshots here -->

!!! note "Content migration in progress"
    Detailed steps and screenshots will be added here.
```

Apply the language rules from `Master/Language.md` — second person, short sentences, conversational tone.

---

### 4. Summary page — `docs/<exercise-slug>/you-did-it.md`

Follow the **Summary Page** template in `Master/CourseStructure.md`.

**For the Learn more table:** Read `docs/<exercise-slug>/documentation.txt` and extract URLs. If no URLs yet, leave a placeholder row.

---

### 5. Update `mkdocs.yml` nav

Add the exercise before `- Next Steps: next-steps.md`. Follow nav conventions from `Master/Filesystem.md`:

```yaml
- Display Name:
  - Overview: exercise-slug/index.md
  - 1. Step One Name: exercise-slug/1-verb-noun.md
  - 2. Step Two Name: exercise-slug/2-verb-noun.md
  - You did it!: exercise-slug/you-did-it.md
```

---

### 6. Update `docs/index.md`

Add a summary card for the new exercise. Read the home page first and match the format of existing entries.

---

## Verify

After creating all files, run `mkdocs build` to check for broken links and nav errors:

```bash
/Users/sergey/Library/Python/3.9/bin/mkdocs build
```

Report any build errors. If the build passes, summarize what was created: files, nav entries, and index card.

$ARGUMENTS
