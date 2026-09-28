"""exr-nested-intervals-b1 (Ch 10, 07): m_1 = 14 (196 <= 200 < 225), m_2 = 141
(19881 <= 20000 < 20164); the truncation intervals are nested for n <= 12 (integer square
roots of 2 * 10^(2n))."""
from math import isqrt

QUOTED = {"m1": 14, "m2": 141}
assert 14 ** 2 == 196 <= 200 < 225 == 15 ** 2 and 141 ** 2 == 19881 <= 20000 < 20164 == 142 ** 2
m = [None] + [isqrt(2 * 10 ** (2 * n)) for n in range(1, 13)]
assert m[1] == QUOTED["m1"] and m[2] == QUOTED["m2"]
for n in range(1, 12):
    assert 10 * m[n] <= m[n + 1] and m[n + 1] + 1 <= 10 * m[n] + 10
print("exr-nested-intervals-b1: all quoted values check")
