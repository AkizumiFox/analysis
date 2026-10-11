"""exr-nested-intervals-c3 (Ch 11, 07): in R(x), n < x/n and the intervals [n, x/n] are nested;
sample elements f are excluded from some I_n, as the degree argument predicts."""
from _grid import RF, X, const

QUOTED = {"nested, and no sample in every I_n": True}

for n in range(1, 60):
    I, J = (const(n), X * const(n).inv()), (const(n + 1), X * const(n + 1).inv())
    assert I[0] < I[1] and I[0] <= J[0] and J[1] <= I[1]
samples = [const(7), RF([1, 1], [1]), RF([0, 1], [2]), RF([0, 0, 1]), RF([0, 0, 0, 1], [1, 1]),
           RF([3, 5]), RF([0, 1], [1000]), RF([2, 1, 1], [1, 1]), RF([0, 1, 0, 1], [0, 0, 1])]
for f in samples:
    assert any(not (const(n) <= f and f <= X * const(n).inv()) for n in range(1, 2000))
print("exr-nested-intervals-c3: all quoted values check")
