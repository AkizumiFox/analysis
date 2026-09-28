# The Archimedean Property

We now have the least upper bound axiom (@ax-least-upper-bound) and a way to use it, the characterization of the supremum by \( \varepsilon \) (@thm-sup-epsilon). This section draws the first consequence, one that looks too obvious to need proof: the natural numbers eventually pass every real number. When we first met suprema, we claimed that \( \sup \{ 1 - 1/n : n \in \nN \} = 1 \) and postponed the proof, because it needs exactly this fact. Here we prove the fact from the axiom, pay off that claim, and then meet an ordered field where the fact is false, so that we can see which line of the proof the axiom is holding up.

## Where the natural numbers live

So far \( \nR \) is an ordered field satisfying one extra axiom. The numbers \( 1, 2, 3, \dots \) are in it, since \( 2 \) is \( 1 + 1 \), \( 3 \) is \( 2 + 1 \), and so on. But "and so on" is not a definition. We want the set you get by starting at \( 1 \) and adding \( 1 \) again and again, and nothing else. The first half of that description is easy to state as a property of a set.

::: {#def-inductive-set}
[Inductive set]

A subset \( S \subseteq \nR \) is **inductive** if

::: {.enumerate options="label=(N\arabic*)"}
1. \( 1 \in S \), and
2. **for every** \( x \in S \), also \( x + 1 \in S \).
:::
:::

In words: an inductive set contains \( 1 \), and it is closed under the step "add one". Nothing stops it from containing other numbers as well.

Some examples, checked clause by clause.

- \( \nR \) itself is inductive: it contains \( 1 \), and \( x + 1 \) is a real number whenever \( x \) is.
- \( [1, \infty) = \{ x \in \nR : x \ge 1 \} \) is inductive: \( 1 \ge 1 \), and \( x \ge 1 \) gives \( x + 1 \ge 1 + 1 > 1 \).
- \( \{ 1 \} \cup [2, \infty) \) is inductive. From \( 1 \) we step to \( 2 \), which is in \( [2, \infty) \), and \( [2, \infty) \) is closed under adding \( 1 \).

A non-example by minimal change: \( [1, 5] \) contains \( 1 \), so (N1) holds, but \( 4.5 \in [1, 5] \) and \( 5.5 \notin [1, 5] \), so (N2) fails. Chopping the top off \( [1, \infty) \) destroys closure under the step.

The inductive sets above are too big: \( [1, \infty) \) contains \( 1.5 \) and \( 4.7 \). What we want is the *smallest* one. Intersecting all of them throws away everything that some inductive set can do without.

The set of **natural numbers** is
\[
    \nN \coloneqq \{ x \in \nR : x \in S \text{ for every inductive set } S \subseteq \nR \},
\]
that is, the real numbers that belong to every inductive subset of \( \nR \).

Two things are true of \( \nN \), and both follow at once from the definition.

- \( \nN \) **is inductive.** Every inductive set contains \( 1 \), so \( 1 \in \nN \). If \( x \in \nN \), then \( x \) lies in every inductive set \( S \), and each such \( S \) then contains \( x + 1 \) by (N2); so \( x + 1 \in \nN \).
- \( \nN \) **is contained in every inductive set**, since it is their intersection.

The second property is the **principle of induction** in disguise. To prove that a statement \( P(n) \) holds for every \( n \in \nN \), let \( S \coloneqq \{ n \in \nN : P(n) \} \). If \( P(1) \) holds and \( P(n) \) implies \( P(n + 1) \), then \( S \) is inductive, so \( \nN \subseteq S \), and \( P(n) \) holds for all \( n \in \nN \).

::: {#exm-naturals-at-least-one}
[Every natural number is at least 1]

Show that \( n \ge 1 \) for every \( n \in \nN \), and deduce that \( 1/n \) is defined and \( 0 < 1/n \le 1 \).
:::

::: {.solution}
The set \( [1, \infty) \) is inductive, as checked above. Since \( \nN \) is contained in every inductive set, \( \nN \subseteq [1, \infty) \), that is, \( n \ge 1 \) for every \( n \in \nN \). In particular \( n > 0 \), so \( n \ne 0 \) and \( 1/n \) is defined. From \( 0 < 1 \le n \) @thm-ordered-field-rules (f) gives \( 0 < 1/n \le 1/1 = 1 \).
:::

The proof never mentioned a single natural number by name. It found an inductive set containing the property we wanted, and let the definition of \( \nN \) do the rest. That is the whole technique.

::: {.remark}
Chapter 6 takes \( \nN \) with induction and well-ordering as its starting point. The set defined here is that same \( \nN \), now located inside \( \nR \); it is also the copy \( 1, 1 + 1, 1 + 1 + 1, \dots \) that every ordered field contains (@exr-ordered-fields-c1), and "\( \nN \) is the smallest inductive set" is exactly the induction principle stated there. From now on we use the familiar arithmetic of \( \nN \), each item proved by induction in Chapter 6: sums and products of natural numbers are natural numbers; if \( n \in \nN \) and \( n \ge 2 \), then \( n - 1 \in \nN \); no natural number lies strictly between \( n \) and \( n + 1 \); and every non-empty subset of \( \nN \) has a least element (**well-ordering**). The integers are \( \nZ \coloneqq \nN \cup \{ 0 \} \cup \{ -n : n \in \nN \} \), and the rationals are \( \nQ \coloneqq \{ m/n : m \in \nZ, \ n \in \nN \} \). We also use, again from Chapter 6, that sums, differences and products of integers are integers. A **positive** integer is a natural number, directly from the definition of \( \nZ \): it is not \( 0 \), and it is not \( -n \) with \( n \in \nN \), since \( -n < 0 \).
:::

## The natural numbers are not bounded

Is \( \nN \) bounded above in \( \nR \)? Everyone's picture of the number line says no: the marks \( 1, 2, 3, \dots \) march off to the right forever. But a picture is not a proof, and here the picture hides something. Nothing in the ordered-field axioms (@def-ordered-field) forbids a number larger than every natural number. At the end of this section we build an ordered field that contains one. So if \( \nR \) has no such number, the reason must be the one axiom that \( \nR \) has and that field lacks.

::: {#thm-naturals-unbounded}
[Archimedean Property]

The set \( \nN \) is not bounded above in \( \nR \); in other words, every real number \( x \) is exceeded by some \( n \in \nN \).
:::

::: {.idea}
Suppose \( \nN \) had an upper bound. Then the axiom hands us the least one, \( s = \sup \nN \), and we can use the "least" half of the supremum (the move of @thm-sup-epsilon with \( \varepsilon = 1 \)). The number \( s - 1 \) is too small to be an upper bound, so some natural number \( n \) sits above it. One more step, \( n + 1 \), is still a natural number, and it jumps past \( s \). A supremum that a natural number can overtake is absurd.
:::

::: {.proof}
Suppose, for contradiction, that \( \nN \) is bounded above. The set \( \nN \) is non-empty, since \( 1 \in \nN \). By @ax-least-upper-bound, \( \nN \) has a supremum \( s \coloneqq \sup \nN \in \nR \).

The number \( s - 1 \) is not an upper bound of \( \nN \): if it were, property (S2) of the supremum (@def-supremum) would give \( s \le s - 1 \), which is false. Hence there is \( n \in \nN \) with \( n > s - 1 \). Then \( n + 1 > s \). But \( \nN \) is inductive, so \( n + 1 \in \nN \), and \( s \) is an upper bound of \( \nN \), so \( n + 1 \le s \). This contradicts \( n + 1 > s \).

Therefore \( \nN \) is not bounded above. Unwinding the definition (@def-bounded-above), no \( x \in \nR \) is an upper bound of \( \nN \): for every \( x \in \nR \) it is false that \( n \le x \) for all \( n \in \nN \). So for every \( x \) some \( n \in \nN \) has \( n \not\le x \), that is, \( n > x \) by trichotomy. This proves the theorem.
:::

Each hypothesis of the axiom was used and named: "non-empty" through \( 1 \in \nN \), "bounded above" through the assumption for contradiction. The inductive property of \( \nN \) supplied the jump \( n \mapsto n + 1 \).

::: {.remark}
The contradiction step is \( \rulename{\neg I} \) (@def-rules-negation), not \( \rulename{RAA} \) (@def-rule-raa), the classical rule of proof by contradiction: we assumed "\( \nN \) is bounded above", reached a contradiction, and concluded its negation. The proof does contain a classical step, but it comes after the \( \rulename{\neg I} \), in the proof's last paragraph. Passing from "not every \( n \) satisfies \( n \le x \)" to "some \( n \) satisfies \( n > x \)" is the quantifier law "not all" gives "some not" of Chapter 3, and that law is derived there with \( \rulename{RAA} \).
:::

The form we will use most often puts a small number, not a large one, in the role of \( x \).

::: {#cor-archimedean-epsilon}
For every \( \varepsilon > 0 \) there is \( n \in \nN \) with \( 1/n < \varepsilon \). In symbols,
\[
    (\forall \varepsilon > 0)\ (\exists n \in \nN) \quad \frac{1}{n} < \varepsilon .
\]
Moreover, every \( m \in \nN \) with \( m \ge n \) then also satisfies \( 1/m < \varepsilon \).
:::

::: {.proof}
Let \( \varepsilon > 0 \). Then \( 1/\varepsilon \) is defined and positive. By @thm-naturals-unbounded applied to \( x = 1/\varepsilon \), there is \( n \in \nN \) with \( n > 1/\varepsilon > 0 \). Taking reciprocals reverses a strict inequality between positive numbers (@thm-ordered-field-rules (f)), so \( 1/n < \varepsilon \). If \( m \ge n \), then \( 1/m \le 1/n < \varepsilon \) by the same rule.
:::

Read the quantifiers in order. The \( \varepsilon \) is given first and the \( n \) is found afterwards, so **\( n \) depends on \( \varepsilon \)**: the proof chose \( n > 1/\varepsilon \), and a smaller \( \varepsilon \) forces a larger \( n \). Swapping the quantifiers gives a false statement. "There is \( n \in \nN \) such that \( 1/n < \varepsilon \) for every \( \varepsilon > 0 \)" would make \( 1/n \) smaller than every positive number. Since \( 1/n > 0 \) (@exm-naturals-at-least-one), we could take \( \varepsilon = 1/n \) itself and get \( 1/n < 1/n \), which is absurd.

The "moreover" clause says that once one \( n \) works, every later one works too. Chapter 11 turns this "from some point on" into the definition of a limit.

::: {.check}
Find the least \( n \in \nN \) with \( 1/n < 0.003 \). Then do the same for \( \varepsilon = 0.0003 \). What does the comparison say about the dependence of \( n \) on \( \varepsilon \)?
:::

::: {.solution}
For positive \( n \), \( 1/n < 0.003 \) is equivalent to \( n > 1/0.003 = 333.\overline{3} \). The least natural number with this property is \( n = 334 \); indeed \( 1/333 = 0.003003\ldots \) is too big. For \( \varepsilon = 0.0003 \) the condition is \( n > 3333.\overline{3} \), so the least \( n \) is \( 3334 \). Dividing \( \varepsilon \) by \( 10 \) multiplied the least \( n \) by about \( 10 \). No single \( n \) serves every \( \varepsilon \), which is why the quantifiers read "for every \( \varepsilon \) there is \( n \)" and not the other way round.
:::

## Paying an old debt

In @exm-sup-one-minus-reciprocal we showed that \( 1 \) is an upper bound of \( A = \{ 1 - 1/n : n \in \nN \} \) and that \( A \) has no maximum. We stopped short of \( \sup A = 1 \), because (S2) needed an \( n \) with \( 1/n \) below a given positive number. That is exactly what @cor-archimedean-epsilon supplies, and the \( \varepsilon \)-characterization tells us what remains to be shown.

::: {#exm-sup-one-minus-reciprocal-finished}
[The supremum is 1]

Let \( A \coloneqq \{ 1 - 1/n : n \in \nN \} \). Prove that \( \sup A = 1 \).
:::

::: {.solution}
The set \( A \) is non-empty, since \( 0 = 1 - 1/1 \in A \).

*Upper bound.* For every \( n \in \nN \) we have \( 1/n > 0 \) (@exm-naturals-at-least-one), so \( 1 - 1/n < 1 \). Hence \( 1 \) is an upper bound of \( A \).

*An element in every band below \( 1 \).* Let \( \varepsilon > 0 \). By @cor-archimedean-epsilon there is \( n \in \nN \) with \( 1/n < \varepsilon \); this \( n \) depends on \( \varepsilon \). Then \( a \coloneqq 1 - 1/n \in A \) and \( a > 1 - \varepsilon \).

Since \( 1 \) is an upper bound of \( A \) and every band \( (1 - \varepsilon, 1] \) contains an element of \( A \), @thm-sup-epsilon gives \( \sup A = 1 \).

For a concrete instance, \( \varepsilon = 0.01 \) needs \( n > 100 \), and \( n = 101 \) gives the element \( 1 - 1/101 = 100/101 > 0.99 \). Together with @exm-sup-one-minus-reciprocal, \( A \) is a set whose supremum \( 1 \) is not attained.
:::

The pattern of this example, "upper bound, then an element in every band below it", is the one every supremum computation in this book follows. The only new input here was @cor-archimedean-epsilon, which turns "\( 1/n \) is small" into a precise choice of \( n \).

## An ordered field without the Archimedean property

We claimed that the Archimedean property does not follow from the ordered-field axioms alone. Now we back that up with a concrete field containing an element larger than every natural number. The field is made of fractions of polynomials, and the element is the variable \( x \) itself.

A **rational function** is a quotient \( p/q \) of real polynomials \( p \) and \( q \) with \( q \) not the zero polynomial. Two quotients \( p/q \) and \( p'/q' \) are the same element when \( p q' = p' q \), exactly as for fractions of integers. With the usual addition and multiplication of fractions, the rational functions form a field, written \( \nR(x) \). This is the same construction that builds \( \nQ \) out of \( \nZ \), applied to polynomials; it is algebra, and we take it as known without proof here. The real numbers sit inside \( \nR(x) \) as the constant functions.

The **leading coefficient** of a non-zero polynomial is the coefficient of its highest power of \( x \). For instance, the leading coefficient of \( 3 - 2x^2 \) is \( -2 \).

Call a non-zero \( p/q \in \nR(x) \) **positive** if the leading coefficients of \( p \) and \( q \) are both positive or both negative, and write \( f < g \) when \( g - f \) is positive.

Here is the picture behind this definition. For large real \( t \), the value \( p(t)/q(t) \) has the sign of the product of the two leading coefficients, because the top powers dominate. So "\( f > 0 \)" means "\( f(t) > 0 \) for all sufficiently large \( t \)", and \( f < g \) means that the graph of \( g \) eventually lies above the graph of \( f \). This is only a picture: the definition uses leading coefficients and nothing else.

Positivity does not depend on how the fraction is written. Suppose \( p/q = p'/q' \), so that \( p q' = p' q \), and let \( \alpha, \beta, \alpha', \beta' \) be the leading coefficients of \( p, q, p', q' \). The leading coefficient of a product of polynomials is the product of their leading coefficients, so \( \alpha \beta' = \alpha' \beta \). Multiplying both sides by \( \beta \beta' \) gives \( \alpha\beta \cdot \beta'^2 = \alpha'\beta' \cdot \beta^2 \), and \( \beta^2, \beta'^2 > 0 \). Hence \( \alpha\beta \) and \( \alpha'\beta' \) have the same sign: \( p/q \) is positive exactly when \( p'/q' \) is.

With this order \( \nR(x) \) is an ordered field. The key facts are that sums and products of positive elements are positive, and that for each non-zero \( f \) exactly one of \( f \) and \( -f \) is positive. Checking these is routine, and @exr-archimedean-property-c2 walks through them. On the constants, the new order is the old one: the constant \( c \) is positive exactly when \( c > 0 \).

The natural numbers of \( \nR(x) \), the smallest inductive subset in the sense of @def-inductive-set, are the constants \( 1, 2, 3, \dots \).

::: {#exm-nonarchimedean-field}
[A non-Archimedean field]

In \( \nR(x) \) with the order just described, show that \( n < x \) for every \( n \in \nN \). Deduce that \( \nN \) is bounded above in \( \nR(x) \), and that @cor-archimedean-epsilon fails in \( \nR(x) \).
:::

::: {.solution}
Let \( n \in \nN \). Then \( x - n = (x - n)/1 \). The numerator \( x - n \) has leading coefficient \( 1 \) and the denominator \( 1 \) has leading coefficient \( 1 \). They have the same sign, so \( x - n \) is positive, that is, \( n < x \).

Hence \( x \) is an upper bound of \( \nN \) in \( \nR(x) \), and \( \nN \) is bounded above there. So the conclusion of @thm-naturals-unbounded is false in \( \nR(x) \).

Now take \( \varepsilon \coloneqq 1/x \). It is positive: numerator \( 1 \) and denominator \( x \) both have leading coefficient \( 1 \). For each \( n \in \nN \) we have \( 0 < n < x \), so taking reciprocals gives \( 1/x < 1/n \). No natural number \( n \) satisfies \( 1/n < \varepsilon \), and @cor-archimedean-epsilon fails.
:::

The element \( 1/x \) is positive yet smaller than every \( 1/n \): an "infinitely small" number. The real line has none, and that is exactly what @cor-archimedean-epsilon says.

## The line of the proof that fails

Every step in the proof of @thm-naturals-unbounded, except one, is valid in any ordered field. So let us run the proof in \( \nR(x) \) and watch where it breaks.

- "Suppose \( \nN \) is bounded above." In \( \nR(x) \) this is true, with upper bound \( x \).
- "\( \nN \) is non-empty." True.
- "**By @ax-least-upper-bound, \( \nN \) has a supremum \( s \).**" This is the line that fails. In \( \nR(x) \), \( \nN \) has no least upper bound at all. Indeed, let \( M \) be any upper bound of \( \nN \) in \( \nR(x) \). For each \( n \in \nN \), also \( n + 1 \in \nN \), so \( n + 1 \le M \), that is, \( n \le M - 1 \). Hence \( M - 1 \) is also an upper bound, and it is strictly smaller than \( M \). No upper bound is the least one.
- The remaining lines, "\( s - 1 \) is not an upper bound, so some \( n > s - 1 \), and \( n + 1 > s \)", use only the ordered-field axioms and the fact that \( \nN \) is inductive. They would go through in \( \nR(x) \) if there were an \( s \) to apply them to.

The argument that shows \( \nN \) has no supremum in \( \nR(x) \) is the proof of @thm-naturals-unbounded read the other way. That proof showed that a supremum of \( \nN \) cannot exist in any ordered field; the axiom then says that, in \( \nR \), a bounded \( \nN \) would have to have one. In \( \nR(x) \) there is no axiom to force it, so no contradiction arises. Two conclusions follow:

- \( \nR(x) \) is an ordered field in which @ax-least-upper-bound fails, with witness the non-empty, bounded-above set \( \nN \).
- In any ordered field, the least upper bound axiom implies the Archimedean property. That is precisely what our proof showed.

::: {.warning}
The Archimedean property is not "obvious", and it is not a consequence of the ordered-field axioms. It is exactly what \( \nR(x) \) lacks, where \( x \) exceeds every natural number. In \( \nR \) it holds only because of the least upper bound axiom. A proof that says "choose an integer larger than \( x \)" is using @thm-naturals-unbounded, and should cite it.
:::

::: {.remark}
The converse fails: an ordered field can be Archimedean without satisfying the axiom. The field \( \nQ \) is one (@exr-archimedean-property-c3), and it fails the axiom by @thm-no-rational-sup-sqrt2. So the Archimedean property is strictly weaker than the axiom. Chapter 20 shows which properties, added to the Archimedean property, bring back the full axiom.
:::

## Exercises

### A. Check your understanding

::: {#exr-archimedean-property-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Write the Archimedean property "for every \( x \in \nR \) there is \( n \in \nN \) with \( n > x \)" in symbols, and write its negation in symbols.
2. Which of the following subsets of \( \nR \) are inductive: \( [\tfrac12, \infty) \), \( [0, 10] \), \( \nN \cup \{ \tfrac12 \} \), \( \nZ \)? Name the failing clause for each one that is not.
3. True or false, with a reason: in @cor-archimedean-epsilon, one \( n \) can be chosen that works for every \( \varepsilon > 0 \).
4. In the proof of @thm-naturals-unbounded, which line uses the least upper bound axiom, and which line uses that \( \nN \) is inductive?
:::
:::

::: {.solution}
(a) The property is \( (\forall x \in \nR)(\exists n \in \nN)\ n > x \). Its negation is \( (\exists x \in \nR)(\forall n \in \nN)\ n \le x \): some real number is an upper bound of \( \nN \).

(b) \( [\tfrac12, \infty) \) is inductive: it contains \( 1 \), and \( x \ge \tfrac12 \) gives \( x + 1 \ge \tfrac32 \ge \tfrac12 \). \( [0, 10] \) is not: it contains \( 1 \), but \( 10 \in [0, 10] \) and \( 11 \notin [0, 10] \), so (N2) fails. \( \nN \cup \{ \tfrac12 \} \) is not: \( \tfrac12 \) is in it but \( \tfrac32 \) is not, since \( \tfrac32 \) lies strictly between the natural numbers \( 1 \) and \( 2 \); so (N2) fails. \( \nZ \) is inductive: \( 1 \in \nZ \), and \( k + 1 \in \nZ \) for every integer \( k \).

(c) False. Such an \( n \) would satisfy \( 1/n < \varepsilon \) for every \( \varepsilon > 0 \). But \( 1/n > 0 \) by @exm-naturals-at-least-one, so \( \varepsilon = 1/n \) is allowed, and it gives \( 1/n < 1/n \), which is absurd. The \( n \) must depend on \( \varepsilon \).

(d) The axiom is used in "\( \nN \) has a supremum \( s \)". That \( \nN \) is inductive is used in "\( n + 1 \in \nN \)".
:::

### B. Practice

::: {#exr-archimedean-property-b1}
[B1: An infimum]

Prove that \( \inf \{ 1/n : n \in \nN \} = 0 \), and that the set has no minimum.
:::

::: {.solution}
Let \( B \coloneqq \{ 1/n : n \in \nN \} \); it is non-empty, since \( 1 \in B \). By @exm-naturals-at-least-one, \( 1/n > 0 \) for every \( n \), so \( 0 \) is a lower bound of \( B \).

Let \( L \) be any lower bound of \( B \); we show \( L \le 0 \). Suppose instead \( L > 0 \). By @cor-archimedean-epsilon with \( \varepsilon = L \), there is \( n \in \nN \) with \( 1/n < L \). This contradicts \( L \) being a lower bound of \( B \). Hence \( L \le 0 \). So \( 0 \) is a lower bound that is greater than or equal to every lower bound, that is, \( \inf B = 0 \) (@def-infimum).

Since \( 0 \notin B \) (every element is positive), the infimum is not attained, and \( B \) has no minimum.
:::

::: {#exr-archimedean-property-b2}
[B2: Scaled Archimedes]

Let \( a > 0 \) and \( y \in \nR \). Prove that there is \( n \in \nN \) with \( n a > y \). What does this say when \( a \) is the length of a measuring stick?
:::

::: {.solution}
Since \( a > 0 \), the number \( y/a \) is defined. By @thm-naturals-unbounded there is \( n \in \nN \) with \( n > y/a \); the \( n \) depends on \( y \) and \( a \). Multiplying by \( a > 0 \) preserves the strict inequality (@thm-ordered-field-rules (c)), so \( n a > y \).

In words: laying a stick of length \( a \), however short, end to end enough times carries you past any given point \( y \), however far away. This is the form in which Archimedes used the property.
:::

::: {#exr-archimedean-property-b3}
[B3: Smaller than every 1/n]

Let \( x \in \nR \) with \( 0 \le x < 1/n \) for every \( n \in \nN \). Prove that \( x = 0 \). Then deduce: if \( a, b \in \nR \) satisfy \( \abs{a - b} < 1/n \) for every \( n \in \nN \), then \( a = b \).
:::

::: {.solution}
Suppose \( x \ne 0 \). Since \( x \ge 0 \), we get \( x > 0 \). By @cor-archimedean-epsilon with \( \varepsilon = x \), there is \( n \in \nN \) with \( 1/n < x \), contradicting the hypothesis \( x < 1/n \). Hence \( x = 0 \).

For the second statement, put \( x \coloneqq \abs{a - b} \). Then \( 0 \le x < 1/n \) for every \( n \), so \( x = 0 \) by the first part, that is, \( a = b \).

This is how equality is proved in analysis over and over: show that the distance is non-negative and smaller than every \( 1/n \).
:::

::: {#exr-archimedean-property-b4}
[B4: Putting a proof in order]

Here are nine lines. Seven of them, in a suitable order, prove that \( \sup A = 1 \) for \( A \coloneqq \{ \frac{n}{n + 1} : n \in \nN \} \). Give an admissible order. Then say why each of the other two lines cannot be used.

::: {.enumerate options="label=(\roman*)"}
1. Let \( \varepsilon > 0 \).
2. Hence \( a \coloneqq \frac{n}{n + 1} \) is an element of \( A \) with \( a > 1 - \varepsilon \).
3. For every \( n \in \nN \), \( n < n + 1 \) and \( n + 1 > 0 \), so \( \frac{n}{n + 1} < 1 \). Hence \( 1 \) is an upper bound of \( A \).
4. By @cor-archimedean-epsilon there is \( n \in \nN \), depending on \( \varepsilon \), with \( \frac1n < \varepsilon \).
5. Choose \( n \in \nN \) such that \( \frac1n < \varepsilon \) for every \( \varepsilon > 0 \).
6. Since \( \varepsilon > 0 \) was arbitrary, every band \( (1 - \varepsilon, 1] \) contains an element of \( A \).
7. Then \( \frac{n}{n + 1} = 1 - \frac1{n + 1} \), and \( \frac1{n + 1} < \frac1n < \varepsilon \).
8. By @thm-sup-epsilon, \( \sup A = 1 \).
9. Fix \( n \in \nN \) and let \( \varepsilon \coloneqq \frac1n \); then \( \frac{n}{n + 1} = 1 - \frac1{n + 1} > 1 - \varepsilon \).
:::
:::

::: {.solution}
An admissible order is (iii), (i), (iv), (vii), (ii), (vi), (viii). The line (iii) may stand anywhere before (viii), since it uses nothing but the definition of \( A \). The other lines admit only this order. Inside the block that starts with (i), line (iv) needs the \( \varepsilon \) of (i), line (vii) needs the \( n \) of (iv), line (ii) needs (vii), and (vi) records that \( \varepsilon \) was arbitrary. Line (viii) needs both (iii) and (vi), the two hypotheses of @thm-sup-epsilon.

Line (v) has the quantifiers in the wrong order. It asks for one \( n \) that works for every \( \varepsilon \), and there is none: \( \varepsilon = \frac1n \) itself would give \( \frac1n < \frac1n \). @cor-archimedean-epsilon gives an \( n \) for each \( \varepsilon \).

Line (ix) is true, but its \( \varepsilon \) is of the wrong kind: it is chosen to fit \( n \), instead of being given first. It shows only that the bands of the special widths \( \frac1n \) meet \( A \), while @thm-sup-epsilon needs **every** band, of every width \( \varepsilon > 0 \). Passing from the special widths to all widths is exactly the work of lines (iv) and (vii), which (ix) skips.
:::

### C. Going deeper

::: {#exr-archimedean-property-c1}
[C1: Exit check, and a circular proof]

::: {.enumerate options="label=(\alph*)"}
1. Without looking back, prove the Archimedean property from the least upper bound axiom. Mark the line that uses the axiom, and explain why that line fails in \( \nR(x) \).
2. A student offers the following proof. "Let \( x \in \nR \). Let \( n \coloneqq \ceil{x} + 1 \), where \( \ceil{x} \) is the least integer that is greater than or equal to \( x \). Then \( n > x \)." Find the gap. Show that in \( \nR(x) \) the element \( x \) has no "least integer greater than or equal to it".
:::
:::

::: {.solution}
(a) Suppose \( \nN \) is bounded above in \( \nR \). Since \( 1 \in \nN \), the set is non-empty, so by @ax-least-upper-bound it has a supremum \( s \) (**this line uses the axiom**). By (S2), the smaller number \( s - 1 \) cannot be an upper bound of \( \nN \); hence some \( n \in \nN \) has \( n > s - 1 \). Then \( n + 1 \in \nN \) since \( \nN \) is inductive, and \( n + 1 > s \), contradicting that \( s \) is an upper bound. So \( \nN \) is not bounded above, which means that every \( x \in \nR \) is exceeded by some \( n \in \nN \).

In \( \nR(x) \) the set \( \nN \) is non-empty and bounded above by \( x \) (@exm-nonarchimedean-field), but it has no supremum. Any upper bound \( M \) gives a smaller one, \( M - 1 \), because \( n + 1 \le M \) for every \( n \in \nN \) forces \( n \le M - 1 \). So the marked line has nothing to produce, and there the proof stops.

(b) The gap is the existence of \( \ceil{x} \). The set \( \{ k \in \nZ : k \ge x \} \) has a least element only if it is non-empty, and it is non-empty exactly when some integer is at least \( x \). That is (a form of) the Archimedean property, the statement being proved. The proof is circular.

In \( \nR(x) \), take the element \( x \) and suppose \( k \in \nZ \) satisfies \( k \ge x \). If \( k \le 0 \), then \( k \le 0 < 1 < x \). If \( k \ge 1 \), then \( k \in \nN \) and \( k < x \) by @exm-nonarchimedean-field. Either way \( k < x \), a contradiction. So no integer is greater than or equal to \( x \), and \( \ceil{x} \) does not exist.

**Marking scheme.** (10 points)
- 1: (a) supposes, for a contradiction, that \( \nN \) is bounded above, and notes \( 1 \in \nN \).
- 2: (a) obtains \( s = \sup \nN \) from @ax-least-upper-bound, with both hypotheses checked, and marks this line.
- 2: (a) uses the "least" property (S2), or @thm-sup-epsilon with \( \varepsilon = 1 \), to find \( n \in \nN \) with \( n > s - 1 \).
- 1: (a) uses that \( \nN \) is inductive to get \( n + 1 \in \nN \) with \( n + 1 > s \), contradicting (S1), and concludes.
- 1: (a) explains why the marked line fails in \( \nR(x) \): every upper bound \( M \) of \( \nN \) there has the smaller upper bound \( M - 1 \).
- 2: (b) names the existence of \( \ceil{x} \) as the gap, and says it already needs an integer at least \( x \), which is what is being proved.
- 1: (b) shows that no integer is at least \( x \) in \( \nR(x) \).
Fatal errors (0 for the step): taking \( s \) to be a natural number, or the maximum of \( \nN \); asserting "some \( n > s - 1 \)" with no appeal to (S2); using \( \ceil{x} \), \( \floor{x} \) or the Archimedean property inside (a).
A proof of (a) that applies the axiom to a bounded set of the form \( \{ n \in \nN : n \le x \} \) instead earns full marks for (a) if it reaches a contradiction from the supremum in the same way.
:::

::: {#exr-archimedean-property-c2}
[C2: The order on the rational functions]

Let \( P \subseteq \nR(x) \) be the set of positive elements defined in this section, and let \( f < g \) mean \( g - f \in P \).

::: {.enumerate options="label=(\alph*)"}
1. Show that every non-zero \( f \in \nR(x) \) can be written as \( p/q \) with the leading coefficient of \( q \) positive, and that then \( f \in P \) if and only if the leading coefficient of \( p \) is positive.
2. Show that for every non-zero \( f \), exactly one of \( f \in P \) and \( -f \in P \) holds.
3. Show that if \( f, g \in P \), then \( f g \in P \) and \( f + g \in P \).
4. Deduce the order axioms of @def-ordered-field for \( < \): trichotomy, transitivity, \( f < g \Rightarrow f + h < g + h \), and \( f, g > 0 \Rightarrow f g > 0 \).
:::

:::

::: {.solution}
[Hint 1]

Choose good representatives first. Every fraction can be rewritten so that its denominator has positive leading coefficient, and after that only the numerator decides positivity.
:::

::: {.solution}
[Hint 2]

For the sum in (c), with both denominators normalized, write \( f + g = (p_1 q_2 + p_2 q_1)/(q_1 q_2) \) and split into two cases: the two terms of the numerator have different degrees, or the same degree.
:::

::: {.solution}
Write \( \operatorname{lc}(p) \) for the leading coefficient of a non-zero polynomial \( p \). Recall that \( \operatorname{lc}(pq) = \operatorname{lc}(p)\operatorname{lc}(q) \), since the top powers multiply.

(a) Let \( f = p/q \). If \( \operatorname{lc}(q) < 0 \), then \( f = (-p)/(-q) \) and \( \operatorname{lc}(-q) = -\operatorname{lc}(q) > 0 \). So we may assume \( \operatorname{lc}(q) > 0 \). Then "\( \operatorname{lc}(p) \) and \( \operatorname{lc}(q) \) have the same sign" means exactly \( \operatorname{lc}(p) > 0 \). By the well-definedness shown in the section, this does not depend on the chosen representation.

(b) Write \( f = p/q \) with \( \operatorname{lc}(q) > 0 \), as in (a). Then \( -f = (-p)/q \) and \( \operatorname{lc}(-p) = -\operatorname{lc}(p) \). Since \( p \ne 0 \), \( \operatorname{lc}(p) \) is a non-zero real number, so by trichotomy in \( \nR \) exactly one of \( \operatorname{lc}(p) > 0 \) and \( -\operatorname{lc}(p) > 0 \) holds. By (a), exactly one of \( f \in P \) and \( -f \in P \) holds.

(c) Write \( f = p_1/q_1 \) and \( g = p_2/q_2 \) with all four leading coefficients positive, using (a). The product is \( f g = (p_1 p_2)/(q_1 q_2) \) with \( \operatorname{lc}(p_1 p_2) = \operatorname{lc}(p_1)\operatorname{lc}(p_2) > 0 \) and \( \operatorname{lc}(q_1 q_2) > 0 \), so \( f g \in P \). The sum is
\[
    f + g = \frac{p_1 q_2 + p_2 q_1}{q_1 q_2}.
\]
Both \( p_1 q_2 \) and \( p_2 q_1 \) have positive leading coefficient. If their degrees differ, the leading coefficient of the sum is that of the term of higher degree, which is positive. If their degrees agree, it is the sum of the two leading coefficients, which is positive. In both cases the numerator is non-zero with positive leading coefficient, and \( \operatorname{lc}(q_1 q_2) > 0 \), so \( f + g \in P \).

(d) *Trichotomy.* Given \( f, g \), either \( g - f = 0 \), or \( g - f \ne 0 \) and by (b) exactly one of \( g - f \in P \) and \( f - g = -(g - f) \in P \) holds. So exactly one of \( f = g \), \( f < g \), \( g < f \) holds.

*Transitivity.* If \( f < g \) and \( g < h \), then \( g - f \in P \) and \( h - g \in P \), so \( h - f = (h - g) + (g - f) \in P \) by (c); that is, \( f < h \).

*Addition.* If \( f < g \), then \( (g + h) - (f + h) = g - f \in P \), so \( f + h < g + h \).

*Products.* If \( f > 0 \) and \( g > 0 \), then \( f = f - 0 \in P \) and \( g \in P \), so \( f g \in P \) by (c); that is, \( f g > 0 \).
:::

::: {#exr-archimedean-property-c3}
[C3: Archimedean without the axiom]

::: {.enumerate options="label=(\alph*)"}
1. Prove, without using @ax-least-upper-bound, that for every \( r \in \nQ \) there is \( n \in \nN \) with \( n > r \).
2. Deduce that the Archimedean property does not imply the least upper bound axiom in an ordered field.
:::
:::

::: {.solution}
(a) Write \( r = m/k \) with \( m \in \nZ \) and \( k \in \nN \). If \( m \le 0 \), then \( r \le 0 < 1 \), and \( n = 1 \) works. If \( m \ge 1 \), then \( m \in \nN \). Since \( k \ge 1 \) (@exm-naturals-at-least-one) and \( m > 0 \), we get \( r = m/k \le m < m + 1 \), and \( n \coloneqq m + 1 \in \nN \) works. No supremum was used: only the arithmetic of integers and the ordered-field rules.

(b) By (a), \( \nQ \) is an ordered field in which \( \nN \) is not bounded above, so \( \nQ \) has the Archimedean property. By @thm-no-rational-sup-sqrt2, the non-empty set \( \{ x \in \nQ : x > 0, \ x^2 < 2 \} \), which is bounded above by \( 2 \), has no supremum in \( \nQ \). So \( \nQ \) is Archimedean and fails the least upper bound axiom, and the Archimedean property cannot imply the axiom.
:::

<!-- dependency ledger
def-inductive-set (example): N is the intersection of all inductive subsets of R (a set defined from a family of sets) | sets and intersections, ch05 (promised)
exm-naturals-at-least-one (solution): none beyond def-inductive-set and thm-ordered-field-rules | inline
thm-naturals-unbounded (proof): "not (n <= x for all n)" gives "n > x for some n" | quantifier negation, ch03 (promised); the remark after the proof says so
cor-archimedean-epsilon (proof): none | inline
exm-nonarchimedean-field (example): R(x) is a field; lc(pq) = lc(p) lc(q) | algebra of polynomials and fractions, taken as known and stated in the text
exm-nonarchimedean-field (example): the natural numbers of R(x) are the constants 1, 2, 3, ... | inline: the constants form an inductive set, and every inductive set contains them (exr-ordered-fields-c1)
exm-sup-one-minus-reciprocal-finished (solution): 100/101 > 0.99 | arithmetic, shown inline
exr-archimedean-property-a1 (solution): 3/2 lies strictly between the natural numbers 1 and 2, so it is not in N | arithmetic of N stated in the remark on N, ch06 (promised)
exr-archimedean-property-c1 (solution): a non-empty set of integers bounded below has a least element (for the ceiling) | well-ordering, ch06 (promised)
exr-archimedean-property-c3 (solution): every rational is m/k with m in Z, k in N | definition of Q in the remark on N
-->
