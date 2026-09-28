"""Tests for tools/check_numbers.py: sidecars run, and their QUOTED values appear in the text."""

import importlib.util
import io
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from fractions import Fraction
from pathlib import Path

TOOL = Path(__file__).resolve().parent.parent / "tools" / "check_numbers.py"
spec = importlib.util.spec_from_file_location("check_numbers", TOOL)
cn = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cn)

SECTION = r"""# Sums

::: {#exm-witness}
[A witness]
Take \( x = -3 \) and \( h = \frac{3}{2} \); then \( x^2 = 9 \), and \( 2{,}047 = 23 \cdot 89 \).
:::

::: {.solution}
Indeed \( h^2 = 2.25 > 2 \) and \( q^2 = 2m^2 \).
:::

::: {#exm-unchecked}
[Unchecked]
Choose \( N = 12 \), then \( 0.75 < 1 \).
:::

::: {#def-plain}
[Plain]
A set is a thing, with \( a = 0 \) allowed.
:::
"""


class NumbersTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        ch = self.root / "src" / "ch03-three"
        ch.mkdir(parents=True)
        (ch / "01-sums.md").write_text(SECTION)
        self.v = self.root / "verify" / "ch03"
        self.v.mkdir(parents=True)
        (self.v / "_helper.py").write_text("raise SystemExit(1)\n")   # helpers are not run

    def tearDown(self):
        self.tmp.cleanup()

    def sidecar(self, name, body):
        (self.v / f"{name}.py").write_text(body)

    def run_check(self, run=True):
        return cn.find_violations(self.root / "verify", self.root / "src", run=run,
                                  python=sys.executable, root=self.root,
                                  crossref=self.root / "none.json")

    def test_passing_sidecar_with_quoted_values_is_clean(self):
        self.sidecar("exm-witness",
                     "from fractions import Fraction as F\n"
                     "QUOTED = {'x': -3, 'h': F(3, 2), 'h^2': 2.25, 'x^2': 9,\n"
                     "          'factors': (2047, (23, 89)), 'holds': True, 'q^2': '2m^2'}\n"
                     "assert QUOTED['x'] ** 2 == QUOTED['x^2']\n")
        fatal, advisory = self.run_check()
        self.assertEqual(fatal, [])
        self.assertTrue(any("exm-unchecked" in m for _, _, m in advisory))
        self.assertFalse(any("def-plain" in m for _, _, m in advisory))   # a = 0 is not a constant
        self.assertFalse(any("exm-witness" in m for _, _, m in advisory))

    def test_failing_sidecar_is_fatal(self):
        self.sidecar("exm-witness", "QUOTED = {}\nassert 1 == 2, 'boom'\n")
        fatal, _ = self.run_check()
        self.assertEqual(len(fatal), 1)
        self.assertIn("sidecar fails", fatal[0][2])
        self.assertIn("boom", fatal[0][2])
        fatal, _ = self.run_check(run=False)
        self.assertEqual(fatal, [])

    def test_quoted_value_missing_from_text_is_fatal(self):
        self.sidecar("exm-witness", "QUOTED = {'x': 3, 'y': -9, 'z': 7, 's': '2m^3'}\n")
        fatal, _ = self.run_check(run=False)
        msgs = " ".join(m for _, _, m in fatal)
        self.assertNotIn("'x'", msgs)                   # 3 appears (inside -3 and 3/2 is fine)
        self.assertIn("'y'", msgs)                      # -9 does not (only 9)
        self.assertIn("'z'", msgs)
        self.assertIn("'s'", msgs)

    def test_orphan_sidecar_and_unreadable_value(self):
        self.sidecar("exm-nowhere", "QUOTED = {'a': 1}\n")
        self.sidecar("exm-witness", "import math\nQUOTED = {'r': math.sqrt(2)}\n")
        fatal, advisory = self.run_check(run=False)
        self.assertTrue(any("no block {#exm-nowhere}" in m for _, _, m in fatal))
        self.assertTrue(any("not a literal" in m for _, _, m in advisory))

    def test_forms(self):
        text = r"\( \frac12 \), \( \tfrac{1}{10} \), \( 7/4 \), \( 0.125 \), \( -\frac{5}{3} \)"
        sq = text.replace(" ", "")
        for v in (Fraction(1, 2), Fraction(1, 10), Fraction(7, 4), Fraction(1, 8),
                  Fraction(-5, 3), 0.125):
            for _, rx in cn.forms(v):
                self.assertTrue(cn.appears(rx, text, sq), v)
        for v in (Fraction(5, 3) + 1, 12, -7):
            self.assertFalse(all(cn.appears(rx, text, sq) for _, rx in cn.forms(v)), v)
        self.assertEqual(cn.forms(True), [("True", None)])

    def test_load_quoted(self):
        self.sidecar("exm-witness", "from fractions import Fraction\n"
                                    "QUOTED = {'a': -Fraction(1, 3), 'b': [1, {2}], 'c': {'k': 5}}\n")
        q = cn.load_quoted(self.v / "exm-witness.py")
        self.assertEqual(q, {"a": Fraction(-1, 3), "b": (1, (2,)), "c": (5,)})
        self.sidecar("exm-none", "x = 1\n")
        self.assertIsNone(cn.load_quoted(self.v / "exm-none.py"))

    def test_main_exit_code(self):
        self.sidecar("exm-witness", "QUOTED = {'x': -3}\n")
        with redirect_stdout(io.StringIO()) as out:
            code = cn.main(["--verify", str(self.root / "verify"), "--src", str(self.root / "src"),
                            "--python", sys.executable, "--advisory"])
        self.assertEqual(code, 0)
        self.assertIn("1 sidecar(s) run: 0 fatal", out.getvalue())


if __name__ == "__main__":
    unittest.main()
