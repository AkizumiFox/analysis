"""exr-nested-intervals-a1 (Ch 10, 07): (b) I_2 = [2, 5/2], I_3 = [3, 10/3]; (e) for the list
0, 1, 2: I_1 = [1, 2], L = [1, 4/3], R = [5/3, 2], I_2 = [5/3, 2], then L = [5/3, 16/9],
R = [17/9, 2], I_3 = [5/3, 16/9]."""
from fractions import Fraction as F

QUOTED = {"I1": (F(1), F(2)), "L1": (F(1), F(4, 3)), "R1": (F(5, 3), F(2)), "I2": (F(5, 3), F(2)),
          "L2": (F(5, 3), F(16, 9)), "R2": (F(17, 9), F(2)), "I3": (F(5, 3), F(16, 9))}
assert (F(2), 2 + F(1, 2)) == (F(2), F(5, 2)) and (F(3), 3 + F(1, 3)) == (F(3), F(10, 3))
xs = [F(0), F(1), F(2)]
a, b = xs[0] + 1, xs[0] + 2
assert (a, b) == QUOTED["I1"]
for k, x in enumerate(xs[1:], start=1):
    d = b - a
    L, R = (a, a + d / 3), (b - d / 3, b)
    assert L == QUOTED[f"L{k}"] and R == QUOTED[f"R{k}"]
    a, b = L if not (L[0] <= x <= L[1]) else R
    assert (a, b) == QUOTED[f"I{k + 1}"] and not (a <= x <= b)
print("exr-nested-intervals-a1: all quoted values check")
