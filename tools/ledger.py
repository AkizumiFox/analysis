#!/usr/bin/env python3
"""The claim ledger: one entry per reviewable item, with verdicts that know when they go stale.

`authoring/design/research-production.md` §5.2 routes every referee finding to a
ledger, `authoring/ledger/chNN.yaml`. An entry is one thing a referee can pass or
fail: a labelled result (`thm`, `lem`, `cor`, `prp`, `ax`, `cnj`), a definition
(`def`), an example or exercise (`exm`, `exr`, hashed together with the solution
that follows it), a Quick check (with its solution), or a proof. Each entry carries
a **content hash** of its source text, and each verdict records the hash it was
given against -- so when the text changes, the verdict is known to be stale instead
of silently still counting.

Keys: a labelled block is its label (`thm-sup-unique`); a proof is `proof:<label>`
of the labelled block before it (`proof:thm-sup-unique`, then `#2`, ... if a
result has more than one); a check is `check:<section file stem>:<n>`. Proofs
nested in a claim or proof are part of the enclosing proof's text.

Needs PyYAML, which lives in the repo's virtualenv: run it as

    .venv/bin/python tools/ledger.py init 8
    .venv/bin/python tools/ledger.py set 8 thm-sup-unique --stage S5a --verdict correct --by refA
    .venv/bin/python tools/ledger.py set 8 proof:thm-sup-sum --stage S5a --verdict gap \\
        --by refA --evidence "04:190 uses sup A + sup B - eps without eps/2 split"
    .venv/bin/python tools/ledger.py stale 8       # verdicts whose text has changed since
    .venv/bin/python tools/ledger.py summary       # every ledger, one line each

Hashes are taken after `usage_forms.normalize`, which rewrites the English usage
forms the series is migrating away from (`non-empty`, `iff`, a missing serial
comma, a kept heading anchor `{#id}`, ...) to their preferred forms, so a usage-only
edit leaves a verdict current while a mathematical edit still stales it. Verdicts
recorded before normalization carry the raw hash; `ledger.py rehash [ch]` moves
every verdict whose hash is the raw hash of its item's current text to the new
hash, and leaves any other mismatch stale. (Adding a rule to usage_forms.py
changes the hash of the items containing that form; their verdicts go stale.)

`init` is also a refresh: on an existing ledger it keeps every verdict, updates
hashes and files, adds new items, and keeps (marked `removed`) any item that has
verdicts but is gone from the source. A non-`correct` verdict must carry
`--evidence` (file:line, a counterexample or a computation). `stale` exits 1 if
anything is stale.

Importable (no YAML needed for these): `extract_items(chapter_dir)`,
`refresh(ledger, items)`, `stale_items(ledger, items)`, `rehash(ledger, items)`.
"""
import argparse
import datetime
import hashlib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mdblocks  # noqa: E402
import usage_forms  # noqa: E402

SRC = Path("src")
LEDGER_DIR = Path("authoring/ledger")
RESULT_KINDS = ("thm", "lem", "cor", "prp", "ax", "cnj", "def", "exm", "exr")
VERDICTS = ("correct", "minor", "gap", "error")


def _raw_hash(text: str) -> str:
    """The hash before usage normalization. Used only by `rehash`, to carry verdicts over."""
    norm = "\n".join(line.rstrip() for line in text.strip().split("\n"))
    norm = re.sub(r"\n{2,}", "\n\n", norm)
    return hashlib.sha256(norm.encode("utf-8")).hexdigest()[:12]


def content_hash(text: str) -> str:
    return _raw_hash(usage_forms.normalize(text))


def _block_text(doc, div, with_solution=False):
    end = div.end
    if with_solution:
        nxt = mdblocks.following_div(doc, div)
        if nxt is not None and nxt.has("solution"):
            end = nxt.end
    return "\n".join(doc.lines[div.start:end + 1])


def extract_items(chapter_dir: Path) -> list:
    """Every ledger item in one chapter directory, in book order.

    Returns dicts {key, kind, file, line, hash, raw_hash}; `raw_hash` is the hash
    without usage normalization, for `rehash`.
    """
    items, seen = [], {}
    for f in sorted(Path(chapter_dir).glob("*.md")):
        doc = mdblocks.parse(f.read_text(encoding="utf-8"))
        owner = None
        n_check = 0
        for div in doc.divs:
            nested = div.parent is not None and (div.parent.has("proof") or div.parent.has("claim")
                                                 or div.parent.has("solution"))
            if div.id and div.kind in RESULT_KINDS:
                owner = div.id
                key, kind = div.id, div.kind
                text = _block_text(doc, div, with_solution=kind in ("exm", "exr"))
            elif div.has("check"):
                n_check += 1
                key, kind = f"check:{f.stem}:{n_check}", "check"
                text = _block_text(doc, div, with_solution=True)
            elif div.has("proof") and not nested:
                key, kind = f"proof:{owner or f.stem}", "proof"
                text = _block_text(doc, div)
            else:
                continue
            if key in seen:
                seen[key] += 1
                key = f"{key}#{seen[key]}"
            else:
                seen[key] = 1
            items.append({"key": key, "kind": kind, "file": f.name,
                          "line": div.start + 1, "hash": content_hash(text),
                          "raw_hash": _raw_hash(text)})
    return items


