
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

## AN2.15 (ch16, A Gallery of Pathological Functions) — S1, 2026-10-25

- **Registry edges.** spec/08 C3 lists AN2.15's s-edges as "—". The blueprint uses, as hard prerequisites, AN2.10 (Lebesgue criterion, R–S), AN2.9 (BV, length), AN1.9 (M-test, C[0,1] complete, term-by-term differentiation), AN1.10 (e^{-1/x}), AN2.2 (Banach fixed point). Proposed: `s: [AN2.10, AN2.9, AN1.9, AN1.10, AN2.2]`, `b: [AN2.6, AN2.3]`, `revisits: [AN1.4, AN1.5, AN1.7, AN1.8, F4.7]`. Nothing may depend on AN2.15 (unchanged).
- **Soft edges into AN2.15 (optional, prose only):** MT.10 see AN2.15 (Cantor function); AM.1 see AN2.15 (bump functions); AN2.6 see AN2.15 (Takagi as explicit nowhere-differentiable).
- **exam-targets.yaml:** Apostol §9.7 (space-filling curve) is fully proved only in AN2.15. Decide: map the apostol-ma 9.7 item to AN1.9 with AN2.15 as optional cover, or mark the item optional. Also pma Ex. 7.14 and pugh "Peano curves" are optional cover here.
- **Upstream blueprints (other workflows):**
  - AN1.9 (an2 ch06): prove only the continuity of Takagi's T = Σ 2^{-n} dist(2^n x, ℤ) (M-test); the full nowhere-differentiability proof is AN2.15 §04 (pays the AN1.7 hook per spec/08 C5). If AN1.9 uses a different function, AN2.15 §04 keeps Takagi and the recall box changes.
  - AN1.5 (an1 ch06): "no function continuous exactly on ℚ" (old blueprint: optional, via Baire) is proved in AN2.15 §01; AN1.5 should point forward in prose instead.
  - AN2.3 (an1 ch08): the old blueprint had "the Peano curve as a uniform limit"; spec/08 puts the space-filling curve in AN2.15 §06. AN2.3 should drop it or keep a prose pointer.
  - AN1.8 (an2 ch02): keeps Volterra as statement only, pointing to AN2.15 §03.
  - F4.7 (fd4): the weird-examples table's row format must match AN2.15's closing table `tbl-weird-examples-closed` (columns: Exhibit | First met | Belief it breaks | Settled in).
  - AN2.10 (an2 ch03): AN2.15 cites its oscillation ω_f(x), the covering lemma for finitely many open intervals, and R–S change of variable / integration by parts. If AN2.10 omits any, AN2.15 proves it locally.
  - AN2.6 (an2 ch12): if AN2.6 defines G_δ, AN2.15 cites it instead of `def-g-delta-set`.
- **NOTATION.md rows:** s(x) = dist(x, ℤ) (chapter-local), C_f (set of continuity points of f).
- **STATUS.md:** AN2.15 row → "S1 blueprint written (an2/authoring/blueprints/ch16.md); S2a next".

## AN2.10 (ch03) The Riemann–Stieltjes Integral, S1, 2026-10-25

- `authoring/STATUS.md`: AN2.10 row → "blueprint (S1 done, S2a next)"; blueprint `an2/authoring/blueprints/ch03.md`; directory `an2/src/ch03-riemann-stieltjes-integral/`.
- **spec/08 section numbers (math-atlas C3 row AN2.11, and `an2/authoring/design/layout-apostol.md`)**: in Apostol 2e, 7.17–7.20 are necessary conditions, mean-value theorems, the integral as a function of the interval, and the second FTC; parameter integrals are **7.23–7.25**. Suggest AN2.11 = Apostol 7.10 (Euler summation), 7.19–7.25. AN2.10 covers 7.1–7.9, 7.11–7.18, 7.26 and, briefly, 7.27 (complex-valued integrals, for CA.1). Euler summation (7.10) sits inside AN2.10's nominal range 7.1–7.16 but goes to AN2.11 by that chapter's title.
- **AN1.8 re-blueprint**: the full proof of Lebesgue's criterion and `def-measure-zero` now live in AN2.10; AN1.8 should at most state the criterion with a forward pointer (prose), and should not define measure zero. AN2.10 cites these AN1.8 labels (provisional): `def-partition`, `def-refinement`, `def-darboux-sums`, `lem-refinement`, `thm-darboux-criterion`, `thm-continuous-integrable`, `thm-monotone-integrable`, `thm-ftc-1`, `thm-ftc-2`, `thm-substitution`, `exm-dirichlet-function`, `exm-thomae-function`.
- **AN2.9 blueprint** should provide (provisional names): `def-bounded-variation`, `def-total-variation`, `thm-variation-additive`, `thm-jordan-decomposition`, `thm-variation-function-continuity`, `thm-monotone-countable-discontinuities` (or AN1.5), `exm-cantor-function` with the properties c(x/3) = c(x)/2, c(2/3 + x/3) = 1/2 + c(x)/2, c(1 − x) = 1 − c(x).
- **AN1.3 (next chapter)**: summation by parts is introduced as a named move in AN2.10 §3. AN1.3's s-edges (AN1.2, F2.3) do not include AN2.10; either add `see AN2.10` (soft) or let AN1.3 re-derive Abel summation in two lines. Same for AN2.13 (s AN2.12, AN1.10).
- `NOTATION.md` rows: ∫_a^b f dα; 𝓡(α) (`\mathcal{R}(\alpha)`), 𝓡 = 𝓡(x); Δαₖ; S(P, f, α); U(P, f, α), L(P, f, α); upper/lower Stieltjes integrals; ω_f(x) (oscillation at a point), Ω_f(I) (oscillation on a set); D_f, D_f(ε) = {ω_f ≥ ε}; ℓ(I).
- Registry (math-atlas, for the registry workflow; no edge change): AN2.10 s-edges stay AN2.9, AN1.8. Terms: Riemann–Stieltjes integral, integrator, Riemann's condition, oscillation, measure zero, Lebesgue's criterion. Exam items: apostol-ma (Apostol 7.1–7.18, 7.26, 7.27), pma (6.1–6.19), pugh (3.2 Riemann–Lebesgue theorem).
- Running pathological-functions table (F4.7 → AN2.15): AN2.10 adds `exm-shared-jump`, `exm-opposite-jumps`, `exm-alpha-d-alpha`, `exm-cantor-mean`, `exm-cantor-indicator`, `exm-fat-cantor-set`, `exm-composition-fails`, `exm-dirichlet-as-limit`.

