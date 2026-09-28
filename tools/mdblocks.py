"""Shared reader for the book's Markdown: fenced divs, headings and code fences.

Not a checker itself. `tools/check_structure.py` and `tools/ledger.py` both need to
know where a `::: {#thm-foo}` block starts and ends, which blocks are siblings, and
which lines are inside a code fence (where a `:::` or a `#` means nothing), so the
rule lives here once. Imported by path, like every tool:

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import mdblocks

Pandoc's rules, as far as the book uses them: a div opens with a line of three or
more colons followed by attributes (`{#id .class key="v"}`) or a bare class word,
and closes with a line of three or more colons and nothing else, matching the
innermost open div. Code fences (```` ``` ```` or `~~~`, three or more) hide
everything inside them, including raw LaTeX blocks.
"""
import re
from dataclasses import dataclass, field

OPEN = re.compile(r"^(:{3,})\s*(\{[^}]*\}|[A-Za-z][\w-]*)\s*:*\s*$")
CLOSE = re.compile(r"^:{3,}\s*$")
FENCE = re.compile(r"^(`{3,}|~{3,})")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*(\{[^}]*\})?\s*$")


@dataclass
class Div:
    start: int                      # 0-based index of the opening fence line
    end: int = -1                   # 0-based index of the closing fence line
    id: str = ""
    classes: tuple = ()
    parent: "Div | None" = None
    children: list = field(default_factory=list)

    @property
    def kind(self) -> str:
        """`thm`, `exr`, ... for a labelled block; the first class otherwise."""
        if self.id and "-" in self.id:
            return self.id.split("-", 1)[0]
        return self.classes[0] if self.classes else ""

    def has(self, cls: str) -> bool:
        return cls in self.classes


@dataclass
class Doc:
    lines: list
    divs: list                      # every div, in order of opening
    top: list                       # divs with no parent
    headings: list                  # (index, level, text)
    in_code: list                   # per line: True inside a code fence (fences included)


def parse_attrs(spec: str):
    spec = spec.strip()
    if not spec.startswith("{"):
        return "", (spec,)
    body = spec[1:-1]
    body = re.sub(r'\w[\w-]*="[^"]*"', " ", body)   # drop key="value" pairs
    ident = ""
    classes = []
    for tok in body.split():
        if tok.startswith("#"):
            ident = tok[1:]
        elif tok.startswith("."):
            classes.append(tok[1:])
    return ident, tuple(classes)


def parse(text: str) -> Doc:
    lines = text.split("\n")
    divs, top, headings, in_code = [], [], [], []
    stack = []
    fence = None
    for i, line in enumerate(lines):
        if fence:
            in_code.append(True)
            m = FENCE.match(line.strip())
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence) \
                    and line.strip() == m.group(1):
                fence = None
            continue
        m = FENCE.match(line.strip())
        if m:
            fence = m.group(1)
            in_code.append(True)
            continue
        in_code.append(False)
        if CLOSE.match(line):
            if stack:
                stack.pop().end = i
            continue
        m = OPEN.match(line)
        if m:
            ident, classes = parse_attrs(m.group(2))
            div = Div(start=i, id=ident, classes=classes,
                      parent=stack[-1] if stack else None)
            (stack[-1].children if stack else top).append(div)
            divs.append(div)
            stack.append(div)
            continue
        m = HEADING.match(line)
        if m and not stack:
            headings.append((i, len(m.group(1)), m.group(2)))
    for div in stack:            # unclosed: runs to the end of the file
        div.end = len(lines) - 1
    return Doc(lines=lines, divs=divs, top=top, headings=headings, in_code=in_code)


def next_nonblank(lines: list, i: int) -> int:
    """Index of the first non-blank line after index i, or -1."""
    for j in range(i + 1, len(lines)):
        if lines[j].strip():
            return j
    return -1


def following_div(doc: Doc, div: Div):
    """The div that opens on the first non-blank line after `div` closes, if any."""
    j = next_nonblank(doc.lines, div.end)
    if j < 0:
        return None
    for d in doc.divs:
        if d.start == j:
            return d
    return None


def previous_sibling(div: Div, doc: Doc):
    siblings = div.parent.children if div.parent else doc.top
    k = siblings.index(div)
    return siblings[k - 1] if k > 0 else None


def body(doc: Doc, div: Div) -> str:
    return "\n".join(doc.lines[div.start + 1:div.end])
