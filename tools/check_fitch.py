#!/usr/bin/env python3
"""Check every Fitch derivation and every truth table in the book's source.

Part 0 prints derivations as fitch.sty `nd` environments inside raw LaTeX blocks
(syntax in `latex/fitch-book.sty`, conventions in `authoring/NOTATION.md`):

    \\hypo {1} {P \\to Q}
    \\open
    \\hypo {2} {P}
    \\have {3} {Q}  \\ie{1,2}
    \\close
    \\have {4} {P \\to Q} \\ii{2-3}

A derivation is mechanical, so it is checked mechanically. For each `nd` block:

* **labels** are unique and number the lines 1, 2, 3, ... in order;
* **boxes** balance, and each box begins with an assumption (`\\hypo`); an
  assumption in the middle of a box is an error;
* **cited lines exist and are available**: earlier, and not inside a box that has
  closed (NOTATION.md: "a line may cite any earlier line not inside a closed box");
* **cited ranges** (`i-j`, for ->I, not-I, RAA, or-E, iff-I) are exactly a closed
  box, first line its assumption and last line its last line, whose enclosing box
  is still open;
* **rule shapes** for the propositional rules (and-I/E, ->I/E, or-I/E, not-I/E,
  bot-E, RAA, iff-I/E, R), at the level of formulas, with a small parser for
  letters (any capital), `\\neg \\wedge \\vee \\to \\leftrightarrow \\bot` and
  parentheses.

Skipped, with a note (shown by `--notes`): a schematic block (non-numeric labels
such as i, j, k), a `\\vdots` row and a justification-free line after it, a
`\\by{text}{refs}` justification (its refs are still checked for availability), a
quantifier or equality rule, and any formula the parser cannot read.

A deliberately flawed derivation -- a non-example, a "find the error" exercise --
carries `% expect-invalid` on a line of its raw LaTeX block before `\\begin{nd}`
(or on the line just before the block). Its errors are then expected: they are not
reported, and the block is an error only if it checks *clean*.

**Truth tables.** A display `array` whose header row is statement letters and
formulas, and whose rows below `\\hline` are T/F (`\\mathrm{T}`, `\\text{F}`, `T`),
is evaluated: every formula column must agree with the letter columns in every
row. Columns the parser cannot read are skipped with a note.

    python3 tools/check_fitch.py                        # all of src/
    python3 tools/check_fitch.py src/ch01-logic-connectives
    python3 tools/check_fitch.py --notes                # also list what was skipped

Exits 1 on any error. Importable:

    from tools.check_fitch import find_violations, report
    errors, notes = find_violations(Path("src"))
"""
import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

# ---------------------------------------------------------------------------
# Formulas
# ---------------------------------------------------------------------------

BOT = ("bot",)
OPS = {  # token -> (kind, precedence, right-associative)
    "iff": (1, True), "imp": (2, True), "or": (3, False), "and": (4, False),
}
MACROS = {
    r"\neg": "not", r"\lnot": "not", r"\wedge": "and", r"\land": "and",
    r"\vee": "or", r"\lor": "or", r"\to": "imp", r"\rightarrow": "imp",
    r"\leftrightarrow": "iff", r"\iff": "iff", r"\bot": "bot",
}
SPACING = re.compile(r"\\[,;:! ]|\\q?quad(?![A-Za-z])|\\(?:left|right|mathrm|mathit)(?![A-Za-z])")


class ParseError(ValueError):
    pass


def tokenize(text: str) -> list:
    s = SPACING.sub(" ", text)
    s = re.sub(r"\{(\\[A-Za-z]+)\}", r" \1 ", s)   # {\to} -> \to
    tokens = []
    i = 0
    while i < len(s):
        c = s[i]
        if c.isspace():
            i += 1
        elif c in "({":
            tokens.append("(")
            i += 1
        elif c in ")}":
            tokens.append(")")
            i += 1
        elif c == "\\":
            m = re.match(r"\\[A-Za-z]+", s[i:])
            if not m or m.group(0) not in MACROS:
                raise ParseError(f"unknown command {m.group(0) if m else s[i:i+2]}")
            tokens.append(MACROS[m.group(0)])
            i += len(m.group(0))
        elif c.isupper() and c.isalpha():
            if i + 1 < len(s) and (s[i + 1].isalnum() or s[i + 1] in "_^'"):
                raise ParseError(f"not a statement letter near {s[i:i+3]!r}")
            tokens.append(("var", c))
            i += 1
        else:
            raise ParseError(f"unexpected {c!r}")
    return tokens


