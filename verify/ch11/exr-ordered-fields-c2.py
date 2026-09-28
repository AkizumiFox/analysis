"""exr-ordered-fields-c2 (Ch 11, 01): max/min by the absolute-value formulas; the
inequality |max{a,b} - max{c,d}| <= max{|a-c|, |b-d|}."""
from _grid import grid

QUOTED = {"formulas and inequality hold": True}

G = grid(-2, 2, 3)
for a in G:
    for b in G:
        assert max(a, b) == (a + b + abs(a - b)) / 2
        assert min(a, b) == (a + b - abs(a - b)) / 2
H = grid(-2, 2, 2)
for a in H:
    for b in H:
        for c in H:
            for d in H:
                assert abs(max(a, b) - max(c, d)) <= max(abs(a - c), abs(b - d))
print("exr-ordered-fields-c2: all quoted values check")
