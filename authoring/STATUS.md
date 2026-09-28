# Status

The state of every chapter, the approved exemplar, and the forward promises still to be paid.
Update it when a chapter changes state; drafting agents report, the author edits.

## Exemplar

None approved yet. The pilot chapters are Chapter 1 (Part 0, logic) and Chapter 8 (Part I, the
least upper bound axiom). When the author approves one, name it here: every later chapter
imitates its register, density and exercise design.

## Chapters

| Ch | Slug | State |
|---|---|---|
| 1 | logic-connectives | pilot: drafted 2026-09-27 (7 sections, ~26.6k words); awaiting author review |
| 8 | least-upper-bound | pilot: drafted 2026-09-27 (7 sections, ~24.2k words); awaiting author review |
| all others | see `blueprint/book.yaml` | not started |

## Forward promises

Prose pointers that must become `@ref`s (or be paid off) when the target chapter is written.

| From | Promise | Target |
|---|---|---|
| Ch 1 §01, §03, §04 | quantifier rules: ∀I ("r was arbitrary"), naming a witness k | Ch 2 |
| Ch 1 §02 warning | using an assumption outside its box, catalogued among what is not allowed | Ch 2 |
| Ch 1 §05 | ¬¬P ⊢ P and P ∨ ¬P are not derivable without RAA; ⊢ ¬¬(P ∨ ¬P) without RAA; the people who refused the rule | Ch 2, final section |
| Ch 1 §06 | full proof of soundness (by induction on the number of lines) | Ch 4 |
| Ch 1 §03 | the lowest-terms fact (L) rests on induction / well-ordering | Ch 4 |
| Ch 1 §05 C1 | every integer ≥ 2 has a prime divisor | Ch 4 |
| Ch 1 §03, §04 | facts about ≤, absolute value, existence of square roots | Ch 8 (paid) |
| Ch 1 §04 warning | differentiable ⇒ continuous | Ch 14 |
| Ch 8 §02, §05 | the quantifier law "not all" ⇒ "some not" (uses RAA); quantifier negation | Ch 2 |
| Ch 8 index | sets, images, −A, A + B as images | Ch 3 |
| Ch 8 §01 C1, §02, §05, §06 | induction; every non-empty finite set has a maximum; ℕ closed under + and ·; nothing between n and n + 1; well-ordering (used in lem-integer-part); definition by recursion | Ch 4 |
| Ch 8 index, §07 | countable = listable with repetitions (image of ℕ); ℕ, ℤ, ℚ countable; diagonal proof via decimals, 0.4999… = 0.5 flagged | Ch 5 (match the definition there) |
| Ch 8 §01, §04 | @eq-abs-interval is the move of limits; sup approximation becomes a limit | Ch 9 |
| Ch 8 index | Heine–Borel and the IVT proved by "construct a point as a sup" | Ch 11, Ch 13 |
| Ch 8 §07 | aˣ for irrational x | Ch 17 |
| Ch 8 index, §03, §07 | equivalent forms of completeness | Ch 18 |
| Ch 8 §03 | constructing ℝ; uniqueness (prose only, optional) | Ch 19, Ch 20 |

## Engine and convention notes from the pilot

- Fitch derivations use fitch.sty (`latex/fitch-book.sty`, `nd` environment in a raw LaTeX block); the website gets build-time SVGs through filters/tikz.lua. Converted from the pilots' arrays on 2026-09-28.
- Line ranges in justifications: `\lines{2}{5}` (no non-ASCII in math, test_display_math_source).
- A paragraph opening "(a) …" becomes a Pandoc list: one lettered item per paragraph, or italic `*(a) ⇒ (b).*`.
- `enumerate` does not take a constant label such as `label=(L)`.
- `blueprint/originality.py` ignores n-grams made only of stock vocabulary (STOCK); both pilots report 0 at n = 8.
