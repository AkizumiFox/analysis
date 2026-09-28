"""Tests for tools/check_notation.py: macros missing from NOTATION.md, symbols with two meanings."""

import importlib.util
import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

TOOL = Path(__file__).resolve().parent.parent / "tools" / "check_notation.py"
spec = importlib.util.spec_from_file_location("check_notation", TOOL)
cn = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cn)

MACROS = r"""
\newcommand{\nR}{\mathbb{R}}
\providecommand\abs[1]{\lvert #1 \rvert}
\def \k {\mathbf{k}}
\DeclareMathOperator{\osc}{osc}
% \newcommand{\commented}{x}
"""

NOTATION = r"""# Notation
| `\nR` | reals |
| `\abs{x}` | absolute value |
"""

CH3 = r"""# One

We write \( \nR^+ \) for the positive reals, and \( \abs{x} \) uses \( \osc \) and \( \frac12 \).

::: {#def-gap}
[Gap]
The **gap** of \( A \) is \( \operatorname{g}(A) \coloneqq \sup A - \inf A \). We write \( P \) for it.
:::

\begin{tikzpicture}
  \foreach \k in {0,1} { \draw (\k,0) -- (\k,1); }
\end{tikzpicture}
"""

CH4 = r"""# Two

::: {#def-other-gap}
[Other gap]
For sets \( A, B \), the gap is denoted by \( \operatorname{g}(A) \), the distance from \( A \) to \( B \).
:::
"""


class NotationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.src = root / "src"
        for name, text in (("ch03-one", CH3), ("ch04-two", CH4)):
            (self.src / name).mkdir(parents=True)
            (self.src / name / "01-a.md").write_text(text)
        self.macros = root / "macros.tex"
        self.macros.write_text(MACROS)
        self.notation = root / "NOTATION.md"
        self.notation.write_text(NOTATION)

    def tearDown(self):
        self.tmp.cleanup()

    def advisories(self, parts):
        return [m for _, _, m in cn.find_violations(self.src, self.notation, self.macros, parts)]

    def test_book_macros(self):
        self.assertEqual(cn.book_macros(self.macros), {"nR", "abs", "k", "osc"})

    def test_unlisted_macro_reported_tikz_and_latex_ignored(self):
        msgs = self.advisories({})
        self.assertTrue(any("\\osc" in m for m in msgs))
        self.assertFalse(any("\\k " in m or "\\frac" in m or "\\nR " in m for m in msgs))

    def test_symbols_collected(self):
        syms = {(s, m) for _, s, m in cn.symbols_in(CH3)}
        self.assertIn(("\\operatorname{g}(A)", "def-gap"), syms)
        self.assertIn(("\\nR^+", None), syms)
        self.assertFalse(any(s == "P" for s, _ in syms))        # a bare letter is a variable

    def test_two_meanings_within_a_part_only(self):
        same = {"ch03-one": "Part I", "ch04-two": "Part I"}
        msgs = self.advisories(same)
        self.assertTrue(any("symbol \\operatorname{g}(A) has 2 meanings in Part I" in m for m in msgs))
        apart = {"ch03-one": "Part I", "ch04-two": "Part II"}
        self.assertFalse(any("meanings" in m for m in self.advisories(apart)))

    def test_main_is_advisory(self):
        with redirect_stdout(io.StringIO()) as out:
            code = cn.main(["--src", str(self.src), "--notation", str(self.notation),
                            "--macros", str(self.macros), "--config", "/nonexistent", "--list"])
        self.assertEqual(code, 0)
        self.assertIn("notation advisory note(s)", out.getvalue())
        with redirect_stdout(io.StringIO()):
            self.assertEqual(cn.main(["--src", str(self.src), "--notation", str(self.notation),
                                      "--macros", str(self.macros), "--strict"]), 1)


if __name__ == "__main__":
    unittest.main()
