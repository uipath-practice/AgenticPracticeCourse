Build a complete lesson page from screenshots for the Agentic Automation Workshop site.

**Before proceeding, read:** `Master/CourseStructure.md` (lesson page section), `Master/Formatting.md`, `Master/Language.md`, and the sample lesson template `Master/Templates/1-sample-lesson.md` (demonstrates all building blocks in context).

## Collect inputs

If any of the following are missing from the user's message, ask before proceeding:

1. **Exercise slug** — folder name of the exercise (e.g., `expense-report-processing`)
2. **Step number** — the numeric prefix (e.g., `3`)
3. **Step name** — display name for the step (e.g., "Configure Agent")
4. **Images folder path** — path to the folder containing the screenshots (e.g., `docs/expense-report-processing/configure-agent.images/`)
5. **Context** (optional) — any additional details: platform features used, expected inputs/outputs, business logic, or special instructions

---

## Step 1: Check documentation references, then extract metadata

**Before running extraction**, check whether `docs/<exercise-slug>/documentation.txt` exists. If it does, remind the user to add links for this lesson's topic before continuing. The extraction script reads this file and embeds the linked documentation as context — this improves metadata quality.

If the file exists but may be missing relevant links, ask the user: *"Have you added the relevant documentation links to documentation.txt for this step?"*

Once ready, run the extraction script:

```bash
python -m scripts.extract_metadata --folder <images-folder-path>
```

**Prerequisites:** `scripts/.env` must exist with Azure OpenAI credentials. See `scripts/.env.example` for the required keys. If the file is missing, stop and ask the user to set it up.

If some images already have `.metadata.json` files, the script skips those by default. Use `--force` only if explicitly requested.

After running, verify that `.metadata.json` files exist next to the images. If the script fails, report the error — do not proceed with placeholder content.

---

## Step 2: Read the metadata

Read every `.metadata.json` file in the images folder. Each file contains:
- `filename` — the image file it describes
- `ocr_text` — raw text visible in the screenshot
- `ui_description` — description of the UI state shown
- `step_instruction` — the action or concept the screenshot illustrates

Build a mental model of the full lesson: what the learner does first, what intermediate states look like, and what the final result is.

Also read the existing lesson `.md` file if it exists (it may be a stub). Note any headings or partial content that should be preserved.

---

## Step 3: Build the lesson page

Write the complete lesson to `docs/<exercise-slug>/N-verb-noun.md`.

Follow the **Lesson Page** template in `Master/CourseStructure.md`:

1. **Title** — descriptive phrase (not "Step N — Verb Noun")
2. **Opening tip admonition** — 2–3 high-level plan items
3. **Goal section** — one paragraph, what the learner will have built
4. **Concept sections** — background needed before hands-on steps
5. **Steps section** — numbered substeps with screenshots

Apply all formatting rules from `Master/Formatting.md`:
- Screenshots use `{ .screenshot }` class
- Wide images (`-W` suffix) use `width="900"`
- Regular images use two-column layout or 4-space indent inside numbered lists
- Code blocks have language identifiers
- Arguments use the `css hl_lines="1"` pattern
- Prompt updates use the collapsible diff + highlighted block pattern

Apply all language rules from `Master/Language.md`:
- Second person, short sentences, conversational tone
- Platform names bold on first appearance
- No forbidden words

Use OCR text from metadata as the source of truth for prompts and config values.

---

## Step 4: Verify

After writing the file, read it back and check:
- Every image referenced exists in the images folder
- All copyable text is in fenced code blocks
- Platform names are bold on first appearance
- No manual navigation links at the bottom
- All two-column blocks have delimiters on their own lines
- Voice matches the language rules

Report what was created and flag any screenshots that had low-confidence metadata for manual review.

$ARGUMENTS
