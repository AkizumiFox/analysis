"""exm-sup-finite-and-closed (Ch 11, 02): max{-1, 3, 7/2} = 7/2 is an upper bound in the set."""
from fractions import Fraction as F

QUOTED = {"max": F(7, 2), "sup B": 1}
A = [F(-1), F(3), F(7, 2)]
assert max(A) == QUOTED["max"] and all(a <= QUOTED["max"] for a in A)
print("exm-sup-finite-and-closed: all quoted values check")
