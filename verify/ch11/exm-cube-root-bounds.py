"""exm-cube-root-bounds (Ch 10, 06): 1.25^3 = 1.953125 < 2 < 2.000376 = 1.26^3."""
from fractions import Fraction as F

QUOTED = {"1.25^3": F("1.953125"), "1.26^3": F("2.000376")}
assert F("1.25") ** 3 == QUOTED["1.25^3"] < 2 < QUOTED["1.26^3"] == F("1.26") ** 3
print("exm-cube-root-bounds: all quoted values check")
