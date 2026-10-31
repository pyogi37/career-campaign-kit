---
name: campaign-apply
description: >-
  Prepare an application batch from leads already in the workbook: re-check each
  posting, pick the resume, draft answers, and record only what was actually
  submitted. Use when the owner says "apply to these", "prepare applications",
  "let's do the batch".
---

# Application batch

Needs the `jobs` module. Read `AGENTS.md` first.

1. **Build the batch from the workbook.** `show Applications --where "State=Lead saved - not applied"`
   and `Ready to apply`. Show the candidates by fit and let them pick. Their request
   sets the scope; nothing outside it.
2. **Re-check each pick.** Open the live posting. Check `Event History` for an earlier
   application to the same role, and any conversation with that company. Closed or
   already applied: say so, update the row (`Closed`, or leave it), and move on.
3. **Prepare each one.**
   - Pick the resume from `workspace/resume/` that fits best and say why.
   - Draft any cover note or form answers from `Context` and their resume only. Facts
     not on file (notice period, pay, visa, start date) are asked, not guessed.
   - A cover note passes the four writing checks in `AGENTS.md`.
   - Set the row to `Ready to apply` with `Next action` saying exactly what is left.
4. **Submitting.** By default they submit and tell you. If they ask you to submit with
   a browser, confirm the role, the resume file and every answer for that one
   application, get a yes, submit, and screenshot or copy the confirmation. Never
   create accounts or enter passwords for them.
5. **Record what happened.** For each confirmed submission, one write: an `Event History`
   row (Record ID, Event type `Applied`, Detail with the resume file and how it was
   sent, Evidence: confirmation email, screenshot path or URL) and the `Applications`
   update to `Applied` with `Applied date`, `Resume used`, `Next action`. A clicked
   button with no confirmation is not `Applied`: leave it `Ready to apply` and add a
   Review row.
6. **Report:** submitted, ready but not sent, skipped and why. If `outreach` is on,
   suggest one person at each company worth a note.
