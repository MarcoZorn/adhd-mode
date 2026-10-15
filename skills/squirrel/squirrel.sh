#!/usr/bin/env bash
# Prints one random concept from outside the model: a random Wikipedia article.
# Falls back to a local list when offline.
set -u
n="${1:-1}"
for _ in $(seq "$n"); do
  got=
  for _try in 1 2 3; do  # retry: skip disambiguation pages
    line=$(curl -fsSL --max-time 5 -H 'User-Agent: adhd-mode (github.com/MarcoZorn/adhd-mode)' \
      https://en.wikipedia.org/api/rest_v1/page/random/summary 2>/dev/null |
      python3 -c 'import json,sys; d=json.load(sys.stdin); assert d.get("type")!="disambiguation"; print("SQUIRREL: " + d["title"] + " — " + " ".join(d.get("extract", "").split())[:400])' 2>/dev/null) &&
      { echo "$line"; got=1; break; }
  done
  [ -n "$got" ] && continue
  # ponytail: offline fallback, a fixed list; the real entropy is the online path
  shuf -n1 <<'EOF'
SQUIRREL: Slime mold — a brainless organism that finds shortest paths through mazes and recreated the Tokyo rail network.
SQUIRREL: Kintsugi — repairing broken pottery with gold, making the crack the most beautiful part.
SQUIRREL: Murmuration — thousands of starlings moving as one, each tracking only its 7 nearest neighbours.
SQUIRREL: Lighthouse keepers — people whose whole job was keeping one light on, alone, for years.
SQUIRREL: Tardigrade cryptobiosis — shutting metabolism down to 0.01% and reviving decades later.
SQUIRREL: Jazz trading fours — musicians alternating four-bar solos, each answering the last.
SQUIRREL: Mycorrhizal networks — fungi linking tree roots to trade sugar and warning signals.
SQUIRREL: Dead reckoning — navigating with no landmarks, only speed, heading and elapsed time.
SQUIRREL: Bonsai — keeping a tree tiny for centuries by pruning roots and branches together.
SQUIRREL: Pneumatic tube mail — cities that shot letters through underground pipes at 35 km/h.
SQUIRREL: Bioluminescent dinoflagellates — plankton that glow only when disturbed.
SQUIRREL: Medieval cathedral builders — projects that outlived three generations of workers.
SQUIRREL: Octopus arms — two-thirds of its neurons live in the arms, which make decisions alone.
SQUIRREL: Sourdough starter — a living culture fed daily and passed down for 100+ years.
SQUIRREL: Air traffic control — strict phrasebooks so stressed strangers never misunderstand each other.
SQUIRREL: Termite mounds — passive ventilation keeping a constant temperature with no machines.
SQUIRREL: Origami tessellations — one uncut sheet folded into infinitely repeating 3D patterns.
SQUIRREL: Casino floor design — no clocks, no windows, maze-like paths that keep people inside.
SQUIRREL: Echolocation — bats building a 3D world from returning sound.
SQUIRREL: The Voyager Golden Record — a message for aliens who may never exist.
EOF
done
