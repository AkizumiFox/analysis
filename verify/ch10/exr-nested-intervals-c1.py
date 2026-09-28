"""exr-nested-intervals-c1 (Ch 10, 07): the bisection of (b) run on A = {x in Q : x > 0,
x^2 < 2} with a = 1, M = 2: b_n is an upper bound, some element of A is >= a_n, and
b_n - a_n = (M - a)/2^(n-1)."""
from fractions import Fraction as F

QUOTED = {"three statements of (b) hold": True}

a, M = F(1), F(2)
lo, hi = a, M
is_upper = lambda c: c > 0 and c * c > 2          # for rational c >= 1 (c^2 = 2 is impossible)
for n in range(1, 60):
    assert is_upper(hi) and lo * lo < 2 and hi - lo == (M - a) / 2 ** (n - 1)
    c = (lo + hi) / 2
    lo, hi = (lo, c) if is_upper(c) else (c, hi)
print("exr-nested-intervals-c1: all quoted values check")
