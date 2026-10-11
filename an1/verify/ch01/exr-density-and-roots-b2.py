"""exr-density-and-roots-b2 (Ch 11, 06): sqrt 3 by the move: Case 1 h = (3 - s^2)/(4s + 2),
0 < h <= 1/3, (s + h)^2 <= (3 + s^2)/2 < 3; Case 2 h = (s^2 - 3)/(2s), s - h = (s^2 + 3)/(2s) > 0,
(s - h)^2 = 3 + h^2; 2 bounds S since x >= 2 gives x^2 >= 4 > 3."""
from fractions import Fraction as F

QUOTED = {"h bound": F(1, 3)}

for k in range(1000, 2001):
    s = F(k, 1000)
    if s * s < 3:
        h = (3 - s * s) / (4 * s + 2)
        assert 0 < h <= F(1, 3) and h * h <= h
        assert (s + h) ** 2 <= s * s + (2 * s + 1) * h == (3 + s * s) / 2 < 3
    elif s * s > 3:
        h = (s * s - 3) / (2 * s)
        assert h > 0 and s - h == (s * s + 3) / (2 * s) > 0 and (s - h) ** 2 == 3 + h * h
print("exr-density-and-roots-b2: all quoted values check")
