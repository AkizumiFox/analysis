"""exm-sup-one-minus-reciprocal-finished (Ch 11, 05): eps = 0.01 needs n > 100; n = 101 gives
1 - 1/101 = 100/101 > 0.99."""
from fractions import Fraction as F

QUOTED = {"n": 101, "element": F(100, 101)}
e = F(1, 100)
assert F(1, 100) >= e and F(1, QUOTED["n"]) < e
assert 1 - F(1, QUOTED["n"]) == QUOTED["element"] > F(99, 100)
print("exm-sup-one-minus-reciprocal-finished: all quoted values check")
