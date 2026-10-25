
## MT.9 (ch13, S1 blueprint 2026-10-25)

- registry/plan-edges.yaml: MT.9 currently s [MT.7, MT.3], see [HA.2]. The blueprint uses MT.8 (weak L¹, layer-cake formula, Chebyshev, a.e.-convergent subsequence) in §§01, 03, 04: add **s MT.8** (MT.8 precedes MT.9 in the D4 order). MT.5 (ball volume, polar coordinates) is also used; MT.4 and MT.5 are in the s-closure via MT.7? check; if not, add see MT.5.
- HA.10 (branch, s [MT.7, FA.6, HA.3]): uses `thm-approx-identity-lebesgue-points` for a.e. Fourier inversion; suggest **s MT.9** (side may depend on main) or at least see MT.9.
- MT.11: reuses `lem-vitali-finite`, `thm-maximal-weak-11`, `thm-differentiation-regular-families` (Radon–Nikodym derivative as a limit); suggest MT.11 see MT.9 (or s).
- authoring/NOTATION.md rows to add: v_d ≔ m(B(0,1)); cB ≔ B(x, cr) for B = B(x,r); A_r f (ball average); Mf, M̃f (centred / uncentred Hardy–Littlewood maximal function); Leb(f) (Lebesgue set); D_E(x) (density of E at x).
- authoring/STATUS.md: MT.9 row → "S1 blueprint (mt/authoring/blueprints/ch13.md), D4 layout; old ch09.md moved there".
- Directory slug: `mt/src/ch13-lebesgue-differentiation/`.

## ch15 (FA.6 Hilbert Spaces), S1 2026-10-25

- registry/plan-edges.yaml FA.6: add `b: [F2.4, FA.4]` with `scope: {F2.4: [FA.6 §4 thm-onb-exists], FA.4: [FA.6 §6 prop-weak-bounded]}`; optional `see: [AN2.6, AN2.2]` (Weierstrass for Legendre completeness; Banach fixed point in Lax–Milgram); both already reachable through FA.4 and FA.1a.
- registry/chapter-constraints.yaml FA.6: rule text says "Part IV (Chapter 49)"; now MT.7 (MT chapter 11 in the D4 order).
- MT.11 (mt ch16) blueprint: FA.6 now precedes it, so its "L² toolkit for L²(μ)" section becomes a recall of FA.6 thm-orthogonal-decomposition and thm-riesz-representation; add `s FA.6` (or `b FA.6`) to MT.11 in plan-edges.yaml.
- Adjoints, self-adjoint/unitary/normal classes moved from FA.6 to FA.9 (spec/08 D4); FA.6 keeps only rem-adjoint-preview and exr-riesz-representation-c2 (forms ↔ operators) for FA.9 to promote.
- Old blueprint fa/authoring/blueprints/ch07.md is superseded by mt/authoring/blueprints/ch15.md (not deleted; fa/ is another workflow's directory).
- NOTATION.md: confirm inner-product slot convention (blueprint assumes linear in the first slot); add ⇀, P_C/P_M, ℓ²(Γ), unordered sum.
- STATUS.md: row for MT ch15 FA.6 → "blueprint (S1)".

## FA.4 (ch09, S1 blueprint 2026-10-25)

- Old blueprint `fa/authoring/blueprints/ch05.md` was **copied** into `mt/authoring/blueprints/ch09.md` and rewritten (it lives outside `mt/`, so not moved). The coordinator may `git rm fa/authoring/blueprints/ch05.md` (or leave a pointer stub) when the fa/ directory is reorganized.
- registry/plan-edges.yaml: `FA.4: {s: [FA.1a, AN2.6], see: [HA.1]}` → add **s AN1.10** (trigonometric functions and eⁱᵗ for the Dirichlet kernel in §3; AN1.10 is not an s-ancestor via FA.1a or AN2.6). Optionally add see [FA.6, FA.13] (Hellinger–Toeplitz pointer).
- registry/statements.yaml: add `thm-open-mapping` (FA.4, thm), `thm-closed-graph` (FA.4, thm), `thm-divergent-fourier-series` (FA.4, thm), `cor-bounded-inverse` (FA.4, cor); edges `thm-open-mapping uses thm-baire`, `thm-closed-graph uses cor-bounded-inverse`, `thm-divergent-fourier-series uses thm-ubp`.
- Scope changes vs the old blueprint (no registry change needed, but record in chapter-constraints if wanted): dropped "Fourier coefficients of L¹ do not exhaust c₀" (needs MT.7 completeness of L¹; could go to HA.10 or FA.1b as an exercise) and Grothendieck's theorem on closed subspaces of Lᵖ (needs MT.7; could go to FA.10/FA.14 as optional). Weakly bounded ⇒ bounded (needs Hahn–Banach) is promised to FA.5.
- authoring/NOTATION.md rows: B_X (open unit ball), Γ(T) (graph), C(𝕋), D_N (Dirichlet kernel), L_N (Lebesgue constants).
- authoring/STATUS.md: FA.4 row → "S1 blueprint (mt/authoring/blueprints/ch09.md), D4 layout; MT ch09".
- Directory slug: `mt/src/ch09-baire-category-operators/`.
- FA.1a's (ch08) blueprint should provide, with labels: completeness by absolutely convergent series, B(X,Y) complete, finite-dimensional subspaces closed, Hölder for ℓᵖ with the equality case on finitely supported vectors, and (if possible) the Neumann series; FA.4 cites these.
