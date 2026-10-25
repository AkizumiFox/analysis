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
