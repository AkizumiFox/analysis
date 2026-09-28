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
| `\abs{x}` | absolute value of a number: defined by cases in Ch 1 (first in §01 C2, displayed in §07; school algebra), formally in Ch 11 (`def-absolute-value`); \( \abs{x - y} \) is the distance from \( x \) to \( y \) |
| `d \mid n` | d divides n: n = dk for some integer k (first used Ch 2 §04, C1) |
| `-A \coloneqq \{ -a : a \in A \}` | reflection of a set of numbers (Ch 11); \( \inf A = -\sup(-A) \) |
| `cA \coloneqq \{ ca : a \in A \}` | scaling of a set of numbers by \( c \in \nR \) (Ch 11) |
| `A + B \coloneqq \{ a + b : a \in A, \ b \in B \}` | sum of two sets of numbers (Ch 11); later also for subsets of a vector space |
| `U(A)` | the set of all upper bounds of \( A \) in the ambient ordered field (Ch 11, local to exercises: §02 C2 in \( F \), §03 C2 in \( \nR \); restated where used). Always written with its argument, so it does not clash with \( U \) for an open set |
| `\sqrt[n]{a}`, `a^{1/n}` | for \( a > 0 \) and \( n \in \nN \), the unique \( s > 0 \) with \( s^n = a \) (Ch 11 `thm-nth-root`); `\sqrt{a}` is \( n = 2 \). In Chapters 1–10, \( \sqrt{a} \) for \( a \ge 0 \) is a school fact. `a^{m/n} \coloneqq (a^{1/n})^m` for \( a > 0 \) (Ch 11 §06); \( a^x \) for irrational \( x \) from Ch 20 |
| `\nR(x)` | the field of rational functions \( p/q \) with real coefficients in one indeterminate \( x \), ordered by the signs of the leading coefficients (Ch 11 §05, `exm-nonarchimedean-field`): the book's non-Archimedean ordered field. Here \( x \) is the indeterminate, not a real number |
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
| `\varphi, \psi, \chi` | metavariables standing for any statements, in rule schemas and in general claims about derivations (introduced in Ch 1 §02 after `def-rule-schema`, used from Ch 1 §03); P, Q, R are statement letters |
| `P \dashv\vdash Q` | P and Q are provably equivalent: P ⊢ Q and Q ⊢ P (Ch 2 §04, `def-provable-equivalence`) |
| `\mathsf{X}`, `\mathsf{Y}` | a variable standing for a rule, in statements about rules (Ch 2 §05, "X derives Y" before `thm-classical-rules-interderivable`) |
| `nd` environment | a Fitch derivation: fitch.sty via `latex/fitch-book.sty` (syntax and rule macros documented there) |
| `\rulename{\wedge I}` | a rule name: ∧I, ∧E, →I, →E, ∨I, ∨E, ¬I, ¬E, ⊥E, RAA, ↔I, ↔E, R, ∀I, ∀E, ∃I, ∃E, =I, =E; derived: ¬¬I, ¬¬E, MT, CP, DS, DM, LEM; plus R (repetition, (D3) of `def-derivation`) |
| `p, q, r, p_1, p_2, \dots` | atoms (propositional letters), symbols of the formal language (Ch 3 §01, `def-formula`); each atom is one symbol. From Ch 3 on, \( \varphi, \psi, \chi \) are metavariables for **formulas** and never occur in them; the capitals \( P, Q, R \) of Ch 1–2 were placeholders, read in Ch 3 as atoms or as arbitrary formulas (Ch 3 §01, "Letters, metavariables and substitution") |
| `\circ` | in Part 0 (Ch 3 on): a metavariable for a binary connective, \( (\varphi \circ \psi) \) any of \( (\varphi \wedge \psi), (\varphi \vee \psi), (\varphi \to \psi), (\varphi \leftrightarrow \psi) \). Later Parts use \( g \circ f \) for composition; the two never meet (the logic chapters compose no functions) |
| `\Gamma, \Delta` | finite lists of formulas (premises), as in `def-derivable` |
| `\hgt(\varphi)` | height of a formula, printed \( \operatorname{ht}(\varphi) \): nodes on a longest branch of its parse tree (Ch 3 §01 `def-height`; recursive form Ch 3 §02). Not `\height`, which the PDF preamble already defines as a length |
| `\atoms(\varphi)` | the set of atoms occurring in a formula (Ch 3 §02, `exm-recursive-definitions`) |
| `\operatorname{len}(\varphi)` | length of a formula: its number of symbols (Ch 3 §02) |
| `\operatorname{ex}(s)` | excess of a string: number of left minus number of right parentheses (local to Ch 3 §02, `lem-parenthesis-count`) |
| `\operatorname{nodes}(\varphi)`, `\operatorname{neg}(\varphi)` | number of nodes of the parse tree; number of occurrences of \( \neg \) (local to Ch 3 §02 exercises B3, C3) |
| `P(n)`, `P(\varphi)` | a property of natural numbers / of formulas, in induction principles (Ch 3 §02); the statement letter \( P \) of Ch 1–2 never takes an argument |
| `\mathrm{T}, \mathrm{F}` | the truth values true and false (Ch 3 §03). No macro: `\T` is the bold one-letter macro. In truth tables, rows are listed T before F, the last atom alternating fastest |
| `v, w` ; `v(\varphi)` | valuations (Ch 3 §03 `def-valuation`); the truth value of a formula under \( v \) (`def-truth-value`, clauses (V1)–(V6)) |
| `\Gamma \models \psi`, `\models \psi`, `\Gamma \not\models \psi` | semantic entailment: every valuation making all of Γ true makes ψ true (Ch 3 §04 `def-valid-argument`); a valuation making Γ true and ψ false is a *refuting row*. Not a formula: never nested inside one |
| `\Gamma \nvdash \psi` | ψ is not derivable from Γ (Ch 3 §05, `cor-refuting-row`) |
| `\varphi \equiv \psi` | semantic equivalence of formulas: φ ⊨ ψ and ψ ⊨ φ (Ch 3 §04 `def-semantic-equivalence`). Ch 7 uses \( a \equiv b \pmod n \) for congruence; the two never meet (the congruence always carries its modulus) |
| `\sigma(\chi)`, `\sigma(\Gamma)` | the result of a substitution σ of formulas for atoms, applied to a formula or to each formula of a list (Ch 3 §04, before `lem-substitution`) |
| `\Gamma_k`, `\varphi_k`; `\Delta \subseteq \Delta'` | the context of line k of a derivation (Ch 1 `def-derivation`) and the formula on line k (Ch 3 §05); for lists, every formula of Δ occurs in Δ' (Ch 3 §05, before `lem-context-inclusion`) |
| `u`, `\models_3` | a three-valued valuation (values 0 < ½ < 1) and its entailment (local to Ch 3 §05, the optional `thm-raa-independent`) |
| `v_{\mathrm{T}}` | the all-T valuation: every atom true (local to Ch 3 §03 C2, §07 `thm-adequate-connectives` (b) and C2 (a)); not \( u \), which is three-valued |
| `\varphi^{v}`, `p^{v}` | the formula signed by a valuation: φ if v(φ) = T, ¬φ if v(φ) = F (Ch 3 §06, before `lem-connective-rows`; the literals of §07 rows) |
| `\mathbin{\vert}`, `\downarrow`, `\mathsf{M}` | NAND ("not both"; the source writes `\mathbin{|}`, which a pipe table cannot show), NOR ("neither"), and the three-place majority connective (local to Ch 3 §04 C1 and §07 exercises C1, C2) |
| `\mathrm{occ}(\varphi)`, `\mathrm{bin}(\varphi)` | number of atom occurrences; number of binary connectives (local to Ch 3 §03 exercise B2) |

