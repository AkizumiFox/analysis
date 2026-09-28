"""School-algebra instances quoted around def-rules-implication and def-derivation (Section 1.2)."""
import sys, pathlib
from fractions import Fraction
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _grid import implies_on_grid

QUOTED = {"1.5": Fraction(3, 2), "refuting value x": 0}
h = QUOTED["1.5"]
assert h * h > 2 and h < 2            # sqrt(2) < 1.5 (as 1.5^2 = 2.25 > 2) and 1.5 < 2
assert implies_on_grid(lambda x: x > 2, lambda x: x**2 > 4)          # hook
assert implies_on_grid(lambda x: x > 3, lambda x: x**2 > 9)          # P -> Q
assert implies_on_grid(lambda x: x**2 > 9, lambda x: x**2 > 4)       # Q -> R
x0 = QUOTED["refuting value x"]
assert implies_on_grid(lambda x: x > 3, lambda x: x > 2)             # flawed derivation's premises
assert implies_on_grid(lambda x: x > 2, lambda x: x > 1)
assert not x0 > 1                                                    # its conclusion fails at 0
assert implies_on_grid(lambda x: x > 1, lambda x: x**2 > 1)          # warning
assert not x0**3 > 1
print("def-rules-implication: checks")
