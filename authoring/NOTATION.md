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
| `\nN, \nZ, \nQ, \nR, \nC` | ℕ, ℤ, ℚ, ℝ, ℂ. **ℕ = {0, 1, 2, …} contains 0** (series-wide convention, math-atlas spec/06 item 1). For indices or numbers starting at 1, write \( n \ge 1 \) or \( \nZ_{>0} \); there is no separate macro for the positive integers |
| `\nNz` | **Retired.** ℕ now contains 0, so ℕ₀ is just `\nN` (Part 0's construction route and Peano's axioms included). Do not use: the macro is removed from `latex/macros.tex`, so a use fails to render |
| `\varepsilon` | ε, always the variant (never `\epsilon`) |
| `\coloneqq` | "is defined to be" |
| `\{ x \in S : P(x) \}` | set-builder notation, with a colon |
| `S \setminus T`, `\card{S}` | difference, cardinality |
| `f \colon X \to Y`, `x \mapsto f(x)` | functions |
| `\id_X` | identity function |
| `\powerset{X}` | power set 𝒫(X) |
| `x \in A`, `x \notin A` | membership. In bounds such as \( n \in \nZ_{>0} \) from Ch 1; as a predicate of an arbitrary set from Ch 4 §01 (\( \in A \) for a fixed set \( A \) is a one-place predicate symbol, Ch 4 §02); sets are developed in Ch 6 §01 |
| `\emptyset` | the empty set. Informal first use Ch 4 §01 ("The empty set", bounded quantifiers over \( \emptyset \)); defined in Ch 6 §01, `def-empty-set`: the set with no elements, unique by `prp-empty-set-unique`; \( \emptyset \subseteq A \) for every set \( A \), and \( \{\emptyset\} \ne \emptyset \) |
| `A \subseteq B`, `A \subsetneq B` | subset (equality allowed), proper subset (Ch 6 §01, `def-subset`). Used for lists of formulas from Ch 3 §05 (\( \Gamma_i \subseteq \Gamma_k \)); glossed for sets in Ch 4 §01 (every element of \( A \) is an element of \( B \)). The book never writes `\subset`, which other books use for either |
| `A \cup B`, `A \cap B`, `X \setminus A` | union, intersection, difference (Ch 6 §02, `def-set-operations`). **No `A^c`:** a complement is always written `X \setminus A` with the ambient set named, so the reader never guesses it (there is no complement without one, by `thm-russell`) |
| `(A_i)_{i \in I}`, `\bigcup_{i \in I} A_i`, `\bigcap_{i \in I} A_i`; `\bigcup \sS`, `\bigcap \sS` | a family indexed by \( I \) (parentheses: indexed); its union, and its intersection taken inside a named ambient \( X \), so the empty intersection is \( X \) (Ch 6 §02, `def-indexed-family`, `def-family-union-intersection`); \( \bigcap \sS \) only for non-empty \( \sS \subseteq \powerset{X} \) |
| `(a, b)`, `(x_1, \dots, x_n)` | ordered pair and \( n \)-tuple (Ch 6 §03, `def-ordered-pair`), known through the characteristic property \( (a, b) = (c, d) \iff a = c \wedge b = d \) and one working convention: a pair is not a number, and tuples of different lengths are different kinds of object, so a triple is not a pair (Ch 6 §03). The pair/interval double reading of `(a, b)` is stated once, in Ch 6 §03 |
| `A \times B`, `X^2`, `X^n` | Cartesian product; \( X \times X \); the set of \( n \)-tuples from \( X \) (Ch 6 §03, `def-cartesian-product`). \( X^n \) has a number as exponent; \( Y^X \) (below) has a set, and the two never clash |
| `a \mathrel{R} b`, `R^{-1}` | \( (a, b) \in R \) for a relation \( R \subseteq A \times B \); the inverse relation \( \{ (b, a) : (a, b) \in R \} \) (Ch 6 §03, `def-relation`). For the graph of a bijection \( f \), the inverse relation is the graph of the inverse function \( f^{-1} \) of Ch 6 §05 |
| `f\|_A` | restriction of \( f \colon X \to Y \) to \( A \subseteq X \), a function \( A \to Y \) (Ch 6 §04). The bar is one of the uses the colon-for-set-builder convention keeps free |
| `Y^X` | the set of all functions \( X \to Y \) (Ch 6 §04); \( \{0, 1\}^{\nN} \) in Ch 8. A function is the pair (graph, codomain), so the codomain is part of the function (Ch 6 §04, `def-function`) |
| `f(A)`, `f^{-1}(B)`, `f^{-1}` | image \( \{ f(a) : a \in A \} \subseteq Y \) and preimage \( \{ x \in X : f(x) \in B \} \subseteq X \), defined for **every** \( f \colon X \to Y \), \( A \subseteq X \), \( B \subseteq Y \) (Ch 6 §06, `def-image`, `def-preimage`); \( f(X) \) for the range of \( f \) is first used in Ch 6 §05, before `thm-left-inverse-iff-injective`; in \( f^{-1}(B) \) the whole expression names a set, and \( f^{-1} \) is not applied to \( B \). Whether \( f(\cdot) \) is a value or an image is decided by the declared argument, a point or a subset. The inverse function \( f^{-1} \colon Y \to X \) exists only for a bijection (Ch 6 §05, `def-inverse-function`). Where the two uses meet: for a bijection, \( f^{-1}(B) \) read as a preimage under \( f \) and read as the image of \( B \) under \( f^{-1} \) are the same set (Ch 6 §06, the remark "Two readings of the inverse symbol", proved there), so the notation is never ambiguous |
| `\card{S}` | cardinality |
| `\ind_{A}` | indicator function 𝟏_A of a set A |
| `\sup A`, `\inf A`, `\max`, `\min` | supremum and infimum (sup ∅ = −∞ and sup of an unbounded set = +∞ only from Part IV on, where it is announced) |
| `\abs{x}` | absolute value of a number: defined by cases in Ch 1 (first in §01 C2, displayed in §07; school algebra), formally in Ch 11 (`def-absolute-value`); \( \abs{x - y} \) is the distance from \( x \) to \( y \) |
| `d \mid n` | d divides n: n = dk for some integer k (first used Ch 2 §04, C1) |
| `-A \coloneqq \{ -a : a \in A \}` | reflection of a set of numbers (first defined Ch 6 §06, as an image: `exm-sets-of-numbers-as-images`; used from Ch 11); \( \inf A = -\sup(-A) \) |
| `cA \coloneqq \{ ca : a \in A \}` | scaling of a set of numbers by \( c \in \nR \) (first defined Ch 6 §06, as an image: `exm-sets-of-numbers-as-images`; used from Ch 11) |
| `A + B \coloneqq \{ a + b : a \in A, \ b \in B \}` | sum of two sets of numbers (first defined Ch 6 §06, as the image of \( A \times B \): `exm-sets-of-numbers-as-images`; used from Ch 11); later also for subsets of a vector space |
| `U(A)` | the set of all upper bounds of \( A \) in the ambient ordered field (Ch 11, local to exercises: §02 C2 in \( F \), §03 C2 in \( \nR \); restated where used). Always written with its argument, so it does not clash with \( U \) for an open set |
| `\sqrt[n]{a}`, `a^{1/n}` | for \( a > 0 \) and an integer \( n \ge 1 \), the unique \( s > 0 \) with \( s^n = a \) (Ch 11 `thm-nth-root`); `\sqrt{a}` is \( n = 2 \). In Chapters 1–10, \( \sqrt{a} \) for \( a \ge 0 \) is a school fact. \( \sqrt[n]{0} = 0 \) (Ch 11 §06). For **odd** \( n \) and \( a < 0 \), \( \sqrt[n]{a} \coloneqq -\sqrt[n]{-a} \), the unique real \( s \) with \( s^n = a \) (first used Ch 6 §04, §05 for the real cube root of every real number, a school fact there; Ch 11's `thm-nth-root` with a sign change). `a^{m/n} \coloneqq (a^{1/n})^m` for \( a > 0 \) (Ch 11 §06); \( a^x \) for irrational \( x \) from Ch 20 |
| `\nR(x)` | the field of rational functions \( p/q \) with real coefficients in one indeterminate \( x \), ordered by the signs of the leading coefficients (Ch 11 §05, `exm-nonarchimedean-field`): the book's non-Archimedean ordered field. Here \( x \) is the indeterminate, not a real number |
| `\limsup_{n \to \infty} a_n`, `\liminf` | upper and lower limits |
| `\floor{x}`, `\ceil{x}` | floor and ceiling |
| `(a_n)_{n \ge 1}` or `(a_n)` | a sequence (parentheses: ordered); `\{a_n : n \ge 1\}` is its set of values |
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
| \( \varepsilon, \delta, r \) | small positive numbers; \( N, M \) thresholds (natural numbers: written \( \exists N \in \nN \), unless the formula needs \( N \ge 1 \), e.g. with \( 1/N \) or \( 1/n \), when \( \nZ_{>0} \) is used) |
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
| `nd` environment | a Fitch derivation: fitch.sty via `latex/fitch-book.sty` (syntax and rule macros documented there). Quantifier and equality rule tags (Ch 4): `\Ae`, `\Ai`, `\Ei`, `\Ee`, `\eqi`, `\eqe` (∀E, ∀I, ∃I, ∃E, =I, =E); the bounded rules of Ch 4 §08 reuse them; an arithmetic fact is `\by{arith}{…}`. A flagged box is `\open[x_0]`. A proved sequent used as one line has a short tag: VI (`prp-vacuous-implication`, Ch 2 §06, Ch 4 §04, §09), QN (`prp-quantifier-negation`, written with its part, `\by{QN (a)}{…}`, `\by{QN (b)}{…}`; Ch 4 §09), NIm (`prp-negated-implication`, Ch 4 §09) |
| `\rulename{\wedge I}` | a rule name: ∧I, ∧E, →I, →E, ∨I, ∨E, ¬I, ¬E, ⊥E, RAA, ↔I, ↔E, R, ∀I, ∀E, ∃I, ∃E, =I, =E; derived: ¬¬I, ¬¬E, MT, CP, DS, DM, LEM; plus R (repetition, (D3) of `def-derivation`) |
| `p, q, r, p_1, p_2, \dots` | atoms (propositional letters), symbols of the formal language (Ch 3 §01, `def-formula`); each atom is one symbol. From Ch 3 on, \( \varphi, \psi, \chi \) are metavariables for **formulas** and never occur in them; the capitals \( P, Q, R \) of Ch 1–2 were placeholders, read in Ch 3 as atoms or as arbitrary formulas (Ch 3 §01, "Letters, metavariables and substitution"). From Ch 4 §02 on, \( p, q \) are also **object variables** ("for primes and other natural numbers", Ch 4 §01); the two uses never meet, because a first-order formula has no propositional atoms (atomic formulas replace them, Ch 4 §02 (Fm1)); in Ch 4, \( p, q, r \) are atoms in §01's opening argument (written in Ch 3's language) and wherever a later section reads a formula with a truth table (Ch 4 §11, R1 and R4); inside a first-order formula they are variables |
| `\circ` | in the logic chapters (Ch 3–5): a metavariable for a binary connective, \( (\varphi \circ \psi) \) any of \( (\varphi \wedge \psi), (\varphi \vee \psi), (\varphi \to \psi), (\varphi \leftrightarrow \psi) \). From Ch 6 on (still Part 0; Ch 6 §04, `def-composition`), \( g \circ f \) is composition of functions. The two never meet: Ch 1–5 compose no functions, and from Ch 6 on no connective metavariable \( \circ \) is used |
| `\Gamma, \Delta` | finite lists of formulas (premises), as in `def-derivable` |
| `\hgt(\varphi)` | height of a formula, printed \( \operatorname{ht}(\varphi) \): nodes on a longest branch of its parse tree (Ch 3 §01 `def-height`; recursive form Ch 3 §02). Not `\height`, which the PDF preamble already defines as a length |
| `\atoms(\varphi)` | the set of atoms occurring in a formula (Ch 3 §02, `exm-recursive-definitions`) |
| `\operatorname{len}(\varphi)` | length of a formula: its number of symbols (Ch 3 §02) |
| `\operatorname{ex}(s)` | excess of a string: number of left minus number of right parentheses (local to Ch 3 §02, `lem-parenthesis-count`) |
| `\operatorname{nodes}(\varphi)`, `\operatorname{neg}(\varphi)` | number of nodes of the parse tree; number of occurrences of \( \neg \) (local to Ch 3 §02 exercises B3, C3) |
| `P(n)`, `P(\varphi)` | a property of natural numbers / of formulas, in induction principles (Ch 3 §02); the statement letter \( P \) of Ch 1–2 never takes an argument |
| `\mathrm{T}, \mathrm{F}` | the truth values true and false (Ch 3 §03). No macro: `\T` is the bold one-letter macro. In truth tables, rows are listed T before F, the last atom alternating fastest |
| `v, w` ; `v(\varphi)` | valuations (Ch 3 §03 `def-valuation`); the truth value of a formula under \( v \) (`def-truth-value`, clauses (V1)–(V6)) |
| `\Gamma \models \psi`, `\models \psi`, `\Gamma \not\models \psi` | semantic entailment: every valuation making all of Γ true makes ψ true (Ch 3 §04 `def-valid-argument`); a valuation making Γ true and ψ false is a *refuting row*. Not a formula: never nested inside one. **For first-order formulas (Ch 4 §11 on, `def-first-order-entailment`):** every structure and every assignment satisfying all of Γ satisfy ψ; a structure with an assignment satisfying Γ and not ψ is a *counter-model*, which plays the refuting row's part. The two readings never clash: the kind of formula decides which applies (valuations for Ch 3's formulas with atoms, structures and assignments for first-order formulas) |
| `\Gamma \nvdash \psi` | ψ is not derivable from Γ (Ch 3 §05, `cor-refuting-row`) |
| `\varphi \equiv \psi` | semantic equivalence of formulas: φ ⊨ ψ and ψ ⊨ φ (Ch 3 §04 `def-semantic-equivalence`). Ch 7 uses \( a \equiv b \pmod n \) for congruence; the two never meet (the congruence always carries its modulus) |
| `\sigma(\chi)`, `\sigma(\Gamma)` | the result of a substitution σ of formulas for atoms, applied to a formula or to each formula of a list (Ch 3 §04, before `lem-substitution`) |
| `\Gamma_k`, `\varphi_k`; `\Delta \subseteq \Delta'` | the context of line k of a derivation (Ch 1 `def-derivation`) and the formula on line k (Ch 3 §05); for lists, every formula of Δ occurs in Δ' (Ch 3 §05, before `lem-context-inclusion`) |
| `u`, `\models_3` | a three-valued valuation (values 0 < ½ < 1) and its entailment (local to Ch 3 §05, the optional `thm-raa-independent`) |
| `v_{\mathrm{T}}` | the all-T valuation: every atom true (local to Ch 3 §03 C2, §07 `thm-adequate-connectives` (b) and C2 (a)); not \( u \), which is three-valued |
| `\varphi^{v}`, `p^{v}` | the formula signed by a valuation: φ if v(φ) = T, ¬φ if v(φ) = F (Ch 3 §06, before `lem-truth-table-line`; the literals of §07 rows) |
| `\mathbin{\vert}`, `\downarrow`, `\mathsf{M}` | NAND ("not both"; the source writes `\mathbin{|}`, which a pipe table cannot show), NOR ("neither"), and the three-place majority connective (local to Ch 3 §04 C1 and §07 exercises C1, C2) |
| `\mathrm{occ}(\varphi)`, `\mathrm{bin}(\varphi)` | number of atom occurrences; number of binary connectives (local to Ch 3 §03 exercise B2) |
| `P(x)`, `R(x, y)`, `\mathrm{Prime}(p)`; `<`, `\le`, `=`, `\in A` | predicate symbols with their holes (Ch 4 §01; symbols of the first-order language, each with an arity \( n \ge 1 \), Ch 4 §02). With parentheses \( P, Q, R, S \) are predicate symbols; a bare \( P, Q, R \) is still a statement letter of Ch 1–3 (Ch 4 §01, "A clash of letters"). `\mathrm{Prime}` is typed directly (no macro yet) |
| `x, y, z, u`; `x_0, y_0, \varepsilon_0, \delta_0` | variables of a first-order language (Ch 4 §02, with \( \varepsilon, \delta, N, n, k, L \) and \( p, q \) in analysis); in a derivation, a subscript 0 marks a **fresh name** of a flagged box (\( \rulename{\forall I} \), \( \rulename{\exists E} \), Ch 4 §§04, 06), always a variable, never a constant; elsewhere \( x_0 \) is an ordinary name |
| `\forall x \in A \; \varphi`, `\exists x \in A \; \varphi`, `\forall \varepsilon > 0 \; \varphi` | bounded quantifiers: abbreviations of \( \forall x\, (x \in A \to \varphi) \), \( \exists x\, (x \in A \wedge \varphi) \), and likewise with \( >, \ge, <, \le \) (Ch 4 §01, `def-bounded-quantifier`); \( \exists! \, y \in Y \; \psi \) abbreviates \( \exists! \, y \, (y \in Y \wedge \psi) \) (first used Ch 6 §04, `def-function`); not symbols of the language. Their derived rules: Ch 4 §08, `prp-bounded-quantifier-rules` |
| `\varphi[t/x]`, `s[t/x]` | substitution of the term \( t \) for the **free** occurrences of the variable \( x \) in a formula, or for every occurrence in a term; read "\( \varphi \) with \( t \) for \( x \)" (Ch 4 §02, `def-substitution`). No macro: typed directly; the slash is a separator, not division. A different operation from Ch 3's \( \sigma(\chi) \), which puts formulas in for atoms. "\( x \) **appears in** \( \varphi \)" (written anywhere, after a quantifier symbol included) is wider than "an occurrence of \( x \)" (inside a term); freshness conditions use "appears" (Ch 4 §02, after `def-free-variable`) |
| `\mathrm{Var}(t)`, `\mathrm{FV}(\varphi)` | the set of variables of a term; the set of free variables of a formula (local to Ch 4 §02 exercises B2 and C1 and their solutions) |
| `\exists! x\, \varphi` | there is exactly one \( x \) with \( \varphi \); shorthand for \( \exists x\, (\varphi \wedge \forall y\, (\varphi[y/x] \to y = x)) \), \( y \) not appearing in \( \varphi \); not a symbol of the language (Ch 4 §07, `def-unique-existence`) |
| `\fM`; `D`; `c^{\fM}`, `f^{\fM}`, `R^{\fM}`; `\fM_{\nN}` | a structure (model) of predicate logic, printed \( \mathfrak{M} \), with domain \( D \) and the interpretations of a constant, a function symbol and a predicate symbol (Ch 4 §11, `def-structure`); a subscript names the domain of a standard structure, and \( \fM_1, \fM_2 \) are structures numbered within an example. Not `\sM`, which is the σ-algebra of Part IV (one symbol, one meaning) |
| `\ell`, `\ell(x)`, `\ell[x \mapsto d]` | an assignment of elements of \( D \) to the variables; the assignment that changes only the value at \( x \) to \( d \) (Ch 4 §11, `def-assignment`). Unrelated to the \( \ell \) of the sequence spaces \( \ell^p \) (Operators table); the two never meet, since \( \ell^p \) always carries its exponent and the assignment never leaves Part 0 |
| `t^{\fM, \ell}` | the value in \( D \) of a term \( t \) under the assignment \( \ell \) (Ch 4 §11, "Assignments and the value of a term") |
| `\fM, \ell \models \varphi`, `\fM, \ell \not\models \varphi`, `\fM, \ell \models \Gamma`; `\fM \models \varphi` | satisfaction: \( \fM \) satisfies \( \varphi \) under \( \ell \), clauses (S1)–(S7) (Ch 4 §11, `def-satisfaction`); for a list, every formula of \( \Gamma \). For a sentence, \( \fM \models \varphi \), "\( \varphi \) is true in \( \fM \)", since the assignment does not matter (Ch 4 §11, after `lem-free-coincidence`) |

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
