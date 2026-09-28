"""Tests for tools/promises.py: forward pointers in prose, reconciled with STATUS.md."""

import importlib.util
import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

TOOL = Path(__file__).resolve().parent.parent / "tools" / "promises.py"
spec = importlib.util.spec_from_file_location("promises", TOOL)
pr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pr)

STATUS = """# Status

## Forward promises

| From | Promise | Target |
|---|---|---|
| Ch 3 §01 | quantifiers | Ch 4 |
| Ch 3 index | limits | Ch 9, Ch 10 (paid) |

## Other
"""


class PromiseTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.src = root / "src"
        ch3 = self.src / "ch03-three"
        ch4 = self.src / "ch04-four"
        ch3.mkdir(parents=True)
        ch4.mkdir(parents=True)
        (ch3 / "index.md").write_text("# Three\n\nChapters 9–10 do limits.\n")
        (ch3 / "01-a.md").write_text(
            "# A\n\n"
            "Chapter 4 proves this. Chapter 2 did that.\n"                  # 4 forward, 2 back
            "The linear-algebra companion, Chapter 7, has it.\n"          # companion: ignored
            "Section 3.2 does more, and §01 is here, and §03 is missing.\n"  # 3.2 fwd, §03 fwd
            "Chapter 4 proves it (@thm-four).\n"                           # linked: not a promise
            "Math \\( \\text{Chapter 12} \\) is ignored.\n"
            "```\nChapter 11 in code\n```\n")
        (ch3 / "02-b.md").write_text("# B\n\nChapter 5 and Chapter 6, see Chapter 5.\n")
        (ch4 / "01-x.md").write_text("# X\n\n::: {#thm-four}\n[Four]\nS.\n:::\n")
        self.status = root / "STATUS.md"
        self.status.write_text(STATUS)

    def tearDown(self):
        self.tmp.cleanup()

    def found(self):
        return sorted((p.file.split("/")[1], p.line, p.target, p.target_section)
                      for p in pr.find_promises(self.src))

    def test_find(self):
        self.assertEqual(self.found(), [
            ("01-a.md", 3, 4, None),
            ("01-a.md", 5, 3, 2),
            ("01-a.md", 5, 3, 3),
            ("02-b.md", 3, 5, None),
            ("02-b.md", 3, 6, None),
            ("index.md", 3, 9, None),
            ("index.md", 3, 10, None),
        ])

    def test_expand_ranges(self):
        self.assertEqual(pr.expand("2", "–5"), [2, 3, 4, 5])
        self.assertEqual(pr.expand("2", " and 4"), [2, 4])

    def test_parse_status(self):
        rows = pr.parse_status(self.status)
        self.assertEqual(len(rows), 2)
        self.assertEqual((rows[0].chapter, rows[0].sections, rows[0].targets), (3, {"01"}, {4}))
        self.assertEqual((rows[1].sections, rows[1].targets, rows[1].paid), ({"index"}, {9, 10}, True))

    def test_reconcile(self):
        missing = pr.reconcile(pr.find_promises(self.src), pr.parse_status(self.status),
                               pr.existing_sections(self.src))
        got = sorted((p.file.split("/")[1], p.target, p.target_section) for p, _ in missing)
        # §02 of ch03 exists (paid in-chapter); §03 does not; Ch 5 and 6 have no rows
        self.assertEqual(got, [("01-a.md", 3, 3), ("02-b.md", 5, None), ("02-b.md", 6, None)])

    def test_cli(self):
        out = io.StringIO()
        with redirect_stdout(out):
            self.assertEqual(pr.main(["--src", str(self.src), "--status", str(self.status), "--for", "4"]), 0)
        self.assertIn("must pay 1 prose promise", out.getvalue())
        self.assertIn("| Ch 3 §01 |", out.getvalue())
        with redirect_stdout(io.StringIO()):
            self.assertEqual(pr.main(["--src", str(self.src), "--status", str(self.status),
                                      "--reconcile"]), 1)


if __name__ == "__main__":
    unittest.main()
