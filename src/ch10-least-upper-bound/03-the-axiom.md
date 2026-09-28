# The Least Upper Bound Axiom

We now know exactly what goes wrong in the rationals. The set of positive rationals whose square is less than \( 2 \) is non-empty and bounded above, and yet it has no supremum in \( \nQ \) (@thm-no-rational-sup-sqrt2). Every failure of calculus over \( \nQ \) traces back to gaps of this kind. This section adds one axiom to the ordered-field axioms, stating that such gaps do not occur in \( \nR \). Then it draws the first consequence: infima exist too, for free.

## The axiom

Up to now, "\( \nR \) is an ordered field containing \( \nQ \)" has been our only assumption about the real numbers (@exm-ordered-fields-q-r). That assumption holds for \( \nQ \) itself, so it cannot be what makes \( \nR \) different. We add exactly one more.

*Every set of reals that is bounded above has a least upper bound, unless it is empty.*

::: {#ax-least-upper-bound}
[Least Upper Bound Axiom]

Every **non-empty** subset of \( \nR \) that is **bounded above** has a supremum in \( \nR \).
:::

In symbols: for every \( A \subseteq \nR \),
\[
\Bigl( A \ne \emptyset
\ \text{ and } \
\exists M \in \nR \ \forall a \in A : a \le M \Bigr)
\ \Rightarrow \
\exists s \in \nR : s = \sup A .
\]

**Standing assumption.** From now on, \( \nR \) is an ordered field (@def-ordered-field), containing \( \nQ \), that satisfies @ax-least-upper-bound. Every theorem about real numbers in this book is proved from these assumptions and nothing else.

In words, the axiom has two hypotheses and one conclusion. The hypotheses are about the set \( A \): it has at least one element, and at least one upper bound. The conclusion is about \( \nR \): among the upper bounds of \( A \) there is a least one, and it is a real number. By @thm-sup-unique it is unique, so the notation \( \sup A \) is justified whenever the two hypotheses hold. The axiom is also called the **completeness axiom**; "complete" will acquire a second, related meaning in Chapter 11, and the two are reconciled in Chapter 20.

Each hypothesis is there because without it the conclusion is false.

- **Non-empty.** The empty set is bounded above, by every real number, and it has no supremum (shown in the section on suprema). Without "non-empty", the axiom would be false.
- **Bounded above.** The interval \( [0, \infty) \) contains \( 0 \), but no real number sits above all of it, so there is no least such number either. The set \( \nN \) is a subtler example of the same failure; that it is not bounded above in \( \nR \) is proved later in this chapter, from this very axiom.

The axiom is a statement about \( \nR \) and not about ordered fields in general. It fails in \( \nQ \): @thm-no-rational-sup-sqrt2 exhibits a non-empty subset of \( \nQ \), bounded above in \( \nQ \), with no supremum in \( \nQ \) (@exr-the-axiom-c1). So the axiom is exactly the property that separates the two fields we have been comparing.

::: {.remark}
Why is this an axiom and not a theorem? Because we have not said what a real number is. One can **construct** \( \nR \) from \( \nQ \), for instance by Dedekind cuts, and then prove the least upper bound property as a theorem; the optional Chapter 21 does this. The optional Chapter 22 shows that any two ordered fields satisfying the axiom are the same up to relabeling, so the axiom pins \( \nR \) down completely. Nothing else in the book uses those chapters: everything we need follows from the axiom.
:::

::: {#exm-lub-first-use}
[A set of reals that must have a supremum]

Let \( S = \{ x \in \nR : x > 0 \text{ and } x^2 < 2 \} \). Show that \( \sup S \) exists in \( \nR \). What can be said about it so far?
:::

::: {.solution}
We check the two hypotheses of @ax-least-upper-bound. \( S \) is non-empty, since \( 1 > 0 \) and \( 1^2 < 2 \). \( S \) is bounded above by \( 2 \): if \( x \in S \) had \( x > 2 \), then \( x^2 > 4 \) by @thm-ordered-field-rules (g), contradicting \( x^2 < 2 \). So the axiom gives a real number \( s = \sup S \).

So far we know only what (S1) and (S2) give: \( 1 \le s \le 2 \), since \( 1 \in S \) and \( 2 \) is an upper bound. Compare this with @thm-no-rational-sup-sqrt2. The rational version of this set has no supremum in \( \nQ \), and the proof of that theorem showed that a rational candidate \( s \) with \( s^2 < 2 \) or \( s^2 > 2 \) cannot be the supremum. Neither case used rationality except to keep \( s \pm h \) rational. So we can guess the answer: \( s^2 = 2 \). Proving it, and so proving that \( \sqrt 2 \) exists, is done later in this chapter.
:::

The example shows the pattern of every use of the axiom. First check the two hypotheses, which is usually routine. Then the axiom hands over a number \( s \), and all we know about \( s \) is (S1) and (S2). Everything else must be extracted from those two properties.

::: {.warning}
**Do not forget "non-empty".** The empty set is bounded above and has no supremum, so an argument that applies the axiom to a set without first producing an element of that set is incomplete. The failure is easy to commit when the set is defined by a condition, such as \( \{ x \in \nR : x^2 < c \} \): for \( c \le 0 \) that set is empty.
:::

::: {.warning}
**The axiom gives existence, not a formula.** It says that \( \sup A \) exists; it does not say what it is, and it is usually **not** the upper bound \( M \) used to check the hypothesis. For \( S \) above, the hypothesis was checked with \( M = 2 \), and \( \sup S \ne 2 \): the smaller number \( \frac32 \) is also an upper bound, since any \( x > \frac32 \) has \( x^2 > \frac94 > 2 \) by @thm-ordered-field-rules (g). To identify a supremum we must still verify (S1) and (S2) for a specific candidate.
:::

::: {.check}
Let \( A = \{ n \in \nZ : n \le 3.5 \} = \{ \dots, 1, 2, 3 \} \). Does \( A \) satisfy the hypotheses of @ax-least-upper-bound? What is \( \sup A \), and is it a maximum?
:::

::: {.solution}
Yes: \( 3 \in A \), so \( A \) is non-empty, and \( 3.5 \) is an upper bound by definition of \( A \). So \( \sup A \) exists. It is \( 3 \), not \( 3.5 \): the element \( 3 \) is an upper bound, because an integer greater than \( 3 \) is at least \( 4 \), which exceeds \( 3.5 \) (arithmetic of the integers, Chapter 6), and it belongs to \( A \), so it is the maximum, and a maximum is the supremum (@exr-suprema-b1). The bound used to check the hypothesis was not the supremum.
:::

## Infima come free

The axiom is stated for suprema only. We do not need a second axiom for infima: reflecting the line through \( 0 \) turns lower bounds into upper bounds and "greatest" into "least". To say this precisely we need the reflected set.

For \( A \subseteq \nR \), let
\[
-A \coloneqq \{ -a : a \in A \} .
\]
So \( x \in -A \) if and only if \( -x \in A \), and \( -(-A) = A \). For example, \( -(0, 1] = [-1, 0) \), and \( -\{ -1, 3 \} = \{ 1, -3 \} \). The definition makes sense in any ordered field, and the next theorem holds in any ordered field; the axiom enters only afterwards.

::: {#thm-inf-neg-sup}
[Infimum by Reflection]

Let \( F \) be an ordered field, \( A \subseteq F \), and \( m, t \in F \).

::: {.enumerate options="label=(\alph*)"}
1. \( m \) is a lower bound of \( A \) if and only if \( -m \) is an upper bound of \( -A \).
2. \( t \) is an infimum of \( A \) if and only if \( -t \) is a supremum of \( -A \).
:::

In particular, if \( -A \) has a supremum, then \( A \) has an infimum, and \( \inf A = -\sup(-A) \).
:::

::: {.idea}
Reflection \( x \mapsto -x \) reverses every inequality (@thm-ordered-field-rules (a)), so it should carry each property of an infimum to the matching property of a supremum. The proof checks this property by property: (I1) against (S1), and (I2) against (S2), which is the "split into two properties" move for suprema.
:::

::: {.proof}
(a) By @thm-ordered-field-rules (a), \( m \le a \) if and only if \( -a \le -m \). So \( m \le a \) for every \( a \in A \) if and only if \( -a \le -m \) for every \( a \in A \). The elements \( -a \) with \( a \in A \) are exactly the elements of \( -A \), so the last statement says that \( -m \) is an upper bound of \( -A \).

(b) (\( \Rightarrow \)) Suppose \( t \) is an infimum of \( A \). By (I1), \( t \) is a lower bound of \( A \), so by (a), \( -t \) is an upper bound of \( -A \): this is (S1) for \( -t \). For (S2), let \( M \) be an upper bound of \( -A \). By (a) applied to \( m = -M \), the element \( -M \) is a lower bound of \( A \). By (I2), \( -M \le t \), and so \( -t \le M \) by @thm-ordered-field-rules (a). Hence \( -t \) is a supremum of \( -A \).

(\( \Leftarrow \)) Suppose \( -t \) is a supremum of \( -A \). By (S1) and (a), \( t \) is a lower bound of \( A \): this is (I1). For (I2), let \( m \) be a lower bound of \( A \). By (a), \( -m \) is an upper bound of \( -A \), so (S2) gives \( -t \le -m \), that is, \( m \le t \). Hence \( t \) is an infimum of \( A \).

The final sentence follows from (b) with \( t \coloneqq -\sup(-A) \), since \( -t = \sup(-A) \).
:::

Now the axiom can be applied to \( -A \).

::: {#thm-greatest-lower-bound}
[Greatest Lower Bound Property]

Every **non-empty** subset \( A \) of \( \nR \) that is **bounded below** has an infimum in \( \nR \), and
\[
\inf A = -\sup(-A) .
\]
:::

::: {.proof}
Since \( A \) is non-empty, so is \( -A \). Let \( m \) be a lower bound of \( A \). By @thm-inf-neg-sup (a), \( -m \) is an upper bound of \( -A \), so \( -A \) is bounded above. By @ax-least-upper-bound, \( -A \) has a supremum, and by @thm-inf-neg-sup, \( A \) has the infimum \( -\sup(-A) \).
:::

Alternatively, one can take the supremum of the lower bounds. Let \( L \) be the set of lower bounds of \( A \). It is non-empty, because \( A \) is bounded below, and any element of \( A \), of which there is at least one because \( A \) is non-empty, sits above all of \( L \). So \( \ell \coloneqq \sup L \) exists by @ax-least-upper-bound. Each \( a \in A \) is an upper bound of \( L \), so \( \ell \le a \) by (S2); hence \( \ell \) is a lower bound of \( A \). And every lower bound of \( A \) lies in \( L \), so it is at most \( \ell \) by (S1). Thus \( \ell = \inf A \). In this route the two hypotheses on \( A \) swap roles: "bounded below" makes \( L \) non-empty, and "non-empty" makes \( L \) bounded above.

The hypotheses of @thm-greatest-lower-bound are needed for the same reasons as those of the axiom. The empty set is bounded below and has no infimum, since every real number is a lower bound of it and \( t + 1 \) beats any candidate \( t \). The interval \( (-\infty, 0] \) is non-empty but not bounded below, and has no infimum.

So in \( \nR \), suprema and infima exist under mirror-image hypotheses, and each can be computed from the other. The mirror identity \( \sup A = -\inf(-A) \), for \( A \) non-empty and bounded above, is @exr-the-axiom-b1.

## Unbounded and empty sets

It is sometimes convenient to give \( \sup A \) a meaning even when the axiom does not apply. For a non-empty set \( A \) that is not bounded above one writes \( \sup A = +\infty \), and one sets \( \sup \emptyset = -\infty \); symmetrically, \( \inf A = -\infty \) for a non-empty set not bounded below, and \( \inf \emptyset = +\infty \). The strange-looking value \( \sup \emptyset = -\infty \) is chosen so that "\( A \subseteq B \) implies \( \sup A \le \sup B \)" stays true when \( A = \emptyset \).

::: {.remark}
These are conventions of notation, and \( \pm\infty \) are **not** real numbers: they obey none of the field axioms, and no rule of @thm-ordered-field-rules applies to them. The book uses them from Part IV on, where measure theory needs suprema of arbitrary sets, and announces them again there. Until then, whenever we write \( \sup A \), the set \( A \) is non-empty and bounded above, and \( \sup A \) is a real number.
:::

## What the axiom will do

With the axiom in place, the rest of the chapter extracts its first consequences: a practical test for recognizing a supremum, the Archimedean property, the density of the rationals, the existence of roots, and the nested interval property. Each of them fails in \( \nQ \) or in some other ordered field, and each is proved by the same pattern: define a set, check the two hypotheses, take its supremum, and extract what is needed from (S1) and (S2).

## Exercises

### A. Check your understanding

::: {#exr-the-axiom-a1}
[A1]

For each set, decide whether it satisfies both hypotheses of @ax-least-upper-bound. If a hypothesis fails, name it; if both hold, find the supremum.

::: {.enumerate options="label=(\alph*)"}
1. \( \{ x \in \nR : x^2 < 0 \} \).
2. \( \{ x^2 : x \in \nR \} \).
3. \( (-\infty, 0) \).
4. \( \{ x \in \nQ : x > 0, \ x^2 < 2 \} \), regarded as a subset of the ordered field \( \nQ \).
:::
:::

::: {.solution}
(a) The set is empty, since \( x^2 \ge 0 \) for every \( x \) (@thm-ordered-field-rules (e)). "Non-empty" fails.

(b) "Bounded above" fails. Given \( M \in \nR \), let \( x \coloneqq \abs{M} + 1 \). Then \( x \ge 1 \), so \( x^2 \ge x \) (multiply \( x \ge 1 \) by \( x > 0 \)), and \( x > \abs{M} \ge M \). Hence \( x^2 > M \), and \( M \) is not an upper bound.

(c) Both hold: \( -1 \) is an element and \( 0 \) is an upper bound. The supremum is \( 0 \): it is an upper bound, and if \( M < 0 \) were an upper bound, then \( M \ge -1 \) and the midpoint \( \frac{M}{2} \) would satisfy \( M < \frac{M}{2} < 0 \), so it lies in the set and exceeds \( M \).

(d) Both hypotheses hold in \( \nQ \) (@thm-no-rational-sup-sqrt2), but the axiom is a statement about \( \nR \), not about \( \nQ \). In \( \nQ \) the conclusion fails: the set has no supremum in \( \nQ \), by the same theorem. This is exactly why \( \nQ \) does not satisfy the axiom.
:::

### B. Practice

::: {#exr-the-axiom-b1}
[B1: The mirror identity]

Let \( A \subseteq \nR \) be non-empty and bounded above. Show that \( -A \) has a lower bound, and that \( \sup A = -\inf(-A) \).
:::

::: {.solution}
Since \( A \) is non-empty, so is \( -A \). Let \( M \) be an upper bound of \( A \). For every \( x \in -A \) we have \( -x \in A \), so \( -x \le M \), and hence \( -M \le x \) by @thm-ordered-field-rules (a). So \( -M \) is a lower bound of \( -A \), and \( -A \) is bounded below. By @thm-greatest-lower-bound, \( \inf(-A) \) exists and equals \( -\sup(-(-A)) = -\sup A \), because \( -(-A) = A \). Negating both sides gives \( \sup A = -\inf(-A) \).
:::

::: {#exr-the-axiom-b2}
[B2: The infimum is below the supremum]

Let \( A \subseteq \nR \) be non-empty and bounded. Prove that \( \inf A \le \sup A \), with equality if and only if \( A \) has exactly one element.
:::

::: {.solution}
Both exist, by @ax-least-upper-bound and @thm-greatest-lower-bound. Since \( A \) is non-empty, choose \( a \in A \). By (I1), \( \inf A \le a \), and by (S1), \( a \le \sup A \). Hence \( \inf A \le \sup A \).

If \( A = \{ a \} \), then \( a \) is both the maximum and the minimum of \( A \), so \( \sup A = a = \inf A \) by @exr-suprema-b1. Conversely, suppose \( \inf A = \sup A = c \). For every \( a \in A \), \( c \le a \le c \), so \( a = c \) by trichotomy. Hence \( A \subseteq \{ c \} \), and since \( A \) is non-empty, \( A = \{ c \} \).
:::

### C. Going deeper

::: {#exr-the-axiom-c1}
[C1: The axiom in other ordered fields]

::: {.enumerate options="label=(\alph*)"}
1. Say what it would mean for the ordered field \( \nQ \) to satisfy the least upper bound property, and show that it does not. Is @thm-no-rational-sup-sqrt2 exactly a witness, or does it need to be adapted?
2. Say that an ordered field \( F \) has the **greatest lower bound property** if every non-empty subset of \( F \) that is bounded below has an infimum in \( F \). Prove that if \( F \) has the greatest lower bound property, then it has the least upper bound property.
3. Conclude that, for an ordered field, the two properties are equivalent.
:::
:::

::: {.solution}
(a) \( \nQ \) would satisfy it if every non-empty subset of \( \nQ \) that is bounded above in \( \nQ \) had a supremum in \( \nQ \). @thm-no-rational-sup-sqrt2 is exactly a witness that it does not: its set is a subset of \( \nQ \), non-empty, bounded above by the rational \( 2 \), and has no supremum in \( \nQ \). Nothing needs adapting, because the theorem was stated and proved inside the ordered field \( \nQ \), with the upper bounds in (S2) ranging over \( \nQ \).

(b) Let \( A \subseteq F \) be non-empty and bounded above, with upper bound \( M \). Then \( -A \) is non-empty, and it is bounded below by \( -M \), by @thm-inf-neg-sup (a) applied with \( m = -M \) and the set \( -A \) in place of \( A \) (so that \( -(-A) = A \)). By the greatest lower bound property, \( -A \) has an infimum \( t \) in \( F \). By @thm-inf-neg-sup (b), applied to the set \( -A \), \( -t \) is a supremum of \( -(-A) = A \). So \( A \) has a supremum in \( F \).

(c) The converse direction is the proof of @thm-greatest-lower-bound, which used only @thm-inf-neg-sup (valid in every ordered field) and the least upper bound property. So in any ordered field each property implies the other.
:::

::: {#exr-the-axiom-c2}
[C2: The upper bounds form a ray]

::: {.enumerate options="label=(\alph*)"}
1. Let \( A \subseteq \nR \) be non-empty and bounded above, and let \( U(A) \) be its set of upper bounds. Prove that \( U(A) = [\sup A, \infty) \).
2. Let \( B = \{ x \in \nQ : x > 0, \ x^2 < 2 \} \), and let \( U \) be its set of upper bounds **in \( \nQ \)**. Prove that there is no rational \( q \) with \( U = \{ u \in \nQ : u \ge q \} \).
3. Explain in one sentence how (a) and (b) restate the difference between \( \nR \) and \( \nQ \).
:::
:::

::: {.solution}
(a) (\( \subseteq \)) If \( M \in U(A) \), then \( \sup A \le M \) by (S2), so \( M \in [\sup A, \infty) \). (\( \supseteq \)) If \( M \ge \sup A \), then for every \( a \in A \), \( a \le \sup A \le M \) by (S1), so \( M \in U(A) \).

(b) Suppose \( U = \{ u \in \nQ : u \ge q \} \) for some rational \( q \). Then \( q \in U \), and \( q \le u \) for every \( u \in U \). So \( q \) is the minimum of \( U \), that is, a rational upper bound of \( B \) below every other rational upper bound. That makes \( q \) a supremum of \( B \) in \( \nQ \), which contradicts @thm-no-rational-sup-sqrt2.

(c) In \( \nR \) the upper bounds of a non-empty bounded-above set always form a closed ray that starts at a point, while in \( \nQ \) they can form a ray whose starting point is missing.
:::

<!-- dependency ledger
ax-least-upper-bound (example): an integer greater than 3 is at least 4 (Quick check on the integers up to 3.5) | arithmetic of Z, ch06 (promised); prose pointer in the text
thm-greatest-lower-bound (proof): A non-empty implies -A non-empty | inline (a in A gives -a in -A)
exr-the-axiom-a1 (solution): x >= 1 and x > 0 give x^2 >= x; |M| >= M | thm-ordered-field-rules (c), prp-absolute-value-rules (c); shown inline
-->
