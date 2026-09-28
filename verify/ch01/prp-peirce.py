"""prp-peirce (Ch 1 s07): valid; its RAA cannot be avoided (stated without proof in the text)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s06s07_logic import *  # noqa: E402,F401,F403
P, Q, R, S, N, G = V("P"), V("Q"), V("R"), V("S"), V("N"), V("G")

# The text states the RAA claim without proof and quotes no number, so QUOTED is empty.
# Internal witness (not in the text): a three-valued (Goedel G3) countermodel.
QUOTED = {}
G3_VALUES = {"P": Fraction(1, 2), "Q": Fraction(0)}
G3_LAW_VALUE = Fraction(1, 2)
law = Imp(Imp(Imp(P, Q), P), P)
assert classically_valid([], law)
v = G3_VALUES
assert g3(law, v) == G3_LAW_VALUE < 1
assert g3_refutation([], law) is not None
assert kripke_refutation([], law) is not None
print("prp-peirce: ok")
