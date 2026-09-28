"""thm-reals-uncountable (Ch 10, 07): the outer-thirds construction avoids x_n, is nested, and
L, R are disjoint; run on several finite lists (including adversarial ones that hit endpoints)."""
from fractions import Fraction as F
import random

QUOTED = {"construction avoids every x_n": True}

random.seed(10)


def run(xs):
    a, b = xs[0] + 1, xs[0] + 2
    assert not (a <= xs[0] <= b)
    out = [(a, b)]
    for x in xs[1:]:
        d = b - a
        L, R = (a, a + d / 3), (b - d / 3, b)
        assert L[1] < R[0]
        a, b = L if not (L[0] <= x <= L[1]) else R
        assert not (a <= x <= b) and out[-1][0] <= a < b <= out[-1][1]
        out.append((a, b))
    return out


for trial in range(200):
    xs = [F(random.randint(-50, 50), random.randint(1, 20)) for _ in range(12)]
    run(xs)
# adversarial: each x_{n+1} is an endpoint of the current L
xs, a, b = [F(0)], F(1), F(2)
for _ in range(12):
    xs.append(a + (b - a) / 3)
    a, b = run(xs)[-1]
print("thm-reals-uncountable: all quoted values check")
