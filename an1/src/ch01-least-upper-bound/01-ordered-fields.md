# Ordered Fields and the Gap in the Rationals

Calculus takes for granted that a continuous curve which starts below the axis and ends above it must cross the axis somewhere. Over the rational numbers that is false, and the failure is already visible in the simplest polynomial one can think of. This section shows the failure, then records exactly what the rationals and the reals have in common: the arithmetic of a field and an order compatible with it. Everything in this section holds in both. The one property that separates them is the subject of the rest of the chapter.

## A sign change with no zero

Consider \( f(x) = x^2 - 2 \) on the rational numbers between \( 1 \) and \( 2 \). At the left end \( f(1) = -1 < 0 \), and at the right end \( f(2) = 2 > 0 \). If the rational line had no holes, the graph would have to cross zero somewhere in between. It never does: a rational \( x \) with \( f(x) = 0 \) would be a rational number whose square is \( 2 \), and @fd1:thm-sqrt2-irrational says there is none.

So the rational numbers have a gap, exactly where \( \sqrt{2} \) ought to be. The real numbers are meant to be "the rationals with the gaps filled", and the first task is to say what that means precisely. Before we can name what \( \nR \) has and \( \nQ \) lacks, we must list what the two share. That list is short: four operations with the usual rules, and a way of comparing two numbers that respects those operations.

## Ordered fields

A field is a number system in which one can add, subtract, multiply, and divide by anything nonzero, with the usual rules. The rational, real, and complex numbers are fields; so is the arithmetic of remainders modulo a prime. What \( \nQ \) and \( \nR \) have beyond this, and \( \nC \) does not, is an order: any two numbers can be compared, and the comparison behaves well under addition and multiplication. Every inequality we manipulate in analysis rests on four rules about that comparison, and the definition below states them.

*An ordered field is a number system where we can do arithmetic and compare, and where comparison respects arithmetic.*

