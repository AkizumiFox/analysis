"""exm-sup-squares-epsilon (Ch 10, 04): h = min{1/2, eps/2}, x = 1 - h in [1/2, 1), and
x^2 > 1 - 2h >= 1 - eps."""
from fractions import Fraction as F
from _grid import eps_values

QUOTED = {"cap": F(1, 2)}
assert QUOTED["cap"] == F(1, 2)

for e in eps_values():
    h = min(F(1, 2), e / 2)
    x = 1 - h
    assert 0 < h <= F(1, 2) and F(1, 2) <= x < 1
    assert x * x == 1 - 2 * h + h * h > 1 - 2 * h >= 1 - e
print("exm-sup-squares-epsilon: all quoted values check")
