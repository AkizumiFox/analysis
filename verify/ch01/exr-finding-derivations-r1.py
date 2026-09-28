"""exr-finding-derivations-r1 (Ch 1 s07): not(N or G) |- not N and (G -> S) is valid, and needs no RAA."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s06s07_logic import *  # noqa: E402,F401,F403
P, Q, R, S, N, G = V("P"), V("Q"), V("R"), V("S"), V("N"), V("G")

seq = ([Not(Or(N, G))], And(Not(N), Imp(G, S)))
assert classically_valid(*seq)
assert kripke_refutation(*seq) is None
print("exr-finding-derivations-r1: ok")