::: {#def-ordered-field}
[Ordered Field]

An **ordered field** consists of a set \( F \), two operations, addition \( (a, b) \mapsto a + b \) and multiplication \( (a, b) \mapsto ab \), and a relation \( < \) on \( F \), such that the following hold.

The **field axioms**: **for all** \( a, b, c \in F \),

::: {.enumerate options="label=(F\arabic*)"}
1. \( a + b = b + a \);
2. \( (a + b) + c = a + (b + c) \);
3. there is an element \( 0 \in F \) with \( a + 0 = a \) **for every** \( a \in F \);
4. **for every** \( a \in F \) there is an element \( -a \in F \) with \( a + (-a) = 0 \);
5. \( (ab)c = a(bc) \);
6. \( ab = ba \);
7. there is an element \( 1 \in F \) with **\( 1 \ne 0 \)** and \( a \cdot 1 = a \) **for every** \( a \in F \);
8. **for every nonzero** \( a \in F \) there is an element \( a^{-1} \in F \) with \( a a^{-1} = 1 \);
9. \( a(b + c) = ab + ac \).
:::

The **order axioms**: **for all** \( a, b, c \in F \),

::: {.enumerate options="label=(O\arabic*)"}
1. (trichotomy) **exactly one** of \( a < b \), \( a = b \), \( b < a \) holds;
2. (transitivity) if \( a < b \) and \( b < c \), then \( a < c \);
3. (addition) if \( a < b \), then \( a + c < b + c \);
4. (multiplication) if \( 0 < a \) and \( 0 < b \), then \( 0 < ab \).
:::
:::

The field axioms are the ones of the linear-algebra companion, Chapter 0, in the same numbering. We write \( a - b \coloneqq a + (-b) \) and \( a / b \coloneqq a b^{-1} \) for \( b \ne 0 \). We write \( b > a \) to mean \( a < b \), and \( a \le b \) to mean "\( a < b \) or \( a = b \)". An element \( a \) is **positive** if \( a > 0 \) and **negative** if \( a < 0 \). It is **nonnegative** if \( a \ge 0 \).

In words, the four order axioms say:

- **(O1)** any two elements can be compared, and the three outcomes exclude one another. In particular \( a < a \) never holds.
- **(O2)** comparisons chain.
- **(O3)** adding the same thing to both sides of a strict inequality keeps it strict and keeps its direction.
- **(O4)** the product of two positive elements is positive. This is the only axiom that links the order to multiplication, and every rule about multiplying inequalities will come from it.

From (O1) and (O2), the relation \( \le \) is transitive as well, and a mixed chain \( a \le b < c \) gives \( a < c \): if \( a = b \) this is the hypothesis \( b < c \), and otherwise it is (O2).

**Field algebra.** The field axioms alone imply the familiar algebraic identities. Their proofs use no order at all. Most of them are already proved in the linear-algebra companion, from the same axioms, and we cite those; the few that are not there are short, and we prove them here.

::: {#lem-field-algebra}
[Field Algebra]

Let \( F \) be an ordered field (only (F1)–(F9) are used) and let \( a, b \in F \).

::: {.enumerate options="label=(\alph*)"}
1. The elements \( 0 \) and \( 1 \) are unique, and so are \( -a \) and, for \( a \ne 0 \), \( a^{-1} \). In particular \( -(-a) = a \).
2. \( a \cdot 0 = 0 \).
3. \( (-a)b = -(ab) \) and \( (-a)(-b) = ab \).
4. If \( ab = 0 \), then \( a = 0 \) or \( b = 0 \).
5. \( (a + b)^2 = a^2 + 2ab + b^2 \), where \( x^2 \coloneqq xx \) and \( 2 \coloneqq 1 + 1 \).
:::
:::

::: {.idea}
Each identity is forced by uniqueness. An element is pinned down by the equation it satisfies, so to show that \( (-a)b \) is \( -(ab) \), we show that it satisfies the equation defining \( -(ab) \), namely that it adds to \( ab \) to give \( 0 \). Part (a) is the uniqueness, and the other parts use it.
:::

::: {.proof}
(a), (b) and (d). Apart from \( -(-a) = a \), these are parts of @la:thm-field-basic-properties: the uniqueness of \( 0 \) and of \( -a \); the rule \( 0 \cdot a = 0 \), which gives \( a \cdot 0 = 0 \) by (F6); and "if \( ab = 0 \), then \( a = 0 \) or \( b = 0 \)". The field axioms there are (F1)–(F9) of @def-ordered-field, in the same numbering, so the proofs there apply verbatim, and we do not repeat them. For \( -(-a) = a \): \( (-a) + a = 0 \) by (F1) and (F4), so \( a \) is an additive inverse of \( -a \), and \( -(-a) = a \) by the uniqueness of additive inverses. The multiplicative halves of (a) are proved the same way. If \( 1' \) also satisfies \( x \cdot 1' = x \) for every \( x \), then \( 1 = 1 \cdot 1' = 1' \cdot 1 = 1' \), by that property of \( 1' \), commutativity (F6), and the property of \( 1 \). If \( ab = 1 \) for some \( b \), then \( b = b(aa^{-1}) = (ba)a^{-1} = 1 \cdot a^{-1} = a^{-1} \), by associativity and commutativity of multiplication; so \( a^{-1} \) is unique.

(c) By (F6), (F9), (F4) and (b), \( ab + (-a)b = (a + (-a))b = 0 \cdot b = 0 \), so \( (-a)b \) is an additive inverse of \( ab \), and \( (-a)b = -(ab) \) by (a). Using this twice, with (F6), and then (a), \( (-a)(-b) = -(a(-b)) = -(-(ab)) = ab \).

(e) By (F9) and (F6), \( (a + b)(a + b) = a^2 + ba + ab + b^2 \), and \( ba + ab = ab \cdot 1 + ab \cdot 1 = ab(1 + 1) = 2ab \) by (F6), (F7) and (F9).
:::

From now on these identities, and the rules of fraction arithmetic that follow from them in the same way, are used without comment.

::: {#exm-ordered-fields-q-r}
[The rationals and the reals]

Explain why \( \nQ \) is an ordered field, and what we are assuming when we say \( \nR \) is one.
:::

::: {.solution}
For \( \nQ \), the field axioms are the rules of fraction arithmetic. The order is \( p/q < p'/q' \) (with \( q, q' > 0 \)) exactly when \( pq' < p'q \) as integers. Trichotomy, transitivity, (O3), and (O4) then come from the corresponding facts about integers. Checking them is routine and belongs to the construction of \( \nQ \) from \( \nZ \); here we accept them.

For \( \nR \) we have not yet said what a real number *is*, and this chapter deliberately does not. Instead we **assume** that \( \nR \) is an ordered field containing \( \nQ \), with its usual operations and order; in particular \( \nR \) contains \( \nN \) and \( \nZ \), with their usual arithmetic. (Later in this chapter we locate \( \nN \) inside \( \nR \) using the axioms alone.) A later section of this chapter completes the list of assumptions by adding exactly one more. Everything proved in this section from (F1)–(F9) and (O1)–(O4) therefore holds in \( \nQ \) and in \( \nR \) alike.
:::

::: {#exm-integers-not-a-field}
[A minimal change: the integers]

The integers \( \nZ \), with the usual operations and order, satisfy (O1)–(O4) and every field axiom except one. Which one fails, and does the failure matter for inequalities?
:::

::: {.solution}
Axiom (F8) fails: \( 2 \ne 0 \), but no integer \( m \) has \( 2m = 1 \). Everything else holds, including all four order axioms. So \( \nZ \) is not an ordered field, although it is an "ordered ring". The failure matters as soon as we divide: the rule "if \( 0 < a < b \) then \( 1/b < 1/a \)" proved below has no meaning in \( \nZ \), because \( 1/a \) is not an integer unless \( a = 1 \).
:::

The two examples mark the scope of the definition. \( \nQ \) and \( \nR \) are the main examples, and the rest of the section is about what the axioms force in both. The complex numbers are the instructive nonexample, and they appear as the first payoff of the next theorem.

::: {.remark}
Why state the order axioms with the strict relation \( < \) rather than with \( \le \)? Either could come first, since each can be defined from the other. We take \( < \) because analysis constantly asks whether a strict inequality **survives** an operation. Adding survives (O3); passing to a limit does not: a number that exceeds \( 1 - \varepsilon \) for every \( \varepsilon > 0 \) is only guaranteed to be \( \ge 1 \), not \( > 1 \). Keeping \( < \) primary keeps that question in view.
:::

## The rules for inequalities

*Logic and Proof*, Chapters 1 and 2 used facts such as \( x^2 \ge 0 \) (in @fd1:exm-square-plus-one) and the sign rules for products (in @fd1:exm-abs-product-cases) as school algebra. We now prove them from (O1)–(O4) and the field axioms. So nothing earlier was circular: those facts were true, and here is why.

::: {#thm-ordered-field-rules}
[Rules for Inequalities]

Let \( F \) be an ordered field and let \( a, b, c, d \in F \).

::: {.enumerate options="label=(\alph*)"}
1. \( a < b \) exactly when \( b - a > 0 \), and exactly when \( -b < -a \); in particular \( a > 0 \) if and only if \( -a < 0 \).
2. If \( a \le b \) and \( c \le d \), then \( a + c \le b + d \), and the conclusion is strict if at least one hypothesis is strict.
3. If \( a < b \) and \( c > 0 \), then \( ac < bc \).
4. If \( a < b \) and \( c < 0 \), then \( ac > bc \).
5. If \( a \ne 0 \), then \( a^2 > 0 \). Hence \( a^2 \ge 0 \) for every \( a \), and \( 1 > 0 \).
6. If \( a > 0 \), then \( 1/a > 0 \). If \( 0 < a < b \), then \( 0 < 1/b < 1/a \).
7. If \( a \ge 0 \) and \( b \ge 0 \), then \( a < b \) if and only if \( a^2 < b^2 \).
8. \( 2 \coloneqq 1 + 1 \) is positive, and if \( a < b \), then \( a < \frac{a + b}{2} < b \).
:::
:::

::: {.idea}
Every rule is proved by the same move: turn a comparison into a statement about a single positive element, using (a), and then apply (O3) or (O4) to that element. For instance "\( a < b \) and \( c > 0 \)" becomes "\( b - a \) and \( c \) are positive", and (O4) says their product \( bc - ac \) is positive. The later parts then lean on the earlier ones, so the proof reads top to bottom.
:::

::: {.proof}
(a) If \( a < b \), then (O3) with \( c = -a \) gives \( a + (-a) < b + (-a) \), that is, \( 0 < b - a \). Conversely, if \( 0 < b - a \), then (O3) with \( c = a \) gives \( a < b \). For the second statement, \( (-a) - (-b) = b - a \), so by what was just shown both \( a < b \) and \( -b < -a \) are equivalent to \( b - a > 0 \). Taking \( a = 0 \) and replacing \( b \) by \( a \) gives: \( 0 < a \) if and only if \( -a < 0 \).

(b) From \( a \le b \) we get \( a + c \le b + c \): by (O3) if \( a < b \), and trivially if \( a = b \). In the same way \( c \le d \) gives \( b + c \le b + d \), using (F1) to add \( b \) on the left. Chaining the two by transitivity gives \( a + c \le b + d \), and if either link is strict the chain is strict.

(c) By (a), \( b - a > 0 \). Since also \( c > 0 \), (O4) gives \( (b - a)c > 0 \), that is, \( bc - ac > 0 \) by (F9). By (a) again, \( ac < bc \).

(d) By (a), \( -c > 0 \). Applying (c) with the positive element \( -c \) gives \( a(-c) < b(-c) \), that is, \( -(ac) < -(bc) \). By the second statement of (a), this says \( bc < ac \).

(e) Since \( a \ne 0 \), trichotomy (O1) leaves two cases. *Case 1:* \( a > 0 \). Then \( a^2 = a \cdot a > 0 \) by (O4). *Case 2:* \( a < 0 \). Then \( -a > 0 \) by (a), and \( a^2 = (-a)(-a) > 0 \) by (O4). So \( a^2 > 0 \) whenever \( a \ne 0 \), and \( a^2 = 0 \) when \( a = 0 \); either way \( a^2 \ge 0 \). Finally \( 1 = 1^2 \) and \( 1 \ne 0 \) by (F7), so \( 1 > 0 \).

(f) Let \( a > 0 \). Then \( a^{-1} \ne 0 \), since otherwise \( 1 = a a^{-1} = a \cdot 0 = 0 \), contradicting (F7). Hence \( (a^{-1})^2 > 0 \) by (e), and \( a^{-1} = a \cdot (a^{-1})^2 \) is a product of two positive elements, so \( a^{-1} > 0 \) by (O4). Now let \( 0 < a < b \). Then \( b > 0 \) by (O2), so \( a^{-1} > 0 \) and \( b^{-1} > 0 \), and \( a^{-1} b^{-1} > 0 \) by (O4). Multiplying \( a < b \) by this positive element, (c) gives \( a \cdot a^{-1} b^{-1} < b \cdot a^{-1} b^{-1} \), which simplifies to \( b^{-1} < a^{-1} \).

(g) (\( \Rightarrow \)) Suppose \( 0 \le a < b \). Then \( b > 0 \) by the mixed chain \( 0 \le a < b \). If \( a = 0 \), then \( a^2 = 0 < b^2 \) by (e). If \( a > 0 \), then (c) applied to \( a < b \), once with the positive factor \( a \) and once with the positive factor \( b \), gives \( a^2 < ab \) and \( ab < b^2 \), so \( a^2 < b^2 \) by (O2).
(\( \Leftarrow \)) Suppose \( a^2 < b^2 \). By (O1), either \( a < b \), or \( a = b \), or \( b < a \). If \( a = b \) then \( a^2 = b^2 \), and if \( 0 \le b < a \) then \( b^2 < a^2 \) by the forward direction with the roles of \( a \) and \( b \) swapped. Either conclusion contradicts \( a^2 < b^2 \) by (O1). Hence \( a < b \).

(h) By (e) and (O3), \( 1 + 1 > 0 + 1 = 1 > 0 \), so \( 2 > 0 \) by (O2); in particular \( 2 \ne 0 \) and \( \frac12 > 0 \) by (f). If \( a < b \), then (O3) gives \( a + a < a + b \) and \( a + b < b + b \), that is, \( 2a < a + b < 2b \), where \( a + a = (1 + 1)a = 2a \) by (F9). Multiplying by \( \frac12 > 0 \) using (c) gives \( a < \frac{a + b}{2} < b \). This proves the theorem.
:::

Three more rules of the same kind are @exr-ordered-fields-b1. With (a)–(h) in hand, every inequality manipulation in this chapter is justified by name. Part (h) looks modest, but it already tells us something structural: between any two elements of an ordered field there is a third, so an ordered field has no "next" element after any given one.

The first payoff is a nonexample. The complex numbers form a field, but no relation \( < \) on \( \nC \) satisfies (O1)–(O4). Indeed, if one did, then \( i \ne 0 \) would give \( i^2 > 0 \) by (e), that is, \( -1 > 0 \). But (e) also gives \( 1 > 0 \), and then (a) gives \( -1 < 0 \). Having both \( -1 > 0 \) and \( -1 < 0 \) contradicts trichotomy. So \( \nC \) is a field that cannot be ordered, and this is why the book compares real numbers and never complex ones.

::: {.warning}
Inequalities may be **added** (part (b)) but not freely **multiplied**. From \( a \le b \) and \( c \le d \) it does **not** follow that \( ac \le bd \): take \( a = c = -3 \) and \( b = d = -1 \). Then \( a \le b \) and \( c \le d \), but \( ac = 9 \) and \( bd = 1 \). Multiplying an inequality needs the sign of the factor, as in (c) and (d), and multiplying two inequalities needs nonnegativity, as in @exr-ordered-fields-b1.
:::

::: {.check}
The set \( \{ 0, 1 \} \), with addition and multiplication modulo \( 2 \), is a field (so \( 1 + 1 = 0 \)). Can it be made into an ordered field by some choice of \( < \)?
:::

::: {.solution}
No. In any ordered field \( 1 > 0 \) by @thm-ordered-field-rules (e), and then (O3) gives \( 1 + 1 > 0 + 1 = 1 \), so \( 1 + 1 > 0 \) by (O2). Here \( 1 + 1 = 0 \), so this says \( 0 > 0 \), which trichotomy forbids. The argument never used which relation was chosen, so no choice works.
:::

## Absolute value and distance

In analysis, the question is almost never "is \( x \) equal to \( a \)?" but "how far is \( x \) from \( a \)?". An answer should be a nonnegative number that ignores on which side of \( a \) the point \( x \) lies. The absolute value supplies it.

*\( \abs{x} \) is the size of \( x \) with its sign removed, and \( \abs{x - a} \) is the distance from \( x \) to \( a \).*

::: {#def-absolute-value}
[Absolute Value]

Let \( F \) be an ordered field. The **absolute value** of \( x \in F \) is
\[
\abs{x} \coloneqq
\begin{cases}
x & \text{if } x \ge 0, \\
-x & \text{if } x < 0.
\end{cases}
\]
:::

The definition is by cases, and trichotomy guarantees that exactly one case applies, so \( \abs{x} \) is well defined. For example \( \abs{3} = 3 \), \( \abs{-3} = -(-3) = 3 \), and \( \abs{0} = 0 \); the degenerate point \( 0 \) falls in the first case, and it is the only element of absolute value \( 0 \). A minimal change shows that the case split is doing real work: the rule "\( \abs{x} = x \) for all \( x \)" agrees with the definition on every nonnegative \( x \) and fails at every negative one, where it would make \( \abs{-3} = -3 < 0 \).

The next proposition collects the facts about absolute value that we use constantly. *Logic and Proof*, Chapter 1 proved some of them by cases (@fd1:exm-triangle-inequality-cases begins with \( a \le \abs{a} \) and \( -a \le \abs{a} \)), taking the sign rules on trust; the sign rules are now @thm-ordered-field-rules.

::: {#prp-absolute-value-rules}
[Rules for Absolute Value]

Let \( F \) be an ordered field and let \( x, y, r \in F \).

::: {.enumerate options="label=(\alph*)"}
1. \( \abs{x} \ge 0 \), and \( \abs{x} = 0 \) if and only if \( x = 0 \).
2. \( \abs{-x} = \abs{x} \), \( \abs{xy} = \abs{x} \abs{y} \), and \( \abs{x}^2 = x^2 \).
3. \( -\abs{x} \le x \le \abs{x} \).
4. \( \abs{x} \le r \) if and only if \( -r \le x \le r \); and \( \abs{x} < r \) if and only if \( -r < x < r \).
:::
:::

::: {.idea}
The definition of \( \abs{x} \) has two cases, so each part is proved by checking \( x \ge 0 \) and \( x < 0 \) separately and quoting the sign rules of @thm-ordered-field-rules in each case. Part (d) is the exception. Once (c) is available, (d) needs no new case split for its forward direction.
:::

::: {.proof}
(a) If \( x \ge 0 \) then \( \abs{x} = x \ge 0 \), with equality exactly when \( x = 0 \). If \( x < 0 \) then \( \abs{x} = -x > 0 \) by @thm-ordered-field-rules (a).

(b) If \( x > 0 \) then \( -x < 0 \), so \( \abs{-x} = -(-x) = x = \abs{x} \); if \( x < 0 \) then \( -x > 0 \), so \( \abs{-x} = -x = \abs{x} \); and \( \abs{-0} = \abs{0} \). For the product, both \( \abs{xy} \) and \( \abs{x}\abs{y} \) are one of the two elements \( xy \) and \( -xy \), since each absolute value is its argument up to sign. Both are nonnegative: \( \abs{xy} \ge 0 \) by (a), and \( \abs{x}\abs{y} \ge 0 \) by (O4) when both factors are positive and trivially when one is \( 0 \). If \( xy = 0 \), both are \( 0 \). If \( xy \ne 0 \), then exactly one of \( xy \) and \( -xy \) is positive, by trichotomy and @thm-ordered-field-rules (a), so both must be that one. Either way \( \abs{xy} = \abs{x}\abs{y} \). Finally \( \abs{x}^2 = (\pm x)^2 = x^2 \).

(c) If \( x \ge 0 \), then \( x = \abs{x} \), and \( -\abs{x} = -x \le 0 \le x \). If \( x < 0 \), then \( -\abs{x} = x \), and \( x < 0 < -x = \abs{x} \).

(d) (\( \Rightarrow \)) Suppose \( \abs{x} \le r \). By (c), \( x \le \abs{x} \le r \). Also \( -r \le -\abs{x} \) by @thm-ordered-field-rules (a), and \( -\abs{x} \le x \) by (c), so \( -r \le x \).
(\( \Leftarrow \)) Suppose \( -r \le x \le r \). If \( x \ge 0 \), then \( \abs{x} = x \le r \). If \( x < 0 \), then \( \abs{x} = -x \le r \), because \( -r \le x \) gives \( -x \le r \) by @thm-ordered-field-rules (a).
The strict version is the same argument with \( < \) in place of \( \le \) wherever \( r \) appears.
:::

Part (d), applied to \( x - a \) in place of \( x \), is the single most used equivalence in this book. Adding \( a \) throughout by (O3), it reads
\[
\abs{x - a} < r
\quad\iff\quad
a - r < x < a + r .
\]{#eq-abs-interval}
In words: *\( x \) is within distance \( r \) of \( a \) exactly when \( x \) lies in the open interval of radius \( r \) centered at \( a \)*. Here, for \( a \le b \) in \( F \), the **intervals** are \( (a, b) \coloneqq \{ x \in F : a < x < b \} \), \( [a, b] \coloneqq \{ x \in F : a \le x \le b \} \), and \( (a, b] \), \( [a, b) \) similarly; in the degenerate case \( a = b \), the closed interval \( [a, a] = \{ a \} \) is a single point and the other three are empty; \( (a, \infty) \coloneqq \{ x \in F : x > a \} \), and the other unbounded intervals are defined in the same way. The symbol \( \infty \) here is part of the name of a set, not an element of \( F \). From Chapter 2 on, every statement "\( a_n \) is close to \( L \)" is turned into two inequalities by @eq-abs-interval, and back.

::: {#exm-solve-abs-inequality}
[Reading an absolute-value inequality as an interval]

Find all real \( x \) with \( \abs{4 - 3x} < 2 \).
:::

::: {.solution}
By @prp-absolute-value-rules (d), \( \abs{4 - 3x} < 2 \) holds if and only if \( -2 < 4 - 3x < 2 \). Subtracting \( 4 \) throughout (O3) gives \( -6 < -3x < -2 \). Multiplying by the negative number \( -\frac13 \) reverses both inequalities, by @thm-ordered-field-rules (d): \( 2 > x > \frac23 \). Every step was an equivalence, so the solution set is the interval \( \left( \frac23, 2 \right) \).

As a check against @eq-abs-interval: \( \abs{4 - 3x} = \abs{-3} \abs{x - \frac43} = 3 \abs{x - \frac43} \) by @prp-absolute-value-rules (b), so the condition says \( \abs{x - \frac43} < \frac23 \), the interval of radius \( \frac23 \) about \( \frac43 \), which is \( \left( \frac23, 2 \right) \) again.
:::

Distance should satisfy one more law: going from \( x \) to \( z \) directly is never longer than going via a third point \( y \). For numbers, that law is the triangle inequality.

::: {#thm-triangle-inequality}
[Triangle Inequality]

Let \( F \) be an ordered field. For all \( x, y \in F \),

::: {.enumerate options="label=(\alph*)"}
1. \( \abs{x + y} \le \abs{x} + \abs{y} \);
2. \( \bigl| \abs{x} - \abs{y} \bigr| \le \abs{x - y} \) (the **reverse triangle inequality**).
:::
:::

::: {.idea}
*Logic and Proof*, Chapter 1 proved (a) in @fd1:exm-triangle-inequality-cases with two case splits: one to show \( a \le \abs{a} \) and \( -a \le \abs{a} \), and then one on the sign of \( x + y \). Here the first split is already done, as @prp-absolute-value-rules (c), and the second is not needed. By @prp-absolute-value-rules (d), the goal \( \abs{x + y} \le \abs{x} + \abs{y} \) is the pair of inequalities \( -(\abs{x} + \abs{y}) \le x + y \le \abs{x} + \abs{y} \), and these come from adding the two sandwiches \( -\abs{x} \le x \le \abs{x} \) and \( -\abs{y} \le y \le \abs{y} \). For (b), write \( x \) as \( (x - y) + y \) and apply (a).
:::

::: {.proof}
(a) By @prp-absolute-value-rules (c), \( -\abs{x} \le x \le \abs{x} \) and \( -\abs{y} \le y \le \abs{y} \). Adding these by @thm-ordered-field-rules (b) gives
\[
-(\abs{x} + \abs{y}) \le x + y \le \abs{x} + \abs{y}.
\]
By @prp-absolute-value-rules (d) with \( r = \abs{x} + \abs{y} \), this says \( \abs{x + y} \le \abs{x} + \abs{y} \).

(b) By (a) applied to \( x - y \) and \( y \), \( \abs{x} = \abs{(x - y) + y} \le \abs{x - y} + \abs{y} \), so \( \abs{x} - \abs{y} \le \abs{x - y} \). Swapping the roles of \( x \) and \( y \) gives \( \abs{y} - \abs{x} \le \abs{y - x} = \abs{x - y} \), using @prp-absolute-value-rules (b). The two inequalities together say \( -\abs{x - y} \le \abs{x} - \abs{y} \le \abs{x - y} \), which is (b) by @prp-absolute-value-rules (d). This proves the theorem.
:::

The case-free proof is typical of what the axioms buy: once a fact such as \( -\abs{x} \le x \le \abs{x} \) is proved, it can be added, multiplied, and chained without redoing sign cases. The triangle inequality is the engine of every estimate in Part I. Its standard use is "insert a third point": to bound \( \abs{x - z} \), write \( x - z = (x - y) + (y - z) \) for a well-chosen \( y \), and bound the two pieces separately (@exr-ordered-fields-b2).

::: {.remark}
The inequality in (a) can be strict: \( \abs{1 + (-1)} = 0 < 2 = \abs{1} + \abs{-1} \). Equality holds exactly when \( x \) and \( y \) do not have strictly opposite signs, that is, when \( xy \ge 0 \) (@exr-ordered-fields-b2).
:::

**Comparing by squaring.** Two absolute values can often be compared without any case split, by squaring. For nonnegative \( a \) and \( b \), @thm-ordered-field-rules (g) says that \( a < b \) holds exactly when \( a^2 < b^2 \), and @prp-absolute-value-rules (b) gives \( \abs{u}^2 = u^2 \). For example, which \( x \) satisfy \( \abs{x - 2} < \abs{x} \)? Both sides are nonnegative, so the inequality holds if and only if \( (x - 2)^2 < x^2 \), that is, \( x^2 - 4x + 4 < x^2 \). By (O3) this is \( 4 < 4x \), and multiplying by \( \frac14 > 0 \) gives \( x > 1 \). Every step was an equivalence, so the solution set is \( (1, \infty) \): the points closer to \( 2 \) than to \( 0 \).

## Where this leaves us

Everything proved so far holds in \( \nQ \) and in \( \nR \) equally. So none of it can explain why \( x^2 - 2 \) has a zero in \( [1, 2] \) over \( \nR \) and not over \( \nQ \). The difference between the two fields is not arithmetic and not the order rules; it is a property of **sets** of numbers. The next section introduces the language for that property: upper bounds, maxima, and the least upper bound.

## Exercises

### A. Check your understanding

::: {#exr-ordered-fields-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Here is a derivation, in an ordered field, of "if \( a > 0 \) and \( b > 0 \) then \( a + b > 0 \)": from \( b > 0 \) we get \( a + b > a + 0 \); and \( a + 0 = a \); and \( a > 0 \); hence \( a + b > 0 \). Name the axiom that justifies each of the four steps.
2. True or false, with a reason: in an ordered field, if \( a < b \) then \( a^2 < b^2 \).
3. True or false, with a reason: \( \abs{x} = \max \{ x, -x \} \) for every \( x \) in an ordered field. (Here \( \max\{ a, b \} \) is the larger of \( a \) and \( b \): it is \( a \) if \( a \ge b \), and \( b \) otherwise.)
4. The integers satisfy all four order axioms. Why is \( \nZ \) not an ordered field?
:::
:::

::: {.solution}
(a) The first step is (O3), adding \( a \) to both sides of \( 0 < b \) (with (F1) to put \( a \) on the left). The second is (F3), the defining property of \( 0 \). The third is the hypothesis. The last is transitivity (O2): \( 0 < a \) and \( a < a + b \) give \( 0 < a + b \).

(b) False. Take \( a = -2 \) and \( b = 1 \): then \( a < b \), but \( a^2 = 4 > 1 = b^2 \). @thm-ordered-field-rules (g) needs both numbers nonnegative.

(c) True. If \( x \ge 0 \), then \( -x \le 0 \le x \), so the larger of \( x \) and \( -x \) is \( x = \abs{x} \). If \( x < 0 \), then \( x < 0 < -x \), so the larger is \( -x = \abs{x} \).

(d) Axiom (F8) fails: \( 2 \) has no multiplicative inverse in \( \nZ \), since \( 2m = 1 \) has no integer solution.
:::

### B. Practice

::: {#exr-ordered-fields-b1}
[B1: Three more rules]

Let \( F \) be an ordered field and \( a, b, c, d \in F \). Prove the following from the axioms and @thm-ordered-field-rules.

::: {.enumerate options="label=(\alph*)"}
1. If \( a > 0 \) and \( b < 0 \), then \( ab < 0 \).
2. If \( 0 \le a < b \) and \( 0 \le c < d \), then \( ac < bd \).
3. If \( a > 0 \) and \( ab > 0 \), then \( b > 0 \).
:::
:::

::: {.solution}
(a) Since \( b < 0 \), @thm-ordered-field-rules (a) gives \( -b > 0 \). By (O4), \( a(-b) > 0 \), that is, \( -(ab) > 0 \). By @thm-ordered-field-rules (a) again, \( ab < 0 \).

(b) Since \( 0 \le c < d \), we have \( d > 0 \). From \( a < b \) and \( d > 0 \), @thm-ordered-field-rules (c) gives \( ad < bd \). From \( c < d \) and \( a \ge 0 \) we get \( ac \le ad \): by @thm-ordered-field-rules (c) if \( a > 0 \), and because both sides are \( 0 \) if \( a = 0 \). Chaining, \( ac \le ad < bd \), so \( ac < bd \).

(c) By trichotomy, \( b > 0 \), \( b = 0 \), or \( b < 0 \). If \( b = 0 \) then \( ab = 0 \), and if \( b < 0 \) then \( ab < 0 \) by (a). Both contradict \( ab > 0 \) by (O1). Hence \( b > 0 \).
:::

::: {#exr-ordered-fields-b2}
[B2: Inserting a third point]

Let \( F \) be an ordered field and \( x, y, z \in F \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \abs{x - z} \le \abs{x - y} + \abs{y - z} \).
2. Prove that \( \abs{x + y} = \abs{x} + \abs{y} \) if and only if \( xy \ge 0 \).
:::
:::

::: {.solution}
(a) Since \( x - z = (x - y) + (y - z) \), @thm-triangle-inequality (a) gives \( \abs{x - z} \le \abs{x - y} + \abs{y - z} \).

(b) Both sides are nonnegative, so by @thm-ordered-field-rules (g) they are equal if and only if their squares are equal (apply (g) in both directions and use trichotomy). Using @prp-absolute-value-rules (b),
\[
\abs{x + y}^2 = x^2 + 2xy + y^2,
\qquad
(\abs{x} + \abs{y})^2 = x^2 + 2\abs{xy} + y^2 .
\]
These are equal if and only if \( xy = \abs{xy} \), which by the definition of absolute value happens if and only if \( xy \ge 0 \).
:::

::: {#exr-ordered-fields-b3}
[B3: Solving inequalities]

Find all real \( x \) satisfying each inequality. Hence write each solution set as an interval.

::: {.enumerate options="label=(\alph*)"}
1. \( \abs{2x - 3} < 5 \).
2. \( \abs{x - 1} < \abs{x + 1} \).
:::
:::

::: {.solution}
(a) By @prp-absolute-value-rules (d), the inequality holds if and only if \( -5 < 2x - 3 < 5 \). Adding \( 3 \) gives \( -2 < 2x < 8 \), and multiplying by \( \frac12 > 0 \) gives \( -1 < x < 4 \). Each step is reversible, so the solution set is \( (-1, 4) \).

(b) Both sides are nonnegative, so by @thm-ordered-field-rules (g) and @prp-absolute-value-rules (b) the inequality holds if and only if \( (x - 1)^2 < (x + 1)^2 \). Expanding, this is \( x^2 - 2x + 1 < x^2 + 2x + 1 \), which by (O3) is equivalent to \( 0 < 4x \), and by multiplying with \( \frac14 > 0 \) to \( x > 0 \). The solution set is \( (0, \infty) \): the points closer to \( 1 \) than to \( -1 \).
:::

### C. Going deeper

::: {#exr-ordered-fields-c1}
[C1: Ordered fields contain the counting numbers]

::: {.enumerate options="label=(\alph*)"}
1. The field \( \{ 0, 1, 2 \} \) with arithmetic modulo \( 3 \) has \( 1 + 1 + 1 = 0 \). Show that it admits no order satisfying (O1)–(O4).
2. In an ordered field \( F \), define \( n \cdot 1 \) for \( n \in \nN \) by \( 0 \cdot 1 \coloneqq 0 \) and \( (n + 1) \cdot 1 \coloneqq n \cdot 1 + 1 \). Prove that \( n \cdot 1 > 0 \) for every \( n \in \nN \) with \( n \ge 1 \), and that \( m \cdot 1 < n \cdot 1 \) whenever \( m < n \).
3. Deduce that the elements \( 0, 1, 1 + 1, 1 + 1 + 1, \dots \) of an ordered field are all different, so every ordered field contains a copy of \( \nN \) (and in particular is infinite).
:::

*Hint: for (b), use induction on \( n \) (@fd1:ax-induction).*
:::

::: {.solution}
(a) Suppose an order existed. By @thm-ordered-field-rules (e), \( 1 > 0 \). By (O3), \( 1 + 1 > 0 + 1 = 1 \), so \( 1 + 1 > 0 \) by (O2), and again \( 1 + 1 + 1 > 1 > 0 \). But \( 1 + 1 + 1 = 0 \), so this says \( 0 > 0 \), contradicting trichotomy (O1).

(b) We prove \( n \cdot 1 > 0 \) by induction on \( n \), starting at \( n = 1 \). For \( n = 1 \), \( 1 \cdot 1 = 0 \cdot 1 + 1 = 0 + 1 = 1 > 0 \) by @thm-ordered-field-rules (e). If \( n \cdot 1 > 0 \), then by (O3), \( (n + 1) \cdot 1 = n \cdot 1 + 1 > n \cdot 1 \), and (O2) gives \( (n + 1) \cdot 1 > 0 \). The same step shows \( (k + 1) \cdot 1 > k \cdot 1 \) for every \( k \). Now fix \( m \) and prove \( m \cdot 1 < n \cdot 1 \) for every \( n > m \) by induction on \( n \), starting at \( n = m + 1 \): the base case is the step just shown with \( k = m \), and if \( m \cdot 1 < n \cdot 1 \), then \( m \cdot 1 < n \cdot 1 < (n + 1) \cdot 1 \), so (O2) gives \( m \cdot 1 < (n + 1) \cdot 1 \).

(c) If \( m \ne n \), say \( m < n \), then \( m \cdot 1 < n \cdot 1 \) by (b), so \( m \cdot 1 \ne n \cdot 1 \) by trichotomy. Hence \( n \mapsto n \cdot 1 \) is injective from \( \nN \) into \( F \), and by (b) it respects order. It also respects addition: \( (m + n) \cdot 1 = m \cdot 1 + n \cdot 1 \), by induction on \( n \) with \( m \) fixed. For \( n = 0 \) both sides are \( m \cdot 1 \), since \( 0 \cdot 1 = 0 \). If it holds for \( n \), then \( (m + (n + 1)) \cdot 1 = ((m + n) + 1) \cdot 1 = (m + n) \cdot 1 + 1 = m \cdot 1 + n \cdot 1 + 1 = m \cdot 1 + (n + 1) \cdot 1 \), using the definition twice and (F2). This is the sense in which \( F \) contains a copy of \( \nN \). The section on the natural numbers inside \( \nR \), later in this chapter, starts from exactly this copy.
:::

::: {#exr-ordered-fields-c2}
[C2: Max and min without cases]

Let \( F \) be an ordered field and \( a, b \in F \). Write \( \max\{ a, b \} \) for the larger of \( a \) and \( b \) and \( \min\{ a, b \} \) for the smaller (as in @exr-ordered-fields-a1). Prove that
\[
\max \{ a, b \} = \frac{a + b + \abs{a - b}}{2},
\qquad
\min \{ a, b \} = \frac{a + b - \abs{a - b}}{2}.
\]
Hence show that \( \abs{\max\{a, b\} - \max\{c, d\}} \le \max\{ \abs{a - c}, \abs{b - d} \} \) for all \( a, b, c, d \in F \).

*Hint: for the last part, bound \( \max\{a, b\} \) above by \( \max\{c, d\} + \max\{ \abs{a - c}, \abs{b - d} \} \).*
:::

::: {.solution}
If \( a \ge b \), then \( \abs{a - b} = a - b \), so \( \frac{a + b + \abs{a - b}}{2} = \frac{2a}{2} = a = \max\{a, b\} \) and \( \frac{a + b - \abs{a - b}}{2} = b = \min\{a, b\} \). If \( a < b \), then \( \abs{a - b} = b - a \), and the same computation gives \( b \) and \( a \). By trichotomy these cases cover everything.

For the inequality, put \( m \coloneqq \max\{ \abs{a - c}, \abs{b - d} \} \). By @prp-absolute-value-rules (c), \( a \le c + \abs{a - c} \le \max\{c, d\} + m \), and likewise \( b \le d + \abs{b - d} \le \max\{c, d\} + m \). Hence \( \max\{a, b\} \le \max\{c, d\} + m \), that is, \( \max\{a, b\} - \max\{c, d\} \le m \). Swapping the roles of \( (a, b) \) and \( (c, d) \), which leaves \( m \) unchanged, gives \( \max\{c, d\} - \max\{a, b\} \le m \). By @prp-absolute-value-rules (d), the two together say \( \abs{\max\{a, b\} - \max\{c, d\}} \le m \).
:::

<!-- dependency ledger
exm-ordered-fields-q-r (example): Q with fraction arithmetic and p/q < p'/q' iff pq' < p'q satisfies (F1)-(F9) and (O1)-(O4) | taken as known from the arithmetic of Z; the construction of Q is not in the main line (F2.2 (promised) for the integer facts)
exm-ordered-fields-q-r (example): R is an ordered field containing Q, N and Z | assumption, stated in the example; completed by ax-least-upper-bound in 03-the-axiom
lem-field-algebra (proof): the rules of fraction arithmetic (a/b + c/d = (ad + bc)/bd and the like) | inline: derived from (F1)-(F9) as in lem-field-algebra, stated in the sentence after the proof and not written out
exm-integers-not-a-field (example): no integer m satisfies 2m = 1 | arithmetic of Z, F2.2 (promised)
exr-ordered-fields-a1 (solution): no integer m satisfies 2m = 1 | arithmetic of Z, F2.2 (promised)
exr-ordered-fields-c1 (solution): proof by induction on n, a second induction starting at m + 1, and a third for (m + n) 1 = m 1 + n 1 | induction, ax-induction
exr-ordered-fields-c1 (solution): (m + n) + 1 = m + (n + 1) in N | arithmetic of N, F2.2 (promised)
thm-ordered-field-rules (example): C is a field with i^2 = -1 (the non-example of C after the theorem) | school algebra of complex numbers; companion ch 0
-->
