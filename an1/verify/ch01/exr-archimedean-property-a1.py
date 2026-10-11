"""exr-archimedean-property-a1 (Ch 11, 05): [1/2, oo) is not inductive (0 is not in it, (N1));
[0, 10] is not (it contains 0, but 10 -> 11); N u {1/2} is not (1/2 -> 3/2, strictly between 1 and 2)."""
from fractions import Fraction as F

QUOTED = {"half": F(1, 2), "three halves": F(3, 2), "10 -> 11": (10, 11)}
assert QUOTED["half"] + 1 == QUOTED["three halves"] >= QUOTED["half"]
assert not 0 >= QUOTED["half"]  # 0 not in [1/2, oo)
assert 1 < QUOTED["three halves"] < 2 and 10 + 1 == 11 > 10 and 0 <= 0 <= 10
print("exr-archimedean-property-a1: all quoted values check")
