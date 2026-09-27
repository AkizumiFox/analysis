# Design decisions (record)

These decisions were made on 2026-09-27, across two planning conversations and the plan that followed them. `curriculum.md` (same directory) holds the stage-by-stage content specification, and `sources.md` holds the reference books and their roles. Blueprints and chapters follow this file. When a decision changes, edit this file and say why.

## The book
- **One book, seven Parts, written in English first.** A Chinese edition comes later; the engine has no CJK support yet (xelatex + ctex, interface strings and spell check all still to do).
- **The reader** is a motivated student who has never written a proof. By the end of Part VI they reach the level of a graduate qualifying exam in analysis. As benchmarks, the UCLA real and complex quals set the floor and the ceiling, and Fredholm theory, Sobolev spaces and Lax–Milgram are added from Cambridge Part II.
- **Linear algebra is not re-taught.** Our linear-algebra book (linear-algebra.akizumifox.com) is the companion text. It is cited by chapter, in prose, because the engine cannot `@ref` another book.

| Part | Title (working) | Course stage |
|---|---|---|
| 0 | Foundations: logic, sets, cardinality (+ optional ZF, ℕ, ℤ, ℚ) | three-year route, first semester; two-year route, a 3–4 week bridge (logic and sets only) |
| I | Analysis on the real line (+ optional Dedekind cuts and uniqueness of ℝ at the end) | S1 |
| II | Metric spaces and several variables | S2 |
| III | Fourier analysis (Riemann setting) | Summer 1 |
| IV | Measure and integration | S3 |
| V | Complex analysis | S3 (read alongside IV, or after it) |
| VI | Functional analysis and distributions | S4, ending with the Dirichlet-problem capstone |

## Structural decisions
1. **Proof skills are practised inside analysis, not in a separate logic course.** Part 0's logic is short, and every rule it introduces comes with an example from real analysis.
2. **Logic is taught through natural deduction, as the grammar of proof.**
   - Each connective is defined by its introduction and elimination rules, and truth tables come afterwards, as a summary of the rules.
   - A central table lines up rule, phrase in mathematical writing and Lean tactic.
   - A worked example annotates "uniformly continuous ⇒ continuous" step by step and shows, rule by rule, why the converse fails: an ∃-intro witness may not depend on a variable introduced later.
   - A catalogue of "what is not allowed" lists common errors and the rule each one violates, and Fitch boxes make the scope of assumptions visible.
   - The vacuous truth of implication is derived from ⊥-elimination.
   - A definition's "if" means "iff"; this is a convention of language, not a rule of logic.
3. **The last section of the logic chapter is the dispute over excluded middle.**
   - LEM, double-negation elimination and proof by contradiction are one extra rule, and intuitionistic logic still proves ¬¬(P ∨ ¬P).
   - The BHK reading of the connectives.
   - Irrational numbers a and b with aᵇ rational, proved with and without a witness: √2^√2 versus √2^(log₂9) = 3.
   - The history: Brouwer 1908, Hilbert's reply of 1927 and the Grundlagenstreit, Heyting 1930, the Gödel–Gentzen double-negation translation, and Bishop 1967.
   - Its consequences for analysis: sup of a located set, Specker's sequence, the approximate intermediate value theorem, the non-constructive step in Bolzano–Weierstrass.
   - Curry–Howard; Lean's `Classical.em` via Diaconescu, and `noncomputable`.
   - The main line stays classical.
4. **The number systems are constructed on a route beside the main line.**
   - Part 0 builds ℕ (Peano), ℤ and ℚ (equivalence classes) and ℝ (Dedekind cuts). It ends with the uniqueness of the complete ordered field, the bridge between "assume the axiom" and "build a model".
   - Part I opens from the **least upper bound axiom** (environment `ax`, label `ax-least-upper-bound`) and depends on no Part 0 construction. The constructions are `.optional`, so no main-line proof may cite them.
   - Routine verifications (the operations are well defined, the field axioms hold) are left mostly as exercises, to avoid becoming Landau.
   - **Placement (settled at the merge, 2026-09-27):** ZF with ℕ, and ℤ with ℚ, are optional chapters at the end of Part 0. The Dedekind-cut construction of ℝ and the uniqueness theorem are optional chapters at the **end of Part I**, after "The Forms of Completeness". They need Part I Chapter 1's ordered-field axioms, and a proof may not cite a later chapter, so this placement is forced. It also carries out the old recommendation to read Part I first and come back to the constructions.
   - **The axiom of choice is on the main line.** It is stated as `ax-choice` in Part 0's cardinality chapter, because Vitali, Hahn–Banach and Tychonoff cite it. Zorn's lemma is proved from it just in time, in Part VI's Hahn–Banach chapter.
