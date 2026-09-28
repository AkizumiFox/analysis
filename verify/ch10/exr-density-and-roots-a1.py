"""exr-density-and-roots-a1 (Ch 10, 06): (f) Case 1 at s = 7/5: 2 - s^2 = 1/25, 4s + 2 = 38/5,
h = 1/190, s + h = 267/190, (267/190)^2 = 71289/36100 < 72200/36100 = 2, bound 1 + s^2/2 = 99/50."""
from fractions import Fraction as F

QUOTED = {"h": F(1, 190), "s+h": F(267, 190), "square": F(71289, 36100), "bound": F(99, 50)}
s = F(7, 5)
assert s * s == F(49, 25) < 2 and 2 - s * s == F(1, 25) and 4 * s + 2 == F(38, 5)
h = (2 - s * s) / (4 * s + 2)
assert h == QUOTED["h"] and s + h == QUOTED["s+h"]
assert (s + h) ** 2 == QUOTED["square"] < F(72200, 36100) == 2
assert 1 + s * s / 2 == QUOTED["bound"] < 2 and (s + h) ** 2 <= QUOTED["bound"]
assert 267 ** 2 == 71289 and 2 * 190 ** 2 == 72200
print("exr-density-and-roots-a1: all quoted values check")
