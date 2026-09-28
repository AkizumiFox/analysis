"""exm-square-even-via-contrapositive (Ch 2, Section 2.3): (E3) (2k+1)^2 = 2(2k^2+2k)+1;
n^2 even implies n even; the skeleton has 13 lines."""
QUOTED = {"lines": 13}

for k in range(-500, 501):
    assert (2 * k + 1) ** 2 == 2 * (2 * k * k + 2 * k) + 1
for n in range(-1000, 1001):
    if (n * n) % 2 == 0:
        assert n % 2 == 0

import re, pathlib
src = pathlib.Path("src/ch02-negation-and-classical-logic/03-derived-rules.md").read_text()
block = src.split("{#exm-square-even-via-contrapositive}")[1].split("\\end{nd}")[0]
labels = re.findall(r"\\(?:hypo|have)\s*\{(\d+)\}", block)
assert len(labels) == QUOTED["lines"], labels
print("exm-square-even-via-contrapositive: all quoted values check")
