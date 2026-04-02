# CLAUDE.md — Agentic Practice Workshop Site

This file is read automatically on every Claude Code session in this project.
Apply all rules below to every task involving this site — no reminders needed.

---

## Project Purpose

A GitHub Pages–hosted MkDocs site that guides learners through hands-on UiPath agentic automation exercises. The primary audience is workshop participants who are practicing for the first time — not developers, not UiPath experts.

**Live site:** https://uipath-practice.github.io/AgenticPracticeCourse/
**Source repo:** https://github.com/uipath-practice/AgenticPracticeCourse
**Theme:** MkDocs Material (`mkdocs.yml`)
**Deploy:** GitHub Actions on every push to `main` (`.github/workflows/deploy.yml`)

---

## Master Reference Files

All detailed rules, templates, and formatting conventions live in `Master/`. Read the relevant file before creating or reviewing content:

| File | What it covers |
|------|---------------|
| `Master/README.md` | Entry point — what each file contains, sanity rules |
| `Master/Filesystem.md` | Directory structure, file/folder naming, image conventions |
| `Master/CourseStructure.md` | Page types (Overview, Lesson, Summary) with full templates |
| `Master/Formatting.md` | Images, two-column layouts, code blocks, admonitions, tables, prompt diffs, argument docs |
| `Master/Language.md` | Voice, tone, humour, word choices, platform names |
| `Master/HOWTO.md` | End-to-end workflows: create exercise, generate lesson, review, validate |

**When creating new content:** read `Master/CourseStructure.md` and `Master/Formatting.md` before writing.
**When reviewing content:** read all Master files for the checklist (or use `/review-lesson` and `/review-exercise` skills).
**When editing language:** read `Master/Language.md`.

---

## Quick Reference (always in context)

These are the most critical rules — kept here so they're available without extra file reads.

### Language essentials
- **Second person, direct:** "you'll configure", "your agent", "open the panel"
- **Short sentences.** One idea per sentence. Paragraphs: 2–4 sentences max.
- **Conversational and warm** — not corporate, not sloppy. Humour welcome where natural.
- **Avoid:** "leverage", "utilize", "robust", "seamlessly", "In this section we will", "Please note that", "It is important to", "feel free to"
- **Platform names:** Bold on first appearance per page. Exact names: **Agent Builder**, **Maestro**, **IXP**, **Action Center**, **ServiceNow**, **Studio Web**, **Data Fabric**, **Integration Service**, **Orchestrator**

### Formatting essentials
- **Code blocks:** Every copyable text in a fenced code block with a language identifier. Never bare ` ``` `.
- **Screenshots:** `{ .screenshot }` for all UI screenshots. Wide images (`-W`) use `width="900"`.
- **Two-column:** `[[[...|N|...]]]` shorthand (processed by `hooks/split_cols.py`). See `Master/Formatting.md`.
- **Admonitions:** Only `tip`, `info`, `note`, `warning`.
- **No bottom nav links.** MkDocs sidebar handles navigation.

### File naming
- Exercise folder: lowercase, hyphenated (`invoice-matching-ixp`)
- Overview: always `index.md`
- Lessons: `N-verb-noun.md` (`1-create-bpmn.md`, `2-configure-robot.md`)
- Images: per-lesson folders (`<step-slug>.images/`)
- Summary: `you-did-it.md` (no prefix)

---

## Behavioural Rules

### When editing an existing page
- Match existing structure. Don't introduce new section patterns.
- **Never remove sections, paragraphs, or explanatory text.** Rephrase — don't delete.
- If editing a prompt in a code block, update all occurrences on the page.
- **Capitalised domain concepts are intentional** (Invoice, Purchase Order, Storage Bucket). Don't lowercase them.

### When creating new content
- Follow templates in `Master/CourseStructure.md` exactly.
- Always update `nav:` in `mkdocs.yml` when adding or removing pages.
- Run `mkdocs build` to verify before committing.

### When reviewing content
- If the human changed structure from the template, flag it but don't rewrite without confirmation.
- Don't add stub placeholders to sections the author intentionally left as future work.

---

## mkdocs.yml — Do Not Change Without Reason

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
