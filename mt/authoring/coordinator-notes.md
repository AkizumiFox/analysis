
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

## MT.4 (ch05, S1 blueprint 2026-10-25)

- Old `ch04.md` (MT.4) was `git mv`ed to `ch05.md` and rewritten; the ch04 slot is free for MT.3.
- Labels of ch02–ch04 (MT.1–MT.3) are cited **in prose by chapter** only; convert to `@ref` once those blueprints freeze. Facts ch05 needs, with labels, from:
  - MT.1: Lebesgue measure on ℝᵈ for all d; translation **and reflection** invariance m(−E) = m(E); regularity (Lebesgue set = Borel set up to a null set; Borel f̃ = f a.e.); a non-measurable set; a non-Borel Lebesgue set (non-Borel subset of the Cantor set).
  - MT.2: Riemann ⇒ Lebesgue with equal integral on boxes of ℝᵈ; translation invariance of the integral.
  - HA.9 or MT.2: **Lebesgue's criterion on boxes of ℝᵈ** (not only ℝ), used by `thm-riemann-fubini-recovered`.
  - MT.3: algebra of sets (definition), σ-finite (definition), abstract MCT/DCT, simple-function approximation, ∫Σ = Σ∫ for g_k ≥ 0, completion and the lemma "completion-measurable f = measurable g a.e.", Carathéodory extension (named in one remark only). If MT.3 introduces π–λ or monotone classes, tell ch05 (it creates `thm-monotone-class` in §2).
