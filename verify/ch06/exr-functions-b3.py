"""exr-functions-b3 (Ch 6 Section 6.4): s(1) = 1, s(n) = n - 1; t(n) = n + 1."""

QUOTED = {"s(1) = s(2)": 1}

s = lambda n: 1 if n == 1 else n - 1
assert s(1) == s(2) == QUOTED["s(1) = s(2)"]
assert all(s(m + 1) == m for m in range(1, 200)) and all(s(n) >= 1 for n in range(1, 200))
t = lambda n: n + 1
assert all(t(n) >= 2 for n in range(1, 200))
print("exr-functions-b3: all quoted values check")
