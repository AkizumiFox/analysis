"""Write authoring/blueprints/chNN.md for every chapter from blueprint/book.yaml.

A blueprint is the brief a writer (or drafting agent) starts from: the chapter's place in
the book, its planned sections, what it must prove, its key examples and exit checks, the
source sections its coverage is checked against, its page budget and its prerequisites
from the DAG. Written chapters keep their blueprint as a record. Regenerate after editing
book.yaml. A chapter whose blueprint was expanded by hand (it contains the line
"<!-- hand-written -->") is left alone.
"""
import json
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
KEEP = "<!-- hand-written -->"


def prerequisites(book, dag):
    cut = book.get("cut", {})
    uses = defaultdict(set)
    for ch in book["chapters"]:
        for node, _ in ch["sources"]:
            uses[node].add(ch["num"])
    first = {n: min(c) for n, c in uses.items()}
    req = defaultdict(set)
    for a, b in dag["hard"]:
        a, b = cut.get(a, a), cut.get(b, b)
        if a is None or b is None or a not in first:
            continue
        for c in uses.get(b, ()):
            if first[a] < c:
                req[c].add(first[a])
    return req


def bullets(title, items):
    return [f"## {title}", ""] + [f"- {x}" for x in items] + [""] if items else []


def main():
    book = yaml.safe_load((ROOT / "blueprint/book.yaml").read_text())
    dag = json.loads((ROOT / "blueprint/dag.json").read_text())
    written = {int(p.name[2:4]) for p in (ROOT / "src").glob("ch[0-9][0-9]-*") if p.is_dir()}
    req = prerequisites(book, dag)
    parts = {str(p["num"]): p for p in book["parts"]}
    titles = {c["num"]: c["title"] for c in book["chapters"]}
    out = ROOT / "authoring" / "blueprints"
    out.mkdir(parents=True, exist_ok=True)
    kept = 0
    for ch in book["chapters"]:
        path = out / f"ch{ch['num']:02d}.md"
        if path.exists() and KEEP in path.read_text():
            kept += 1
            continue
        part = parts[str(ch["part"])]
        lines = [f"# Chapter {ch['num']}: {ch['title']}", "",
                 f"Directory: `src/ch{ch['num']:02d}-{ch['slug']}/`. "
                 f"State: {'written' if ch['num'] in written else 'not started'}.", "",
                 f"**Part {part['num']}, {part['title']}.** {part.get('summary', '')}", ""]
        if ch.get("optional"):
            lines += ["**Optional chapter.** It sits beside the main line: mark its results `.optional`; "
                      "no main-line proof may cite them (`tools/check_optional.py`).", ""]
        if ch.get("note"):
            lines += [f"*{ch['note']}*", ""]
        lines += [f"**Page budget:** about {ch.get('pages', '?')} source-book pages.", ""]
        optional = {c["num"] for c in book["chapters"] if c.get("optional")}
        # A main-line chapter never rests on an optional one: an edge that says so comes from a
        # reference book's own order, which the optional route re-arranges (check_order reports it).
        pre = sorted(p for p in req.get(ch["num"], []) if ch.get("optional") or p not in optional)
        lines += ["**Prerequisites (from the DAG):** "
                  + (", ".join(f"Chapter {p} ({titles[p]})" for p in pre) or "none") + ".", ""]
        ext = [e["needs"] for e in book.get("external_prerequisites", []) if e.get("for_chapter") == ch["slug"]]
        if ext:
            lines += ["**Needs from other Parts:**", ""] + [f"- {x}" for x in ext] + [""]
        lines += ["## Planned sections", ""] + [f"{i}. {s}" for i, s in enumerate(ch["outline"], 1)] + [""]
        lines += bullets("Must prove", ch.get("must_prove"))
        lines += bullets("Key examples and counterexamples", ch.get("key_examples"))
        lines += bullets("Exit checks (C-exercises)", ch.get("exit_checks"))
        if ch.get("sources"):
            lines += ["## Coverage is checked against", ""]
            for node, secs in ch["sources"]:
                n = dag["nodes"][node]
                name = dag["books"][n["book"]]["name"]
                where = "" if secs == "all" else f", {secs}"
                lines.append(f"- {name}, ch. {n['ch']} ({n['title']}){where} [`{node}`]")
            lines.append("")
        path.write_text("\n".join(lines))
    print(f"wrote {len(book['chapters']) - kept} blueprints, kept {kept} hand-written "
          f"({len(written)} chapters written)")


if __name__ == "__main__":
    main()
