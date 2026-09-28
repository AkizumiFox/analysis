# Book-wide notation

This list is fixed. A chapter that needs a new symbol adds it **here**, and a new macro in
`latex/macros.tex`, before using it. The left column is what to type.

The conventions in "Standing conventions" are shared with the linear-algebra companion; the
tables below are the analysis book's. Fill a row the first time a symbol is used, not later.

## Standing conventions

These are book-independent. Keep them.

- **Points and vectors are plain italic** (\( x \in \nR^n \), \( f \in C[a,b] \)), unlike
  the linear-algebra companion's bold vectors: in analysis the same letter moves between ℝ,
  ℝⁿ and function spaces, and bold would have to switch on and off. The bold one-letter
  macros (`\v`, `\A`, …) exist in `latex/macros.tex` for the engine; this book does not use
  them.
- **Ordered things go in parentheses, unordered in braces.** An ordered basis is
  `\sB = (\v_1, \dots, \v_n)`; a set is `\{ \v_1, \dots, \v_n \}`. The distinction is load
  bearing the first time order matters, and a reader who has seen it kept everywhere trusts
  it.
- **The two-slot bracket rule.** `\coord{x}{B}` renders \( [x]_{B} \) and `\mtx{T}{B}{C}`
  renders \( [T]_{B}^{C} \): the object in brackets, the data it is taken relative to hanging
  off the brackets, **source below and target above**, always in that order. One notation for
  "X relative to Y", chosen once. Never write a second one for the same thing; the linear
  algebra book carried two for a year and every cross-reference had to be checked by hand
  when one was retired.
- **One symbol, one meaning, book-wide.** If a symbol must be reused with a different
  meaning in a later chapter, say so in its row here and state where the two uses could meet
  and why they do not.
- **Define it before you use it.** No symbol appears before the row that introduces it.
- **`\coloneqq` for "is defined to be"**, not `=` and not `:=` typed by hand.
- **Set-builder notation uses a colon**, `\{ x \in S : P(x) \}`, not a bar, so a bar is free
  to mean divisibility, restriction or absolute value.
- **Functions:** `f \colon X \to Y` and `x \mapsto f(x)`; composition is `g \circ f`.
- **Every symbol here has a macro** in `latex/macros.tex`, so the PDF and the website agree
  and a change of mind is one edit. Nothing ad hoc in a section file.

## Numbers, sets, logic

| Type | Renders / meaning |
|---|---|
| `\nN, \nZ, \nQ, \nR, \nC` | ℕ, ℤ, ℚ, ℝ, ℂ. **ℕ = {1, 2, 3, …} does not contain 0.** |
| `\nNz` | ℕ₀ = {0, 1, 2, …}, used on Part 0's construction route (Peano's axioms start at 0) |
| `\varepsilon` | ε, always the variant (never `\epsilon`) |
| `\coloneqq` | "is defined to be" |
| `\{ x \in S : P(x) \}` | set-builder notation, with a colon |
| `S \setminus T`, `\card{S}` | difference, cardinality |
| `f \colon X \to Y`, `x \mapsto f(x)` | functions |
| `\id_X` | identity function |
| `\powerset{X}` | power set 𝒫(X) |
| `\card{S}` | cardinality |
| `\ind_{A}` | indicator function 𝟏_A of a set A |
| `\sup A`, `\inf A`, `\max`, `\min` | supremum and infimum (sup ∅ = −∞ and sup of an unbounded set = +∞ only from Part IV on, where it is announced) |
| `\abs{x}` | absolute value of a number (Ch 8, `def-absolute-value`); \( \abs{x - y} \) is the distance from \( x \) to \( y \) |
| `-A \coloneqq \{ -a : a \in A \}` | reflection of a set of numbers (Ch 8); \( \inf A = -\sup(-A) \) |
| `cA \coloneqq \{ ca : a \in A \}` | scaling of a set of numbers by \( c \in \nR \) (Ch 8) |
| `A + B \coloneqq \{ a + b : a \in A, \ b \in B \}` | sum of two sets of numbers (Ch 8); later also for subsets of a vector space |
| `\limsup_{n \to \infty} a_n`, `\liminf` | upper and lower limits |
| `\floor{x}`, `\ceil{x}` | floor and ceiling |
| `(a_n)_{n \ge 1}` or `(a_n)` | a sequence (parentheses: ordered); `\{a_n : n \in \nN\}` is its set of values |
| `(a, b)`, `[a, b]`, `(a, b]` | intervals; an ordered pair is written `(a, b)` too and context decides, stated once in Part 0 |

## The book's objects

The main characters: what letter each kind of object gets.

