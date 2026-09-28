<!-- hand-written -->
# Part 0 logic block: overview of Chapters 1–4

One page for the coordinator and the drafters: how the four logic chapters divide the material, what the pilot Chapter 1 becomes, and how Chapter 4 hands over to the rest of the book. The chapter blueprints (`ch01.md` … `ch04.md`) are binding; this file only maps them.

## The division

| Ch | Slug | Question it answers | Level reference (depth only) | Main results |
|---|---|---|---|---|
| 1 | `propositional-natural-deduction` | What are the rules for the connectives, and how do I find a derivation? | Huth & Ryan §1.1–1.2 | the primitive rules; `def-derivation`, `def-derivable`; the derived rules (MT, contrapositive, \( \neg\neg \)I/E, DS, LEM, De Morgan); `thm-classical-rules-interderivable`; `thm-sqrt2-irrational`; the search method |
| 2 | `semantics-soundness-completeness` | Are the rules right — do they prove exactly the truth-table consequences? | §1.3–1.5 (no Horn, no SAT) | formulas, parse trees, unique readability; `ax-induction`, `thm-strong-induction`, `thm-structural-induction`; valuations, \( \models \); `thm-soundness` and `thm-completeness`, both proved in full; CNF/DNF; adequate connectives |
| 3 | `predicate-logic` | What are the rules for "for every", "there exists" and "=", and what do their side conditions protect? | §2.1–2.4 | terms, free variables, substitution; \( \forall \)/\( \exists \)/= rules; quantifier negation and passage laws; uniformly continuous \( \Rightarrow \) continuous as a derivation; models, counter-models, `thm-first-order-soundness` |
| 4 | `from-derivations-to-prose` | How do derivations become the prose mathematicians write, and how do I read, write and check that prose? | — | the rhetoric dictionary; four levels of abbreviation; the self-explanation training passage; `exm-not-allowed-catalogue` (N1)–(N11); the excluded-middle dispute |

Then Part 0 continues: 5 sets and functions, 6 relations and induction, 7 cardinality (Gate 0); Part I starts at Chapter 10.

## The rule system (one decision for all four chapters)

- Primitive: \( \wedge \)I/E, \( \to \)I/E, \( \vee \)I/E, \( \neg \)I, \( \neg \)E, \( \bot \)E, **RAA**, \( \leftrightarrow \)I/E, R; Chapter 3 adds \( \forall \)I/E, \( \exists \)I/E, =I/E.
- RAA is the only classical rule. "PBC" is not a separate rule (it is RAA under another name). \( \neg\neg \)E, LEM, MT, contrapositive, DS, De Morgan are **derived**, each proved once and then used as one line.
- \( \bot \)E is kept primitive although RAA derives it, so that "all primitive rules but RAA" is the intuitionistic system of Chapter 4 §07.
- Every rule name has a `fitch-book.sty` macro; the additions needed are listed at the end of `ch01.md`.

## Where the pilot's Chapter 1 goes

| Pilot section (`src/ch01-logic-connectives/`) | New home |
|---|---|
| 01 statements-and-proofs | Ch 1 §01 (almost whole) |
| 02 conjunction-and-implication | Ch 1 §02 (whole) |
| 03 disjunction-negation-contradiction | Ch 1 §03 (∨, cases, absolute-value examples) and §04 (¬, ⊥, contrapositive, √2, vacuous truth) |
| 04 biconditional-and-definitions | Ch 1 §05 (whole) |
| 05 reductio | Ch 1 §06; the "costume" examples and exercises → Ch 4 §01 |
| 06 truth-tables | Ch 2 §03–§05 (made exact; soundness now proved) and §07 (two connectives are enough) |
| 07 proof-skeletons | skeletons and the rule table → Ch 1 §07; annotating and writing → Ch 4 §05; Proofs A–D and "four proofs to check" → Ch 4 §06 |

All labels that Chapter 10 cites keep their names and stay in Chapter 1: `thm-sqrt2-irrational`, `thm-square-even-implies-even`, `prp-contrapositive`, `def-rule-raa`, `def-rules-negation`, `def-rules-conjunction`, `def-rules-implication`, `def-rules-disjunction`, `def-rules-biconditional`, `def-derivation`, `def-derivable`, `def-statement`, `prp-vacuous-implication`, `prp-ex-falso`, `prp-disjunctive-syllogism`, `prp-double-negation`, `prp-de-morgan`, `prp-excluded-middle`. Pilot labels that move chapters keep their names too (list in each blueprint).

## Induction arrives early

Chapter 2 needs induction for soundness and completeness. It states `ax-induction` (a basic property of ℕ, taken as given), proves `thm-strong-induction` and `thm-structural-induction`. **Chapter 6's blueprint must be adjusted**: it cites these and does not re-derive them; it keeps well-ordering (and its equivalence with induction), recursion on ℕ, and the induction pitfalls.

## How Chapter 4 hands over to the rest of the book

- **Level 3 prose from Chapter 5 on.** Chapter 4 §03 defines the four levels and `def-silent-steps` (which rules may go unstated). Chapters 5–7 may still use level-2 rule tags (`[\( \rulename{\forall I} \)]`, STYLE §10: Part 0 only); from Chapter 10 on, proofs are level 3 with no tags.
- **The dependency parenthesis.** "Choose \( N \) (depending on \( \varepsilon \))" is explained in Chapter 3 §07 and Chapter 4 §02 as the record of open \( \forall \)I boxes; STYLE §4's rule "say what each constant depends on" now has its logical justification, and later chapters may point to Chapter 4 §02.
- **The catalogue.** Warnings in every later Part cite `@exm-not-allowed-catalogue` with the entry number (N1)–(N11) when the error is one of them (STYLE §10).
- **Self-explanation.** The one training passage is Chapter 4 §04; every later *Before reading on* prompt assumes it (STYLE §11.1, which currently says "Chapter 2" and must be updated).
- **Checking.** The two-column check of Chapter 4 §06 is the method behind every later find-the-error item; after Part 0 the solution names the missing hypothesis or illegal step instead of the rule (STYLE §10).
- **Non-constructive steps.** Chapter 4 §07 is where later chapters point when they flag a use of LEM (Bolzano–Weierstrass bisection, the sup of a non-located set) or of choice (Chapter 7's `ax-choice`).
- **Lean.** The Lean column of the dictionary (Chapter 4 §01–§02) is the last place Lean appears systematically.

## Renumbering the Chapter 10 pilot's prose pointers

The pilot Part I chapter (was ch08, now ch10) points to Part 0 by number. When it is renamed: "Chapter 2" (quantifier negation, derived with RAA) → **Chapter 3** (`prp-quantifier-negation`, now `@ref`-able); "Chapter 1 explains why a statement with no instances counts as true" → **Chapter 3** §03; "Chapter 4" (induction, well-ordering, facts about ℕ and ℤ, recursion) → **Chapter 2** for induction itself (`ax-induction`, `thm-strong-induction`) and **Chapter 6** for well-ordering and recursion; "Chapter 5" (countable sets) → **Chapter 7**; "Chapter 1 proved (a) by splitting into cases" stays true (Chapter 1 §03). The STATUS promise rows "full proof of soundness → Ch 4" and "¬¬P ⊢ P, P ∨ ¬P not derivable without RAA; the people who refused the rule → Ch 2" are paid by Chapter 2 §05 and Chapter 4 §07.
