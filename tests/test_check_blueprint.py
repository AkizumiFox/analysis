"""Tests for blueprint/check_blueprint.py: labels in hand-written blueprints."""

import importlib.util
import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

TOOL = Path(__file__).resolve().parent.parent / "blueprint" / "check_blueprint.py"
spec = importlib.util.spec_from_file_location("check_blueprint", TOOL)
cb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cb)

BP5 = """<!-- hand-written -->
# Blueprint: Chapter 5

**Labels.** `def-countable`, `thm-countable-union`.

- Proof of `thm-countable-union` uses `def-countable`.
- Cite `thm-induction` from Chapter 4, and `@thm-rationals-countable`.
- It needs `lem-later` here, but `lem-later` is created further down.
- **`lem-later`**: stated here.
- Recall `thm-construct-n` (from Chapter 6).
"""
BP9 = """<!-- hand-written -->
- `def-countable` is defined again here.
"""
LABELS = {"thm-induction": [(4, "src/ch04/01.md")],
          "def-countable": [(5, "src/ch05/01.md")],
          "thm-construct-n": [(6, "src/ch06/01.md")]}


class BlueprintTests(unittest.TestCase):
    def test_mentions(self):
        ms = cb.mentions(BP5)
        self.assertEqual([l for _, l, h in ms if h == "create"],
                         ["def-countable", "thm-countable-union", "lem-later"])
        cites = {(l, n) for n, l, h in ms if h == "cite"}
        self.assertIn(("thm-induction", 7), cites)
        self.assertIn(("thm-rationals-countable", 7), cites)
        self.assertIn(("lem-later", 8), cites)          # same line, after its creation

    def test_violations(self):
        problems = cb.find_violations({5: BP5, 9: BP9}, LABELS, optional={6})
        text = "\n".join(f"{ch}:{n}: {m}" for ch, n, m in problems)
        self.assertIn("5:7: cites thm-rationals-countable, which is defined nowhere", text)
        # lem-later's first mention (line 8) creates it, so no citation problem
        self.assertNotIn("lem-later", text)
        self.assertIn("5:10: main-line chapter cites thm-construct-n from optional Chapter 6", text)
        self.assertIn("9:2: creates def-countable, already defined in src/ch05/01.md", text)
        self.assertIn("9:2: creates def-countable, also created by the blueprint of Chapter 5", text)
        self.assertIn("5:4: creates def-countable, also created by the blueprint of Chapter 9", text)
        self.assertFalse(any("thm-induction" in m for _, _, m in problems))

    def test_cited_before_created(self):
        bp = "<!-- hand-written -->\n- Cite `lem-x` first.\n- Then `lem-x` again.\n"
        # the first mention is a citation (cite word); the second, with no cite word, creates
        problems = cb.find_violations({3: bp}, {}, set())
        self.assertEqual([(n, m) for _, n, m in problems],
                         [(2, "cites lem-x, which is created later in this blueprint (line 3)")])
        bp2 = "<!-- hand-written -->\n- Cite `@lem-x` first.\n- **`lem-x`**: created.\n"
        # an @-mention never creates; the bold line has no cite word, so it creates
        problems = cb.find_violations({3: bp2}, {}, set())
        self.assertEqual([m for _, _, m in problems],
                         ["cites lem-x, which is created later in this blueprint (line 3)"])

    def test_optional_chapter_may_cite_anything(self):
        self.assertEqual(cb.find_violations({6: "<!-- hand-written -->\nCite `thm-construct-n`.\n"},
                                            LABELS, {6}), [])

    def test_optional_chapters_fallback_reader(self):
        with tempfile.TemporaryDirectory() as tmp:
            book = Path(tmp) / "book.yaml"
            book.write_text("chapters:\n- num: 1\n  optional: false\n- num: 6\n  title: x\n  optional: true\n")
            self.assertEqual(cb.optional_chapters(book), {6})

    def test_cli(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "bp").mkdir()
            (root / "src" / "ch05-c").mkdir(parents=True)
            (root / "src" / "ch05-c" / "01-a.md").write_text("::: {#def-countable}\n:::\n")
            (root / "bp" / "ch05.md").write_text(BP5)
            (root / "bp" / "ch07.md").write_text("generated, not hand-written: `thm-zzz`\n")
            (root / "book.yaml").write_text("chapters:\n- num: 6\n  optional: true\n")
            args = ["--src", str(root / "src"), "--blueprints", str(root / "bp"),
                    "--book", str(root / "book.yaml")]
            out = io.StringIO()
            with redirect_stdout(out):
                self.assertEqual(cb.main(args), 1)
            self.assertIn("1 hand-written blueprint(s) (5)", out.getvalue())
            with redirect_stdout(io.StringIO()):
                self.assertEqual(cb.main(args + ["--list"]), 0)


if __name__ == "__main__":
    unittest.main()
