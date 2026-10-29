# AN1 layout: Apostol's skeleton (2026-10-25)

Binding plan: math-atlas `spec/08-map-v2.md` §C (C0–C6). The author's corrections (2026-10-25):
"Apostol's skeleton, Cummings' motivation", and approval to run the workflow. This file records
the layout move of the `an1` and `an2` blueprints. AN2's order is in
`an2/authoring/design/layout-apostol.md`.

AN1 becomes *Real Numbers, Metric Spaces, and Derivatives*. It covers Apostol, *Mathematical
Analysis* (2e), Chapters 1–5. It has 10 chapters. The drafted AN1.1 stays Chapter 1, unchanged.

## Chapter order

| Pos. | Atlas id | Title (spec/08 C2) | Directory | Blueprint | Starts from (old blueprint) | Apostol |
|---|---|---|---|---|---|---|
| 1 | AN1.1 | Ordered Fields and the Least Upper Bound Axiom (drafted) | `an1/src/ch01-least-upper-bound/` | `an1/authoring/blueprints/ch01.md` | an1 ch01 (unchanged) | 1.1–1.20 |
| 2 | AN1.4 | Open, Closed, and Compact Subsets of ℝⁿ (renamed from "of ℝ") | `an1/src/ch02-open-closed-compact-subsets/` | `an1/authoring/blueprints/ch02.md` | an1 ch04 | 3.1–3.12 |
| 3 | AN2.1 | Metric Spaces and Their Topology (renamed; moved in) | `an1/src/ch03-metric-spaces/` | `an1/authoring/blueprints/ch03.md` | an2 ch01 | 3.13–3.16 |
| 4 | AN1.2 | Sequences, Subsequences, and Cauchy Sequences | `an1/src/ch04-sequences-and-cauchy-sequences/` | `an1/authoring/blueprints/ch04.md` | an1 ch02 | 4.1–4.4; 8.2–8.3 (monotone sequences, limsup) |
| 5 | AN2.2 | Completeness and the Completion of a Metric Space (+ Banach fixed point; moved in) | `an1/src/ch05-completeness-and-completion/` | `an1/authoring/blueprints/ch05.md` | an2 ch02 | 4.4, 4.48 |
| 6 | AN1.5 | Limits of Functions and Continuity (+ classification of discontinuities) | `an1/src/ch06-limits-and-continuity/` | `an1/authoring/blueprints/ch06.md` | an1 ch05 | 4.5–4.12, 4.22–4.23 |
| 7 | AN1.6 | Continuous Functions on Compact Sets and Intervals | `an1/src/ch07-continuity-on-compact-sets/` | `an1/authoring/blueprints/ch07.md` | an1 ch06 | 4.13–4.20 (on ℝ first) |
| 8 | AN2.3 | Compactness and Connectedness in Metric Spaces (moved in) | `an1/src/ch08-compactness-and-connectedness/` | `an1/authoring/blueprints/ch08.md` | an2 ch03 | 3.16, 4.13–4.21 |
| 9 | AN1.7 | The Derivative and the Mean Value Theorem (+ vector-valued and complex derivatives, Cauchy–Riemann) | `an1/src/ch09-derivative-and-mean-value/` | `an1/authoring/blueprints/ch09.md` | an1 ch07 | 5 (incl. 5.14–5.22) |
| 10 | AN1.11 | The Forms of Completeness (closing chapter) | `an1/src/ch10-forms-of-completeness/` | `an1/authoring/blueprints/ch10.md` | an1 ch11 | — |

Positions 2–10 are the nine chapters to blueprint. Each moved blueprint keeps its old body. Its
`Directory:` line now names the new directory and the old one, and says that the body still
follows the old layout. The body is replaced when the chapter is re-blueprinted against spec/08 C2
and C5.

