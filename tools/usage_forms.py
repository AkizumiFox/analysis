"""English usage forms, for hashing: normalize(text) rewrites every avoided form to its preferred one.

The series is migrating its prose to the usage conventions of math-atlas (registry/usage.yaml). A
usage-only edit -- `non-empty` -> `nonempty`, `iff` -> `if and only if`, an added serial comma, a
heading anchor kept as `{#old-id}` -- does not change the mathematics, so the claim ledger
(tools/ledger.py) hashes `normalize(text)` and such an edit leaves a referee verdict current. A
mathematical edit changes the normalized text as much as the raw text, so it still stales the verdict.

The text is normalized as a whole, mathematics and labels included: hashing only needs the old and
the new text to normalize to the same string, so there is no need to mask what the migration itself
leaves alone. The price is that a few non-usage edits are invisible to the hash too, and a referee
should know them: adding or removing any comma before "and"/"or" (not only a serial comma, so
also a scope change such as "P or Q, and R"), an avoided form inside mathematics, a label or
`\text{}` (e.g. renaming `non-negative` in a label), and renaming any trailing heading anchor
`{#id}`, not only one the migration appended.

RULES is copied from math-atlas tools/usage_apply.py (the RULES list) at math-atlas commit 1dcc264
(last change to that file: 7b1c19b). The two lists must be kept in step: when a mechanical rule is
added there, add it here too, before the migration is applied to this book. (A new rule changes
the hash of every item that contains its avoided form, so add it while those verdicts can be
re-stamped.) REVIEW_RULES are the review-type forms that the linear algebra book's migration also
edited, and the serial comma.
"""
import re

# avoided form -> replacement, for the mechanical groups. Copied verbatim from
# math-atlas tools/usage_apply.py (commit 1dcc264). Keep in step.
RULES = [
    (re.compile(r"(?<![\w-])([Nn])on-([a-z])"), r"\1on\2"),
    (re.compile(r"\b(is|are|be|not) one-to-one\b"), r"\1 injective"),
    (re.compile(r"\bone-one\b"), "injective"),
    (re.compile(r"\bone-to-one correspondence(s?)\b"), r"bijection\1"),
    (re.compile(r"\blinear transformation(s?)\b"), r"linear map\1"),
    (re.compile(r"\bnullspace(s?)\b"), r"null space\1"),
    (re.compile(r"\b([Cc])o-domain"), r"\1odomain"),
    (re.compile(r"\b([Pp])re-image"), r"\1reimage"),
    (re.compile(r"\b([Cc])ounter-example"), r"\1ounterexample"),
    (re.compile(r"\b([Ff]inite|[Ii]nfinite) dimensional\b"), r"\1-dimensional"),
    (re.compile(r"\b(positive|negative)(?:-| semi-|-semi)(definite|semidefinite)\b"),
     lambda m: f"{m.group(1)} {'semidefinite' if 'semi' in m.group(0) else m.group(2)}"),
    (re.compile(r"\b([Ss])elf ?adjoint\b"), r"\1elf-adjoint"),
    (re.compile(r"\b(is|are|be|been) well-defined\b"), r"\1 well defined"),
    (re.compile(r"\b(a|an|the) well defined\b"), r"\1 well-defined"),
    (re.compile(r"\bformulae\b"), "formulas"),
    (re.compile(r"\blemmata\b"), "lemmas"),
    (re.compile(r"\b([Nn])eighbour"), r"\1eighbor"),
    (re.compile(r"\b([Bb])ehaviour"), r"\1ehavior"),
    (re.compile(r"\b([Cc])entre(s|d)?\b"), r"\1enter\2"),
    (re.compile(r"\b([Ff])ibre"), r"\1iber"),
    (re.compile(r"\b([Cc])olour"), r"\1olor"),
    (re.compile(r"\b([Ff])avour"), r"\1avor"),
    (re.compile(r"\b([Aa])nalys(e|ed|ing)\b"), r"\1nalyz\2"),
    (re.compile(r"\b(label|model|cancel)l(ed|ing)\b"), r"\1\2"),
]

# Review-type forms the linear algebra migration also edited, applied after RULES, in order.
REVIEW_RULES = [
    (re.compile(r"(?<![\\\w])([Ii])ff\b"), r"\1f and only if"),          # the word, not \iff
    (re.compile(r"\b(is|are|be|not) onto\b"), r"\1 surjective"),          # adjectival only
    (re.compile(r",(?=\s+(?:and|or)\b)"), ""),                            # serial comma: ", and" = " and"
]

# A heading's explicit anchor, as the migration appends it to keep the old automatic id.
HEADING_ANCHOR = re.compile(r"^(#{1,6} .*?)[ \t]+\{#[\w.:-]+\}[ \t]*$", re.M)


def _apply_mechanical(text: str) -> str:
    """RULES applied as usage_apply.rewrite applies them: all matches found on the input, then
    the non-overlapping ones replaced (on overlap the earlier match wins)."""
    edits = []
    for pat, rep in RULES:
        for m in pat.finditer(text):
            edits.append((m.start(), m.end(), m.expand(rep) if isinstance(rep, str) else rep(m)))
    edits.sort()
    out, last = [], 0
    for a, b, new in edits:
        if a < last:
            continue
        out += [text[last:a], new]
        last = b
    return "".join(out) + text[last:]


def normalize(text: str) -> str:
    """The text with every avoided usage form rewritten to its preferred form and the migration's
    heading anchors removed. The identity on text that contains none of them."""
    text = HEADING_ANCHOR.sub(r"\1", text)
    text = _apply_mechanical(text)
    for pat, rep in REVIEW_RULES:
        text = pat.sub(rep, text)
    return text
