"""exr-reductio-and-classical-rules-c2 (Ch 1 s06): the sequent is derivable (true conclusion);
the illegal step proves P or Q |- P, refuted by the row P false, Q true."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s06s07_logic import *  # noqa: E402,F401,F403
P, Q, R, S, N, G = V("P"), V("Q"), V("R"), V("S"), V("N"), V("G")

QUOTED = {"row": {"P": False, "Q": True}}
assert classically_valid([Not(And(Not(P), Not(Q)))], Or(P, Q))
v = QUOTED["row"]
assert tv(Or(P, Q), v) is True and tv(P, v) is False
print("exr-reductio-and-classical-rules-c2: ok")
