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

## ch07 (CA.15, optional), S1, 2026-10-25

- **STATUS.md:** add the row CA.15 → `ca2/authoring/blueprints/ch07.md`, state "S1 done, awaiting S2a" (new chapter; no old stub in ca/).
- **Promise from CA.7 paid:** σ as the genus-2 canonical product (`thm-sigma-entire`, CA.15 §05), citing CA.7 `lem-elementary-factor-bound`, `thm-holomorphic-product`, `thm-product-log-derivative`.
- **plan-edges.yaml (math-atlas):** currently `CA.15: {s: [CA.7], see: [CA.13]}`. The blueprint also cites CA.2, CA.3, CA.4, CA.10 (ancestors through CA.7, no change needed) and, in §06–§07 only, CA.5 (Schwarz reflection), CA.8a (continuation along paths, path lifting) and CA.14 (prose comparison, R1). Proposed: add `b: [CA.8a]` (or `s` if the coordinator prefers, since `thm-elliptic-integral-inversion` and `cor-picard-via-lambda` use it), and `see: [CA.14]`. CA.5 is an ancestor of CA.7 via CA.11? check; if not, add `b: [CA.5]`.
- **NOTATION.md:** new rows Λ, Λ*, ω₃ = ω₁ + ω₂, τ = ω₂/ω₁ with Im τ > 0; P_a (period parallelogram); ℘ (`\wp`), G_k(Λ), g₂ = 60G₄, g₃ = 140G₆, e_j = ℘(ω_j/2), Δ = g₂³ − 27g₃²; **ζ_Λ** for the Weierstrass zeta (never bare ζ: CA.13 owns ζ for Riemann zeta); σ_Λ; η_j quasi-periods; λ(τ), Γ(2).
- **exam-targets.yaml:** no change; CA.15 is the sole cover of `ahlfors` item "Ahlfors 7 橢圓函數". Coverage note: the blueprint also uses Stein–Shakarchi II ch. 9 (outside the S&S ch. 5–6, 8 named for CA2) for coverage.
- **CA.8b (ch08):** may point at CA.15 `def-modular-lambda` / `thm-lambda-mapping` in prose only; CA.15 is optional, so CA.8b must not prove anything from it.

## ch03 (CA.12), S1, 2026-10-25

1. **STATUS.md:** add the row CA.12 → `ca2/authoring/blueprints/ch03.md`, state "S1 done, awaiting S2a" (new chapter; the old `ca/authoring/blueprints/ch07.md` §7 Runge section is superseded, as the CA.7 note already says).
2. **plan-edges.yaml (math-atlas):** `CA.12: {s: [CA.4, CA.7]}` → `{s: [CA.4, CA.7, CA.5]}`. CA.5 (Riemann mapping theorem, for condition (i)) and, through it, CA.6 (harmonic conjugates, for condition (j)) are used in `thm-simply-connected-equivalences`; neither is an ancestor via CA.4 or CA.7. If the edge is refused, (i) and (j) become a stated remark and the theorem keeps (a)–(h).
3. **CA workflow (owner of ca/), requests:**
   - CA.5: state the Riemann mapping theorem (or a remark after it) under the hypothesis "every non-vanishing holomorphic function on G has a holomorphic square root", since its proof uses simple connectivity only there. CA.12 (h)⇒(i) needs that statement, not an inspection of the proof (S2a item 9).
   - CA.4: confirm (i) simple connectivity is defined by closed-path homotopy (CA.8a asks the same); (ii) CA.4 proves log and √ of non-vanishing functions on simply connected regions, the open mapping theorem, and the global Cauchy integral formula for cycles with n(Γ, a) = 0 off the region; give the labels.
   - CA.2: labels for the maximum modulus principle on bounded regions, Cauchy's formula on convex open sets, the Weierstrass convergence theorem, the identity theorem.