def parse_formula(text: str):
    """Parse a propositional formula into a tuple tree; raise ParseError."""
    tokens = tokenize(text)
    if not tokens:
        raise ParseError("empty formula")
    pos = 0

    def peek():
        return tokens[pos] if pos < len(tokens) else None

    def unary():
        nonlocal pos
        t = peek()
        if t == "not":
            pos += 1
            return ("not", unary())
        if t == "bot":
            pos += 1
            return BOT
        if isinstance(t, tuple):
            pos += 1
            return t
        if t == "(":
            pos += 1
            inner = binary(0)
            if peek() != ")":
                raise ParseError("unbalanced parentheses")
            pos += 1
            return inner
        raise ParseError(f"unexpected {t!r}")

    def binary(min_prec):
        nonlocal pos
        left = unary()
        while isinstance(peek(), str) and peek() in OPS and OPS[peek()][0] >= min_prec:
            op = peek()
            prec, right_assoc = OPS[op]
            pos += 1
            right = binary(prec if right_assoc else prec + 1)
            left = (op, left, right)
        return left

    tree = binary(0)
    if pos != len(tokens):
        raise ParseError(f"trailing {tokens[pos]!r}")
    return tree


def evaluate(f, env: dict) -> bool:
    k = f[0]
    if k == "var":
        return env[f[1]]
    if k == "bot":
        return False
    if k == "not":
        return not evaluate(f[1], env)
    a, b = evaluate(f[1], env), evaluate(f[2], env)
    return {"and": a and b, "or": a or b, "imp": (not a) or b, "iff": a == b}[k]


def show(f) -> str:
    k = f[0]
    if k == "var":
        return f[1]
    if k == "bot":
        return "⊥"
    if k == "not":
        return "¬" + show(f[1])
    sym = {"and": "∧", "or": "∨", "imp": "→", "iff": "↔"}[k]
    return f"({show(f[1])} {sym} {show(f[2])})"


# ---------------------------------------------------------------------------
# Derivations
# ---------------------------------------------------------------------------

RULES = {  # macro -> (display name, citation shape: L = line, B = box)
    "ai": ("∧I", "LL"), "ae": ("∧E", "L"), "ii": ("→I", "B"), "ie": ("→E", "LL"),
    "oi": ("∨I", "L"), "oe": ("∨E", "LBB"), "ni": ("¬I", "B"), "ne": ("¬E", "LL"),
    "be": ("⊥E", "L"), "raa": ("RAA", "B"), "bi": ("↔I", "BB"), "bie": ("↔E", "LL"),
    "r": ("R", "L"),
    # derived rules (Chapter 1 proves each once; latex/fitch-book.sty has their macros)
    "nni": ("¬¬I", "L"), "nne": ("¬¬E", "L"), "mt": ("MT", "LL"), "ctp": ("CP", "L"),
    "ds": ("DS", "LL"), "dm": ("DM", "L"), "lem": ("LEM", ""),
}
UNCHECKED = {"Ai": "∀I", "Ae": "∀E", "Ei": "∃I", "Ee": "∃E", "eqi": "=I", "eqe": "=E"}


@dataclass
class Line:
    label: str
    text: str
    hypo: bool
    rule: str = ""          # macro name, "by", or ""
    by_text: str = ""
    refs: str = ""
    lineno: int = 0         # line in the source file
    boxes: tuple = ()       # ids of the boxes containing this line, outermost first
    formula: object = None
    parse_error: str = ""


@dataclass
class Box:
    id: int
    parent: int | None
    lines: list = field(default_factory=list)   # indices into the line list
    closed_at: int = -1                          # index of the first line after it


