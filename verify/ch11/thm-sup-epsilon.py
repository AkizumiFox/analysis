"""thm-sup-epsilon (Ch 10, 04): the witness a = max{1/2, 1 - eps/2} for (0, 1): it lies in
(0, 1) and exceeds 1 - eps; eps = 1/10 gives 19/20; for eps = 1/1000, 19/20 is not above
999/1000."""
from fractions import Fraction as F
from _grid import eps_values

QUOTED = {"eps=1/10": F(19, 20), "eps=1/1000 bound": F(999, 1000)}
for e in eps_values():
    a = max(F(1, 2), 1 - e / 2)
    assert 0 < a < 1 and a > 1 - e
assert max(F(1, 2), 1 - F(1, 10) / 2) == QUOTED["eps=1/10"]
assert 1 - F(1, 1000) == QUOTED["eps=1/1000 bound"] and not QUOTED["eps=1/10"] > QUOTED["eps=1/1000 bound"]
print("thm-sup-epsilon: all quoted values check")
