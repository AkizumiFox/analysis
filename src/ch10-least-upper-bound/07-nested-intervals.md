# Nested Intervals and the Uncountability of the Reals

Each point we have built so far was a single supremum: the supremum of a set that "reaches toward" the point we want. This section builds points from a different kind of data, a sequence of closed intervals, each inside the one before. We prove that such intervals always have a point in common. In \( \nQ \) this fails, and so it is one more way of saying that \( \nR \) has no gaps. The payoff is a proof that the real numbers cannot be listed, one that uses no decimal expansions, only the axiom.

## Trapping a point

Here is a way to hunt for \( \sqrt{2} \) using nothing but rational arithmetic. Start with the interval \( [1, 2] \); since \( 1^2 < 2 < 2^2 \), the number we are after is in there. Cut the interval at its midpoint \( \tfrac32 \). Since \( (\tfrac32)^2 = \tfrac94 > 2 \), keep the left half \( [1, \tfrac32] \). Cut again at \( \tfrac54 \): since \( (\tfrac54)^2 = \tfrac{25}{16} < 2 \), keep the right half. Continuing, we get
\[
\begin{aligned}
    [1, 2] &\supseteq \bigl[ 1, \tfrac32 \bigr] \supseteq \bigl[ \tfrac54, \tfrac32 \bigr] \\
           &\supseteq \bigl[ \tfrac{11}8, \tfrac32 \bigr] \supseteq \bigl[ \tfrac{11}8, \tfrac{23}{16} \bigr] \supseteq \cdots,
\end{aligned}
\]
each interval half as long as the one before, each with rational endpoints, and each containing \( \sqrt{2} \). Is there a number lying in all of them?

In \( \nR \) the answer should be "yes, \( \sqrt{2} \)". In \( \nQ \) the answer is "no": the only candidate is \( \sqrt{2} \), and it is not rational. We make both answers precise below. First, a name for the shape of this data. A family of sets \( I_1, I_2, I_3, \dots \) is **nested** if \( I_{n+1} \subseteq I_n \) for every \( n \in \nN \).

