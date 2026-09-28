"""exr-density-and-roots-c2 (Ch 10, 06): 2^k > k; m = floor(2^k x) + 1 gives x < m/2^k < y
once 1/k < y - x."""
from fractions import Fraction as F
import math

QUOTED = {"dyadic between any two reals": True}

for k in range(1, 200):
    assert 2 ** k > k
for x, y in [(F(0), F(1, 1000)), (F(-7, 3), F(-2)), (F(314, 100), F(3142, 1000))]:
    k = 1
    while not F(1, k) < y - x:
        k += 1
    m = math.floor(2 ** k * x) + 1
    assert x < F(m, 2 ** k) < y
print("exr-density-and-roots-c2: all quoted values check")
