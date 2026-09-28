"""exr-ordered-fields-c1 (Ch 11, 01): Z/3 admits no order satisfying (O1)-(O4); n*1 > 0 and
strictly increasing in Q (first 200 terms)."""
from itertools import permutations
from fractions import Fraction as F

QUOTED = {"1+1+1 mod 3": 0}
assert (1 + 1 + 1) % 3 == QUOTED["1+1+1 mod 3"]
E = [0, 1, 2]
found = False
for rank in permutations(E):
    lt = lambda u, v: rank[u] < rank[v]
    o3 = all(not lt(u, v) or lt((u + w) % 3, (v + w) % 3) for u in E for v in E for w in E)
    o4 = all(not (lt(0, u) and lt(0, v)) or lt(0, (u * v) % 3) for u in E for v in E)
    found |= o3 and o4
assert not found
s, prev = F(0), F(0)
for n in range(1, 201):
    s += 1
    assert s > 0 and s > prev
    prev = s
print("exr-ordered-fields-c1: all quoted values check")
