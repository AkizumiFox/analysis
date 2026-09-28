"""exr-biconditional-and-definitions-c2 (Ch 1, Section 1.5): with y >= 0 only, (<=) survives,
(=>) fails at x = -2, y = 1; |x| <= |y| iff x^2 <= y^2 for all reals."""
from fractions import Fraction as F

QUOTED = {"witness": (-2, 1)}

pts = [F(k, 8) for k in range(-80, 81)]
for x in pts:
    for y in pts:
        if y >= 0 and x * x <= y * y:
            assert x <= y
        assert (abs(x) <= abs(y)) == (x * x <= y * y)
        assert abs(x) ** 2 == x * x
x, y = QUOTED["witness"]
assert x <= y and y >= 0 and x * x > y * y
print("exr-biconditional-and-definitions-c2: all quoted values check")
