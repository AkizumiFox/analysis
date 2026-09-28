"""exr-epsilon-characterization-c3 (Ch 10, 04): A = B = (0, 1): a + b = 2 (the two suprema)
is not in A + B, since every element of A + B is < 2."""
from fractions import Fraction as F

QUOTED = {"a + b": 2}
for i in range(1, 50):
    for j in range(1, 50):
        assert F(i, 50) + F(j, 50) < QUOTED["a + b"]
print("exr-epsilon-characterization-c3: all quoted values check")
