"""exr-finding-derivations-c2 (Ch 1 s07): the rows quoted in (b); validity; RAA/LEM not avoidable."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s06s07_logic import *  # noqa: E402,F401,F403
P, Q, R, S, N, G = V("P"), V("Q"), V("R"), V("S"), V("N"), V("G")

QUOTED = {"row_PQ_TF": {"P": True, "Q": False, "P->Q": False},
          "row_PQ_FT": {"P": False, "Q": True, "Q->P": False}}
goal = Or(Imp(P, Q), Imp(Q, P))
assert classically_valid([], goal)
r = QUOTED["row_PQ_TF"]; assert tv(Imp(P, Q), {"P": r["P"], "Q": r["Q"]}) == r["P->Q"]
r = QUOTED["row_PQ_FT"]; assert tv(Imp(Q, P), {"P": r["P"], "Q": r["Q"]}) == r["Q->P"]
assert kripke_refutation([], goal) is not None      # "stronger claim, which we do not prove"
print("exr-finding-derivations-c2: ok")