Chapters that leave AN1 for AN2 (their blueprints moved to `an2/authoring/blueprints/`, bodies
unchanged): AN1.3 → AN2 ch04, AN1.8 → AN2 ch02, AN1.9 → AN2 ch06, AN1.10 → AN2 ch07.

## Blueprint file moves (git mv)

| Old path | New path |
|---|---|
| `an1/authoring/blueprints/ch01.md` | unchanged |
| `an1/authoring/blueprints/ch04.md` (AN1.4) | `an1/authoring/blueprints/ch02.md` |
| `an2/authoring/blueprints/ch01.md` (AN2.1) | `an1/authoring/blueprints/ch03.md` |
| `an1/authoring/blueprints/ch02.md` (AN1.2) | `an1/authoring/blueprints/ch04.md` |
| `an2/authoring/blueprints/ch02.md` (AN2.2) | `an1/authoring/blueprints/ch05.md` |
| `an1/authoring/blueprints/ch05.md` (AN1.5) | `an1/authoring/blueprints/ch06.md` |
| `an1/authoring/blueprints/ch06.md` (AN1.6) | `an1/authoring/blueprints/ch07.md` |
| `an2/authoring/blueprints/ch03.md` (AN2.3) | `an1/authoring/blueprints/ch08.md` |
| `an1/authoring/blueprints/ch07.md` (AN1.7) | `an1/authoring/blueprints/ch09.md` |
| `an1/authoring/blueprints/ch11.md` (AN1.11) | `an1/authoring/blueprints/ch10.md` |
| `an1/authoring/blueprints/ch08.md` (AN1.8) | `an2/authoring/blueprints/ch02.md` |
| `an1/authoring/blueprints/ch03.md` (AN1.3) | `an2/authoring/blueprints/ch04.md` |
| `an1/authoring/blueprints/ch09.md` (AN1.9) | `an2/authoring/blueprints/ch06.md` |
| `an1/authoring/blueprints/ch10.md` (AN1.10) | `an2/authoring/blueprints/ch07.md` |
| `an2/authoring/blueprints/ch04.md`–`ch08.md` (AN2.4–AN2.8) | `an2/authoring/blueprints/ch10.md`–`ch14.md` |

## Label migration

- **Atlas ids do not change.** An id travels with its chapter (spec/08 C6): AN2.1, AN2.2 and AN2.3
  are AN1 chapters 3, 5 and 8, and AN1.3, AN1.8, AN1.9 and AN1.10 are AN2 chapters. STATUS,
  NOTATION, blueprints and ledgers name chapters by atlas id. Only the volume and the local number
  change.
- **Labels do not change.** Book labels (`def-…`, `thm-…`, `exr-<section-slug>-…`) carry no chapter
  number. A label created in a moved chapter keeps its name.
- **Cross-book prefixes change with the volume.** A reference from AN1 to a label of AN2.1–AN2.3 is
  now an in-book `@label`, not `@an2:label`. A reference from AN1.3, AN1.8, AN1.9 or AN1.10 to an
  AN1 chapter is now `@an1:label`. Nothing is drafted in those chapters yet, so the rule applies
  when they are blueprinted and drafted.
- **Prose pointers use local numbers.** A pointer is "Chapter N" inside a volume, and "*Volume*,
  Chapter N" across volumes (`tools/series.py`). The old blueprints' "Part I / Part II" wording
  and their old `src/chNN-…` directories are out of date. Re-blueprinting removes them.
- **New prerequisites.** F4 *Analytic Preliminaries* is now a prerequisite. Its blueprints are being
  written in `../foundations/fd4/authoring/blueprints`. Cite only the planned chapters, as "F4.6",
  "F4.7", "F4.8", "F4.11" pointers, and no F4 labels until F4 is drafted. AN1 depends only on
  F-volumes, not on LA (spec/08 C2: AN2.1 drops s LA1.1 and b LA3.11; AN2.3's s LA1.2 becomes
  F4.8).

### Seam items in the drafted AN1.1 (not applied here)

