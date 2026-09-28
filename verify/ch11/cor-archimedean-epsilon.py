"""cor-archimedean-epsilon (Ch 10, 05): the Quick check: the least n with 1/n < 0.003 is 334
(1/333 = 0.003003... is too big); for 0.0003 it is 3334."""
from fractions import Fraction as F

QUOTED = {F(3, 1000): 334, F(3, 10000): 3334}
for e, n0 in QUOTED.items():
    n = 1
    while not F(1, n) < e:
        n += 1
    assert n == n0 and F(1, n0 - 1) >= e
assert F(1, 333) > F(3, 1000)
print("cor-archimedean-epsilon: all quoted values check")