Typesetting rules for logic (learned in the Chapter 1 pilot):
- **Derivations** are fitch.sty `nd` environments in a raw LaTeX block (```` ```{=latex} ````, inside `\begin{center} $ … $ \end{center}`), never `array`s. The PDF typesets them; the website gets an SVG compiled at build time (filters/tikz.lua). `\open`/`\close` make boxes, `\begin{nd}[schema]` prints each line's own label (i, j, k) instead of a number for a rule pattern, `\hypo` an assumption or premise, `\have` a derived line; justifications are the rule macros of `latex/fitch-book.sty` (`\ai{3,2}`, `\ii{3-5}`, `\oe{1,3-5,6-8}`, `\raa{i-j}`) or `\by{text}{refs}`. A derivation cannot carry an `{#eq-…}` label: refer to it in prose ("the derivation after @def-…").
- A rule name in prose: `\( \rulename{\neg I} \)`; with a relation symbol, brace it: `\rulename{{\to}I}`. A bare Unicode ¬, ∧, → in prose stops pdflatex.
- A range of cited lines in prose: `\lines{2}{5}` (no non-ASCII inside math).
- Truth tables, and any table whose headers are formulas, are display arrays (`\begin{array}{cc|c} … \hline …`), not pipe tables.
- Citing lines follows `def-derivation` (Chapter 1, Section 1.5). A line may cite any **available** line: an earlier line such that every box containing it also contains the citing line (that is, not inside a box that has already closed). A closed box, cited as a whole, must sit directly in the part of the derivation where the citing line is.
- **Repetition** is clause (D3) of `def-derivation`, typeset `\r{i}` ("R i"): it copies an available line into the current box. Most rules may cite the available line directly, so R is needed only when a rule wants the statement as a line **of a particular box** — \( \rulename{{\to}I} \), \( \rulename{\neg I} \), \( \rulename{\vee E} \), \( \rulename{{\leftrightarrow}I} \) and RAA require the box's conclusion as a line of that box itself, not inside a further box (e.g. \( \vdash P \to (Q \to P) \) repeats \( P \) inside the box of \( Q \)).
- A result already derived may be used as one line (a derived rule), citing the result; this abbreviates pasting in its derivation with premises replaced by repetitions.

## Operators and named maps

| Type | Meaning |
|---|---|
| `\diam A`, `\dist(x, A)` | diameter, distance to a set |
| `\closure{A}`, `\interior{A}`, `\boundary{A}` | closure, interior, boundary |
| `\supp f` | support |
| `\esssup` | essential supremum |
| `\osc` | oscillation |
| `\operatorname{lc}(p)`, `\deg p` | leading coefficient and degree of a non-zero polynomial \( p \) (Ch 11 §05 C2 and §07 C3 solutions, defined where used); \( \operatorname{lc}(pq) = \operatorname{lc}(p)\operatorname{lc}(q) \) |
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
