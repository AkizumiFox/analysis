# Upper Bounds, Maxima and Suprema

The previous section ended with a puzzle. The rationals and the reals obey the same rules of arithmetic and the same rules of order (@def-ordered-field), yet \( x^2 - 2 \) has a zero in one (as @thm-sqrt2-exists will prove) and not in the other. The difference lies in how **sets** of numbers behave: in \( \nQ \), a set can press against a point that is not there. This section builds the vocabulary to say that precisely. Everything happens in an arbitrary ordered field \( F \), because we need to compare \( F = \nQ \) with \( F = \nR \), and the definitions must not already take a side.

## A largest element that is not there

Ask for the largest element of the open interval \( (0, 1) \) in \( \nR \). There is none. Whatever \( a \in (0, 1) \) you propose, the midpoint \( \frac{a + 1}{2} \) lies strictly between \( a \) and \( 1 \) by @thm-ordered-field-rules (h), so it belongs to \( (0, 1) \) and beats \( a \). The same happens, less visibly, for the set of positive rationals whose square is less than \( 2 \); Case 1 of the proof at the end of this section is the reason, and @exr-suprema-c1 writes it out.

And yet both sets are heading somewhere. The interval \( (0, 1) \) is pressed against \( 1 \): nothing in it reaches \( 1 \), and nothing smaller than \( 1 \) stays above it. "Largest element" is the wrong notion, because it demands that the target belong to the set. What survives is the smallest number that sits above the whole set. To define it we first need words for "sits above".

## Upper and lower bounds

