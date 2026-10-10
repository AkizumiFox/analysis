"""exr-inverses-c2 (Ch 6, Section 6.5): left inverses of f(k) = 2k, {1,2} -> {1,2,3,4}."""
from itertools import product
QUOTED = {"count": 4, "2^2": 4,
          "list": [(1, 1, 1, 2), (1, 1, 2, 2), (2, 1, 1, 2), (2, 1, 2, 2)]}
f = {1: 2, 2: 4}
lefts = sorted(v for v in product([1, 2], repeat=4) if all(v[f[x] - 1] == x for x in f))
assert lefts == QUOTED["list"] and len(lefts) == QUOTED["count"] == 2 ** 2
print("exr-inverses-c2: all quoted values check")
