"""exr-finding-derivations-b1 (Ch 1 s07): (b) the conjunct P needs RAA, not-Q does not."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s06s07_logic import *  # noqa: E402,F401,F403
P, Q, R, S, N, G = V("P"), V("Q"), V("R"), V("S"), V("N"), V("G")

QUOTED = {"g3_countermodel_for_P": {"P": Fraction(1, 2), "Q": Fraction(0)}, "lines_b": 15, "lines_c": 8}
prem = Not(Imp(P, Q))
assert classically_valid([prem], And(P, Not(Q)))
v = QUOTED["g3_countermodel_for_P"]
assert g3(prem, v) == 1 and g3(P, v) == Fraction(1, 2)
assert kripke_refutation([prem], Not(Q)) is None
assert classically_valid([And(P, Imp(Q, R))], Imp(Q, And(P, R)))
assert classically_valid([Imp(Not(P), Q)], Or(P, Q))
print("exr-finding-derivations-b1: ok")
