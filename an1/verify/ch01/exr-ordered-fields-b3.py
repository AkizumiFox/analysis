"""exr-ordered-fields-b3 (Ch 11, 01): |2x - 3| < 5 iff -1 < x < 4; |x - 1| < |x + 1| iff x > 0."""
from fractions import Fraction as F
from _grid import grid

QUOTED = {"(a)": (-1, 4), "(b)": 0}
for x in grid(-6, 6, 24):
    assert (abs(2 * x - 3) < 5) == (QUOTED["(a)"][0] < x < QUOTED["(a)"][1])
    assert (abs(x - 1) < abs(x + 1)) == (x > QUOTED["(b)"])
print("exr-ordered-fields-b3: all quoted values check")
