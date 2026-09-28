"""exr-the-axiom-a1 (Ch 10, 03): (b) x = |M| + 1 gives x^2 > M; (c) for -1 <= M < 0 the
midpoint M/2 lies in (M, 0)."""
from fractions import Fraction as F
from _grid import grid

QUOTED = {"witnesses work": True}

for M in grid(-10, 10, 8):
    x = abs(M) + 1
    assert x >= 1 and x * x >= x > abs(M) >= M
for k in range(-1000, 0):
    M = F(k, 1000)
    assert M < M / 2 < 0
print("exr-the-axiom-a1: all quoted values check")
