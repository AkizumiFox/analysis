# Writing standard for the book

This file is for anyone who writes a section: me, or a drafting agent. Read all of it before you write. Also read `authoring/NOTATION.md` and the chapter's blueprint in `authoring/blueprints/`.

The method comes from the kwok-proof skill (`/home/akizumi/coding/kw/skill/kwok-proof/`). Read these parts of it before your first section:

- `SKILL.md`: the sections "How he thinks", "Typeset register" and "Board register".
- `references/explaining.md`: §1–§7, and the exemplar in §8 closest to your topic.
- `references/written-solutions.md`: §1–§3 and two exemplars.
- `references/ana.md`: all of §1 (heuristics H1–H28), §2–§3, and §5 (the spoken-vs-written gap: backwards Idea, forward Proof; constants placed first and justified last). This is the analysis reference; `la1.md`/`la2.md` only when a chapter leans on linear algebra.
- `references/problem-setting.md`: §1–§4, for the exercises.

**Hard rules**
- **Nobody is named.** The book never names, quotes or alludes to the lecturer the skill was distilled from. It uses his method silently. Never write "as X would say", course weeks or theorem numbers from his notes.
- **No copying.** The reference books (converted to Markdown under `~/coding/analysis/converted/`, listed in `blueprint/sources.yaml`) are copyrighted. You may use them to check which topics exist and whether a statement is true. Do not paraphrase their prose or copy their examples or exercises. Standard theorems are common property, but the explanation, the examples and the exercises must be our own. `blueprint/originality.py <chapter>` checks this; run it before handing a chapter back.
- **No forward references in proofs.** A proof may cite only results that appear **earlier** in the book: an earlier section, or earlier in the same section. The blueprint lists what each section may use. A forward pointer in the prose ("we will prove in Chapter 10 that …") is fine. It must never be a step in an argument.
- **Every claim is true.** Check every computation (with sympy, privately: the book text never mentions software, "sympy confirms" or how a result was verified; write a by-hand check the reader can follow instead), and state every hypothesis (non-empty, bounded, closed, compact, complete, σ-finite, 1 ≤ p < ∞, …). If you are unsure, compute it (sympy) or leave a `TODO(verify)` comment. Never guess.

---

## 1. The reader

The reader is a motivated student working **alone**. They have no lecture to fill gaps and no one to ask. Care for them:

- **Say why before what.** Explain what problem a definition or theorem solves before stating it.
- **Recall before use.** When an earlier result is used, recall it in a clause, name it, and link it with `@label`.
- **Warn early.** Name a known trap *before* the reader can fall into it, with a concrete failing case.
- **Let the reader check themselves.** Put a Quick check with a folded answer in every section.
- **Show every move.** Where a move is not visible ("why this basis?"), give one clause of reason. The written proof stays minimal and forward; the Idea block carries the discovery.
- **Stay calm.** No hype and no "clearly" or "obviously" hiding a step. "Trivially" is allowed only for something that really is one line and is then written out.
- **One new notion at a time.** Use at most two new **major** notions per section. Minor definitions (notation, auxiliary terms) may exceed this when they are introduced just before their first use; if a section carries more than two major notions, the blueprint splits it.

## 2. Page skeleton

Each section is one Markdown file, `src/chNN-slug/MM-slug.md`, whose first line is `# Title`.

```markdown
# Title of the Section

Opening frame: 2–4 sentences. Where we are, what question is open, what this section
does. Plain prose, no heading.

## First subsection heading

...notion or theorem blocks...

## Exercises

### A. Check your understanding
### B. Practice
### C. Going deeper
```

