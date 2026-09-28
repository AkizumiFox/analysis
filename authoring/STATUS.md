# Status

The state of every chapter, the approved exemplar, and the forward promises still to be paid.
Update it when a chapter changes state; drafting agents report, the author edits.

## Exemplar

None approved yet. The pilot chapters are Chapter 1 (Part 0, logic) and Chapter 11 (Part I, the
least upper bound axiom). When the author approves one, name it here: every later chapter
imitates its register, density and exercise design.

Renumbering of 2026-09-28: Part 0's logic went from two chapters to four (modelled on Huth & Ryan
ch. 1–2), so the book has 77 chapters and every chapter from the old Chapter 3 on moved up by two
(old 8 → 10, …, old 75 → 77). The Chapter 1 pilot (`src/ch01-logic-connectives/`) is kept until it
is rewritten as `propositional-natural-deduction`; its prose still carries the old chapter numbers
(Chapter 3, 5, 9, 15), recorded below beside the new targets.

Second renumbering of 2026-09-28 (77 → 78 chapters): the author split Chapter 1 into
`connectives-and-derivations` (Ch 1) and `negation-and-classical-logic` (Ch 2), slower and with one new
rule or idea per section; every chapter from the old Chapter 2 on moved up by one (old 7 → 8 with Gate 0,
old 10 → 11, …, old 77 → 78). The pilot `src/ch01-propositional-natural-deduction/` stays in place until
the drafting agents split it; the targets below use the 78-chapter numbers, and the "Ch 1 §NN" source
columns still name the sections of that pilot.

## Chapters

| Ch | Slug | State |
|---|---|---|
| 1, 2 | connectives-and-derivations, negation-and-classical-logic | split 2026-09-28 from the pilot `propositional-natural-deduction` (still `src/ch01-propositional-natural-deduction/`; `authoring/blueprints/ch02.md` is a copy of the old ch01 blueprint as a starting point), which was rewritten to the four-chapter logic plan 2026-09-28 (7 sections, ~34k words, 104 checked derivations); S2 blueprint, S3 draft, S4 gates, S5 referees A/B, S6 exercises, S7 revision + fresh re-check, S8 seam all passed; **awaiting author review (S9)** — candidate exemplar for Part 0 |
| 11 | least-upper-bound | pilot drafted 2026-09-27; renumbered 2026-09-28; retrofitted to STYLE §11 2026-09-28 (sidecars, R group, ledgers, Time line); S5–S7 re-run after the retrofit (123 ledger items, 0 stale); S8 seam 2026-09-28 (`authoring/reviews/ch11-S8-seam.md`: 0 error, 1 gap, 13 minor; src fixes pending for rows 3–6); **awaiting author review** — candidate exemplar for Parts I–VI |
| 3, 4, 5 | logic block | hand-written blueprints, S2 passed 2026-09-28; not drafted |
| 6, 7, 8 | sets, relations and induction, cardinality (Gate 0) | hand-written blueprints 2026-09-28; S2 pending |
| all others | see `blueprint/book.yaml` | generated blueprints; not started |

## Forward promises

Prose pointers that must become `@ref`s (or be paid off) when the target chapter is written.
Chapter 1 rows use the rewritten chapter's section numbers (2026-09-28, S7); its prose uses the new chapter numbers.

