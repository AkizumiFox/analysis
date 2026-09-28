"""def-supremum (Ch 10, 02): the Quick check after the warnings, A = {(-1)^n / n}: max A = 1/2
(at n = 2) and min A = -1 (at n = 1), checked on the first 10^4 terms (the tail is trapped in
[-1/n, 1/n])."""
from fractions import Fraction as F

QUOTED = {"max": F(1, 2), "min": F(-1)}
terms = [F((-1) ** n, n) for n in range(1, 10001)]
assert max(terms) == QUOTED["max"] == terms[1] and min(terms) == QUOTED["min"] == terms[0]
print("def-supremum: all quoted values check")
