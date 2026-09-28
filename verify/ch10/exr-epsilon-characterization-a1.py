"""exr-epsilon-characterization-a1 (Ch 10, 04): witnesses (a) max{0, 5 - eps/2} for [0, 5),
(c) max{3, 4 - eps/2} for (2, 4); (e) eps = 1/10: a = 24/25 > 19/20, b = 5,
a + b = 149/25 = 5.96 > 5.9."""
from fractions import Fraction as F
from _grid import eps_values

QUOTED = {"a": F(24, 25), "threshold": F(19, 20), "a+b": F(149, 25), "target": F(59, 10)}
for e in eps_values():
    a = max(F(0), 5 - e / 2)
    assert 0 <= a < 5 and a > 5 - e
    a = max(F(3), 4 - e / 2)
    assert 2 < a < 4 and a > 4 - e
e = F(1, 10)
assert 1 - e / 2 == QUOTED["threshold"] and 0 < QUOTED["a"] < 1 and QUOTED["a"] > QUOTED["threshold"]
assert 5 > 5 - e / 2
assert QUOTED["a"] + 5 == QUOTED["a+b"] == F(596, 100) > QUOTED["target"] == 1 + 5 - e
print("exr-epsilon-characterization-a1: all quoted values check")
