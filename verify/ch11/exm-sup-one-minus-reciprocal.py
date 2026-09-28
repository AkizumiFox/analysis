"""exm-sup-one-minus-reciprocal (Ch 10, 02): A = {0, 1/2, 2/3, 3/4, ...}; 1 - 1/n < 1 and
strictly increasing in n."""
from fractions import Fraction as F

QUOTED = {"first terms": (0, F(1, 2), F(2, 3), F(3, 4))}
assert tuple(1 - F(1, n) for n in range(1, 5)) == QUOTED["first terms"]
for n in range(1, 5000):
    assert 1 - F(1, n) < 1 - F(1, n + 1) < 1
print("exm-sup-one-minus-reciprocal: all quoted values check")
