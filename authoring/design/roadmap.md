# Roadmap: decisions from the three research reports (2026-09-28)

This is a synthesis of `research-route.md` (the route), `research-production.md` (how to write it) and `research-reader.md` (how a self-taught reader travels it). Each item names its source section, the lead's recommendation, and its state (**proposed** until the author decides). Once an item is accepted, it is applied to `book.yaml`, `decisions.md` or `STYLE.md`, and its state becomes **done**.

## A. The route (book.yaml)

The verdict of research-route: the spine is right. Keep the real line before metric spaces, Fourier before Lebesgue, ℝᵈ before abstract measure, functional analysis out of measure theory, and the Dirichlet capstone.

| # | Change | Evidence | Lead's view | State |
|---|---|---|---|---|
| A1 | A new main-line chapter, **surfaces, surface measure and the divergence theorem**, after ch. 46. Green's theorem moves there; the traces in ch. 71 and ch. 72 need it (route R1). | strong | accept: it fills a real gap in the capstone's prerequisites | proposed |
| A2 | **Topology in one block**: ch. 30, 31 and 41 become two chapters at the start of Part VI. Part IV uses the metric Urysohn. This reverses decision 8 (route R2). | moderate | accept: it saves about 40 pages, and topology arrives just before its only users | proposed |
| A3 | A new main-line chapter, **probability on measure spaces**, at the end of Part IV (LLN, CLT by Lindeberg), plus an optional section on characteristic functions in Part VI (route R3). | strong | accept; if the S3 load is too heavy, it can be read after Part VI | proposed |
| A4 | A new chapter on **linear systems, the matrix exponential and flows** in Part II (route R4). | moderate | accept (paid for by A2) | proposed |
| A5 | **Interpolation**: Marcinkiewicz in ch. 49; Riesz–Thorin and Hausdorff–Young in Part VI (route R5). | moderate | accept | proposed |
| A6 | A **complex-early** reading path (0 → I → II → V) (route R6, reader B6). | strong | accept; nearly free | proposed |
| A7 | **Part III trimmed**: ch. 38 (finite groups) and the Kirchhoff/Radon parts of ch. 37 become optional (route R7). | opinion/moderate | accept | proposed |
| A8 | Publish the **linear-algebra gates**: which companion chapters must be done before ch. 27 and ch. 34 (route R8). | moderate | accept | proposed |
| A9 | Consider: optional chapters on Hausdorff measure and differential forms/Stokes; interior H² regularity in the capstone; Hilbert before Banach in Part VI; the bounded self-adjoint spectral theorem (route C1–C7). | moderate/opinion | decide after Part IV; not blocking | proposed |
| A10 | Two-year schedule: **Parts IV and V in sequence, not in parallel.** Parallel would be about 32 hours a week (reader B1). | estimate | accept (a reading-path/schedule change, not a book change) | proposed |

## B. The reader (STYLE.md, exercise design, config)

| # | Change | Evidence | Lead's view | State |
|---|---|---|---|---|
| B1 | **Self-explanation training passage**, once, in Chapter 2 (reader B7.1; d = 0.95). | strong | accept | proposed |
| B2 | **A Gate at the end of each Part**: timed, with a marking scheme, a pass line, and an `@ref` remediation map (ch. 5, 18, 31, 40, 51, 59, 72) (reader B2). | moderate | accept | proposed |
| B3 | An **R. Review** exercise group at the end of each chapter, with spaced and interleaved items (reader B3/B7.5). | strong | accept | proposed |
| B4 | **New exercise formats**: proof comprehension, find-the-error with a *true* conclusion, proof ordering, faded proofs, "try it first", marking schemes, a hint ladder (reader B4, B7.2–8). | strong for most | accept, tapering after Part I (B7.12) | proposed |
| B5 | A **time estimate** in each chapter index; a weekly rhythm in the preface (reader B1, B7.9). | estimate | accept | proposed |
| B6 | **Reading paths** become about 10 narrow paths. The two-year and three-year routes become schedules on a "How to read this book" page, not paths (reader B6). | — | accept | proposed |

## C. Production (tools, per-chapter pipeline)

The key finding of research-production is that the pilots' mathematics is sound and their errors are in prose meta-claims and dependency bookkeeping. False mathematics enters through **blueprints**, as linear-algebra's history shows.

| # | Change | Lead's view | State |
|---|---|---|---|
| C1 | **Fix the pilot findings** (§3.1): Ch 8 has 2 false prose sentences and 4 dependency gaps; Ch 1 has 1 false meta-claim, 1 Lean rendering problem and 1 "RAA in costume" model proof; the reiteration rule in NOTATION.md must be reconciled with the chapter. | do before approving the exemplar | proposed |
| C2 | **The per-chapter pipeline** of §5.2: blueprint expansion → blueprint verification (statement referee plus Mathlib anchoring with back-translation) → draft (sidecar scripts, dependency ledger) → mechanical gates → two blind referees (proofs; claims and bookkeeping) → exercises solved blind → revision accepted by a fresh re-referee → seam referee → author samples one section. | accept | proposed |
| C3 | **Tools** (§6), first tranche: `check_structure.py`, `check_fitch.py`, `promises.py`, `check_rendered.py`, `ledger.py`, `check_blueprint.py`. Second tranche: `lean/` + `lean_check.py` + back-translation, `verify/` + `check_numbers.py`, `metrics.py`, `seed_errors.py`, `check_notation.py`. | accept; first tranche before wave 1 | proposed |
| C4 | **Order**: waves of 3–4 chapters in dependency order, starting with Part 0 (ch. 2–5, which pay Chapter 8's promises); the first chapter of each Part goes alone as a Part pilot; Parts IV and V interleaved (§5.1). | accept | proposed |
| C5 | **Budget**: about 6–9M tokens and 5–7 agent-hours per chapter; about 3–5 weeks for the book, limited by the author's review (about 60–70 hours) (§7.2). | note | — |

## Proposed next steps, in order

1. The author decides on A, B and C (this file).
2. Wave 0:
   - fix the pilot findings (C1), including the B-items that touch Chapters 1 and 8;
   - approve the exemplar;
   - build the first tranche of tools (C3);
   - apply the accepted A-items to `book.yaml` and re-run `check_order.py`;
   - regenerate the blueprints.
3. Wave 1: Chapters 2–5, the rest of Part 0's main line, including the excluded-middle section and the self-explanation training.
