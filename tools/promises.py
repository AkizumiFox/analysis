#!/usr/bin/env python3
"""Find the book's forward promises and reconcile them with authoring/STATUS.md.

A forward promise is a prose pointer to a later part of the book with no `@ref`
behind it: "Chapter 9 turns this into the definition of a limit", "Section 1.5
separates the two", "the rules of §04". STYLE §7 says every one must be paid off
and recorded in STATUS.md's "Forward promises" table; this tool finds them so the
table can be checked rather than remembered.

What counts:

* `Chapter N`, `Chapters N–M` (each chapter in the range), `Chapters N and M`,
  `Section N.M` (chapter N, section M), and `§NN` / `§NN–§MM` (a section of the
  *current* chapter);
* only pointers **forward** of the file they are in: a later chapter, or a later
  section of the same chapter; a pointer back is a recall, not a promise;
* not the linear-algebra companion's chapters ("the linear-algebra companion,
  Chapter 0"), and not math, code or raw LaTeX;
* a pointer whose sentence also carries an `@ref` to a label defined in the target
  chapter counts as linked, not as a promise.

    python3 tools/promises.py                 # every promise, grouped by target chapter
    python3 tools/promises.py --for 2         # what Chapter 2 must pay, with STATUS rows
    python3 tools/promises.py --reconcile     # promises with no STATUS row; exit 1 if any

Importable:

    from tools.promises import find_promises, parse_status, reconcile
"""
import argparse
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mdblocks  # noqa: E402

SRC = Path("src")
STATUS = Path("authoring/STATUS.md")

DASH = r"\s*(?:–|—|-|to)\s*"
CHAPTERS = re.compile(
    rf"\bChapters?\s+(\d+)((?:(?:{DASH}|\s*,\s*|\s+and\s+|\s+or\s+)\d+)*)")
SECTION = re.compile(r"\bSections?\s+(\d+)\.(\d+)")
PARA = re.compile(rf"§\s*(\d+)(?:{DASH}§?\s*(\d+))?")
LABEL_DEF = re.compile(r"\{#([a-z]+-[\w-]+)")
REF = re.compile(r"@([a-z]+-[\w-]+)")


@dataclass(frozen=True)
class Promise:
    file: str          # e.g. ch11-least-upper-bound/03-the-axiom.md
    line: int
    chapter: int       # chapter the pointer is written in
    section: str       # "03", or "index"
    target: int        # target chapter
    target_section: int | None
    text: str          # the pointer as written, with a little context


def chapter_of(dirname: str):
    m = re.match(r"ch(\d+)", dirname)
    return int(m.group(1)) if m else None


def section_of(path: Path) -> str:
    m = re.match(r"(\d+)", path.name)
    return m.group(1) if m else "index"


def expand(first: str, rest: str) -> list:
    nums = [int(first)]
    for m in re.finditer(rf"({DASH}|\s*,\s*|\s+and\s+|\s+or\s+)(\d+)", rest):
        n = int(m.group(2))
        if re.fullmatch(DASH, m.group(1)) and n > nums[-1]:
            nums += list(range(nums[-1] + 1, n + 1))
        else:
            nums.append(n)
    return nums


def prose_lines(text: str):
    """(lineno, line) for prose lines, with math and code blanked out."""
    doc = mdblocks.parse(text)
    joined = "\n".join("" if code else ln for ln, code in zip(doc.lines, doc.in_code))
    joined = re.sub(r"\\\[.*?\\\]", lambda m: "\n" * m.group(0).count("\n"), joined, flags=re.S)
    joined = re.sub(r"\\\(.*?\\\)", lambda m: " " + "\n" * m.group(0).count("\n"), joined, flags=re.S)
    joined = re.sub(r"`[^`\n]*`", " ", joined)
    return list(enumerate(joined.split("\n"), 1))


def sentence_around(line: str, pos: int) -> str:
    start = max(line.rfind(". ", 0, pos), line.rfind("; ", 0, pos))
    end_candidates = [i for i in (line.find(". ", pos), line.find("; ", pos)) if i >= 0]
    end = min(end_candidates) if end_candidates else len(line)
    return line[start + 1 if start >= 0 else 0:end + 1]


def labels_by_chapter(src: Path) -> dict:
    out = defaultdict(set)
    for f in src.rglob("*.md"):
        ch = chapter_of(f.parent.name)
        if ch is not None:
            out[ch] |= set(LABEL_DEF.findall(f.read_text(encoding="utf-8")))
    return out


def find_promises(src: Path = SRC) -> list:
    src = Path(src)
    labels = labels_by_chapter(src)
    promises = []
    for f in sorted(src.rglob("*.md")):
        ch = chapter_of(f.parent.name)
        if ch is None:
            continue
        sec = section_of(f)
        rel = f"{f.parent.name}/{f.name}"
        for lineno, line in prose_lines(f.read_text(encoding="utf-8")):
            hits = []
            for m in CHAPTERS.finditer(line):
                if "companion" in line[max(0, m.start() - 40):m.start()]:
                    continue
                for n in expand(m.group(1), m.group(2) or ""):
                    hits.append((m, n, None))
            for m in SECTION.finditer(line):
                hits.append((m, int(m.group(1)), int(m.group(2))))
            for m in PARA.finditer(line):
                lo = int(m.group(1))
                hi = int(m.group(2)) if m.group(2) else lo
                for s in range(lo, hi + 1):
                    hits.append((m, ch, s))
            seen = set()
            for m, target, tsec in hits:
                cur = int(sec) if sec.isdigit() else 0
                forward = target > ch or (target == ch and tsec is not None and tsec > cur)
                if not forward or (target, tsec) in seen:
                    continue
                seen.add((target, tsec))
                sentence = sentence_around(line, m.start())
                if any(r in labels.get(target, ()) for r in REF.findall(sentence)):
                    continue
                context = line[max(0, m.start() - 50):m.end() + 50].strip()
                promises.append(Promise(rel, lineno, ch, sec, target, tsec, context))
    return promises