Section titles (the `#` line) contain no math, since they appear in navigation links and page titles. Use `##` for subsections (they appear in the page's table of contents) and `###` only inside Exercises or for a long worked computation. Aim for **2,500–5,000 words**. Split a longer section at a natural seam.

A chapter's `index.md` contains, in this order:
1. `# Chapter Title`.
2. A 1–2 paragraph story of the chapter: the question it answers and why the reader should care.
3. **What you need:** the earlier chapters or sections used, with links.
4. **Roadmap:** a bullet per section, with one sentence each.
5. **Named moves:** a short list of the proof techniques this chapter introduces, so the reader can transfer them.

## 3. Introducing a notion (the explain template)

For each new definition, in order:

1. **Situate** (1–2 sentences). Where does it sit? Objects then maps, an object then its subobjects, or a question left open.
2. **Hook.** Choose **one**:
   - a naive notion that fails, shown failing;
   - a recurring expression that deserves a name;
   - the standard example, generalised;
   - a goal theorem stated first ("we want to prove …; we need a word for …");
   - an everyday word.
3. **Slogan.** One sentence in plain words, written in *italics* as its own paragraph.
4. **Definition.**
   - Every quantifier, and what it is defined on.
   - **Bold** the term defined and the small words that carry weight: **for every**, **there exists**, **strictly**, **a** vs **the**, **non-empty**, **eventually**, **uniformly**.
5. **Paraphrase** clause by clause ("In words: the first condition says …").
6. **Well-definedness**, if there is anything to check: independence of choices, existence, uniqueness.
7. **Examples**, 2–4 of them, simplest first.
   - Check each against the definition clause by clause.
   - Spread them across the families: sequences in ℝ, functions on intervals, ℝⁿ, sequence spaces (ℓᵖ), function spaces (C[a,b], Lᵖ), the discrete metric.
   - Include one degenerate case (the empty set, a singleton, a constant sequence, the zero function) and say why it matters.
8. **Non-example by minimal change.** Change one example slightly, say what still works, and name the exact clause that fails.
9. **Why this definition.** What breaks if a clause is dropped or a convention changed. Where the name comes from, if it helps.
10. **Warning** (`::: {.warning}`). The misconception, with a concrete failing case.
11. **Payoff.** The first small result, a link to an earlier concept, and one sentence on where this is going.

Not every notion needs every step at full size. A minor auxiliary definition may use steps 4, 7 and 8 only. **Major notions get all eleven.** These include: supremum, limit of a sequence, Cauchy sequence, series convergence, open/closed/compact set, continuity, uniform continuity, derivative, Riemann integral, uniform convergence, metric space, completeness, compactness, connectedness, equicontinuity, Fréchet derivative, topology, Fourier series, σ-algebra, measure, measurable function, Lebesgue integral, Lᵖ, holomorphic function, contour integral, residue, normed and Banach space, Hilbert space, dual space, weak convergence, compact operator, distribution, Sobolev space, and similar.

## 4. Theorems and proofs

For each theorem:

1. **Lead-in sentence.** Say what the result does or what need it fills ("It turns out that a continuous function cannot skip a value:").
2. **The statement**, complete and self-contained, with all hypotheses. Give it a short `[Name]` title when it has a standard name or will be cited later.
3. **Idea** (`::: {.idea}`, 2–6 lines, plain prose).
   - The reasoning found backwards, a picture described in words (or TikZ), a small case, or a numbered plan ① ② ③.
   - This is where "why do we do this?" is answered.
   - Omit it for proofs of 3 lines or fewer.
4. **Proof** (`::: {.proof}`), in the typeset register:
   - **First sentence does mathematics:** "Let …", "Suppose …", "Since …", "By @thm-x, …". Never motivation (that went in the Idea).
   - **Chain the steps** with Therefore / Hence / Thus / In particular / Then.
   - **Every step names its reason**: a hypothesis, a definition, or a cited result (`@label`, not restated). Where a display hides a reason, add "where the second equality uses …".
   - **Always justify:**
     - each clause of a definition being verified;
     - why a choice is possible (a sup exists because the set is non-empty and bounded above);
     - what each chosen constant depends on;
     - non-zero before dividing, positive before taking a square root or logarithm;
     - the theorem licensing every exchange of limits, sums, integrals and derivatives;
     - measurability and integrability before integrating (from Part IV on).
   - **You may skip:** a symmetric half ("swapping the roles of \( d_1 \) and \( d_2 \) gives the reverse inequality"), and a repeat of an argument just given.
   - **Labels:** `\( (\Rightarrow) \)`/`\( (\Leftarrow) \)`, `\( (\subseteq) \)`/`\( (\supseteq) \)`, *Case 1.*/*Case 2.*, and `::: {.claim}` with a nested `::: {.proof}` for a genuinely separate fact inside a long proof.
   - **Ending:** "This shows …" / "This proves …" / "as claimed".
   - **Length:** most proofs are 5–20 lines. For a long theorem (Heine–Borel, Arzelà–Ascoli, the inverse function theorem, Carathéodory, Lebesgue differentiation, Radon–Nikodym, the Riemann mapping theorem, Rellich), write a **Step roadmap** in the Idea, then `**Step 1.**` … inside the proof, with Claims.
   - **One proof per theorem.** A second route gets at most one short "Alternatively," paragraph, and only when it teaches something.
5. **Aftermath** (1–2 sentences). What is this result for? What does it let us do now? Use a `::: {.remark}` only if it needs a separate block, e.g. "the converse fails: …".

**Preferred proof routes.** These are the analysis heuristics of `references/ana.md` §1, in the book's words. Use whichever fits.

- **Givens and goal first (H1).** Unwind the goal into its definition; the definition tells you what to fix arbitrarily (a point, ε, a sequence, an open cover).
- **Backwards Idea, forward Proof (H17, G1–G2).** For ε–N and ε–δ, the Idea works backwards from the target inequality, bounding by "something a little bigger" when it cannot be solved. The Proof then places the constant first (`Let \( \delta \coloneqq \min\{1, \varepsilon/10\} \)`) and justifies it last. Never make the reader reverse-engineer where a constant came from.
- **Say what each chosen constant depends on.** "Choose \( N \) (depending on \( \varepsilon \))", "\( \delta \) depends on \( \varepsilon \) **and on \( x \)**". Quantifier order is the single commonest source of false proofs in analysis, and the page must make dependence visible (see §10).
- **Combine constraints with a max or min (H13),** and say that finiteness is what makes it legitimate.
- **Insert a third point (H14).** Use the triangle inequality through the limit, a subsequence term, or an approximant; the 3ε argument; telescoping plus a geometric series for Cauchy bounds.
- **Suppose not; negate quantifier by quantifier (H4, H23).** Write the negation as its own display line. Then specialise δ = 1/n to get a sequence.
- **Sup and inf (H24).** Split into "upper bound" and "least"; use "least" through "sup S − ε is not an upper bound", which hands you a witness.
- **Bounded sequence ⇒ Bolzano–Weierstrass (H19),** then closedness keeps the limit inside.
- **Compactness (H10).** To prove it, take an arbitrary cover or sequence. To use it, manufacture a cover from the data, keep finitely many, and exploit the finiteness.
- **Existence by completeness (H25).** Show the natural sequence is Cauchy and let completeness supply the limit. For "X is complete": find a candidate, upgrade the convergence, and check the limit is in the space.
- **Switch characterization (H12).** Use sequences for discontinuity, and preimages of open sets for inverses and regions.
- **Reduce to real numbers (H15),** by coordinates or by freezing a point.
- **Density.** Prove it on a dense class, then extend by a uniform or norm bound.
- **Exchange of limits.** Before swapping lim with lim, sum, ∫ or d/dx, name the theorem that licenses it (uniform convergence, M-test, MCT, DCT, Fubini–Tonelli) and check its hypotheses on the page.
- **Give each hypothesis a job (H6).** An unused hypothesis is where the finish comes from.
- **Refute with one concrete witness (H9).** The discrete metric, ℚ, (0,1), xⁿ, a shrinking interval, the typewriter sequence.

### Optional results

Some results are worth stating and proving and yet nobody is obliged to read them: an illustration of a definition just given, a remark that deserves a proof, a bridge showing how this corner of the book meets another. Keep writing them. Mark them:

```markdown
::: {#thm-adjoint-vs-dual .optional}
[The Adjoint Is the Dual Map Read Through Riesz]
```

`.optional` goes on the statement's div, beside its id. Both editions then print a marker on the title line — *Optional: nothing later depends on this.* — and the reader may skip the block, its Idea and its proof without wondering what they lost.

**What it buys.** The reading paths (`tools/reading_path.py`) treat an optional result's citations as context rather than prerequisites. Nothing requires the result, so nothing it cites can be required through it, and it puts no section on anybody's path. That is the point: `thm-adjoint-vs-dual`, a two-line verification that the adjoint is the dual map read through Riesz, put two sections of Chapter 5 and one of Chapter 1 onto seven of the ten reading paths. Marked optional, it puts nothing on any of them, and the label stays in the book.

**The invariant.** *Nothing anywhere may be proved from an optional result.* No proof, proof idea, claim or written solution may cite one — in the whole book, not just later in the section. `tools/check_optional.py` checks it and `./build.py check` fails on it, naming the citing sites:

```
ch12-spectral-theory/04: thm-spectral cites thm-aside in its proof,
but thm-aside is marked optional (ch11-inner-products/06)
```

When that fires, one of two things is true: the result is genuinely used, so drop `.optional`; or the citing argument can be written without it, so write it that way. Never both mark a result optional and lean on it — the marker is a promise printed on the page.

Prose, statements, remarks, warnings and quick checks may point at an optional result freely. That is how a connection is meant to be referred to.

**When to reach for it.** An illustration, or a connection between two parts of the book. Reach for it especially when a short result cites material from a chapter the surrounding section otherwise never needs; the marker is what lets the material stay without taxing the reader. Never use it on something a later proof needs, and never as a way to keep a result whose citations you would rather not justify. If in doubt, ask what breaks if the reader skips it: if the answer is anything but "a sentence elsewhere loses a pointer", it is not optional.

Run `python3 tools/check_optional.py --list` to see everything currently marked.

## 5. Examples, checks, warnings, remarks

- **Examples** `::: {#exm-slug}` with a `[Title]` first line. State the question inside the example. Put the worked answer in a following `::: {.solution}`; it starts folded on the web. Choose data so the computation is clean: explicit ε-thresholds that come out as integers, sums that telescope, functions whose integrals are elementary.
- **Quick check** `::: {.check}`: one short question. Its answer is a `::: {.solution}` placed **right after** the check block closes, never nested inside it. Put at least one per section, placed right after the idea it tests. Good checks:
  - a non-example failing only clause k;
  - "why must this be strict?";
  - "is this look-alike an example?";
  - a tiny computation.
- **Warning** `::: {.warning}`: one misconception, a concrete failing case, 1–4 sentences.
- **Remark** `::: {.remark}`: 1–3 sentences with one job (converse fails, other names or notations, in other words, outlook).
- **Pictures:** TikZ inside `\begin{center}\begin{tikzpicture}…\end{tikzpicture}\end{center}` in a raw LaTeX block, or with the tikz syntax already used in `src/`. Use one idea per figure. Colour must never be the only carrier of meaning.
- **Interactive:** `::: {.plot fn= x= y= params=}` for functions with sliders, `{.python .run}` for small numpy/sympy experiments, and `::: {.widget src=}` with a `::: {.print}` fallback. Use them sparingly and only where exploring helps (partial sums of a series, uniform vs pointwise convergence of fₙ, Fejér means, a contraction's iterates).

## 6. Exercises

Each section ends with `## Exercises` and three groups.

**A. Check your understanding.** Exactly one exercise with 2–6 lettered parts: define, state, decide true/false with a reason, negate a definition, name the method. Readers should be able to answer before moving on.

**B. Practice.** 2–4 exercises "like the examples", each with a worked example type in the section:
- A "Determine which of the following … Justify your answer." batch with one or two planted failures.
- A computation (a limit, a sup, an explicit N or δ, an integral) ending in "Hence …".
- A routine proof applying one theorem once.

**C. Going deeper.** 1–4 exercises:
- a (a) Prove / (b) Deduce pair;
- a counterexample, construction or dropped-hypothesis item ("Is this still true on (0,1)?");
- optionally one harder problem, made reachable with scaffolded parts and a hint.

**Format.** Every exercise is `::: {#exr-<section-slug>-a1}` (then `-b1`, `-b2`, `-c1`, …) whose first line is a title `[A1]`, `[B2: Short name]`, etc. It is followed by a `::: {.solution}` written in the typeset register (complete, not a sketch).

**Parts** use a lettered list:

```markdown
::: {.enumerate options="label=(\alph*)"}
1. ...
2. ...
:::
```

**Wording:** "Prove that", "Determine whether … Justify your answer.", "Give an example of …", "Explain why … is **not** …", "Hence deduce …".

**Hints** go at the end in italics: *Hint: consider the kernel of …*. A hint names a tool or an object, never a step.

**Calibration:**
- B uses one theorem once.
- C combines two ideas, generalizes (ℝ → metric space → normed space), or drops a hypothesis and asks what survives.
- A harder C item uses three ingredients, one from an earlier chapter.
- A later exercise may cite an earlier one ("By @exr-span-b2 …").

## 7. Prose

- **Voice.** "We" for the author and reader together; "you" sparingly, for direct advice. Median sentence 12–18 words. Paragraphs of 1–4 sentences. Vary rhythm; no walls of text.
- **Emphasis.** Bold is for defined terms and load-bearing small words, italics for slogans and light emphasis. No exclamation marks, and no "Note that" at the start of every other sentence.
- **Names.** Name results by content ("the Bolzano–Weierstrass Theorem"), with `@label`. Titles of named theorems match exactly so the dependency graph picks up mentions.
- **Promises.** Every forward promise ("we will see in @sec…" or "in Chapter 9") must be paid off. When writing, add each promise to `authoring/STATUS.md`.
- **Spelling.** American spelling: "normalize", "color", "behavior", "center". Mathematical names keep their accents (Gershgorin, Schur, Cauchy–Schwarz with an en dash).
- **Math delimiters.** `\( … \)` inline and `\[ … \]` display, never `$` (except inside TikZ and inside `\tag{$\ast$}`). Numbered equations take `{#eq-slug}` **on the same line as the closing `\]`, with no space** (`\]{#eq-normal-equations}`), and are cited with `@eq-slug`; on its own line, or after a blank line, the label is just text.
- **Relation symbols are typeset, never plain characters.** Write `\( \Rightarrow \)`, `\( \subseteq \)`, `\( \in \)`, `\( \le \)`, not the unicode characters — including proof-direction tags `\( (\Rightarrow) \)` and chains such as `(a) \( \Rightarrow \) (b)`. (An arrow used rhetorically, as in "abstract space → write down a matrix", is ordinary prose and stays plain, as does an environment title such as `[The 2 × 2 puzzle]`.)
- **Vectors are plain.** Unlike the linear-algebra companion, points of ℝⁿ, of a metric space and of a function space are plain italic (x, y, f); bold is reserved for defined terms in prose. Matrices, when they appear (Jacobians, linear maps of ℝⁿ), are plain capitals (A, Df(a)).
- **Displays must fit the text column.** A formula wider than about 60 characters of ordinary math should be broken with `aligned`, `split` or `cases` inside `\[ … \]`, aligned at `=` or at a natural operator, rather than left to overflow.
- **Macros** are in `latex/macros.tex`; use those listed in `NOTATION.md`. Define nothing ad hoc. If a new macro is needed, add it to `macros.tex` and `NOTATION.md`.

## 8. Authoring syntax reference

```markdown
::: {#thm-bolzano-weierstrass}
[Bolzano–Weierstrass Theorem]

Every bounded sequence in \( \nR \) has a convergent subsequence.
:::

::: {.idea}
We want ...
:::

::: {.proof}
Let ...  This proves the theorem.
:::
```

- **Environment prefixes:** `thm`, `lem`, `cor`, `prp`, `ax` (shared counter; `ax` is Axiom, used for the least upper bound axiom); `def`; `exm`; `exr`; `cnj`. Small blocks with no label: `.proof`, `.solution`, `.remark`, `.claim`, `.idea`, `.warning`, `.check`, `.algorithm`.
- **Labels** are lowercase-hyphenated and describe content (`thm-bolzano-weierstrass`, not `thm-3`). They are global across the book and must be unique.
- **References:** `@thm-bolzano-weierstrass` renders as "Theorem 3.12" with a hover preview; `@eq-slug` works for equations.
- **Optional results:** `::: {#thm-foo .optional}` marks a result nothing later depends on (§4). Nothing may be proved from one; `./build.py check` enforces it.
- **Labeled lists:** `::: {.enumerate options="label=(O\arabic*)"}` wraps an ordered list.
- **Web-only content:** `::: {.content-visible when-format="html"}`.

## 9. Before handing a section back

- [ ] Every definition is preceded by its need. Major notions follow §3 in full.
- [ ] Every proof cites only earlier results, and every step names its reason.
- [ ] Every example's arithmetic is verified (sympy for anything with more than two steps), and every chosen constant (N, δ, r) is checked to do its job.
- [ ] There is at least one Quick check (its solution a sibling block after it), one warning and one non-example. The exercises have A, B and C groups, each exercise with a complete solution.
- [ ] Every B-type task has a worked example in the text.
- [ ] Notation matches `NOTATION.md`. No symbol is used before it is introduced, and none is reused with a new meaning.
- [ ] Labels are unique (grep `src/`), and every `@ref` target exists or is created in this chapter.
- [ ] Anything marked `.optional` is genuinely skippable: no proof, idea, claim or solution anywhere cites it (`python3 tools/check_optional.py`).
- [ ] Every theorem's hypotheses are each used, and each major theorem has a remark or exercise showing what fails when one is dropped.
- [ ] Every chosen constant says what it depends on.
- [ ] No copied text or examples from the references (`blueprint/originality.py`), and no attribution to any person.

## Hyphenation of "non-"

The book writes **non-negative**, **non-empty**, **non-zero**, **non-decreasing**, **non-increasing**, **non-measurable** and **non-Archimedean** with a hyphen, as the linear-algebra companion does. Labels and directory names are exempt: write `thm-nonempty-bounded-sup`, not `thm-non-empty-...`.

## 10. Analysis-specific rules

These come from the planning record (`authoring/design/decisions.md`, `curriculum.md`) and from the education research summarized there.

- **Quantifiers are shown, not hidden.** A definition with nested quantifiers is also given in symbols (∀ε > 0 ∃N ∈ ℕ ∀n ≥ N …) after its prose form. When a uniform notion first appears (uniform continuity, uniform convergence, equicontinuity), a Quick check asks the reader to swap two quantifiers and say what changes.
- **A counterexample for every hypothesis that matters.** Each major theorem is followed by a remark, warning or exercise showing what fails when one hypothesis is dropped, with a named witness. The four modes of convergence, compact versus closed-and-bounded, and Riemann versus Lebesgue all get their own tables of witnesses.
- **The spiral is written out.** When a concept returns at a higher stage (compactness on ℝ, then in a metric space, then weakly), the opening frame of the section recalls the earlier version with `@label` and says in one sentence what changes and what survives. The spiral table in `curriculum.md` lists the returns.
- **Motivating problems come first.** Each chapter's `index.md` names the concrete problem that forces the chapter's main abstraction. A section never introduces a notion without saying what problem it answers (§3, step 2).
- **Proof verification is practised.** At least one exercise per chapter (usually a C item) gives a flawed proof and asks for the exact line that fails and the reason. In Part 0 the reason names the natural-deduction rule broken; after Part 0 it names the missing hypothesis or the illegal step.
- **Self-explanation prompts.** For the three or four hardest proofs of a chapter, the Idea ends with a prompt such as "*Before reading on: where will compactness be used?*" (at most one per proof).
- **Part 0's rule tags.** In Part 0 only, proofs may annotate steps with the natural-deduction rule in small caps in brackets (e.g. `[∀I]`, `[∃E]`). Later Parts do not, but the "what is not allowed" catalogue of Part 0 is cited (`@...`) when a warning concerns one of its errors.
- **Choice and non-constructive steps are flagged in prose.** Where a proof uses the axiom of choice (countable unions, Vitali, Hahn–Banach, Tychonoff) or a genuinely non-constructive step discussed in the excluded-middle section, one clause says so. Do not dwell on it.
- **The companion book.** Linear algebra is cited as "the linear-algebra companion, Chapter N" in prose, never re-proved and never `@ref`ed.
