<div align="center">

# ⚡ ADHD Mode

### Un team di brainstorming neurodivergente per Claude Code.

**Zap** ha 400 schede aperte nel cervello. **Doc** dice sì a tutto e poi ti spiega come costruirlo. **Vera** ha un gusto perfetto e ne boccia l'80%. Quando non sono d'accordo decide una **Corte delle Idee** con una giuria cieca.

[🇬🇧 English](README.md)

</div>

---

Se chiedi idee a un LLM ti dà l'idea **più probabile**, cioè la media di tutto quello che ha letto. Va benissimo per il codice ed è pessimo per la creatività.

ADHD Mode divide il pensiero come fanno gli studi creativi. Un agente genera senza freni e non può costruire nulla. Uno lo rende reale dal lato tecnico. Uno lo taglia col gusto. Ogni fase gira come subagent separato, con il proprio contesto: così l'idea folle non viene "normalizzata" dal critico a metà pensiero.

Serve per idee di prodotto, concept di UI e 3D, naming, architetture alternative e **per sbloccarti sui bug**.

## Installazione

```bash
/plugin marketplace add MarcoZorn/adhd-mode
/plugin install adhd-mode@adhd-mode
```

## Comandi

| Comando | Cosa fa |
|---|---|
| `/adhd-mode:adhd <problema>` | Pipeline completa: Zap ⚡ → Doc 🧪 → Vera 🎯. Finisce con un'idea vincente concreta e il primo passo da fare domani. |
| `/adhd-mode:adhd bug: <sintomo>` | Modalità bug: 10+ ipotesi sulla causa (anche quelle assurde), ordinate dalla **più economica da testare**, ognuna con un controllo da 5 minuti. |
| `… --squirrel` | Casualità vera, presa da fuori dal modello (articoli Wikipedia a caso) e usata come analogia forzata. |
| `… --trial` | Le due idee migliori vanno in tribunale. |
| `/adhd-mode:trial <A> vs <B>` | Corte delle Idee ⚖️: due avvocati, cinque giurati isolati, verdetto con conteggio dei voti e il dissenso migliore. |
| `/adhd-mode:squirrel <problema>` | SQUIRREL! 🐿️ Tre idee per ogni articolo pescato a caso, più un'idea che li fa scontrare. |
| `/adhd-mode:evolve <problema>` | 🧬 Algoritmo genetico per idee: generazioni di idee che si incrociano, mutano e vengono selezionate dalla giuria. |

Puoi anche dire "vai in ADHD mode su questo" e Claude sceglie da solo.

## Il team

- **⚡ Zap**: iperattivo e curioso. Fa il Why-Drill (perché, per 5 livelli), usa 10 motori creativi nominati e le idee ovvie le scarta. **Non può scrivere né codice né file**: ha solo strumenti di lettura.
- **🧪 Doc**: ingegnere un po' pazzo. "Sì, e si fa così", ma ogni affermazione è etichettata `[EXISTS]` / `[PLAUSIBLE]` / `[INVENTED]`. Cerca sul web se l'idea esiste già.
- **🎯 Vera**: designer con un gusto spietato. KEEP / MERGE / KILL, poi un solo vincitore reso concreto, la versione minima e la 📮 *Cartolina dal 2031* (un pre-mortem).
- **⚖️ Corte**: giurati isolati con 5 prospettive diverse, memorie anonime, ordine casuale per ogni giurato contro il bias di posizione.
- **🐿️ Cimitero delle tangenti**: le divagazioni e le idee bocciate finiscono in `.adhd/tangents.md`.

## Licenza

MIT © Marco Zorn
