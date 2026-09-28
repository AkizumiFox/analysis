"""exm-nonarchimedean-field (Ch 10, 05) and exr-archimedean-property-c2: in R(x) with the
leading-coefficient order, n < x and 1/x < 1/n for n in N; positivity does not depend on the
representation; the order axioms hold on a sample; lc(3 - 2x^2) = -2."""
from fractions import Fraction as F
from itertools import product
from _grid import RF, X, const, lc

QUOTED = {"lc(3 - 2x^2)": -2}
assert lc([3, 0, -2]) == QUOTED["lc(3 - 2x^2)"]
for n in range(1, 200):
    assert const(n) < X and X.inv() < const(n).inv() and X.inv().positive()
    # the M - 1 argument: x is an upper bound, and so is x - 1
    assert const(n) <= X - const(1)

polys = [[1], [-2], [0, 1], [1, -1], [3, 0, -2], [0, 0, 1], [-1, 2, 1], [5, 0, 0, -1]]
fs = [RF(p, q) for p in polys for q in polys]
# representation independence: multiply top and bottom by the same non-zero polynomial
for f in fs[:30]:
    for m in polys:
        g = RF([c for c in f.p], f.q)
        from _grid import pmul
        g2 = RF(pmul(f.p, [F(c) for c in m]), pmul(f.q, [F(c) for c in m]))
        assert g.positive() == g2.positive()
sample = fs[::5]
for f in sample:
    if not f.is_zero():
        assert f.positive() != (-f).positive()          # exactly one of f, -f positive
for f, g in product(sample, sample):
    if f.positive() and g.positive():
        assert (f * g).positive() and (f + g).positive()
for f, g, h in product(sample[:8], sample[:8], sample[:8]):
    if f < g and g < h:
        assert f < h
    if f < g:
        assert f + h < g + h
print("exm-nonarchimedean-field: all quoted values check")