## ch04 (AN1.3 Infinite Series), S1 2026-10-25

- **STATUS.md:** AN1.3 row → "blueprint written (S1, deepen, Apostol layout); next S2a". Promise F2.3 → AN1.3 (decimal expansions) is paid by `prp-decimal-expansion`, `prp-decimal-two-expansions`; AN1.2 → AN1.3 (e = Σ1/k!) by `thm-e-series`. New promises opened toward AN1.10 (L(2) = ln 2; exp := E with `thm-exp-series-product`; Abel's product theorem), AN2.13, AN2.12, AN2.11, HA, AN2.15 (listed in the blueprint's "Promises").
- **NOTATION.md rows:** sₙ, rₙ (partial sum, tail); aₙ⁺, aₙ⁻; O, o, ∼; Hₙ; L(x) = ∫₁ˣ dt/t (renamed log in AN1.10); Cauchy product (a ∗ b)ₙ.
- **Registry edges (math-atlas `registry/plan-edges.yaml`), for the coordinator to decide:** spec/08 C3 gives AN1.3 only s AN1.2, F2.3. The blueprint also uses: `b F4.1` (complex terms, Apostol 8.9), `b F4.10` (scope: Σ sin(nx)/n example), `b AN1.8` (scope: integral test, Apostol 8.12, and the hook's value L(2)), `b AN1.5` (scope: one C exercise). All point to earlier chapters. If the integral test should stay in AN1.8 instead (old AN1.8 blueprint §7 has it), drop `b AN1.8` and AN1.3 cites it; tell the AN1.8 (ch02) worker either way so it is proved once.
- **spec/08 C3 Apostol numbering:** in the 2e text 8.20–8.23 are double series, 8.24 multiplication of series (Mertens), 8.25 Cesàro, 8.26–8.27 infinite products and the Euler product. C3 says "8.20–8.25" for AN2.12 and "8.26" for AN2.13; it should read AN2.12 = 8.20–8.23, 8.26–8.27 (8.24 Mertens proved in AN1.3, cited), AN2.13 = 8.25, 9.21–9.23. Exam-target item text can stay.
- **AN1.2 labels:** the blueprint cites expected labels `thm-monotone-convergence`, `def-limsup`, `thm-limsup-properties`, `thm-cauchy-criterion`, `thm-algebraic-limits`, `exm-power-to-zero`, `exm-nth-root-n`, `def-e`; AN1.2's worker should use these or report its own so S2a can reconcile.

## ch07 (AN1.10 Power Series, Taylor Series, and the Elementary Functions), S1 2026-10-25

- **Edge request (math-atlas registry/plan-edges.yaml):** add `AN2.12` to AN1.10's s-edges: `AN1.10: {s: [AN1.7, AN1.9, AN2.12], revisits: [F4.1, F4.7, F4.10]}`. §3 (substitution, re-centering) uses AN2.12's rearrangement of absolutely convergent double series; the Cauchy product is cited from AN1.3 (Mertens there, per the ch04 note above). No cycle (AN2.12 s AN1.3, F4.6, F4.7). If refused, the blueprint's fallback proves the lemma in §3.
- **Apostol 9.21 (binomial series) placement:** spec/08 C3 lists 9.21–9.23 under AN2.13; the AN1.10 blueprint proves the binomial series on |x| < 1 (Taylor-series content, ODE identification) and leaves the endpoints to AN2.13. Consistent with the ch04 note's AN2.13 = 8.25, 9.21–9.23, read 9.21 there as "endpoints only", and let the apostol-ma items map 9.21 to AN1.10 + AN2.13.
- **STATUS.md promise rows:** AN1.10 pays F4.7 (E1)–(E4), F4.1 `ax-cosine-sine` (T1)–(T5), F4.10 (rotation by E(iθ)), F4.6 (real powers), AN2.12's log box, AN1.2/AN1.3 e and provisional sin/log, LA2.10 (A1), (A2), (A5). AN1.10 opens promises to AN2.13 (Abel's theorem, binomial endpoints), AN2.4 (exp via Picard), AN2.11 (Γ), AN2.15 and AM (bump function), CA (principal Log branch cut), CA.1 (radius = distance to nearest singularity).
- **NOTATION.md rows:** E (the exponential series during its construction), Log, Arg (principal branches, Arg ∈ (−π, π]), \binom{\alpha}{n} for real α, z^w ≔ E(w Log z).
- **F4.1 wording (foundations repo):** F4.1 §1.5 says the box is "proved in *Analysis on the Real Line*, Chapter 10"; after the re-cut this is AN2 *Integration, Series, and Function Spaces*, Chapter 7 (atlas id AN1.10). Same for any F4.7 pointer once written.

