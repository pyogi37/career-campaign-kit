---
name: campaign-resume
description: >-
  Build the owner's master resume once, then tailored versions per role family
  or per job that can only use confirmed facts, rendered to a clean PDF. Use when
  they say "tailor my resume", "resume for this job", "make a version for X",
  "fix my resume".
---

# Resume tailoring

Needs the `resume` module. Read `AGENTS.md` first. The tool is `tools/resume.py`; its
header shows both file formats.

## Once: the master

1. Read every resume in `workspace/resume/` (and their LinkedIn PDF if it is in
   `workspace/inbox/`). Merge them into `workspace/resume/master.json`: every role,
   project, education line, skill group and bullet they have ever used, each bullet
   with `source` (the file it came from). Give stable ids (`e1`, `e1.1`, `p1`, ...).
2. Where two versions disagree (a date, a title, a number), ask which is right. Do not
   keep both.
3. Show the master grouped by role and ask: is every bullet true, and is anything
   missing? Add what they tell you with `source: user said YYYY-MM-DD`. Bullets that
   name an `Off limits` item are rewritten without it or dropped, with their yes.

The master is the only place facts enter. A new achievement goes into the master first.

## Each tailored version

1. **Read the target.** A JOB row and its posting, or a role family they named. Pull
   out the five or six things the posting cares about most, in its words.
2. **Choose, then reword.** Write `workspace/resume/variants/<label>.json`:
   - pick and order the entries and bullets that prove those things; drop the rest;
   - reword bullets to use the posting's language where it is honestly the same thing.
     The tool rejects a rewording that adds a number its source bullet does not have;
   - a headline and a two or three line summary for this role, from master facts only;
   - one page for under about ten years of experience unless they say otherwise.
3. **Check:** `python tools/resume.py check <variant>`. Fix every problem it lists; never
   work around it by adding the number to the master without their confirmation.
4. **Show the changes** as a short list (what moved up, what was cut, what was
   reworded and why), with the four writing checks applied to the summary.
5. **Render** on their yes: `python tools/resume.py render <variant>`. It writes HTML and,
   if Chrome or Edge is installed, a PDF. Look at the PDF, or ask them to, before it
   is used. If they need Word, they can open the HTML in Word and save as .docx.
6. **Record:** when the version is used for an application, the campaign-apply routine
   puts its file name in that row's `Resume used`.

Keep variants per role family (for example `pricing-actuary`, `reserving`) and make a
per-job copy only when a posting needs it.
