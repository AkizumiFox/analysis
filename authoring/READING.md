# Reading the book: schedules, rhythm, gates, feedback

This is the source for a future front-matter page, **"How to read this book"**, and for the reading paths still to be configured. It is written for the author and the coordinator; the page itself will be written from it in the book's voice (second person where it advises, per STYLE §7). It implements roadmap A6, A10, B2, B5 and B6; the evidence is in `authoring/design/research-reader.md` B1–B6.

Two warnings for whoever turns this into the page:
- **Chapter numbers are those of the 75-chapter `blueprint/book.yaml`**, after the accepted route changes (roadmap A1–A5, A7: linear systems as Ch 29, surfaces and the divergence theorem as Ch 45, probability as Ch 51 at the end of Part IV, topology in one block as Ch 60–61 at the start of Part VI, interpolation as Ch 72; Ch 37 now optional). If `book.yaml` is renumbered again, redo every table below before publishing.
- **Hours are estimates to be replaced by data.** They come from the formula in research-reader B1 (reading at about 15 minutes per 400 words of proof-dense prose; 20–45 minutes per exercise). When test readers log hours, the chapter index pages' **Time** lines and the tables here take the medians.

## Two tracks

- **Core track, about 25 hours a chapter:** read every section; do every Quick check and self-explanation prompt; all of A, one B and one C per section, the R group, and the exit checks.
- **Full track, about 35–45 hours a chapter:** every exercise.

A main-line reading is 68 chapters and **about 1,650–1,700 hours** on the core track; the seven optional chapters (6, 7, 19, 20, 37, 38, 69) add about 175.

## Schedules

These are **schedules**, not reading paths: orderings with weeks attached. They go on the page as tables, not in `config.json` (research-reader B6). Each Part ends with a Gate week.

### Two years, about 20 hours a week

A half-time student's load. 96 study weeks plus about 8 weeks of breaks. **Parts IV and V run one after the other, not side by side**: in parallel they would be about 32 hours a week for a semester, and every other stage is about 20 (roadmap A10).

