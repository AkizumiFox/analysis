
## AN2.5 (ch11) S1, 2026-10-25

- `authoring/STATUS.md`: AN2.5 row → "blueprint (S1 done, S2a next)"; blueprint `an2/authoring/blueprints/ch11.md`.
- Labels cited with † from AN2.3, AN2.4, AN1.9, AN1.4, AN1.7, AN2.9 are provisional (those chapters are not yet re-blueprinted); reconcile at their S1 or at AN2.5 S2a.
- AN2.4's blueprint should provide `thm-ivp-integral-equation` for **continuous** f (not only Lipschitz) and keep the y^{1/3} example and the blow-up alternative; AN2.5 relies on all three.
- `NOTATION.md`: add `Lip(f)` (best Lipschitz constant) if AN2.4 does not.
- Registry (math-atlas, no change required): `thm-arzela-ascoli` (AN2.5) kept with edge `uses thm-metric-compact-equiv`; downstream s-edges CA.5, FA.7, PDE.5 served by `thm-arzela-ascoli`, `thm-arzela-ascoli-compact`, `lem-diagonal-extraction`, `exm-integral-operator-compact`.

## ch14 (AN2.8 Separation, Urysohn–Tietze, LCH), S1, 2026-10-25

- STATUS.md: AN2.8 row → "S1 blueprint (deepen) written; S2a next"; directory `an2/src/ch14-separation-urysohn-lch/`.
- NOTATION.md rows: \( X_\infty \) one-point compactification (not \( X^* \), reserved for duals in FA); \( K \prec f \prec U \); \( C_b(X) \), \( C_0(X) \) next to the existing `C_c` row; convention "regular and normal include T1".
- AN2.7 (ch13) label names are assumed in ch14's "Assumed AN2.7 labels" list; reconcile when ch13 is re-blueprinted (pasting lemma: if ch13 lacks it, ch14 §05 proves `lem-pasting-closed`).
- AN1 re-cut dependency: ch14 cites the metric Urysohn function and the non-compact unit ball (ℓ²) from AN2.3 if the AN1 rewrite of an1 ch08 keeps them; ch14 proves `prp-metric-normal` locally either way, so no break if they go. Please tell the AN1 workflow not to reuse the labels listed in ch14.
- AN2.6 (ch12): ch14 §02 makes a meta-claim that AN2.6's Stone–Weierstrass proof uses only compactness and point separation (so it holds for compact Hausdorff K). Keep that route in ch12, or ch14 weakens the remark (S2a item 6).
- Registry (math-atlas, not edited here): AN2.8 s-edges already [AN2.7, AN2.2, AN1.9]. Suggested soft edges: AN2.8 see AN2.6; FA.5 revisits AN2.8; AM.1 see AN2.8 (continuous partitions of unity before smooth ones); CA.1 see AN2.8 (ℝ²_∞ ≅ S², Riemann sphere).

## ch15 (AN2.14 The Gauge Integral, opt) — S1, 2026-10-25

