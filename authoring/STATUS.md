# Status

The state of every chapter, the approved exemplar, and the forward promises still to be paid.
Update it when a chapter changes state; drafting agents report, the author edits.

## Exemplar

None approved yet. The pilot chapters are Chapter 1 (Part 0, logic) and Chapter 11 (Part I, the
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

| Ch | Slug | State |
|---|---|---|
| 1 | connectives-and-derivations | the first half of the pilot `propositional-natural-deduction` (split 2026-09-28); hand-written blueprint `authoring/blueprints/ch01.md` (S2 v3: `authoring/reviews/ch01v3-S2.md`); drafted as `src/ch01-connectives-and-derivations/` (7 sections, 119 derivations checked by check_fitch); **passed S2–S8 2026-09-28** (`authoring/reviews/ch01-*.md`, seam `ch01-S8-seam.md`); Chapter 3 pointers now `@ref`s (cross-chapter cleanup); **awaiting author review (S9)** — candidate exemplar for Part 0 |
| 2 | negation-and-classical-logic | the second half of the pilot, split 2026-09-28; hand-written blueprint `authoring/blueprints/ch02.md` (S2 v3: `authoring/reviews/ch02v3-S2.md`); drafted as `src/ch02-negation-and-classical-logic/`; **passed S2–S8 2026-09-28** (`authoring/reviews/ch02-*.md`, seam `ch02-S8-seam.md`; 120 ledger items, 0 stale); Chapter 3 pointers now `@ref`s (cross-chapter cleanup); **awaiting author review (S9)** |
| 11 | least-upper-bound | pilot drafted 2026-09-27; renumbered and retrofitted to STYLE §11 2026-09-28; **passed S2–S8 2026-09-28** (S5–S7 re-run after the retrofit; seam `authoring/reviews/ch11-S8-seam.md`: src rows 3–5 applied, optional rows 2 and 6 not); induction now cites `@ax-induction` (cross-chapter cleanup); **awaiting author review (S9)** — candidate exemplar for Parts I–VI |
| 3 | semantics-soundness-completeness | hand-written blueprint `authoring/blueprints/ch03.md` (S2 + recheck passed 2026-09-28); drafted as `src/ch03-semantics-soundness-completeness/` (7 sections, 31 derivations and 20 truth tables checked by check_fitch, 60 sidecars); **passed S2–S8 2026-09-28** (`authoring/reviews/ch03-*.md`, two S7r rounds, seam `ch03-S8-seam.md`); **awaiting author review (S9)** |
| 4, 5 | logic block | hand-written blueprints, S2 passed 2026-09-28; not drafted |
| 6, 7, 8 | sets, relations and induction, cardinality (Gate 0) | hand-written blueprints 2026-09-28; S2 pending |
| all others | see `blueprint/book.yaml` | generated blueprints; not started |

## Forward promises

Prose pointers that must become `@ref`s (or be paid off) when the target chapter is written.
Chapter 1 rows use the sections of `connectives-and-derivations` (reconciled at its S7, 2026-09-28); rows for material that moved to Chapter 2 at the split are filed under Ch 2 with its sections.

| From | Promise | Target |
|---|---|---|
| Ch 1 §01, §02, §03, §04, §05, §06, §07, index | soundness: truth tables for the connectives, the rules never lead from true premises to a false conclusion, a refuting row rules out every derivation (`thm-soundness`, `cor-refuting-row`); the length and context of a derivation (§05); completeness (§03); induction on the lines of a derivation (§02 B3's lower bound m − 1, §03 C1's first bad line) | Ch 3 (paid: `thm-soundness`, `cor-refuting-row`, `cor-derivable-iff-valid`, `thm-completeness`, `thm-strong-induction`, `ax-induction`; the pointers are `@ref`s since the cross-chapter cleanup) |
| Ch 1 §01 | unique readability: a statement built from letters by connectives is read in only one way | Ch 3 (paid: `def-formula`, `thm-unique-readability`, cited) |
| Ch 1 §02 | substitution: a derivation stays a derivation under each way of putting statements in for the letters | Ch 3 (paid by §01 "Letters, metavariables and substitution", which has no label, so 02:210 stays a prose pointer) |
| Ch 2 §01, §02, §03, §04, §06, index | soundness (`thm-soundness`, `cor-refuting-row`): ⊥E and the box rules never lead from true premises to a false conclusion (§01, the "line of the box itself" clause of ¬I, §02); the rows of → with a false hypothesis (§01); a refuting row rules out every derivation (§04 warning, §06 "cannot be filled", the failed search, C2, R3; index); substitution into a derived rule made exact (§03) | Ch 3 (paid; `@ref`s since the cross-chapter cleanup, except 03:120, whose substitution passage has no label, and the Idea blocks of §05 (05:232, 05:333), where a forward `@ref` would be a proof step) |
| Ch 2 §04, §05 | ¬¬P ⊢ P is not derivable without RAA, by reading statements with more than two truth values (`thm-raa-independent`, optional there); Peirce's law likewise (§05, after `prp-peirce`; paid by the remark after `thm-raa-independent`, value ½ at p = ½, q = 0; pointer added at Ch 2 S8) | Ch 3 (paid: `@thm-raa-independent` and the remark after it, cited in prose at 04:227, 05:37, 05:309) |
| Ch 1 §01, §02, §04, §05, §06, §07, index | quantifier rules: "for every" (∀I, "r was arbitrary"; applying a hypothesis "for every ε"), "there exists" (naming a witness k); a rule with no given lines (=I, §02); the quantifier and equality rows of the rule / phrase / Lean table (§06) | Ch 4 |
| Ch 1 §01, §02, index | checking a proof line by line: the rules run silently under written proofs; the rule/phrase table extended to every rule | Ch 5 |
| Ch 1 §03, §04, §05, §06 | the full rule, phrase and Lean dictionary | Ch 5 |
| Ch 2 §02, §05 | the reading ¬P as P → ⊥, and the system of the rules other than RAA (intuitionistic logic); the history of those who declined RAA | Ch 5, final section |
| Ch 2 §05 | spotting a "proof by contradiction" that is a direct proof in disguise | Ch 5 |
| Ch 2 §01, §02, §04, §05, §06 | quantifier steps: "for every" (a hypothesis applied to ε = x/2, §05; "for all x and y", §04; r arbitrary, §02), "there exists" (naming a witness k, §01, §02, §06); statements about every element of the empty set (§01) | Ch 4 |
| Ch 2 §02 | the lowest-terms fact (L) rests on well-ordering | Ch 7 |
| Ch 1 §01, §07 | every integer is even or odd, and not both (Argument A of §01; §07 A1, B3); an integer 4k + 1 or 4k + 3 is odd (§07) | Ch 7 |
| Ch 1 §02, §03, §04, §05, §06, §07, index | facts about <, ≤ and absolute value from the ordered-field axioms; existence of square roots of non-negative reals; `thm-sqrt2-irrational` (now Ch 2) used as is | Ch 11 (paid) |
| Ch 2 §02, §04, §05 | `thm-sqrt2-irrational` used as a statement about ℚ (§02); existence of square roots of non-negative reals (§04); the school algebra of < from the axioms (§05); the proof that ℕ is not bounded above is ¬I (§05; the proof of `thm-naturals-unbounded` opens "Suppose, for contradiction") | Ch 11 (paid) |
| Ch 2 §04 | differentiable ⇒ continuous | Ch 17 |
| Ch 1 §04 | the extreme value theorem (its hypotheses named in the warning on using the whole hypothesis; not used in any argument) | Ch 16 |
| Ch 1 §01, §03, §04, §05, §06, §07, index | the rules for ¬, ⊥, ↔ and RAA; `thm-square-even-implies-even` (the §01 hook); `prp-vacuous-implication` (Section 2.1); derived rules, `def-derived-rule` (Section 2.3), and the green card of `exm-wason-selection`; "if" in definitions and `def-provable-equivalence` (Section 2.4); the method of finding derivations (Section 2.6) | Ch 2 |
| Ch 3 §02, §03, §05 | quantifier rules: ∀, ∃ as abbreviations of words in the statement of `ax-induction` (§02); the step from "let n be arbitrary" to "for every n" (§02); looking inside atoms (§03 warning); Ch 4's soundness extension cites `lem-context-inclusion` (b) (§05) | Ch 4 |
| Ch 3 §05 | what RAA says, and who objected to it (remark after `thm-raa-independent`) | Ch 5 |
| Ch 3 §01, §02 | sets and functions in the everyday sense made precise: the formulas as the smallest set closed under the building steps (§01); sets of formulas and numbers, "function" (§02) | Ch 6 |
| Ch 3 §02 | induction is equivalent to well-ordering; a famous false "proof" that fails at the step 1 → 2, like §02's warning on 2n² ≥ (n + 1)² (`exm-all-equal-induction`) | Ch 7 |
| Ch 3 §02 | the induction axiom derived from the axioms of set theory (optional chapter) | Ch 9 |
| Ch 3 §01, §02 | the axiomatic method: say exactly which objects we reason about (§01); `ax-induction` given and not proved, as `ax-least-upper-bound` is (§02) | Ch 11 (paid) |
| Ch 11 §02, §05 | the quantifier law "not all" ⇒ "some not" (uses RAA); quantifier negation | Ch 4 |
| Ch 11 §01 C1, §02, §04, §05, §06, §07, index | induction on ℕ (`ax-induction`): n > 0 in exm-sup-one-minus-reciprocal and cor-sup-approximation; the copy of ℕ in an ordered field, and (m + n)·1 = m·1 + n·1 (§01 C1); "ℕ is the smallest inductive set" (§05 remark); x₀ⁿ ≤ x₀ and the claim of thm-nth-root, 2ᵏ > k (§06); I_k ⊆ I_m, 2ⁿ⁻¹ ≥ n, and the one induction of C1 (b) (§07) | Ch 3 (paid: `@ax-induction`, cited at index, 01 C1 hint, 02:169, 05:43, 05:58, 06 C2, 07:52; the ledgers name it) |
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

- *(Resolved by the split; Ch 1 S8, 2026-09-28: the three §03 labels are in `ch01.md`'s kept-label list (all three now in §07), and the other three belong to `ch02.md`.)* Ch 1 (recorded at S7 from S5 Referee B, R4; for S2a to confirm): six labels not in the frozen blueprint's label list carry content the blueprint asks for: `exm-disjunction-first-derivations`, `exm-disjunction-regroup`, `exm-cases-on-hypothesis` (§03); `exm-double-negation-introduction`, `exm-modus-tollens-instance` (§04); `prp-provable-equivalence-basics` (§05).

- Ch 2 (recorded at S7 from S5 Referee B, row 4; for S2a to confirm): `exm-search-raa` (§06, "When nothing else works") is not in the frozen blueprint, whose §06 lists three worked searches, the failed one and a Peirce paragraph with no new derivation; step 5's clause "try the same with a goal further out" is also new (it matches `prp-peirce`'s Idea and the Peirce paragraph after `exm-search-raa`). Also for the coordinator: `ch07.md` l.54 pays a STATUS row "every integer ≥ 2 has a prime divisor" placed in "Chapter 2 §04 C1", but that item (divisibility by six) uses no prime divisor and no such row remains in the promise table; drop the payment line. *(Ch 2 S8, 2026-09-28: content checked. `exm-search-raa` and the step-5 clause are correct and consistent with `prp-peirce`'s Idea, the Peirce paragraph and the failed search (`ch02-S8-seam.md` row 6). Only the blueprint amendment is left for S2a or the author. ch07.md:54 still carries the prime-divisor row, row 19.)* *(Cross-chapter cleanup, 2026-09-28: the prime-divisor row is gone from ch07.md, replaced by the row paying "even or odd, not both; 4k + 1, 4k + 3 odd".)*

- Ch 3 (recorded at S7 from S5 Referee B, rows 5 and 6; for S2a to confirm): `lem-weakening-cut` has a part (c), "Chaining", not in the frozen blueprint, which the proofs of §06 use throughout; §03 has a B3 (the disjunctive-syllogism table) not in the blueprint; `thm-structural-recursion` is proved by ordinary induction on the length with "n-good" functions, not by strong induction on the number of symbols; all five candidate exit checks are kept (§02 C3, §05 C2, §06 C2, §07 C3, §07 C4), the §05 and §06 ones now marked "write from memory". All sound. The blueprint's claim that `lem-parenthesis-count` (b) is needed by unique readability (l.87) is false; the text now says (b) serves §02 C1. Also for the coordinator: §02 B1 (`exr-induction-b1`) proves 2ⁿ ≥ n + 1 in full, as the ch03 blueprint asks; `ch05.md` (l.86, 107) plans `exm-rhetoric-induction` on the same inequality and `ch07.md` (l.23) calls it Chapter 5's. Ch 5 should cite `@exr-induction-b1` as its source (annotating it, not re-proving it) or pick another inequality, and ch07's note should name Chapter 3. *(Done at the cross-chapter cleanup: ch05.md's example is now \( 0 < a^n \le a \) for \( 0 < a \le 1 \), and ch07.md:23 names Chapter 3's `exr-induction-b1`.)*

- Ch 11 (recorded at S7 from S5 Referee B, R6; for S2a to confirm): `lem-field-algebra`, `prp-absolute-value-rules` and `lem-integer-part` are not in the frozen blueprint's label list (they carry facts the blueprint's results need; `lem-field-algebra` now cites `@la:thm-field-basic-properties` for the parts the companion has and proves only −(−a) = a, (c) and (e)). The blueprint's §07 task "the reals not in a given countable set are dense" is now §07 C2 (c). The blueprint names no key proofs (STYLE §11.2).
- Ch 11 (for NOTATION, from S5 Referee B, R5 (b); not changed at S7): rows are wanted for ℝ(x) (the rational functions, §05), \( \sqrt[n]{a} \) / \( a^{1/n} \) (§06), \( U(A) \) (the set of upper bounds, §02 C2, §03 C2) and \( \operatorname{lc} \) (leading coefficient; defined where used in §05 C2 and §07 C3). **Done at S8** (NOTATION rows added, with `\deg`).
- Ch 11 S8 (`authoring/reviews/ch11-S8-seam.md`), src fixes for S7: `lem-field-algebra` cites LA 0.7.1 for the uniqueness of 1 and a⁻¹, which LA leaves to `@la:exr-fields-b1` (gap, row 3); `thm-nth-root` covers only a > 0, while the Ch 1 promise is for non-negative a (add ⁿ√0 = 0, row 4); 06:105 gives powers with u¹ as the base, where Ch 7's `def-power` has u⁰ ≔ 1 (row 5). *(All three found applied at the cross-chapter cleanup: 01:78, 06:76, 06:105.)*
- Ch 11 S8, blueprint fixes: ch03.md:195 must list the Ch 11 induction row as paid by `ax-induction`; ch04.md:90 and 197 should say `prp-vacuous-implication` is Chapter 2's; ch06.md:53 lacks the row "ℕ as ⋂ of all inductive subsets", and `def-family-union-intersection` must cover ⋂ of a set of sets; ch07.md:55 still quotes "induction (Chapter 7)" and lacks paying labels for 2m ≠ 1, (t²)² = t⁴ and (m+n)+1 = m+(n+1); part0-logic-overview.md:38 omits 5 cited labels (`exm-abs-product-cases`, `exm-triangle-inequality-cases` → Ch 1; `exm-square-plus-one`, `prp-equivalence-cycle`, `exr-negation-and-contradiction-c1` → Ch 2; keep the slug `negation-and-contradiction` or the C1 label). ch01.md and ch02.md are still identical copies of the old blueprint, so re-run S8 check (a) when the split is written. *(All found done at the cross-chapter cleanup: ch03.md:198, ch04.md (Chapter 2's `prp-vacuous-implication`), ch06.md:57, ch07.md:55–58, part0-logic-overview.md's keep-list and renumbering note; ch01.md and ch02.md are now the two split blueprints and were seam-checked at Ch 1/Ch 2 S8.)*
- Ch 11 → Ch 7 blueprint (from S5 Referee B, R2): the Ch 7 blueprint opens a promise to Ch 11, that `@def-supremum` gains a clause pointing back to `def-order-supremum`; schedule it when Ch 7 is drafted.

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