5. **Cauchy completion is a spiral node in Part II.** The completion of a metric space, applied to ℚ, gives ℝ a second time; Lᵖ later reappears as a completion too.
6. **The spiral.** Convergence, completeness, compactness and continuity each return on ℝ, on ℝⁿ, on metric spaces and C(K), on normed and Banach spaces, on Hilbert spaces, and on Lᵖ and the weak* topology (see the spiral table in `curriculum.md`). When a concept comes back at a higher stage, the text explicitly recalls the earlier version.
7. **Every abstraction is forced by a concrete problem.**
   - ODE existence leads to contraction maps and Arzelà–Ascoli.
   - Whether Fourier series converge leads to the list of what the Riemann integral lacks, and so to Lebesgue.
   - The Dirichlet problem leads to Hilbert spaces and Lax–Milgram.
   - Polynomial approximation leads to Stone–Weierstrass.
8. **Point-set topology is split into three places.**
   - End of Part II: topological spaces, Hausdorff, compactness, quotients.
   - Start of Part IV: Urysohn and Tietze (locally compact Hausdorff), needed for Lusin and the density of C_c.
   - Part VI, just before Alaoglu: Tychonoff (with Zorn), plus the diagonal proof in the separable case.
9. **Load moved out of measure theory into Part VI.** Lᵖ duality, the Riesz–Markov theorem for C(K)*, weak topologies and abstract Hilbert space theory all go in Part VI. Part IV uses L² only for the von Neumann proof of Radon–Nikodym.
10. **Fubini–Tonelli and change of variables are proved in full** in Part IV. Part II covers the Riemann integral on ℝⁿ: Jordan content, Fubini for continuous functions, and linear change of variables.
11. **Complex analysis covers the qualifying-exam "second layer".** That means harmonic functions and Harnack, subharmonic functions, normal families, Hurwitz, infinite products, Weierstrass and Mittag-Leffler, Hadamard (in outline), analytic continuation and monodromy, Schwarz reflection, and little Picard.
12. **Differential forms and Stokes are deferred.** They are not in the main line, but a Green's theorem node (rectangle and disc) is kept, because harmonic functions and PDE need it.
13. **Abstract algebra is taught just in time.** Groups and characters appear with Fourier analysis on finite abelian groups (Part III). Ideals and quotients appear with Gelfand theory, an optional section of Part VI.
14. **Cross-cutting skills are named and recur**, in Quick checks, warnings and C-exercises:
    - quantifier management;
    - ε allocation;
    - extracting subsequences, including the diagonal argument and weak compactness;
    - density arguments;
    - a checklist for exchanging limits;
    - approximation machinery;
    - Baire arguments;
    - duality arguments;
    - self-explanation;
    - proof verification (finding the error).
15. **Every chapter ends with exit checks.** These are C-level exercises taken from the "exit check" items in `curriculum.md`. Examples include proving that a continuous function on [a,b] is uniformly continuous in two different ways, and the capstone at the end of Part VI.

## Reading paths (`config.json` `reading-paths`)
- `two-year`: Part 0 logic and sets without the constructions, then Parts I–VI.
- `three-year`: everything, including the constructions.
- Narrower paths: `measure-only` (up to Radon–Nikodym), `complex-only`, and `foundations` (Part 0 alone).

## Source policy
- Original prose only. The converted reference books (`~/coding/analysis/converted/`) may be used to check truth and coverage and for nothing else.
- `blueprint/originality.py` flags shared n-grams against the source sections listed for each chapter.
- Converted text is never committed.

## Deferred on purpose
- The one-node-per-file YAML knowledge graph, `term:` links, natural-deduction rule tags on proof steps, and `uses_choice` / `nonconstructive` flags. For now the engine's `@ref` graph, `graph.json` and the reading paths stand in for them.
- The Chinese edition.
