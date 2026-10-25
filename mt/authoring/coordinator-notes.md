
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

## MT.10 (ch14, S1 blueprint 2026-10-25)

- Old `mt/authoring/blueprints/ch10.md` (ab:52 stub) was `git mv`'d to ch14.md (commit f195786) and rewritten.
- registry/plan-edges.yaml: `MT.10: {s: [MT.9], revisits: [AN2.9]}` is sufficient. The chapter uses MT.3 (Lebesgue–Stieltjes μ_F, §5) and MT.2/MT.1, all in MT.9's s-closure. If MT.9 gains s MT.8 (see MT.9 note), nothing changes here. Optional: add `see: [HA.9]` (the Volterra hook is paid in §4, `exm-volterra-paid`; HA.9 is already an s-ancestor via MT.1).
- MT.9 (ch13) lists `thm-vitali-covering-fine` as used by MT.10 for Lebesgue's monotone theorem. MT.10's main route is rising sun + saltus split + `lem-vitali-finite`; the fine-cover theorem appears in an "Alternatively" paragraph and in §3 C3. MT.9's wording "(MT.10, which uses this chapter's fine-cover theorem)" stays true but could say "as an alternative route".
- AN2.9 is a revisit, not an s-ancestor: §1 restates BV / total variation / Jordan decomposition and re-proves Jordan in one paragraph. If the AN2.9 blueprint fixes label names, MT.10 prose-points to them only.
- MT.11 (ch16): pays MT.10's hook (decomposition of increasing F ↔ Lebesgue decomposition of μ_F; density F′). Suggest MT.11 cite `thm-decomposition-increasing`, `thm-ac-iff-measure-ac`, `thm-singular-iff-concentrated` (edge MT.11 see MT.10 already registered).
- PDE.4 (s MT.10): cites `def-absolutely-continuous`, `thm-ftc-lebesgue`, `thm-ac-parts`.
- registry/statements.yaml candidates: `thm-lebesgue-monotone`, `thm-ftc-lebesgue`, `thm-banach-zarecki`, `thm-ftc-everywhere-differentiable`, `thm-decomposition-increasing`, `thm-arc-length-ac` (MT.10); edges `thm-ftc-lebesgue uses cor-indefinite-integral-derivative`, `thm-jump-derivative-zero uses lem-vitali-finite`.
- authoring/NOTATION.md rows: D⁺F, D₊F, D⁻F, D₋F (Dini derivatives); Mν (maximal function of a finite measure on ℝ); AC[a,b]; c (the Cantor function) and μ_c (Cantor measure) if not fixed earlier; T_a^b(F) if AN2.9 does not add it.
- authoring/STATUS.md: MT.10 row → "S1 blueprint (mt/authoring/blueprints/ch14.md), D4 layout; MT ch14".
- Directory slug: `mt/src/ch14-bv-absolute-continuity/`.

## ch07 (MT.6 Surfaces, Surface Measure, and the Divergence Theorem), S1 2026-10-25

