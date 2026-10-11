"""exr-nested-intervals-c4 (Ch 11, 07): g(x) = x^3 + x; the two expansions; with 0 <= s <= 1:
Case 1 h = (1 - g(s))/16 gives g(s + h) - g(s) <= 8h < 1 - g(s); Case 2 h = (g(s) - 1)/10 gives
0 < h < s/5, g(s) - g(s - h) <= 5h < g(s) - 1; g(0.68) = 0.994432, g(0.69) = 1.018509."""
from fractions import Fraction as F

g = lambda x: x ** 3 + x
QUOTED = {"g(0.68)": F("0.994432"), "g(0.69)": F("1.018509"), "0.68^3": F("0.314432"), "0.69^3": F("0.328509")}
for k in range(0, 1001):
    s = F(k, 1000)
    for h in [F(j, 97) for j in range(-97, 98)]:
        assert g(s + h) - g(s) == h * (3 * s * s + 3 * s * h + h * h + 1)
        assert g(s) - g(s - h) == h * (3 * s * s - 3 * s * h + h * h + 1)
    if g(s) < 1:
        h = (1 - g(s)) / 16
        assert 0 < h <= F(1, 16)
        assert g(s + h) - g(s) <= 8 * h == (1 - g(s)) / 2 < 1 - g(s) and s + h >= 0
    elif g(s) > 1:
        h = (g(s) - 1) / 10
        assert s > 0 and 0 < h < s / 5 < s and s ** 3 <= s
        assert g(s) - g(s - h) <= 5 * h == (g(s) - 1) / 2 < g(s) - 1
assert F("0.68") ** 3 == QUOTED["0.68^3"] and g(F("0.68")) == QUOTED["g(0.68)"] < 1
assert F("0.69") ** 3 == QUOTED["0.69^3"] and g(F("0.69")) == QUOTED["g(0.69)"] > 1
assert g(0) == 0 and g(1) == 2
print("exr-nested-intervals-c4: all quoted values check")
