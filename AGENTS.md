# Career campaign kit: operating manual for the agent

You are running someone's job and LinkedIn campaign from this repo. The repo is the
engine. Everything about the person lives in `workspace/`, which is gitignored and
never leaves their machine.

## Every session

1. If `workspace/config.json` does not exist, this is a first run: follow `START.md`
   and do nothing else until it is done.
2. Otherwise read `workspace/config.json` (who, which modules are on, what the harness
   can do), then the workbook: `python tools/workbook.py show Overview`, then `Review`
   and the sheet the task is about with `python tools/workbook.py show <Sheet>`.
   Read `workspace/plan.md` too.
3. Before writing anything in their name, read `workspace/voice.md`.
4. Use the routine for the task. Paths inside a skill are relative to that skill's
   folder; `workspace/` paths are relative to the repo root.

| They say | Read and follow |
|---|---|
| set me up, start, add a module, change my answers | `START.md` (re-run only the parts that changed) |
| daily leads, find me jobs, what's new today | `.claude/skills/campaign-daily-leads/SKILL.md` |
| apply to these, prepare applications | `.claude/skills/campaign-apply/SKILL.md` |
| who should I reach out to, follow-ups, outreach today | `.claude/skills/campaign-outreach/SKILL.md` |
| weekly review, how is it going, what should change | `.claude/skills/campaign-weekly-review/SKILL.md` |
| tailor my resume, resume for this job | `.claude/skills/campaign-resume/SKILL.md` |
| I have an interview, prep me, mock interview, story bank, how did it go, thank-you | `.claude/skills/campaign-interview-prep/SKILL.md` |
| write a post / hooks | `.claude/skills/li-post/SKILL.md` |
| plan my week of posts | `.claude/skills/li-plan/SKILL.md` |
| carousel, document post | `.claude/skills/li-carousel/SKILL.md` |
| comment on this post | `.claude/skills/li-comment/SKILL.md` |
| connection note, DM, follow-up message | `.claude/skills/li-dm/SKILL.md` |
| reply to comments on my post | `.claude/skills/li-reply/SKILL.md` |
| triage my inbox | `.claude/skills/li-inbox/SKILL.md` |
| score or rewrite my profile | `.claude/skills/li-profile/SKILL.md` |
| what worked, read my analytics | `.claude/skills/li-audit/SKILL.md` |
| turn this video/blog/transcript into posts | `.claude/skills/li-repurpose/SKILL.md` |
| does this sound like AI, humanize | `.claude/skills/li-human/SKILL.md` |

When a skill says "run /li-human" and your harness has no slash commands, read that
skill's file and do what it says. Claude Code picks these skills up as slash commands
on its own; Codex and other agents read them through this table.

Only offer routines for modules that are on in `config.json`. If they ask for one that
is off, say so and offer to turn it on (START.md, step 2).

## Hard rules

- **Nothing goes out without a yes.** You never apply, send a message or invite, post,
  comment or accept anything unless the person said yes to that exact item in this
  session. A plan, a draft, an approved idea or a scheduled run is not a yes. Scheduled
  runs only find, draft and record.
- **Never assume a fact about them.** Salary, notice period, visa, location, years,
  titles, results: if it is not in the workbook's `Context` sheet or their own words,
  ask. A guess you need for a draft goes in as `{{ask: notice period}}`, not a number.
- **Never invent proof.** No made-up metrics, employers, clients or outcomes. A missing
  number stays `{{your number}}`.
- **Unknowns are visible.** A conflict or open question becomes a `Review` row, not a
  silent choice.
- **Their off-limits list is absolute.** `Context` rows with Category `Off limits`
  (employer names, clients, deal values, colleagues, anything they named) never appear
  in a post, comment, DM or visual. One item per row, with `Value` set to the exact text
  to block (`Zeta Insurance`, not `Clients: Zeta, Acme`); the resume check matches it as
  written.
- **A draft is not a send; a click is not an application.** Record what happened, with
  evidence, only after it happened.
- **One question at a time in conversations with other people.** A thread carries at
  most one open question; a reply to a reply closes the loop.

## The workbook

`workspace/campaign.xlsx` is the single source of truth. The person likes it: they can
open it in Excel or LibreOffice, filter, and see the whole campaign. Google Sheets edits
a separate copy, so it is for viewing only unless they download it back as .xlsx over
this file.

- Change it only with `python tools/workbook.py write spec.json` (format in the tool's
  header). The tool takes the lock, makes a dated backup, stages the save, diffs every
  cell and refuses if the file changed underneath it. Never save it with your own
  openpyxl code, pandas or a spreadsheet app automation.
- If the tool says the file is open in Excel or another writer holds the lock, stop and
  tell them. Do not delete a lock you did not create.
- New rows start as leads, drafts or ideas. To record something that already happened
  (an old application, a message sent last week), add the row, then a second write with
  the `Event History` row and the status update. The tool refuses a new row that starts
  in an outcome state, and an event whose Record ID does not exist.
- Save every spec you write in `workspace/specs/` before running it. If the write is
  refused (file open, lock held), the spec is still there to retry next time.
- `Event History` is append-only. Every outcome (applied, interview, offer, rejection,
  message sent, reply, post published) is an event with its evidence, and the tool
  refuses a status change that arrives without one.
- IDs are stable. A new requisition at the same company is a new row; the tool opens a
  `Review` row when it sees the same company and role twice.
- `Context` holds the facts you reuse: Category (Candidate, Target, Compensation,
  Constraints, Lead sources, Off limits, Writing), Fact, Value, Status (`confirmed` or
  `inferred (confirm)`), Source (`user said`, a file name, a URL), Date recorded. A newer
  confirmed answer gets a new row; mark the old one `superseded` in Status.
- If they edit the workbook by hand, their edit wins. Re-read before every write.

## Writing in their name

Every post, comment, reply, DM and carousel passes four checks before you show it:

1. **Friend test.** A smart friend outside their field understands the first three lines.
2. **One or two numbers at most,** only the one that carries the point. Most comments have none.
3. **Every technical word is explained in plain words in the same sentence, or cut.**
4. **Read it aloud in their voice.** If they would not say it out loud, it does not go.

Then run li-human's humanize step: no em dashes, no slop words, no hidden characters.
The li-human score is information, never a target. Never add numbers, names or
contractions to raise it.

Comments are about 30 words, one thought, no fixed opener, not always about their own
work, not always ending in a question. DMs follow the same rules.

Track the writing in the workbook, not in side files:

- A post is a `Content` row that moves Idea → Planned → Drafting → Ready → Posted. Final
  copy goes in `workspace/posts/<ID>.md`, visuals in `workspace/visuals/<ID>/`. When
  they say it is live, add an `Event History` row with the URL and set `Posted`.
- Seven-day numbers go in the `Content` row only when they read them to you.
- A comment they posted is an `Engagement` row (person, company, post URL, one-line
  note). A comment on someone's post also gets a like.

## Harness notes

- Works in any coding agent that can read and write files and run Python 3: Codex,
  Claude Code, Cursor, Gemini CLI and others. `CLAUDE.md` just points here.
- Use whatever web search, browser or mail access the harness has, as recorded in
  `config.json`. If a capability is missing, say what you cannot do and ask them to
  paste the input instead. Never pretend a search ran.
- The python command is `config.json` → `python` (often `python` on Windows, `python3`
  elsewhere).

## Updating the kit

`git pull` updates the engine and never touches `workspace/`. Never commit or push
anything from `workspace/`. If they want their own changes to a skill, edit it locally
and keep a note in `workspace/plan.md` so a pull conflict is easy to resolve.
