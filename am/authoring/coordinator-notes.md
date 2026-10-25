# AM coordinator notes

Changes to shared files or to math-atlas that AM blueprint work needs. Not applied by the volume workflows (parallel run); the coordinator applies them.

## From ch06 (AM.3) S1, 2026-10-25

- **STATUS.md:** add the AM volume and the row "AM.3 — ch06 — blueprint (S1), not frozen — `am/authoring/blueprints/ch06.md`".
- **math-atlas registry (edges):** AM.3 keeps s AN3.5, AN2.7, AN3.3 (spec/08 D3). Proposed additions:
  - `b AM.2` and `b AN3.7`: used only in §6.4 (hairy ball: the closed non-exact form on ℝⁿ⁺¹ ∖ {0} and Stokes on [0,1] × Sⁿ). Both are earlier chapters of AM, so reading order is unaffected.
  - `b AM.1`: smooth bumps and partitions of unity on ℝⁿ, transplanted in §2.
  - see-edges (prose only, no s-edge): PDE → AM.3 (flows, straightening for characteristics); CA2 → AM.3 (charts and atlases as the model for Riemann surfaces).
- **exam-targets:** AM.3 serves no E1 target (seg B). If a graduate manifolds target (Lee ISM 1–9) is ever added, AM.3 is its first item.
- **NOTATION.md rows** (series file): (U, φ) chart and ψ ∘ φ⁻¹ transition; TₚM (derivations); ∂/∂xⁱ|ₚ; dFₚ (vs AN3's DF(a): they agree on open subsets of Euclidean space); TM, π; 𝔛(M); C^∞(M); γ′(t); flow θ: 𝒟 → M, θₜ, θ⁽ᵖ⁾; F_*X; [X, Y]; ℒ_X Y. Upper indices on coordinates and components; no summation convention.
- **Label reconciliation:** ch06 cites AN3.5, AM.1, AN3.7, AM.2, AN2.4, AN3.3 by prose description because those blueprints are being written in parallel. S2a list item 1 in ch06 replaces them with the frozen labels.
- **AN2.7:** ch06 does not depend on AN2.7's optional quotient section (§1 restates the quotient topology). It uses `second countable`, which AN2.7 does not define; ch06 defines it (`def-second-countable`). If AN2.7 later adds it, ch06 should cite it instead.

## From ch04 (AN3.7) S1, 2026-10-25

- **STATUS.md:** add the row "AN3.7 — am ch04 — blueprint (S1), not frozen — `am/authoring/blueprints/ch04.md`". Remove AN3.7 from the AN3 rows (it moved, spec/08 D3; seg B mark dropped).
- **math-atlas registry:** plan-edges `AN3.7: {s: [AN3.4, AN3.5, AN3.6, AM.1]}` is what ch04 uses; no change. Proposed see-edges (prose only): PDE → AN3.7 (`thm-green-identities`), CA.2 → AN3.7 (`thm-green`), FX → AN3.7 (`thm-smooth-no-retraction`, once FX is registered).
- **statements.yaml:** ch04 uses the registry label `thm-stokes`. Its divergence theorem is `thm-divergence-manifold`, not `thm-divergence` (that one is MT.6's). Consider adding `[thm-divergence-manifold, AN3.7, thm, ...]` and the relation `thm-divergence generalizes thm-divergence-manifold`.
- **Seam items with Chapters 1–3 (parallel S1; ch04 cites them by prose only, its blueprint lists the assumed contents under "Prerequisites"):**
  - Chapter 2 (AN3.5): the half-space convention. ch04 assumes Hᵏ = {x_k ≥ 0} (Munkres). If AN3.5 uses x₁ ≥ 0 or x₁ ≤ 0, re-derive the sign (−1)ᵏ in ch04 §2 and §4.
  - Chapter 2: whether it defines V(Dα), "measure zero in M" and the scalar integral ∫_M f dV (Munkres §21–22, §25). AN3.5's s-edge is only AN3.2, so ch04 §3 defines them. If AN3.5 does, ch04 §3 recalls them and shrinks.
  - Chapter 2: the outward unit tangent vector at boundary points, and the claim that patches carry boundary points to boundary points.
  - Chapter 1 (AM.1): the partition-of-unity theorem must give Σφᵢ = 1 on an **open** set containing a compact M (ch04 `thm-stokes` uses it). Also the change of variables theorem and extended integrals.
  - Chapter 3 (AN3.6): pullback for maps with domain open in Hᵏ; α*(dω) = d(α*ω) for C² α; the work/flux-form dictionary; ω(Ta) = det T·ω(a).
- **Weird-examples table:** ch04 §6 has the table "When Stokes fails". If Chapters 1–3 open an AM-wide multivariable table, ch04's rows join it.
- **NOTATION.md rows:** Hᵏ, ∂Hᵏ; ∫_{Y_α} ω; −M; n_out; V(Dα); dV (dS, ds aliases in §5 only); λ_ω; ι_F (flux form), ω_F (work form), if Chapter 3 does not already fix them.

## From ch02 (AN3.5) S1, 2026-10-25

- **STATUS.md:** row "AN3.5 — am ch02 (`am/src/ch02-submanifolds-tangent-spaces/`) — blueprint (S1), not frozen — `am/authoring/blueprints/ch02.md`".
- **math-atlas registry (edges):** none. AN3.5 keeps s AN3.2. Determinants in §5 (SL(n), det = ±1 on O(n)) come through AN3.1's b LA2.7; if the scope lint `scope: {LA2.7: [AN3.1, LA1.3]}` objects to AN3.5 using it, either add `b LA2.7` to AN3.5 with scope [AN3.5] or tell the drafter to prove det(I + tH) = 1 + t·tr H + O(t²) from the Leibniz formula in place.
- **Labels expected from AN3.2** (its blueprint has no label list yet): `thm-inverse-function`, `thm-inverse-regularity`, `thm-implicit-function`, `thm-rank`, `thm-lagrange-multipliers`; from AN3.1: `thm-chain-rule`, `thm-gl-open`. Rename in ch02 when AN3.2/AN3.1 are re-blueprinted.
- **Labels ch02 provides that ch06 (AM.3) cites by prose:** `thm-transition-smooth`, `cor-straightening`, `def-coordinate-patch`, `def-tangent-space`, `def-differential-submanifold`, `thm-orthogonal-group`, `thm-special-linear-group`, `exm-dense-winding`, `thm-constrained-critical-point`. For AN3.7: `def-manifold-with-boundary`, `thm-boundary-well-defined`, `thm-boundary-is-manifold`, `prp-regular-sublevel-set`, `prp-tangent-space-at-boundary`, `def-outward-normal`, `exm-moebius-band` (orientation hook planted for AN3.7), `exm-square-corner` (corner hook: confirm AN3.7 takes corners; else ch02 drops the sentence).
- **Scope split with AN3.7:** ch02 covers Munkres §23–24 (manifolds, boundary); Munkres §21–22, §25 (k-volume, Gram determinant, scalar integrals) are left to AN3.7.
- **Notation alignment (NOTATION.md):** ch02 writes the differential of a map between submanifolds of ℝⁿ as df_p : T_pM → T_{f(p)}N with T_pM ⊆ ℝⁿ (velocity vectors); ch06 writes dFₚ with TₚM as derivations. Proposed rows: T_pM (subspace of ℝⁿ, AN3.5) vs TₚM (derivations, AM.3), identified in AM.3; N_pM normal space; ℍᵏ half-space with ∂ℍᵏ = {x_k = 0} (Munkres' convention, last coordinate ≥ 0 — AN3.7 must use the same); O(n), SO(n), SL(n, ℝ), Sym(n), Skew(n). Decide one letter case for the differential across AM.
- **Promise rerouted:** old AN3.2 blueprint's forward hook "surface measure on regular level sets (Part IV)" now runs AN3.2 → AN3.5 `thm-regular-level-set` → AN3.7 → MT.6.
- **exam-targets:** AN3.5 serves no E1 item directly; it is the s-prerequisite of AN3.7 for `pma` "PMA 10" and `pugh` "Pugh 5 後半". Optional: list AN3.5 in those items' notes.
