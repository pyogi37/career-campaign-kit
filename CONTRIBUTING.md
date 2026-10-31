# Changing the kit

This repo is the engine; nobody's data is in it. Keep it that way: never commit
anything from `workspace/`, and grep for real names before every push.

- **Code** (`tools/`): run `python tools/test_workbook.py` and `python tools/test_resume.py`.
  New logic that guards data or facts gets a test that fails when the guard breaks.
- **Review:** changes to `tools/` get a ponytail review before they are pushed
  (`/ponytail-review` in Claude Code). Ponytail is for building the kit, not for the
  agent that runs someone's campaign, so it is not installed by the kit.
- **Routines and skills** (`.claude/skills/`, `AGENTS.md`, `START.md`): every rule must
  work in any agent, not just one harness. Read a changed routine end to end as if you
  were an agent seeing it for the first time.
- **Docs and prompts** follow the same plain-language rules the kit applies to posts:
  a reader outside tech should follow them.