- Old mt/authoring/blueprints/ch06.md (MT.6) was git-mv'd to ch07.md (commit f22c80e) and rewritten there.
- Exam targets: no item in registry/exam-targets.yaml lists MT.6 (`mira` omits it; spec/08 D4 keeps it in place). Its consumers are PDE.1 (s), PDE.5 (s), CA.2 see, CA.6 see. No registry change needed; record in report.md if a "main-line chapter with no exam-target item" list exists.
- registry/plan-edges.yaml MT.6 = s [MT.5, AN3.2, LA2.7, LA3.11], revisits [AN3.7]: unchanged. Optional: add `see: [AM.1]` (§04 re-proves a compact-case smooth partition of unity that AM.1 also proves; no proof cites AM).
- Label coordination across books: MT.6 keeps `thm-green` (moved from AN3.4) and creates `thm-smooth-partition-compact`, `lem-smooth-bump`; AM's AN3.7/AM.1 S1 should use different labels (e.g. derive Green as a Stokes corollary under its own label, or cite MT forward only in prose).
- MT.5 (ch06) S1 must: define σ on S^{d−1} by σ(E) = d·m({rω : 0 < r ≤ 1, ω ∈ E}) (or tell ch07, whose `thm-sphere-measure-agrees` depends on that normalization); state the polar formula, |B₁|, ∫e^{−|x|²} = π^{d/2}, and |x|^{−α} ∈ L¹(B₁) iff α < d.
- MT.2 (ch03) S1: if it creates differentiation under the integral sign (DCT corollary), ch07 §06 cites it; otherwise ch07 proves the case it needs (`lem-differentiate-sphere-average`).
- MT.7 (ch11) may cite `lem-smooth-bump` (MT.6 §04) for mollifiers instead of rebuilding e^{−1/t}.
- authoring/NOTATION.md rows to add: σ_M / σ (surface measure), J_φ (area element √det(DφᵀDφ)), ν (outward unit normal), ∂_ν u = ∇u·ν, C¹(Ω̄) = restrictions of C¹ functions on an open neighbourhood of Ω̄, ⨍ (average), Φ (fundamental solution of Laplace), ∮_{∂Ω}(P dx + Q dy) := ∫_{∂Ω}(P, Q)·τ dσ with τ = (−ν₂, ν₁).
- authoring/STATUS.md: MT.6 row → "S1 blueprint (mt/authoring/blueprints/ch07.md), D4 layout; directory `mt/src/ch07-surfaces-divergence-theorem/`". Promises paid: AN3.4 → Green (`thm-green`); MT.5 → surface measure (`def-surface-measure`, `thm-sphere-measure-agrees`). Promises opened: PDE.1 (−ΔΦ = δ), PDE.5 (traces on C¹ domains).
- an3/authoring/blueprints/ch04.md still says "Green's theorem has moved to surfaces-divergence-theorem in Part IV": update the pointer to MT.6 (MT chapter 7) when an3 is re-blueprinted.

## MT.11 (ch16, S1 blueprint 2026-10-25)

