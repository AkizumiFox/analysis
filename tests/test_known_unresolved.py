"""The baseline of accepted unresolved references (config/known-unresolved.json).

References into sections that are planned but not yet written are listed with a reason,
so `check` fails only on new unresolved references; see build/check.py known_unresolved.
"""

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from build.check import KNOWN_UNRESOLVED, known_unresolved  # noqa: E402


class _Book:
    def __init__(self, root):
        self.root = root


class KnownUnresolved(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)
        (self.root / "config").mkdir()

    def write(self, data):
        text = data if isinstance(data, str) else json.dumps(data)
        (self.root / KNOWN_UNRESOLVED).write_text(text, encoding="utf-8")
        return known_unresolved(_Book(self.root))

    def test_no_file_accepts_nothing(self):
        self.assertEqual(known_unresolved(_Book(self.root)), ({}, []))

    def test_entries_are_keyed_by_reference_and_source(self):
        known, problems = self.write([{"why": "section 03 not written", "references": [
            {"ref": "thm-a", "in": "src/ch04/07.md"}, {"ref": "@thm-b", "in": "src/ch04/08.md"}]}])
        self.assertEqual(problems, [])
        self.assertEqual(set(known), {("thm-a", "src/ch04/07.md"), ("thm-b", "src/ch04/08.md")})

    def test_a_group_needs_a_reason(self):
        _, problems = self.write([{"references": [{"ref": "thm-a", "in": "src/x.md"}]}])
        self.assertIn("has no `why`", problems[0])

    def test_bad_json_is_reported(self):
        _, problems = self.write("[{")
        self.assertIn("not valid JSON", problems[0])


if __name__ == "__main__":
    unittest.main()