## ch01 — AN2.9 Functions of Bounded Variation and Rectifiable Curves (S1, 2026-10-25)

Blueprint: `an2/authoring/blueprints/ch01.md`. Requested changes to shared files and other volumes (not made here):

1. **STATUS.md**: AN2 row 1 (AN2.9) → "blueprint written (S1); next S2a". Promises opened: AN2.10 (V = ∫|f'| and L = ∫‖γ'‖ for C¹ data; Stieltjes with BV integrators; ∫ dκ = 1), AN1.8 (BV ⇒ Riemann integrable remark), CA.1 (contour integrals over rectifiable paths, ML estimate), HA (Dirichlet–Jordan test), MT.9–MT.10 (a.e. differentiability of BV; absolute continuity; κ), AN2.15 (gallery rows), AM.1 (arc-length parametrization). Promise paid: AN1.4 Cantor-set hook (spec/08 C5).
2. **NOTATION.md** new rows: partition P, 𝒫[a,b], mesh ‖P‖; Var(f;P); V_a^b(f); v_f, v_f^±; BV[a,b]; Λ(γ;P), L(γ), L(γ;[c,d]), s_γ; κ (Cantor function).
3. **AN1 labels needed** (AN1 re-blueprints in progress; the AN2.9 blueprint names facts, S3 swaps in `@ref`s):
   - AN1.4: Cantor set construction (C_n, C = ⋂C_n, gap endpoints in C, C contains no interval).
   - AN1.5: one-sided limits of monotone functions; discontinuities of monotone functions are jumps, countably many; classification of discontinuities (first kind = removable or jump).
   - AN1.6: IVT; continuous strictly monotone function on an interval has continuous inverse; Heine–Cantor on [a,b].
   - AN1.7: MVT; derivatives have the intermediate value property (Darboux). If AN1.7 also proves the vector mean value inequality ‖γ(t)−γ(s)‖ ≤ K|t−s|, AN2.9 §05 B2 will cite it instead of proving it.
   - AN1.2: unboundedness of harmonic partial sums (if absent, AN2.9 §01 proves it in a Brief Review box).
   - AN1.11: nested intervals (used by an R exercise only).
4. **Shared definitions with AN1.8** (same book `an2`, labels unique book-wide): AN2.9 defines `def-partition`, `def-refinement`, `def-mesh`. The AN1.8 re-blueprint should cite them rather than redefine. spec/08 C3 lists AN1.8 → AN2.9 as "see"; citing definition labels makes it a `b` edge (atlas registry: AN1.8 `b: AN2.9`). Alternative if the coordinator prefers AN1.8 self-contained: AN1.8 owns the labels and AN2.9 §01 says "partition (defined again in AN1.8)" — this would need AN2.9 to define them under different labels. Recommend the `b` edge.
5. **spec/08 C3 discrepancy**: row AN2.9 cites "Pugh 3 習題", but Pugh's bounded-variation material is §6.10 (Lebesgue's last theorem) and Appendix-H exercises *67–*68; Pugh ch. 3 has only Cantor-set and zero-set exercises. Suggest "Pugh §6.10、附錄習題" in C3 and the layout table.
6. **Pathological-functions table** (F4.7 → AN2.15): AN2.9 contributes eight rows (listed in the blueprint §06); AN2.15's blueprint should pick them up.
