"""exr-finding-derivations-c3 (Ch 1 s07): (b) needs no RAA, (c) does."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s06s07_logic import *  # noqa: E402,F401,F403
P, Q, R, S, N, G = V("P"), V("Q"), V("R"), V("S"), V("N"), V("G")

b = ([Not(And(P, Q)), P], Not(Q))
c = ([Not(And(P, Not(Q))), P], Q)
assert classically_valid(*b) and classically_valid(*c)
assert kripke_refutation(*b) is None
assert g3_refutation(*c) is not None
print("exr-finding-derivations-c3: ok")
