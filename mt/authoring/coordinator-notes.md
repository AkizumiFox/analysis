
## MT.9 (ch13, S1 blueprint 2026-10-25)

- registry/plan-edges.yaml: MT.9 currently s [MT.7, MT.3], see [HA.2]. The blueprint uses MT.8 (weak L¹, layer-cake formula, Chebyshev, a.e.-convergent subsequence) in §§01, 03, 04: add **s MT.8** (MT.8 precedes MT.9 in the D4 order). MT.5 (ball volume, polar coordinates) is also used; MT.4 and MT.5 are in the s-closure via MT.7? check; if not, add see MT.5.
- HA.10 (branch, s [MT.7, FA.6, HA.3]): uses `thm-approx-identity-lebesgue-points` for a.e. Fourier inversion; suggest **s MT.9** (side may depend on main) or at least see MT.9.
- MT.11: reuses `lem-vitali-finite`, `thm-maximal-weak-11`, `thm-differentiation-regular-families` (Radon–Nikodym derivative as a limit); suggest MT.11 see MT.9 (or s).
- authoring/NOTATION.md rows to add: v_d ≔ m(B(0,1)); cB ≔ B(x, cr) for B = B(x,r); A_r f (ball average); Mf, M̃f (centred / uncentred Hardy–Littlewood maximal function); Leb(f) (Lebesgue set); D_E(x) (density of E at x).
- authoring/STATUS.md: MT.9 row → "S1 blueprint (mt/authoring/blueprints/ch13.md), D4 layout; old ch09.md moved there".
- Directory slug: `mt/src/ch13-lebesgue-differentiation/`.