- registry/plan-edges.yaml: MT.11 is s [MT.3, MT.7], see [MT.10]. The blueprint needs **s [MT.3, MT.7, FA.6, MT.9, MT.10]**: FA.6 `thm-riesz-representation` for von Neumann's proof (the old in-chapter L² toolkit is dropped, since FA.6 now precedes MT.11 in the D4 order); MT.9 `lem-vitali-finite`, `thm-differentiation-regular-families` for differentiation of measures; MT.10 `thm-ac-iff-measure-ac`, `thm-decomposition-increasing`, `thm-jordan-decomposition-recalled`, `thm-ftc-lebesgue` for the NBV section. Also uses MT.2 (MCT/DCT) and AN1.3 (rearrangements), both in the s-closure.
- registry/exam-targets.yaml: the Axler MIRA target currently carries `id: algebra-harvard` (looks like a mis-paste; spec/08 §E1 calls it `mira`). Please check.
- Old design note decisions.md 9 ("L² facts proved concretely in MT.11, recalled in Part VI") is superseded by the D4 order; mark it superseded.
- MT.3 (old ch03, not yet rewritten): MT.11 §6 needs outer regularity of locally finite Borel measures on ℝᵈ (not only Lebesgue–Stieltjes measures on ℝ). If MT.3's rewrite does not prove it, MT.11 states outer regularity as a hypothesis (as now written); flag to the MT.3 S1 author.
- MT.10 (ch14): `lem-variation-right-continuous` (T_F right-continuous when F is) and "F AC ⇒ T_F AC" are used by MT.11 §6; if MT.10 does not prove them, MT.11 proves them in a paragraph each (already allowed for in the blueprint).
- MT.1/MT.2: Borel–Cantelli is proved inline in MT.11 §4 unless an earlier chapter labels it.
- authoring/NOTATION.md rows to add: ν⁺, ν⁻, |ν|; ν ≪ μ, ν ⊥ μ; dν/dμ, dν = f dμ; M(X), ‖ν‖ = |ν|(X); NBV; μ_F for F ∈ NBV (extends MT.3's increasing case); F_ac, F_sc, F_pp.
- authoring/STATUS.md: MT.11 row → "S1 blueprint (mt/authoring/blueprints/ch16.md), D4 layout; old ch11.md moved there".
- Directory slug: `mt/src/ch16-signed-measures-radon-nikodym/`.

## MT.7 (ch11, S1 blueprint 2026-10-25)

- Old `ch07.md` (MT.7) was `git mv`ed to `ch11.md` (commit bf11c1d) and rewritten. Directory slug `mt/src/ch11-lp-spaces/`.
- registry/plan-edges.yaml: `MT.7: {s: [MT.2, MT.4], see: [HA.2, LA3.11]}` → add **s FA.1a** (absolutely-summable-series test for completeness, ℓᵖ and (ℓᵖ)* ≅ ℓ^{p′}, dual norm) and **see FA.3** (one remark). MT.5 is used only in two flagged exercises (`exr-approximate-identities-c2`, `-r2`); no edge needed (MT.5 precedes in D4 order; optionally see MT.5).
- registry/statements.yaml: split row `thm-holder-minkowski` (MT.7) into `thm-holder` and `thm-minkowski`; `def-lp`, `thm-riesz-fischer` keep their labels. Suggested new rows: `thm-norming-formula`, `thm-minkowski-integral`, `thm-young-convolution`, `thm-approximate-identity-lp`, `thm-cc-infinity-dense`.
- Scope moved out: old §7 (L²(𝕋) completes ℛ(𝕋), Parseval for all of L²(𝕋), Fejér in L¹, uniqueness for L¹(𝕋)) goes to **HA.10** (side; main line may not depend on it). MT.7 adds `cor-periodic-continuous-dense` (continuous periodic functions dense in Lᵖ[−π, π]) so that **FA.6 `thm-trig-onb` must prove completeness of the trigonometric system itself** (AN2.6 trigonometric Weierstrass + this corollary); ch15's "revisits MT.7 … L²(𝕋) and the trigonometric system complete" should be reworded accordingly.
- Labels agreed with neighbours: `def-approximate-identity` and K_ε are created here (ch13 item 7 confirmed); `@def-convolution`, `@thm-convolution-l1`, `@lem-convolution-measurable`, `@thm-tonelli`, `@thm-fubini` are ch05's and are cited, not re-created. MT.9 pays `rem-pointwise-later`; FA.1b pays `rem-duality-later`; FA.6 pays `rem-l2-inner-product`; MT.8 pays the weak-Lᵖ hook (x^{−1/p}) and reuses `exm-typewriter-lp`, `exm-escaping-bump`.
- Needs from earlier rewritten blueprints (S2a will check): MT.1 inner regularity by compacts, dyadic-cube decomposition of open sets, dilation invariance m(λE) = λᵈm(E); MT.2 absolute continuity of the integral, simple-function approximation, L¹ density/translation facts; HA.9 the L²-Cauchy step-function sequence with no Riemann limit; FA.1a the series test (label); whether AN1/AN2 already prove e^{−1/t} is C^∞ (`lem-smooth-cutoff-function` becomes a recall if so).
- authoring/NOTATION.md rows: ‖f‖_p, ‖f‖_∞ (ess sup); p′ (conjugate exponent); ℒᵖ(μ) vs Lᵖ(μ); τ_h f(x) = f(x − h); K_ε(x) = ε^{−d}K(x/ε); η, η_ε (standard mollifier); L¹_loc; C_c^k, C_c^∞, C₀; sgn z = z/|z| (0 at 0).
- authoring/STATUS.md: MT.7 row → "S1 blueprint (mt/authoring/blueprints/ch11.md), D4 layout; MT ch11".
- exam-targets: no change; ch11 serves mira "MIRA 7" (with MT.8), real-ntu "Lᵖ、Hölder、Minkowski、Riesz–Fischer", apostol-ma / pma deferred_cover (Apostol 10, PMA 11 L² part).

## MT.3 (ch04, S1 blueprint 2026-10-25)

- Old `ch03.md` (MT.3) was `git mv`ed to `ch04.md` and rewritten; the ch03 slot is free for MT.2.
- Directory slug: `mt/src/ch04-abstract-measure/`.
- authoring/STATUS.md: MT.3 row → "S1 blueprint (mt/authoring/blueprints/ch04.md), D4 layout; MT ch04".
- registry/plan-edges.yaml: `MT.3: {s: [MT.2]}` → add `see: [AN2.10]` (§05 hook and §06 `thm-stieltjes-agrees` compare with the Riemann–Stieltjes integral). AN2.1, AN1.4, F2.3 are used directly; confirm they are in the s-closure of MT.2 (via MT.1/HA.9), else add see edges.
- registry/statements.yaml (suggested): `thm-caratheodory` (MT.3, thm), `thm-caratheodory-extension` (MT.3, thm), `thm-pi-lambda` (MT.3, thm), `thm-uniqueness-pi` (MT.3, thm), `thm-metric-outer-borel` (MT.3, thm), `thm-lebesgue-stieltjes` (MT.3, thm), `thm-translation-invariant-unique` (MT.3, thm); edges `thm-caratheodory-extension uses thm-caratheodory`, `thm-uniqueness-pi uses thm-pi-lambda`, `thm-lebesgue-stieltjes uses thm-caratheodory-extension, thm-uniqueness-pi`.
- **Division of labour with MT.4 (ch05):** MT.3 proves π-λ (`thm-pi-lambda`, `thm-uniqueness-pi`); MT.4 keeps `thm-monotone-class` (MT.3 only forward-points). MT.3 adds `lem-completion-measurable-function` which MT.4 asked for, and supplies abstract MCT/DCT, ∫Σ = Σ∫ (`thm-additivity-abstract`), `thm-simple-approximation-abstract`, `def-algebra-of-sets`, `def-sigma-finite`, `thm-completion`, `thm-lebesgue-completes-borel`. MT.5 can cite `thm-translation-invariant-unique` for m(TE) = |det T| m(E).
- **Division of labour with MT.1 (ch02), to settle before S2a:**
  - Equivalence "Lebesgue measurable ⇔ Carathéodory measurable for m*": the old MT.1 stub had it; MT.3 §03 proves it as `thm-lebesgue-caratheodory` unless MT.1 keeps it (then it becomes a recall).
  - Non-Borel Lebesgue set (subset of the Cantor set): MT.4's notes expect it from MT.1; MT.3 §05 builds it as `exm-lebesgue-not-borel` via φ(x) = x + F(x) (needs the Cantor function, which MT.3 defines as `lem-cantor-function` if MT.1/AN2.9 do not). Pick one home; if MT.1 keeps it, MT.3 §05 cites it and keeps only the composition consequence.
  - `lem-nonmeasurable-inside` (every positive-measure set has a non-measurable subset): MT.3 §05 proves it unless MT.1 does.
  - Label clash check: MT.1 may use `def-outer-measure` for Lebesgue exterior measure; then MT.3's abstract one is `def-abstract-outer-measure`.
- authoring/NOTATION.md rows: 𝓐 (`\sA`) algebra of sets; σ(𝓔) generated σ-algebra; 𝓑(X) Borel σ-algebra — `\sB` is taken (LA basis), propose new macro `\Bor`; μ* outer measure; μ̄, 𝓜̄ completion; δₓ Dirac; # counting measure; T_*μ pushforward; μ_F Lebesgue–Stieltjes measure; μ|_E restriction; H^s Hausdorff outer measure (example only).

## MT.2 (ch03, S1 blueprint 2026-10-25)

- Old blueprint `mt/authoring/blueprints/ch02.md` (MT.2) was git-moved to `ch03.md` and rewritten (MIRA 3 skeleton on Lebesgue measure on ℝᵈ, per D4 "ℝᵈ first"). The MT.1 author (new ch02) starts from an empty slot or from old ch01.
- registry/plan-edges.yaml: `MT.2: {s: [MT.1, AN1.8, AN2.2], revisits: [AN2.10]}` → add **revisits HA.9** (§4 proves HA.9's stated Arzelà theorem, §6 closes HA.9's list; HA.9 is an s-ancestor via MT.1 but the blueprint cites its labels) and **see AN2.11** (continuity/differentiation under the integral sign revisit AN2.11's parameter integrals). Optional see AN3.4 (one remark: Riemann ⇒ Lebesgue on boxes).
- registry/statements.yaml: add MT.2 `thm-monotone-convergence-integral`, `thm-fatou-lemma`, `thm-dominated-convergence`, `thm-riemann-is-lebesgue`, `thm-lebesgue-criterion-measure`, `thm-arzela-bounded-convergence`, `thm-riesz-fischer-l1`, `thm-l1-density`, `thm-l1-translation-continuous`; edges `thm-fatou-lemma uses thm-monotone-convergence-integral`, `thm-dominated-convergence uses thm-fatou-lemma`, `thm-riesz-fischer-l1 uses thm-dominated-convergence`, `thm-arzela-bounded-convergence uses thm-riemann-is-lebesgue`.
- MT.1 (ch02) blueprint should create labels for the interface MT.2 cites in prose: countable additivity, continuity from below/above, m(box) = volume, completeness of m, outer regularity, open sets as countable unions of almost disjoint closed cubes, m(E+h), m(δE), m(−E), closure of measurable functions under limits, the simple approximation theorem (increasing non-negative form; |φₖ| ≤ |f| form), a.e., Egorov.
- MT.3 (ch04) blueprint: cite MT.2's "What these proofs used of m" box (§3) and restate MCT/Fatou/DCT/Riesz–Fischer for (X, 𝓜, μ) "with the same proof"; Lebesgue–Stieltjes measures pay AN2.10's Riemann–Stieltjes pointer.
- STATUS.md promises: paid by MT.2: HA.9 "Arzelà proved in MT" (`thm-arzela-bounded-convergence`), HA.9 list items "limits" and "complete L¹". Opened: typewriter/Vitali → MT.8; L² completeness → MT.7; iterated integrals → MT.4; FTC for Volterra-type F → MT.9/MT.10; transfer → MT.3; dual of L¹ → FA.1b.
- authoring/NOTATION.md rows: [0, ∞] arithmetic with 0 · ∞ = 0; ∫ f, ∫ f dm, ∫ f(x) dx, ∫_E f ≔ ∫ f 1_E; f⁺, f⁻; ℒ¹(E) vs L¹(E), class [f]; τ_h f(x) ≔ f(x − h); C_c(ℝᵈ).
- authoring/STATUS.md: MT.2 row → "S1 blueprint (mt/authoring/blueprints/ch03.md), D4 layout; MT ch03".
- Directory slug: `mt/src/ch03-lebesgue-integral/`.

## MT.8 (ch12, S1 blueprint 2026-10-25)

- Old `mt/authoring/blueprints/ch08.md` (MT.8) was git-moved to `ch12.md` (commit 90c2403) and rewritten there. Directory slug: `mt/src/ch12-modes-of-convergence/`.
- registry/plan-edges.yaml MT.8: keep `s: [MT.7]`. The blueprint also uses MT.4 (Tonelli, layer cake) and MT.5 (m(B(0,r)) = v_d r^d) — both in the closure via MT.7 s MT.4 (check MT.5; if not in closure add `see: [MT.5]`). R2 uses FA.4 (Baire) in a review exercise only: optional `see: [FA.4]`.
- Agrees with the MT.9 note above: add **MT.9 s MT.8**. Labels MT.9 should cite: `thm-markov-inequality`, `def-distribution-function`, `thm-layer-cake`, `def-weak-lp`, `prp-lp-in-weak-lp`, `thm-weak-lp-sandwich`, `thm-riesz-subsequence`. MT.9 writes the level variable as λ; MT.8 uses t and d_f(t) = μ({|f| > t}) — harmonise in NOTATION (proposal: d_f, level variable t or λ, never λ for Lebesgue measure, which is m).
- Vitali *convergence* theorem labels are `thm-vitali-convergence-*` to stay distinct from MT.9's Vitali *covering* lemma (`lem-vitali-finite`).
- Possible label collisions to settle when MT.2/MT.3/AN1 are re-blueprinted: `thm-markov-inequality` (MT.8 owns it unless MT.2 takes it; MIRA has it in ch 4 = MT.9, which comes later), `lem-borel-cantelli` (MT.8 unless MT.3 takes it; PR.1 cites whichever), `lem-subsubsequence` (recall from AN1 if it exists there).
- MT.3's blueprint should state that MCT/Fatou/DCT hold on an arbitrary measure space (MT.8 §1 relies on it).
- authoring/NOTATION.md rows to add: d_f (distribution function), ‖f‖_{p,∞} and L^{p,∞} (weak Lᵖ quasi-norm), "UI", "tight".
- authoring/STATUS.md: MT.8 row → "S1 blueprint (mt/authoring/blueprints/ch12.md), D4 layout; old ch08.md moved there". Promises opened: `sec-weak-lp` → MT.9 weak (1,1); `thm-weak-lp-sandwich` → MT.9 Marcinkiewicz; `exm-typewriter` → PR.1 (in probability, not a.s.).
- PR.1 (branch, s [MT.4, MT.8]): may cite `def-convergence-in-measure`, `lem-borel-cantelli`, `thm-vitali-convergence-finite`, `cor-lp-by-tails` (E|X| = ∫ P(|X| > t) dt).
- mt/README.md still says "MT: Measure and Integration"; volume renamed to *Measure, Integration, and Real Analysis* (spec/08 D4). Not edited here to avoid conflicting with parallel MT workflows.
