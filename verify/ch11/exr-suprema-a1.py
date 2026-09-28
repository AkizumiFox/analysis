"""exr-suprema-a1 (Ch 11, 02): (e) Case 2 at s = 17/12 gives h = 1/408, s - h = 577/408,
(s - h)^2 = 2 + 1/166464; 577^2 = 332929 = 2 * 408^2 + 1. (c) x^2 <= 4 iff -2 <= x <= 2."""
from fractions import Fraction as F
from _grid import grid

QUOTED = {"h": F(1, 408), "s-h": F(577, 408), "408^2": 166464, "577^2": 332929}
s = F(17, 12)
assert s * s == 2 + F(1, 144)
h = (s * s - 2) / (2 * s)
assert h == QUOTED["h"] and s - h == QUOTED["s-h"]
assert (s - h) ** 2 == 2 + F(1, QUOTED["408^2"]) == 2 + h * h
assert 408 ** 2 == QUOTED["408^2"] and 577 ** 2 == QUOTED["577^2"] == 2 * 408 ** 2 + 1
for x in grid(-4, 4, 12):
    assert (x * x <= 4) == (-2 <= x <= 2)
print("exr-suprema-a1: all quoted values check")