| Letter | Meaning |
|---|---|
| \( x, y, z, a, b \) | points or real numbers |
| \( (x_n), (a_n) \) | sequences; subsequences \( (x_{n_k}) \) |
| \( f, g, h \) | functions; \( (f_n) \) sequences of functions |
| \( A, B, S, E \) | subsets; \( K \) compact; \( U, V, W \) open; \( F \) closed |
| \( (X, d), (Y, \rho) \) | metric spaces; \( B(x, r) \) open ball, \( \overline{B}(x, r) \) closed ball |
| \( (X, \norm{\cdot}) \), \( H \) | normed spaces; Hilbert spaces |
| \( \varepsilon, \delta, r \) | small positive numbers; \( N, M \) thresholds (positive integers) |
| \( (X, \sM, \mu) \) | a measure space: σ-algebra \( \sM \), measure \( \mu \); Lebesgue measure \( m \) |
| \( z, w \); \( \Omega \) | complex numbers; an open set in ℂ or ℝⁿ |
| \( T, S \) | operators between normed spaces |

## Logic (Part 0)

| Type | Meaning |
|---|---|
| `\wedge, \vee, \to, \leftrightarrow, \neg, \bot` | and, or, implies, iff, not, contradiction (in derivations; prose says "implies", and theorems use `\Rightarrow`, `\iff`) |
| `\forall, \exists` | quantifiers |
| `\Gamma \vdash P` | P is derivable from the assumptions Γ |
| `nd` environment | a Fitch derivation: fitch.sty via `latex/fitch-book.sty` (syntax and rule macros documented there) |
| `\rulename{\wedge I}` | a rule name: ∧I, ∧E, →I, →E, ∨I, ∨E, ¬I, ¬E, ⊥E, RAA, ∀I, ∀E, ∃I, ∃E, =I, =E |

Typesetting rules for logic (learned in the Chapter 1 pilot):
- **Derivations** are fitch.sty `nd` environments in a raw LaTeX block (```` ```{=latex} ````, inside `\begin{center} $ … $ \end{center}`), never `array`s. The PDF typesets them; the website gets an SVG compiled at build time (filters/tikz.lua). `\open`/`\close` make boxes, `\hypo` an assumption or premise, `\have` a derived line; justifications are the rule macros of `latex/fitch-book.sty` (`\ai{3,2}`, `\ii{3-5}`, `\oe{1,3-5,6-8}`, `\raa{i-j}`) or `\by{text}{refs}`. A derivation cannot carry an `{#eq-…}` label: refer to it in prose ("the derivation after @def-…").
- A rule name in prose: `\( \rulename{\neg I} \)`; with a relation symbol, brace it: `\rulename{{\to}I}`. A bare Unicode ¬, ∧, → in prose stops pdflatex.
- A range of cited lines in prose: `\lines{2}{5}` (no non-ASCII inside math).
- Truth tables, and any table whose headers are formulas, are display arrays (`\begin{array}{cc|c} … \hline …`), not pipe tables.
- In a derivation a line may cite any earlier line not inside a closed box, and a result already derived may be used as one line.

## Operators and named maps

| Type | Meaning |
|---|---|
| `\diam A`, `\dist(x, A)` | diameter, distance to a set |
| `\closure{A}`, `\interior{A}`, `\boundary{A}` | closure, interior, boundary |
| `\supp f` | support |
| `\esssup` | essential supremum |
| `\osc` | oscillation |
| `Df(a)`, `f'(a)` | Fréchet derivative at a; the derivative on ℝ |
| `\pd{f}{x_i}` | partial derivative |
| `C[a,b]`, `C(K)`, `C^k`, `C_c` | continuous, k-times continuously differentiable, compactly supported functions |
| `\hat{f}(n)`, `\hat{f}(\xi)` | Fourier coefficient; Fourier transform |
| `f * g` | convolution |
| `L^p`, `\ell^p`, `\norm{f}_p` | Lebesgue spaces, sequence spaces, their norms |

## Relations

One row per relation symbol, saying what it relates and to what. A relation reused with a
second meaning is recorded here, with the reason the two uses never meet.

| Type | Meaning |
|---|---|
| | |
| | |

## Retired notation

Notation the book used and no longer uses. Keep the row: it stops a drafting agent
reintroducing it, and it explains an old label that cannot be renamed.

| Was | Now | Why |
|---|---|---|
| | | |

## Major notions

The notions that get the full eleven-step explain template (`authoring/STYLE.md` §3),
listed once so the judgement is not remade per section.

- The list in `authoring/STYLE.md` §3; add a notion here when a blueprint promotes one. 