def read_group(s: str, i: int):
    """Read a balanced {...} group starting at or after i; return (content, end)."""
    while i < len(s) and s[i].isspace():
        i += 1
    if i >= len(s) or s[i] != "{":
        return None, i
    depth, j = 0, i
    while j < len(s):
        if s[j] == "{":
            depth += 1
        elif s[j] == "}":
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
        j += 1
    raise ParseError("unbalanced braces")


COMMAND = re.compile(r"\\(hypo|have|open|close)\b")


def parse_nd(body: str, first_lineno: int):
    """Turn an nd body into (lines, boxes, structural errors)."""
    lines, boxes, errors = [], [], []
    stack = []
    pos = 0
    while True:
        m = COMMAND.search(body, pos)
        if not m:
            break
        lineno = first_lineno + body.count("\n", 0, m.start())
        cmd = m.group(1)
        pos = m.end()
        if cmd == "open":
            box = Box(id=len(boxes), parent=stack[-1] if stack else None)
            boxes.append(box)
            stack.append(box.id)
            continue
        if cmd == "close":
            if not stack:
                errors.append((lineno, "\\close without a matching \\open"))
                continue
            box = boxes[stack.pop()]
            box.closed_at = len(lines)
            if not box.lines:
                errors.append((lineno, "empty box"))
            continue
        label, pos = read_group(body, pos)
        text, pos = read_group(body, pos)
        if label is None or text is None:
            errors.append((lineno, f"\\{cmd} needs {{label}} {{formula}}"))
            continue
        line = Line(label=label.strip(), text=text.strip(), hypo=(cmd == "hypo"),
                    lineno=lineno, boxes=tuple(stack))
        # justification: the rest up to the next command
        nxt = COMMAND.search(body, pos)
        rest = body[pos:nxt.start() if nxt else len(body)]
        jm = re.match(r"\s*\\([A-Za-z]+)", rest)
        if jm:
            name = jm.group(1)
            j = len(jm.group(0))
            if name == "by":
                by_text, j = read_group(rest, j)
                refs, j = read_group(rest, j)
                line.rule, line.by_text, line.refs = "by", by_text or "", refs or ""
            else:
                refs, j = read_group(rest, j)
                line.rule, line.refs = name, refs or ""
        for b in stack:
            boxes[b].lines.append(len(lines))
        lines.append(line)
    for b in stack:
        errors.append((first_lineno, "box opened but never closed"))
        boxes[b].closed_at = len(lines)
    return lines, boxes, errors


def parse_refs(refs: str):
    """'1,3-5' -> [('L', '1'), ('B', ('3', '5'))]."""
    out = []
    for part in [p.strip() for p in refs.split(",") if p.strip()]:
        if "-" in part:
            a, b = [x.strip() for x in part.split("-", 1)]
            out.append(("B", (a, b)))
        else:
            out.append(("L", part))
    return out


