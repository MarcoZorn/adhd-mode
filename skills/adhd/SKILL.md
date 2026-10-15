---
name: adhd
description: ADHD Mode — run the full neurodivergent brainstorm pipeline. Zap ⚡ floods wild ideas, Doc 🧪 breaks them down technically and checks prior art, Vera 🎯 picks the winner and makes it concrete. Use for creative ideas, product/design concepts, out-of-the-box alternatives, or getting unstuck on a bug ("bug: ..."). Add "--trial" to settle the top two in Idea Court, "--squirrel" to inject random entropy.
argument-hint: "[bug:] <problem or idea> [--squirrel] [--trial]"
allowed-tools: Bash(bash *squirrel.sh*) Read Write Edit
---

# ADHD Mode ⚡🧪🎯

Request: $ARGUMENTS

You are the **conductor**. You don't ideate yourself — you run the team and pass full context between them. Subagents don't share memory, so always paste the previous agent's complete output into the next prompt.

## 0. Setup
- **Mode**: if the request starts with `bug:` → bug mode, else idea mode.
- If the request is vague, don't ask questions — Zap thrives on ambiguity.
- Gather context: if the request mentions files or this codebase, note the relevant paths so agents can read them.
- If `--squirrel` is present, run `bash "${CLAUDE_SKILL_DIR}/../squirrel/squirrel.sh" 2` and keep both SQUIRREL lines.

## 1. Zap ⚡ — diverge
Spawn the `adhd-mode:zap` agent with: the request, the mode, relevant file paths, and the SQUIRREL lines if any.

## 2. Doc 🧪 — break it down
Spawn the `adhd-mode:doc` agent with: the request, the mode, and Zap's full output. Ask for prior-art checks on the top 5 ideas (idea mode) or a cheapest-test-first ranking (bug mode).

## 3. Vera 🎯 — converge
Spawn the `adhd-mode:vera` agent with: the request, the mode, Zap's full output and Doc's full output.

## 4. Trial (optional)
If `--trial` was passed, or Vera says two ideas are close, run the `/adhd-mode:trial` procedure on Vera's top two (read `${CLAUDE_SKILL_DIR}/../trial/SKILL.md` and follow it).

## 5. Save the tangents 🐿️
Append Zap's "Tangents" section to `.adhd/tangents.md` in the project root (create it if missing) under a heading `## <YYYY-MM-DD> — <short request>`. Never overwrite — append. Killed ideas are not lost: also append Vera's KILL list there under `### Graveyard`.

## 6. Report to the user
Keep it short and scannable:
1. **Zap's top 5** (names + one line each) and how many ideas were generated.
2. **Doc's verdict** on those: feasibility, prior art (NOVEL / EXISTS).
3. **Vera's winner** — pitch, the slice, first step tomorrow, the Postcard from 2031.
4. Trial verdict if run.
5. One line: "Tangents saved to `.adhd/tangents.md`".

Answer in the user's language.