::: {#thm-nested-intervals}
[Nested Interval Theorem]

For each \( n \in \nN \), let \( I_n = [a_n, b_n] \) be a closed bounded interval with \( a_n \le b_n \), and suppose the family is nested: \( I_{n+1} \subseteq I_n \) for every \( n \in \nN \). Then \( \bigcap_{n \in \nN} I_n \ne \emptyset \). More precisely, \( \alpha \coloneqq \sup \{ a_n : n \in \nN \} \) exists and lies in every \( I_n \).

If moreover for every \( \varepsilon > 0 \) there is \( n \in \nN \) with \( b_n - a_n < \varepsilon \), then \( \bigcap_{n \in \nN} I_n = \{ \alpha \} \).
:::

::: {.idea}
Picture the intervals on the line. As \( n \) grows, the left endpoints move right (or stay), the right endpoints move left (or stay), and they never cross: every left endpoint lies below every right endpoint, even for different indices. So the set of left endpoints is bounded above by each \( b_n \). Its supremum \( \alpha \) is at least every \( a_n \), because it is an upper bound. It is at most every \( b_n \), because it is the *least* upper bound and each \( b_n \) is an upper bound. Hence \( \alpha \in [a_n, b_n] \) for every \( n \).

For uniqueness: two different common points \( x < y \) would force every interval to have length at least \( y - x \), and the shrinking hypothesis with \( \varepsilon = y - x \) forbids that.
:::

::: {.proof}
We first compare endpoints with different indices.

::: {.claim}
\( a_m \le b_n \) for all \( m, n \in \nN \).
:::

::: {.proofofclaim}
From \( I_{j+1} \subseteq I_j \) for every \( j \), induction on \( k - m \) gives \( I_k \subseteq I_m \) whenever \( m \le k \). Let \( m, n \in \nN \) and \( k \coloneqq \max\{ m, n \} \). Then \( I_k \subseteq I_m \) and \( I_k \subseteq I_n \). Since \( a_k \in I_k \subseteq I_m \), we have \( a_m \le a_k \). Since \( b_k \in I_k \subseteq I_n \), we have \( b_k \le b_n \). Hence \( a_m \le a_k \le b_k \le b_n \).
:::

Let \( A \coloneqq \{ a_n : n \in \nN \} \). It is non-empty, since \( a_1 \in A \), and by the claim it is bounded above by \( b_1 \). By @ax-least-upper-bound, \( \alpha \coloneqq \sup A \) exists.

Fix \( n \in \nN \). Since \( \alpha \) is an upper bound of \( A \), \( a_n \le \alpha \). By the claim, \( b_n \) is an upper bound of \( A \), so (S2) of @def-supremum gives \( \alpha \le b_n \). Hence \( \alpha \in [a_n, b_n] = I_n \). As \( n \) was arbitrary, \( \alpha \in \bigcap_{n} I_n \), and the intersection is non-empty.

Now assume the shrinking hypothesis, and let \( x \in \bigcap_n I_n \). Suppose \( x \ne \alpha \), and let \( u \coloneqq \min\{ x, \alpha \} \) and \( v \coloneqq \max\{ x, \alpha \} \), so \( u < v \) and both lie in every \( I_n \). For every \( n \), \( a_n \le u < v \le b_n \), so \( b_n - a_n \ge v - u \). But \( \varepsilon \coloneqq v - u > 0 \), and by hypothesis some \( n \) has \( b_n - a_n < v - u \). This is a contradiction, so \( x = \alpha \). Hence \( \bigcap_n I_n = \{ \alpha \} \).
:::

Closedness is what lets \( \alpha \) belong to \( I_n \). The proof gives only \( a_n \le \alpha \le b_n \), with non-strict inequalities, and \( \alpha \) may well equal an endpoint. An open interval would exclude it.

Now back to the bisection. Its intervals have length \( 1/2^{n-1} \), and \( 2^{n-1} \ge n \) for every \( n \in \nN \) (induction), so \( 1/2^{n-1} \le 1/n \). Given \( \varepsilon > 0 \), @cor-archimedean-epsilon gives \( n \) with \( 1/n < \varepsilon \), and then the \( n \)-th interval is shorter than \( \varepsilon \). The rule keeps \( a_n^2 < 2 < b_n^2 \) at every step, so \( a_n < \sqrt{2} < b_n \) by @thm-ordered-field-rules (g), and every interval contains \( \sqrt{2} \). By @thm-nested-intervals the intersection is exactly \( \{ \sqrt{2} \} \). The bisection traps \( \sqrt{2} \) and nothing else.

## What each hypothesis does

@thm-nested-intervals has four hypotheses: the intervals are closed, they are bounded, they are nested, and they live in \( \nR \). The uniqueness clause adds a fifth, that the lengths shrink below every \( \varepsilon \). Each one is needed, and each has a witness.

| Hypothesis dropped | Family | Intersection |
|---|---|---|
| closed | \( (0, 1/n) \) | \( \emptyset \) |
| bounded | \( [n, \infty) \) | \( \emptyset \) |
| nested | \( [n, n + 1] \) | \( \emptyset \) |
| the field is \( \nR \) | the rational bisection intervals, in \( \nQ \) | \( \emptyset \) |
| lengths shrink (uniqueness only) | \( [-1/n, 1 + 1/n] \) | \( [0, 1] \) |

We check each row.

- **Closed.** The intervals \( (0, 1/n) \) are nested and bounded. A real \( x \le 0 \) is not in \( (0, 1) \). For \( x > 0 \), @cor-archimedean-epsilon gives \( n \) with \( 1/n < x \), so \( x \notin (0, 1/n) \). Hence no real number is in every interval. Here the supremum of the left endpoints is \( \alpha = 0 \), and it lies in none of the intervals: exactly the step that closedness secured.
- **Bounded.** The intervals \( [n, \infty) \) are closed and nested. For any \( x \in \nR \), @thm-naturals-unbounded gives \( n > x \), and then \( x \notin [n, \infty) \). The proof breaks earlier here: the left endpoints form \( \nN \), which has no upper bound, so \( \alpha \) does not exist.
- **Nested.** The intervals \( [n, n + 1] \) are closed and bounded, but \( [1, 2] \cap [3, 4] = \emptyset \) already.
- **The field is \( \nR \).** In \( \nQ \), a closed interval means \( \{ q \in \nQ : a \le q \le b \} \). Take the bisection intervals \( [a_n, b_n] \) from the start of this section. They are defined by rational arithmetic alone, because each midpoint \( c \) is rational, and \( c^2 \ne 2 \) by @thm-sqrt2-irrational, so the rule "keep the half whose endpoints' squares straddle \( 2 \)" always applies. We showed that the real intervals \( [a_n, b_n] \) have intersection \( \{ \sqrt{2} \} \). So their rational parts have intersection \( \nQ \cap \{ \sqrt{2} \} = \emptyset \).
- **Shrinking.** The intervals \( [-1/n, 1 + 1/n] \) are closed, bounded and nested, and their intersection is \( [0, 1] \): every point of \( [0, 1] \) lies in all of them, and a point outside \( [0, 1] \) is excluded from some interval by @cor-archimedean-epsilon (@exr-nested-intervals-b2 writes this out). The intersection is non-empty, but it is not a single point. Their lengths \( 1 + 2/n \) never drop below \( 1 \).

::: {.warning}
Dropping a hypothesis removes the guarantee. It does not force the conclusion to fail. The open intervals \( (-1/n, 1/n) \) are nested, and their intersection is \( \{ 0 \} \), which is not empty. A witness that a hypothesis is needed must be a family where the conclusion actually fails, like \( (0, 1/n) \).
:::

::: {.check}
Why must the intervals in @thm-nested-intervals be closed? Give a one-line witness.
:::

::: {.solution}
The half-open intervals \( (0, 1/n] \) are nested and bounded, but no real number lies in all of them: \( x \le 0 \) is not in \( (0, 1] \), and for \( x > 0 \) some \( n \) has \( 1/n < x \) (@cor-archimedean-epsilon). The supremum of the left endpoints is \( 0 \), which is excluded from every interval. Closing the intervals at the left end, \( [0, 1/n] \), puts \( 0 \) back in all of them.
:::

## The real numbers cannot be listed

Chapter 7 calls a set **countable** if its elements can be listed as \( x_1, x_2, x_3, \dots \), repetitions allowed; for a non-empty set this means that it is the image of some function from \( \nN \). That chapter shows that \( \nN \), \( \nZ \) and \( \nQ \) are countable. It also shows that \( \nR \) is not, by Cantor's diagonal argument with decimal expansions. Decimal expansions were taken there as a fact from school: every real number has one, and two different expansions such as \( 0.4999\ldots \) and \( 0.5000\ldots \) can name the same number. Neither fact has been proved from our axioms.

Here is a proof with no decimals, using only @thm-nested-intervals.

::: {#thm-reals-uncountable}
[Uncountability of the Reals]

Let \( x_1, x_2, x_3, \dots \) be any list of real numbers, that is, any function \( n \mapsto x_n \) from \( \nN \) to \( \nR \). Then there is \( c \in \nR \) with \( c \ne x_n \) for every \( n \in \nN \). Consequently \( \nR \) is not countable.
:::

::: {.idea}
Build nested closed intervals \( I_1 \supseteq I_2 \supseteq \cdots \), where \( I_n \) is chosen to avoid \( x_n \). A point \( c \) common to all of them, which @thm-nested-intervals provides, avoids every \( x_n \): it lies in \( I_n \), and \( x_n \) does not.

To pass from \( I_n \) to \( I_{n+1} \), cut \( I_n \) into thirds and look at the two outer thirds. They are disjoint closed intervals, so \( x_{n+1} \) misses at least one of them; take that one.

*Before reading on: why thirds, and not halves?*
:::

::: {.proof}
We define closed intervals \( I_n = [a_n, b_n] \) with \( a_n < b_n \) by recursion on \( n \).

Let \( I_1 \coloneqq [x_1 + 1, x_1 + 2] \). Then \( x_1 \notin I_1 \).

Suppose \( I_n = [a_n, b_n] \) with \( a_n < b_n \) has been defined. Let \( d \coloneqq b_n - a_n > 0 \), and let
\[
    L \coloneqq \bigl[ a_n, \ a_n + \tfrac{d}{3} \bigr], \qquad
    R \coloneqq \bigl[ b_n - \tfrac{d}{3}, \ b_n \bigr].
\]
Both are closed intervals of length \( d/3 > 0 \) contained in \( I_n \). They are disjoint, because \( a_n + d/3 < b_n - d/3 \), which is \( 2d/3 < d \). Define
\[
    I_{n+1} \coloneqq
    \begin{cases}
        L & \text{if } x_{n+1} \notin L, \\
        R & \text{if } x_{n+1} \in L.
    \end{cases}
\]
In the second case \( x_{n+1} \in L \), so \( x_{n+1} \notin R \), since \( L \) and \( R \) are disjoint. In both cases \( x_{n+1} \notin I_{n+1} \), \( I_{n+1} \subseteq I_n \), and \( I_{n+1} \) has positive length.

Each \( I_{n+1} \) is determined by \( I_n \) and \( x_{n+1} \) through an explicit rule, so the family is defined by recursion (Chapter 6); no choice principle is involved.

The intervals \( I_n \) are closed, bounded and nested. By @thm-nested-intervals, there is \( c \in \bigcap_n I_n \). For each \( n \in \nN \) we have \( c \in I_n \) and \( x_n \notin I_n \), so \( c \ne x_n \).

Hence no function from \( \nN \) to \( \nR \) has image all of \( \nR \). Since \( \nR \) is non-empty, it is not countable. This proves the theorem.
:::

The answer to the prompt: halves share their midpoint. If \( x_{n+1} \) were exactly that midpoint, it would lie in both closed halves, and neither could be chosen to avoid it. Thirds leave a gap between the two outer pieces.

Only the existence half of @thm-nested-intervals was used; the intervals need not shrink.

::: {.remark}
Since \( \nQ \) is countable, and a union of two countable sets is countable (both from Chapter 7), the set \( \nR \setminus \nQ \) of irrational numbers is uncountable. Otherwise \( \nR = \nQ \cup (\nR \setminus \nQ) \) would be countable. In this sense most real numbers are irrational, although so far we have named only a few of them, such as \( \sqrt{2} \) and \( \sqrt[3]{2} \).
:::

The decimal proof of Chapter 7 is secretly a nested interval proof too: the first \( n \) digits of a number place it in an interval of length \( 10^{-n} \). The version above avoids the digits, and with them the numbers that have two expansions.

## What the axiom bought us

Here is the chapter so far in one table. Each row is a property that \( \nR \) has, checked against the two ordered fields we have used as foils: \( \nQ \) and the field \( \nR(x) \) of @exm-nonarchimedean-field.

| Property | \( \nR \) | \( \nQ \) | \( \nR(x) \) |
|---|---|---|---|
| non-empty sets bounded above have suprema | yes (axiom) | no: positive \( x \) with \( x^2 < 2 \) | no: \( \nN \) |
| Archimedean property | yes | yes | no: \( x > n \) for all \( n \) |
| \( \nQ \) is dense | yes | yes | no: nothing rational in \( (x, x + 1) \) |
| positive elements have square roots | yes | no: \( 2 \) | no: \( x \) |
| nested closed intervals meet | yes | no: bisection toward \( \sqrt{2} \) | no: \( [n, x/n] \) |
| uncountable | yes | no (Chapter 7) | yes: contains \( \nR \) |

The entries for \( \nR \) are this chapter's theorems. For \( \nQ \), the failures come from @thm-no-rational-sup-sqrt2, @thm-sqrt2-irrational and the bisection above; \( \nQ \) is Archimedean by @exr-archimedean-property-c3; and \( \nQ \) is dense in itself because the average of two rationals is a rational between them. For \( \nR(x) \): every rational \( r \) is below some natural number (@exr-archimedean-property-c3), hence below \( x \), so none lies in \( (x, x + 1) \). If \( (p/q)^2 = x \) for polynomials \( p, q \), then \( p^2 = x q^2 \), whose sides have even and odd degree, which is impossible. That the nested intervals \( [n, x/n] \) have no common point is proved in @exr-nested-intervals-c3. And \( \nR(x) \) contains the constants, a copy of \( \nR \), so it cannot be countable, since a subset of a countable set is countable (Chapter 7).

The \( \nQ \) column shows that the Archimedean property and density are far weaker than the axiom; the \( \nR(x) \) column shows an ordered field where even they fail.

Two questions are left open. Is the least upper bound axiom *equivalent* to some of the other rows? And could a different "no gaps" property serve as the axiom instead? Chapter 20 answers both. Over an arbitrary ordered field, the least upper bound axiom is equivalent to each of: the monotone convergence of bounded monotone sequences; the Bolzano–Weierstrass property; Cauchy completeness together with the Archimedean property; and the nested interval property together with the Archimedean property. You can prove one arrow of that last equivalence now (@exr-nested-intervals-c1).

## Exercises

### A. Check your understanding

::: {#exr-nested-intervals-a1}
[A1]

For each family \( (I_n)_{n \in \nN} \), say which hypothesis of @thm-nested-intervals fails, and find \( \bigcap_n I_n \).

::: {.enumerate options="label=(\alph*)"}
1. \( I_n = [0, 1/n) \).
2. \( I_n = [n, n + 1/n] \).
3. \( I_n = (-1/n, 1/n) \).
4. \( I_n = [-n, n] \).
5. Run the construction in the proof of @thm-reals-uncountable on a list that begins \( x_1 = 0 \), \( x_2 = 1 \), \( x_3 = 2 \): find \( I_1 \), \( I_2 \) and \( I_3 \).
6. Where does the proof of @thm-reals-uncountable use that the intervals \( L \) and \( R \) are **closed**, and what could go wrong with open thirds?
:::
:::

::: {.solution}
(a) Not closed. The intersection is \( \{ 0 \} \): \( 0 \) lies in every \( [0, 1/n) \); a negative number lies in none; and for \( x > 0 \), @cor-archimedean-epsilon gives \( n \) with \( 1/n < x \), so \( x \notin [0, 1/n) \). The conclusion holds although a hypothesis fails.

(b) Not nested: \( I_2 = [2, \tfrac52] \not\subseteq [1, 2] = I_1 \). The intersection is empty, since already \( I_1 \cap I_3 = [1, 2] \cap [3, \tfrac{10}3] = \emptyset \).

(c) Not closed. The intersection is \( \{ 0 \} \): \( 0 \) lies in every interval, and for \( x \ne 0 \), @cor-archimedean-epsilon gives \( n \) with \( 1/n < \abs{x} \), so \( x \notin I_n \).

(d) Not nested in the required direction: \( I_{n+1} \supseteq I_n \), and \( I_2 = [-2, 2] \not\subseteq [-1, 1] = I_1 \). The intersection is \( I_1 = [-1, 1] \), since every \( I_n \) contains \( [-1, 1] \).

(e) \( I_1 = [x_1 + 1, x_1 + 2] = [1, 2] \). For \( n = 1 \), \( d = 1 \), \( L = [1, \frac43] \) and \( R = [\frac53, 2] \); since \( x_2 = 1 \in L \), \( I_2 = R = [\frac53, 2] \). For \( n = 2 \), \( d = \frac13 \), \( L = [\frac53, \frac{16}9] \) and \( R = [\frac{17}9, 2] \); since \( x_3 = 2 \notin L \), \( I_3 = L = [\frac53, \frac{16}9] \). Each \( I_n \) misses \( x_n \), and \( I_3 \subseteq I_2 \subseteq I_1 \).

(f) Only in the last step, where @thm-nested-intervals is applied: its hypothesis is that the intervals are closed. With open thirds the family would be nested open intervals, and those can have empty intersection, like \( (0, \frac1n) \); then there might be no point \( c \) at all. The avoidance of \( x_{n+1} \) does not need closedness, only that \( L \) and \( R \) are disjoint.
:::

### B. Practice

::: {#exr-nested-intervals-b1}
[B1: Shrinking by a fixed factor]

::: {.enumerate options="label=(\alph*)"}
1. Let \( I_n = [a_n, b_n] \) be nested closed intervals with \( b_n - a_n = 2^{-n} \) for every \( n \). Prove that \( \bigcap_n I_n \) consists of exactly one point.
2. For \( n \in \nN \), let \( m_n \coloneqq \floor{10^n \sqrt{2}} \) (@lem-integer-part), and let \( a_n \coloneqq m_n / 10^n \) and \( b_n \coloneqq a_n + 10^{-n} \), so that \( a_n \) is the \( n \)-digit decimal truncation of \( \sqrt{2} \). Prove that the intervals \( [a_n, b_n] \) are nested, and that their intersection is \( \{ \sqrt{2} \} \). Compute \( a_1 \) and \( a_2 \).
:::
:::

::: {.solution}
(a) By @thm-nested-intervals it suffices to check the shrinking hypothesis. By induction, \( 2^n > n \) for every \( n \in \nN \) (as in @exr-density-and-roots-c2), so \( 2^{-n} < 1/n \). Given \( \varepsilon > 0 \), @cor-archimedean-epsilon gives \( n \) with \( 1/n < \varepsilon \), and then \( b_n - a_n = 2^{-n} < \varepsilon \). Hence the intersection is a single point.

(b) By definition of the floor, \( m_n \le 10^n \sqrt{2} < m_n + 1 \), so \( a_n \le \sqrt{2} < b_n \) for every \( n \).

*Nested.* Multiplying \( m_n \le 10^n \sqrt{2} \) by \( 10 \) gives \( 10 m_n \le 10^{n+1} \sqrt{2} \). An integer \( k \le z \) always satisfies \( k \le \floor{z} \), since \( k \ge \floor{z} + 1 \) would give \( k > z \). Applied to \( k = 10 m_n \) and \( z = 10^{n+1}\sqrt{2} \), this gives \( 10 m_n \le m_{n+1} \), that is, \( a_n \le a_{n+1} \). Similarly \( m_{n+1} \le 10^{n+1} \sqrt{2} < 10 m_n + 10 \), so \( m_{n+1} < 10 m_n + 10 \), and since both sides are integers, \( m_{n+1} + 1 \le 10 m_n + 10 \). Dividing by \( 10^{n+1} \) gives \( b_{n+1} \le b_n \). Hence \( [a_{n+1}, b_{n+1}] \subseteq [a_n, b_n] \).

*The intersection.* The lengths are \( 10^{-n} \le 2^{-n} \), so by the argument of (a) the intersection is one point. Since \( \sqrt{2} \) lies in every interval, that point is \( \sqrt{2} \).

*The first terms.* \( 14^2 = 196 \le 200 < 225 = 15^2 \), so \( 14 \le 10\sqrt{2} < 15 \), \( m_1 = 14 \) and \( a_1 = 1.4 \). Likewise \( 141^2 = 19881 \le 20000 < 20164 = 142^2 \), so \( m_2 = 141 \) and \( a_2 = 1.41 \).
:::

::: {#exr-nested-intervals-b2}
[B2: An intersection that is not a point]

Prove that \( \bigcap_{n \in \nN} [-1/n, 1 + 1/n] = [0, 1] \). Which hypothesis of the uniqueness clause of @thm-nested-intervals fails?
:::

::: {.solution}
\( (\supseteq) \) Let \( x \in [0, 1] \). For every \( n \), \( -1/n < 0 \le x \le 1 < 1 + 1/n \), so \( x \in [-1/n, 1 + 1/n] \).

\( (\subseteq) \) Let \( x \) lie in every \( [-1/n, 1 + 1/n] \). Suppose \( x < 0 \). By @cor-archimedean-epsilon with \( \varepsilon = -x > 0 \), there is \( n \) with \( 1/n < -x \), that is, \( x < -1/n \), so \( x \notin [-1/n, 1 + 1/n] \): a contradiction. Suppose \( x > 1 \). With \( \varepsilon = x - 1 > 0 \), there is \( n \) with \( 1/n < x - 1 \), that is, \( x > 1 + 1/n \): again a contradiction. Hence \( 0 \le x \le 1 \).

The lengths are \( 1 + 2/n > 1 \), so for \( \varepsilon = 1 \) no interval is shorter than \( \varepsilon \): the shrinking hypothesis fails. The intervals are closed, bounded and nested, and the existence part applies, as it must.
:::

### C. Going deeper

::: {#exr-nested-intervals-c1}
[C1: Exit check: nested intervals and the axiom]

::: {.enumerate options="label=(\alph*)"}
1. Without looking back, prove the existence part of @thm-nested-intervals from the least upper bound axiom.
2. Now work in an ordered field \( F \) in which the Archimedean property holds (for every \( t \in F \) some \( n \in \nN \) has \( n > t \)) and every nested family of closed bounded intervals has a common point. Let \( A \subseteq F \) be non-empty and bounded above by \( M \), and pick \( a \in A \). Define intervals \( [a_n, b_n] \) by \( a_1 \coloneqq a \), \( b_1 \coloneqq M \), and, with \( c \coloneqq (a_n + b_n)/2 \), let \( [a_{n+1}, b_{n+1}] \coloneqq [a_n, c] \) if \( c \) is an upper bound of \( A \), and \( [c, b_n] \) otherwise. Prove that for every \( n \): \( b_n \) is an upper bound of \( A \); some element of \( A \) is \( \ge a_n \); and \( b_n - a_n = (M - a)/2^{n-1} \).
3. Let \( s \) be a common point of all the \( [a_n, b_n] \). Prove that \( s = \sup A \). Deduce that in an ordered field, the nested interval property together with the Archimedean property implies the least upper bound axiom.
:::

:::

::: {.solution}
[Hint 1]

In (c), prove the two properties of a supremum separately, each by contradiction. Each contradiction comes from making \( b_n - a_n \) smaller than a positive gap you are given, which is where the Archimedean property enters.
:::

::: {.solution}
[Hint 2]

For "\( s \) is an upper bound" in (c): suppose some \( y \in A \) has \( y > s \), and choose \( n \) with \( b_n - a_n < y - s \).
:::

::: {.solution}
(a) Let \( I_n = [a_n, b_n] \) be nested. For \( m \le k \), \( I_k \subseteq I_m \), by induction from \( I_{j+1} \subseteq I_j \). Given \( m, n \), put \( k \coloneqq \max\{ m, n \} \); then \( a_m \le a_k \le b_k \le b_n \). So \( A \coloneqq \{ a_n : n \in \nN \} \) is non-empty and bounded above by \( b_1 \), and \( \alpha \coloneqq \sup A \) exists by @ax-least-upper-bound. For each \( n \), \( a_n \le \alpha \) because \( \alpha \) is an upper bound, and \( \alpha \le b_n \) because \( b_n \) is an upper bound and \( \alpha \) is the least one. So \( \alpha \in I_n \) for every \( n \).

(b) In an ordered field \( 2 = 1 + 1 > 0 \), so \( c \) is defined and \( a_n \le c \le b_n \) when \( a_n \le b_n \). We prove the three statements together by induction on \( n \). For \( n = 1 \): \( b_1 = M \) is an upper bound, \( a_1 = a \in A \), and \( b_1 - a_1 = M - a \). Suppose they hold for \( n \). If \( c \) is an upper bound of \( A \), then \( b_{n+1} = c \) is an upper bound, and \( a_{n+1} = a_n \), so the element of \( A \) that is \( \ge a_n \) still works. Otherwise, \( c \) is not an upper bound, so some \( y \in A \) has \( y > c = a_{n+1} \), and \( b_{n+1} = b_n \) is an upper bound. In both cases \( b_{n+1} - a_{n+1} = (b_n - a_n)/2 = (M - a)/2^n \). The intervals are nested, since each is one half of the previous one.

(c) *\( s \) is an upper bound.* Suppose some \( y \in A \) has \( y > s \). Since \( 2^{n-1} \ge n \), we have \( b_n - a_n \le (M - a)/n \). By the Archimedean property in \( F \), choose \( n > (M - a)/(y - s) \); then \( b_n - a_n < y - s \). Since \( a_n \le s \), this gives \( b_n < a_n + (y - s) \le y \). But \( b_n \) is an upper bound of \( A \) and \( y \in A \), a contradiction.

*No smaller upper bound.* Let \( u < s \), and assume for contradiction that \( u \) bounds \( A \) from above. As before, choose \( n \) with \( b_n - a_n < s - u \). Since \( s \le b_n \), we get \( a_n > b_n - (s - u) \ge s - (s - u) = u \). By (b) some \( y \in A \) has \( y \ge a_n > u \), contradicting that \( u \) is an upper bound.

So \( s = \sup A \). Every non-empty subset of \( F \) that is bounded above has a supremum, which is the least upper bound axiom for \( F \). The Archimedean property was used twice, to make \( b_n - a_n \) smaller than a given positive gap. (If \( M = a \), all the intervals are \( \{ a \} \), and the same argument gives \( s = a = \sup A \); the Archimedean step is then not even needed.)

**Marking scheme.** (10 points)
- 2: (a) shows \( a_m \le b_n \) for all \( m, n \), takes \( \alpha = \sup \{ a_n \} \) with both hypotheses of the axiom checked, and shows \( a_n \le \alpha \le b_n \) by (S1) and (S2).
- 3: (b) proves the three statements of (b) by one induction, treating both cases of the bisection rule, including the element of \( A \) that is at least \( a_{n+1} \) in the second case.
- 2: (c) shows \( s \) is an upper bound: a \( y \in A \) above \( s \) is excluded by choosing \( n \) with \( b_n - a_n < y - s \), using the Archimedean property.
- 2: (c) shows no \( u < s \) is an upper bound, choosing \( n \) with \( b_n - a_n < s - u \) and using the element of \( A \) that is at least \( a_n \).
- 1: (c) concludes that \( F \) has the least upper bound property, and says where each of the two assumed properties was used.
Fatal errors (0 for the step): using @ax-least-upper-bound, or any supremum, in (b) or (c); choosing \( n \) before the gap \( y - s \) or \( s - u \) is known; assuming \( A \) has a maximum.
A proof of (c) that shows \( \sup A = s \) through @thm-sup-epsilon instead of (S2) earns the same points.
:::

::: {#exr-nested-intervals-c2}
[C2: Uncountable pieces]

::: {.enumerate options="label=(\alph*)"}
1. Let \( x < y \). Prove that the interval \( (x, y) \) is not countable.
2. Deduce that \( (x, y) \) contains an irrational number, without using \( \sqrt{2} \) or any other named irrational. You may use the facts from Chapter 7 that \( \nQ \) is countable, and that a subset of a countable set is countable.
:::
:::

::: {.solution}
(a) Let \( z_1, z_2, \dots \) be any list of real numbers. Run the construction in the proof of @thm-reals-uncountable, but start from a closed interval inside \( (x, y) \) that avoids \( z_1 \). Let \( d \coloneqq y - x \), and let \( L \coloneqq [x + d/4, x + d/3] \) and \( R \coloneqq [y - d/3, y - d/4] \). They are disjoint, closed, of positive length, and inside \( (x, y) \). Let \( I_1 \) be \( L \) if \( z_1 \notin L \), and \( R \) otherwise. Then define \( I_2, I_3, \dots \) by the outer-thirds rule from the proof. The intervals are nested, closed and bounded, \( z_n \notin I_n \) for every \( n \), and by @thm-nested-intervals some \( c \) lies in all of them. Then \( c \in I_1 \subseteq (x, y) \), and \( c \ne z_n \) for every \( n \). So no list exhausts \( (x, y) \), and \( (x, y) \), which is non-empty, is not countable.

(b) Suppose every element of \( (x, y) \) were rational. Then \( (x, y) \subseteq \nQ \), and a subset of the countable set \( \nQ \) is countable, contradicting (a). So \( (x, y) \) contains an irrational number. This reproves @cor-irrationals-dense by counting: there are too many reals in \( (x, y) \) for all of them to be rational.
:::

::: {#exr-nested-intervals-c3}
[C3: Nested intervals in the rational functions]

Work in the ordered field \( \nR(x) \) of @exm-nonarchimedean-field. For \( n \in \nN \), let \( I_n \coloneqq \{ f \in \nR(x) : n \le f \le x/n \} \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( n < x/n \), so \( I_n \) is a closed bounded interval of positive length, and that \( I_{n+1} \subseteq I_n \).
2. Let \( f = p/q \) with the leading coefficient of \( q \) positive, and suppose \( f \in I_n \) for every \( n \). Show that \( \deg p > \deg q \).
3. Show that \( \deg p \ge \deg q + 2 \) and \( \deg p = \deg q + 1 \) both lead to a contradiction, and conclude that \( \bigcap_n I_n = \emptyset \).
4. Which line of the proof of @thm-nested-intervals fails in \( \nR(x) \)?
:::

:::

::: {.solution}
[Hint 1]

Positivity in \( \nR(x) \) is decided by leading coefficients. Write each difference you need to sign, such as \( x/n - f \) or \( N - f \), as a single fraction with a positive denominator.
:::

::: {.solution}
[Hint 2]

For (b): since \( f \ge 1 \), the leading coefficient of \( p \) is positive. Suppose \( \deg p \le \deg q \), choose \( N \in \nN \) with \( N > \operatorname{lc}(p)/\operatorname{lc}(q) \), and look at \( N - f = (Nq - p)/q \).
:::

::: {.solution}
Write \( \operatorname{lc} \) for the leading coefficient, and recall from @exr-archimedean-property-c2 that for \( g = u/w \) with \( \operatorname{lc}(w) > 0 \), \( g > 0 \) if and only if \( \operatorname{lc}(u) > 0 \).

(a) \( x/n - n = (x - n^2)/n \) has numerator with leading coefficient \( 1 > 0 \) and positive denominator, so \( n < x/n \). Nesting: \( n + 1 > n \), and \( x/n - x/(n+1) = x/(n(n+1)) > 0 \). So \( I_{n+1} \subseteq I_n \).

(b) Since \( f \ge 1 > 0 \), \( \operatorname{lc}(p) > 0 \). Suppose \( \deg p \le \deg q \). Pick \( N \in \nN \) with \( N > \operatorname{lc}(p)/\operatorname{lc}(q) \). Then \( N - f = (Nq - p)/q \). If \( \deg p < \deg q \), the leading coefficient of \( Nq - p \) is \( N \operatorname{lc}(q) > 0 \); if \( \deg p = \deg q \), it is \( N \operatorname{lc}(q) - \operatorname{lc}(p) > 0 \). Either way \( f < N \), so \( f \notin I_N \), a contradiction. Hence \( \deg p > \deg q \).

(c) For each \( n \),
\[
    \frac{x}{n} - f = \frac{x q - n p}{n q}, \qquad \operatorname{lc}(nq) = n \operatorname{lc}(q) > 0 .
\]
If \( \deg p \ge \deg q + 2 \), then \( \deg(np) > \deg(xq) \), so the numerator has leading coefficient \( -n \operatorname{lc}(p) < 0 \). Thus \( f > x/n \) for every \( n \), and \( f \notin I_1 \). If \( \deg p = \deg q + 1 \), both \( xq \) and \( np \) have degree \( \deg q + 1 \), and the numerator has leading coefficient \( \operatorname{lc}(q) - n \operatorname{lc}(p) \). Choosing \( n > \operatorname{lc}(q)/\operatorname{lc}(p) \) makes it negative, so \( f > x/n \) and \( f \notin I_n \). Both cases contradict \( f \in \bigcap_n I_n \). With (b), no \( f \) lies in every \( I_n \), and the intersection is empty.

(d) The line "\( \alpha \coloneqq \sup \{ a_n \} \) exists by @ax-least-upper-bound". Here the left endpoints are \( a_n = n \), and \( \{ a_n \} = \nN \) is bounded above (by \( x/1 \), for instance) but has no supremum in \( \nR(x) \), as shown in the section on the Archimedean property. The claim \( a_m \le b_n \) and every other line survive.
:::

::: {#exr-nested-intervals-c4}
[C4: A root of a cubic, from half a proof]

Let \( g(x) \coloneqq x^3 + x \). Then \( g(0) = 0 \) and \( g(1) = 2 \), so \( g \) passes the value \( 1 \) somewhere in \( [0, 1] \). Here is the first half of a proof that it takes the value \( 1 \).

> Let \( S \coloneqq \{ x \in \nR : x \ge 0, \ g(x) < 1 \} \). Then \( 0 \in S \). If \( x \ge 1 \), then \( x^3 \ge 1 \) and \( g(x) \ge 2 > 1 \), so every element of \( S \) is less than \( 1 \). By @ax-least-upper-bound, \( s \coloneqq \sup S \) exists, and \( 0 \le s \le 1 \).

*Name the move, then complete it.* Prove that \( g(s) = 1 \). Then show that \( 0.68 < s < 0.69 \), and that \( s \) is the only real number \( t \) with \( g(t) = 1 \).
:::

::: {.solution}
[Hint 1]

Rule out \( g(s) < 1 \) and \( g(s) > 1 \) by nudging \( s \) to \( s + h \) and \( s - h \). For that you need a bound on \( g(s + h) - g(s) \), and on \( g(s) - g(s - h) \), of the form "a constant times \( h \)", valid for small \( h \).
:::

::: {.solution}
[Hint 2]

Expanding, \( g(s + h) - g(s) = h(3s^2 + 3sh + h^2 + 1) \). With \( 0 \le s \le 1 \) and \( 0 < h \le 1 \) this is at most \( 8h \).
:::

::: {.solution}
The move is **construct a point as a supremum**. The given half defines the set of points where things are still fine (\( g(x) < 1 \)) and takes its supremum; what remains is to rule out each way \( s \) could fail.

We use that \( g \) is strictly increasing on \( [0, \infty) \): if \( 0 \le u < v \), then \( u^3 < v^3 \) by the claim in the proof of @thm-nth-root, and adding \( u < v \) gives \( g(u) < g(v) \) by @thm-ordered-field-rules (b). Expanding with @lem-field-algebra, for every \( h \),
\[
\begin{aligned}
g(s + h) - g(s) &= h(3s^2 + 3sh + h^2 + 1), \\
g(s) - g(s - h) &= h(3s^2 - 3sh + h^2 + 1).
\end{aligned}
\]

*Case \( g(s) < 1 \).* Let \( h \coloneqq (1 - g(s))/16 \), which depends only on \( s \). Since \( 0 \le g(s) < 1 \), we have \( 0 < h \le \frac1{16} \). With \( s \le 1 \) and \( h \le 1 \), the first identity gives
\[
g(s + h) - g(s) \le h(3 + 3 + 1 + 1) = 8h = \tfrac12 \bigl( 1 - g(s) \bigr) < 1 - g(s),
\]
so \( g(s + h) < 1 \). As \( s + h \ge 0 \), we get \( s + h \in S \), and \( s + h > s \) contradicts (S1).

*Case \( g(s) > 1 \).* Then \( s > 0 \), since \( g(0) = 0 \). Let \( h \coloneqq (g(s) - 1)/10 > 0 \). Since \( s \le 1 \) gives \( s^3 \le s \), we have \( g(s) - 1 < g(s) \le 2s \), so \( h < \frac{s}{5} < s \) and \( s - h > 0 \). As \( 0 < h < s \le 1 \), we have \( -3sh < 0 \), and the second identity gives
\[
g(s) - g(s - h) \le h(3 + 1 + 1) = 5h = \tfrac12 \bigl( g(s) - 1 \bigr) < g(s) - 1,
\]
so \( g(s - h) > 1 \). Now \( s - h \) is an upper bound of \( S \): if \( x \in S \) had \( x > s - h \), then, as \( s - h > 0 \), monotonicity would give \( g(x) > g(s - h) > 1 \), contradicting \( x \in S \). So (S2) gives \( s \le s - h \), which is false.

By trichotomy, \( g(s) = 1 \).

*Location.* Exact arithmetic gives \( g(0.68) = 0.314432 + 0.68 = 0.994432 < 1 \) and \( g(0.69) = 0.328509 + 0.69 = 1.018509 > 1 \). If \( s \le 0.68 \), monotonicity would give \( g(s) \le g(0.68) < 1 \), and if \( s \ge 0.69 \), it would give \( g(s) > 1 \). So \( 0.68 < s < 0.69 \).

*Uniqueness.* Let \( t \in \nR \) with \( g(t) = 1 \). If \( t < 0 \), then \( t^2 > 0 \) and \( t^3 = t \cdot t^2 < 0 \) by @thm-ordered-field-rules (c), so \( g(t) < 0 \); hence \( t \ge 0 \). On \( [0, \infty) \), \( g \) is strictly increasing, so \( t < s \) or \( t > s \) would give \( g(t) \ne g(s) \). Hence \( t = s \).

This is the intermediate value theorem for one polynomial, proved by the move that proves it in general in Chapter 15.

**Marking scheme.** (10 points)
- 1: names the move, and records that \( g \) is strictly increasing on \( [0, \infty) \) with a reason.
- 3: rules out \( g(s) < 1 \) with an explicit \( h > 0 \) depending only on \( s \), a verified bound on \( g(s + h) - g(s) \), and a contradiction with (S1).
- 3: rules out \( g(s) > 1 \) with an explicit \( h \), checking \( s - h > 0 \), that \( g(s - h) > 1 \), and that \( s - h \) is an upper bound, then contradicting (S2).
- 1: concludes \( g(s) = 1 \) by trichotomy.
- 2: the location \( 0.68 < s < 0.69 \) from two exact computations and monotonicity, and uniqueness, including the case \( t < 0 \).
Fatal errors (0 for the step): an \( h \) that depends on an element of \( S \) or is not shown positive; using that \( s - h \) is an upper bound without monotonicity; assuming the intermediate value theorem.
Other constants (for instance \( h = \min\{ 1, (1 - g(s))/10 \} \)) earn full marks when the bound they need is verified.
:::

### R. Review

::: {#exr-nested-intervals-r1}
[R1]

Let \( A \subseteq \nR \) be non-empty, and let \( s \) be an upper bound of \( A \). Prove that the following are equivalent.

::: {.enumerate options="label=(\roman*)"}
1. \( s = \sup A \).
2. For every \( n \in \nN \) there is \( a \in A \) with \( a > s - \frac1n \).
3. No real number smaller than \( s \) is an upper bound of \( A \).
:::
:::

::: {.solution}
By @prp-equivalence-cycle it suffices to prove (i) \( \Rightarrow \) (ii) \( \Rightarrow \) (iii) \( \Rightarrow \) (i).

*(i) \( \Rightarrow \) (ii).* This is @cor-sup-approximation, or @thm-sup-epsilon (\( \Rightarrow \)) with \( \varepsilon = \frac1n \).

*(ii) \( \Rightarrow \) (iii).* Let \( u < s \). By @cor-archimedean-epsilon there is \( n \), depending on \( s - u \), with \( \frac1n < s - u \). By (ii) some \( a \in A \) has \( a > s - \frac1n > u \), so \( u \) is not an upper bound.

*(iii) \( \Rightarrow \) (i).* (S1) holds because \( s \) is an upper bound. For (S2), let \( M \) be an upper bound. By (iii), \( M < s \) is impossible, so \( s \le M \) by trichotomy.

The cycle is the method of Chapter 1 for equivalences (@prp-equivalence-cycle). Here (ii) \( \Rightarrow \) (iii) is the only arrow with content: it is where the Archimedean property turns the special widths \( \frac1n \) into every width.
:::

::: {#exr-nested-intervals-r2}
[R2]

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( x \) is a real number and \( x^2 \) is irrational, then \( x \) is irrational.
2. Hence prove that the positive real number \( t \) with \( t^4 = 2 \) is irrational.
:::
:::

::: {.solution}
(a) By @prp-contrapositive it suffices to prove: if \( x \) is rational, then \( x^2 \) is rational. That holds because a product of rationals is rational (@exm-ordered-fields-q-r).

(b) The number \( t \) exists by @thm-nth-root. Then \( t^2 > 0 \) and \( (t^2)^2 = t^4 = 2 \), so \( t^2 \) is the positive square root of \( 2 \), by the uniqueness in @thm-sqrt2-exists. It is irrational by @thm-sqrt2-irrational. By (a), \( t \) is irrational.

The direct statement (a) would be awkward to prove as it stands, since "irrational" is a negative property; its contrapositive is one line. That is the reason to reach for the contrapositive (@prp-contrapositive, Chapter 1).
:::

::: {#exr-nested-intervals-r3}
[R3]

Prove that the real number \( \sqrt2 + \sqrt3 \) is irrational.
:::

::: {.solution}
Here \( \sqrt3 \) and \( \sqrt6 \) are the positive square roots given by @thm-nth-root. First, \( \sqrt2 \sqrt3 = \sqrt6 \): the left side is positive and its square is \( 2 \cdot 3 = 6 \), so it is the unique positive square root of \( 6 \).

Suppose, for a contradiction, that \( r \coloneqq \sqrt2 + \sqrt3 \) is rational \( [\text{assumption for } \rulename{\neg I}] \). Then
\[
r^2 = 2 + 2\sqrt2 \sqrt3 + 3 = 5 + 2\sqrt6 ,
\]
so \( \sqrt6 = (r^2 - 5)/2 \) is rational, because the rationals are closed under the field operations. But no rational number has square \( 6 \) (@exr-negation-and-contradiction-c1). Hence \( r \) is irrational \( [\rulename{\neg I}] \).

Chapter 1 could prove only the negative half: no rational squares to \( 6 \). With @thm-nth-root the number \( \sqrt6 \) exists in \( \nR \), and the negative statement becomes the positive one, "\( \sqrt6 \) is irrational", which is what the argument uses.
:::

::: {#exr-nested-intervals-r4}
[R4]

Prove that \( \abs{x - 1} + \abs{x + 1} \ge 2 \) for every real \( x \), and find all \( x \) for which equality holds.
:::

::: {.solution}
The tool is the triangle inequality (@thm-triangle-inequality), applied to a sum chosen so that \( x \) cancels:
\[
2 = \abs{(1 - x) + (x + 1)} \le \abs{1 - x} + \abs{x + 1} = \abs{x - 1} + \abs{x + 1},
\]
using \( \abs{1 - x} = \abs{x - 1} \) (@prp-absolute-value-rules (b)). By @exr-ordered-fields-b2 (b), equality holds exactly when \( (1 - x)(x + 1) \ge 0 \), that is, when \( 1 - x^2 \ge 0 \), that is, when \( -1 \le x \le 1 \) (by @thm-ordered-field-rules (g) and @prp-absolute-value-rules (d), \( x^2 \le 1 \) means \( \abs{x} \le 1 \)). So equality holds exactly on \( [-1, 1] \).

The look-alike tools work less well. Proof by cases, as in @exm-triangle-inequality-cases, succeeds but needs three cases (\( x < -1 \), \( -1 \le x \le 1 \), \( x > 1 \)) and a formula in each. Squaring both sides leaves the cross term \( 2\abs{x^2 - 1} \), which still has an absolute value in it, so it only postpones the case split.
:::

<!-- dependency ledger
thm-nested-intervals (claim): I_k is contained in I_m for m <= k, from I_(j+1) contained in I_j | inline, by induction on k - m (ch06 (promised))
thm-nested-intervals (example): 2^(n-1) >= n for n in N (the bisection intervals shrink) | inline, by induction (ch06 (promised))
thm-reals-uncountable (proof): a family defined by recursion from an explicit rule exists | definition by recursion, ch06 (promised); prose pointer in the proof
thm-reals-uncountable (proof): countable means listable, i.e. the image of a function from N | ch07 (promised); prose pointer before the theorem
thm-reals-uncountable (example): Q is countable; a union of two countable sets is countable; a subset of a countable set is countable (remark and table) | ch07 (promised); used only in a remark and the table, never in a proof
thm-reals-uncountable (example): (p/q)^2 = x is impossible in R(x), since p^2 and x q^2 have degrees of different parity (table) | inline
exr-nested-intervals-b1 (solution): 14^2 = 196, 15^2 = 225, 141^2 = 19881, 142^2 = 20164; an integer k <= z satisfies k <= floor(z) | arithmetic and lem-integer-part, shown inline
exr-nested-intervals-c1 (solution): 2^(n-1) >= n | inline, by induction (ch06 (promised))
exr-nested-intervals-c2 (solution): Q is countable; a subset of a countable set is countable | ch07 (promised); the item states them as usable facts
exr-nested-intervals-c4 (solution): the expansions of (s + h)^3 + (s + h) and (s - h)^3 + (s - h); 0.68^3 = 0.314432 and 0.69^3 = 0.328509 | lem-field-algebra; arithmetic, shown inline
exr-nested-intervals-r2 (solution): a product of rationals is rational | exm-ordered-fields-q-r
exr-nested-intervals-r3 (solution): sqrt(2) sqrt(3) = sqrt(6), by uniqueness of positive square roots | inline, from thm-nth-root
-->