| Weeks | Part | Chapters | Pace |
|---|---|---|---|
| 1–4 | 0, as a bridge | Ch 1–5, selected sections: skip Ch 2's final two sections and the depth of the Lean table; read Ch 4 §01–§04 and Ch 5 §01–§04 | about 1.3 chapters a week |
| 5 | Gate 0 | | |
| 6–19 | I | Ch 8–18 | 0.8 a week |
| 20 | Gate I | | |
| 21–33 | II | Ch 21–30 | 0.8 a week |
| 34 | Gate II | | |
| 35–43 | III | Ch 31–36, 39 | 0.8 a week |
| 44 | Gate III | | |
| 45–59 | IV | Ch 40–51 | 0.8 a week |
| 60 | Gate IV | | |
| 61–70 | V | Ch 52–59 | 0.8 a week |
| 71 | Gate V | | |
| 72–90 | VI | Ch 60–68, 70–75 | 0.8 a week |
| 91 | Gate VI (the capstone's mixed qualifying exam) | | |
| 92–96 | slack, and review for a qualifying exam | | |

### Three years, about 12–13 hours a week

A working adult's load. All 75 chapters, including the optional ones, over about 160 study weeks: about half a chapter a week (two weeks a chapter, plus a week for each Gate), so a seven-section chapter takes two weeks. The total is close to the two-year route's; the difference is that the three-year reader has time for the **full track in Parts 0 and I**, where the habits form.

| Year | Weeks | Content |
|---|---|---|
| 1 | 1–14 | Part 0, all 7 chapters, and Gate 0 |
| 1 | 15–44 | Part I (Ch 8–18, 19–20), and Gate I |
| 2 | 45–65 | Part II (Ch 21–30), and Gate II |
| 2 | 66–84 | Part III (Ch 31–39; Ch 37–38 optional), and Gate III |
| 2–3 | 85–109 | Part IV (Ch 40–51), and Gate IV |
| 3 | 110–126 | Part V (Ch 52–59), and Gate V |
| 3–4 | 127–159 | Part VI (Ch 60–75; Ch 69 optional), and the Gate VI capstone |

### Measure theory only, about 10–12 hours a week for one long semester

For a reader who already has real analysis, or wants only enough of it. About 320 hours.
1. **Weeks 0–2, entry test.** Take Gate I and the metric-space half of Gate II. Each failed problem's remediation map names sections; read exactly those, using the `measure-only` path page's list.
2. **Weeks 3–28: Ch 39 and Part IV** (Ch 40–51), about half a chapter a week. Ch 39 is the motivation; Ch 45 (surfaces) and Ch 51 (probability) can be left for later, but Gate IV's non-core problems test Ch 51.
3. **Weeks 29–30: Gate IV.**

A reader starting from nothing should instead take the two-year schedule through Part II, then Part IV: the path page will show that measure theory's prerequisites pull in most of Parts I–II.

### Complex analysis early (0 → I → II → V)

Part V needs nothing from Parts III–IV beyond one Poisson/Abel link, for which Part V gives a self-contained fallback (roadmap A6). A reader who wants complex analysis sooner can therefore run the two-year schedule with **Part V moved to weeks 35–44** (plus its Gate in week 45), then Parts III, IV and VI. The matching reading path is `complex-early` below.

## A week's rhythm

For every schedule. The shares are of the week's hours.

| Session | Share | What to do |
|---|---|---|
| 1–2 | 35% | Read a section. Attempt each *Try it first* theorem, and any theorem you like, for 5–10 minutes before reading its proof. Do every Quick check and self-explanation prompt **in writing**. |
| 3 | 30% | Exercises: all of A, one B, one C. Attempt before looking; open the hint ladder one rung at a time. |
| 4 | 15% | Review: the chapter's R items, re-attempted exit checks, and anything marked for review. |
| 5 | 20% | Write one proof in full, grade it against its marking scheme, and fix it. Keep an **error log**: for each error, the rule broken or the hypothesis missed. |

**When to move on from a chapter:**
- every A item is right;
- at least one B and one C per section are done without opening the solution;
- one exit check, **re-attempted after 48 hours or more**, succeeds.

If after a week you still cannot, **move on anyway** and mark the section for the next review session. Stalling is the likeliest way a reader working alone stops altogether; a mastery loop that never ends costs more than a gap that review will close.

## Checkpoints and gates

Three levels, each with feedback the reader can get alone.

| Level | What | Feedback |
|---|---|---|
| Section | Quick checks and the A exercise | immediate folded answers; no grading needed |
| Chapter | Exit checks (titled "Exit check"), each with a marking scheme | grade yourself, a partner or an AI against the scheme; re-attempt after 48 hours |
| Part | A **Gate**: the last section of the Part's last main-line chapter | timed and closed-book; pass line; remediation map |

**How a Gate works.**
- It is timed (2 hours for Gate 0, 3 hours after) and closed-book; the solutions are folded.
- It opens with a **definition drill**: every major definition of the Part, stated in symbols.
- Each problem has a marking scheme. **Pass line: 70% overall, and no core problem at 0.**
- Each problem lists, with links, the sections it tests. A failed problem sends you to those sections, not to "reread Part II".
- **A Gate is also an entry test.** A reader arriving at a Part by a reading path takes the Gate of the Part before it.

| Gate | Where | Size |
|---|---|---|
| Gate 0 | Ch 5 §07 (last section) | 2 h, 6 problems |
| Gate I | Ch 18 §06 (last section) | 3 h, 8 problems |
| Gate II | Ch 30 §07 (last section) | 3 h, 8 problems |
| Gate III | Ch 39 §08 (last section) | 3 h, 6 problems |
| Gate IV | Ch 51 §08 (last section); problems on Ch 51 are non-core | 3 h, 8 problems |
| Gate V | Ch 59 §08 (last section) | 3 h, 8 problems |
| Gate VI | Ch 75 §08 (last section) | 3 h, mixed across Parts IV–VI |

**Each Part is a complete course.** Stopping after Part I (a first course in real analysis) or after Part IV (measure and integration) is a legitimate outcome, and the page should say so plainly.

## Getting feedback without a teacher

This is the one place the book advises rather than teaches. Write it once, on the front-matter page.

**The loop.**
1. Attempt the problem.
2. Write the proof in full.
3. Self-explain it line by line, as Chapter 2 teaches: each line by earlier lines, definitions and named results.
4. Grade it against the marking scheme.
5. Only then read the book's solution, and compare it with yours line by line.
6. Log the error type.

**Using an AI tutor.**
- Unrestricted help lowers a learner's later independent performance; a tutor that withholds answers and asks for reasoning helps (research-reader B5). So give the AI a role, not the problem. Protocols to copy:
  - "Do not give me the proof. Ask me what the next step needs."
  - "Here is my proof and the marking scheme. For each step, say whether it is justified and which earlier result it uses."
  - "Find the first line that does not follow."
- **An AI grader disagrees with human graders on about a third of proofs**, is usually too strict, and marks down valid proofs that differ from the expected one. Treat a flagged line as a question to investigate, not a verdict. The marking schemes are written to award steps, not wording, so that a different correct proof can pass.

**People.**
- A question-and-answer site (Mathematics Stack Exchange) for a pinpointed question: the line, what you tried, why you think it fails.
- A study partner: exchange proofs and grade each other's with the marking scheme. Practise on a sample first (grade the book's own solution) so your grading is calibrated.

