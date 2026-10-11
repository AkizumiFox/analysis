"""exr-epsilon-characterization-b3 (Ch 11, 04): A = {0}, B = [0, 1]: differences fill [-1, 0],
sup 0 = sup A - inf B, while sup A - sup B = -1."""
QUOTED = {"sup A - inf B": 0, "sup A - sup B": -1}
assert 0 - 0 == QUOTED["sup A - inf B"] and 0 - 1 == QUOTED["sup A - sup B"]
print("exr-epsilon-characterization-b3: all quoted values check")
