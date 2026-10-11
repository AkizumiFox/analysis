"""exm-lub-first-use (Ch 11, 03): 1 is in S; 2 bounds S; the warning's smaller bound 3/2
(9/4 > 2); and the Quick check: the integers up to 3.5 have maximum 3."""
from fractions import Fraction as F

QUOTED = {"bound": F(3, 2), "square": F(9, 4), "max Z <= 3.5": 3}
assert 1 > 0 and 1 * 1 < 2 and 2 * 2 == 4 > 2
b = QUOTED["bound"]
assert b * b == QUOTED["square"] > 2
for k in range(1500, 1600):   # every x > 3/2 has x^2 > 9/4
    x = F(k, 1000) + F(1, 10**6)
    assert x > b and x * x > QUOTED["square"]
ints = [n for n in range(-50, 50) if n <= F(7, 2)]
assert max(ints) == QUOTED["max Z <= 3.5"]
print("exm-lub-first-use: all quoted values check")
