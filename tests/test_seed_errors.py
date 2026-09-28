"""Tests for tools/seed_errors.py: planting known errors in a copy, and scoring recall."""

import importlib.util
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

TOOL = Path(__file__).resolve().parent.parent / "tools" / "seed_errors.py"
spec = importlib.util.spec_from_file_location("seed_errors", TOOL)
se = importlib.util.module_from_spec(spec)
spec.loader.exec_module(se)

SECTION = r"""# Suprema

This section is about suprema and how the rest of the chapter uses them in several proofs below.

::: {#thm-sup-sum}
[Sum]
Let \( A, B \subseteq \nR \) be non-empty and bounded above. Then \( \sup(A + B) = \sup A + \sup B \).
:::

::: {.proof}
By @thm-other, for every \( \varepsilon > 0 \) there is \( a \in A \) with \( a > \sup A - \varepsilon \).
:::

::: {#exm-constant}
[A constant]
Take \( N \coloneqq 12 \) and \( \delta = \frac{1}{10} \).
:::

## Exercises

::: {#exr-a-one}
[A1]
Show that \( x < 3 \) implies \( x \le 3 \).
:::

::: {.solution}
Since \( x < 3 \), also \( x \le 3 \).
:::

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee Q}
  \open
  \hypo {2} {P}
  \have {3} {Q \vee P} \oi{2}
  \close
  \open
  \hypo {4} {Q}
  \have {5} {Q \vee P} \oi{4}
  \close
  \have {6} {Q \vee P} \oe{1,2-3,4-5}
\end{nd}$
\end{center}
```
"""


class PlantTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.ch = self.root / "src" / "ch03-three"
        self.ch.mkdir(parents=True)
        (self.ch / "01-suprema.md").write_text(SECTION)
        (self.ch / "index.md").write_text("# Three\n")

    def tearDown(self):
        self.tmp.cleanup()

    def test_every_kind_has_a_site(self):
        cands = se.candidates(self.ch, list(se.KINDS))
        for kind in se.KINDS:
            self.assertTrue(cands[kind], kind)
        drops = [new for _, _, new, _ in cands["drop-hypothesis"]]
        self.assertIn(r"Let \( A, B \subseteq \nR \) be bounded above. Then \( \sup(A + B) = \sup A + \sup B \).",
                      drops)
        swaps = [new for _, _, new, _ in cands["swap-quantifiers"]]
        self.assertTrue(any("there exists \\( \\varepsilon > 0 \\) for every \\( a \\in A \\)" in s
                            for s in swaps))
        boxes = [d for _, _, _, d in cands["closed-box-cite"]]
        self.assertTrue(any("line 6 now cites line" in d for d in boxes))

    def test_plant_is_deterministic_and_line_preserving(self):
        k1 = se.plant(self.ch, self.root / "a", 6, seed=3)
        k2 = se.plant(self.ch, self.root / "b", 6, seed=3)
        self.assertEqual(k1, k2)
        self.assertEqual(len(k1), 6)
        self.assertEqual(len({e["kind"] for e in k1}), 6)            # round-robin over kinds
        orig = (self.ch / "01-suprema.md").read_text().split("\n")
        copy = (self.root / "a" / "ch03-three" / "01-suprema.md").read_text().split("\n")
        self.assertEqual(len(orig), len(copy))
        changed = {i + 1 for i, (x, y) in enumerate(zip(orig, copy)) if x != y}
        self.assertEqual(changed, {e["line"] for e in k1})
        for e in k1:
            self.assertEqual(copy[e["line"] - 1], e["planted"])
            self.assertEqual(orig[e["line"] - 1], e["original"])
        self.assertTrue((self.root / "a" / "ch03-three" / "index.md").exists())
        other = [se.plant(self.ch, self.root / "c", 2, seed=k, kinds=["perturb-constant", "wrong-variant"])
                 for k in range(6)]
        self.assertGreater(len({json.dumps(k) for k in other}), 1)   # the seed matters

    def test_kinds_subset(self):
        key = se.plant(self.ch, self.root / "a", 5, seed=0, kinds=["perturb-constant"])
        self.assertTrue(key and all(e["kind"] == "perturb-constant" for e in key))

    def test_cli_keeps_key_outside_copy(self):
        out = self.root / "scratch" / "ch03"
        with redirect_stdout(io.StringIO()):
            se.main(["plant", str(self.ch), "--out", str(out), "-n", "3", "--seed", "1"])
        key = json.loads((self.root / "scratch" / "ch03.key.json").read_text())
        self.assertEqual(len(key["errors"]), 3)
        with self.assertRaises(SystemExit):
            se.main(["plant", str(self.ch), "--out", str(out), "--key", str(out / "k.json")])


REVIEW = """# Referee A

| # | Location | Claim | Verdict | Evidence |
|---|---|---|---|---|
| 1 | §01 | the sum rule | correct | 01-suprema.md:7 is fine |
| 2 | §01 thm-sup-sum | hypotheses | **gap** | 01-suprema.md:7 lost non-empty |
| 3 | §01 | the proof | error | 01:12, quantifiers swapped |
| 4 | §02 | elsewhere | minor | 02-other.md:40 |
"""


class ScoreTests(unittest.TestCase):
    KEY = [
        {"id": 1, "kind": "drop-hypothesis", "file": "01-suprema.md", "line": 7},
        {"id": 2, "kind": "swap-quantifiers", "file": "01-suprema.md", "line": 11},
        {"id": 3, "kind": "perturb-constant", "file": "01-suprema.md", "line": 16},
    ]

    def test_parse_review_table_skips_correct_rows(self):
        f = se.parse_findings(REVIEW)
        self.assertEqual([n for n, _ in f], [6, 7, 8])
        self.assertEqual(f[1][1], [("01", 12, 12)])

    def test_parse_simple_list(self):
        f = se.parse_findings("src/ch03-three/01-suprema.md:16\nnothing here\n01-suprema.md:30-33 bad\n")
        self.assertEqual(f, [(1, [("01-suprema.md", 16, 16)]), (3, [("01-suprema.md", 30, 33)])])

    def test_score(self):
        r = se.score(self.KEY, se.parse_findings(REVIEW), tolerance=1)
        self.assertEqual((r["found"], r["planted"], r["recall"]), (2, 3, 0.667))
        self.assertEqual([e["id"] for e in r["missed"]], [3])
        self.assertEqual(r["unmatched_findings"], [8])
        self.assertEqual(r["per_kind"]["perturb-constant"], {"planted": 1, "found": 0})
        r0 = se.score(self.KEY, se.parse_findings(REVIEW), tolerance=0)
        self.assertEqual(r0["found"], 1)                       # 01:12 is one off line 11

    def test_score_cli_json(self):
        with tempfile.TemporaryDirectory() as d:
            key, rev, out = Path(d) / "k.json", Path(d) / "r.md", Path(d) / "s.json"
            key.write_text(json.dumps({"chapter": "ch03-three", "seed": 1, "errors": self.KEY}))
            rev.write_text(REVIEW)
            with redirect_stdout(io.StringIO()) as buf:
                se.main(["score", str(key), str(rev), "--json", str(out)])
            self.assertIn("Recall 2/3", buf.getvalue())
            self.assertEqual(json.loads(out.read_text())["recall"], 0.667)


if __name__ == "__main__":
    unittest.main()
