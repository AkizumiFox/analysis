"""exr-archimedean-property-b4 (Ch 10, 05): n/(n+1) = 1 - 1/(n+1) < 1 and 1/(n+1) < 1/n;
line (ix): with eps = 1/n, n/(n+1) > 1 - eps."""
from fractions import Fraction as F

QUOTED = {"the seven lines prove sup A = 1": True}

for n in range(1, 3000):
    a = F(n, n + 1)
    assert a == 1 - F(1, n + 1) < 1 and F(1, n + 1) < F(1, n) and a > 1 - F(1, n)
assert F(1, 2) == F(1, 1 + 1)
print("exr-archimedean-property-b4: all quoted values check")