# ---------------------------------------------------------------------------
# STATUS.md
# ---------------------------------------------------------------------------

@dataclass
class Row:
    line: int
    source: str
    chapter: int | None
    sections: set          # {"01", "index", ...}; empty = whole chapter
    promise: str
    targets: set
    paid: bool


def parse_status(path: Path = STATUS) -> list:
    rows = []
    text = Path(path).read_text(encoding="utf-8")
    in_table = False
    for n, line in enumerate(text.split("\n"), 1):
        if line.startswith("## "):
            in_table = line.strip() == "## Forward promises"
            continue
        if not in_table or not line.startswith("|") or set(line) <= set("|-: "):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3 or cells[0] == "From":
            continue
        frm, promise, target = cells[0], cells[1], cells[2]
        m = re.match(r"Ch\s*(\d+)", frm)
        sections = set(re.findall(r"§(\d+)", frm))
        if re.search(r"\bindex\b", frm):
            sections.add("index")
        rows.append(Row(n, line, int(m.group(1)) if m else None, sections, promise,
                        {int(x) for x in re.findall(r"Ch\s*(\d+)", target)},
                        "paid" in target.lower()))
    return rows


def existing_sections(src: Path = SRC) -> set:
    """{(chapter, section number)} for every section file in src."""
    out = set()
    for f in Path(src).rglob("*.md"):
        ch, sec = chapter_of(f.parent.name), section_of(f)
        if ch is not None and sec.isdigit():
            out.add((ch, int(sec)))
    return out


def reconcile(promises: list, rows: list, sections: set = frozenset()):
    """Promises with no STATUS row: (promise, reason) pairs.

    A row covers a promise when it has the same source chapter and target chapter,
    and lists the promise's section (or lists no section at all). A pointer to a
    later section of the *same* chapter needs no row: it is paid when that section
    exists (`sections`, from `existing_sections`), and reported when it does not.
    """
    missing = []
    for p in promises:
        if p.target == p.chapter:
            if (p.target, p.target_section) not in sections:
                missing.append((p, f"points at §{p.target_section:02d}, which does not exist"))
            continue
        candidates = [r for r in rows if r.chapter == p.chapter and p.target in r.targets]
        if not candidates:
            missing.append((p, f"no row Ch {p.chapter} → Ch {p.target}"))
        elif not any(not r.sections or p.section in r.sections for r in candidates):
            missing.append((p, f"row(s) Ch {p.chapter} → Ch {p.target} exist but do not list "
                               f"{'§' + p.section if p.section != 'index' else 'index'}"))
    return missing


def fmt(p: Promise) -> str:
    tgt = f"Ch {p.target}" + (f" §{p.target_section:02d}" if p.target_section else "")
    return f"{p.file}:{p.line}: → {tgt}: …{p.text}…"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="List forward promises (prose pointers without "
                                             "@ref) and reconcile them with STATUS.md.")
    ap.add_argument("--src", default=str(SRC), help="source directory (default: src)")
    ap.add_argument("--status", default=str(STATUS), help="STATUS.md path")
    ap.add_argument("--for", dest="target", type=int, metavar="N",
                    help="list only the promises chapter N must pay")
    ap.add_argument("--reconcile", action="store_true",
                    help="list promises with no STATUS row; exit 1 if any")
    args = ap.parse_args(argv)

    promises = find_promises(Path(args.src))
    rows = parse_status(Path(args.status)) if Path(args.status).exists() else []

    if args.target is not None:
        mine = [p for p in promises if p.target == args.target]
        print(f"Chapter {args.target} must pay {len(mine)} prose promise(s):")
        for p in mine:
            print("  " + fmt(p))
        status_rows = [r for r in rows if args.target in r.targets]
        print(f"\nSTATUS.md rows targeting Chapter {args.target}: {len(status_rows)}")
        for r in status_rows:
            print(f"  {'[paid] ' if r.paid else ''}{r.source}")
        return 0

    if args.reconcile:
        missing = reconcile(promises, rows, existing_sections(Path(args.src)))
        for p, why in missing:
            print(f"{fmt(p)}\n    {why}")
        print(f"\n{len(promises)} promise(s) in the prose, {len(rows)} STATUS row(s), "
              f"{len(missing)} promise(s) not recorded.")
        return 1 if missing else 0

    by_target = defaultdict(list)
    for p in promises:
        by_target[p.target].append(p)
    for t in sorted(by_target):
        print(f"Chapter {t} ({len(by_target[t])}):")
        for p in by_target[t]:
            print("  " + fmt(p))
    print(f"\n{len(promises)} forward promise(s) to {len(by_target)} chapter(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
