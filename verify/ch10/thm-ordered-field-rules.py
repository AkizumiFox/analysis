"""thm-ordered-field-rules (Ch 10, 01): the warning's witness a = c = -3, b = d = -1
(ac = 9 > 1 = bd); rules (c)-(h) spot-checked on a grid; the Quick check that Z/2 admits no
order (brute force over all strict total orders on {0, 1} checking (O3) and (O4))."""
from fractions import Fraction as F
from itertools import permutations
from _grid import grid

QUOTED = {"warning": (-3, -1, -3, -1, 9, 1)}

a, b, c, d, ac, bd = QUOTED["warning"]
assert a <= b and c <= d and a * c == ac and b * d == bd and ac > bd

G = grid(-3, 3, 4)
for x in G:
    if x != 0:
        assert x * x > 0
    for y in G:
        if x < y:
            assert x < (x + y) / 2 < y                          # (h)
            if x > 0:
                assert 0 < 1 / y < 1 / x                        # (f)
            if x >= 0:
                assert x * x < y * y                            # (g)
assert 1 > 0


def orders_ok(elements, add, mul):
    """Is there a strict total order (a ranking) satisfying (O3) and (O4)?"""
    for rank in permutations(range(len(elements))):
        lt = lambda u, v: rank[u] < rank[v]
        o3 = all(not lt(u, v) or lt(add(u, w), add(v, w)) for u in elements for v in elements for w in elements)
        o4 = all(not (lt(0, u) and lt(0, v)) or lt(0, mul(u, v)) for u in elements for v in elements)
        if o3 and o4:
            return True
    return False


assert not orders_ok([0, 1], lambda u, v: (u + v) % 2, lambda u, v: (u * v) % 2)
print("thm-ordered-field-rules: all quoted values check")