4. **CA.7 (ca2 ch02):** CA.12 owns the proof of `thm-weierstrass-region` (no new label; §6 restates it) and pays the interpolation pointer of CA.7 §06 C1 (`thm-interpolation`). Because Mittag-Leffler in ℂ left CA.7, CA.12 §5 proves `thm-mittag-leffler-plane` first (Taylor corrections) and introduces the telescoping-correction move there. To avoid a duplicate label CA.12 uses `cor-meromorphic-quotient-region` (CA.7 keeps `cor-meromorphic-quotient` for ℂ).
5. **CA.8a (ca2 ch05):** `exm-every-region-natural-domain` may cite CA.12 `thm-no-extension` (proved, with the construction of the accumulating sequence) instead of resting on a stated theorem; needs `see: [CA.12]` or `b: [CA.12]` in plan-edges.
6. **NOTATION.md:** new rows R(E) (rational functions with all poles in E ⊂ ℂ∞); "hole" of a compact K (bounded component of ℂ∖K); K_n = {|z| ≤ n, dist(z, ℂ∖G) ≥ 1/n} as the book's standard exhaustion; H(G) as in CA.5.
7. **exam-targets.yaml:** no change. CA.12 serves `complex` "Runge、Mittag-Leffler" (sole cover) and `ahlfors` items 4 (simply connected regions, with CA.4) and 5 (with CA.7, CA.13).

## ch01 (CA.11), S1, 2026-10-25

1. **STATUS.md:** add the row CA.11 → `ca2/authoring/blueprints/ch01.md`, state "S1 done, awaiting S2a" (new chapter; built from the second half of `ca/authoring/blueprints/ch06.md`, copied not moved — CA owns that file).
2. **Scope against the old CA.6 stub:** Harnack (inequality, principle), subharmonic functions, Perron, barriers and Green's function moved here (constraint 2026-10-25). Perron is now proved in full (was outline-level); barriers proved for the segment condition and, in a starred subsection, for any point on a non-degenerate complementary component; Green's function is main line and yields a second proof of the Riemann mapping theorem (`thm-green-riemann-map`).
3. **CA workflow (owner of ca/), requests:**
   - CA.6: confirm labelled results for (a) mean value property, (b) maximum principle incl. the bounded-region limsup form, (c) Poisson integral solves the disc Dirichlet problem, (d) continuous + mean value property ⇒ harmonic, (e) locally uniform limits of harmonic functions are harmonic, (f) harmonic conjugates on simply connected regions. If (d) or (e) left CA.6, CA.11 §01 proves them as a lemma. CA.6 should carry a forward pointer "subharmonic functions, Harnack and Perron: CA.11"; its labels must not take `thm-harnack-inequality` / `thm-harnack-principle` (the old stub had Harnack in CA.6).
   - CA.4: labels for (i) the existence of a holomorphic log of g on G when ∫_γ g′/g = 0 for all cycles γ in G; (ii) the compact-set cycle lemma (Γ in Ω ∖ K, n(Γ,·) = 1 on K, 0 off Ω); (iii) the argument principle for cycles. CA.11 states its simply-connected results with the hypothesis "ℂ̂ ∖ Ω connected"; please say whether CA.4 proves the equivalence with its own definition (CA.8a and CA.12 notes ask about the definition too).
   - CA.5: labels for Schwarz's lemma and the RMT uniqueness clause.
4. **plan-edges.yaml (math-atlas):** `CA.11: {s: [CA.6, CA.5]}` is enough (CA.4, CA.2, CA.10, AN2.5 are ancestors). Proposed see-edges: `CA.12 see CA.11` (Dirichlet regions / Green's function among the simply-connected equivalences, as a remark), `PDE.1 see CA.11` and `PDE.6 see CA.11` (planar Perron and barriers, alongside the existing see CA.6), `CA.9 see CA.11` (Harnack for positive harmonic functions; or add CA.11 to CA.9's s if its blueprint cites `thm-harnack-inequality`). CA.7 needs no edge (prose pointer from Jensen only, as the ch02 note says).
5. **Answer to the ch07 note's question:** CA.5 is not an ancestor of CA.7 through CA.11 (CA.7's edges are s [CA.3, CA.4]; CA.11 is not an ancestor of CA.7).
6. **NOTATION.md:** new rows A_v(a, r) (circle average), v_D (harmonic replacement on the disc D), 𝔓(f) / 𝔓(f, Ω) (Perron family), u_f (Perron function), g_Ω(z, a) (Green's function).
7. **exam-targets.yaml:** no change. CA.11 is the sole cover of `complex` "次調和函數、Harnack、Perron 方法" and covers the Perron/Green part of `ahlfors` "Ahlfors 6 共形映射與 Dirichlet 問題" with CA.5.