def check_derivation(lines, boxes):
    """Return (errors, notes) for one parsed derivation: lists of (lineno, message)."""
    errors, notes = [], []
    if any(not re.fullmatch(r"\d+", ln.label) for ln in lines if ln.label):
        notes.append((lines[0].lineno if lines else 0,
                      "schematic derivation (non-numeric labels): skipped"))
        return errors, notes

    index = {}
    for k, ln in enumerate(lines):
        if not ln.label:
            continue
        if ln.label in index:
            errors.append((ln.lineno, f"line label {ln.label} used twice"))
        else:
            index[ln.label] = k
    numbered = [int(ln.label) for ln in lines if ln.label]
    if numbered != list(range(1, len(numbered) + 1)) and len(set(numbered)) == len(numbered):
        errors.append((lines[0].lineno, f"lines are not numbered 1, 2, 3, ...: {numbered}"))

    # boxes begin with their assumption; no assumption in mid-box
    for box in boxes:
        if box.lines and not lines[box.lines[0]].hypo:
            errors.append((lines[box.lines[0]].lineno,
                           f"box starting at line {lines[box.lines[0]].label} "
                           f"does not begin with an assumption"))
    for k, ln in enumerate(lines):
        if ln.hypo and ln.boxes:
            box = boxes[ln.boxes[-1]]
            run = box.lines[:next((n for n, i in enumerate(box.lines)
                                   if not lines[i].hypo), len(box.lines))]
            if k not in run:
                errors.append((ln.lineno, f"assumption {ln.label} in the middle of a box"))

    def available(j, k):
        """Line index j may be cited at line index k."""
        return j < k and set(lines[j].boxes) <= set(lines[k].boxes)

    def box_for(a, b, k):
        """The closed box a-b citable at line index k, or an error message."""
        if a not in index or b not in index:
            return None, f"cites {a}-{b}, but line {a if a not in index else b} does not exist"
        ia, ib = index[a], index[b]
        for box in boxes:
            if box.lines and box.lines[0] == ia and box.lines[-1] == ib:
                if box.closed_at > k:
                    return None, f"cites box {a}-{b}, which is still open"
                parent_ok = box.parent is None or box.parent in lines[k].boxes
                if not parent_ok:
                    return None, f"cites box {a}-{b}, which sits inside a box that has closed"
                return box, ""
        if any(box.lines and box.lines[0] == ia and k in box.lines for box in boxes):
            return None, f"cites box {a}-{b}, which is still open"
        return None, f"cites {a}-{b}, which is not a box (a box runs from its assumption to its last line)"

    after_vdots = False
    for k, ln in enumerate(lines):
        if not ln.label:
            after_vdots = True
            notes.append((ln.lineno, "\\vdots row: skipped"))
            continue
        try:
            ln.formula = parse_formula(ln.text)
        except ParseError as e:
            ln.parse_error = str(e)
        if ln.hypo:
            if ln.rule and ln.rule != "by":
                errors.append((ln.lineno, f"assumption {ln.label} carries a rule"))
            continue
        if not ln.rule:
            if after_vdots:
                notes.append((ln.lineno, f"line {ln.label} follows \\vdots, unjustified: skipped"))
            else:
                errors.append((ln.lineno, f"line {ln.label} has no justification"))
            continue
        after_vdots = False

        cites = parse_refs(ln.refs)
        cited_ok = True
        resolved = []
        for shape, ref in cites:
            if shape == "L":
                if ref not in index:
                    errors.append((ln.lineno, f"line {ln.label} cites line {ref}, which does not exist"))
                    cited_ok = False
                elif not available(index[ref], k):
                    why = "a later line" if index[ref] >= k else "inside a box that has closed"
                    errors.append((ln.lineno, f"line {ln.label} cites line {ref}, {why}"))
                    cited_ok = False
                resolved.append(("L", index.get(ref)))
            else:
                box, err = box_for(ref[0], ref[1], k)
                if err:
                    errors.append((ln.lineno, f"line {ln.label} {err}"))
                    cited_ok = False
                resolved.append(("B", box))

        if ln.rule == "by":
            notes.append((ln.lineno, f"line {ln.label} justified by text "
                                     f"({ln.by_text.strip() or 'empty'}): shape not checked"))
            continue
        if ln.rule in UNCHECKED:
            notes.append((ln.lineno, f"line {ln.label}: {UNCHECKED[ln.rule]} not checked"))
            continue
        if ln.rule not in RULES:
            errors.append((ln.lineno, f"line {ln.label}: unknown rule macro \\{ln.rule}"))
            continue
        name, want = RULES[ln.rule]
        got = "".join(s for s, _ in cites)
        if got != want:
            errors.append((ln.lineno, f"line {ln.label}: {name} cites "
                                      f"{_shape_words(want)}, got {ln.refs or 'nothing'}"))
            continue
        if not cited_ok:
            continue
        involved = [ln] + [lines[i] for s, i in resolved if s == "L"]
        for s, box in resolved:
            if s == "B":
                involved += [lines[box.lines[0]], lines[box.lines[-1]]]
        bad = [x for x in involved if x.formula is None]
        if bad:
            notes.append((ln.lineno, f"line {ln.label}: formula of line {bad[0].label} "
                                     f"not propositional ({bad[0].parse_error}): shape not checked"))
            continue
        problem = check_shape(ln.rule, ln.formula, resolved, lines)
        if problem:
            errors.append((ln.lineno, f"line {ln.label}: {name} {problem}"))
    return errors, notes


