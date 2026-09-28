# Working with the Supremum

The least upper bound axiom (@ax-least-upper-bound) tells us that suprema exist. To use a supremum, or to recognize one, we need a handle on its second property. As defined (@def-supremum), (S2) quantifies over **all** upper bounds of the set, and in practice there is no way to list them. This section replaces (S2) by an equivalent statement quantified over small positive numbers \( \varepsilon \), which can be checked by exhibiting elements. With it we prove the rules for computing suprema of scaled sets and of sums of sets, and meet the first \( \varepsilon/2 \) argument of the book.

## The epsilon characterization

Look back at how (S2) was verified for \( (0, 1) \) in @exm-sup-open-interval. We supposed that some \( M < 1 \) was an upper bound and then produced an element of the set above \( M \). Writing \( M = 1 - \varepsilon \), the argument really showed: for every \( \varepsilon > 0 \), some element of the set exceeds \( 1 - \varepsilon \). That is a statement about elements of the set, not about upper bounds, and it is exactly equivalent to (S2).

*A supremum is an upper bound that the set comes arbitrarily close to.*

::: {#thm-sup-epsilon}
[Epsilon Characterization of the Supremum]

Let \( A \subseteq \nR \) and let \( s \in \nR \) be an upper bound of \( A \). Then \( s = \sup A \) if and only if **for every** \( \varepsilon > 0 \) **there exists** \( a \in A \) with \( a > s - \varepsilon \).
:::

In symbols, for an upper bound \( s \) of \( A \):
\[
s = \sup A
\quad\iff\quad
\forall \varepsilon > 0 \ \ \exists a \in A : \ s - \varepsilon < a \ (\le s) .
\]
The part in parentheses is automatic, since \( s \) is an upper bound; it is written to show where \( a \) lies.

\begin{center}
\begin{tikzpicture}[scale=1.0]
  \draw[->] (-0.4,0) -- (8.2,0);
  \draw[line width=2.4pt] (0.5,0) -- (6,0);
  \node[above] at (2.2,0.2) {$A$};
  \draw (6,0.15) -- (6,-0.15);
  \node[below] at (6,-0.18) {$s$};
  \draw (4.4,0.15) -- (4.4,-0.15);
  \node[below] at (4.4,-0.18) {$s - \varepsilon$};
  \draw[pattern=north east lines] (4.4,-0.08) rectangle (6,0.5);
  \node[above] at (5.2,0.55) {band $(s-\varepsilon, s]$};
  \filldraw (5.3,0) circle (2.6pt);
  \node[below] at (5.3,-0.6) {$a$};
  \draw[->] (5.3,-0.62) -- (5.3,-0.15);
\end{tikzpicture}
\end{center}

::: {.idea}
Draw the band \( (s - \varepsilon, s] \) just below \( s \). The theorem says: \( s \) is the supremum exactly when every such band, however thin, contains a point of \( A \).

(\( \Rightarrow \)) The number \( s - \varepsilon \) is smaller than \( s \), so it cannot be an upper bound, by (S2). Not being an upper bound means precisely that some element of \( A \) lies above it.

(\( \Leftarrow \)) We need (S2): every upper bound \( M \) satisfies \( s \le M \). Suppose some upper bound \( M \) lies below \( s \). Then the band between \( M \) and \( s \) contains no point of \( A \), and the hypothesis says every band does. So the band of width \( s - M \), that is, the hypothesis with \( \varepsilon = s - M \), gives the contradiction.
:::

::: {.proof}
(\( \Rightarrow \)) Suppose \( s = \sup A \), and let \( \varepsilon > 0 \). Then \( s - \varepsilon < s \) by @thm-ordered-field-rules (a). If \( s - \varepsilon \) were an upper bound of \( A \), then (S2) would give \( s \le s - \varepsilon \), contradicting \( s - \varepsilon < s \) by trichotomy. So \( s - \varepsilon \) is not an upper bound of \( A \), which means there is \( a \in A \) with \( a > s - \varepsilon \).

(\( \Leftarrow \)) Suppose that for every \( \varepsilon > 0 \) there is \( a \in A \) with \( a > s - \varepsilon \). Since \( s \) is an upper bound of \( A \) by hypothesis, (S1) holds, and it remains to check (S2). Let \( M \) be an upper bound of \( A \), and suppose, for a contradiction, that \( M < s \). Put \( \varepsilon \coloneqq s - M \), which is positive by @thm-ordered-field-rules (a). By hypothesis there is \( a \in A \) with \( a > s - \varepsilon = M \). This contradicts \( M \) being an upper bound of \( A \). Hence \( s \le M \) by trichotomy, which is (S2). So \( s = \sup A \).
:::

The theorem does not use the axiom. It holds in any ordered field, and it **recognizes** a supremum; the axiom is what guarantees that there is one to recognize. The two halves are used differently. The forward direction is how a known supremum is **used**: it hands us elements of \( A \) as close to \( \sup A \) as we like. The backward direction is how a candidate is **confirmed**: it replaces "every upper bound is at least \( s \)" by "every band below \( s \) meets \( A \)", which can be checked by writing down an element.

::: {.remark}
The hypothesis "\( s \) is an upper bound" cannot be dropped. For \( A = (0, 1) \) and \( s = \frac12 \), every band \( (\frac12 - \varepsilon, \frac12] \) meets \( A \), yet \( \frac12 \) is not the supremum. The band condition alone says only that \( s \) is not too big; being an upper bound says it is not too small.
:::

The element \( a \) that the theorem produces **depends on \( \varepsilon \)**, as the order "\( \forall \varepsilon \ \exists a \)" allows. For \( A = (0, 1) \) and \( s = 1 \), the choice \( a \coloneqq \max \{ \frac12, 1 - \frac{\varepsilon}{2} \} \) works: it lies in \( (0, 1) \) and exceeds \( 1 - \varepsilon \). For \( \varepsilon = \frac1{10} \) it gives \( a = \frac{19}{20} \); for \( \varepsilon = \frac1{1000} \) it must be above \( \frac{999}{1000} \), and \( \frac{19}{20} \) no longer works. No single element of \( (0, 1) \) works for every \( \varepsilon \).

::: {.warning}
**The witness depends on \( \varepsilon \).** The theorem gives, **for each** \( \varepsilon \), **some** \( a \); it never gives one \( a \) that serves every \( \varepsilon \) at once. A proof that fixes \( a \) first and then says "for every \( \varepsilon > 0 \), \( a > s - \varepsilon \)" has swapped the quantifiers, and for \( (0, 1) \) it asserts something false. When you take a witness from the theorem, write "choose \( a \in A \) (depending on \( \varepsilon \)) with …".
:::

::: {.check}
Let \( s \) be an upper bound of a set \( A \subseteq \nR \). Compare
\[
\text{(i)} \ \ \forall \varepsilon > 0 \ \ \exists a \in A : a > s - \varepsilon
\qquad\text{and}\qquad
\text{(ii)} \ \ \exists a \in A \ \ \forall \varepsilon > 0 : a > s - \varepsilon .
\]
Statement (i) says \( s = \sup A \). What does (ii) say, and when is it true?
:::

::: {.solution}
Fix \( a \in A \). The condition "\( a > s - \varepsilon \) for every \( \varepsilon > 0 \)" forces \( a \ge s \): if \( a < s \), then \( \varepsilon \coloneqq s - a > 0 \) would give \( a > s - (s - a) = a \), which is absurd. Since \( s \) is an upper bound, also \( a \le s \), so \( a = s \). Conversely, if \( s \in A \), then \( a = s \) satisfies \( s > s - \varepsilon \) for every \( \varepsilon > 0 \).

So (ii) says exactly that \( s \in A \), that is, \( s \) is the **maximum** of \( A \). Swapping the quantifiers turned "supremum" into "maximum". For \( A = (0, 1) \) and \( s = 1 \), (i) is true and (ii) is false.
:::

Here is the theorem at work on a set where the witness must be found by a short computation. The Idea finds it backwards; the solution writes it forwards.

::: {#exm-sup-squares-epsilon}
[Confirming a supremum with epsilon]

Prove that \( \sup \{ x^2 : x \in (0, 1) \} = 1 \).
:::

::: {.solution}
*Idea.* The upper bound part is easy. For the band condition, fix \( \varepsilon > 0 \); we need \( x \in (0, 1) \) with \( x^2 > 1 - \varepsilon \). Try \( x = 1 - h \) with \( h > 0 \) small. Then \( x^2 = 1 - 2h + h^2 > 1 - 2h \), so it suffices that \( 1 - 2h \ge 1 - \varepsilon \), that is, \( h \le \frac{\varepsilon}{2} \). But we also need \( x \in (0, 1) \), that is, \( 0 < h < 1 \), and \( \frac{\varepsilon}{2} \) can be large. Capping it fixes this: take \( h = \min\{ \frac12, \frac{\varepsilon}{2} \} \).

*Proof.* Let \( A = \{ x^2 : x \in (0, 1) \} \). For \( x \in (0, 1) \), @thm-ordered-field-rules (g) gives \( x^2 < 1^2 = 1 \), so \( 1 \) is an upper bound of \( A \).

Let \( \varepsilon > 0 \), and let \( h \coloneqq \min\{ \frac12, \frac{\varepsilon}{2} \} \), which depends only on \( \varepsilon \). Then \( 0 < h \le \frac12 \), so \( x \coloneqq 1 - h \) lies in \( [\frac12, 1) \subseteq (0, 1) \), and \( x^2 \in A \). Since \( h > 0 \), \( h^2 > 0 \), and so
\[
x^2 = 1 - 2h + h^2 > 1 - 2h \ge 1 - \varepsilon ,
\]
where the last step uses \( h \le \frac{\varepsilon}{2} \). By @thm-sup-epsilon, \( \sup A = 1 \).
:::

The \( \frac12 \) in the minimum is arbitrary: any cap below \( 1 \) keeps \( x \) positive. What matters is that a constraint discovered late in the Idea (here \( h < 1 \)) is built into the constant from the start of the proof.

## Sup approximation

The forward direction of @thm-sup-epsilon is used so often with \( \varepsilon = \frac1n \) that it deserves its own statement.

::: {#cor-sup-approximation}
[Sup Approximation]

Let \( A \subseteq \nR \) be non-empty and bounded above. For every \( n \in \nN \) there is \( a_n \in A \) with
\[
\sup A - \frac1n < a_n \le \sup A .
\]
:::

::: {.proof}
By @ax-least-upper-bound, \( \sup A \) exists. Let \( n \in \nN \). Then \( n > 0 \), by the induction on \( n \) in @exm-sup-one-minus-reciprocal, and \( \frac1n > 0 \) by @thm-ordered-field-rules (f). By @thm-sup-epsilon (\( \Rightarrow \)) with \( \varepsilon = \frac1n \), there is \( a_n \in A \) with \( a_n > \sup A - \frac1n \), and \( a_n \le \sup A \) by (S1).
:::

The corollary gives, for each \( n \) separately, an element \( a_n \). Choosing one for every \( n \) at once, so as to form a sequence \( (a_n) \), is a use of the axiom of countable choice; we flag it and move on. Once limits are defined in Chapter 12, this says that \( \sup A \) is the limit of a sequence from \( A \). We call the move **sup approximation**: "\( \sup A - \frac1n \) is not an upper bound, so some \( a_n \in A \) exceeds it."

## Monotonicity and scaling

We now compute suprema of sets built from other sets. The first rule says that enlarging a set cannot lower its supremum.

::: {#thm-sup-monotone}
[Monotonicity of the Supremum]

Let \( A \subseteq B \subseteq \nR \), where \( A \) is non-empty and \( B \) is bounded above. Then \( \sup A \) and \( \sup B \) exist, and \( \sup A \le \sup B \).
:::

::: {.proof}
Since \( A \) is non-empty and \( A \subseteq B \), the set \( B \) is non-empty; as it is bounded above, \( \sup B \) exists by @ax-least-upper-bound. Every \( a \in A \) lies in \( B \), so \( a \le \sup B \) by (S1) for \( B \). Hence \( \sup B \) is an upper bound of \( A \). So \( A \) is non-empty and bounded above, \( \sup A \) exists by @ax-least-upper-bound, and \( \sup A \le \sup B \) by (S2) for \( A \).
:::

Strict inclusion does not give strict inequality: \( (0, 1) \subsetneq (0, 1] \), and both have supremum \( 1 \). The hypothesis that \( A \) is non-empty cannot be dropped, since \( \emptyset \subseteq B \) always and \( \emptyset \) has no supremum.

For scaling we need the scaled set. For \( A \subseteq \nR \) and \( c \in \nR \), let
\[
cA \coloneqq \{ ca : a \in A \} .
\]
For example \( 2(0, 1] = (0, 2] \) and \( (-1)A = -A \).

::: {#thm-sup-scaling}
[Scaling the Supremum]

Let \( A \subseteq \nR \) be non-empty and bounded above, and let \( c \in \nR \).

::: {.enumerate options="label=(\alph*)"}
1. If \( c > 0 \), then \( cA \) is non-empty and bounded above, and \( \sup(cA) = c \sup A \).
2. If \( c < 0 \), then \( cA \) is non-empty and bounded below, and \( \inf(cA) = c \sup A \).
:::
:::

::: {.idea}
For (a), prove the equality as two inequalities. Multiplying the inequality \( a \le \sup A \) by \( c > 0 \) shows that \( c \sup A \) is an upper bound of \( cA \), which gives \( \le \). For \( \ge \), undo the scaling: dividing by \( c \) turns an upper bound of \( cA \) into an upper bound of \( A \). No \( \varepsilon \) is needed, because multiplication by \( c > 0 \) is invertible and preserves order. For (b), a negative factor reverses order, so write \( c = -\abs{c} \) and let @thm-inf-neg-sup handle the sign.
:::

::: {.proof}
Let \( s \coloneqq \sup A \), which exists by @ax-least-upper-bound. Since \( A \) is non-empty, so is \( cA \).

(a) Let \( c > 0 \). For every \( a \in A \), \( a \le s \) by (S1), so \( ca \le cs \) by @thm-ordered-field-rules (c) (or trivially if \( a = s \)). Hence \( cs \) is an upper bound of \( cA \), so \( \sup(cA) \) exists by @ax-least-upper-bound, and \( t \coloneqq \sup(cA) \le cs \) by (S2).
For the reverse inequality, let \( a \in A \). Then \( ca \in cA \), so \( ca \le t \). Multiplying by \( \frac1c > 0 \) (@thm-ordered-field-rules (f) and (c)) gives \( a \le \frac{t}{c} \). Hence \( \frac tc \) is an upper bound of \( A \), and (S2) gives \( s \le \frac tc \). Multiplying by \( c > 0 \) gives \( cs \le t \). By trichotomy, \( \sup(cA) = cs \).

(b) Let \( c < 0 \), so \( -c > 0 \). The set \( -(cA) = \{ -ca : a \in A \} \) equals \( (-c)A \), which by (a) is non-empty and bounded above with \( \sup((-c)A) = -cs \). By @thm-inf-neg-sup (a), \( cA = -((-c)A) \) is bounded below, and by @thm-inf-neg-sup,
\[
\inf(cA) = -\sup\bigl( -(cA) \bigr) = -\sup\bigl( (-c)A \bigr) = -(-cs) = cs .
\]
This proves the theorem.
:::

For \( c = 0 \) the set \( cA \) is \( \{ 0 \} \), and \( \sup(0A) = 0 = 0 \cdot \sup A \) as well. Part (a) genuinely needs \( c > 0 \): with \( c = -1 \) and \( A = (0, 1] \), the set \( cA = [-1, 0) \) has supremum \( 0 \), not \( c \sup A = -1 \). Part (b) says what happens instead: a negative factor exchanges supremum and infimum, and indeed \( \inf [-1, 0) = -1 \).

## The supremum of a sum

For \( A, B \subseteq \nR \), let
\[
A + B \coloneqq \{ a + b : a \in A, \ b \in B \} .
\]
For instance \( (0, 1) + \{ 5 \} = (5, 6) \) and \( [0, 1] + [0, 2] = [0, 3] \). It is natural to expect \( \sup(A + B) = \sup A + \sup B \). This time the reverse inequality cannot be obtained by undoing an operation: a single element of \( A + B \) mixes one element of each set. We need the \( \varepsilon \) characterization.

::: {#thm-sup-sum}
[Supremum of a Sum]

Let \( A, B \subseteq \nR \) be non-empty and bounded above. Then \( A + B \) is non-empty and bounded above, and
\[
\sup(A + B) = \sup A + \sup B .
\]
:::

*Try it first (ten minutes): the inequality \( \le \) takes one line. Try to prove \( \ge \).*

::: {.idea}
The attempt that comes first to mind takes \( a = \sup A \) and \( b = \sup B \): then \( a + b \in A + B \), and (S1) for \( \sup(A + B) \) gives \( \ge \) at once. It fails because a supremum need not belong to its set: for \( A = B = (0, 1) \), the number \( 2 \) is not in \( A + B = (0, 2) \). (The last exercise of this section takes that attempt apart.) The repair is to use elements that are only **close** to the suprema, which is what @thm-sup-epsilon (\( \Rightarrow \)) supplies.

So we prove the equality as **two inequalities**.

(\( \le \)) Every \( a + b \) is at most \( \sup A + \sup B \), so the right side is an upper bound, and the supremum is at most any upper bound.

(\( \ge \)) Work backwards. To show that \( \sup(A + B) \) is at least \( \sup A + \sup B \), it suffices to find, for each \( \varepsilon > 0 \), an element of \( A + B \) above \( \sup A + \sup B - \varepsilon \). The natural candidate is \( a + b \) with \( a \) close to \( \sup A \) and \( b \) close to \( \sup B \). If \( a \) falls short of \( \sup A \) by less than \( \varepsilon/2 \), and \( b \) falls short of \( \sup B \) by less than \( \varepsilon/2 \), the total shortfall is less than \( \varepsilon \). So we split the budget \( \varepsilon \) into two halves, one for each set, and ask @thm-sup-epsilon for an element within \( \varepsilon/2 \) of each supremum. This is the **\( \varepsilon/2 \) argument**. The number \( \varepsilon/2 \) depends only on \( \varepsilon \); the elements \( a \) and \( b \) depend on \( \varepsilon \). *Before reading on: the proof asks for elements within \( \varepsilon/2 \) of each supremum. What would it give if it asked for \( \varepsilon \) instead, and would that still be enough?*
:::

::: {.proof}
By @ax-least-upper-bound, \( \sup A \) and \( \sup B \) exist. Choosing \( a_0 \in A \) and \( b_0 \in B \) gives \( a_0 + b_0 \in A + B \), so \( A + B \) is non-empty.

(\( \le \)) Let \( a \in A \) and \( b \in B \). By (S1), \( a \le \sup A \) and \( b \le \sup B \), so \( a + b \le \sup A + \sup B \) by @thm-ordered-field-rules (b). Hence \( \sup A + \sup B \) is an upper bound of \( A + B \). By @ax-least-upper-bound, \( \sup(A + B) \) exists, and by (S2), \( \sup(A + B) \le \sup A + \sup B \).

(\( \ge \)) Let \( \varepsilon > 0 \). Then \( \frac{\varepsilon}{2} > 0 \). By @thm-sup-epsilon (\( \Rightarrow \)), there are \( a \in A \) and \( b \in B \) (both depending on \( \varepsilon \)) with
\[
a > \sup A - \tfrac{\varepsilon}{2}
\quad\text{and}\quad
b > \sup B - \tfrac{\varepsilon}{2} .
\]
Adding, by @thm-ordered-field-rules (b), gives \( a + b > \sup A + \sup B - \varepsilon \). Since \( a + b \in A + B \), (S1) gives
\[
\sup(A + B) \ge a + b > \sup A + \sup B - \varepsilon .
\]
This holds for every \( \varepsilon > 0 \). If we had \( \sup(A + B) < \sup A + \sup B \), then the choice \( \varepsilon \coloneqq \sup A + \sup B - \sup(A + B) > 0 \) would give \( \sup(A + B) > \sup(A + B) \), which is absurd. Hence \( \sup(A + B) \ge \sup A + \sup B \).

The two inequalities and trichotomy give \( \sup(A + B) = \sup A + \sup B \).
:::

The answer to the prompt: with \( \varepsilon \) in place of \( \varepsilon/2 \) the proof gives \( \sup(A + B) > \sup A + \sup B - 2\varepsilon \) for every \( \varepsilon > 0 \), and that is still enough, since \( 2\varepsilon \) runs through all positive numbers as \( \varepsilon \) does. Halving is a convenience: it makes the final inequality come out with exactly \( \varepsilon \), which is the form @thm-sup-epsilon (\( \Leftarrow \)) asks for.

The halves of the proof use the two halves of the definition. The first inequality used only that each supremum is an upper bound (S1) and that \( \sup(A + B) \) is least (S2). The second used that each of \( \sup A \) and \( \sup B \) is least, in its \( \varepsilon \) form, and that \( \sup(A + B) \) is an upper bound. We call the pattern **equality by two inequalities**: prove \( \le \) by exhibiting an upper bound, and \( \ge \) with an \( \varepsilon \).

Every hypothesis is needed. If \( B = \emptyset \), then \( A + B = \emptyset \) has no supremum. If \( B \) is not bounded above, neither is \( A + B \) (@exr-epsilon-characterization-c2). And the analogous rule for differences is **not** \( \sup(A - B) = \sup A - \sup B \): the correct version subtracts an infimum (@exr-epsilon-characterization-b3).

::: {.warning}
**Proving one inequality only.** Here is a tempting "proof" of @thm-sup-sum: "For \( a \in A \) and \( b \in B \), \( a + b \le \sup A + \sup B \). Therefore \( \sup(A + B) = \sup A + \sup B \)." The first sentence proves only that \( \sup A + \sup B \) is **an** upper bound of \( A + B \), which gives \( \le \). It says nothing about being the **least** one: the same sentence with \( \sup A + \sup B + 1 \) is equally true, and would "prove" \( \sup(A + B) = \sup A + \sup B + 1 \). Whenever a supremum is claimed to equal something, both (S1) and (S2), or both inequalities, must appear.
:::

## Exercises

### A. Check your understanding

::: {#exr-epsilon-characterization-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Use @thm-sup-epsilon to confirm that \( \sup [0, 5) = 5 \). Give the witness \( a \) as a formula in \( \varepsilon \).
2. Use @thm-sup-epsilon to confirm that \( \sup \{ 3 \} = 3 \). Does your witness depend on \( \varepsilon \)? Why not?
3. Use @thm-sup-epsilon to confirm that \( \sup \bigl( (-1, 1) \cup (2, 4) \bigr) = 4 \).
4. Let \( s \) be an upper bound of \( A \). Write in symbols, using the \( \varepsilon \) characterization, the statement "\( s \) is **not** the supremum of \( A \)".
5. Run the (\( \ge \)) half of the proof of @thm-sup-sum on \( A = (0, 1) \), \( B = \{ 5 \} \) and \( \varepsilon = \frac1{10} \): give an \( a \) and a \( b \) the proof could use, and check the inequality it derives.
6. In the proof of @thm-sup-sum, which line can no longer be justified if \( B \) is allowed to be empty?
:::
:::

::: {.solution}
(a) \( 5 \) is an upper bound of \( [0, 5) \). Given \( \varepsilon > 0 \), let \( a \coloneqq \max\{ 0, 5 - \frac{\varepsilon}{2} \} \). Then \( a \ge 0 \), and \( a < 5 \) because both \( 0 \) and \( 5 - \frac{\varepsilon}{2} \) are less than \( 5 \); so \( a \in [0, 5) \). Also \( a \ge 5 - \frac{\varepsilon}{2} > 5 - \varepsilon \). By @thm-sup-epsilon, \( \sup [0, 5) = 5 \).

(b) \( 3 \) is an upper bound of \( \{ 3 \} \), and for every \( \varepsilon > 0 \) the element \( a = 3 \) satisfies \( 3 > 3 - \varepsilon \). The witness does not depend on \( \varepsilon \) because \( 3 \) belongs to the set: by the Quick check above, a single witness for all \( \varepsilon \) exists exactly when the supremum is a maximum.

(c) Every element is less than \( 4 \), so \( 4 \) is an upper bound. Given \( \varepsilon > 0 \), let \( a \coloneqq \max\{ 3, 4 - \frac{\varepsilon}{2} \} \). Then \( 3 \le a < 4 \), so \( a \in (2, 4) \), and \( a \ge 4 - \frac{\varepsilon}{2} > 4 - \varepsilon \). By @thm-sup-epsilon the supremum is \( 4 \).

(d) \( \exists \varepsilon > 0 \ \ \forall a \in A : a \le s - \varepsilon \). In words: some band below \( s \) contains no point of \( A \), so \( s - \varepsilon \) is a smaller upper bound.

(e) Here \( \sup A = 1 \), \( \sup B = 5 \) and \( \frac{\varepsilon}{2} = \frac1{20} \). The proof needs \( a \in (0, 1) \) with \( a > 1 - \frac1{20} = \frac{19}{20} \), for instance \( a = \frac{24}{25} \), and \( b \in B \) with \( b > 5 - \frac1{20} \), which forces \( b = 5 \). Then \( a + b = \frac{149}{25} = 5.96 > 5.9 = \sup A + \sup B - \varepsilon \). Any \( a \in (\frac{19}{20}, 1) \) works; the one \( b \) works for every \( \varepsilon \) because \( 5 \) is the maximum of \( B \).

(f) The first line, "By @ax-least-upper-bound, \( \sup A \) and \( \sup B \) exist". The axiom needs \( B \) non-empty, and \( \emptyset \) has no supremum. The line that chooses \( b \in B \) in the (\( \ge \)) half fails too, since there is nothing to choose.
:::

### B. Practice

::: {#exr-epsilon-characterization-b1}
[B1: A computed supremum]

Prove that \( \sup \{ x^2 : x \in (-1, 2) \} = 4 \). Hence show that the set has no maximum.
:::

::: {.solution}
Let \( A = \{ x^2 : x \in (-1, 2) \} \). *Upper bound.* Let \( x \in (-1, 2) \). If \( x \ge 0 \), then \( x < 2 \) gives \( x^2 < 4 \) by @thm-ordered-field-rules (g). If \( -1 < x < 0 \), then \( \abs{x} < 1 \) by @prp-absolute-value-rules (d), so \( x^2 = \abs{x}^2 < 1 < 4 \) by @thm-ordered-field-rules (g). So \( 4 \) is an upper bound, and \( 4 \notin A \).

*Band condition.* Working backwards as in @exm-sup-squares-epsilon: with \( x = 2 - h \) we have \( x^2 = 4 - 4h + h^2 > 4 - 4h \), so \( h \le \frac{\varepsilon}{4} \) suffices, provided \( 0 < h < 3 \) to keep \( x \in (-1, 2) \). So let \( \varepsilon > 0 \) and \( h \coloneqq \min\{ 1, \frac{\varepsilon}{4} \} \), which depends only on \( \varepsilon \). Then \( 0 < h \le 1 \), so \( x \coloneqq 2 - h \in [1, 2) \subseteq (-1, 2) \), and since \( h^2 > 0 \),
\[
x^2 = 4 - 4h + h^2 > 4 - 4h \ge 4 - \varepsilon .
\]
By @thm-sup-epsilon, \( \sup A = 4 \). Since \( 4 \notin A \), the set has no maximum, by @exr-suprema-b1 (a).
:::

::: {#exr-epsilon-characterization-b2}
[B2: Supremum of a union]

Let \( A, B \subseteq \nR \) be non-empty and bounded above. Prove that \( A \cup B \) is bounded above and \( \sup(A \cup B) = \max\{ \sup A, \sup B \} \).
:::

::: {.solution}
Let \( m \coloneqq \max\{ \sup A, \sup B \} \); both suprema exist by @ax-least-upper-bound. If \( x \in A \cup B \), then \( x \le \sup A \le m \) or \( x \le \sup B \le m \), so \( m \) is an upper bound of \( A \cup B \), which is non-empty. By symmetry we may assume \( m = \sup A \). Given \( \varepsilon > 0 \), @thm-sup-epsilon (\( \Rightarrow \)) gives \( a \in A \) with \( a > \sup A - \varepsilon = m - \varepsilon \), and \( a \in A \cup B \). By @thm-sup-epsilon (\( \Leftarrow \)), \( \sup(A \cup B) = m \).
:::

::: {#exr-epsilon-characterization-b3}
[B3: Supremum of a difference]

Let \( A \subseteq \nR \) be non-empty and bounded above, and \( B \subseteq \nR \) non-empty and bounded below. Prove that
\[
\sup \{ a - b : a \in A, \ b \in B \} = \sup A - \inf B .
\]
Give an example showing that the right side cannot be replaced by \( \sup A - \sup B \).
:::

::: {.solution}
The set in question is \( A + (-B) \). By @thm-inf-neg-sup (a), \( -B \) is bounded above, and it is non-empty. By @thm-greatest-lower-bound, \( \inf B = -\sup(-B) \), that is, \( \sup(-B) = -\inf B \). So @thm-sup-sum applies to \( A \) and \( -B \):
\[
\sup\bigl( A + (-B) \bigr) = \sup A + \sup(-B) = \sup A - \inf B .
\]
For the example, take \( A = \{ 0 \} \) and \( B = [0, 1] \). The differences \( 0 - b \) fill \( [-1, 0] \), whose supremum is \( 0 = \sup A - \inf B \), whereas \( \sup A - \sup B = -1 \).
:::

### C. Going deeper

::: {#exr-epsilon-characterization-c1}
[C1: Products of sets]

For \( A, B \subseteq \nR \) let \( AB \coloneqq \{ ab : a \in A, \ b \in B \} \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \sup(AB) = \sup A \cdot \sup B \) can fail for non-empty bounded sets \( A, B \).
2. Prove that it holds when \( A \) and \( B \) are non-empty, bounded above, and contained in \( (0, \infty) \).
:::

:::

::: {.solution}
[Hint 1]

For (a), try sets of negative numbers. For (b), the inequality \( \le \) is routine; for \( \ge \), fix one element \( b \in B \) and compare the set \( bA \) with \( AB \).
:::

::: {.solution}
[Hint 2]

For \( \ge \) in (b): fix \( b \in B \). Which theorem computes \( \sup(bA) \), and which compares the suprema of two sets, one inside the other? What does the inequality you get say about \( b \), once \( b \) varies?
:::

::: {.solution}
(a) Take \( A = B = [-2, -1] \). Then \( \sup A \cdot \sup B = (-1)(-1) = 1 \), but \( 4 = (-2)(-2) \in AB \), so \( \sup(AB) \ge 4 \ne 1 \) by (S1).

(b) Let \( s \coloneqq \sup A \) and \( t \coloneqq \sup B \), which exist by @ax-least-upper-bound. Since \( A \) contains a positive element and \( s \) is an upper bound, \( s > 0 \); likewise \( t > 0 \).

(\( \le \)) For \( a \in A \) and \( b \in B \), we have \( 0 < a \le s \) and \( 0 < b \le t \), so \( ab \le sb \le st \) by @thm-ordered-field-rules (c) (with trivial equality cases). So \( st \) is an upper bound of the non-empty set \( AB \), \( \sup(AB) \) exists, and \( \sup(AB) \le st \) by (S2).

(\( \ge \)) Fix \( b \in B \). Then \( bA \subseteq AB \) and \( b > 0 \), so @thm-sup-scaling and @thm-sup-monotone give \( bs = \sup(bA) \le \sup(AB) \). Multiplying by \( \frac1s > 0 \) gives \( b \le \frac{\sup(AB)}{s} \). As \( b \in B \) was arbitrary, \( \frac{\sup(AB)}{s} \) is an upper bound of \( B \), so \( t \le \frac{\sup(AB)}{s} \) by (S2), that is, \( st \le \sup(AB) \).

By trichotomy, \( \sup(AB) = st \). Positivity was used in (\( \le \)), to multiply inequalities, and in (\( \ge \)), to scale by \( b \) and divide by \( s \); part (a) shows it cannot be dropped.
:::

::: {#exr-epsilon-characterization-c2}
[C2: Exit check: sums of sets]

Let \( A, B \subseteq \nR \) be non-empty.

::: {.enumerate options="label=(\alph*)"}
1. Assume \( A \) and \( B \) are bounded above. Without looking back, prove \( \sup(A + B) = \sup A + \sup B \). This time, instead of proving \( \ge \) separately, show that \( \sup A + \sup B \) satisfies both hypotheses of @thm-sup-epsilon for the set \( A + B \).
2. Assume \( A \) and \( B \) are bounded below. State and prove the corresponding formula for \( \inf(A + B) \).
3. Show that if \( B \) is not bounded above, then neither is \( A + B \).
:::
:::

::: {.solution}
(a) Let \( s \coloneqq \sup A + \sup B \), where both suprema exist by @ax-least-upper-bound. *Upper bound:* for \( a \in A \), \( b \in B \), (S1) and @thm-ordered-field-rules (b) give \( a + b \le s \). *Band condition:* let \( \varepsilon > 0 \); then \( \frac{\varepsilon}{2} > 0 \), and @thm-sup-epsilon (\( \Rightarrow \)) gives \( a \in A \) and \( b \in B \), depending on \( \varepsilon \), with \( a > \sup A - \frac{\varepsilon}{2} \) and \( b > \sup B - \frac{\varepsilon}{2} \). Adding, \( a + b > s - \varepsilon \), and \( a + b \in A + B \). By @thm-sup-epsilon (\( \Leftarrow \)), \( s = \sup(A + B) \).

(b) \( \inf(A + B) = \inf A + \inf B \). Indeed \( -(A + B) = (-A) + (-B) \), since \( -(a + b) = (-a) + (-b) \). By @thm-inf-neg-sup (a), \( -A \) and \( -B \) are non-empty and bounded above, so (a) and @thm-greatest-lower-bound give
\[
\begin{aligned}
\inf(A + B) &= -\sup\bigl( (-A) + (-B) \bigr) \\
&= -\sup(-A) - \sup(-B) = \inf A + \inf B .
\end{aligned}
\]
Here \( A + B \) is bounded below because \( -(A + B) \) is bounded above, by (a) and @thm-inf-neg-sup (a).

(c) Fix \( a_0 \in A \) and let \( M \in \nR \). Since \( B \) is not bounded above, \( M - a_0 \) is not an upper bound of \( B \), so some \( b \in B \) has \( b > M - a_0 \). Then \( a_0 + b \in A + B \) and \( a_0 + b > M \). As \( M \) was arbitrary, \( A + B \) is not bounded above.

**Marking scheme.** (10 points)
- 1: (a) says why \( \sup A \), \( \sup B \) exist and why \( A + B \) is non-empty.
- 2: (a) shows \( \sup A + \sup B \) is an upper bound of \( A + B \), adding the two (S1) inequalities.
- 3: (a) fixes an arbitrary \( \varepsilon > 0 \), obtains \( a \in A \) and \( b \in B \), **depending on \( \varepsilon \)**, within \( \varepsilon/2 \) of their suprema, and concludes with @thm-sup-epsilon (\( \Leftarrow \)).
- 2: (b) reduces to (a) through \( -(A + B) = (-A) + (-B) \) and @thm-greatest-lower-bound, including why \( A + B \) is bounded below.
- 2: (c) produces, for an arbitrary \( M \), an element of \( A + B \) above \( M \).
Fatal errors (0 for the step): taking \( a = \sup A \in A \); choosing one \( a \) before \( \varepsilon \) is fixed; proving only \( \le \) in (a).
A solution of (a) that proves \( \le \) and \( \ge \) separately, as in @thm-sup-sum, earns the 5 points of the second and third lines if the \( \ge \) half is complete. A solution of (b) that repeats the argument of (a) with lower bounds earns the (b) points.
:::

::: {#exr-epsilon-characterization-c3}
[C3: Find the wrong line]

Each "proof" below contains a line that is false in general. Find it, give a set for which it fails, and decide whether the claim itself is true.

::: {.enumerate options="label=(\alph*)"}
1. *Claim.* If \( A \subseteq \nR \) is non-empty and bounded above and \( a < 1 \) for every \( a \in A \), then \( \sup A < 1 \). *"Proof."* (1) Let \( s = \sup A \). (2) Since \( s \in A \), the hypothesis gives \( s < 1 \). (3) Hence \( \sup A < 1 \).
2. *Claim.* If \( A, B \subseteq \nR \) are non-empty and bounded above, then \( \sup(A + B) \ge \sup A + \sup B \). *"Proof."* (1) Let \( a = \sup A \) and \( b = \sup B \). (2) Then \( a \in A \) and \( b \in B \), so \( a + b \in A + B \). (3) By (S1), \( a + b \le \sup(A + B) \), which is the claim.
:::
:::

::: {.solution}
(a) Line (2) is wrong: it assumes \( \sup A \in A \), which fails for \( A = (0, 1) \), where \( \sup A = 1 \notin A \). For that set the claim is **false**: every element is less than \( 1 \), and \( \sup A = 1 \not< 1 \). The correct conclusion is \( \sup A \le 1 \), which follows from (S2) because \( 1 \) is an upper bound.

(b) Line (2) is wrong for the same reason: for \( A = B = (0, 1) \), neither supremum belongs to its set, so \( a + b = 2 \) need not lie in \( A + B = (0, 2) \), and here it does not. The claim is **true**, since it is half of @thm-sup-sum, but this argument does not prove it; a correct argument for this inequality is the \( \varepsilon/2 \) argument in the proof of @thm-sup-sum. The flawed line is valid exactly when \( A \) and \( B \) have maxima, which is the situation the author of the "proof" silently imagined.
:::

<!-- dependency ledger
exm-sup-squares-epsilon (solution): min{1/2, eps/2} is at most each of 1/2 and eps/2, and is positive | def-maximum (minimum of a two-element set), existence by trichotomy (O1)
cor-sup-approximation (proof): choosing a_n for every n at once is countable choice | flagged in the prose after the proof; the corollary itself makes one choice per n and needs no choice principle
exr-epsilon-characterization-a1 (solution): 24/25 > 19/20 and 24/25 + 5 = 149/25 | arithmetic, shown inline
exr-epsilon-characterization-b2 (solution): max{sup A, sup B} is one of the two, so "by symmetry" covers both cases | def-maximum and trichotomy (O1)
exr-epsilon-characterization-c3 (solution): A + B = (0, 2) for A = B = (0, 1) | inline (only 2 not in (0, 2) is used, since every element of A + B is < 2)
-->
