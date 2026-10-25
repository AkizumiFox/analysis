# CA coordinator notes

Changes to shared files (STATUS.md, NOTATION.md, ...) requested by CA blueprint runs. Each entry names its chapter.

## CA.4 (ch05) — S1, 2026-10-25

- **File slot.** CA.4 now lives at `ca/authoring/blueprints/ch05.md` (spec/08 §D1 position 5). Its old blueprint was `ch04.md` (left in place for the CA.3 run to overwrite). The old CA.5 blueprint that used to be `ch05.md` is overwritten by this commit; recover it with `git show 9f4b861a/authoring/blueprints/ch05.md` (CA.5 now goes to ch07). A CA.5 run must **not** `git mv ch05.md ch07.md` after this commit.
- **STATUS.md:** CA.4 row → CA chapter 5, directory `ca/src/ch05-winding-numbers-global-cauchy/`, state S1 done, next S2a.
- **NOTATION.md:** add n(γ, a) (winding number; Ind_γ(a) mentioned once), γ* (trace), γ ∼ 0 (Ω) (homologous to zero), γ₀ ≃ γ₁ (Ω) (homotopic closed curves), ord_a f (order, negative at poles).
- **Label reconciliation:** ch05 cites CA.1–CA.3 results with *expected* labels in brackets; reconcile after those S1 runs freeze.
- **Atlas registry (math-atlas, for whoever edits it):** no edge change needed; plan-edges `CA.4: {s: [CA.3, AN2.3], see: [CA.10]}` matches. `thm-three-lines` is kept in CA.4 for PDE.3.

## CA.6 (ch06) — S1, 2026-10-25

- **File slot.** CA.6 stays at `ca/authoring/blueprints/ch06.md` (spec/08 §D1 position 6; the old CA.6 blueprint was already in this slot and is rewritten in place).
- **STATUS.md:** CA.6 row → title "Harmonic Functions and the Poisson Integral", CA chapter 6, directory `ca/src/ch06-harmonic-functions/`, state S1 done, next S2a.
- **NOTATION.md:** add Δ (Laplacian), P(z, ζ) and P_r(θ) (Poisson kernel), P[g] (Poisson integral), 𝕋 (unit circle), ℍ (upper half-plane) if not already there.
- **blueprint/book.yaml (ch 60 entry, shared):** per the 2026-10-09 constraint, remove the external_prerequisites entries "Poisson kernel, Abel summability and Fourier series of continuous functions (Part III)" and "Green's theorem and Green's identities (Part IV …)" for `harmonic-functions` (the new blueprint uses neither); update title/outline/must_prove to the cut chapter (Harnack, reflection, subharmonic, Perron removed).
- **math-atlas registry/plan-edges.yaml (proposed, coordinator decides):** `CA.6: b [CA.10]` (scope: disc automorphisms φ_a, Cayley map; used for the main Poisson derivation and the half-plane section; the Poisson formula also has a CA.2-only proof, so `see` would also do) and `see [CA.4]` (one remark: conjugates on simply connected regions). Both targets precede CA.6 in reading order.
- **For the CA.5 run:** reflection by harmonic continuation should cite `thm-mvp-implies-harmonic` and `thm-harmonic-mvp`; CA.6 §6 has an unlabelled remark (odd reflection of a function harmonic off ℝ has the mean value property on circles centred on ℝ) and leaves the reflection theorem itself to CA.5. CA.6's index hook ("Im f → 0 on the diameter: can f be continued?") is to be paid there.
- **For the CA.11 run (CA2):** Harnack is not named in CA.6; the kernel bound (1 − r)/(1 + r) ≤ P ≤ (1 + r)/(1 − r) is CA.6 exercise `ex-poisson-kernel-bounds` (§4 B1), and the punctured-disc example `exm-punctured-disc-dirichlet` is the first irregular point to name.
- **Label reconciliation:** ch06 cites CA.2 results (Cauchy formula, Gauss mean value, maximum modulus, primitives on a disc, holomorphic integrals, Liouville) and CA.10 (φ_a, Cayley) by description; insert labels once those S1 runs freeze.

## CA.2 (ch03) — S1, 2026-10-25

- **File slot.** CA.2 now lives at `ca/authoring/blueprints/ch03.md` (spec/08 §D1 position 3). Written fresh rather than `git mv ch02.md ch03.md`, so the CA.10 run's ch02.md is untouched. The old CA.3 blueprint that used to be `ch03.md` is overwritten by this commit; recover it with `git show 20a9503a/authoring/blueprints/ch03.md` (CA.3 now goes to ch04). The old CA.2 blueprint stays recoverable at `git show 20a9503a/authoring/blueprints/ch02.md`.
- **STATUS.md:** CA.2 row → CA chapter 3, directory `ca/src/ch03-cauchy-theorem/`, state S1 done, next S2a.
- **NOTATION.md:** add D(a, r), D̄(a, r), C(a, r) (positively oriented circle), ∂T (triangle boundary, counterclockwise), [z, w] (segment as a curve), "locally uniformly", ord_a f (shared with CA.4's entry).
- **math-atlas registry/plan-edges.yaml (proposed, coordinator decides):** `CA.2: b [AN3.4]` → `see [AN3.4]`: the blueprint proves the derivative formula by difference quotients and parameter integrals by Riemann sums, so no differentiation-under-the-integral theorem is used. Add `see [CA.10, AN2.11, AN2.6]` (CA.10: φ_a in §4 C2 and R1; AN2.11: real Γ in examples; AN2.6: Weierstrass approximation in a warning and a find-the-error item). All precede CA.2 in reading order.
- **Labels other runs should use** (CA.2 S1 names): `thm-goursat`, `thm-disc-primitive`, `thm-cauchy-disc`, `cor-cauchy-convex`, `lem-circle-kernel`, `thm-cauchy-formula-disc`, `thm-holomorphic-analytic`, `cor-holomorphic-infinitely-differentiable`, `cor-cauchy-formula-derivatives`, `cor-taylor-largest-disc`, `thm-cauchy-estimates`, `thm-liouville`, `cor-polynomial-growth`, `thm-fta`, `thm-morera`, `def-locally-uniform`, `thm-weierstrass-limits`, `cor-series-holomorphic`, `thm-holomorphic-param-integral`, `thm-identity`, `thm-zeros-isolated`, `cor-identity-power-series`, `thm-mean-value-property`, `thm-max-modulus`, `cor-max-boundary`, `cor-min-modulus`.
- **For the CA.3 run:** the two-circles (annulus) lemma and the removable-singularity theorem are *not* in CA.2 and fall to CA.3; open mapping and ∮ dz/z over a triangle around 0 fall to CA.4.
- **For the CA.1 run:** CA.2 cites, by expected name, `def-holomorphic`, `def-region` (CA.2 §6 defines it if CA.1 does not), `def-contour-integral`, `thm-ml-inequality`, `thm-primitive-closed-curve`, `thm-power-series-holomorphic`, `thm-derivative-zero-constant`, and needs e^z = 1 ⇔ z ∈ 2πiℤ.