def _shape_words(want: str) -> str:
    words = {"L": "a line", "B": "a box i-j"}
    return ", ".join(words[c] for c in want)


def check_shape(rule, f, resolved, lines):
    """Return '' if the line is a correct instance of the rule, else what is wrong."""
    L = [lines[i].formula for s, i in resolved if s == "L"]
    B = [(lines[b.lines[0]].formula, lines[b.lines[-1]].formula) for s, b in resolved if s == "B"]
    s = show
    if rule == "ai":
        if f[0] == "and" and {(f[1], f[2]), (f[2], f[1])} & {(L[0], L[1])}:
            return ""
        return f"needs {s(f)} to be the conjunction of the cited lines {s(L[0])}, {s(L[1])}"
    if rule == "ae":
        if L[0][0] == "and" and f in (L[0][1], L[0][2]):
            return ""
        return f"needs the cited line to be a conjunction with {s(f)} as one side (got {s(L[0])})"
    if rule == "ii":
        (a, b), = B
        if f == ("imp", a, b):
            return ""
        return f"needs {s(a)} → {s(b)} from its box, not {s(f)}"
    if rule == "ie":
        for imp, ant in ((L[0], L[1]), (L[1], L[0])):
            if imp[0] == "imp" and imp[1] == ant and imp[2] == f:
                return ""
        return f"needs an implication and its antecedent giving {s(f)} (got {s(L[0])}, {s(L[1])})"
    if rule == "oi":
        if f[0] == "or" and L[0] in (f[1], f[2]):
            return ""
        return f"needs {s(f)} to be a disjunction with {s(L[0])} as one side"
    if rule == "oe":
        d = L[0]
        (a1, c1), (a2, c2) = B
        if d[0] != "or":
            return f"cites {s(d)}, which is not a disjunction"
        if (a1, a2) != (d[1], d[2]):
            return f"boxes must assume {s(d[1])} and {s(d[2])} (got {s(a1)}, {s(a2)})"
        if c1 != f or c2 != f:
            return f"both boxes must end in {s(f)} (got {s(c1)}, {s(c2)})"
        return ""
    if rule == "ni":
        (a, b), = B
        if b != BOT:
            return f"box must end in ⊥ (ends in {s(b)})"
        if f != ("not", a):
            return f"concludes {s(f)}, but the box assumed {s(a)}"
        return ""
    if rule == "ne":
        if f != BOT:
            return f"concludes ⊥, not {s(f)}"
        if L[1] == ("not", L[0]) or L[0] == ("not", L[1]):
            return ""
        return f"needs a statement and its negation (got {s(L[0])}, {s(L[1])})"
    if rule == "be":
        return "" if L[0] == BOT else f"cites {s(L[0])}, not ⊥"
    if rule == "raa":
        (a, b), = B
        if b != BOT:
            return f"box must end in ⊥ (ends in {s(b)})"
        if a != ("not", f):
            return f"concludes {s(f)}, but the box assumed {s(a)}, not ¬{s(f)}"
        return ""
    if rule == "bi":
        (a1, c1), (a2, c2) = B
        if f[0] == "iff" and (a1, c1, a2, c2) == (f[1], f[2], f[2], f[1]):
            return ""
        return f"needs boxes {s(f[1]) if f[0] == 'iff' else 'A'} … {s(f[2]) if f[0] == 'iff' else 'B'} and back, concluding a biconditional"
    if rule == "bie":
        for bic, side in ((L[0], L[1]), (L[1], L[0])):
            if bic[0] == "iff" and ((bic[1] == side and bic[2] == f) or (bic[2] == side and bic[1] == f)):
                return ""
        return f"needs a biconditional and one side giving the other (got {s(L[0])}, {s(L[1])}, {s(f)})"
    if rule == "r":
        return "" if L[0] == f else f"repeats {s(L[0])} as {s(f)}"
    if rule == "nni":
        return "" if f == ("not", ("not", L[0])) else f"needs ¬¬{s(L[0])}, not {s(f)}"
    if rule == "nne":
        return "" if L[0] == ("not", ("not", f)) else f"needs the cited line to be ¬¬{s(f)} (got {s(L[0])})"
    if rule == "mt":
        for imp, neg in ((L[0], L[1]), (L[1], L[0])):
            if imp[0] == "imp" and neg == ("not", imp[2]) and f == ("not", imp[1]):
                return ""
        return f"needs A → B and ¬B giving ¬A (got {s(L[0])}, {s(L[1])}, {s(f)})"
    if rule == "ctp":
        a = L[0]
        if a[0] == "imp" and f == ("imp", ("not", a[2]), ("not", a[1])):
            return ""
        if (a[0] == "imp" and a[1][0] == "not" and a[2][0] == "not"
                and f == ("imp", a[2][1], a[1][1])):
            return ""          # the converse direction, ¬B → ¬A to A → B
        return f"needs the contrapositive of {s(a)}, not {s(f)}"
    if rule == "ds":
        for d, n in ((L[0], L[1]), (L[1], L[0])):
            if d[0] == "or" and ((n == ("not", d[1]) and f == d[2]) or (n == ("not", d[2]) and f == d[1])):
                return ""
        return f"needs A ∨ B and ¬A giving B (got {s(L[0])}, {s(L[1])}, {s(f)})"
    if rule == "dm":
        a = L[0]
        def dual(x):
            if x[0] == "not" and x[1][0] in ("and", "or"):
                op = "or" if x[1][0] == "and" else "and"
                return (op, ("not", x[1][1]), ("not", x[1][2]))
            return None
        if dual(a) == f or dual(f) == a:
            return ""
        return f"is not a De Morgan law between {s(a)} and {s(f)}"
    if rule == "lem":
        if f[0] == "or" and f[2] == ("not", f[1]):
            return ""
        return f"needs A ∨ ¬A, not {s(f)}"
    return "unknown rule"


