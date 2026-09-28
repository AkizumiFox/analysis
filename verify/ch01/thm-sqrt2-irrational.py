"""thm-sqrt2-irrational (Ch 1, Section 1.4): p = 2m and p^2 = 2q^2 give q^2 = 2m^2;
no p, q with p^2 = 2q^2 in a range; the example 2 = 4/2 (both even) of A1(d)."""
QUOTED = {"p^2 = 2q^2, p = 2m  =>  q^2": "2m^2", "A1(d) fraction": (4, 2)}

for m in range(-100, 101):
    for q in range(-100, 101):
        p = 2 * m
        if p * p == 2 * q * q:
            assert q * q == 2 * m * m
        # identity behind the step: (2m)^2 = 2q^2  <=>  q^2 = 2m^2
        assert ((2 * m) ** 2 == 2 * q * q) == (q * q == 2 * m * m)
for q in range(1, 2000):
    for p in range(0, 3 * q):
        assert p * p != 2 * q * q
p, q = QUOTED["A1(d) fraction"]
assert p == 2 * q and p % 2 == 0 and q % 2 == 0
print("thm-sqrt2-irrational: all quoted values check")
