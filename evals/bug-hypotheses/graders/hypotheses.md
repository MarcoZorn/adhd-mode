---
type: llm
---

PASS if the final answer lists at least 6 distinct plausible root-cause hypotheses (should include at least one time/date related one such as DST, timezone or calendar edge cases, and at least one non-obvious one), each paired with a concrete quick check to confirm or rule it out, and orders them by how cheap they are to test.
FAIL if it offers fewer than 6 hypotheses, gives no concrete checks, or jumps to a single fix.
