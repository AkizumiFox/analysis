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
