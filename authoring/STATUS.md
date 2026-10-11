# Status

The state of every chapter, the approved exemplar, and the forward promises still to be paid.
Update it when a chapter changes state; drafting agents report, the author edits.

**Split of 2026-10-12.** analysis-book was split into per-volume books (math-atlas spec/06, "系列與冊"). Chapters are named here by their atlas id (`F1.4`, `F2.1`, `AN1.1`: math-atlas `registry/chapters.yaml`; `python3 tools/series.py show` lists them with their volume and local number), so the tables survive renumbering. This file keeps the chapters and promises of the `analysis` repository; rows of the other repository's chapters live in its STATUS.md. The renumbering notes below use analysis-book's 78-chapter numbers.

## Exemplar

None approved yet. The pilot chapters are F1.1 (Part 0, logic) and AN1.1 (Part I, the
least upper bound axiom). When the author approves one, name it here: every later chapter
imitates its register, density and exercise design.

Renumbering of 2026-09-28: Part 0's logic went from two chapters to four (modelled on Huth & Ryan
ch. 1–2), so the book has 77 chapters and every chapter from the old Chapter 3 on moved up by two
(old 8 → 10, …, old 75 → 77). The Chapter 1 pilot (`src/ch01-logic-connectives/`) was then
rewritten as `propositional-natural-deduction`, and that in turn was split (next paragraph); neither
directory exists any more.

Second renumbering of 2026-09-28 (77 → 78 chapters): the author split Chapter 1 into
`connectives-and-derivations` (Ch 1) and `negation-and-classical-logic` (Ch 2), slower and with one new
rule or idea per section; every chapter from the old Chapter 2 on moved up by one (old 7 → 8 with Gate 0,
old 10 → 11, …, old 77 → 78). The pilot `src/ch01-propositional-natural-deduction/` has since been split
into `src/ch01-connectives-and-derivations/` and `src/ch02-negation-and-classical-logic/` (drafted
2026-09-28) and no longer exists; the targets below use the 78-chapter numbers, and the "Ch 1 §NN" and
"Ch 2 §NN" source columns name the sections of the split chapters (Ch 1 rows reconciled at Ch 1 S7, round 1).

## Chapters

| Chapter | Slug | State |
|---|---|---|
| AN1.1 | least-upper-bound | pilot drafted 2026-09-27; renumbered and retrofitted to STYLE §11 2026-09-28; **passed S2–S8 2026-09-28** (S5–S7 re-run after the retrofit; seam `an1/authoring/reviews/ch01-S8-seam.md`: src rows 3–5 applied, optional rows 2 and 6 not); induction now cites `@ax-induction` (cross-chapter cleanup); **awaiting author review (S9)** — candidate exemplar for Parts I–VI |
| all others | see `blueprint/book.yaml` | generated blueprints; not started |

## Forward promises

Prose pointers that must become `@ref`s (or be paid off) when the target chapter is written.
Chapter 1 rows use the sections of `connectives-and-derivations` (reconciled at its S7, 2026-09-28); rows for material that moved to Chapter 2 at the split are filed under Ch 2 with its sections.

