"""exm-solve-abs-inequality (Ch 10, 01): |4 - 3x| < 2 iff 2/3 < x < 2; |4 - 3x| = 3|x - 4/3|."""
from fractions import Fraction as F
from _grid import grid

QUOTED = {"interval": (F(2, 3), F(2)), "center": F(4, 3), "radius": F(2, 3)}
lo, hi = QUOTED["interval"]
pts = grid(-3, 4, 60) + [lo, hi, lo + F(1, 10**9), hi - F(1, 10**9)]
for x in pts:
    assert (abs(4 - 3 * x) < 2) == (lo < x < hi)
    assert abs(4 - 3 * x) == 3 * abs(x - QUOTED["center"])
assert QUOTED["center"] - QUOTED["radius"] == lo and QUOTED["center"] + QUOTED["radius"] == hi
print("exm-solve-abs-inequality: all quoted values check")
