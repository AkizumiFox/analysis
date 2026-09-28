"""exr-reductio-and-classical-rules-b1 (Ch 1 s06): (a) holds without RAA; (b) is valid and uses RAA."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s06s07_logic import *  # noqa: E402,F401,F403
P, Q, R, S, N, G = V("P"), V("Q"), V("R"), V("S"), V("N"), V("G")

assert classically_valid([Not(Not(Not(P)))], Not(P))
assert kripke_refutation([Not(Not(Not(P)))], Not(P)) is None
b = ([Imp(Not(P), Q), Imp(Not(P), Not(Q))], P)
assert classically_valid(*b)
assert g3_refutation(*b) is not None     # RAA is genuinely needed in (b)
print("exr-reductio-and-classical-rules-b1: ok")
