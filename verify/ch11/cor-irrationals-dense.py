"""cor-irrationals-dense (Ch 10, 06): the Quick check after it: 1.4143^2 = 2.00024449 > 2 and
1.4143 < 1.415; z = sqrt2 * 10^-7 lies in (0, 2 * 10^-7), below 10^-6 (using 1 < sqrt2 < 2)."""
from fractions import Fraction as F

QUOTED = {"1.4143^2": F("2.00024449")}
assert F("1.4143") ** 2 == QUOTED["1.4143^2"] > 2 and F("1.4143") < F("1.415")
assert 1 < 2 < 4 and 2 * F(1, 10**7) < F(1, 10**6)
print("cor-irrationals-dense: all quoted values check")