| From | Promise | Target |
|---|---|---|
| Ch 1 §01, §02, §03, §04, §05, §06, §07, index | soundness: truth tables for the connectives, the rules never lead from true premises to a false conclusion, a refuting row rules out every derivation (`thm-soundness`, `cor-refuting-row`); the length and context of a derivation (§02) | Ch 3 |
| Ch 1 §01 | unique readability: a statement built from letters by connectives is read in only one way | Ch 3 |
| Ch 1 §02 | substitution: a derivation stays a derivation under each way of putting statements in for the letters | Ch 3 |
| Ch 1 §05, §06 | ¬¬P ⊢ P is not derivable without RAA, by reading statements with more than two truth values (`thm-raa-independent`, optional there) | Ch 3 |
| Ch 1 §01, §04, §05, §06, §07, index | quantifier rules: "for every" (∀I, "r was arbitrary"; applying a hypothesis "for every ε"), "there exists" (naming a witness k) | Ch 4 |
| Ch 1 §01, §02, index | checking a proof line by line: the rules run silently under written proofs; the rule/phrase table extended to every rule | Ch 5 |
| Ch 1 §03, §06 | the full rule, phrase and Lean dictionary | Ch 5 |
| Ch 1 §04, §06 | the reading ¬P as P → ⊥, and the system of the rules other than RAA (intuitionistic logic); the history of those who declined RAA | Ch 5, final section |
| Ch 1 §06 | spotting a "proof by contradiction" that is a direct proof in disguise | Ch 5 |
| Ch 1 §04 | the lowest-terms fact (L) rests on well-ordering | Ch 7 |
| Ch 1 §03, §04, §05, §06, index | facts about ≤ and absolute value from the ordered-field axioms; existence of square roots of non-negative reals; `thm-sqrt2-irrational` used as is | Ch 11 (paid) |
| Ch 1 §05 | differentiable ⇒ continuous | Ch 17 |
| Ch 11 §02, §05 | the quantifier law "not all" ⇒ "some not" (uses RAA); quantifier negation | Ch 4 |
| Ch 11 §01 C1, §02, §04, §05, §06, §07, index | induction on ℕ (`ax-induction`): n > 0 in exm-sup-one-minus-reciprocal and cor-sup-approximation; the copy of ℕ in an ordered field, and (m + n)·1 = m·1 + n·1 (§01 C1); "ℕ is the smallest inductive set" (§05 remark); x₀ⁿ ≤ x₀ and the claim of thm-nth-root, 2ᵏ > k (§06); I_k ⊆ I_m, 2ⁿ⁻¹ ≥ n, and the one induction of C1 (b) (§07) | Ch 3 |
| Ch 11 index, §05 | sets, images, −A, A + B as images; the intersection of a family of sets (ℕ as the intersection of all inductive subsets of ℝ, §05) | Ch 6 |
| Ch 11 §01, §02, §03, §05, §06, §07, index | every non-empty finite set has a maximum (§02); ℕ closed under + and ·, and (m + n) + 1 = m + (n + 1) (§01 C1); n ≥ 2 ⇒ n − 1 ∈ ℕ; nothing between n and n + 1 (§03 Quick check, §05 A1, §07 B1); well-ordering (lem-integer-part, §05 C1); definition by recursion (powers uⁿ and the finite sum Σ in thm-nth-root; the intervals of thm-reals-uncountable); the power law (t²)² = t⁴ (§07 R2); the arithmetic of ℤ, e.g. no integer m has 2m = 1 (§01 exm-integers-not-a-field, A1) | Ch 7 |
| Ch 11 §05 remark, §06 lem-integer-part, thm-rationals-dense | ℤ closed under +, − and · (used for m = j₀ − p − 1 and for m′ − m in lem-integer-part, and ⌊nx⌋ + 1 in thm-rationals-dense; "positive integer ⇒ natural number" is proved in the §05 remark) | Ch 7 |
| Ch 11 index, §07 | countable = listable with repetitions (image of ℕ); ℕ, ℤ, ℚ countable; a union of two countable sets is countable, and a subset of a countable set is countable (§07 remark after thm-reals-uncountable, the table, C2); diagonal proof via decimals, 0.4999… = 0.5 flagged | Ch 8 (match the definition there) |
| Ch 11 §01, §03, §04, §05 | @eq-abs-interval is the move of limits; sup approximation becomes a limit; "complete" acquires a second meaning | Ch 12 |
| Ch 11 §06, §07 (C4 solution), index | Heine–Borel and the IVT proved by "construct a point as a sup" | Ch 14, Ch 16 |
| Ch 11 §06 | aˣ for irrational x | Ch 20 |
| Ch 11 index, §03, §05, §07 | equivalent forms of completeness | Ch 21 |
| Ch 11 index, §03 | constructing ℝ; uniqueness (prose only, optional) | Ch 22, Ch 23 |

## Blueprint deviations

