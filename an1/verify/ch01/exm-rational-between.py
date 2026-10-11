"""exm-rational-between (Ch 11, 06): n = 12 is the least n with 1/n < 3/2 - sqrt 2
((17/12)^2 = 289/144 > 2, (31/22)^2 = 961/484 < 2); floor(12 sqrt 2) = 16 since
256 <= 288 < 289; m = 17 and sqrt 2 < 17/12 < 3/2."""
from fractions import Fraction as F

QUOTED = {"n": 12, "17/12 squared": F(289, 144), "31/22 squared": F(961, 484), "floor": 16, "m": 17}


def spacing_ok(n):      # 1/n < 3/2 - sqrt2  iff  sqrt2 < 3/2 - 1/n  iff  2 < (3/2 - 1/n)^2 (both positive)
    t = F(3, 2) - F(1, n)
    return t > 0 and t * t > 2


assert spacing_ok(12) and not any(spacing_ok(n) for n in range(1, 12))
assert (F(3, 2) - F(1, 12)) == F(17, 12) and F(17, 12) ** 2 == QUOTED["17/12 squared"] > 2
assert (F(3, 2) - F(1, 11)) == F(31, 22) and F(31, 22) ** 2 == QUOTED["31/22 squared"] < 2
assert 16 ** 2 == 256 <= 144 * 2 == 288 < 289 == 17 ** 2
assert QUOTED["m"] == QUOTED["floor"] + 1
assert F(17, 12) ** 2 > 2 and F(17, 12) < F(18, 12) == F(3, 2)
print("exm-rational-between: all quoted values check")
