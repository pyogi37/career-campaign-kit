# Career campaign kit

An AI agent that runs your job search and LinkedIn campaign with you: finds roles that
fit every day, keeps every lead and outcome in one Excel workbook, drafts outreach and
posts in your own voice, and reviews the week. It never sends, posts or applies
anything without your yes.

It knows nothing about you when you start. It reads what you give it (resume, LinkedIn
profile, an old tracker), asks about everything else, and builds your campaign from
that. You pick what you want:

- **jobs**: daily leads in a workbook, application batches on request
- **outreach**: who to contact, the messages, the follow-ups, the replies
- **content**: LinkedIn posts planned and drafted in your voice
- **engagement**: comments on other people's posts, replies under yours

## Start

You need a coding agent that can read and write files and run Python 3: Codex, Claude
Code, Cursor, Gemini CLI or similar. Open it in an empty folder where you want your
campaign to live, and paste this:

```text
Set up my career campaign agent from this kit: https://github.com/pyogi37/career-campaign-kit

1. Clone the repo into this folder (git clone <url> .), or into a new folder here
   called career-campaign if this one is not empty. Tell me which.
2. Read AGENTS.md, then follow START.md step by step.
3. Build everything from my own data and answers. Never assume a fact about me:
   ask, and record what I say with the date.
4. Never send, post, apply or message anything for me without my yes for that
   exact item.

Start with step 1 of START.md.
```

Setup takes about 20 to 40 minutes of back and forth. After that, say things like
"daily leads", "apply to these", "outreach today", "write a post about ...", or
"weekly review".

## Where your data lives

Everything about you is in `workspace/`: the workbook (`campaign.xlsx`), your voice
profile, plan, resumes and drafts. That folder is ignored by git, so it stays on your
machine. `git pull` updates the kit without touching it. Do not push it anywhere.

You can open `workspace/campaign.xlsx` in Excel or Google Sheets any time and edit it.
Close it before asking the agent to update it; the agent refuses to write while it is
open, takes a backup before every change, and checks every cell after.

## What is in the repo

| Path | What it is |
|---|---|
| `AGENTS.md` | The agent's operating manual and hard rules (Codex reads it directly; `CLAUDE.md` points to it) |
| `START.md` | The first-run interview and setup |
| `.claude/skills/campaign-*` | Routines: daily leads, application batch, outreach, weekly review |
| `.claude/skills/li-*` | LinkedIn writing skills: posts, comments, DMs, replies, carousels, profile, audit, humanizer |
| `tools/workbook.py` | The only way the workbook is changed: lock, backup, staged save, cell-by-cell check |
| `templates/voice.md` | Shape of the voice profile the agent writes for you |

Check the workbook tool on your machine with `python tools/test_workbook.py`.
