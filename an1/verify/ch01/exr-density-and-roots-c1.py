"""exr-density-and-roots-c1 (Ch 11, 06): the marking scheme's alternative Case 1 constant
h = min{1, (2 - s^2)/6} works for 1 <= s <= 2 with s^2 < 2 (since 2s + 1 <= 5)."""
from fractions import Fraction as F

QUOTED = {"denominator": 6, "bound on 2s + 1": 5}

for k in range(1000, 1415):
    s = F(k, 1000)
    h = min(F(1), (2 - s * s) / 6)
    assert h > 0 and h * h <= h and 2 * s + 1 <= 5
    assert (s + h) ** 2 <= s * s + (2 * s + 1) * h <= s * s + 5 * h < 2
print("exr-density-and-roots-c1: all quoted values check")