| From | Promise | Target |
|---|---|---|
| AN1.1 §02, §05 | the quantifier law "not all" ⇒ "some not" (uses RAA); quantifier negation | F1.4 (paid: `prp-quantifier-negation` (a), `prp-bounded-quantifier-negation`) |
| AN1.1 §01 C1, §02, §04, §05, §06, §07, index | induction on ℕ (`ax-induction`): n > 0 in exm-sup-one-minus-reciprocal and cor-sup-approximation; the copy of ℕ in an ordered field, and (m + n)·1 = m·1 + n·1 (§01 C1); "ℕ is the smallest inductive set" (§05 remark); x₀ⁿ ≤ x₀ and the claim of thm-nth-root, 2ᵏ > k (§06); I_k ⊆ I_m, 2ⁿ⁻¹ ≥ n, and the one induction of C1 (b) (§07) | F1.3 (paid: `@ax-induction`, cited at index, 01 C1 hint, 02:169, 05:43, 05:58, 06 C2, 07:52; the ledgers name it) |
| AN1.1 index, §05 | sets, images, −A, A + B as images; the intersection of a family of sets (ℕ as the intersection of all inductive subsets of ℝ, §05) | F2.1 (paid: `def-image` and `exm-sets-of-numbers-as-images` (§06); `def-family-union-intersection` (⋂𝒮 for a non-empty set of sets) and `prp-smallest-closed-set` (§02). AN1.1 has passed S8, so its pointers change only with the author's consent) |
| AN1.1 §01, §02, §03, §05, §06, §07, index | every non-empty finite set has a maximum (§02); ℕ closed under + and ·, and (m + n) + 1 = m + (n + 1) (§01 C1); n ≥ 1 ⇒ n − 1 ∈ ℕ; nothing between n and n + 1 (§03 Quick check, §05 A1, §07 B1); well-ordering (lem-integer-part, §05 C1); definition by recursion (powers uⁿ and the finite sum Σ in thm-nth-root; the intervals of thm-reals-uncountable); the power law (t²)² = t⁴ (§07 R2); the arithmetic of ℤ, e.g. no integer m has 2m = 1 (§01 exm-integers-not-a-field, A1) | F2.2 (paid: the finite maximum by `prp-finite-max`, for lists of reals, its proof valid in any ordered field, set → list being F2.3's; ℕ closed under + and · by `lem-naturals-arithmetic` (b); n ≥ 1 ⇒ n − 1 ∈ ℕ by `lem-naturals-arithmetic` (c); nothing between n and n + 1 by `lem-naturals-arithmetic` (e), and "an integer > 3 is ≥ 4" (03:68, 06:201) by `prp-integers-closed` (c); well-ordering by `thm-well-ordering` (lem-integer-part), and 05:399 by `cor-well-ordering-integers`, for an integer lower bound only; definition by recursion by `thm-recursion`, `cor-recursion-from-base`, `def-power`, `def-sum-product`; (t²)² = t⁴ by `prp-power-laws` (b); no m with 2m = 1 (§01 A1) by `thm-division-algorithm`, uniqueness. Not named by the S3 replies: (m + n) + 1 = m + (n + 1)) |
| AN1.1 §05 remark, §06 lem-integer-part, thm-rationals-dense | ℤ closed under +, − and · (used for m = j₀ − p − 1 and for m′ − m in lem-integer-part, and ⌊nx⌋ + 1 in thm-rationals-dense; "positive integer ⇒ natural number" is proved in the §05 remark) | F2.2 (paid: `prp-integers-closed`; \( \nZ_{>0} = \{ n \in \nZ : n > 0 \} \) by `prp-integers-closed` (b); "ℕ is the smallest inductive set" by `ax-induction` with the set-form remark of §01) |
| AN1.1 index, §07 | countable = listable with repetitions (image of ℕ); ℕ, ℤ, ℚ countable; a union of two countable sets is countable, and a subset of a countable set is countable (§07 remark after thm-reals-uncountable, the table, C2); diagonal proof via decimals, 0.4999… = 0.5 flagged | F2.3 (match the definition there; paid: `def-countable`, matching AN1.1's wording; ℕ, ℤ, ℚ by `thm-integers-rationals-countable`; two countable sets by `prp-union-two-countable`; a subset by `prp-countable-subset`; the index's "countable sets (F2.3)" by §02 as a whole; the diagonal via decimals and 0.4999… = 0.5 by `def-decimal-expansion`, (D1)–(D3) and `thm-reals-uncountable-decimal`. Still open, a seam item from the blueprint: `07-nested-intervals.md` ("every real number has one") should say "every number in [0, 1) has one" to match (D1), which needs the author's consent, since AN1.1 has passed S8) |
| AN1.1 §01, §03, §04, §05 | @eq-abs-interval is the move of limits; sup approximation becomes a limit; "complete" acquires a second meaning | AN1.2 |
| AN1.1 §06, §07 (C4 solution), index | Heine–Borel and the IVT proved by "construct a point as a sup" | AN1.4, AN1.6 |
| AN1.1 §06 | aˣ for irrational x | AN1.10 |
| AN1.1 index, §03, §05, §07 | equivalent forms of completeness | AN1.11 |
| AN1.1 index, §03 | constructing ℝ (from Cauchy sequences, main line of fd3; by Dedekind cuts, optional); uniqueness — prose only, nothing in AN1 depends on them | F3.10, F3.3, F3.4 (prose pointers with fd3 chapter numbers; fd3 does not cite an1 and an1 does not cite these) |

## Seam items for the split (approved chapters)

The split of 2026-10-12 left pointers in AN1.1 that it had made wrong: the construction of ℝ is now main line in fd3 (from Cauchy sequences, F3.10, fd3 Chapter 5; uniqueness F3.4, fd3 Chapter 6), and only Dedekind cuts (F3.3, fd3 Chapter 7) is optional; and the old book's Parts are now volumes. **Fixed in the seam pass of 2026-10-12** (commit "Seam pass after the split: pointers that the split made wrong"). Ledger items whose hash changed went back to the coordinator for re-refereeing. The rows for fd1 and fd2 are in foundations' STATUS.md.

| File:line | Was | Now |
|---|---|---|
| `an1/src/ch01-least-upper-bound/03-the-axiom.md:38` | "the optional *Number Systems*, Chapter 7 does this [Dedekind cuts]. The optional … Chapter 6 shows …; nothing else in the book uses those chapters" | "*Number Systems*, Chapters 5 and 6 take this route with Cauchy sequences of rationals, and show …; the optional *Number Systems*, Chapter 7 builds ℝ by Dedekind cuts instead. This volume does not use those chapters" |
| `an1/src/ch01-least-upper-bound/index.md:5` | "The optional *Number Systems*, Chapter 7 builds it from ℚ …, and Chapter 11 shows" | "*Number Systems*, Chapter 5 builds it from ℚ by Cauchy sequences …, as the optional *Number Systems*, Chapter 7 does by Dedekind cuts; Chapter 11 of this volume shows" |
| `an1/src/ch01-least-upper-bound/03-the-axiom.md:26` | "the logic and set theory of Part 0" | "the logic and set theory of *Logic and Proof* and *Sets, Relations, and Cardinality*" |
| `an1/src/ch01-least-upper-bound/03-the-axiom.md:134` | "The book uses them from Part IV on" | "The series uses them from *Measure and Integration* on" |
| `an1/src/ch01-least-upper-bound/01-ordered-fields.md:274` | "every estimate in Part I" | "every estimate in this volume" |
| `an1/src/ch01-least-upper-bound/06-density-and-roots.md:280` | "In Part II the word **dense**" | "In *Metric and Topological Spaces* the word **dense**" |
| `an1/src/index.md` | the preface of the old 78-chapter book (Parts 0–VI, two routes) | the preface of *Analysis on the Real Line*: readers (fd1, fd2 and Gate 0; fd3's construction of ℝ not needed), the chapters AN1.1–AN1.11 (only AN1.1 written), how to read it |

## Blueprint deviations

- Ch 11 (recorded at S7 from S5 Referee B, R6; for S2a to confirm): `lem-field-algebra`, `prp-absolute-value-rules` and `lem-integer-part` are not in the frozen blueprint's label list (they carry facts the blueprint's results need; `lem-field-algebra` now cites `@la:thm-field-basic-properties` for the parts the companion has and proves only −(−a) = a, (c) and (e)). The blueprint's §07 task "the reals not in a given countable set are dense" is now §07 C2 (c). The blueprint names no key proofs (STYLE §11.2).
- Ch 11 (for NOTATION, from S5 Referee B, R5 (b); not changed at S7): rows are wanted for ℝ(x) (the rational functions, §05), \( \sqrt[n]{a} \) / \( a^{1/n} \) (§06), \( U(A) \) (the set of upper bounds, §02 C2, §03 C2) and \( \operatorname{lc} \) (leading coefficient; defined where used in §05 C2 and §07 C3). **Done at S8** (NOTATION rows added, with `\deg`).
- Ch 11 S8 (`an1/authoring/reviews/ch01-S8-seam.md`), src fixes for S7: `lem-field-algebra` cites LA 0.7.1 for the uniqueness of 1 and a⁻¹, which LA leaves to `@la:exr-fields-b1` (gap, row 3); `thm-nth-root` covers only a > 0, while the Ch 1 promise is for non-negative a (add ⁿ√0 = 0, row 4); 06:105 gives powers with u¹ as the base, where Ch 7's `def-power` has u⁰ ≔ 1 (row 5). *(All three found applied at the cross-chapter cleanup: 01:78, 06:76, 06:105.)*
- Ch 11 → Ch 7 blueprint (from S5 Referee B, R2): the Ch 7 blueprint opens a promise to Ch 11, that `@def-supremum` gains a clause pointing back to `def-order-supremum`; schedule it when Ch 7 is drafted. *(Ch 7 drafted 2026-10-11: `def-order-supremum` is in §06, and 06:219 points to Chapter 11's supremum; the back-pointer in `@def-supremum` is still open, recorded in the Ch 7 → Ch 11 promise row, and needs the author's consent.)*

## Engine and convention notes from the pilot

- Fitch derivations use fitch.sty (`latex/fitch-book.sty`, `nd` environment in a raw LaTeX block); the website gets build-time SVGs through filters/tikz.lua. Converted from the pilots' arrays on 2026-09-28.
- Line ranges in justifications: `\lines{2}{5}` (no non-ASCII in math, test_display_math_source).
- A paragraph opening "(a) …" becomes a Pandoc list: one lettered item per paragraph, or italic `*(a) ⇒ (b).*`.
- `enumerate` does not take a constant label such as `label=(L)`.
- `blueprint/originality.py` ignores n-grams made only of stock vocabulary (STOCK); both pilots report 0 at n = 8.

## Open engineering items

- `tools/seed_errors.py` does not skip `% schema` blocks yet.
- `tools/check_numbers.py` is advisory (`NUMBERS_FATAL = False`) until Chapter 1's three unprinted QUOTED values (the three-valued 1/2 in prp-peirce and exr-finding-derivations-b1) are resolved in S7. *(Ch 2 S8, 2026-09-28: those items now live in Chapter 2 and no longer quote 1/2; `check_numbers.py --advisory` reports 0 fatal over 194 sidecars, the 3 advisories being Chapter 1 sidecars with no QUOTED dict. The flag can be made fatal once the coordinator agrees.)*
- Ch 1 §05 PDF: 102 `Overfull \vbox` warnings from mdframed ("Box was splittet wrong") around the 14-line derivation of the C1 (b) solution; the page renders correctly (Ch 1 S8 seam, row 23). Let mdframed split it cleanly or keep the derivation off a page break.
- The PDF running head overflows for long section titles (e.g. Chapter 1 §01); needs a short-title mechanism in the engine.
- fitch.sty resolves line references in one pass, so a (deliberately illegal) citation of a LATER line prints "??". Workaround in Ch 1 §02: write the justification as literal text, `\by{Tr\ 5, 3}{}`, which check_fitch cannot see. Fix: teach check_fitch to read such literal citations (or add a `\byfwd` macro that prints the numbers verbatim) so illegal-example blocks can carry `% expect-invalid` again.