- Ch 1 (recorded at S7 from S5 Referee B, R4; for S2a to confirm): six labels not in the frozen blueprint's label list carry content the blueprint asks for: `exm-disjunction-first-derivations`, `exm-disjunction-regroup`, `exm-cases-on-hypothesis` (§03); `exm-double-negation-introduction`, `exm-modus-tollens-instance` (§04); `prp-provable-equivalence-basics` (§05).

- Ch 11 (recorded at S7 from S5 Referee B, R6; for S2a to confirm): `lem-field-algebra`, `prp-absolute-value-rules` and `lem-integer-part` are not in the frozen blueprint's label list (they carry facts the blueprint's results need; `lem-field-algebra` now cites `@la:thm-field-basic-properties` for the parts the companion has and proves only −(−a) = a, (c) and (e)). The blueprint's §07 task "the reals not in a given countable set are dense" is now §07 C2 (c). The blueprint names no key proofs (STYLE §11.2).
- Ch 11 (for NOTATION, from S5 Referee B, R5 (b); not changed at S7): rows are wanted for ℝ(x) (the rational functions, §05), \( \sqrt[n]{a} \) / \( a^{1/n} \) (§06), \( U(A) \) (the set of upper bounds, §02 C2, §03 C2) and \( \operatorname{lc} \) (leading coefficient; defined where used in §05 C2 and §07 C3). **Done at S8** (NOTATION rows added, with `\deg`).
- Ch 11 S8 (`authoring/reviews/ch11-S8-seam.md`), src fixes for S7: `lem-field-algebra` cites LA 0.7.1 for the uniqueness of 1 and a⁻¹, which LA leaves to `@la:exr-fields-b1` (gap, row 3); `thm-nth-root` covers only a > 0, while the Ch 1 promise is for non-negative a (add ⁿ√0 = 0, row 4); 06:105 gives powers with u¹ as the base, where Ch 7's `def-power` has u⁰ ≔ 1 (row 5).
- Ch 11 S8, blueprint fixes: ch03.md:195 must list the Ch 11 induction row as paid by `ax-induction`; ch04.md:90 and 197 should say `prp-vacuous-implication` is Chapter 2's; ch06.md:53 lacks the row "ℕ as ⋂ of all inductive subsets", and `def-family-union-intersection` must cover ⋂ of a set of sets; ch07.md:55 still quotes "induction (Chapter 7)" and lacks paying labels for 2m ≠ 1, (t²)² = t⁴ and (m+n)+1 = m+(n+1); part0-logic-overview.md:38 omits 5 cited labels (`exm-abs-product-cases`, `exm-triangle-inequality-cases` → Ch 1; `exm-square-plus-one`, `prp-equivalence-cycle`, `exr-negation-and-contradiction-c1` → Ch 2; keep the slug `negation-and-contradiction` or the C1 label). ch01.md and ch02.md are still identical copies of the old blueprint, so re-run S8 check (a) when the split is written.
- Ch 11 → Ch 7 blueprint (from S5 Referee B, R2): the Ch 7 blueprint opens a promise to Ch 11, that `@def-supremum` gains a clause pointing back to `def-order-supremum`; schedule it when Ch 7 is drafted.

## Engine and convention notes from the pilot

- Fitch derivations use fitch.sty (`latex/fitch-book.sty`, `nd` environment in a raw LaTeX block); the website gets build-time SVGs through filters/tikz.lua. Converted from the pilots' arrays on 2026-09-28.
- Line ranges in justifications: `\lines{2}{5}` (no non-ASCII in math, test_display_math_source).
- A paragraph opening "(a) …" becomes a Pandoc list: one lettered item per paragraph, or italic `*(a) ⇒ (b).*`.
- `enumerate` does not take a constant label such as `label=(L)`.
- `blueprint/originality.py` ignores n-grams made only of stock vocabulary (STOCK); both pilots report 0 at n = 8.

## Open engineering items

- `tools/seed_errors.py` does not skip `% schema` blocks yet.
- `tools/check_numbers.py` is advisory (`NUMBERS_FATAL = False`) until Chapter 1's three unprinted QUOTED values (the three-valued 1/2 in prp-peirce and exr-finding-derivations-b1) are resolved in S7.
- The PDF running head overflows for long section titles (e.g. Chapter 1 §01); needs a short-title mechanism in the engine.
