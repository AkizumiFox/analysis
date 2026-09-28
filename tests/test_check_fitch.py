"""Tests for tools/check_fitch.py: Fitch derivations and truth tables, checked by machine."""

import importlib.util
import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

TOOL = Path(__file__).resolve().parent.parent / "tools" / "check_fitch.py"
spec = importlib.util.spec_from_file_location("check_fitch", TOOL)
fitch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fitch)


def block(body, marker=False):
    head = "```{=latex}\n" + ("% expect-invalid\n" if marker else "") + "\\begin{center}\n$\\begin{nd}\n"
    return "Some prose.\n\n" + head + body.strip("\n") + "\n\\end{nd}$\n\\end{center}\n```\n"


def errors(body, marker=False):
    e, _, _ = fitch.check_text(block(body, marker))
    return [m for _, m in e]


TRANSITIVE = r"""
  \hypo {1} {P \to Q}
  \hypo {2} {Q \to R}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \have {5} {R} \ie{2,4}
  \close
  \have {6} {P \to R} \ii{3-5}
"""


class FormulaTests(unittest.TestCase):
    def test_precedence_and_macros(self):
        f = fitch.parse_formula(r"\neg P \wedge Q \to R \vee {\bot}")
        self.assertEqual(f, ("imp", ("and", ("not", ("var", "P")), ("var", "Q")),
                             ("or", ("var", "R"), ("bot",))))

    def test_leftrightarrow_is_not_eaten_by_left(self):
        self.assertEqual(fitch.parse_formula(r"P \leftrightarrow Q")[0], "iff")

    def test_non_propositional_text_is_rejected(self):
        for text in (r"x > 2", r"\quad \vdots", r"\forall x P(x)"):
            with self.assertRaises(fitch.ParseError):
                fitch.parse_formula(text)