AN1.1 has passed S8. Its forward pointers use the old local numbers. They need one seam pass, and
the ledger hashes that change go back for re-refereeing.

| File:line | Now says | Should say |
|---|---|---|
| `an1/src/ch01-least-upper-bound/03-the-axiom.md:28` | "a second, related meaning in Chapter 2, … reconciled in Chapter 11" | Chapter 4 (Cauchy sequences; or Chapter 5, metric completeness); Chapter 10 |
| `an1/src/ch01-least-upper-bound/04-epsilon-characterization.md:123` | "Once limits are defined in Chapter 2" | Chapter 4 |
| `an1/src/ch01-least-upper-bound/01-ordered-fields.md:233` | "From Chapter 2 on" | Chapter 4 (or "From the next chapters on", since Chapter 2 already uses ε-balls in ℝⁿ) |
| `an1/src/ch01-least-upper-bound/05-archimedean-property.md:111` | "Chapter 2 turns this … into the definition of a limit" | Chapter 4 |
| `an1/src/ch01-least-upper-bound/05-archimedean-property.md:198` | "Chapter 11 shows …" | Chapter 10 |
| `an1/src/ch01-least-upper-bound/06-density-and-roots.md:64` | "In Chapter 6 the IVT …; In Chapter 4 the Heine–Borel theorem" | Chapter 7; Chapter 2 |
| `an1/src/ch01-least-upper-bound/06-density-and-roots.md:175` | "which Chapter 10 builds from power series" | "*Integration, Series, and Function Spaces*, Chapter 7" |
| `an1/src/ch01-least-upper-bound/06-density-and-roots.md:280` | "In *Metric and Topological Spaces* the word dense" | "In Chapter 3" |
| `an1/src/ch01-least-upper-bound/07-nested-intervals.md:160` | "Chapter 11 answers both" | Chapter 10 |
| `an1/src/ch01-least-upper-bound/07-nested-intervals.md:389` | "in general in Chapter 6" | Chapter 7 |
| `an1/src/index.md` | the preface: title *Analysis on the Real Line*, chapter table AN1.1–AN1.11, "Chapters 2–10 … Chapter 11" | the new title and the 10-chapter table above |

Also pending, outside this move: `an1/config/config.json` `title` and the book's subdir
(`real-numbers-metric-spaces-and-derivatives`, with `analysis-on-the-real-line` as an alias) follow
the registry rename. `authoring/series.json` is regenerated by
`python3 tools/series.py refresh ../../registry` once the registry has the new volumes.
The config's `chapters` list does not change (only ch01 is drafted).

## Teaching manner (spec/08 C5, AN1 column)

- Apostol's order and breadth. The reference shelf (Apostol, Rudin PMA, Pugh, Tao, Abbott, Ross,
  Bartle–Sherbert, Spivak) is a source of coverage and technique only. Never copy wording,
  examples or exercises.
- Cummings' devices, at full strength in AN1:
  - Story hooks that are paid later: the Cantor set (AN1.4 → AN2.9, AN2.15), the Banach fixed
    point (AN2.2 → AN2.4, AN3.2), and the nowhere-differentiable function (AN1.7 → AN2.15).
  - Scratch Work kept apart from every major formal proof.
  - Support that fades through each chapter's exercises.
  - Definitions motivated by failure: open sets (the sequential definition is awkward), and Cauchy
    sequences (we do not know the limit).
  - The weird-examples table continued from F4.7.
  - A List of Results at the end of each chapter.
- No footnote jokes, no historical-anecdote footnotes, no first-person persona.
- AN1.4 proves Bolzano–Weierstrass and Heine–Borel with accumulation points (Apostol). The
  sequential versions wait for AN1.2.
- AN1.2 does one round on ℝ and then moves to metric spaces. Monotone convergence and limsup live
  here.
- The B(S) and C(K) completeness examples of the old AN2.2 move to AN1.9 (AN2).
