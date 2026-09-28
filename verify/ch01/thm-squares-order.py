"""thm-squares-order (Ch 1, Section 1.5): x, y >= 0 gives x <= y iff x^2 <= y^2; the remark's
witnesses (-2, 1) and (1, -2); C2(a)'s surviving direction checked in exr-...-c2."""
from fractions import Fraction as F

QUOTED = {"(=>) fails": (-2, 1, 4, 1), "(<=) fails": (1, -2, 1, 4)}

pts = [F(k, 8) for k in range(0, 161)]
for x in pts:
    for y in pts:
        assert (x <= y) == (x * x <= y * y)
x, y, x2, y2 = QUOTED["(=>) fails"]
assert x <= y and x * x == x2 > y2 == y * y and y >= 0 and x < 0
x, y, x2, y2 = QUOTED["(<=) fails"]
assert x * x == x2 <= y2 == y * y and x > y and x >= 0 and y < 0
print("thm-squares-order: all quoted values check")
