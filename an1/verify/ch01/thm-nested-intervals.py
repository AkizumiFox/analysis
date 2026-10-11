"""thm-nested-intervals (Ch 11, 07): the bisection toward sqrt 2 from [1, 2]:
[1, 2], [1, 3/2], [5/4, 3/2], [11/8, 3/2], [11/8, 23/16]; each keeps a^2 < 2 < b^2 and has
length 1/2^(n-1) <= 1/n; midpoints never square to 2."""
from fractions import Fraction as F

QUOTED = {"intervals": [(F(1), F(2)), (F(1), F(3, 2)), (F(5, 4), F(3, 2)), (F(11, 8), F(3, 2)), (F(11, 8), F(23, 16))]}
a, b = F(1), F(2)
got = [(a, b)]
for n in range(1, 60):
    c = (a + b) / 2
    assert c * c != 2
    a, b = (a, c) if c * c > 2 else (c, b)
    got.append((a, b))
assert got[:5] == QUOTED["intervals"]
for n, (a, b) in enumerate(got, start=1):
    assert a * a < 2 < b * b and b - a == F(1, 2 ** (n - 1)) <= F(1, n)
assert F(3, 2) ** 2 == F(9, 4) > 2 and F(5, 4) ** 2 == F(25, 16) < 2
print("thm-nested-intervals: all quoted values check")
