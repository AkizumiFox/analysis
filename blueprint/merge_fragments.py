"""Assemble blueprint/book.yaml and blueprint/dag.json from the per-Part planning fragments.

    python blueprint/merge_fragments.py

The fragments (blueprint/fragments/part-<X>.yaml, one per Part, schema in
blueprint/fragments/BRIEF.md) were written independently, so this is where they meet:
chapters get global numbers in Part order, nodes that two Parts both drew on are merged,
and edges are pooled. After the first merge book.yaml is edited by hand and becomes the
source of truth; rerunning this overwrites it, so it refuses to unless --force is given.
"""
import argparse
import json
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
PART_ORDER = ["0", "I", "II", "III", "IV", "V", "VI"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    if (HERE / "book.yaml").exists() and not args.force:
        sys.exit("book.yaml exists and is edited by hand; pass --force to regenerate it")

    sources = yaml.safe_load((HERE / "sources.yaml").read_text())["books"]
    frags = {}
    for path in sorted((HERE / "fragments").glob("part-*.yaml")):
        frag = yaml.safe_load(path.read_text())
        frags[str(frag["part"])] = frag
    missing = [p for p in PART_ORDER if p not in frags]
    if missing:
        sys.exit(f"no fragment for Part(s) {missing}")

    nodes, hard, soft, alt = {}, [], [], []
    parts, chapters, cut, exemptions, external, gaps = [], [], {}, [], [], []
    slugs = set()
    for p in PART_ORDER:
        f = frags[p]
        parts.append({"num": p, "title": f["title"], "summary": f.get("summary", "")})
        for nid, n in (f.get("nodes") or {}).items():
            if nid in nodes:
                old = nodes[nid]
                old["pages"] = max(old.get("pages") or 0, n.get("pages") or 0)
                if n.get("files") and n.get("files") != old.get("files"):
                    old.setdefault("files_alt", []).append(n["files"])
            else:
                nodes[nid] = {"id": nid, **n}
        for kind, bucket in (("hard", hard), ("soft", soft), ("alt", alt)):
            for e in f.get(kind) or []:
                e = list(e)[:2] if kind != "alt" else list(e)  # an alt edge may carry a label
                if e not in bucket:
                    bucket.append(e)
        cut.update(f.get("cut") or {})
        exemptions += f.get("exemptions") or []
        external += [{**e, "part": p} for e in f.get("external") or []]
        gaps += [{"part": p, "gap": g} for g in f.get("coverage_gaps") or []]
        for ch in f["chapters"]:
            if ch["slug"] in slugs:
                sys.exit(f"duplicate chapter slug {ch['slug']}")
            slugs.add(ch["slug"])
            chapters.append({"num": len(chapters) + 1, "part": p, **ch})

    for e in hard + soft + alt:
        for n in e[:2]:
            if n not in nodes:
                print(f"warning: edge {e} names unknown node {n}")
    for ch in chapters:
        for s in ch.get("sources") or []:
            if s[0] not in nodes:
                print(f"warning: ch.{ch['num']} {ch['slug']} cites unknown node {s[0]}")

    books = {code: {"name": Path(v["dir"]).name, "role": v["role"]} for code, v in sources.items()}
    dag = {"books": books, "nodes": nodes, "hard": hard, "soft": soft, "alt": alt}
    (HERE / "dag.json").write_text(json.dumps(dag, indent=1, ensure_ascii=False) + "\n")

    book = {
        "title": "Analysis: From First Proofs to Modern Analysis",
        "cut": cut,
        "exemptions": exemptions,
        "external_prerequisites": external,
        "coverage_gaps": gaps,
        "parts": parts,
        "chapters": chapters,
    }
    header = ("# The analysis book -- single source of truth for the chapter plan.\n"
              "# First assembled from blueprint/fragments/ by merge_fragments.py; edited by hand since.\n"
              "# sources: [DAG node, sections]. Node ids refer to blueprint/dag.json (<BOOK>.<chapter>).\n\n")
    (HERE / "book.yaml").write_text(header + yaml.safe_dump(book, sort_keys=False, allow_unicode=True, width=110))
    print(f"{len(chapters)} chapters in {len(parts)} parts, {len(nodes)} nodes, "
          f"{len(hard)} hard / {len(soft)} soft / {len(alt)} alt edges, "
          f"{sum(c.get('pages') or 0 for c in chapters)} source pages")


if __name__ == "__main__":
    main()