- registry/plan-edges.yaml: `MT.4: {s: [MT.3, AN3.4], see: [HA.5]}` stays; optionally add `revisits: [AN2.12]` (double series as Fubini for counting measure) and `see: [HA.10]` (Fourier inversion moved there from the old §7; HA.10 should list it, s MT.4 via MT.7 is already in its closure).
- MT.5 (ch06): ch05 no longer does |x|^{−α} or the ball volume (left to MT.5); ch05 §7 B1 computes ∫e^{−x²} without polar coordinates — MT.5 may cite it as the first route.
- MT.8 (ch12) and MT.9 (ch13): `thm-layer-cake` is proved in ch05 §7 (MT.9's note says it uses MT.8's layer-cake formula — cite ch05's instead, or MT.8 recalls it).
- MT.7 (ch11): `thm-convolution-l1`, `lem-convolution-measurable` are in ch05 §7; MT.7 starts from them.
- MT.10 (ch14): ch05 §4 C1 proves integration by parts for F = ∫f, G = ∫g (exercise; promote if MT.10 needs it as a theorem).
- authoring/NOTATION.md rows: 𝒮 ⊗ 𝒯; μ × ν; sections E_x, E^y, f_x, f^y; completion (μ × ν)‾; f ∗ g.
- authoring/STATUS.md: MT.4 row → "S1 blueprint (mt/authoring/blueprints/ch05.md), D4 layout; old ch04.md moved there". Directory slug `mt/src/ch05-product-measures-fubini/`.
- exam-targets: no change; ch05 serves mira "MIRA 5", real-ntu "Fubini–Tonelli", apostol-ma/pugh deferred_cover.

## FA.3 (ch10, S1 blueprint 2026-10-25)

- Old blueprint `fa/authoring/blueprints/ch04.md` was **copied** into `mt/authoring/blueprints/ch10.md` and rewritten (outside `mt/`, so not moved); the coordinator may `git rm` it when fa/ is reorganized.
- Zorn is **cited** from F2.4 (`thm-zorn`), no longer proved here (old stub's "prove Zorn just in time" dropped; matches registry `b: [F2.4]`).
- registry/plan-edges.yaml FA.3 (now `{s: [FA.1a], b: [F2.4], revisits: [MA.18], …}`): add **b FA.4** (scope `thm-ubp`, for `cor-weakly-bounded` in §03), **b MT.2** and **see MT.1** (§05 invariant mean on the circle extends the Lebesgue integral; contrast with MT.1's non-measurable set), **see AN2.9, AN2.10** (optional §06, Riesz on C[a,b] via Stieltjes). All precede FA.3 in the D4 order.
- Weakly bounded ⇒ bounded: FA.4's blueprint promises it to FA.5 and FA.6 has `prop-weak-bounded`; FA.3 (ch10) now proves it as `cor-weakly-bounded`, so FA.5/FA.6 can cite it instead (FA.6 then needs b FA.3 or keeps its own proof).
- registry/statements.yaml: add `thm-hb-complex`, `thm-hb-normed`, `cor-hb-distance`, `thm-dense-criterion`, `thm-bidual-isometry`, `thm-adjoint-norm`, `prp-adjoint-kernel-range`, `thm-hb-geometric-strict`, `cor-closed-convex-halfspaces`, `thm-banach-limit`, `cor-linfty-dual-not-l1`, `thm-invariant-mean-circle`, `cor-finitely-additive-measure` (FA.3); edges `thm-hb-geometric uses thm-hb-analytic`, `cor-hb-norming uses thm-hb-normed`, `thm-banach-limit uses thm-hb-analytic`, `cor-weakly-bounded uses thm-ubp`.
- authoring/NOTATION.md rows: X* (dual; reconcile with FA.1a), X**, J_X, M^⊥ and ⊥N (annihilators; FA.6 reuses M^⊥ for the orthogonal complement), T' (Banach adjoint; T* kept for FA.9), p_C (Minkowski gauge), S (left shift on ℓ^∞), f_a (translate).
- Promises opened: (L^∞)* ≠ L¹ → MT.7 (ch11) or FA.1b; Mazur → FA.5; Hilbert uniqueness of norm-preserving extension → FA.6; X* separable ⇒ X separable → FA.10; normalization of the representing g → FA.2. Paid: FA.1a's "(ℓ^∞)* needs Hahn–Banach".
- FA.1a (ch08) blueprint should label: X* is Banach; (ℓᵖ)* = ℓ^q, c₀* = ℓ¹, (ℓ¹)* = ℓ^∞; quotient norm and completeness of X/M; BLT extension; Hölder for ℓ². FA.3 cites these descriptively until the labels exist.
- authoring/STATUS.md: FA.3 row → "S1 blueprint (mt/authoring/blueprints/ch10.md), D4 layout; MT ch10". Directory slug `mt/src/ch10-hahn-banach/`.

## ch08 (FA.1a Banach Spaces, Bounded Operators, and Dual Spaces), S1 2026-10-25

- Blueprint: mt/authoring/blueprints/ch08.md (new file). The old FA.1a blueprint fa/authoring/blueprints/ch01.md is superseded (copied, not moved: fa/ is outside this workflow); retire it. Its L^p-duality sections belong to FA.1b (mt ch17).
- registry/plan-edges.yaml FA.1a (currently `s: [AN2.2, AN2.3, LA1.2], see: [AN3.1]`): add `see: [F2.4]` (Hamel basis, only prp-discontinuous-functional-exists, off every later proof path) and `see: [HA.9]` (step-function integral example). Confirm AN1.8, AN1.9, AN1.10, AN2.11 are in the s-closure (used in examples and Young's inequality); if not, add them as see. AN2.9/AN2.10 are used only in one example (Stieltjes functionals): see at most.
- AN2.2/AN2.3 have no labels yet (old-layout blueprints). ch08 writes expected names in brackets ([AN2.2 thm-cauchy-subsequence-converges], [AN2.3 thm-norms-equivalent], AN2.3 metric Tietze with bound, AN2.2 completion); S2a/S3 must replace them once those chapters are re-blueprinted.
- authoring/NOTATION.md rows: \nK (scalar field ℝ or ℂ); c_0, c, c_{00}, e_n (from n = 1); p' dual exponent (MT.7 and FA.1b should use p' too); \mathcal B(X,Y), \mathcal B(X); X^*, X^{**}; J canonical embedding; X/M, π, ‖x + M‖; T^* Banach adjoint (FA.9 relates it to the Hilbert adjoint); R, L shifts; M_a multiplication operator; V, V_k Volterra operators; sgn z = z/|z|.
- authoring/STATUS.md: MT ch08 FA.1a row → "S1 blueprint (mt/authoring/blueprints/ch08.md), D4 layout".
- Directory slug: `mt/src/ch08-banach-spaces/`.
- Promises opened for other chapters: FA.3 ((ℓ^∞)* ≠ ℓ¹; J isometric; ‖T*‖ = ‖T‖), FA.1b ((L^p)* = L^{p'}), FA.2 (Riesz on C[a,b]), MT.7 (completion of (C[0,1], ‖·‖₁) is L¹), FA.4 (no countable Hamel basis), FA.6 (θ = 1 in Riesz's lemma).
