# CA coordinator notes

Changes to shared files (STATUS.md, NOTATION.md, ...) requested by CA blueprint runs. Each entry names its chapter.

## CA.4 (ch05) — S1, 2026-10-25

- **File slot.** CA.4 now lives at `ca/authoring/blueprints/ch05.md` (spec/08 §D1 position 5). Its old blueprint was `ch04.md` (left in place for the CA.3 run to overwrite). The old CA.5 blueprint that used to be `ch05.md` is overwritten by this commit; recover it with `git show 9f4b861a/authoring/blueprints/ch05.md` (CA.5 now goes to ch07). A CA.5 run must **not** `git mv ch05.md ch07.md` after this commit.
- **STATUS.md:** CA.4 row → CA chapter 5, directory `ca/src/ch05-winding-numbers-global-cauchy/`, state S1 done, next S2a.
- **NOTATION.md:** add n(γ, a) (winding number; Ind_γ(a) mentioned once), γ* (trace), γ ∼ 0 (Ω) (homologous to zero), γ₀ ≃ γ₁ (Ω) (homotopic closed curves), ord_a f (order, negative at poles).
- **Label reconciliation:** ch05 cites CA.1–CA.3 results with *expected* labels in brackets; reconcile after those S1 runs freeze.
- **Atlas registry (math-atlas, for whoever edits it):** no edge change needed; plan-edges `CA.4: {s: [CA.3, AN2.3], see: [CA.10]}` matches. `thm-three-lines` is kept in CA.4 for PDE.3.
