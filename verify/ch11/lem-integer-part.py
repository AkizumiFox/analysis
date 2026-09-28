"""lem-integer-part (Ch 10, 06): floor(2.7) = 2 and floor(-2.7) = -3."""
from fractions import Fraction as F
import math

QUOTED = {F(27, 10): 2, F(-27, 10): -3}
for y, m in QUOTED.items():
    assert m <= y < m + 1 and math.floor(y) == m
print("lem-integer-part: all quoted values check")
