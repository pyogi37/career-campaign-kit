---
name: campaign-interview-prep
description: >-
  Prepare for an interview round, keep a story bank of the owner's real
  examples, and debrief afterwards. Use when they say "I have an interview",
  "prep me for X", "mock interview", "build my story bank", "how did it go", or
  "draft a thank-you".
---

# Interview prep

Needs the `interview` module. Read `AGENTS.md` first. Files live in
`workspace/interviews/`; rounds are rows in the `Interviews` sheet.

## When an interview is booked

1. Record it: an `Interviews` row (`Linked record` = the JOB ID, Company, Role, Round,
   Date, With, Format, `Scheduled`), plus an `Event History` row with the invite as
   evidence. If the JOB row is not yet `Interviewing`, update it in the same write.
2. Ask what they know: who they meet, what the round is (screen, technical, case,
   assignment, panel, founder), how long, anything the recruiter said.

## The company file: `workspace/interviews/<company>.md`

Research from the posting, the company's site, recent news and the interviewers'
public profiles; list sources at the bottom. Then write, in this order:

1. **Status and next action** at the top, from the workbook.
2. **The company in 60 seconds:** what they sell, to whom, how they make money, what
   changed recently.
3. **The posting against their evidence:** each requirement, the story or fact that
   proves it (from the story bank, master resume or `Context`), and a strength. For
   each gap, one honest line they can say. Never stretch a title or years.
4. **Likely questions** (10 to 12) for this round type and field, each with talking
   points that point to a story by its id.
5. **A 30-60-90 day plan** they can talk through, grounded in what the company said.
6. **Five questions to ask them,** specific to this company and round.
7. **Gaps to fill:** what you need them to tell you before the day.

Set the row to `Prep ready` with `Prep file`. Offer a mock round: you ask, they answer,
you give feedback on one thing at a time.

## The story bank: `workspace/interviews/story-bank.md`

Built once and grown after every interview. Each story:

- an id (S1, S2, ...) and a title;
- a 20-second version they can say out loud, passing the four writing checks;
- the STAR version: situation, task, action, result;
- themes it answers (ownership, failure, conflict, ambiguity, influence, technical
  depth, speed vs quality, ethics);
- `{{placeholders}}` for any detail they have not given. Never fill a number or a name.

Build it by interview, not invention: ask for their proudest piece of work, a failure,
a disagreement, a time they changed someone's mind, something they built from nothing.
Keep a theme index at the top and an `Off limits` reminder: no client names, deal values
or colleagues unless they said yes to that detail.

## After the round

1. Ask how it went: questions asked, what felt weak, anything promised, next steps and
   dates they were given.
2. Record it: `Event History` row (`Interview done`, notes) and the `Interviews` row to
   `Done` (or `Next round` / `Rejected` / `Offer` when they hear). Set the JOB row's
   `Next action` with the date to follow up if they hear nothing.
3. Draft a short thank-you (four writing checks, one specific line from the
   conversation, no new question). They send it; record `Thank-you sent` after.
4. Add any new question to the company file and any new story to the story bank.

An offer: record the numbers exactly as written in the offer, with the basis (annual,
fixed, variable). Compare with their `Compensation` rows. Never accept, decline or
negotiate for them; draft what they ask for.
