---
name: evolve
description: Idea evolution 🧬 — a genetic algorithm for ideas. Zap breeds a population, isolated jurors select the fittest, survivors crossbreed and mutate for several generations. Use when you want an idea pushed far beyond the first brainstorm.
argument-hint: "<problem> [generations=3]"
allowed-tools: Bash(shuf *) Bash(bash *squirrel.sh*)
---

# Evolve 🧬

Problem: $ARGUMENTS

Run N generations (default 3, max 5). Keep a lineage log as you go.

## Generation 0
Spawn `adhd-mode:zap` with the problem. Take its 8 most diverse ideas as the population (cover all three of 🟢🟡🔴).

## Each generation
1. **Selection** — spawn 3 `adhd-mode:juror` agents in parallel, each with a different lens (end user · engineer on call · skeptical investor). Instead of two exhibits, give each the whole population as a numbered list shuffled with `shuf` (fresh order per juror), and ask: "Score every idea 1-10 on impact, feasibility and originality, then name your top 3." Sum scores across jurors; keep the top 4 as survivors.
2. **Crossover + mutation** — spawn `adhd-mode:zap` with the survivors and this instruction: "Breed 4 children: 2 crossovers (combine the core mechanisms of two parents into one coherent idea) and 2 mutations (take one parent and push it with a new engine). Name each child and list its parents." On generation 2, inject one squirrel: `bash "${CLAUDE_SKILL_DIR}/../squirrel/squirrel.sh" 1` and require one child to mutate through it.
3. Next population = 4 survivors + 4 children.

## Finale
Spawn `adhd-mode:doc` on the final top 2 (feasibility + prior art), then `adhd-mode:vera` to pick and concretize the champion.

Report:
- The family tree of the champion (e.g. `#3 × #7 → "Mycelium Cache" → mutated (squirrel: Murmuration) → "Flock Cache"`).
- Score progression per generation (best and average).
- Vera's concretized champion.

Answer in the user's language.
