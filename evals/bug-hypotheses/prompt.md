---
description: Bug mode produces many cause hypotheses ranked by cheapest test, not a single guess.
max_turns: 30
timeout_seconds: 900
runs: 1
allowed_tools: [Skill, Agent, Read, Grep, Glob, Write, Edit, Bash]
---

ADHD mode, bug: our nightly CSV export job works every day except it silently produces an empty file on the first Sunday of some months. No errors in the logs. Give me alternatives I haven't thought of.
