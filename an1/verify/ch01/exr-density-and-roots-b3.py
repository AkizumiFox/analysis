"""exr-density-and-roots-b3 (Ch 11, 06): 1.70^3 = 4.913 < 5 < 5.000211 = 1.71^3."""
from fractions import Fraction as F

QUOTED = {"1.70^3": F("4.913"), "1.71^3": F("5.000211")}
assert F("1.70") ** 3 == QUOTED["1.70^3"] < 5 < QUOTED["1.71^3"] == F("1.71") ** 3
print("exr-density-and-roots-b3: all quoted values check")
