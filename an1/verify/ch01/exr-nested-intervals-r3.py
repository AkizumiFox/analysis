"""exr-nested-intervals-r3 (Ch 11, 07): (sqrt2 + sqrt3)^2 = 5 + 2 sqrt6, computed exactly in the
basis 1, sqrt2, sqrt3, sqrt6 of Q(sqrt2, sqrt3); and (sqrt2 sqrt3)^2 = 6."""
from fractions import Fraction as F

QUOTED = {"r^2 = 5 + 2 sqrt6": (5, 2), "sqrt2 sqrt3 squared": 6}

# element = dict basis -> coefficient; basis labels are square-free products of {2, 3}
MUL = {(1, 1): (1, 1), (1, 2): (1, 2), (1, 3): (1, 3), (1, 6): (1, 6),
       (2, 2): (2, 1), (2, 3): (1, 6), (2, 6): (2, 3), (3, 3): (3, 1), (3, 6): (3, 2), (6, 6): (6, 1)}


def mul(u, v):
    out = {}
    for a, x in u.items():
        for b, y in v.items():
            c, basis = MUL[tuple(sorted((a, b)))]
            out[basis] = out.get(basis, 0) + c * x * y
    return {k: w for k, w in out.items() if w}


r = {2: F(1), 3: F(1)}
assert mul(r, r) == {1: 5, 6: 2}
assert mul(mul({2: 1}, {3: 1}), mul({2: 1}, {3: 1})) == {1: 6}
print("exr-nested-intervals-r3: all quoted values check")
