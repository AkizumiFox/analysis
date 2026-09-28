"""exr-nested-intervals-r4 (Ch 11, 07): |x - 1| + |x + 1| >= 2, with equality exactly on
[-1, 1]; (1 - x)(x + 1) = 1 - x^2; the squared form has cross term 2|x^2 - 1|."""
from _grid import grid

QUOTED = {"bound": 2, "equality set": (-1, 1)}

for x in grid(-5, 5, 24):
    t = abs(x - 1) + abs(x + 1)
    assert t >= 2 and (t == 2) == (-1 <= x <= 1)
    assert (1 - x) * (x + 1) == 1 - x * x and ((1 - x) * (x + 1) >= 0) == (-1 <= x <= 1)
    assert t * t == 2 * x * x + 2 + 2 * abs(x * x - 1)
print("exr-nested-intervals-r4: all quoted values check")