def refresh(ledger: dict, items: list) -> tuple:
    """Merge freshly extracted items into a ledger. Returns (ledger, added, removed)."""
    old = {it["key"]: it for it in ledger.get("items", [])}
    new_items, added = [], []
    for it in items:
        entry = dict(old.get(it["key"], {}))
        if not entry:
            added.append(it["key"])
        entry.update({"key": it["key"], "kind": it["kind"], "file": it["file"],
                      "line": it["line"], "hash": it["hash"]})
        entry.pop("removed", None)
        entry.setdefault("verdicts", [])
        new_items.append(entry)
    current = {it["key"] for it in items}
    removed = []
    for key, entry in old.items():
        if key not in current:
            removed.append(key)
            if entry.get("verdicts"):
                entry["removed"] = True
                new_items.append(entry)
    ledger["items"] = new_items
    return ledger, added, removed


def stale_items(ledger: dict, items: list) -> list:
    """(key, reason) for every item whose latest verdict no longer matches the source."""
    current = {it["key"]: it["hash"] for it in items}
    out = []
    for entry in ledger.get("items", []):
        verdicts = entry.get("verdicts") or []
        if not verdicts:
            continue
        last = verdicts[-1]
        if entry["key"] not in current:
            out.append((entry["key"], "no longer in the source"))
        elif last.get("hash") != current[entry["key"]]:
            out.append((entry["key"], f"{last.get('stage')} verdict '{last.get('verdict')}' "
                                      f"by {last.get('by')} was on {last.get('hash')}, "
                                      f"text is now {current[entry['key']]}"))
    return out


def rehash(ledger: dict, items: list) -> int:
    """Carry verdicts over to the normalized hash. A verdict whose recorded hash is the raw
    (unnormalized) hash of its item's current text was current before normalization, so it is
    rewritten to the new hash; any other hash is left as it is (stale stays stale). The entry's own
    `hash` is updated the same way. Returns the number of verdicts rewritten."""
    current = {it["key"]: it for it in items}
    n = 0
    for entry in ledger.get("items", []):
        it = current.get(entry["key"])
        if it is None or it["raw_hash"] == it["hash"]:
            continue
        if entry.get("hash") == it["raw_hash"]:
            entry["hash"] = it["hash"]
        for v in entry.get("verdicts") or []:
            if v.get("hash") == it["raw_hash"]:
                v["hash"] = it["hash"]
                n += 1
    return n


def add_verdict(ledger: dict, items: list, key: str, stage: str, verdict: str, by: str,
                evidence: str = "", model: str = "", today: str | None = None) -> dict:
    if verdict not in VERDICTS:
        raise ValueError(f"verdict must be one of {', '.join(VERDICTS)}")
    if verdict != "correct" and not evidence:
        raise ValueError(f"a '{verdict}' verdict needs --evidence")
    current = {it["key"]: it["hash"] for it in items}
    if key not in current:
        raise KeyError(f"{key} is not an item of this chapter (run `init` to refresh)")
    entry = next((e for e in ledger["items"] if e["key"] == key), None)
    if entry is None:
        raise KeyError(f"{key} is not in the ledger yet (run `init` to refresh)")
    v = {"stage": stage, "verdict": verdict, "by": by, "hash": current[key],
         "date": today or datetime.date.today().isoformat()}
    if model:
        v["model"] = model
    if evidence:
        v["evidence"] = evidence
    entry.setdefault("verdicts", []).append(v)
    return v


def summarize(ledger: dict, items: list) -> dict:
    counts = {v: 0 for v in VERDICTS}
    reviewed = 0
    for e in ledger.get("items", []):
        if e.get("removed"):
            continue
        if e.get("verdicts"):
            reviewed += 1
            counts[e["verdicts"][-1]["verdict"]] += 1
    return {"items": len(items), "reviewed": reviewed, **counts,
            "stale": len(stale_items(ledger, items))}


# ---------------------------------------------------------------------------
# Files
# ---------------------------------------------------------------------------

def _yaml():
    try:
        import yaml
    except ImportError:
        sys.exit("ledger.py needs PyYAML: run it with .venv/bin/python")
    return yaml


def chapter_dir(src: Path, ch: int) -> Path:
    found = sorted(Path(src).glob(f"ch{ch:02d}-*"))
    if not found:
        sys.exit(f"no chapter directory ch{ch:02d}-* under {src}")
    return found[0]


def ledger_path(ledger_dir: Path, ch: int) -> Path:
    return Path(ledger_dir) / f"ch{ch:02d}.yaml"


def load(path: Path) -> dict:
    if not path.exists():
        return {}
    return _yaml().safe_load(path.read_text(encoding="utf-8")) or {}


