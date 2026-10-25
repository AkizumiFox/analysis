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

## ch05 (CA.8a), S1, 2026-10-25

1. **STATUS.md:** add the row CA.8a → `ca2/authoring/blueprints/ch05.md`, state "S1 done, awaiting S2a". The old `ca/authoring/blueprints/ch08.md` (CA owns it; copied, not moved) should be retired or marked "moved to CA2". Bloch/Landau/Picard/Schottky now go to CA.14, the theta/modular route to CA.8b, Γ/ζ continuation to CA.13; Gate V dropped.
2. **Prerequisite question for the CA workflow:** the monodromy route assumes CA.4 defines "simply connected" by closed-path homotopy (every closed path homotopic in G, through closed paths, to a constant). If CA.4 uses the homology (winding-number) definition, CA.8a needs a different step (i) in `thm-monodromy-simply-connected`; please confirm the CA.4 label.
3. **CA.7 / CA.12:** the §5 remark `exm-every-region-natural-domain` cites CA.7 `thm-weierstrass-region` (stated in CA.7, proof promised to CA.12). CA.12 is not an s-edge of CA.8a; either keep the remark labelled "rests on a stated theorem" or add `see CA.12`. This is also the only use of CA.7 in CA.8a, so the `CA.8a s CA.7` edge could become `see` (agrees with the ch02 note).
4. **plan-edges.yaml (math-atlas):** `CA.8a b AN2.11` is now used only for real Γ facts (Γ(1/2) = √π, Γ(x+1) = xΓ(x)) in a Quick check previewing CA.13; consider downgrading to `see AN2.11`.
5. **Promises opened:** to CA.13, apply `prp-functional-equation-continuation` to Γ and answer the ζ(−1) hook; to CA.14, cite `cor-roots-and-logs-by-monodromy` / `thm-monodromy-simply-connected` for branches and point to the lifting route in prose; to CA.8b, use `thm-lift-local-homeomorphism` with the modular function.
6. **NOTATION.md:** new rows: function element (f, D); germ [f]ₐ; continuation along γ as (f_t, D_t)_{t∈[0,1]}; γ·σ (concatenation), γ⁻ (reverse path).
7. **Volume order:** spec/08 §D2 numbers CA.13 as ch04 before CA.8a (ch05), but CA.13 s-depends on CA.8a; the file numbering ch04/ch05 should be swapped when the book is set up (README already notes the swap).
