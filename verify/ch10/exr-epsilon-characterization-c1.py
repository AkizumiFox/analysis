"""exr-epsilon-characterization-c1 (Ch 10, 04): A = B = [-2, -1]: sup A sup B = 1, while
(-2)(-2) = 4 lies in AB."""
QUOTED = {"product of sups": 1, "element": 4}
assert (-1) * (-1) == QUOTED["product of sups"] and (-2) * (-2) == QUOTED["element"] > 1
print("exr-epsilon-characterization-c1: all quoted values check")
