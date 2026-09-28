"""thm-nth-root (Ch 10, 06): the claim 0 < y^k - x^k <= k y^(k-1) (y - x) for 0 <= x < y;
x0 = a/(1 + a) is in S and 1 + a bounds S; with C = n (s + 1)^(n-1) and
h = min{1/2, |s^n - a| / (2C)}, Case 1 gives (s + h)^n < a and Case 2 gives s - h > 0,
(s - h)^n > a; for n = 2 the constant C = 2(s + 1)."""
from fractions import Fraction as F

QUOTED = {"cap": F(1, 2)}

pts = [F(k, 7) for k in range(0, 36)]
for k in range(1, 7):
    for x in pts:
        for y in pts:
            if x < y:
                assert 0 < y ** k - x ** k <= k * y ** (k - 1) * (y - x)

for a in [F(1, 10), F(1, 2), F(2), F(5), F(27, 4), F(100)]:
    for n in range(1, 7):
        x0 = a / (1 + a)
        assert 0 < x0 < 1 and x0 < a and x0 ** n <= x0 < a
        assert (1 + a) ** n >= 1 + a > a
        for j in range(1, 60):
            s = x0 + (1 + a - x0) * F(j, 60)
            if s ** n == a:
                continue
            C = n * (s + 1) ** (n - 1)
            h = min(F(1, 2), abs(s ** n - a) / (2 * C))
            assert h > 0 and h * C < abs(s ** n - a)
            if s ** n < a:
                assert (s + h) ** n < a
            else:
                assert s - h > 0 and (s - h) ** n > a
for s in [F(1), F(7, 5), F(3, 2)]:
    assert 2 * (s + 1) ** 1 == 2 * (s + 1) > 2 * s + 1
print("thm-nth-root: all quoted values check")