::: {#def-upper-bound}
[Upper and Lower Bounds]

Let \( F \) be an ordered field and \( A \subseteq F \). An element \( M \in F \) is an **upper bound** of \( A \) if \( a \le M \) **for every** \( a \in A \). An element \( m \in F \) is a **lower bound** of \( A \) if \( m \le a \) **for every** \( a \in A \).
:::

In symbols, \( M \) is an upper bound of \( A \) when
\[
\forall a \in A : \ a \le M .
\]
The bound is an element of \( F \), and nothing requires it to belong to \( A \).

For the interval \( (0, 1) \) in \( \nR \), the numbers \( 1 \), \( \frac32 \), and \( 2026 \) are all upper bounds, and \( 0 \) and \( -17 \) are lower bounds. Upper bounds are never unique: if \( M \) is one, so is every \( M' \ge M \), by transitivity. A minimal change gives a nonexample: \( \frac12 \) is **not** an upper bound of \( (0, 1) \), because \( \frac34 \in (0, 1) \) and \( \frac34 > \frac12 \). One element above \( M \) is enough to spoil it. Negating the definition quantifier by quantifier (the negation rules are the subject of *Logic and Proof*, Chapter 6),
\[
M \text{ is not an upper bound of } A
\quad\iff\quad
\exists a \in A : \ a > M ,
\]
where we have used trichotomy to rewrite "not \( a \le M \)" as "\( a > M \)".

The empty set is the degenerate case, and it will matter. **Every** \( M \in F \) is an upper bound of \( \emptyset \): the condition "\( a \le M \) for every \( a \in \emptyset \)" has no instances to check, so it holds vacuously. Instance by instance it is the implication "if \( a \in \emptyset \), then \( a \le M \)", whose hypothesis is false, and @fd1:prp-vacuous-implication derives an implication from the negation of its hypothesis. Likewise every element of \( F \) is a lower bound of \( \emptyset \).

::: {#def-bounded-above}
[Bounded Sets]

Let \( F \) be an ordered field and \( A \subseteq F \). The set \( A \) is **bounded above** if it has **at least one** upper bound, **bounded below** if it has at least one lower bound, and **bounded** if it is both bounded above and bounded below.
:::

In symbols, \( A \) is bounded above when
\[
\exists M \in F \ \ \forall a \in A : \ a \le M .
\]
The order of the quantifiers carries the meaning. **One** \( M \) is chosen first and must then work **for every** \( a \). Swap them, to "\( \forall a \in A \ \exists M \in F : a \le M \)", and the statement becomes empty of content: every set satisfies it, since each \( a \) can take \( M = a \).

Examples in \( \nR \): the interval \( (0, 1) \) is bounded; the empty set is bounded (by anything); the interval \( [0, \infty) \) is bounded below by \( 0 \) but **not** bounded above. To see the last claim, negate the definition: we must show that for every \( M \in \nR \) there is \( a \in [0, \infty) \) with \( a > M \). Given \( M \), the element \( a \coloneqq \max\{ M, 0 \} + 1 \) works, where \( \max\{ M, 0 \} \) is the larger of \( M \) and \( 0 \) (maxima are defined in general just below): it is at least \( 1 > 0 \), so it lies in \( [0, \infty) \), and it exceeds \( M \) by (O3). The witness \( a \) depends on \( M \), as the order \( \forall M \ \exists a \) allows.

Whether \( \nN \) is bounded above in \( \nR \) looks like the same kind of question, but it is not. The answer, "no", is the Archimedean property, and it is proved later in this chapter from the axiom of the next section. It cannot be proved from the ordered-field axioms alone.

## Maximum and minimum

::: {#def-maximum}
[Maximum and Minimum]

Let \( F \) be an ordered field and \( A \subseteq F \). An element \( m \) is a **maximum** (or greatest element) of \( A \) if \( m \in A \) **and** \( m \) is an upper bound of \( A \). It is a **minimum** (or least element) of \( A \) if \( m \in A \) **and** \( m \) is a lower bound of \( A \).
:::

A set has at most one maximum. If \( m \) and \( m' \) are both maxima, then \( m \in A \) and \( m' \) is an upper bound, so \( m \le m' \); by the same argument with the roles swapped, \( m' \le m \); and trichotomy forces \( m = m' \). So when it exists we may write \( \max A \), and likewise \( \min A \).

Examples: the set \( \{ -1, 3, \frac72 \} \) has maximum \( \frac72 \), since \( \frac72 \) is in the set and \( -1 \le \frac72 \), \( 3 \le \frac72 \), \( \frac72 \le \frac72 \). The interval \( (0, 1] \) has maximum \( 1 \). The minimal change from \( (0, 1] \) to \( (0, 1) \) keeps every upper bound but removes the only candidate: \( (0, 1) \) has **no** maximum, as the opening subsection showed. The empty set has no maximum, since it has no elements at all.

## The supremum

Here is the notion that survives where "maximum" fails. Look again at \( (0, 1) \). Its upper bounds form the set \( [1, \infty) \), and **that** set has a least element, namely \( 1 \). The number we want is the least element of the set of upper bounds.

\begin{center}
\begin{tikzpicture}[scale=1.0]
  \draw[->] (-0.6,0) -- (7.4,0);
  \draw[line width=2.4pt] (0,0) -- (3,0);
  \draw[fill=white] (0,0) circle (2.6pt);
  \draw[fill=white] (3,0) circle (2.6pt);
  \node[below] at (0,-0.12) {$0$};
  \node[below] at (3,-0.12) {$1$};
  \node[above] at (1.5,0.18) {$A = (0,1)$};
  \draw[thick,-{Latex[length=2mm]}] (3,0.35) -- (3,0.6) -- (7.2,0.6);
  \node[above] at (5.1,0.62) {upper bounds of $A$: the set $[1,\infty)$};
  \draw[->] (3,-0.95) -- (3,-0.45);
  \node[below] at (3,-0.95) {$\sup A = 1$, the least upper bound, not in $A$};
\end{tikzpicture}
\end{center}

*The supremum is the upper bound that cannot be lowered.*

::: {#def-supremum}
[Supremum]

Let \( F \) be an ordered field and \( A \subseteq F \). An element \( s \in F \) is a **supremum** (or **least upper bound**) of \( A \) in \( F \) if

::: {.enumerate options="label=(S\arabic*)"}
1. \( s \) is an upper bound of \( A \), and
2. \( s \le M \) **for every** upper bound \( M \) of \( A \).
:::
:::

In symbols, \( s \) is a supremum of \( A \) in \( F \) when
\[
\bigl( \forall a \in A : \ a \le s \bigr)
\ \text{ and } \
\bigl( \forall M \in F : \ (\forall a \in A : a \le M) \Rightarrow s \le M \bigr).
\]

In words: (S1) says that \( s \) sits above the whole set. (S2) says that no upper bound sits below \( s \); every upper bound is at least \( s \). So \( s \) is an upper bound (S1), and it is the least one (S2). The words "in \( F \)" matter: \( s \) must be an element of \( F \), and the upper bounds \( M \) in (S2) range over \( F \). The same set of rationals can have a supremum when viewed in one field and none when viewed in another, and that is precisely the phenomenon this chapter is about.

Before we write "*the* supremum", we must know there cannot be two.

::: {#thm-sup-unique}
[Uniqueness of the Supremum]

Let \( F \) be an ordered field and \( A \subseteq F \). If \( s \) and \( s' \) are both suprema of \( A \) in \( F \), then \( s = s' \).
:::

::: {.proof}
By (S1) for \( s' \), the element \( s' \) is an upper bound of \( A \). So (S2) for \( s \) gives \( s \le s' \). Swapping the roles of \( s \) and \( s' \) gives \( s' \le s \). By trichotomy, \( s = s' \).
:::

The proof is the standard uniqueness move: suppose there are two, use the first property of one against the second property of the other, and then swap. From now on, when \( A \) has a supremum in \( F \), we call it **the** supremum and write \( \sup A \). Existence is a different matter, and nothing so far guarantees it. It can fail in three ways: the set may have no upper bound at all, like \( [0, \infty) \) above; it may have no elements; or it may press against a gap in the field. The rest of this section shows the last two.

The mirror-image notion comes with its own definition, since we use it as often.

::: {#def-infimum}
[Infimum]

Let \( F \) be an ordered field and \( A \subseteq F \). An element \( t \in F \) is an **infimum** (or **greatest lower bound**) of \( A \) in \( F \) if

::: {.enumerate options="label=(I\arabic*)"}
1. \( t \) is a lower bound of \( A \), and
2. \( M \le t \) **for every** lower bound \( M \) of \( A \).
:::
:::

The proof of @thm-sup-unique, with every inequality reversed, shows that a set has at most one infimum, written \( \inf A \). The names are Latin: *supremum* is "the highest", *infimum* "the lowest".

::: {#exm-sup-finite-and-closed}
[A finite set, and a half-open interval]

Find the supremum of \( A = \{ -1, 3, \frac72 \} \) and of \( B = (0, 1] \) in \( \nR \).
:::

::: {.solution}
For \( A \): the element \( \frac72 \) is an upper bound, as checked above, so (S1) holds. For (S2), let \( M \) be any upper bound of \( A \). Since \( \frac72 \in A \), the definition of upper bound gives \( \frac72 \le M \). So \( \sup A = \frac72 = \max A \).

For \( B \): the same two lines work with \( 1 \) in place of \( \frac72 \). It bounds \( (0, 1] \) from above by the definition of that interval, and it is least because \( 1 \in B \), so every upper bound \( M \) satisfies \( 1 \le M \). So \( \sup B = 1 = \max B \).

The argument used only that the candidate is a maximum. It shows that **a maximum, when it exists, is the supremum** (@exr-suprema-b1). Every nonempty finite set has a maximum, by an induction on the number of elements of the kind practiced in *Sets and Functions*, Chapters 3 and 4, so for finite sets the supremum is nothing new.
:::

::: {#exm-sup-open-interval}
[The supremum need not belong to the set]

Show that \( \sup (0, 1) = 1 \) in \( \nR \), although \( 1 \notin (0, 1) \).
:::

::: {.solution}
(S1): every \( a \in (0, 1) \) satisfies \( a < 1 \), so \( 1 \) is an upper bound.

(S2): let \( M \) be an upper bound of \( (0, 1) \); we show \( 1 \le M \). Suppose instead that \( M < 1 \). Since \( \frac12 \in (0, 1) \), we have \( \frac12 \le M \), so \( M > 0 \). By @thm-ordered-field-rules (h), the midpoint \( a \coloneqq \frac{M + 1}{2} \) satisfies \( M < a < 1 \). Then \( 0 < M < a < 1 \), so \( a \in (0, 1) \), and \( a > M \). This contradicts \( M \) being an upper bound. Hence \( 1 \le M \), by trichotomy.

So \( 1 \) is the supremum. It is not a maximum, since \( 1 \notin (0, 1) \). Nothing in the argument used anything beyond the ordered-field axioms; the same proof shows that \( \{ x \in \nQ : 0 < x < 1 \} \) has supremum \( 1 \) in \( \nQ \).
:::

::: {#exm-sup-one-minus-reciprocal}
[A supremum we cannot yet prove]

Let \( A = \{ 1 - \frac1n : n \in \nZ_{>0} \} = \{ 0, \frac12, \frac23, \frac34, \dots \} \) in \( \nR \), where \( \nZ_{>0} = \{ 1, 2, 3, \dots \} \) is the set of positive integers (taken informally for now; later in this chapter, once the natural numbers are defined inside \( \nR \), it becomes a defined subset of \( \nR \)). Show that \( 1 \) is an upper bound of \( A \) and that \( A \) has no maximum.
:::

::: {.solution}
Each \( n \in \nZ_{>0} \) is positive, so \( \frac1n > 0 \) by @thm-ordered-field-rules (f), and hence \( 1 - \frac1n < 1 \) by @thm-ordered-field-rules (a). So \( 1 \) is an upper bound, and \( 1 \notin A \). No element is a maximum either: \( 1 - \frac1n < 1 - \frac1{n + 1} \), because \( \frac1{n + 1} < \frac1n \) by @thm-ordered-field-rules (f), so every element is beaten by the next one.

It is true that \( \sup A = 1 \), but (S2) is harder than it looks. It says that no \( M < 1 \) is an upper bound, that is, for every \( M < 1 \) some \( 1 - \frac1n \) exceeds \( M \). That requires \( \frac1n < 1 - M \) for some \( n \). The existence of such an \( n \) says, in effect, that the natural numbers are not bounded above, and that does not follow from the ordered-field axioms. We prove it later in this chapter, from the axiom of the next section, and prove \( \sup A = 1 \) right after it.
:::

The degenerate case is the empty set. By the vacuous-truth remark above, every element of \( F \) is an upper bound of \( \emptyset \). If \( s \) were a supremum, then \( s - 1 \) would be an upper bound too, and (S2) would give \( s \le s - 1 \), that is, \( 1 \le 0 \), contradicting \( 1 > 0 \). So **the empty set has no supremum**, although it is bounded above. This is why the axiom of the next section has to say "nonempty".

A nonexample by minimal change shows why both clauses are needed. Keep \( A = (0, 1) \). The number \( 2 \) satisfies (S1) but fails (S2): the upper bound \( 1 \) lies below it. The number \( \frac12 \) satisfies (S2), since every upper bound is at least \( 1 \ge \frac12 \), but it fails (S1). Drop (S1) from the definition and every number below \( 1 \), such as \( \frac12 \) or \( -5 \), would qualify. Drop (S2) and every upper bound would. Only the two clauses together pin down a single number.

::: {.warning}
**The supremum is not the maximum.** The supremum of a set need not belong to the set: \( \sup (0, 1) = 1 \notin (0, 1) \). The two notions agree exactly when the supremum lies in the set (@exr-suprema-b1). A proof that writes "let \( a = \sup A \in A \)" has assumed something false in general; the section on working with the supremum contains a proof that fails for exactly this reason.
:::

::: {.warning}
**A bounded set need not have a maximum.** The interval \( (0, 1) \) is bounded, and it has no greatest element. "Bounded" promises upper bounds, which live outside the set; it promises nothing about the elements themselves.
:::

::: {.check}
Let \( A = \{ \frac{(-1)^n}{n} : n \in \nZ_{>0} \} = \{ -1, \frac12, -\frac13, \frac14, \dots \} \). Find \( \max A \) and \( \sup A \) in \( \nR \), if they exist. Do the same for \( \min A \) and \( \inf A \).
:::

::: {.solution}
For odd \( n \) the element is \( -\frac1n < 0 \). For even \( n \ge 2 \) it is \( \frac1n \le \frac12 \), by @thm-ordered-field-rules (f). So \( \frac12 \) is an upper bound, and it is attained at \( n = 2 \). Hence \( \max A = \frac12 \), and by the argument of @exm-sup-finite-and-closed (a maximum is the supremum), \( \sup A = \frac12 \).

Similarly, every element is at least \( -1 \): even-indexed ones are positive, and odd-indexed ones are \( -\frac1n \ge -1 \) because \( \frac1n \le 1 \). The value \( -1 \) is attained at \( n = 1 \). So \( \min A = \inf A = -1 \). Although \( A \) is infinite, both extremes are attained, at its first two elements.
:::

## A bounded set of rationals with no rational supremum

We now prove what the opening section promised: in \( \nQ \), a nonempty set that is bounded above can fail to have a supremum. This is the gap in \( \nQ \), expressed in the language of this section.

::: {#thm-no-rational-sup-sqrt2}
[No Rational Supremum for the Rationals Below the Square Root of Two]

Let \( A = \{ x \in \nQ : x > 0 \text{ and } x^2 < 2 \} \). Then \( A \) is nonempty and bounded above in \( \nQ \), but \( A \) has no supremum in \( \nQ \).
:::

::: {.idea}
Suppose a rational \( s \) were the supremum. By @fd1:thm-sqrt2-irrational, \( s^2 \ne 2 \), so \( s^2 < 2 \) or \( s^2 > 2 \), and each case is a disaster.

If \( s^2 < 2 \), then \( s \) is too small: there is room to step right to a rational \( s + h \) whose square is still below \( 2 \), and then \( s + h \in A \) beats \( s \). To find \( h \), work backwards from the goal \( (s + h)^2 < 2 \). Expanding, \( (s + h)^2 = s^2 + 2sh + h^2 \). The \( h^2 \) is awkward, so bound it by something simpler: **if \( 0 < h \le 1 \)**, then \( h^2 \le h \), and \( (s + h)^2 \le s^2 + h(2s + 1) \). The room available is \( 2 - s^2 \). Asking \( h(2s + 1) \) to use only half of it, \( h(2s + 1) = \frac{2 - s^2}{2} \), gives \( h = \frac{2 - s^2}{4s + 2} \). We then owe a check of the condition \( h \le 1 \) that we assumed along the way.

If \( s^2 > 2 \), then \( s \) is too big: step left to \( s - h \), still an upper bound, and then \( s \) was not the least one. Now \( (s - h)^2 = s^2 - 2sh + h^2 > s^2 - 2sh \), and the right side equals \( 2 \) exactly when \( h = \frac{s^2 - 2}{2s} \).

In both cases \( h \) depends only on \( s \), and it is rational because \( s \) is. *Before reading on: where does the proof use that \( s \) is rational, and where does it use @fd1:thm-sqrt2-irrational?*
:::

::: {.proof}
Since \( 1 > 0 \) and \( 1^2 = 1 < 2 \), we have \( 1 \in A \), so \( A \) is nonempty. The rational number \( 2 \) is an upper bound: if some \( x \in A \) had \( x > 2 \), then \( x^2 > 4 \) by @thm-ordered-field-rules (g), contradicting \( x^2 < 2 \), so \( x \le 2 \) by trichotomy.

Suppose, for a contradiction, that \( s \in \nQ \) is a supremum of \( A \) in \( \nQ \). Since \( 1 \in A \), (S1) gives \( s \ge 1 \); in particular \( s > 0 \), and \( s^2 \ge 1 \) by @thm-ordered-field-rules (g). By @fd1:thm-sqrt2-irrational, \( s^2 \ne 2 \), so by trichotomy either \( s^2 < 2 \) or \( s^2 > 2 \).

*Case 1: \( s^2 < 2 \).* Let
\[
h \coloneqq \frac{2 - s^2}{4s + 2} .
\]
Then \( h \in \nQ \), and \( h > 0 \) because \( 2 - s^2 > 0 \) and \( 4s + 2 > 0 \). Moreover \( h \le \frac16 \), since \( 2 - s^2 \le 1 \) (as \( s^2 \ge 1 \)) and \( 4s + 2 \ge 6 \) (as \( s \ge 1 \)). Hence \( h \le 1 \), and multiplying by \( h > 0 \) gives \( h^2 \le h \). Therefore
\[
\begin{aligned}
(s + h)^2 &= s^2 + 2sh + h^2 \\
&\le s^2 + h(2s + 1) \\
&= s^2 + \tfrac{2 - s^2}{2} = 1 + \tfrac{s^2}{2} < 2,
\end{aligned}
\]
where the last inequality holds because \( s^2 < 2 \). So \( s + h \) is a positive rational with square less than \( 2 \), that is, \( s + h \in A \). But \( s + h > s \), so \( s \) is not an upper bound of \( A \), contradicting (S1).

*Case 2: \( s^2 > 2 \).* Let
\[
h \coloneqq \frac{s^2 - 2}{2s} .
\]
Then \( h \in \nQ \) and \( h > 0 \). Also \( s - h = \frac{s^2 + 2}{2s} > 0 \), and
\[
(s - h)^2 = s^2 - 2sh + h^2 = s^2 - (s^2 - 2) + h^2 = 2 + h^2 > 2 .
\]
We claim that \( s - h \) is an upper bound of \( A \). Indeed, if some \( x \in A \) had \( x > s - h \), then, as \( s - h > 0 \), @thm-ordered-field-rules (g) would give \( x^2 > (s - h)^2 > 2 \), contradicting \( x^2 < 2 \). So \( s - h \) is a rational upper bound of \( A \) with \( s - h < s \), contradicting (S2).

Both cases are impossible. Hence \( A \) has no supremum in \( \nQ \). This proves the theorem.
:::

Rationality of \( s \) was used in exactly two places: to make \( h \), and so \( s \pm h \), rational, which is what membership in \( A \) and "upper bound in \( \nQ \)" require; and to rule out \( s^2 = 2 \) by @fd1:thm-sqrt2-irrational. The logical shape is the same as in the irrationality of \( \sqrt2 \): assume the object exists, reach a contradiction, conclude that it does not.

To see the constants at work, start from the rational upper bound \( s = \frac32 \), whose square \( \frac94 \) exceeds \( 2 \). Case 2 gives \( h = \frac{1}{12} \) and the smaller upper bound \( s - h = \frac{17}{12} \), with \( (\frac{17}{12})^2 = \frac{289}{144} = 2 + \frac{1}{144} \). Starting instead from \( s = 1 \in A \), Case 1 gives \( h = \frac16 \), and \( \frac76 \in A \) because \( \frac{49}{36} < 2 \). Each step can be repeated forever from either side, and no rational number is ever reached at which both processes stop.

This is the gap in \( \nQ \) in its final form. The next section adds to the ordered-field axioms the single statement that such gaps do not occur in \( \nR \). Later in the chapter, the same two-case argument, with \( s \) now a real number supplied by that axiom, proves that \( \sqrt 2 \) exists.

## Exercises

### A. Check your understanding

::: {#exr-suprema-a1}
[A1]

In (a)–(d), give the supremum, infimum, maximum, and minimum of the set in \( \nR \), or say that it does not exist. Justify each answer in a line or two. Parts (e) and (f) are about the proof of @thm-no-rational-sup-sqrt2.

::: {.enumerate options="label=(\alph*)"}
1. \( \{ -2, 0, \frac73 \} \).
2. \( [-1, 4) \).
3. \( \{ x \in \nR : x^2 \le 4 \} \).
4. \( \emptyset \).
5. Run Case 2 of the proof on the rational upper bound \( s = \frac{17}{12} \): compute \( h \) and \( s - h \), and check that \( (s - h)^2 > 2 \).
6. Replace \( \nQ \) by \( \nR \) throughout the statement and the proof. Which single step of the proof can no longer be justified, and what possibility does it leave open?
:::
:::

::: {.solution}
(a) \( \max = \sup = \frac73 \) and \( \min = \inf = -2 \): both are elements of the set, and comparing with the three elements shows they are an upper and a lower bound. A maximum is the supremum and a minimum is the infimum (@exr-suprema-b1).

(b) \( \min = \inf = -1 \), since \( -1 \) belongs to the set and is a lower bound. \( \sup = 4 \) and there is no maximum: \( 4 \) is an upper bound not in the set, and the midpoint argument of @exm-sup-open-interval shows that no \( M < 4 \) is an upper bound (if \( M < 4 \) is an upper bound, then \( M \ge -1 \) and \( \frac{M + 4}{2} \) is in the set and exceeds \( M \)).

(c) The set is \( [-2, 2] \): by @thm-ordered-field-rules (g) applied to \( \abs{x} \) and \( 2 \), and @prp-absolute-value-rules (b), \( x^2 \le 4 \) holds if and only if \( \abs{x} \le 2 \), which by @prp-absolute-value-rules (d) means \( -2 \le x \le 2 \). So \( \max = \sup = 2 \) and \( \min = \inf = -2 \).

(d) None of the four exists. Every real number is an upper and a lower bound of \( \emptyset \), so there is no least upper bound and no greatest lower bound (as shown in the text), and \( \emptyset \) has no elements to be a maximum or minimum.

(e) Here \( s^2 = \frac{289}{144} = 2 + \frac1{144} \), so
\[
h = \frac{s^2 - 2}{2s} = \frac{1/144}{17/6} = \frac{1}{408},
\qquad
s - h = \frac{17}{12} - \frac{1}{408} = \frac{577}{408} .
\]
Then \( (s - h)^2 = 2 + h^2 = 2 + \frac{1}{166464} > 2 \), as the proof's display predicts; directly, \( 577^2 = 332929 = 2 \cdot 408^2 + 1 \). So \( \frac{577}{408} \) is a smaller rational upper bound, and the step can be repeated from it.

(f) The step "by @fd1:thm-sqrt2-irrational, \( s^2 \ne 2 \)". Over \( \nR \) nothing rules out \( s^2 = 2 \), so after Cases 1 and 2 the possibility \( s^2 = 2 \) remains, and no contradiction is reached. Every other step is algebra valid in any ordered field, \( \nR \) included. This is exactly the opening that the existence proof for \( \sqrt2 \), later in this chapter, walks through.
:::

### B. Practice

::: {#exr-suprema-b1}
[B1: Maxima are suprema]

Let \( F \) be an ordered field and \( A \subseteq F \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( A \) has a maximum \( m \), then \( m \) is the supremum of \( A \).
2. Prove that if \( A \) has a supremum \( s \) and \( s \in A \), then \( s \) is the maximum of \( A \).
3. State and prove the corresponding facts for minimum and infimum.
:::
:::

::: {.solution}
(a) By @def-maximum, \( m \) is an upper bound of \( A \), which is (S1). For (S2), let \( M \) be any upper bound of \( A \). Since \( m \in A \), the definition of upper bound gives \( m \le M \). Hence \( m \) is a supremum of \( A \), and by @thm-sup-unique it is the supremum.

(b) By (S1), \( s \) is an upper bound of \( A \), and \( s \in A \) by hypothesis. That is exactly @def-maximum.

(c) If \( A \) has a minimum \( m \), then \( m = \inf A \); and if \( \inf A \) exists and belongs to \( A \), it is the minimum. The proofs are those of (a) and (b) with every inequality reversed: \( m \) is a lower bound (I1), and any lower bound \( M \) satisfies \( M \le m \) because \( m \in A \) (I2).
:::

::: {#exr-suprema-b2}
[B2: Negating the definitions]

Let \( F \) be an ordered field and \( A \subseteq F \).

::: {.enumerate options="label=(\alph*)"}
1. Write in symbols the statement "\( s \) is **not** an upper bound of \( A \)".
2. Write in symbols the statement "\( s \) is **not** a supremum of \( A \)", as a disjunction of two statements.
3. Use (b) to show directly that \( 2 \) is not the supremum of \( (0, 1) \) in \( \nR \), by exhibiting a witness.
:::
:::

::: {.solution}
(a) \( \exists a \in A : a > s \).

(b) Negating the conjunction (S1) and (S2) gives: (S1) fails or (S2) fails. So "\( s \) is not a supremum of \( A \)" is
\[
\bigl( \exists a \in A : a > s \bigr)
\ \text{ or } \
\bigl( \exists M \in F : (\forall a \in A : a \le M) \text{ and } M < s \bigr).
\]
The second disjunct says: some upper bound lies strictly below \( s \).

(c) The first disjunct fails for \( s = 2 \), since every element of \( (0, 1) \) is below \( 2 \). The second holds with the witness \( M = 1 \): it is an upper bound of \( (0, 1) \), and \( 1 < 2 \). Hence \( 2 \) is not the supremum.
:::

::: {#exr-suprema-b3}
[B3: A supremum that is approached but not attained]

Let \( A = \{ \frac{x}{x + 1} : x \in \nR, \ x > 0 \} \). Prove that \( \sup A = 1 \) and that \( A \) has no maximum.
:::

::: {.solution}
For \( x > 0 \), the denominator \( x + 1 \) is positive, and \( x < x + 1 \); multiplying by \( \frac{1}{x + 1} > 0 \) (@thm-ordered-field-rules (c) and (f)) gives \( \frac{x}{x + 1} < 1 \). So \( 1 \) is an upper bound (S1), and \( 1 \notin A \).

For (S2), let \( M \) be an upper bound of \( A \), and suppose \( M < 1 \). Since \( \frac12 = \frac{1}{1 + 1} \in A \), we have \( M \ge \frac12 > 0 \). Let \( x \coloneqq \frac{M}{1 - M} + 1 \), which is positive because \( M > 0 \) and \( 1 - M > 0 \). Then
\[
x(1 - M) = M + (1 - M) = 1 > M ,
\]
so \( x > Mx + M = M(x + 1) \), and dividing by \( x + 1 > 0 \) gives \( \frac{x}{x + 1} > M \). This element of \( A \) exceeds the upper bound \( M \), a contradiction. Hence \( M \ge 1 \) for every upper bound \( M \), and \( \sup A = 1 \). Finally, \( A \) has no maximum: by @exr-suprema-b1 (a), a maximum would be the supremum \( 1 \), but \( 1 \notin A \).

(The choice of \( x \) comes from solving \( \frac{x}{x + 1} > M \) backwards: it is equivalent to \( x(1 - M) > M \), that is, \( x > \frac{M}{1 - M} \), and adding \( 1 \) gives a strict margin.)
:::

### C. Going deeper

::: {#exr-suprema-c1}
[C1: The two sides of the gap]

::: {.enumerate options="label=(\alph*)"}
1. Give a set \( A \subseteq \nQ \) that is bounded above and has a supremum in \( \nQ \) that does not belong to \( A \).
2. Let \( B = \{ x \in \nQ : x > 0, \ x^2 < 2 \} \), and let \( U \) be the set of **rational** upper bounds of \( B \). Prove that \( U = \{ u \in \nQ : u > 0, \ u^2 > 2 \} \).
3. Deduce that every positive rational number lies in exactly one of \( B \) and \( U \), that \( B \) has no largest element, and that \( U \) has no smallest element.
:::

*Hint: the two cases in the proof of @thm-no-rational-sup-sqrt2 each produce a new rational from an old one.*
:::

::: {.solution}
(a) \( A = \{ x \in \nQ : 0 < x < 1 \} \). The argument of @exm-sup-open-interval works in the ordered field \( \nQ \), because the midpoint of two rationals is rational; it shows \( \sup A = 1 \) in \( \nQ \), and \( 1 \notin A \).

(b) (\( \subseteq \)) Let \( u \in U \). Since \( 1 \in B \), we get \( u \ge 1 > 0 \). By @fd1:thm-sqrt2-irrational, \( u^2 \ne 2 \). If \( u^2 < 2 \), then \( u \in B \), and Case 1 of the proof of @thm-no-rational-sup-sqrt2, applied to \( s = u \) (which used only \( s \in \nQ \), \( s \ge 1 \), and \( s^2 < 2 \)), produces \( u + h \in B \) with \( u + h > u \), contradicting \( u \in U \). Hence \( u^2 > 2 \).
(\( \supseteq \)) Let \( u \in \nQ \) with \( u > 0 \) and \( u^2 > 2 \). If some \( x \in B \) had \( x > u \), then \( x^2 > u^2 > 2 \) by @thm-ordered-field-rules (g), contradicting \( x^2 < 2 \). So \( u \) is an upper bound of \( B \), and \( u \in U \).

(c) Let \( q \in \nQ \) with \( q > 0 \). By @fd1:thm-sqrt2-irrational, \( q^2 \ne 2 \), so by trichotomy exactly one of \( q^2 < 2 \) and \( q^2 > 2 \) holds, that is, \( q \) lies in exactly one of \( B \) and \( U \), by (b). If \( B \) had a largest element \( b \), Case 1 of the proof (with \( s = b \), valid since \( b \ge 1 \) when \( b \) is largest, as \( 1 \in B \)) would give a larger element \( b + h \in B \). If \( U \) had a smallest element \( u \), Case 2 of the proof (with \( s = u \), which needs only \( s > 0 \), \( s \in \nQ \), and \( s^2 > 2 \)) would give \( u - h \in U \), smaller. So the positive rationals split into a lower piece with no top and an upper piece with no bottom. Nothing rational sits between the two pieces; that missing point is the gap.
:::

::: {#exr-suprema-c2}
[C2: The least element of the upper bounds]

Let \( F \) be an ordered field, \( A \subseteq F \), and let \( U(A) \) be the set of all upper bounds of \( A \) in \( F \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( s \) is a supremum of \( A \) if and only if \( s \) is the minimum of \( U(A) \). (This explains the name "least upper bound".)
2. Prove that if \( A \subseteq B \subseteq F \), then \( U(B) \subseteq U(A) \).
3. Describe \( U(\emptyset) \) and \( U(F) \), and use (a) to decide whether \( \emptyset \) and \( F \) have suprema.
:::
:::

::: {.solution}
(a) (\( \Rightarrow \)) If \( s \) is a supremum, then \( s \in U(A) \) by (S1), and \( s \le M \) for every \( M \in U(A) \) by (S2). So \( s \) is an element of \( U(A) \) and a lower bound of \( U(A) \), which is @def-maximum's definition of minimum.
(\( \Leftarrow \)) If \( s = \min U(A) \), then \( s \in U(A) \), which is (S1), and \( s \le M \) for every \( M \in U(A) \), which is (S2).

(b) Let \( M \in U(B) \). For every \( a \in A \) we have \( a \in B \), so \( a \le M \). Hence \( M \in U(A) \).

(c) \( U(\emptyset) = F \), since every element is an upper bound of the empty set vacuously; and \( F \) has no minimum, because \( m - 1 < m \) for every \( m \in F \). So \( \emptyset \) has no supremum. \( U(F) = \emptyset \), since for any \( M \) the element \( M + 1 \in F \) exceeds \( M \); and \( \emptyset \) has no minimum. So \( F \) has no supremum either. The two degenerate cases fail for opposite reasons: too many upper bounds, and none.
:::

<!-- dependency ledger
def-upper-bound (example): negating "for every a in A, a <= M" to "there exists a in A with a > M" | quantifier negation, F1.4 (promised); prose pointer in the text
def-bounded-above (example): max{M, 0} + 1 > M for every real M | thm-ordered-field-rules and (O3), shown inline
exm-sup-finite-and-closed (solution): every non-empty finite subset of an ordered field has a maximum | induction on the number of elements, F2.2 (promised); prose pointer in the text; not used in any proof
exm-sup-one-minus-reciprocal (solution): every n in Z_{>0} is positive | definition of Z_{>0} as the positive integers, stated inline
thm-no-rational-sup-sqrt2 (proof): Q is closed under the field operations, so h and s + h, s - h are rational | exm-ordered-fields-q-r
thm-no-rational-sup-sqrt2 (proof): the arithmetic of the two values of h ((s + h)^2 bound, (s - h)^2 = 2 + h^2) | inline; lem-field-algebra
exr-suprema-a1 (solution): 577^2 = 332929 = 2 * 408^2 + 1 | arithmetic, shown inline
exr-suprema-c1 (solution): the midpoint of two rationals is rational | exm-ordered-fields-q-r
-->
