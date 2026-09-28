#!/usr/bin/env python3
"""Check the labels in hand-written chapter blueprints against the book and each other.

A blueprint expanded by hand (`authoring/blueprints/chNN.md` containing the line
`<!-- hand-written -->`) names the labels its chapter will create and the earlier
labels its proofs will cite. linear-algebra's blueprints were wrong about these
three to ten times per chapter (`authoring/design/research-production.md` §6), so
they are checked before drafting starts:

1. **every label it creates is unique book-wide**: not defined in `src/` outside
   this chapter's own directory, and not created by another hand-written blueprint;
2. **every label it cites exists**: defined somewhere in `src/`, or created earlier
   in the same blueprint;
3. **no main-line chapter cites an optional chapter's label** (`optional: true` in
   `blueprint/book.yaml`); an optional chapter may cite anything.

Creating versus citing. Labels are the backquoted ids (`` `thm-sup-unique` ``,
also `` `@thm-...` ``) with a book prefix (thm, lem, cor, prp, ax, def, exm, exr,
cnj, eq). A mention is a **citation** when it is written `@label`, or when its line
says so -- "cite", "cited", "from Chapter N", "Chapter N's", "recall", "reusing",
"point back", "(from ...)". Otherwise the label's first mention **creates** it, and
later mentions refer to it. The heuristic suits how the pilots' blueprints are
written; when it misreads a line, add a cite word to the line.

    .venv/bin/python blueprint/check_blueprint.py             # every hand-written blueprint
    .venv/bin/python blueprint/check_blueprint.py 8           # just Chapter 8's
    .venv/bin/python blueprint/check_blueprint.py --list 8    # what it creates and cites

Reads `blueprint/book.yaml` with PyYAML when available (the repo's .venv), else
with a small fallback reader for the `num:` and `optional:` keys. Exits 1 on any
problem. Importable: `mentions(text)`, `find_violations(blueprints, src_labels,
optional)`.
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KEEP = "<!-- hand-written -->"
PREFIXES = "thm|lem|cor|prp|ax|def|exm|exr|cnj|eq"
LABEL = re.compile(rf"`(@?)((?:{PREFIXES})-[A-Za-z0-9][\w-]*)`")
CITE_WORDS = re.compile(
    r"\bcit(?:e|es|ed|ing)\b|\bfrom Chapters? \d+|\bChapter \d+'s\b|\brecall(?:s|ed|ing)?\b"
    r"|\breus(?:e|es|ed|ing)\b|\bpoint(?:s|ing)? back\b|\(from\b", re.I)
DEF = re.compile(r"\{#([a-z]+-[\w-]+)")


def mentions(text: str):
    """(line number, label, 'create' | 'cite') for every label mention, in order."""
    out, seen = [], set()
    for n, line in enumerate(text.split("\n"), 1):
        citing_line = bool(CITE_WORDS.search(line))
        for m in LABEL.finditer(line):
            label = m.group(2)
            if m.group(1) or citing_line or label in seen:
                out.append((n, label, "cite"))
            else:
                out.append((n, label, "create"))
                seen.add(label)
    return out


def src_labels(src: Path) -> dict:
    """label -> list of (chapter number, file) where it is defined in src."""
    out = {}
    for f in sorted(Path(src).rglob("*.md")):
        m = re.match(r"ch(\d+)", f.parent.name)
        ch = int(m.group(1)) if m else None
        for label in DEF.findall(f.read_text(encoding="utf-8")):
            out.setdefault(label, []).append((ch, str(f)))
    return out


def optional_chapters(book_yaml: Path) -> set:
    text = Path(book_yaml).read_text(encoding="utf-8")
    try:
        import yaml
        book = yaml.safe_load(text)
        return {c["num"] for c in book.get("chapters", []) if c.get("optional")}
    except ImportError:
        pass
    out, num = set(), None
    for line in text.split("\n"):
        m = re.match(r"^- num:\s*(\d+)", line)
        if m:
            num = int(m.group(1))
        elif re.match(r"^  optional:\s*true\b", line) and num is not None:
            out.add(num)
    return out


def find_violations(blueprints: dict, labels: dict, optional: set, only=None) -> list:
    """Problems as (blueprint chapter, line, message).

    blueprints: {chapter: text} of the hand-written blueprints (all of them, so
    cross-blueprint duplicates are seen); labels: from `src_labels`; optional: set
    of optional chapter numbers; only: restrict reports to these chapters.
    """
    created = {ch: {} for ch in blueprints}          # ch -> label -> first line
    order = {ch: {} for ch in blueprints}            # ch -> label -> index of creating mention
    parsed = {ch: mentions(t) for ch, t in blueprints.items()}
    for ch, ms in parsed.items():
        for k, (n, label, how) in enumerate(ms):
            if how == "create" and label not in created[ch]:
                created[ch][label] = n
                order[ch][label] = k

    def owner(label):
        """Chapters that define or create a label."""
        chs = {c for c, _ in labels.get(label, []) if c is not None}
        chs |= {c for c, cr in created.items() if label in cr}
        return chs

    problems = []
    for ch in sorted(blueprints):
        if only and ch not in only:
            continue
        for label, n in created[ch].items():
            elsewhere = [f for c, f in labels.get(label, []) if c != ch]
            if elsewhere:
                problems.append((ch, n, f"creates {label}, already defined in {', '.join(elsewhere)}"))
            others = sorted(c for c, cr in created.items() if c != ch and label in cr)
            if others:
                problems.append((ch, n, f"creates {label}, also created by the blueprint of "
                                        f"{', '.join(f'Chapter {c}' for c in others)}"))
        for k, (n, label, how) in enumerate(parsed[ch]):
            if how != "cite":
                continue
            in_src = label in labels
            earlier = order[ch].get(label, 10 ** 9) < k
            if not in_src and not earlier:
                where = ("created later in this blueprint (line "
                         f"{created[ch][label]})") if label in created[ch] else "defined nowhere"
                problems.append((ch, n, f"cites {label}, which is {where}"))
            if ch not in optional:
                opt = sorted(c for c in owner(label) if c in optional and c != ch)
                if opt:
                    problems.append((ch, n, f"main-line chapter cites {label} from optional "
                                            f"Chapter {', '.join(map(str, opt))}"))
    return problems


def load_blueprints(bp_dir: Path) -> dict:
    out = {}
    for f in sorted(Path(bp_dir).glob("ch*.md")):
        text = f.read_text(encoding="utf-8")
        if KEEP in text:
            out[int(re.search(r"\d+", f.stem).group(0))] = text
    return out


def report(problems) -> str:
    return "\n".join(f"authoring/blueprints/ch{ch:02d}.md:{n}: {msg}" for ch, n, msg in problems)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Check label creation and citation in hand-written "
                                             "blueprints (unique, existing, no optional-chapter "
                                             "citations from the main line).")
    ap.add_argument("chapters", nargs="*", type=int, help="limit the report to these chapters")
    ap.add_argument("--list", action="store_true", help="list each blueprint's creates and cites")
    ap.add_argument("--src", default=str(ROOT / "src"))
    ap.add_argument("--blueprints", default=str(ROOT / "authoring" / "blueprints"))
    ap.add_argument("--book", default=str(ROOT / "blueprint" / "book.yaml"))
    args = ap.parse_args(argv)

    blueprints = load_blueprints(Path(args.blueprints))
    only = set(args.chapters) or None
    if args.list:
        for ch, text in sorted(blueprints.items()):
            if only and ch not in only:
                continue
            ms = mentions(text)
            creates = [l for _, l, h in ms if h == "create"]
            cites = sorted({l for _, l, h in ms if h == "cite"} - set(creates))
            print(f"Chapter {ch}: creates {len(creates)}: {', '.join(creates)}")
            print(f"Chapter {ch}: cites {len(cites)} from elsewhere: {', '.join(cites) or '-'}")
        return 0
    optional = optional_chapters(Path(args.book)) if Path(args.book).exists() else set()
    problems = find_violations(blueprints, src_labels(Path(args.src)), optional, only)
    if problems:
        print(report(problems))
    print(f"\n{len(blueprints)} hand-written blueprint(s) "
          f"({', '.join(map(str, sorted(blueprints))) or 'none'}): {len(problems)} problem(s).")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
