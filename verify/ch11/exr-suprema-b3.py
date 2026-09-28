"""exr-suprema-b3 (Ch 10, 02): for 1/2 <= M < 1, x = M/(1 - M) + 1 > 0 has x(1 - M) = 1 and
x/(x + 1) > M; x/(x + 1) < 1 for x > 0."""
from fractions import Fraction as F

QUOTED = {"sup": 1, "element": F(1, 2)}

for k in range(500, 1000):
    M = F(k, 1000)
    x = M / (1 - M) + 1
    assert x > 0 and x * (1 - M) == 1 and x / (x + 1) > M
for k in range(1, 5000):
    x = F(k, 100)
    assert x / (x + 1) < 1
assert F(1, 1 + 1) == F(1, 2)
print("exr-suprema-b3: all quoted values check")
