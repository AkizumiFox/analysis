"""exr-negation-and-contradiction-a1 (Ch 1, Section 1.4): part (e), the sqrt(4) run:
p^2 = 4q^2 = 2(2q^2); p = 2k gives q^2 = k^2; r = 2 = 2/1 has q = 1 odd."""
QUOTED = {"r": (2, 1), "q": 1}

for k in range(-100, 101):
    for q in range(-100, 101):
        assert ((2 * k) ** 2 == 4 * q * q) == (q * q == k * k)
        assert 4 * q * q == 2 * (2 * q * q)
p, q = QUOTED["r"]
assert (p * p) == 4 * q * q and q == QUOTED["q"] and q % 2 == 1
print("exr-negation-and-contradiction-a1: all quoted values check")
