# CA2 coordinator notes

Changes to shared files and other volumes requested by CA2 workflow agents. Agents append; the coordinator applies.

## ch02 (CA.7), S1, 2026-10-25

- **STATUS.md:** add the row CA.7 → `ca2/authoring/blueprints/ch02.md`, state "S1 done, awaiting S2a"; the old row pointing at `ca/authoring/blueprints/ch07.md` (CA owns that file; it was copied, not moved) should be retired or marked "moved to CA2".
- **Scope change against the old stub:** Γ moved to CA.13; Mittag-Leffler and Runge moved to CA.12; Hadamard is now proved in full (exam-targets `complex` item "Weierstrass 乘積、Hadamard"), not outlined.
- **Promise to CA.12:** prove Weierstrass factorization in an arbitrary open set (`thm-weierstrass-region`, stated in CA.7 §02). If CA.12's blueprint declines it, CA.7 gets an optional section for it. Also suggested for CA.12: general interpolation f(aₙ) = cₙ as an exercise.
- **Promises to CA.13 / CA.14 / CA.15:** 1/Γ as a genus-1 product (CA.13); little Picard without the finite-order hypothesis (CA.14; CA.7 §06 C2 proves the finite-order case); σ-function as a genus-2 canonical product (CA.15).
- **plan-edges.yaml (math-atlas):** `CA.8a: s [CA.4, CA.7]` — CA.7 supplies only holomorphic products; check whether a `see` edge suffices.
- **Prerequisite question for the CA workflow:** which CA chapter carries the Weierstrass convergence theorem (locally uniform limits of holomorphic functions, derivatives converge)? CA.7 needs it from CA.2 or CA.4 (ancestors); CA.5 is not an ancestor.
- **NOTATION.md:** new rows M_f(r), n_f(r), E_p (Weierstrass elementary factor), ρ_f (order), ρ₁ (exponent of convergence).
