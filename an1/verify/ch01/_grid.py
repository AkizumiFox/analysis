"""Shared helpers for the Chapter 10 sidecars: exact rational sample points and
rational functions R(x) with the leading-coefficient order."""
from fractions import Fraction as F


def grid(lo=-5, hi=5, den=12):
    """Every rational k/den in [lo, hi], plus points within 1e-9 of a few integers."""
    pts = {F(k, den) for k in range(lo * den, hi * den + 1)}
    for b in range(lo, hi + 1):
        for e in (F(1, 10**6), F(1, 10**9)):
            pts |= {F(b) - e, F(b) + e}
    return sorted(p for p in pts if lo <= p <= hi)


def eps_values():
    """A spread of positive epsilons, large and tiny."""
    return [F(k, 1) for k in (1, 2, 3, 10, 1000)] + [F(1, 10**j) for j in range(1, 10)] + [F(3, 7), F(5, 11)]


# ---- polynomials as coefficient lists [c0, c1, ...] with exact Fractions ----

def trim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p


def padd(p, q):
    n = max(len(p), len(q))
    return trim([(p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0) for i in range(n)])


def pneg(p):
    return [-c for c in p]


def pmul(p, q):
    if not p or not q:
        return []
    r = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i + j] += a * b
    return trim(r)


def lc(p):
    return trim(p)[-1]


class RF:
    """p/q in R(x); positive iff lc(p) and lc(q) have the same sign."""

    def __init__(self, p, q=(1,)):
        self.p, self.q = trim([F(c) for c in p]), trim([F(c) for c in q])
        assert self.q, "zero denominator"

    def __add__(self, o):
        return RF(padd(pmul(self.p, o.q), pmul(o.p, self.q)), pmul(self.q, o.q))

    def __neg__(self):
        return RF(pneg(self.p), self.q)

    def __sub__(self, o):
        return self + (-o)

    def __mul__(self, o):
        return RF(pmul(self.p, o.p), pmul(self.q, o.q))

    def inv(self):
        assert self.p
        return RF(self.q, self.p)

    def positive(self):
        return bool(self.p) and (lc(self.p) > 0) == (lc(self.q) > 0)

    def __lt__(self, o):
        return (o - self).positive()

    def __le__(self, o):
        d = o - self
        return (not d.p) or d.positive()

    def is_zero(self):
        return not self.p


X = RF([0, 1])


def const(c):
    return RF([c])
