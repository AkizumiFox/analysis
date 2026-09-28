"""exm-sup-open-interval (Ch 10, 02): for 1/2 <= M < 1 the midpoint (M + 1)/2 lies in (M, 1)."""
from fractions import Fraction as F

QUOTED = {"element used": F(1, 2)}
for k in range(500, 1000):
    M = F(k, 1000)
    a = (M + 1) / 2
    assert 0 < M < a < 1
print("exm-sup-open-interval: all quoted values check")
