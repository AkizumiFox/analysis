"""thm-triangle-inequality (Ch 11, 01): (a), (b) on a grid; the remark's
|1 + (-1)| = 0 < 2; equality in (a) iff xy >= 0 (also exr-ordered-fields-b2 (b))."""
from _grid import grid

QUOTED = {"remark": (0, 2)}
assert abs(1 + (-1)) == QUOTED["remark"][0] < QUOTED["remark"][1] == abs(1) + abs(-1)
G = grid(-3, 3, 6)
for x in G:
    for y in G:
        assert abs(x + y) <= abs(x) + abs(y)
        assert abs(abs(x) - abs(y)) <= abs(x - y)
        assert (abs(x + y) == abs(x) + abs(y)) == (x * y >= 0)
print("thm-triangle-inequality: all quoted values check")