class DerivationTests(unittest.TestCase):
    def test_valid_derivation_is_clean(self):
        self.assertEqual(errors(TRANSITIVE), [])

    def test_all_propositional_rules_accepted(self):
        body = r"""
  \hypo {1} {P \wedge (Q \vee R)}
  \hypo {2} {P \leftrightarrow S}
  \have {3} {P} \ae{1}
  \have {4} {Q \vee R} \ae{1}
  \have {5} {S} \bie{2,3}
  \open
  \hypo {6} {Q}
  \have {7} {S \wedge Q} \ai{5,6}
  \have {8} {(S \wedge Q) \vee R} \oi{7}
  \close
  \open
  \hypo {9} {R}
  \have {10} {(S \wedge Q) \vee R} \oi{9}
  \close
  \have {11} {(S \wedge Q) \vee R} \oe{4,6-8,9-10}
  \open
  \hypo {12} {\neg P}
  \have {13} {\bot} \ne{3,12}
  \have {14} {\bot} \r{13}
  \close
  \have {15} {\neg\neg P} \ni{12-14}
  \open
  \hypo {16} {\neg S}
  \have {17} {\bot} \ne{5,16}
  \close
  \have {18} {S} \raa{16-17}
  \have {19} {S} \r{18}
"""
        self.assertEqual(errors(body), [])
        ex_falso = r"\hypo {1} {P} \hypo {2} {\neg P} \have {3} {\bot} \ne{1,2} \have {4} {Q} \be{3}"
        self.assertEqual(errors(ex_falso), [])
        self.assertTrue(errors(ex_falso.replace(r"\be{3}", r"\be{1}")))

    def test_citing_inside_a_closed_box(self):
        body = TRANSITIVE + r"  \have {7} {R} \r{5}" + "\n"
        self.assertEqual(errors(body), ["line 7 cites line 5, inside a box that has closed"])

    def test_citing_a_later_line_and_a_missing_line(self):
        body = r"""
  \hypo {1} {P}
  \have {2} {P \wedge P} \ai{1,3}
  \have {3} {P} \r{1}
  \have {4} {P} \r{9}
"""
        msgs = errors(body)
        self.assertIn("line 2 cites line 3, a later line", msgs)
        self.assertIn("line 4 cites line 9, which does not exist", msgs)

    def test_range_must_be_a_closed_box(self):
        body = r"""
  \hypo {1} {P}
  \hypo {2} {Q}
  \have {3} {P \to Q} \ii{1-2}
"""
        self.assertTrue(any("not a box" in m for m in errors(body)))

    def test_citing_an_open_box(self):
        body = r"""
  \open
  \hypo {1} {P}
  \have {2} {P \to P} \ii{1-1}
  \close
"""
        self.assertTrue(any("still open" in m for m in errors(body)))

    def test_wrong_rule_shapes(self):
        body = r"""
  \hypo {1} {P \to Q}
  \hypo {2} {Q}
  \have {3} {P} \ie{1,2}
  \open
  \hypo {4} {P}
  \have {5} {\bot} \by{assumed}{}
  \close
  \have {6} {P} \raa{4-5}
  \have {7} {P \wedge Q} \ae{1}
"""
        msgs = errors(body)
        self.assertTrue(any(m.startswith("line 3: →E") for m in msgs), msgs)
        self.assertTrue(any(m.startswith("line 6: RAA") for m in msgs), msgs)
        self.assertTrue(any(m.startswith("line 7: ∧E") for m in msgs), msgs)

    def test_duplicate_labels_and_bad_box(self):
        body = r"""
  \hypo {1} {P}
  \open
  \have {2} {P} \r{1}
  \close
  \have {2} {P} \r{1}
"""
        msgs = errors(body)
        self.assertIn("line label 2 used twice", msgs)
        self.assertTrue(any("does not begin with an assumption" in m for m in msgs))

    def test_wrong_number_of_citations(self):
        self.assertTrue(any("cites a line, a line" in m for m in
                            errors(r"\hypo {1} {P} \have {2} {P \wedge P} \ai{1}")))

    def test_schematic_and_vdots_are_notes(self):
        body = r"""
  \open
  \hypo {i} {\neg P}
  \have {} {\quad \vdots}
  \have {j} {\bot}
  \close
  \have {k} {P} \raa{i-j}
"""
        e, notes, _ = fitch.check_text(block(body))
        self.assertEqual(e, [])
        self.assertTrue(any("schematic" in m for _, m in notes))
        body2 = r"""
  \have {1} {P \vee \neg P} \by{excluded middle}{}
  \open
  \hypo {2} {\neg P}
  \have {} {\quad \vdots}
  \have {3} {\bot}
  \close
  \have {4} {P} \raa{2-3}
"""
        e, notes, _ = fitch.check_text(block(body2))
        self.assertEqual(e, [])
        self.assertTrue(any("follows \\vdots" in m for _, m in notes))
        self.assertTrue(any("justified by text" in m for _, m in notes))

    def test_expect_invalid(self):
        bad = TRANSITIVE + r"  \have {7} {R} \r{5}" + "\n"
        e, notes, counts = fitch.check_text(block(bad, marker=True))
        self.assertEqual(e, [])
        self.assertEqual(counts["expected_invalid"], 1)
        e, _, _ = fitch.check_text(block(TRANSITIVE, marker=True))
        self.assertEqual([m for _, m in e], ["marked % expect-invalid but checks clean"])


class TruthTableTests(unittest.TestCase):
    TABLE = r"""
\[
\begin{array}{cc|cc}
P & Q & P \to Q & \neg P \vee Q \\
\hline
\mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} \\
\mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{F} & \mathrm{F} & \mathrm{T} & %s
\end{array}
\]
"""

    def test_correct_table(self):
        e, _, counts = fitch.check_text(self.TABLE % r"\mathrm{T}")
        self.assertEqual((e, counts["tables"]), ([], 1))

    def test_wrong_entry(self):
        e, _, _ = fitch.check_text(self.TABLE % r"\mathrm{F}")
        self.assertEqual(len(e), 1)
        self.assertIn("row 4", e[0][1])

    def test_non_truth_table_array_ignored(self):
        e, _, counts = fitch.check_text(r"\[ \begin{array}{cc} 1 & 2 \\ \hline 3 & 4 \end{array} \]")
        self.assertEqual((e, counts["tables"]), ([], 0))


class CliTests(unittest.TestCase):
    def test_exit_codes(self):
        with tempfile.TemporaryDirectory() as tmp:
            good = Path(tmp) / "good.md"
            good.write_text(block(TRANSITIVE))
            bad = Path(tmp) / "bad.md"
            bad.write_text(block(TRANSITIVE + r"  \have {7} {R} \r{5}" + "\n"))
            with redirect_stdout(io.StringIO()):
                self.assertEqual(fitch.main([str(good)]), 0)
            out = io.StringIO()
            with redirect_stdout(out):
                self.assertEqual(fitch.main([str(bad)]), 1)
            self.assertIn("bad.md", out.getvalue())


if __name__ == "__main__":
    unittest.main()