**Certain feedback, Part 0 only (optional).** Proof-assistant games (the Natural Number Game, and the logic worlds of the Lean game server) check a whole proof with certainty. They are optional practice beside Chapters 1–4, shown and never required.

## Reading paths to configure

These go into `config.json`'s `reading-paths` **only when every target section exists**; a missing target breaks the build. Targets are provisional, `<chapter dir>/<planned section number>` from the outlines in `blueprint/book.yaml` (75-chapter numbering). When each target chapter is drafted: re-check the target's section number and run `python3 tools/reading_path.py --profile <slug> --verify`.

Each target is the section holding the result the reader came for. `two-year` and `three-year` are **not** paths (they are the schedules above) and are removed from `decisions.md`'s list when these are configured.

**Entry Gate for each path** (a sentence in its `description` until the engine has a field for it): `measure-only` and `measure-for-probability` take Gate I and the metric half of Gate II; `complex-first-course`, `complex-only` and `complex-early` take Gate I; `functional-analysis` takes Gate IV; `toward-pde` takes Gate IV; `metric-spaces-and-odes` and `fourier-classical` take Gate I; `first-course-real-analysis` takes Gate 0.

```json
{
  "reading-paths": [
    {
      "slug": "foundations",
      "name": "Proof and sets: the foundations",
      "description": "Learning to write proofs from nothing: the rules behind every proof step, quantifiers and their negation, sets, functions and preimages, induction, and why the real numbers cannot be listed. For a reader preparing for any proof-based course.",
      "targets": [
        "ch02-quantifiers-and-proof/06",
        "ch03-sets-and-functions/06",
        "ch04-relations-and-induction/06",
        "ch05-countable-and-uncountable/04",
        "ch05-countable-and-uncountable/05"
      ]
    },
    {
      "slug": "first-course-real-analysis",
      "name": "A first course in real analysis",
      "description": "The standard first analysis course and nothing beyond it: continuous functions on closed intervals, the mean value theorem and Taylor's theorem, the Riemann integral and the fundamental theorem of calculus, uniform convergence, and the exponential and trigonometric functions built from power series.",
      "targets": [
        "ch13-continuity-on-intervals/03",
        "ch13-continuity-on-intervals/05",
        "ch14-derivative-and-mean-value/06",
        "ch15-riemann-darboux-integral/05",
        "ch16-sequences-of-functions/06",
        "ch17-power-series/07"
      ]
    },
    {
      "slug": "metric-spaces-and-odes",
      "name": "Metric spaces and differential equations",
      "description": "Why an ODE has a solution and when it is unique: contraction mappings and Picard–Lindelöf, compactness of function families and Peano's theorem, the inverse and implicit function theorems, the Baire category theorem, and linear systems solved by the matrix exponential, with the flow of an autonomous equation.",
      "targets": [
        "ch24-contraction-picard/05",
        "ch24-contraction-picard/06",
        "ch25-arzela-ascoli-peano/06",
        "ch26-stone-weierstrass-baire/05",
        "ch28-inverse-implicit/03",
        "ch29-linear-odes-flows/03",
        "ch29-linear-odes-flows/07"
      ]
    },
    {
      "slug": "fourier-classical",
      "name": "Classical Fourier analysis",
      "description": "Fourier series and integrals with the Riemann integral: Fejér's theorem, mean-square convergence and Parseval, Fourier inversion and Plancherel on the Schwartz space, the heat and wave equations, and Fourier analysis on finite groups.",
      "targets": [
        "ch32-good-kernels-summability/03",
        "ch33-mean-square-pointwise/03",
        "ch35-fourier-transform-line/03",
        "ch36-fourier-transform-rd/03",
        "ch37-finite-fourier-analysis/06"
      ]
    },
    {
      "slug": "measure-only",
      "name": "Measure and integration",
      "description": "The Lebesgue integral and what it buys: the dominated convergence theorem, Fubini–Tonelli, completeness of Lᵖ, the Lebesgue differentiation theorem, and Radon–Nikodym. For a reader who needs measure theory for analysis, probability or PDE.",
      "targets": [
        "ch41-lebesgue-integral/03",
        "ch43-fubini-tonelli/03",
        "ch46-lp-spaces/02",
        "ch48-lebesgue-differentiation/04",
        "ch50-signed-measures-radon-nikodym/05"
      ]
    },
    {
      "slug": "measure-for-probability",
      "name": "Measure theory for probability",
      "description": "Just what a probability course assumes: constructing a measure from its values on intervals and proving it unique, Lebesgue–Stieltjes measures as distribution functions, product measures, uniform integrability and Vitali's theorem, densities by Radon–Nikodym, and then probability itself: independence, the laws of large numbers and the central limit theorem.",
      "targets": [
        "ch42-abstract-measure/05",
        "ch42-abstract-measure/06",
        "ch43-fubini-tonelli/03",
        "ch47-modes-of-convergence/03",
        "ch50-signed-measures-radon-nikodym/05",
        "ch51-probability-measure-spaces/05",
        "ch51-probability-measure-spaces/07"
      ]
    },
    {
      "slug": "complex-first-course",
      "name": "A first course in complex analysis",
      "description": "Cauchy's theorem and integral formula, Liouville and the fundamental theorem of algebra, residues and real integrals, and counting zeros with the argument principle and Rouché's theorem.",
      "targets": [
        "ch53-cauchy-theorem/04",
        "ch54-singularities-residues/06",
        "ch55-global-cauchy-theory/05"
      ]
    },
    {
      "slug": "complex-only",
      "name": "Complex analysis to qualifying-exam level",
      "description": "Everything a graduate complex-analysis exam asks: the Riemann mapping theorem, harmonic functions and Harnack, Weierstrass products and Mittag-Leffler, analytic continuation, and Picard's little theorem.",
      "targets": [
        "ch56-conformal-riemann-mapping/06",
        "ch57-harmonic-functions/05",
        "ch58-entire-functions-products/04",
        "ch59-continuation-and-picard/02",
        "ch59-continuation-and-picard/06"
      ]
    },
    {
      "slug": "complex-early",
      "name": "Complex analysis straight after metric spaces",
      "description": "Complex analysis taken early, right after real analysis and metric spaces and before Fourier analysis and measure theory: holomorphic functions, Cauchy's theorem, residues, the Riemann mapping theorem, harmonic functions and Picard's little theorem, with nothing from Parts III or IV required.",
      "targets": [
        "ch55-global-cauchy-theory/05",
        "ch56-conformal-riemann-mapping/06",
        "ch57-harmonic-functions/05",
        "ch59-continuation-and-picard/06"
      ]
    },
    {
      "slug": "functional-analysis",
      "name": "Functional analysis",
      "description": "The four theorems of Banach-space theory — Hahn–Banach, uniform boundedness, open mapping and Banach–Alaoglu — then Hilbert spaces, Lax–Milgram, and the spectral theorem for compact self-adjoint operators.",
      "targets": [
        "ch64-hahn-banach/04",
        "ch65-baire-category-operators/04",
        "ch66-weak-topologies-alaoglu/06",
        "ch67-hilbert-spaces/06",
        "ch68-compact-operators-spectral/07"
      ]
    },
    {
      "slug": "toward-pde",
      "name": "Toward PDE: the Dirichlet problem",
      "description": "Solving −Δu = f in a bounded domain the modern way: distributions, Sobolev spaces, Plancherel, Rellich compactness, weak solutions by Lax–Milgram, and the eigenbasis of the Dirichlet Laplacian.",
      "targets": [
        "ch71-tempered-distributions-fourier/03",
        "ch74-poincare-rellich/05",
        "ch75-dirichlet-capstone/03",
        "ch75-dirichlet-capstone/06"
      ]
    }
  ]
}
```

