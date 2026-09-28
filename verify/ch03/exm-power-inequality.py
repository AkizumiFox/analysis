"""exm-power-inequality (Ch 3, Section 3.2): 3^n >= 2n + 1, and the step's estimates."""
QUOTED = {"base": 3}

for n in range(1, 300):
    assert 3 ** n >= 2 * n + 1
    assert 3 * (2 * n + 1) == 6 * n + 3 and 6 * n + 3 >= 2 * n + 3 == 2 * (n + 1) + 1
assert 3 ** 1 == 2 * 1 + 1 == 3
print("exm-power-inequality: all quoted values check")
