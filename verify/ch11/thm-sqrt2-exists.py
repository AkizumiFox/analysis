"""thm-sqrt2-exists (Ch 10, 06): the two nudges on real-like (rational) s in [1, 2]:
Case 1 (s^2 < 2): h = (2 - s^2)/(4s + 2), 0 < h <= 1/6, (s + h)^2 <= 1 + s^2/2 < 2;
Case 2 (s^2 > 2): h = (s^2 - 2)/(2s), s - h = (s^2 + 2)/(2s) > 0, (s - h)^2 = 2 + h^2."""
from fractions import Fraction as F

QUOTED = {"h bound": F(1, 6)}

for k in range(1000, 2001):
    s = F(k, 1000)
    if s * s < 2:
        h = (2 - s * s) / (4 * s + 2)
        assert 0 < h <= F(1, 6) and (s + h) ** 2 <= 1 + s * s / 2 < 2
    elif s * s > 2:
        h = (s * s - 2) / (2 * s)
        assert h > 0 and s - h == (s * s + 2) / (2 * s) > 0 and (s - h) ** 2 == 2 + h * h
print("thm-sqrt2-exists: all quoted values check")
