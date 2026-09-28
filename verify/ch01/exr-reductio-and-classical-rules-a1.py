"""exr-reductio-and-classical-rules-a1 (Ch 1 s06): 3 < 7/2 < 4; x^2 < 2x - 1 iff (x - 1)^2 < 0."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s06s07_logic import *  # noqa: E402,F401,F403
P, Q, R, S, N, G = V("P"), V("Q"), V("R"), V("S"), V("N"), V("G")

QUOTED = {"k": Fraction(7, 2)}
k = QUOTED["k"]
assert 2 * k == 7 and 3 < k < 4
# two quadratics that agree at three points are equal
for x in (Fraction(0), Fraction(1), Fraction(5, 2)):
    assert (x - 1) ** 2 == x**2 - 2 * x + 1
print("exr-reductio-and-classical-rules-a1: ok")
