# Density of the Rationals and the Existence of Roots

When we first met suprema, @thm-no-rational-sup-sqrt2 showed that the set of positive rationals whose square is less than \( 2 \) has no supremum in \( \nQ \). In \( \nR \) the axiom gives that set a supremum. This section finds out what the supremum is: a positive number whose square is exactly \( 2 \). The same template produces every root \( a^{1/n} \). With roots in hand, and with the Archimedean property of the previous section, we then answer a question about arrangement: the rationals and the irrationals are both spread through every interval of the line, however short.

## Constructing a point as a supremum

Chapter 1 showed that no rational number squares to \( 2 \) (@thm-sqrt2-irrational). Nothing so far says that any real number does. The ordered-field axioms cannot say it, since \( \nQ \) satisfies them all. So if a square root of \( 2 \) exists in \( \nR \), the least upper bound axiom must produce it.

::: {#thm-sqrt2-exists}
[The Square Root of Two Exists]

There is exactly one real number \( s > 0 \) with \( s^2 = 2 \).
:::

::: {.idea}
Collect the positive reals whose square is below \( 2 \) into a set \( S \). The candidate is \( s = \sup S \). The plan has three steps: ① check that \( S \) is non-empty and bounded above, so the axiom supplies \( s \); ② rule out \( s^2 < 2 \); ③ rule out \( s^2 > 2 \). Trichotomy then leaves \( s^2 = 2 \).

Each case is ruled out by nudging \( s \). If \( s^2 < 2 \), there is still room below \( 2 \), so a slightly larger number \( s + h \) is still in \( S \). That is impossible for an upper bound. If \( s^2 > 2 \), a slightly smaller number \( s - h \) still has square above \( 2 \), and is therefore still an upper bound. That is impossible for the *least* upper bound.

The nudges are the ones found in @thm-no-rational-sup-sqrt2, where they were derived backwards from the goal. To recall the first: we want \( (s + h)^2 = s^2 + 2sh + h^2 < 2 \). If \( h \le 1 \), then \( h^2 \le h \), so \( (s + h)^2 \le s^2 + (2s + 1)h \). Letting \( (2s + 1)h \) use half of the room \( 2 - s^2 \) gives \( h = (2 - s^2)/(4s + 2) \), and we must then check \( h \le 1 \). For the second nudge, \( (s - h)^2 > s^2 - 2sh \), and the right side is \( 2 \) exactly when \( h = (s^2 - 2)/(2s) \). None of this used rationality. What is new is only that \( s \) now exists.

*Before reading on: which line of the proof uses the axiom, and what would that line say over \( \nQ \)?*
:::

::: {.proof}
Let \( S \coloneqq \{ x \in \nR : x > 0, \ x^2 < 2 \} \). By @exm-lub-first-use, \( S \) is non-empty (it contains \( 1 \)) and bounded above by \( 2 \), so by @ax-least-upper-bound its supremum \( s \coloneqq \sup S \) exists, and \( 1 \le s \le 2 \). In particular \( s > 0 \) and \( s^2 \ge 1 \). Throughout we use @thm-ordered-field-rules (g): for \( u, v \ge 0 \), \( u < v \) if and only if \( u^2 < v^2 \).

*Case 1: \( s^2 < 2 \).* Let
\[
    h \coloneqq \frac{2 - s^2}{4s + 2},
\]
which depends only on \( s \). Then \( h > 0 \), because \( 2 - s^2 > 0 \) and \( 4s + 2 > 0 \). Also \( h \le \tfrac16 \), because \( 2 - s^2 \le 1 \) and \( 4s + 2 \ge 6 \). Hence \( h \le 1 \), and multiplying by \( h > 0 \) gives \( h^2 \le h \). Therefore
\[
\begin{aligned}
    (s + h)^2 &= s^2 + 2sh + h^2 \le s^2 + (2s + 1)h \\
              &= s^2 + \tfrac{2 - s^2}{2} = 1 + \tfrac{s^2}{2} < 2,
\end{aligned}
\]
where the last inequality holds because \( s^2 < 2 \). Also \( s + h > 0 \). Hence \( s + h \in S \). But \( s + h > s \), which contradicts (S1), that \( s \) is an upper bound of \( S \). So Case 1 is impossible.

*Case 2: \( s^2 > 2 \).* Let
\[
    h \coloneqq \frac{s^2 - 2}{2s},
\]
which is defined and positive because \( s > 0 \) and \( s^2 > 2 \). Then \( s - h = (s^2 + 2)/(2s) > 0 \), and
\[
    (s - h)^2 = s^2 - 2sh + h^2 = 2 + h^2 > 2 .
\]
We claim that \( s - h \) is an upper bound of \( S \). Let \( x \in S \) and suppose \( x > s - h \). Since \( s - h > 0 \), we get \( x^2 > (s - h)^2 > 2 \), contradicting \( x^2 < 2 \). Hence \( x \le s - h \) for every \( x \in S \). Then (S2) gives \( s \le s - h \), which is false since \( h > 0 \). So Case 2 is impossible.

By trichotomy, \( s^2 = 2 \). For uniqueness, let \( t > 0 \) with \( t^2 = 2 \). If \( t < s \), then \( t^2 < s^2 \), and if \( s < t \), then \( s^2 < t^2 \); both contradict \( t^2 = 2 = s^2 \). Hence \( t = s \). This proves the theorem.
:::

We write \( \sqrt{2} \) for this number. By @thm-sqrt2-irrational it is not rational, so \( \nR \ne \nQ \): irrational numbers exist.

Compare this proof with the one of @thm-no-rational-sup-sqrt2. The two computations with \( h \) are the same, word for word: they are ordered-field algebra, and for a rational \( s \) both values of \( h \) are rational. What changed is a single line. In \( \nQ \) there was no \( s \) to start from: the argument showed that no rational number can be the supremum, since its square cannot be less than \( 2 \), more than \( 2 \), or equal to \( 2 \). In \( \nR \) the axiom supplies \( s \), and the very same argument now shows that its square can only be \( 2 \).

The proof is an instance of a move this book uses again and again.

*To construct a point: collect the points where "things are still fine" into a set, take its supremum, and rule out each way the supremum could fail to be the point you want.*

Here "things are still fine" meant \( x^2 < 2 \). In Chapter 13 the Intermediate Value Theorem is proved the same way: the point where a continuous function crosses zero is the supremum of the points where it is still negative. In Chapter 11 the Heine–Borel theorem takes the supremum of the points \( x \) for which \( [a, x] \) is still covered by finitely many of the given open sets.

## Roots of every order

The template does not care that the exponent is \( 2 \) or that the number is \( 2 \). Only the choice of \( h \) needs new work.

::: {#thm-nth-root}
[Existence of Roots]

Let \( a > 0 \) and \( n \in \nN \). There is exactly one real number \( s > 0 \) with \( s^n = a \).
:::

We write this number \( a^{1/n} \), or \( \sqrt[n]{a} \).

::: {.idea}
Take \( S = \{ x > 0 : x^n < a \} \) and \( s = \sup S \), as before, and rule out \( s^n < a \) and \( s^n > a \). The new difficulty is the estimate. For \( n = 2 \) we expanded \( (s + h)^2 \) and bounded \( h^2 \) by \( h \). For general \( n \), expanding \( (s + h)^n \) is messy. We work backwards from what we need instead.

We need \( (s + h)^n - s^n < a - s^n \). A difference of \( n \)-th powers factors:
\[
    y^n - x^n = (y - x)\bigl( y^{n-1} + y^{n-2} x + \dots + x^{n-1} \bigr).
\]
With \( y = s + h \) and \( x = s \), the first factor is \( h \), which we control. The second factor is a sum of \( n \) terms, each at most \( (s + h)^{n-1} \). That still depends on \( h \), and we cannot solve for \( h \) while \( h \) is on both sides. So we bound it by something a little bigger: if \( h < 1 \), each term is at most \( (s + 1)^{n-1} \). This gives
\[
    (s + h)^n - s^n \le h \cdot C, \qquad C \coloneqq n (s + 1)^{n-1} .
\]
The point is that \( C \) depends only on \( n \) and \( s \), and not on \( h \). Now it suffices to have \( hC < a - s^n \), and \( h = (a - s^n)/(2C) \) does it, with a factor \( \tfrac12 \) to make the inequality strict. We needed \( h < 1 \) along the way, so we cap \( h \) at \( \tfrac12 \).

For \( s - h \) the same factorization gives \( s^n - (s - h)^n \le h \cdot n s^{n-1} \le hC \), so the same \( C \), and the same \( h \), serve both cases.
:::

::: {.proof}
We first prove a power estimate.

::: {.claim}
Let \( 0 \le x < y \) and \( k \in \nN \). Then
\[
    0 < y^k - x^k \le k y^{k-1} (y - x).
\]
In particular \( x^k < y^k \): the map \( x \mapsto x^k \) is strictly increasing on \( [0, \infty) \).
:::

::: {.proofofclaim}
Write \( \Sigma \coloneqq \sum_{j=0}^{k-1} y^j x^{k-1-j} \), with the convention \( u^0 = 1 \). Multiplying out,
\[
\begin{aligned}
    (y - x)\Sigma &= \sum_{j=0}^{k-1} y^{j+1} x^{k-1-j} - \sum_{j=0}^{k-1} y^j x^{k-j} \\
                  &= y^k - x^k,
\end{aligned}
\]
since every other term appears once in each sum and cancels. Since \( 0 \le x < y \), each term of \( \Sigma \) satisfies \( 0 \le y^j x^{k-1-j} \le y^{k-1} \), and the term with \( j = k - 1 \) equals \( y^{k-1} > 0 \). Hence \( 0 < \Sigma \le k y^{k-1} \). Multiplying by \( y - x > 0 \) gives the claim.
:::

Let \( S \coloneqq \{ x \in \nR : x > 0, \ x^n < a \} \).

*\( S \) is non-empty.* Let \( x_0 \coloneqq a/(1 + a) \). Then \( 0 < x_0 < 1 \) and \( x_0 < a \). Since \( 0 < x_0 < 1 \), multiplying by \( x_0 \) repeatedly gives \( x_0^n \le x_0 \) (by induction on \( n \)). Hence \( x_0^n \le x_0 < a \), and \( x_0 \in S \).

*\( S \) is bounded above by \( 1 + a \).* If \( x \ge 1 + a \), then \( x \ge 1 \), so \( x^n \ge x \) (again by induction on \( n \)), and \( x^n \ge 1 + a > a \). So \( x \notin S \).

By @ax-least-upper-bound, \( s \coloneqq \sup S \) exists, and \( s \ge x_0 > 0 \). Let
\[
    C \coloneqq n (s + 1)^{n-1},
\]
which depends only on \( n \) and \( s \). Suppose \( s^n \ne a \), and let
\[
    h \coloneqq \min\Bigl\{ \frac12, \ \frac{\abs{s^n - a}}{2C} \Bigr\} > 0 .
\]
Then \( hC \le \tfrac12 \abs{s^n - a} < \abs{s^n - a} \).

*Case 1: \( s^n < a \).* Apply the claim with \( k = n \), \( x = s \) and \( y = s + h \). Since \( s + h < s + 1 \), the claim with \( k = n - 1 \) gives \( (s + h)^{n-1} \le (s + 1)^{n-1} \) (with equality \( 1 = 1 \) when \( n = 1 \)). Therefore
\[
    (s + h)^n - s^n \le n (s + h)^{n-1} h \le C h < a - s^n ,
\]
so \( (s + h)^n < a \). Hence \( s + h \in S \), although \( s + h > s \). This contradicts that \( s \) is an upper bound of \( S \).

*Case 2: \( s^n > a \).* First, \( s - h > 0 \). Indeed \( (s + 1)^{n-1} \ge s^{n-1} \) by the claim with \( k = n - 1 \), so
\[
    h \le \frac{s^n - a}{2C} < \frac{s^n}{2C} \le \frac{s^n}{2 n s^{n-1}} = \frac{s}{2n} < s .
\]
Apply the claim with \( k = n \), \( x = s - h \) and \( y = s \):
\[
    s^n - (s - h)^n \le n s^{n-1} h \le C h < s^n - a ,
\]
so \( (s - h)^n > a \). Now \( s - h \) is an upper bound of \( S \): if \( x \in S \) had \( x > s - h \), the claim would give \( x^n > (s - h)^n > a \), contradicting \( x \in S \). But \( s - h < s \), which contradicts that \( s \) is the least upper bound.

Both cases are impossible, so \( s^n = a \) by trichotomy. If also \( t > 0 \) and \( t^n = a \), then \( t = s \), since \( t < s \) or \( s < t \) would give \( t^n \ne s^n \) by the claim. This proves the theorem.
:::

For \( n = 2 \) and \( a = 2 \) the constant is \( C = 2(s + 1) \), slightly larger than the \( 2s + 1 \) that the direct expansion gave. The general proof pays for its generality with a cruder bound. We never needed a good bound, only one that does not depend on \( h \).

::: {#exm-cube-root-bounds}
[Locating a cube root]

Show that \( 1.25 < \sqrt[3]{2} < 1.26 \).
:::

::: {.solution}
By @thm-nth-root, \( s \coloneqq \sqrt[3]{2} \) exists and \( s^3 = 2 \). Exact arithmetic gives
\[
    1.25^3 = 1.953125 < 2 < 2.000376 = 1.26^3 .
\]
The claim in the proof of @thm-nth-root says that \( x \mapsto x^3 \) is strictly increasing on \( [0, \infty) \). If \( s \le 1.25 \), then \( s^3 \le 1.25^3 < 2 \); and if \( s \ge 1.26 \), then \( s^3 \ge 1.26^3 > 2 \). Both contradict \( s^3 = 2 \), so \( 1.25 < s < 1.26 \).
:::

::: {.remark}
With \( n \)-th roots we can define \( a^{m/n} \coloneqq (a^{1/n})^m \) for \( a > 0 \), and check that the usual exponent laws hold for rational exponents. The powers \( a^x \) with irrational \( x \) wait for the exponential function, which Chapter 17 builds from power series.
:::

## The integer part of a real number

Before asking where the rationals are, we need to locate every real number between two consecutive integers. This sounds like school arithmetic, and it is. But its proof uses both the Archimedean property and well-ordering, and in \( \nR(x) \) it fails for the element \( x \) (@exr-archimedean-property-c1).

::: {#lem-integer-part}
[Integer Part]

For every \( y \in \nR \) there is exactly one integer \( m \) with \( m \le y < m + 1 \).
:::

This integer is the **integer part** or **floor** of \( y \), written \( \floor{y} \). For instance \( \floor{2.7} = 2 \) and \( \floor{-2.7} = -3 \).

::: {.idea}
Picture the integers as marks spaced \( 1 \) apart. The Archimedean property puts a mark to the right of \( y \), and a mark to the left of \( y \). Among the marks to the right, well-ordering picks out the first one; the mark just before it is \( \floor{y} \). Well-ordering is a statement about subsets of \( \nN \), so we shift the marks so that they start at \( 1 \).
:::

::: {.proof}
*Existence.* Let \( y \in \nR \). By @thm-naturals-unbounded, there is \( p \in \nN \) with \( p > -y \), and there is \( j \in \nN \) with \( j > y + p \). Hence the set
\[
    T \coloneqq \{ j \in \nN : j - p > y \}
\]
is non-empty. By well-ordering (Chapter 4), \( T \) has a least element \( j_0 \). Let \( m \coloneqq j_0 - p - 1 \), an integer. Then \( m + 1 = j_0 - p > y \), since \( j_0 \in T \). It remains to show \( m \le y \).

- If \( j_0 = 1 \), then \( m = -p < y \), by the choice of \( p \).
- If \( j_0 \ge 2 \), then \( j_0 - 1 \in \nN \), and \( j_0 - 1 \notin T \) because it is smaller than the least element of \( T \). So \( (j_0 - 1) - p \le y \), that is, \( m \le y \).

*Uniqueness.* Suppose \( m \) and \( m' \) are integers with \( m \le y < m + 1 \) and \( m' \le y < m' + 1 \), and suppose \( m < m' \). Then \( m' \ge m + 1 \), since no integer lies strictly between \( m \) and \( m + 1 \). Hence \( y \ge m' \ge m + 1 > y \), a contradiction. By symmetry \( m' < m \) is impossible too, so \( m = m' \).
:::

## The rationals are dense

We know now that irrational numbers exist. How are they arranged among the rationals? Could there be a whole interval with no rational number in it? No: every interval, however short, contains a rational.

::: {#thm-rationals-dense}
[Density of the Rationals]

Let \( x, y \in \nR \) with \( x < y \). There is \( q \in \nQ \) with \( x < q < y \).
:::

::: {.idea}
Think of a ruler whose marks are the fractions \( k/n \), spaced \( 1/n \) apart. If the spacing is smaller than the gap \( y - x \), the ruler cannot jump over the interval \( (x, y) \): the first mark to the right of \( x \) is at most one step past \( x \), and so it lands before \( y \).

\begin{center}
\begin{tikzpicture}[scale=1.0]
  \draw[->] (-0.4,0) -- (7.4,0);
  \foreach \k in {0,1,2,3,4,5,6,7} { \draw (\k,0.1) -- (\k,-0.1); }
  \node[below] at (2,-0.15) {$\tfrac{m-1}{n}$};
  \node[below] at (3,-0.15) {$\tfrac{m}{n}$};
  \filldraw (2.55,0) circle (2pt) node[above] {$x$};
  \filldraw (4.2,0) circle (2pt) node[above] {$y$};
  \draw[<->] (5,0.4) -- (6,0.4) node[midway,above] {$\tfrac1n$};
\end{tikzpicture}
\end{center}

The plan: ① choose \( n \) with \( 1/n < y - x \), by the Archimedean property; ② let \( m/n \) be the first mark strictly to the right of \( x \), that is, \( m = \floor{nx} + 1 \); ③ check that \( m/n < y \).
:::

::: {.proof}
Let \( x < y \). Then \( y - x > 0 \), so by @cor-archimedean-epsilon there is \( n \in \nN \) with \( 1/n < y - x \); the \( n \) depends on \( x \) and \( y \), through \( y - x \). By @lem-integer-part, let \( m \coloneqq \floor{nx} + 1 \), an integer. Then \( m - 1 \le nx < m \). Therefore
\[
    nx < m \le nx + 1 < nx + n(y - x) = ny ,
\]
where the last inequality uses \( 1 < n(y - x) \), which is \( 1/n < y - x \) multiplied by \( n > 0 \). Dividing by \( n > 0 \) gives \( x < m/n < y \). Since \( m \in \nZ \) and \( n \in \nN \), \( q \coloneqq m/n \) is rational. This proves the theorem.
:::

::: {#exm-rational-between}
[Running the proof]

Follow the proof of @thm-rationals-dense to find a rational number between \( \sqrt{2} \) and \( \tfrac32 \).
:::

::: {.solution}
*Step ①: the spacing.* We need \( 1/n < \tfrac32 - \sqrt{2} \), that is, \( \sqrt{2} < \tfrac32 - \tfrac1n \). By @thm-ordered-field-rules (g), applied to the positive numbers \( \sqrt{2} \) and \( \tfrac32 - \tfrac1n \), this holds exactly when \( 2 < (\tfrac32 - \tfrac1n)^2 \). For \( n = 12 \), \( \tfrac32 - \tfrac1{12} = \tfrac{17}{12} \) and \( (\tfrac{17}{12})^2 = \tfrac{289}{144} > \tfrac{288}{144} = 2 \), so \( n = 12 \) works. (For \( n = 11 \), \( (\tfrac{31}{22})^2 = \tfrac{961}{484} < 2 \), so \( 12 \) is the least \( n \) that works, but any \( n \ge 12 \) would do.)

*Step ②: the first mark past \( x \).* We need \( \floor{12\sqrt{2}} \). Since \( 16^2 = 256 \le 288 = (12\sqrt{2})^2 < 289 = 17^2 \), @thm-ordered-field-rules (g) gives \( 16 \le 12\sqrt{2} < 17 \), so \( \floor{12\sqrt{2}} = 16 \) and \( m = 17 \).

*Step ③: the answer.* The proof guarantees \( \sqrt{2} < \tfrac{17}{12} < \tfrac32 \). Directly: \( (\tfrac{17}{12})^2 = \tfrac{289}{144} > 2 \) gives the left inequality, and \( \tfrac{17}{12} < \tfrac{18}{12} \) gives the right one.
:::

The irrationals are just as widely spread. The trick is to shift the rationals by \( \sqrt{2} \).

::: {#cor-irrationals-dense}
Let \( x, y \in \nR \) with \( x < y \). There is an irrational number \( z \) with \( x < z < y \).
:::

::: {.proof}
Since \( x - \sqrt{2} < y - \sqrt{2} \), @thm-rationals-dense gives \( q \in \nQ \) with \( x - \sqrt{2} < q < y - \sqrt{2} \). Let \( z \coloneqq q + \sqrt{2} \). Then \( x < z < y \). If \( z \) were rational, then \( \sqrt{2} = z - q \) would be a difference of rationals, hence rational, contradicting @thm-sqrt2-irrational. So \( z \) is irrational.
:::

This is why the existence of \( \sqrt{2} \) came first in this section: the proof of @cor-irrationals-dense needs one irrational number to shift by, and @thm-sqrt2-exists supplies it.

::: {.check}
Name a rational number between \( \sqrt{2} \) and \( 1.415 \), and an irrational number between \( 0 \) and \( 10^{-6} \). Justify both.
:::

::: {.solution}
*Rational:* \( 1.4143 \). Its square is \( 2.00024449 > 2 \), so \( 1.4143 > \sqrt{2} \) by @thm-ordered-field-rules (g), and \( 1.4143 < 1.415 \).

*Irrational:* \( z \coloneqq \sqrt{2} \cdot 10^{-7} \). Since \( 1 < \sqrt{2} < 2 \), we get \( 0 < z < 2 \cdot 10^{-7} < 10^{-6} \). If \( z \) were rational, then \( \sqrt{2} = 10^7 z \) would be rational, contradicting @thm-sqrt2-irrational.
:::

::: {.warning}
"Dense" does not mean "next to each other". There is no smallest positive rational number and no "next rational after \( 0 \)": if \( q > 0 \) is rational, then \( q/2 \) is a smaller positive rational. The same holds for irrationals: if \( z > 0 \) is irrational, so is \( z/2 \), and it is smaller. Between any two distinct rationals there are infinitely many more, and between any two distinct reals there are rationals and irrationals alike.
:::

Density is what makes decimals, and more generally rational approximation, possible. Every real number can be pinned down by rationals from below as closely as we like (@exr-density-and-roots-b1). In Part II the word **dense** becomes a notion in any metric space: a set that meets every ball. The rationals in the real line are the model example.

## Exercises

### A. Check your understanding

::: {#exr-density-and-roots-a1}
[A1]

True or false? Give a reason or a counterexample for each.

::: {.enumerate options="label=(\alph*)"}
1. There is a least positive irrational number.
2. Between any two distinct rational numbers there is an irrational number.
3. Between any two distinct irrational numbers there is a rational number.
4. Every non-empty set of rationals that is bounded above has a supremum in \( \nR \), and that supremum is rational.
5. In the proof of @thm-nth-root, the constant \( C \) depends on \( h \).
:::
:::

::: {.solution}
(a) False. If \( z > 0 \) is irrational, then \( z/2 \) is positive, smaller than \( z \), and irrational (if \( z/2 \) were rational, so would be \( z = 2 \cdot (z/2) \)).

(b) True, by @cor-irrationals-dense applied to the two rationals.

(c) True, by @thm-rationals-dense applied to the two irrationals.

(d) False. The set \( A \coloneqq \{ x \in \nQ : x > 0, \ x^2 < 2 \} \) is non-empty and bounded above by \( 2 \), so it has a supremum \( s \in \nR \) by @ax-least-upper-bound. If \( s \) were rational, it would be a rational upper bound of \( A \) that is at most every real upper bound, and in particular at most every rational one. So \( s \) would be a supremum of \( A \) in \( \nQ \), contradicting @thm-no-rational-sup-sqrt2. (In fact \( s = \sqrt{2} \).)

(e) False. \( C = n(s + 1)^{n-1} \) depends only on \( n \) and \( s \). It has to be independent of \( h \), because \( h \) is then chosen in terms of \( C \).
:::

### B. Practice

::: {#exr-density-and-roots-b1}
[B1: Every real number is a supremum of rationals]

Let \( x \in \nR \). Prove that \( x = \sup \{ q \in \nQ : q < x \} \).
:::

::: {.solution}
Let \( A \coloneqq \{ q \in \nQ : q < x \} \). By @thm-rationals-dense applied to \( x - 1 < x \), there is a rational in \( (x - 1, x) \), so \( A \) is non-empty. By definition every element of \( A \) is less than \( x \), so \( x \) is an upper bound of \( A \).

Let \( \varepsilon > 0 \). By @thm-rationals-dense applied to \( x - \varepsilon < x \), there is \( q \in \nQ \) with \( x - \varepsilon < q < x \). Then \( q \in A \) and \( q > x - \varepsilon \). By @thm-sup-epsilon, \( x = \sup A \).
:::

::: {#exr-density-and-roots-b2}
[B2: The square root of three]

Prove that there is exactly one real \( s > 0 \) with \( s^2 = 3 \), following the proof of @thm-sqrt2-exists. Give the explicit \( h \) in each case, and check that it works.
:::

::: {.solution}
Let \( S \coloneqq \{ x \in \nR : x > 0, \ x^2 < 3 \} \). Then \( 1 \in S \), and if \( x \ge 2 \), then \( x^2 \ge 4 > 3 \); so \( S \) is non-empty and bounded above by \( 2 \). By @ax-least-upper-bound, \( s \coloneqq \sup S \) exists, and \( s \ge 1 \).

*Case \( s^2 < 3 \).* Let \( h \coloneqq (3 - s^2)/(4s + 2) \), which uses half of the room \( 3 - s^2 \). Then \( h > 0 \). Since \( s \ge 1 \), we have \( 3 - s^2 \le 2 \) and \( 4s + 2 \ge 6 \), so \( h \le \tfrac13 \le 1 \), and hence \( h^2 \le h \). Therefore
\[
\begin{aligned}
    (s + h)^2 &\le s^2 + (2s + 1)h = s^2 + \tfrac{3 - s^2}{2} \\
              &= \tfrac{3 + s^2}{2} < 3 ,
\end{aligned}
\]
where the last step uses \( s^2 < 3 \).
So \( s + h \in S \) and \( s + h > s \), contradicting that \( s \) is an upper bound.

*Case \( s^2 > 3 \).* Let \( h \coloneqq (s^2 - 3)/(2s) > 0 \). Then \( s - h = (s^2 + 3)/(2s) > 0 \) and \( (s - h)^2 = s^2 - 2sh + h^2 = 3 + h^2 > 3 \). If \( x \in S \) had \( x > s - h \), then \( x^2 > (s - h)^2 > 3 \), which is impossible. So \( s - h \) is an upper bound of \( S \) smaller than \( s \), contradicting that \( s \) is the least upper bound.

By trichotomy \( s^2 = 3 \). Uniqueness is as in @thm-sqrt2-exists: two distinct positive numbers have distinct squares.
:::

::: {#exr-density-and-roots-b3}
[B3: The cube root of five]

Prove that there is exactly one real \( s > 0 \) with \( s^3 = 5 \). Hence show that \( 1.70 < s < 1.71 \).
:::

::: {.solution}
By @thm-nth-root with \( a = 5 \) and \( n = 3 \), there is exactly one \( s > 0 \) with \( s^3 = 5 \).

Exact arithmetic gives \( 1.70^3 = 4.913 < 5 \) and \( 1.71^3 = 5.000211 > 5 \). By the claim in the proof of @thm-nth-root, \( x \mapsto x^3 \) is strictly increasing on \( [0, \infty) \). If \( s \le 1.70 \), then \( s^3 \le 4.913 < 5 \); if \( s \ge 1.71 \), then \( s^3 \ge 5.000211 > 5 \). Both contradict \( s^3 = 5 \), so \( 1.70 < s < 1.71 \).
:::

### C. Going deeper

::: {#exr-density-and-roots-c1}
[C1: Exit check: the square root of two, in both fields]

::: {.enumerate options="label=(\alph*)"}
1. Prove that there is a real number \( s > 0 \) with \( s^2 = 2 \).
2. Prove that the set \( \{ x \in \nQ : x > 0, \ x^2 < 2 \} \) has no supremum in \( \nQ \).
3. Both proofs use the same two values of \( h \). Explain in two or three sentences why the same computation yields an existence theorem in \( \nR \) and a non-existence theorem in \( \nQ \).
:::
:::

::: {.solution}
(a) This is @thm-sqrt2-exists. Let \( S \coloneqq \{ x \in \nR : x > 0, \ x^2 < 2 \} \); it contains \( 1 \) and is bounded above by \( 2 \), so \( s \coloneqq \sup S \) exists by @ax-least-upper-bound, and \( s \ge 1 \). If \( s^2 < 2 \), then \( h \coloneqq (2 - s^2)/(4s + 2) \) satisfies \( 0 < h \le \tfrac16 \), so \( h^2 \le h \) and \( (s + h)^2 \le s^2 + (2s + 1)h = 1 + s^2/2 < 2 \), and \( s + h \in S \) exceeds the upper bound \( s \): impossible. If \( s^2 > 2 \), then \( h \coloneqq (s^2 - 2)/(2s) \) satisfies \( s - h = (s^2 + 2)/(2s) > 0 \) and \( (s - h)^2 = 2 + h^2 > 2 \); every \( x \in S \) then satisfies \( x \le s - h \), since \( x > s - h \) would give \( x^2 > 2 \). So \( s - h < s \) is an upper bound, contradicting (S2). By trichotomy \( s^2 = 2 \).

(b) Let \( A \coloneqq \{ x \in \nQ : x > 0, \ x^2 < 2 \} \), and suppose \( r \in \nQ \) is a supremum of \( A \) in \( \nQ \), that is, a rational upper bound of \( A \) that is at most every rational upper bound. As \( 1 \in A \), \( r \ge 1 \). By @thm-sqrt2-irrational, \( r^2 \ne 2 \).

If \( r^2 < 2 \), let \( h \coloneqq (2 - r^2)/(4r + 2) \). This is rational, and the computation of (a) gives \( (r + h)^2 < 2 \). So \( r + h \in A \) and \( r + h > r \), contradicting that \( r \) is an upper bound.

If \( r^2 > 2 \), let \( h \coloneqq (r^2 - 2)/(2r) \). Then \( r - h = (r^2 + 2)/(2r) \) is rational and positive, with \( (r - h)^2 = 2 + h^2 > 2 \). As in (a), every \( x \in A \) satisfies \( x \le r - h \), so \( r - h \) is a rational upper bound of \( A \) smaller than \( r \), contradicting the choice of \( r \).

Both cases are impossible, so \( A \) has no supremum in \( \nQ \).

(c) The computation shows, in any ordered field, that a supremum of the set cannot have square less than \( 2 \) or greater than \( 2 \). In \( \nR \) the axiom guarantees that a supremum exists, so its square must be \( 2 \): existence. In \( \nQ \) no element has square \( 2 \) (@thm-sqrt2-irrational), so no case is left, and no supremum can exist. For rational \( r \) the values of \( h \) are rational, which is why the argument stays inside \( \nQ \).
:::

::: {#exr-density-and-roots-c2}
[C2: Dyadic rationals]

A **dyadic rational** is a number of the form \( m/2^k \) with \( m \in \nZ \) and \( k \in \nN \). Prove that between any two real numbers \( x < y \) there is a dyadic rational.

*Hint: compare \( 2^k \) with \( k \).*
:::

::: {.solution}
First, \( 2^k > k \) for every \( k \in \nN \), by induction: \( 2^1 = 2 > 1 \), and if \( 2^k > k \), then \( 2^{k+1} = 2^k + 2^k > k + 1 \), since \( 2^k \ge 1 \).

Let \( x < y \). By @cor-archimedean-epsilon there is \( k \in \nN \) with \( 1/k < y - x \); the \( k \) depends on \( y - x \). Then \( 1/2^k < 1/k < y - x \). By @lem-integer-part, let \( m \coloneqq \floor{2^k x} + 1 \). Then \( m - 1 \le 2^k x < m \), and
\[
    2^k x < m \le 2^k x + 1 < 2^k x + 2^k (y - x) = 2^k y ,
\]
using \( 1 < 2^k (y - x) \). Dividing by \( 2^k > 0 \) gives \( x < m/2^k < y \).

The proof is that of @thm-rationals-dense with the ruler of step \( 1/n \) replaced by one of step \( 1/2^k \). Only the choice of step size changed; any family of steps that can be made smaller than every \( \varepsilon > 0 \) would do.
:::

::: {#exr-density-and-roots-c3}
[C3: Find the faulty line]

A student proves @thm-rationals-dense as follows. Let \( x < y \).

::: {.enumerate options="label=(\arabic*)"}
1. Let \( R \coloneqq \{ r \in \nQ : r > x \} \). By @thm-naturals-unbounded some natural number exceeds \( x \), so \( R \) is non-empty.
2. By well-ordering, \( R \) has a least element \( q \).
3. By @cor-archimedean-epsilon, choose \( n \in \nN \) with \( 1/n < y - x \).
4. Since \( q - 1/n \) is rational and smaller than the least element \( q \) of \( R \), it is not in \( R \). So \( q - 1/n \le x \), and hence \( q \le x + 1/n < y \).
5. Therefore \( q \in \nQ \) and \( x < q < y \).
:::

Find the line that fails and say why. Show that for \( x = 0 \) the set \( R \) has no least element. Then repair the proof by changing \( R \) so that the faulty line becomes correct.
:::

::: {.solution}
Line (2) fails. Well-ordering says that a non-empty subset of \( \nN \) has a least element. The set \( R \) is a set of rationals, not of natural numbers, and it need not have a least element. For \( x = 0 \), \( R \) is the set of positive rationals; if \( q \in R \), then \( q/2 \in R \) and \( q/2 < q \). So no element of \( R \) is least. Lines (3)–(5) are correct once a least element is available.

*Repair.* Fix \( n \) first, as in line (3), and replace \( R \) by a set of integers: \( R_n \coloneqq \{ m \in \nZ : m/n > x \} \). By @lem-integer-part, its least element is \( m \coloneqq \floor{nx} + 1 \): indeed \( m/n > x \), while \( (m - 1)/n \le x \). Now line (4) holds with \( q \coloneqq m/n \): since \( (m - 1)/n = q - 1/n \le x \), we get \( q \le x + 1/n < y \). This is the proof of @thm-rationals-dense. The point is that the step \( 1/n \) is fixed first, so the candidates \( m/n \) form a copy of the integers, where "least" makes sense.
:::
