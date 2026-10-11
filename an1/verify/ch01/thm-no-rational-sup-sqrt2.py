"""thm-no-rational-sup-sqrt2 (Ch 11, 02): the two values of h, the bounds used in each case,
and the worked constants after the proof: s = 3/2 gives h = 1/12, s - h = 17/12,
(17/12)^2 = 289/144 = 2 + 1/144; s = 1 gives h = 1/6, s + h = 7/6, 49/36 < 2."""
from fractions import Fraction as F


def h1(s):
    return (2 - s * s) / (4 * s + 2)


def h2(s):
    return (s * s - 2) / (2 * s)


QUOTED = {"s=3/2": (F(1, 12), F(17, 12), F(289, 144)), "s=1": (F(1, 6), F(7, 6), F(49, 36)), "h1 max": F(1, 6)}

s = F(3, 2)
h, sh, sq = QUOTED["s=3/2"]
assert h2(s) == h and s - h == sh and sh * sh == sq == 2 + F(1, 144)
s = F(1)
h, sh, sq = QUOTED["s=1"]
assert h1(s) == h and s + h == sh and sh * sh == sq < 2

# Case 1 on rationals 1 <= s with s^2 < 2; Case 2 on rationals s > 0 with s^2 > 2
for k in range(1000, 1415):
    s = F(k, 1000)
    assert s * s < 2
    h = h1(s)
    assert 0 < h <= QUOTED["h1 max"] and h * h <= h
    assert (s + h) ** 2 <= s * s + h * (2 * s + 1) == 1 + s * s / 2 < 2
for k in list(range(1415, 3000)) + [100000]:
    s = F(k, 1000)
    assert s * s > 2
    h = h2(s)
    assert h > 0 and s - h == (s * s + 2) / (2 * s) > 0 and (s - h) ** 2 == 2 + h * h
print("thm-no-rational-sup-sqrt2: all quoted values check")
