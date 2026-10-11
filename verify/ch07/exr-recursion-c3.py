"""exr-recursion-c3: Fibonacci identities (re-indexed form) for n <= 25 and the small cases."""
QUOTED = {"first": [0, 1, 1, 2, 3, 5, 8]}
F = [0, 1]
for n in range(80):
    F.append(F[n + 1] + F[n])
assert F[:7] == QUOTED["first"]
for n in range(26):
    assert F[2 * n + 1] == F[n] ** 2 + F[n + 1] ** 2
    assert F[2 * n + 2] == F[n + 1] * (F[n] + F[n + 2])
# quoted small cases
assert F[2] == 1 * (0 + 1) and F[4] == 3 == 1 * (1 + 2) and F[6] == 8 == 2 * (1 + 3)
assert F[1] == 0 + 1 and F[3] == 2 == 1 + 1 and F[5] == 5 == 1 + 4
print("ok")
