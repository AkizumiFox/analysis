"""The instance in exr-conjunction-implication-derivations-c1 (c), Section 1.2."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _grid import implies_on_grid

QUOTED = {"refuting value x": 0}
assert implies_on_grid(lambda x: x > 2 and x > 3, lambda x: x > 1)   # premise true everywhere
assert not QUOTED["refuting value x"] > 1                            # conclusion false at 0
print("exr-conjunction-implication-derivations-c1: checks")