**Notes.**
- **`complex-early`** exists to prove a claim: that Part V's closure contains nothing from Parts III and IV. Its `--verify` page must show no Part III or IV section; if one appears, Part V needs the fallback the route report asks for (roadmap A6), not a longer path. If its closure turns out identical to `complex-only`'s, keep one entry, with `complex-early`'s description folded into `complex-only`'s.
- **`toward-pde`** will close over most of the main line. Keep it only if its page still lists a meaningful set of skippable sections (Part V, Ch 37–38 and 51, much of the topology in Ch 60–61); otherwise drop it and let the two-year schedule stand for it.
- **`foundations`** is almost all of Part 0's main line. That is acceptable: its reader is narrow (someone who wants a transition-to-proof course).
- **`measure-only` and `measure-for-probability`** differ mainly by Ch 48–49 (maximal function, bounded variation), Ch 46 §5–§7, and Ch 51 (probability, roadmap A3), which only `measure-for-probability` targets. If the rest of the difference is small, keep both anyway: Ch 51 is the reason for the second path.
- **`complex-first-course` and `complex-only`** are split on purpose: a one-semester undergraduate reader should not be sent through normal families and Picard.
- **Linear-algebra gates** (roadmap A8): the gates are published as external prerequisites of Ch 21 (Part II), Ch 27, Ch 29 and Ch 31 (Part III, needed before Ch 33). Paths whose closure reaches any of them should say in their description which chapters of the linear-algebra companion to finish first.
