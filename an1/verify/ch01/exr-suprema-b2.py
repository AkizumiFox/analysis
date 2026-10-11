"""exr-suprema-b2 (Ch 11, 02): s = 2 is not sup (0, 1): the upper bound M = 1 lies below it."""
QUOTED = {"s": 2, "M": 1}
assert QUOTED["M"] < QUOTED["s"]
print("exr-suprema-b2: all quoted values check")
