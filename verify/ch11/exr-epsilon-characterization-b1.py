"""exr-epsilon-characterization-b1 (Ch 10, 04): x^2 < 4 on (-1, 2); h = min{1, eps/4},
x = 2 - h in [1, 2), x^2 > 4 - 4h >= 4 - eps."""
from fractions import Fraction as F
from _grid import eps_values

QUOTED = {"sup": 4, "cap": 1}

for k in range(-999, 2000):
    x = F(k, 1000)
    assert x * x < 4
for e in eps_values():
    h = min(F(1), e / 4)
    x = 2 - h
    assert 0 < h <= 1 and 1 <= x < 2 and x * x > 4 - 4 * h >= 4 - e
print("exr-epsilon-characterization-b1: all quoted values check")
