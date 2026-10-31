---
name: campaign-daily-leads
description: >-
  Find new roles that fit the owner and record them in the campaign workbook as
  leads. Use when they say "daily leads", "find me jobs", "what's new today", or
  when a scheduled run asks for it. Finds and records only; never applies.
---

# Daily leads

Needs the `jobs` module. Read `AGENTS.md` first.

1. **Load the brief.** `python tools/workbook.py show Context`: Target, Constraints,
   Compensation, Lead sources and Off limits rows. `show Applications` for what is
   already known. `config.json` → `daily_leads.count` is today's quota of new leads.
2. **Search every source on the list.** Use the harness's web search or browser.
   If a source cannot be reached, note it for the summary; it is not an empty result.
   No search tool at all: say so and ask them to paste listings or alert emails.
3. **Check each candidate role on its own posting**, not a summary: still open, the
   real location and remote rules, seniority, requirements, how to apply. A role you
   could not open stays a lead with `Notes: not verified (reason)`.
4. **Score fit 1 to 5** against their Target rows and what they said makes a 5. Write
   the gaps honestly in `Fit notes and gaps`. Roles that break a deal-breaker are not
   recorded unless they asked to see near-misses.
5. **Record in one write.** Each role is an `Applications` row: Company, Role, Job URL
   (the canonical posting, not a search page), Location, Source (board name + URL),
   Captured, Fit, Fit notes, Next action. The tool skips exact URL repeats and opens a
   Review row for same-company same-role pairs; mention both in the summary.
   Label the spec `daily-leads-YYYY-MM-DD` and save it as
   `workspace/specs/daily-leads-YYYY-MM-DD.json` before running the write.
   If the write is refused (workbook open, lock held), leave the spec there and say so.
   At the start of every run, first retry any earlier daily-leads spec that was never
   written (its leads are not in `Applications`); the tool skips ones already saved.
6. **Report** in a few lines: sources searched and any that failed, new leads with fit
   and one-line why, repeats skipped, Review rows opened, and the three best leads to
   apply to first. Ask whether to prepare an application batch (campaign-apply).

Discovery is never permission to apply. A scheduled run stops after step 6.
