"""exm-search-postpone-or (Ch 1 s07): the two rows quoted, validity, and why a classical step is used."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s06s07_logic import *  # noqa: E402,F401,F403
P, Q, R, S, N, G = V("P"), V("Q"), V("R"), V("S"), V("N"), V("G")

QUOTED = {
    "row1": {"P": True, "Q": True, "R": False, "premise": True, "P->R": False},
    "row2": {"P": True, "Q": False, "R": True, "premise": True, "P->Q": False},
    "derivation_lines_LEM_on_Q": 14,
}
prem = Imp(P, Or(Q, R))
goal = Or(Imp(P, Q), Imp(P, R))
r = QUOTED["row1"]; v = {k: r[k] for k in "PQR"}
assert tv(prem, v) == r["premise"] and tv(Imp(P, R), v) == r["P->R"]
r = QUOTED["row2"]; v = {k: r[k] for k in "PQR"}
assert tv(prem, v) == r["premise"] and tv(Imp(P, Q), v) == r["P->Q"]
assert classically_valid([prem], goal)
assert not classically_valid([prem], Imp(P, Q)) and not classically_valid([prem], Imp(P, R))
assert kripke_refutation([prem], goal) is not None   # no RAA-free derivation exists (not claimed in text)
print("exm-search-postpone-or: ok")
