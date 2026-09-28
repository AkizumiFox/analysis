"""prp-de-morgan (Ch 1 s06): the rows quoted in the Idea, the four laws, and which need RAA."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s06s07_logic import *  # noqa: E402,F401,F403
P, Q, R, S, N, G = V("P"), V("Q"), V("R"), V("S"), V("N"), V("G")

QUOTED = {
    # Idea of (d): with P true, Q false the premise is true and not-P false; symmetric row.
    "row_P_true_Q_false": {"premise": True, "notP": False},
    "row_P_false_Q_true": {"premise": True, "notQ": False},
    # proof: (a)-(c) derived without RAA, (d) with RAA
    "raa_free": ["a", "b", "c"],
}
prem = Not(And(P, Q))
v = {"P": True, "Q": False}
assert tv(prem, v) == QUOTED["row_P_true_Q_false"]["premise"]
assert tv(Not(P), v) == QUOTED["row_P_true_Q_false"]["notP"]
v = {"P": False, "Q": True}
assert tv(prem, v) == QUOTED["row_P_false_Q_true"]["premise"]
assert tv(Not(Q), v) == QUOTED["row_P_false_Q_true"]["notQ"]
laws = {
    "a": ([Not(Or(P, Q))], And(Not(P), Not(Q))),
    "b": ([And(Not(P), Not(Q))], Not(Or(P, Q))),
    "c": ([Or(Not(P), Not(Q))], Not(And(P, Q))),
    "d": ([Not(And(P, Q))], Or(Not(P), Not(Q))),
}
for k, (pr, c) in laws.items():
    assert classically_valid(pr, c), k
    km = kripke_refutation(pr, c)
    if k in QUOTED["raa_free"]:
        assert km is None, (k, km)          # consistent with the RAA-free derivations
    else:
        assert km is not None               # (d): "no derivation avoids RAA" (stated, not proved)
# neither disjunct of (d) follows from the premise alone (Idea; A1(e))
assert not classically_valid([prem], Not(P)) and not classically_valid([prem], Not(Q))
print("prp-de-morgan: ok")