# ---------------------------------------------------------------------------
# Truth tables
# ---------------------------------------------------------------------------

TV = re.compile(r"^(?:\\mathrm\{([TF])\}|\\text\{([TF])\}|\\textsf\{([TF])\}|([TF]))$")


def check_truth_table(body: str, first_lineno: int):
    errors, notes = [], []
    rows = [r.strip() for r in re.split(r"\\\\", body)]
    if not any("\\hline" in r for r in rows):
        return None
    header_raw, *rest = re.split(r"\\hline", body, maxsplit=1)
    if not rest:
        return None
    header = [c.strip() for c in header_raw.strip().rstrip("\\").split("&")]
    data = []
    for r in re.split(r"\\\\", rest[0]):
        r = r.replace("\\hline", "").strip()
        if not r:
            continue
        cells = [c.strip() for c in r.split("&")]
        vals = []
        for c in cells:
            m = TV.match(c)
            if not m:
                return None            # not a T/F table
            vals.append(next(g for g in m.groups() if g) == "T")
        data.append(vals)
    if not data:
        return None
    columns = []
    for h in header:
        try:
            columns.append(parse_formula(h))
        except ParseError as e:
            columns.append(None)
            notes.append((first_lineno, f"truth table column {h!r} not propositional ({e}): skipped"))
    letters = {c[1]: n for n, c in enumerate(columns) if c is not None and c[0] == "var"}
    for r, vals in enumerate(data, 1):
        if len(vals) != len(header):
            errors.append((first_lineno, f"truth table row {r} has {len(vals)} cells, header {len(header)}"))
            continue
        env = {x: vals[n] for x, n in letters.items()}
        for n, col in enumerate(columns):
            if col is None or col[0] == "var":
                continue
            try:
                want = evaluate(col, env)
            except KeyError as e:
                notes.append((first_lineno, f"truth table column {header[n]!r} uses letter "
                                            f"{e.args[0]} with no column: skipped"))
                columns[n] = None
                continue
            if want != vals[n]:
                row = ", ".join(f"{x}={'T' if env[x] else 'F'}" for x in sorted(env))
                errors.append((first_lineno, f"truth table: {header[n]} is "
                                             f"{'T' if want else 'F'} in row {r} ({row}), "
                                             f"table says {'T' if vals[n] else 'F'}"))
    return errors, notes


