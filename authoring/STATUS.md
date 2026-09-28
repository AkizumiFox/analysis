# Status

The state of every chapter, the approved exemplar, and the forward promises still to be paid.
Update it when a chapter changes state; drafting agents report, the author edits.

## Exemplar

None approved yet. The pilot chapters are Chapter 1 (Part 0, logic) and Chapter 10 (Part I, the
least upper bound axiom). When the author approves one, name it here: every later chapter
imitates its register, density and exercise design.

Renumbering of 2026-09-28: Part 0's logic went from two chapters to four (modelled on Huth & Ryan
ch. 1–2), so the book has 77 chapters and every chapter from the old Chapter 3 on moved up by two
(old 8 → 10, …, old 75 → 77). The Chapter 1 pilot (`src/ch01-logic-connectives/`) is kept until it
is rewritten as `propositional-natural-deduction`; its prose still carries the old chapter numbers
(Chapter 2, 4, 8, 14), recorded below beside the new targets.

## Chapters

| Ch | Slug | State |
|---|---|---|
| 1 | propositional-natural-deduction | pilot drafted as `logic-connectives` 2026-09-27 (7 sections, ~26.6k words); referee findings (research-production §3.1) fixed 2026-09-28 (roadmap C1); to be rewritten to the new four-chapter logic plan (blueprint being re-authored); labels `thm-sqrt2-irrational`, `def-rule-raa`, `prp-contrapositive` stay in Chapter 1 |
| 2–4 | semantics-soundness-completeness, predicate-logic, from-derivations-to-prose | blueprints being authored |
| 10 | least-upper-bound | pilot: drafted 2026-09-27 as Chapter 8 (7 sections, ~24.2k words); referee findings (research-production §3.1) fixed 2026-09-28 (roadmap C1); renumbered to 10 on 2026-09-28; awaiting author review |
| all others | see `blueprint/book.yaml` | not started |

## Forward promises

Prose pointers that must become `@ref`s (or be paid off) when the target chapter is written.
Chapter 1 rows use the rewritten chapter's section numbers (2026-09-28, S7); its prose uses the new chapter numbers.

| From | Promise | Target |
|---|---|---|
| Ch 1 §01, §02, §03, §04, §05, §06, §07, index | soundness: truth tables for the connectives, the rules never lead from true premises to a false conclusion, a refuting row rules out every derivation (`thm-soundness`, `cor-refuting-row`); the length and context of a derivation (§02) | Ch 2 |
| Ch 1 §01 | unique readability: a statement built from letters by connectives is read in only one way | Ch 2 |
| Ch 1 §02 | substitution: a derivation stays a derivation under each way of putting statements in for the letters | Ch 2 |
| Ch 1 §05, §06 | ¬¬P ⊢ P is not derivable without RAA, by reading statements with more than two truth values (`thm-raa-independent`, optional there) | Ch 2 |
| Ch 1 §01, §04, §05, §06, §07, index | quantifier rules: "for every" (∀I, "r was arbitrary"; applying a hypothesis "for every ε"), "there exists" (naming a witness k) | Ch 3 |
| Ch 1 §01, §02, index | checking a proof line by line: the rules run silently under written proofs; the rule/phrase table extended to every rule | Ch 4 |
| Ch 1 §03, §06 | the full rule, phrase and Lean dictionary | Ch 4 |
| Ch 1 §04, §06 | the reading ¬P as P → ⊥, and the system of the rules other than RAA (intuitionistic logic); the history of those who declined RAA | Ch 4, final section |
| Ch 1 §06 | spotting a "proof by contradiction" that is a direct proof in disguise | Ch 4 |
| Ch 1 §04 | the lowest-terms fact (L) rests on well-ordering | Ch 6 |
| Ch 1 §03, §04, §05, §06, index | facts about ≤ and absolute value from the ordered-field axioms; existence of square roots of non-negative reals; `thm-sqrt2-irrational` used as is | Ch 10 (paid) |
| Ch 1 §05 | differentiable ⇒ continuous | Ch 16 |
| Ch 10 §02, §05 | the quantifier law "not all" ⇒ "some not" (uses RAA); quantifier negation | Ch 3 |
| Ch 10 index | sets, images, −A, A + B as images | Ch 5 |
| Ch 10 §01 C1, §02, §04, §05, §06 | induction (used for n > 0 in exm-sup-one-minus-reciprocal and cor-sup-approximation, and in §06); every non-empty finite set has a maximum; ℕ closed under + and ·; n ≥ 2 ⇒ n − 1 ∈ ℕ; nothing between n and n + 1; well-ordering (used in lem-integer-part); definition by recursion (powers uⁿ in thm-nth-root) | Ch 6 |
| Ch 10 §05 remark, §06 lem-integer-part | ℤ closed under +, − and · (used for m = j₀ − p − 1 and for m′ − m in lem-integer-part; "positive integer ⇒ natural number" is proved in the §05 remark) | Ch 6 |
| Ch 10 index, §07 | countable = listable with repetitions (image of ℕ); ℕ, ℤ, ℚ countable; diagonal proof via decimals, 0.4999… = 0.5 flagged | Ch 7 (match the definition there) |
| Ch 10 §01, §03, §04, §05 | @eq-abs-interval is the move of limits; sup approximation becomes a limit; "complete" acquires a second meaning | Ch 11 |
| Ch 10 §06 | Heine–Borel and the IVT proved by "construct a point as a sup" | Ch 13, Ch 15 |
| Ch 10 §06 | aˣ for irrational x | Ch 19 |
| Ch 10 index, §03, §05, §07 | equivalent forms of completeness | Ch 20 |
| Ch 10 index, §03 | constructing ℝ; uniqueness (prose only, optional) | Ch 21, Ch 22 |

## Blueprint deviations

- Ch 1 (recorded at S7 from S5 Referee B, R4; for S2a to confirm): six labels not in the frozen blueprint's label list carry content the blueprint asks for: `exm-disjunction-first-derivations`, `exm-disjunction-regroup`, `exm-cases-on-hypothesis` (§03); `exm-double-negation-introduction`, `exm-modus-tollens-instance` (§04); `prp-provable-equivalence-basics` (§05).

## Engine and convention notes from the pilot

- Fitch derivations use fitch.sty (`latex/fitch-book.sty`, `nd` environment in a raw LaTeX block); the website gets build-time SVGs through filters/tikz.lua. Converted from the pilots' arrays on 2026-09-28.
- Line ranges in justifications: `\lines{2}{5}` (no non-ASCII in math, test_display_math_source).
- A paragraph opening "(a) …" becomes a Pandoc list: one lettered item per paragraph, or italic `*(a) ⇒ (b).*`.
- `enumerate` does not take a constant label such as `label=(L)`.
- `blueprint/originality.py` ignores n-grams made only of stock vocabulary (STOCK); both pilots report 0 at n = 8.

## Open engineering items

- `tools/check_fitch.py` rejects ∀I boxes (a box opened with a guard `\open[x_0]` and no assumption line). Fix before Chapter 3 is drafted; quantifier rules are currently only noted, not checked.
- `tools/seed_errors.py` does not skip `% schema` blocks yet.
- `tools/check_numbers.py` is advisory (`NUMBERS_FATAL = False`) until Chapter 1's three unprinted QUOTED values (the three-valued 1/2 in prp-peirce and exr-finding-derivations-b1) are resolved in S7.
- The PDF running head overflows for long section titles (e.g. Chapter 1 §01); needs a short-title mechanism in the engine.
