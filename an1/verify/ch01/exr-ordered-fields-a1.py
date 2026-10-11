"""exr-ordered-fields-a1 (Ch 11, 01): (b) a = -2 < 1 = b but a^2 = 4 > 1; (c) |x| = max{x, -x}."""
from _grid import grid

QUOTED = {"(b)": (-2, 1, 4, 1)}
a, b, a2, b2 = QUOTED["(b)"]
assert a < b and a * a == a2 > b2 == b * b
for x in grid():
    assert abs(x) == max(x, -x)
print("exr-ordered-fields-a1: all quoted values check")