# ---------------------------------------------------------------------------
# Files
# ---------------------------------------------------------------------------

ND = re.compile(r"\\begin\{nd\}(.*?)\\end\{nd\}", re.S)
ARRAY = re.compile(r"\\begin\{array\}\{[^}]*\}(.*?)\\end\{array\}", re.S)
EXPECT = "% expect-invalid"


def expects_invalid(text: str, start: int) -> bool:
    """`% expect-invalid` inside the raw block before \\begin{nd}, or just before the block."""
    before = text[:start]
    lines = before.split("\n")
    # walk back to the fence that opens the raw block, plus one line more
    window = []
    for ln in reversed(lines[-8:]):
        window.append(ln)
        if ln.strip().startswith("```"):
            break
    idx = len(lines) - len(window) - 1
    if idx >= 0:
        window.append(lines[idx])
    return any(EXPECT in ln for ln in window)


def check_text(text: str):
    """(errors, notes, counts) for one file: errors/notes are (lineno, message)."""
    errors, notes = [], []
    counts = {"derivations": 0, "expected_invalid": 0, "tables": 0}
    for m in ND.finditer(text):
        lineno = text.count("\n", 0, m.start(1)) + 1
        counts["derivations"] += 1
        try:
            lines, boxes, struct = parse_nd(m.group(1), lineno)
            errs, nts = check_derivation(lines, boxes) if lines else ([], [])
            errs = struct + errs
        except ParseError as e:
            errs, nts = [(lineno, f"cannot read derivation: {e}")], []
        if expects_invalid(text, m.start()):
            counts["expected_invalid"] += 1
            if errs:
                nts = nts + [(lineno, f"expected invalid, and is: {errs[0][1]}"
                                      + (f" (+{len(errs) - 1} more)" if len(errs) > 1 else ""))]
                errs = []
            else:
                errs = [(lineno, "marked % expect-invalid but checks clean")]
        errors += errs
        notes += nts
    for m in ARRAY.finditer(text):
        lineno = text.count("\n", 0, m.start()) + 1
        res = check_truth_table(m.group(1), lineno)
        if res is None:
            continue
        counts["tables"] += 1
        errors += res[0]
        notes += res[1]
    return errors, notes, counts


def find_violations(root: Path):
    """Check every .md under `root` (a file or directory).

    Returns (errors, notes, counts); errors and notes are (path, lineno, message).
    """
    root = Path(root)
    files = [root] if root.is_file() else sorted(root.rglob("*.md"))
    errors, notes = [], []
    total = {"derivations": 0, "expected_invalid": 0, "tables": 0}
    for f in files:
        e, n, c = check_text(f.read_text(encoding="utf-8"))
        errors += [(f, ln, msg) for ln, msg in e]
        notes += [(f, ln, msg) for ln, msg in n]
        for k in total:
            total[k] += c[k]
    return errors, notes, total


def report(items) -> str:
    return "\n".join(f"{p}:{ln}: {msg}" for p, ln, msg in items)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="Check Fitch derivations (nd blocks) and truth tables in the book's source.",
        epilog="Mark a deliberately flawed derivation with '% expect-invalid' before \\begin{nd}.")
    ap.add_argument("paths", nargs="*", default=["src"], help="files or directories (default: src)")
    ap.add_argument("--notes", action="store_true", help="also list what was skipped and why")
    args = ap.parse_args(argv)
    errors, notes, total = [], [], {"derivations": 0, "expected_invalid": 0, "tables": 0}
    for p in args.paths:
        e, n, c = find_violations(Path(p))
        errors += e
        notes += n
        for k in total:
            total[k] += c[k]
    if args.notes and notes:
        print(report(notes))
        print()
    if errors:
        print(report(errors))
    print(f"\n{total['derivations']} derivation(s) ({total['expected_invalid']} marked "
          f"expect-invalid), {total['tables']} truth table(s): {len(errors)} error(s), "
          f"{len(notes)} note(s){'' if args.notes else ' (--notes to list)'}.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