- **Label clash avoided:** `def-gauge` is MA.18's (Minkowski functional, registry/terms.yaml); this chapter uses `def-interval-gauge`. Registry terms to add when drafted: gauge (on an interval) → `def-interval-gauge@AN2.14`, δ-fine → `def-delta-fine`, gauge integral / Henstock–Kurzweil integral → `def-gauge-integral`, Cousin's lemma → `thm-cousin`, Saks–Henstock lemma → `lem-saks-henstock`, Hake's theorem → `thm-hake`.
- **Edges:** keep `AN2.14: {s: [AN2.10]}`. Suggested soft edge `see: [AN1.9, AN2.9]` (uniform convergence restated in one remark/B exercise; Cantor function in one warning). Suggested soft pointers *to* AN2.14 (never s): AN2.15 (Volterra's derivative is gauge integrable), MT (Lebesgue = absolutely gauge integrable).
- **Exam targets:** AN2.14 serves no §E1 target item; do not add it to any target's `chapters`.
- **AN2.10 dependency:** blueprint assumes labels `def-tagged-partition`, `def-riemann-sum`, `def-mesh`, `thm-riemann-sum-criterion` (mesh form, α(x) = x), `def-measure-zero`, `thm-lebesgue-criterion`; reconcile when AN2.10's blueprint lands.
- **AN2.9 dependency (soft):** §03 warning uses the Cantor function (continuous, increasing, φ′ = 0 off C); ask AN2.9 to build it or the warning states the properties.
- **NOTATION.md rows:** gauge δ: [a, b] → (0, ∞); "δ-fine"; δ₁ ∧ δ₂ (pointwise min of gauges); (R)∫ vs (G)∫ when compared.
- **STATUS.md:** AN2.14 row → "S1 blueprint written (ch15.md); S2a next".

## ch13 (AN2.7 Topological Spaces, Products, and Compactness), S1 2026-10-25

- STATUS.md: AN2 ch13 row → "S1 written (deepen blueprint, Apostol layout); next S2".
- NOTATION.md new rows: 𝒯 / (X, 𝒯), 𝒯_d, cl / int / ∂ in topological spaces, ℝ_ℓ (Sorgenfrey line), ∏ X_α with π_α, Y^I (product topology), X/∼ with q.
- registry (math-atlas): AN2.7 s-edges unchanged {AN2.3, F2.5}; suggest soft edges `revisits: [AN2.1]` (open sets as axioms; equivalent-metrics preview paid) and `see: [AN1.9]` (pointwise convergence = product topology).
- AL3.9 (s AN2.7) needs Tychonoff for products of finite discrete spaces (profinite groups); AN2.7 only states Tychonoff (proof in FA.5). AL3.9 should add b FA.5 or prove the finite-discrete case itself.
- FA.5 blueprint: cite thm-hilbert-cube-compact (countable Tychonoff by diagonal), thm-compact-fip, def-initial-topology, def-net / prp-closure-nets from AN2.7.
- AN2.8 blueprint: continue exm-weird-spaces-table (regular / normal / locally compact columns) and prove "Sorgenfrey line not metrizable" (entry marked "(AN2.8)" in AN2.7).
- AM.3: def-second-countable and exm-line-two-origins live in AN2.7.
- Coverage sources: the AN2 reference list has no general topology; AN2.7 checks coverage against Munkres Topology, Sutherland, Willard, Steen–Seebach (topology shelf).
- AN1 ch03 (AN2.1) and ch08 (AN2.3) labels do not exist yet; AN2.7 cites their results in prose until re-blueprinted.

## ch02 (AN1.8, The Riemann–Darboux Integral), S1 2026-10-25

- **STATUS.md:** AN1.8 row: S1 done (deepen blueprint `an2/authoring/blueprints/ch02.md`), next S2a.
- **NOTATION.md, new rows:** U(f, P), L(f, P); lower/upper integral (`\underline{\int}`, `\overline{\int}`; agree macros); ℛ[a, b]; ‖P‖ (mesh); S(f, P, t) (Riemann sum); ω_f(x) under the existing `\osc` row; orientation convention ∫ᵦᵃ = −∫ₐᵇ.
- **Label coordination:** AN1.8 owns `def-partition-of-interval`, `def-mesh`, `def-darboux-sums`, `def-measure-zero`, `def-oscillation`, `def-improper-integral` (`def-partition` is F2.2's set partition). AN2.9 (bounded variation, read first) should use its own partition wording or cite this label by prose pointer only, since AN1.8 has no s-edge to AN2.9 and AN2.9 none to AN1.8; if AN2.9 needs a labelled partition definition, give it `def-partition-bv` or move ownership to AN2.9 and have AN1.8 restate unlabelled.
- **Series-free measure zero:** `def-measure-zero` uses partial sums (AN1.3 comes after AN1.8). AN1.3's blueprint should restate it as Σ|Iₙ| ≤ ε and note the equivalence.
- **Integral test** moves from AN1.8 to AN1.3 (series now come after the integral); AN1.3 cites `def-improper-integral`, `thm-improper-comparison`, `exm-power-integrals`.
- **Promises opened** (for STATUS's promise table): `thm-lebesgue-criterion` proof → AN2.10 closing section; mesh vs refinement for Stieltjes → AN2.10; ∫lim vs lim∫ (χ_{q₁..qₙ} ↑ χ_ℚ) → AN1.9, MT/HA.9; L(x) = ∫₁ˣ dt/t identified with log → AN1.10; Bonnet's second MVT → AN2.10; Volterra → AN2.15 (optional, prose only).
- **AN1.4–AN1.7 labels needed** (cited by name until their S1 fixes labels): Heine–Cantor, EVT, IVT (AN1.6); MVT, chain rule, derivatives of rational powers, Lagrange-remainder Taylor (AN1.7); limits at ∞, one-sided limits of monotone functions, Thomae continuity example (AN1.5); Cantor set construction Cₙ, Heine–Borel (AN1.4).
- **spec/08 section numbers (math-atlas, for the coordinator):** in Apostol 2e the Riemann case of AN1.8 is 7.1–7.7, 7.11–7.14, 7.18–7.21 (7.26 statement), not "7.1–7.10"; 7.8–7.10 (step integrators, Euler summation) are Stieltjes. Parameter integrals are Apostol 7.23–7.25, not 7.17–7.20 as C3 gives for AN2.11. Suggest correcting spec/08 C3 and the `apostol-ma` items.

## ch06 (AN1.9 Sequences and Series of Functions), S1, 2026-10-25

1. **STATUS.md**: AN1.9 row → "S1 blueprint written (an2/authoring/blueprints/ch06.md); next S2a". Directory `an2/src/ch06-sequences-of-functions/`.
2. **Registry edge (optional)**: add `b AN2.3` to AN1.9 (scope: `rem-ck-compact-metric` and `exr-modes-c2`, C(K) and Dini on a compact metric space). The main line uses only compact K ⊆ ℝ (AN1.6), so no s-edge change is required; AN2.3 precedes AN1.9 in reading order either way.
3. **NOTATION.md**: add `f_n \rightrightarrows f` (uniform convergence, set always named); `\norm{f}_S` / `\norm{f}_\infty` = sup norm (until MT's `\esssup`); `B(S)`, `C_b(S)`, metric `d_\infty`; `d_1` (mean distance on C[a,b]).
4. **Promises opened** (for STATUS's promise list): AN1.10 ← `thm-weierstrass-m-test`, `thm-term-by-term`, `thm-uniform-limit-derivative`; AN2.4 ← `cor-ck-complete`; AN2.6 ← `cor-ck-complete`, `exm-takagi-continuous`, `thm-dini`; AN2.8 ← `thm-continuous-bounded-complete`; AN2.11 ← `thm-moore-osgood`, `thm-uniform-limit-integral`; AN2.13 ← `thm-abel-test-uniform`; MT ← `thm-arzela-bounded-convergence` (stated without proof here), `exm-mean-distance-incomplete`; HA ← Fourier-crisis hook, `exm-sine-series-nonuniform`, `def-mean-convergence`.
5. **Promises paid**: AN1.7's deferred continuous nowhere-differentiable function (continuity `exm-takagi-continuous`, nondifferentiability `exr-function-series-c2`); AN2.2's moved B(S)/C(K) completeness (spec/08 C2).
6. **Conflict in the AN1 volume (for the an1 workflow)**: the old AN2.3 stub (now `an1/authoring/blueprints/ch08.md`) still plans "the Peano curve as a uniform limit" (§5) and "Tietze ... using completeness of C_b" (§7). Both need AN1.9, which now comes later (AN2 ch06). Peano curve → AN2.15 (optional); Tietze by uniform approximation → AN2.8 (which has s AN1.9 per spec/08 C6).
7. **Planned labels** cited from AN1.2–AN1.8, AN2.1, AN2.2 (`thm-cauchy-criterion`, `prp-closed-subset-complete`, `prp-closed-sequential`, `thm-continuity-sequential`, `thm-extreme-value`, `thm-bolzano-weierstrass`, `thm-mean-value`, `thm-riemann-criterion`, `prp-integral-monotone`, `prp-integral-abs`, `thm-ftc-derivative`, `thm-ftc-evaluation`, `thm-series-cauchy-criterion`, `thm-comparison-test`, `lem-summation-by-parts`, `thm-dirichlet-test`, `thm-abel-test`, `exm-cantor-set`, `exm-fat-cantor-set`, `prp-distance-to-set`): reconcile when those blueprints freeze.

## ch08 (AN2.11 Integrals with a Parameter, Euler Summation, and the Gamma Function) — S1, 2026-10-25

- `authoring/STATUS.md`: AN2.11 row → "blueprint (S1 done, S2a next)"; blueprint `an2/authoring/blueprints/ch08.md`; directory `an2/src/ch08-parameter-integrals-and-gamma/`.
- **spec/08 C3 section numbers are off** (math-atlas, not edited here): Apostol 2e's parameter integrals are 7.23–7.25 and Euler's summation formula is 7.10; 7.17–7.20 (necessary conditions, MVT, integral as a function of the interval, second FTC) belong to AN2.10. Apostol has Γ only as examples in 10.14, 10.16. Suggest C3 row 8 read "7.10, 7.23–7.25; PMA 8 (Γ, Stirling), 9.42; Spivak 19", and the same in `an2/authoring/design/layout-apostol.md` row 8 and the `apostol-ma` items if they quote section numbers.
- `registry/exam-targets.yaml` (`pma`): no item names PMA 9.42 (differentiation of integrals); suggest adding AN2.11 to the "PMA 9" topic or a separate item.
- Edges (registry, suggestions only): s-edges unchanged [AN2.10, AN1.9, AN1.10]; add b AN2.12 (ζ, one exercise only, §03 C1) or leave as prose. Soft edges: AN3.4 see AN2.11 (`thm-interchange-order` → Fubini on rectangles); HA.5 see AN2.11 (Gaussian, Dirichlet integral); PR.1 see AN2.11 (Gaussian, Stirling); CA.13 revisits AN2.11 already in C6.
- Provisional earlier labels: ch08 cites AN2.10 (R–S integration by parts, step integrators, reduction for C¹ integrators), AN1.8 (improper integrals, integral test, substitution), AN1.9 (uniform-limit continuity, integration and differentiation theorems, M-test), AN1.10 (exp/log/real powers, arctan 1 = π/4) by prose until those chapters' labels are fixed. AN2.10's blueprint must provide R–S integration by parts for f continuous, α of bounded variation, and ∫ f d⌊x⌋ as a finite sum. AN1.8's must keep improper integrals (both kinds) and the integral test. ch08 does not need AN2.10 to cover Apostol 7.22 (second MVT).
- ch08 proves `lem-integral-cauchy-schwarz` itself; if AN1.8 proves Cauchy–Schwarz for integrals in the main line, S2a may replace the lemma by a citation.
- `NOTATION.md` rows: {x} fractional part; P₁, P₂, P₃ periodic sawtooth (this series' names); γ Euler's constant; Γ, B(x,y); F_R(t) truncated parameter integral; "f ~ g" (f/g → 1) if AN1.3/AN1.10 do not define it.
- AN2.15 weird-examples table: five entries from ch08 (listed in its "Weird-examples table").
