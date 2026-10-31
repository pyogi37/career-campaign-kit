# START: first-run setup

Follow these steps in order. Each step ends with something saved, so if the session
stops you can pick up where it left off (check what already exists in `workspace/`).
Read `AGENTS.md` first; its hard rules apply from the first question.

## How to interview

- Ask three to five questions at a time, in plain words. Wait for answers.
- Never fill a gap with a guess. If you infer something from a file, mark it
  `inferred (confirm)` and read it back in step 5.
- Write down what they say as they say it, with today's date and `user said`.
- They can skip any question (salary is a common one). Record a skip as
  `declined to share`, and do not ask again unless a form needs it.
- If the answer to one question changes which others matter, adjust. A sales person
  looking for clients does not need a notice-period question.

## 1. Check the harness

Find out, by trying rather than assuming, and tell them what you found:

- Which agent and model you are (Codex, Claude Code, Cursor, ...).
- Can you write files in this folder and run `python --version` (or `python3`)?
  Python 3.9+ is required. If `import openpyxl` fails, ask before running
  `python -m pip install openpyxl`.
- Do you have web search? A browser? Mail, calendar or Notion connectors? Scheduled or
  recurring runs?

Save `workspace/config.json`:

```json
{"owner": "", "created": "YYYY-MM-DD", "harness": "", "python": "python",
 "capabilities": {"web_search": false, "browser": false, "mail": false, "schedules": false},
 "modules": [], "goal": "", "timezone": "", "daily_leads": {"count": 0, "time": null}}
```

## 2. Ask what they want

Show this menu and let them pick any mix. Nothing is on by default.

| Module | What it does each week | Sheets |
|---|---|---|
| `jobs` | Finds roles that fit, every day or on request, and keeps every lead, application and outcome in the workbook. Prepares application batches when they ask. | Applications |
| `outreach` | Picks people worth reaching (hiring managers, recruiters, alumni, or clients and prospects), drafts the invite and follow-ups, tracks who replied. | Outreach |
| `content` | Plans and drafts LinkedIn posts in their voice, tracks what was posted and how it did. | Content |
| `engagement` | Drafts comments on other people's posts and replies under their own. | Engagement |
| `resume` | Builds one master resume from every version they have, then tailored versions per role that can only use confirmed facts, as PDFs. | (files) |
| `interview` | Company research and likely questions before each round, a story bank of their real examples, mock rounds, debriefs and thank-you notes. | Interviews |

`Event History`, `Context` and `Review` come with every setup. Ask what the campaign is
for in one sentence (a new job, a switch of field, clients for a business) and save it
as `goal`. Save the chosen modules.

## 3. Collect their data

Create `workspace/inbox/` and ask them to put in whatever they have. None of it is
required, all of it saves questions:

- Resume or CV (every version they use).
- LinkedIn profile: on the profile page, More → Save to PDF, or paste the text.
- Any tracker they already keep (spreadsheet, Notion export, notes).
- If `content` or `engagement` is on: five or more things they wrote themselves (posts,
  comments, emails, messages they were happy with). Their own words, not edited by AI.
- Job alert emails or lists of companies they like.

Read everything. Build a draft fact list: each fact with its source file. Do not show
it yet.

## 4. Fill the gaps

Ask only what the files did not answer, for the modules they chose.

**Always:** name, where they live, their field in their own words, the one-line story
of their career, what they are best at, and what must never be mentioned in public
(current employer details, clients, numbers, people). Off-limits answers become
`Context` rows with Category `Off limits`, one item per row, `Value` set to the exact
name or text to block.

**jobs:** target titles and the close variants they would also take; seniority; the
industries and kinds of employer they want and do not want; locations, remote,
relocation, travel; work authorization; notice period; current or last pay and expected
pay (optional, record the basis: annual, fixed or total); deal-breakers; companies to
skip (current employer, past rejections); how many new leads a day and at what time;
what makes a role a 5 out of 5 for them.

Then work out where roles in their field are actually posted. Search if you can: for
their field and country, which job boards, professional bodies, recruiters and career
pages matter. Propose a source list, let them edit it, save each as a `Lead sources`
row. Never assume LinkedIn alone covers a field.

**outreach:** who they want to reach and why; how many new people a week; channels
(LinkedIn, email); whether they pay for LinkedIn Premium or Sales Navigator and until
when; people or companies never to contact.

**content:** who they want reading; what they want those readers to think of them; how
often they will really post; topics they know cold; topics they will not touch.

**engagement:** whose posts they want to be seen on (people, companies, communities);
how many comments a day they will really do.

**resume:** which resume versions they use and for what; page size (A4 or Letter);
whether their current employer's name may appear on a resume even if it is off limits
in posts.

**interview:** any interviews already booked or done (company, round, date, outcome);
the kinds of rounds their field usually has (case study, technical test, exams,
portfolio review).

## 5. Read it back

Show the full fact list, grouped by category, each marked `confirmed` or
`inferred (confirm)`. Fix what they correct. Anything still unknown that a module needs
becomes a `Review` row. Get a yes before step 6.

## 6. Build the workspace

1. `python tools/workbook.py init <modules, comma separated>`
2. Write all `Context` rows in one spec (`label: setup-context`).
3. If they gave an existing tracker, map its columns to the workbook's, show the
   mapping, and ask about any column you are unsure of. Import with `Source` set to the
   file name. Rows go in as leads first. Then, for outcomes they listed (applied,
   interviewed), a second write: one `Event History` row each, dated as their tracker
   says, `Source` set to the file name, plus the status update for that row.
4. If `content`, `engagement` or `outreach` is on, write `workspace/voice.md` from
   `templates/voice.md`, filled from their own writing and answers. Mark anything you
   inferred `(confirm)` and show it.
5. If `content` is on, run li-plan to write `workspace/plan.md`'s content section, and
   offer li-profile to score their profile.
6. Save their resumes in `workspace/resume/`.
7. If `resume` is on, build `workspace/resume/master.json` (campaign-resume, "Once: the
   master") and make the first tailored version for their main target role.
8. If `interview` is on, record any booked or past rounds in `Interviews`, and start
   `workspace/interviews/story-bank.md` with three stories (campaign-interview-prep).
   If a round is coming up, prepare its company file first.

## 7. Design their campaign

Write `workspace/plan.md` and show it before saving:

- The goal, in their words, and the one line a stranger should be able to repeat about
  them.
- Their week: which routine runs when (for example: leads every weekday at 10:00,
  outreach Tuesday and Thursday, posts Tuesday and Thursday morning, weekly review
  Sunday). Use the numbers they gave, not bigger ones.
- What success looks like in four weeks, in counts the workbook can show (applications,
  replies, interviews, posts).
- Their rules: anything they said about tone, timing or people that is not already in
  `AGENTS.md`.

## 8. Schedules (only if they want them)

If the harness supports scheduled runs and `jobs` is on, offer to schedule daily leads
at their time, with this prompt:

> In `<this folder's full path>`, read AGENTS.md and run the campaign-daily-leads routine.
> Find and record only. Do not apply, send or post anything.

If schedules are not available, tell them the phrase to use instead: "daily leads".

## 9. First run and handover

Offer to run the first routine now (usually daily leads). Then end with:

- What exists now: the workbook (with sheet names), voice.md, plan.md.
- The phrases that run each routine (the table in `AGENTS.md`, only for their modules).
- That they can open `workspace/campaign.xlsx` any time in Excel or LibreOffice, edit it
  by hand, and that the agent re-reads it before every change. Ask them to close it
  before asking the agent to update it. Google Sheets is for viewing a copy only.
- That nothing is ever sent, posted or applied without their yes.