def save(path: Path, ledger: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(_yaml().safe_dump(ledger, sort_keys=False, allow_unicode=True, width=100),
                    encoding="utf-8")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="The claim ledger: items with content hashes and "
                                             "referee verdicts (authoring/ledger/chNN.yaml). "
                                             "Needs PyYAML: use .venv/bin/python.")
    ap.add_argument("--src", default=str(SRC), help="source directory (default: src)")
    ap.add_argument("--dir", default=str(LEDGER_DIR), help="ledger directory (default: authoring/ledger)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("init", help="create or refresh a chapter's ledger")
    p.add_argument("ch", type=int)
    p = sub.add_parser("set", help="record a verdict on one item")
    p.add_argument("ch", type=int)
    p.add_argument("label", help="item key: a label, proof:<label> or check:<stem>:<n>")
    p.add_argument("--stage", required=True, help="pipeline stage, e.g. S5a, S6")
    p.add_argument("--verdict", required=True, choices=VERDICTS)
    p.add_argument("--by", required=True, help="reviewer name")
    p.add_argument("--evidence", default="", help="file:line, counterexample or computation")
    p.add_argument("--model", default="", help="model that produced the verdict")
    p = sub.add_parser("rehash", help="carry verdicts that were current over to the "
                                      "usage-normalized hash (every ledger, or one chapter)")
    p.add_argument("ch", type=int, nargs="?")
    p = sub.add_parser("stale", help="verdicts whose item text has changed; exit 1 if any")
    p.add_argument("ch", type=int)
    sub.add_parser("summary", help="one line per ledger")
    p = sub.add_parser("list", help="every item of a chapter with its latest verdict")
    p.add_argument("ch", type=int)
    args = ap.parse_args(argv)

    src, ldir = Path(args.src), Path(args.dir)
    if args.cmd == "summary":
        paths = sorted(ldir.glob("ch*.yaml"))
        if not paths:
            print(f"no ledgers in {ldir}")
        for path in paths:
            ch = int(re.search(r"\d+", path.stem).group(0))
            s = summarize(load(path), extract_items(chapter_dir(src, ch)))
            print(f"ch{ch:02d}: {s['items']} items, {s['reviewed']} reviewed "
                  f"(correct {s['correct']}, minor {s['minor']}, gap {s['gap']}, "
                  f"error {s['error']}), {s['stale']} stale")
        return 0

    if args.cmd == "rehash":
        paths = ([ledger_path(ldir, args.ch)] if args.ch is not None
                 else sorted(ldir.glob("ch*.yaml")))
        for path in paths:
            ledger = load(path)
            if not ledger:
                print(f"{path}: no ledger, skipped")
                continue
            ch = ledger.get("chapter") or int(re.search(r"\d+", path.stem).group(0))
            found = ([Path(src) / ledger["dir"]] if ledger.get("dir")
                     else sorted(Path(src).glob(f"ch{ch:02d}-*")))
            cdir = found[0] if found else Path(src) / f"ch{ch:02d}-*"
            if not cdir.is_dir():   # skip, not chapter_dir's exit: the other ledgers still run
                print(f"{path}: chapter directory {cdir} not found, skipped")
                continue
            before = repr(ledger)
            n = rehash(ledger, extract_items(cdir))
            if repr(ledger) != before:      # also an entry's own hash, with no verdict moved
                save(path, ledger)
            print(f"{path}: {n} verdict(s) rehashed")
        return 0

    items = extract_items(chapter_dir(src, args.ch))
    path = ledger_path(ldir, args.ch)
    ledger = load(path)
    if args.cmd == "init":
        existed = bool(ledger)
        ledger.setdefault("chapter", args.ch)
        ledger["dir"] = chapter_dir(src, args.ch).name
        ledger, added, removed = refresh(ledger, items)
        save(path, ledger)
        print(f"{'refreshed' if existed else 'wrote'} {path}: {len(items)} items"
              f" ({len(added)} new, {len(removed)} gone)")
        return 0
    if not ledger:
        sys.exit(f"{path} does not exist; run `init {args.ch}` first")
    if args.cmd == "set":
        try:
            add_verdict(ledger, items, args.label, args.stage, args.verdict, args.by,
                        args.evidence, args.model)
        except (KeyError, ValueError) as e:
            sys.exit(str(e).strip("'\""))
        save(path, ledger)
        print(f"{args.label}: {args.verdict} ({args.stage}, {args.by})")
        return 0
    if args.cmd == "stale":
        stale = stale_items(ledger, items)
        for key, why in stale:
            print(f"{key}: {why}")
        print(f"{len(stale)} stale verdict(s) in {path}.")
        return 1 if stale else 0
    if args.cmd == "list":
        cur = {it["key"]: it for it in items}
        for e in ledger["items"]:
            last = (e.get("verdicts") or [{}])[-1]
            mark = "" if not last else f"{last['verdict']} ({last['stage']})"
            if last and cur.get(e["key"], {}).get("hash") != last.get("hash"):
                mark += " STALE"
            print(f"{e['file']}:{e['line']}: {e['key']} [{e['kind']}] {mark}")
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
