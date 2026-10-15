"""Renders docs/demo.svg: an animated terminal replay of examples/adhd-todo-app.md."""
from html import escape
from pathlib import Path

LINES = [  # (seconds, color, text) — all content taken from the real example run
    (0.0, "#e6e6e6", "$ /adhd-mode:adhd a to-do app people with ADHD would actually keep using --squirrel"),
    (1.4, "#c49a6c", "🐿️  SQUIRREL  For Today (metalcore band) · Rushmoor Borough Council election"),
    (2.6, "#f5d547", "⚡ Zap    25 ideas · why-drill: lists turn into guilt piles by day 9"),
    (3.8, "#5fd38d", "🧪 Doc    prior art: 1 NOVEL · 2 PARTIAL · 2 ALREADY EXIST"),
    (5.0, "#c792ea", "🎯 Vera   21 killed · winner: Rushmoor Thirds"),
    (6.2, "#ff7a7a", "⚖️  Court  Rushmoor Thirds  vs  For Today Only"),
    (7.0, "#82aaff", "   juror · end user           → Rushmoor"),
    (7.6, "#82aaff", "   juror · 3am engineer       → For Today"),
    (8.2, "#82aaff", "   juror · skeptical investor → Rushmoor"),
    (8.8, "#82aaff", "   juror · curious 12-yo      → For Today"),
    (9.4, "#82aaff", "   juror · historian 2036     → Rushmoor"),
    (10.4, "#ffffff", "⚖️  VERDICT  Rushmoor Thirds (3–2)"),
    (11.4, "#e6e6e6", "   “Every 3 days, a third of your tasks stand for re-election.”"),
    (12.6, "#c49a6c", "📮 2031: everyone re-elected everything → cap parliament at 21 seats"),
]
TOTAL = 18.0
W, LH, TOP = 980, 26, 56
H = TOP + LH * len(LINES) + 24

css, rows = [], []
for i, (t, color, text) in enumerate(LINES):
    a, b = t / TOTAL * 100, (t + 0.25) / TOTAL * 100
    css.append(f"@keyframes l{i}{{0%,{a:.2f}%{{opacity:0}}{b:.2f}%,96%{{opacity:1}}100%{{opacity:0}}}}"
               f".l{i}{{animation:l{i} {TOTAL}s linear infinite}}")
    weight = ' font-weight="700"' if "VERDICT" in text else ""
    rows.append(f'<text class="l{i}" x="24" y="{TOP + i * LH}" fill="{color}"{weight}>{escape(text)}</text>')

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="ADHD Mode demo: Zap, Doc, Vera and a blind jury pick a winning idea">
<style>text{{font:15px ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;white-space:pre;opacity:0}}{"".join(css)}</style>
<rect width="{W}" height="{H}" rx="12" fill="#14141a"/>
<circle cx="22" cy="20" r="6" fill="#ff5f57"/><circle cx="42" cy="20" r="6" fill="#febc2e"/><circle cx="62" cy="20" r="6" fill="#28c840"/>
<text x="{W // 2}" y="25" fill="#777" text-anchor="middle" style="opacity:1;font-size:13px">claude — adhd-mode (replay of a real run)</text>
{chr(10).join(rows)}
</svg>
'''
out = Path(__file__).with_name("demo.svg")
out.write_text(svg)
assert out.read_text().count("<text class=") == len(LINES)
print(out)
