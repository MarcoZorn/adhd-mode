---
name: squirrel
description: SQUIRREL! 🐿️ — break out of a creative rut with real outside entropy. Pulls random Wikipedia articles and forces Zap to solve your problem through analogy with them. Use when ideas feel samey, predictable or stuck.
argument-hint: "<problem> [count]"
allowed-tools: Bash(bash *squirrel.sh*)
---

# SQUIRREL! 🐿️

Problem: $ARGUMENTS

LLMs drift toward the most likely answer. This skill injects randomness that doesn't come from the model.

1. Run `bash "${CLAUDE_SKILL_DIR}/squirrel.sh" 3` (use the count from the arguments if given, max 5).
2. Spawn the `adhd-mode:zap` agent with the problem and all SQUIRREL lines. Tell it: "For each SQUIRREL, produce 3 ideas by forced analogy — steal its mechanism, not its surface. Then one Collision idea combining two squirrels. Skip the full idea list; squirrel ideas only, plus Tangents."
3. Report to the user: each squirrel (title + one line), the ideas it spawned, and Zap's favorite. Append the Tangents to `.adhd/tangents.md` (append, never overwrite).

Answer in the user's language.
