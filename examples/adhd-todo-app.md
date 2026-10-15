# Example: `/adhd-mode:adhd A to-do app for people with ADHD that they would actually keep using --squirrel`

Unedited final output of a real run (Claude Code 2.1.300). The squirrels were random Wikipedia articles: the metalcore band *For Today* and the UK *Rushmoor Borough Council* election.

---

# ⚡🧪🎯 ADHD to-do app ideas: Rushmoor Thirds wins

Diagnosis: to-do apps keep a permanent record of what you haven't done. People with ADHD quit after about 9 days, once the list has turned into a pile of guilt. The fix is a list that forgets on purpose.

## ⚡ Zap's top 5 (25 ideas generated, with two random squirrel prompts: the metalcore band For Today and a UK council election)
1. **For Today Only.** The list deletes itself every night. To keep a task you rescue it at a morning "Wake gate".
2. **Rushmoor Thirds.** Every 3 days, a third of your tasks stand for "re-election". The ones you don't vote for leave quietly.
3. **Album Eras.** The app changes its look and its rules every 6 weeks, so the novelty comes back on schedule.
4. **Body Double Ghost.** A silent figure on screen "works" next to you.
5. **Doorway Tasks.** Tasks are tied to places and transitions instead of dates.

## 🧪 Doc's verdict
| Idea | Feasibility | Prior art |
|---|---|---|
| For Today Only | 5/5, 2–3 days | PARTIAL: Check (iOS, ~2016), Slate |
| Rushmoor Thirds | 5/5, 3–5 days | PARTIAL: Sunsama auto-archives tasks, but no app lets you vote → **the mechanic is new** |
| Album Eras | 3/5, months | NOVEL among to-do apps |
| Body Double Ghost | 5/5 | EXISTS: Alongside is nearly identical |
| Doorway Tasks | 3/5 | EXISTS: Apple Reminders, TODO At |

Doc also flagged **#24 Election Night Breakdown** as stronger than several top-5 ideas: a task that's losing its vote gets split into smaller ones.

## 🎯 Vera's winner: Rushmoor Thirds + Recount
**Pitch:** Every three days, a third of your tasks stand for re-election, and the ones you don't vote for quietly leave office.

**What you see:**
- The look of a ballot paper: cream background, black ink, and one red X stamp.
- Capture is a single input. No dates, no tags.
- Every 3 *active* days you get a full-screen ballot that takes under 60 seconds. Swipe up to re-elect (stamp + haptic). Swipe down to concede (the card folds into the ballot box). Or abstain.
- Long-press a task to call a **Recount**: it splits into 2–3 smaller candidates.
- The **Constitution** holds up to 3 items that never go up for election (meds, rent).

**The slice:** one web page with localStorage, containing capture, the cohort rule `hash(id) % 3`, the epoch rule `floor(activeDays/3)`, the swipe ballot, a manual Recount, 3 Constitution slots, and a 10-second undo.

**First step tomorrow:** write `whoIsUpForElection(tasks, activeDays)` with an assert check. Paste in your real backlog and fake three elections. If conceding stale tasks doesn't feel like relief by the third election, stop.

**📮 Postcard from 2031, three ways it failed:**
1. People re-elected everything by reflex. Fix: cap Parliament at 21 seats, so a new task forces a by-election.
2. People came back after two weeks away and found the same stale list. Fix: after 7+ days away, call a snap General Election where the default swipe is concede.
3. Someone conceded a tax form and got burned. Fix: ask for the Constitution during onboarding, and keep a 30-day "Hansard" archive that you can search but not browse.

## ⚖️ Trial: Rushmoor Thirds vs For Today Only
Vera called these two close, so I ran the trial.

**⚖️ VERDICT: Rushmoor Thirds (3–2)**
| Juror lens | Vote | Conf. | Reason |
|---|---|---|---|
| End user | Rushmoor | 3 | Nothing disappears unless I swipe it, and the Recount helps right when I'd give up |
| 3am engineer | For Today | 3 | One date field plus a wipe; much less state to break |
| Skeptical investor | Rushmoor | 3 | For Today copies Check and Slate; the voting mechanic is harder for competitors to copy |
| Curious 12-year-old | For Today | 3 | "Your list disappears every night" is clear right away, with no onboarding |
| Historian 2036 | Rushmoor | 3 | Voting and the active-day clock could become standard patterns |

**Dissent worth hearing:** For Today is far simpler to explain and to keep running.

**Average scores (impact/feasibility/originality/risk, normalized to 1–5):** Rushmoor 3.6 / 3.5 / 3.8 / 3.2 · For Today 3.2 / 4.6 / 2.3 / 2.7

This was 3–2 with every juror at the same middling confidence, so treat it as a hung jury in spirit. **Merge suggestion:** keep Rushmoor and take two things from For Today. First, the "clean slate on return" (which is Vera's snap election). Second, its one-sentence explanation. Vera's validation test still applies: 8 people with ADHD, 4 per prototype, using their real backlogs.


---

## `.adhd/tangents.md` written by the run

### Tangents 🐿️

## 2026-10-15 — ADHD to-do app people keep using

- Rushmoor elects by thirds — a third of the council is always fresh. Decent model for a team's rotating on-call.
- Metalcore breakdowns are basically scheduled dopamine spikes. Is song structure an ADHD-friendly attention format?
- An app that deletes your data by default = privacy selling point and guilt fix in one.
- Why does doing your own laundry feel impossible but folding someone else's feels fine? A separate "tasks for other people" app is hiding there.
- Mushroom fruiting depends on humidity, not time. What's "task humidity"? Probably mood.
- The For Today discography reads like an arc: community, portraits, breaking, immortality, fighting the silence, waking. Accidental habit-formation curve.

### Graveyard
- Album Eras — six mini-apps to maintain; breaks routines
- Body Double Ghost — Alongside already shipped it
- Doorway Tasks — Apple Reminders has it; iOS setup pain
- Ward Map — a map of neglect is still a guilt map
- Mycelium List — one-visible-task already exists
- Casino Floor — exploits the users it claims to serve
- The List Gets Slower — punishes capture, the one thing that works
- You Are the Notification — iOS turns it into Shortcuts busywork
- Tasks as Food That Rots — rot is guilt with a texture
- Dice Mode — a toy; fun once
- Air Traffic Control — one-task focus is generic
- Hum of Unfinished — audible guilt drone, muted by day 2
- 1890 Telegram — a cute limit, not a system
- 2090 Dopamine Ledger — no product here
- One User Forever — no mechanic
- Ten Thousand Doers — cold start kills it
- Wake Ritual — Addie covers it
- Fight the Silence — voice input is a feature, not a concept
- Parliament bundle (1+2+24) — three layers of forgetting nobody can explain
- Ghost of Yesterday-You, Eras novelty detector, Next Doorway — parents killed
