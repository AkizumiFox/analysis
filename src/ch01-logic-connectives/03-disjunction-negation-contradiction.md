# Or, Not, and Contradiction

With the rules for "and" and "implies" (@def-rules-conjunction, @def-rules-implication) we can already derive a fair amount, but two of the commonest moves in mathematics are still missing. One is the split into cases: "if \( x \ge 0 \), then …; if \( x < 0 \), then …". The other is the proof of a negative statement, such as "no rational number has square \( 2 \)", by showing that its opposite leads to something impossible. This section gives the rules behind both. With them we prove that \( \sqrt{2} \) is irrational, and we find out where the strangest feature of implication comes from.

## The rules for "or"

The absolute value of a real number is defined in two cases:
\[
\abs{x} \coloneqq
\begin{cases}
x & \text{if } x \ge 0, \\
-x & \text{if } x < 0 .
\end{cases}
\]
So nearly every argument about \( \abs{x} \) begins by splitting into the two cases, which is legitimate because every real number satisfies \( x \ge 0 \) or \( x < 0 \). The split uses a disjunction, and what it does with it is the elimination rule for "or".

*To use "\( P \) or \( Q \)", reach your goal from \( P \), and reach it again from \( Q \).*

::: {#def-rules-disjunction}
[Rules for Disjunction]

- \( \rulename{\vee I} \) (**or-introduction**). If \( P \) stands on an available line, we may write \( P \vee Q \), and we may write \( Q \vee P \), for **any** statement \( Q \).
- \( \rulename{\vee E} \) (**or-elimination**, or **proof by cases**). Suppose \( P \vee Q \) stands on an available line, and there are two available boxes: one opened by the assumption \( P \), the other by the assumption \( Q \), each containing the **same** statement \( R \) as a line of its own. Then we may write \( R \). The justification cites the disjunction and both boxes, as in \( \rulename{\vee E}\ 1, \lines{3}{5}, \lines{6}{8} \).
:::

In words: \( \rulename{\vee I} \) weakens a statement. Knowing \( x = 0 \), we know "\( x < 0 \) or \( x = 0 \)", which is \( x \le 0 \); we have thrown information away, but sometimes the weaker form is exactly what a definition asks for. \( \rulename{\vee E} \) is the case split. The disjunction \( P \vee Q \) does not say which of \( P \), \( Q \) holds, so we must be ready for both, and each case gets its own box, since each case's assumption is temporary. The one thing both boxes must share is the conclusion \( R \): whichever case we are in, \( R \) holds, and so \( R \) holds.

The facts about \( \le \) and the absolute value used below are school algebra. Chapter 8 proves all of them from the axioms of an ordered field; here we take them as known.

::: {#exm-abs-product-cases}
[The absolute value of a product]

Let \( x \) and \( y \) be real numbers. Prove that \( \abs{xy} = \abs{x}\abs{y} \).
:::

::: {.solution}
We use that every real number \( a \) satisfies \( a \ge 0 \) or \( a < 0 \), and that \( \abs{a} = -a \) whenever \( a \le 0 \) (for \( a < 0 \) this is the definition, and for \( a = 0 \) both sides are \( 0 \)).

The number \( x \) satisfies \( x \ge 0 \) or \( x < 0 \), and we argue by cases \( [\rulename{\vee E}] \). Inside each case, \( y \ge 0 \) or \( y < 0 \), and we argue by cases again.

*Case \( x \ge 0 \), \( y \ge 0 \).* Then \( xy \ge 0 \), so \( \abs{xy} = xy = \abs{x}\abs{y} \).

*Case \( x \ge 0 \), \( y < 0 \).* Then \( xy \le 0 \), so \( \abs{xy} = -xy = x \cdot (-y) = \abs{x}\abs{y} \).

*Case \( x < 0 \), \( y \ge 0 \).* Then \( xy \le 0 \), so \( \abs{xy} = -xy = (-x) \cdot y = \abs{x}\abs{y} \).

*Case \( x < 0 \), \( y < 0 \).* Then \( xy > 0 \), so \( \abs{xy} = xy = (-x)(-y) = \abs{x}\abs{y} \).

Each inner case split reaches \( \abs{xy} = \abs{x}\abs{y} \), so each outer case does, and hence the equation holds.
:::

The structure is two uses of \( \rulename{\vee E} \), one inside each box of the other: four boxes in all, every one of them ending in the same equation. The second case needed the remark about \( a \le 0 \): when \( x = 0 \) and \( y < 0 \), the product is \( 0 \), not negative, and the case would otherwise have a hole.

A case split need not be the obvious one. The triangle inequality has an equally short proof with two cases, if we split on the sign of the right quantity.

::: {#exm-triangle-inequality-cases}
[The triangle inequality by cases]

Let \( x \) and \( y \) be real numbers. Prove that \( \abs{x + y} \le \abs{x} + \abs{y} \).
:::

::: {.solution}
First, every real number \( a \) satisfies \( a \le \abs{a} \) and \( -a \le \abs{a} \). This is itself a proof by cases \( [\rulename{\vee E}] \): if \( a \ge 0 \), then \( \abs{a} = a \), so \( a \le \abs{a} \), and \( -a \le 0 \le a = \abs{a} \); if \( a < 0 \), then \( \abs{a} = -a \), so \( -a \le \abs{a} \), and \( a < 0 < -a = \abs{a} \).

Now \( x + y \ge 0 \) or \( x + y < 0 \), and we argue by cases \( [\rulename{\vee E}] \).

*Case \( x + y \ge 0 \).* Then \( \abs{x + y} = x + y \le \abs{x} + \abs{y} \), adding \( x \le \abs{x} \) and \( y \le \abs{y} \).

*Case \( x + y < 0 \).* Then \( \abs{x + y} = -x - y = (-x) + (-y) \le \abs{x} + \abs{y} \), adding \( -x \le \abs{x} \) and \( -y \le \abs{y} \).

Both cases reach \( \abs{x + y} \le \abs{x} + \abs{y} \), so it holds.
:::

::: {.warning}
A case split must cover every possibility. A common faulty proof of the triangle inequality treats "\( x \ge 0 \) and \( y \ge 0 \)" and "\( x < 0 \) and \( y < 0 \)", checks both, and stops. The disjunction of these two cases is not a fact: \( x = 1 \), \( y = -1 \) satisfies neither. So there is no line \( P \vee Q \) for \( \rulename{\vee E} \) to cite, and the rule was never legally applied. The missing mixed-sign cases are the interesting ones: at \( x = 1 \), \( y = -1 \) the inequality reads \( 0 \le 2 \), and it is strict.
:::

## The rules for "not"

How can a proof establish that something is **not** the case? To show that no rational number has square \( 2 \), we cannot inspect the rational numbers one by one. What a mathematician does is to suppose the opposite and show that it leads to something impossible: "suppose \( r \) is rational and \( r^2 = 2 \); … this is a contradiction; hence …". The rules for negation make this precise, with the statement \( \bot \) from Section 1.1, read "contradiction", as the impossible thing.

*To prove "not \( P \)", assume \( P \) and reach a contradiction.*

::: {#def-rules-negation}
[Rules for Negation and Contradiction]

- \( \rulename{\neg I} \) (**not-introduction**). Open a box with the assumption \( P \). If \( \bot \) is reached as a line of that box, not inside a further box, we may close the box and write \( \neg P \).
- \( \rulename{\neg E} \) (**not-elimination**). If \( P \) and \( \neg P \) stand on available lines, we may write \( \bot \).
- \( \rulename{\bot E} \) (**contradiction-elimination**, or **ex falso**). If \( \bot \) stands on an available line, we may write **any** statement.
:::

In words. \( \rulename{\neg I} \) has the same shape as \( \rulename{{\to}I} \) with the goal \( \bot \): assume \( P \), reach the impossible, discharge. It is the rule that proves every negative statement, from "\( x^2 + 1 \ne 0 \)" to "there is no largest prime". \( \rulename{\neg E} \) says how to **use** a negation: \( \neg P \) is exactly what clashes with \( P \), and the clash is \( \bot \). \( \rulename{\bot E} \) says what \( \bot \) is good for. A line \( \bot \) can only be reached in a situation that cannot occur, and in such a situation there is nothing left to be careful about.

In derivations about numbers, the clash usually comes from a school fact. For real numbers \( a \) and \( b \), the statement \( a \ge b \) is the negation of \( a < b \): exactly one of them holds. So from \( x^2 < 0 \) and the fact \( x^2 \ge 0 \), which is \( \neg(x^2 < 0) \), the rule \( \rulename{\neg E} \) gives \( \bot \). Similarly \( a \ne b \) means \( \neg(a = b) \), and "odd" means "not even" for integers, since every integer is exactly one of the two.

::: {#exm-square-plus-one}
[A negative statement proved by not-introduction]

Let \( x \) be a real number. Prove that \( x^2 + 1 \ne 0 \), naming the rules.
:::

::: {.solution}
The goal \( x^2 + 1 \ne 0 \) is \( \neg(x^2 + 1 = 0) \), so we use \( \rulename{\neg I} \). Suppose \( x^2 + 1 = 0 \). Then \( x^2 = -1 \), so \( x^2 < 0 \). But \( x^2 \ge 0 \), that is, \( \neg(x^2 < 0) \), so we have a contradiction \( [\rulename{\neg E}] \). Hence \( x^2 + 1 \ne 0 \) \( [\rulename{\neg I}] \).
:::

::: {.remark}
Many books call every argument of this shape a "proof by contradiction". Section 1.5 separates it from a second rule that looks almost the same and is not, and it will matter there which of the two a proof uses.
:::

## The contrapositive

With negation available, we can prove the most useful single fact about implication. An implication \( P \to Q \) promises \( Q \) whenever \( P \). So if \( Q \) fails, \( P \) must have failed too, or the promise would have been broken.

::: {#prp-contrapositive}
[Contrapositive]

\( P \to Q \vdash \neg Q \to \neg P \).
:::

::: {.idea}
The goal is an implication, so assume \( \neg Q \). The new goal \( \neg P \) is a negation, so assume \( P \) and aim at \( \bot \). With \( P \) available, the premise gives \( Q \), which clashes with \( \neg Q \).
:::

::: {.proof}
The following is a derivation with premise \( P \to Q \) and last line \( \neg Q \to \neg P \).
\[
\begin{array}{r l l}
1 & P \to Q & \text{premise} \\
2 & \fsc \fhyp{\neg Q} & \text{assumption} \\
3 & \fsc \fsc \fhyp{P} & \text{assumption} \\
4 & \fsc \fsc Q & \rulename{{\to}E}\ 1, 3 \\
5 & \fsc \fsc \bot & \rulename{\neg E}\ 4, 2 \\
6 & \fsc \neg P & \rulename{\neg I}\ \lines{3}{5} \\
7 & \neg Q \to \neg P & \rulename{{\to}I}\ \lines{2}{6}
\end{array}
\]
Line 5 may cite line 2, since the only box containing line 2, the box 2–6, also contains line 5. This proves the proposition.
:::

The statement \( \neg Q \to \neg P \) is the **contrapositive** of \( P \to Q \). The derivation uses \( \rulename{{\to}I} \), \( \rulename{{\to}E} \), \( \rulename{\neg I} \) and \( \rulename{\neg E} \), and nothing else. We stress this because the reverse passage, from \( \neg Q \to \neg P \) back to \( P \to Q \), is a different matter: Section 1.5 shows that it needs a rule we have not yet met. The contrapositive is how one proves an implication whose hypothesis is hard to use directly, as in Argument A of Section 1.1, where "\( n^2 \) is even" gave nothing to work with and "\( n \) is odd" gave a formula.

Section 1.1's Argument A also used a second pattern: a case split in which one case is impossible. "Every integer is odd or even; \( n \) is not odd; so \( n \) is even." This pattern is common enough to record.

::: {#prp-disjunctive-syllogism}
[Disjunctive Syllogism]

\( P \vee Q, \; \neg P \vdash Q \).
:::

::: {.proof}
The following is a derivation with premises \( P \vee Q \) and \( \neg P \), and last line \( Q \).
\[
\begin{array}{r l l}
1 & P \vee Q & \text{premise} \\
2 & \neg P & \text{premise} \\
3 & \fsc \fhyp{P} & \text{assumption} \\
4 & \fsc \bot & \rulename{\neg E}\ 3, 2 \\
5 & \fsc Q & \rulename{\bot E}\ 4 \\
  & & \\[-1.5ex]
6 & \fsc \fhyp{Q} & \text{assumption} \\
7 & Q & \rulename{\vee E}\ 1, \lines{3}{5}, \lines{6}{6}
\end{array}
\]
The two boxes 3–5 and 6–6 are separate, as the break in the bar shows; the second consists of its assumption alone, which is already the statement \( Q \) that \( \rulename{\vee E} \) needs. This proves the proposition.
:::

In the first box, the case \( P \) is impossible given \( \neg P \), and \( \rulename{\bot E} \) turns that impossibility into the required conclusion. This is how "this case cannot occur" is written as a rule: a case that cannot occur may be closed with any conclusion we like, in particular the one the other case reaches.

## Squares of even numbers, and the square root of two

We can now prove the fact from Section 1.1, with every rule named. Three school facts about integers enter as premises:

::: {.enumerate options="label=(E\arabic*)"}
1. every integer is odd or even;
2. no integer is both even and odd;
3. the square of an odd integer is odd.
:::

The third is a computation: if \( n = 2k + 1 \) for an integer \( k \), then
\[
n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1 ,
\]
and \( 2k^2 + 2k \) is an integer. Naming the integer \( k \) is a quantifier step ("there is a \( k \) with \( n = 2k + 1 \); take one"), whose rule comes in Chapter 2.

::: {#thm-square-even-implies-even}
[Even Square, Even Number]

Let \( n \) be an integer. If \( n^2 \) is even, then \( n \) is even.
:::

::: {.idea}
The hypothesis "\( n^2 \) is even" hands us nothing to compute with, while "\( n \) is odd" hands us \( n = 2k + 1 \). So we turn (E3) around by @prp-contrapositive: an integer whose square fails to be odd fails to be odd itself. Then "even or odd" with one option ruled out leaves "even".
:::

::: {.proof}
Suppose \( n^2 \) is even \( [\text{assumption for } \rulename{{\to}I}] \). By (E3), \( n \) odd implies \( n^2 \) odd, so @prp-contrapositive gives: \( n^2 \) not odd implies \( n \) not odd. Since \( n^2 \) is even, (E2) rules out \( n^2 \) odd. Hence \( n \) is not odd \( [\rulename{{\to}E}] \). By (E1), \( n \) is odd or \( n \) is even, and \( n \) is not odd, so @prp-disjunctive-syllogism gives that \( n \) is even. This proves that if \( n^2 \) is even, then \( n \) is even \( [\rulename{{\to}I}] \).
:::

Every step is one of the rules so far, or a derived result built from them. In particular, although the argument feels like "suppose not", it never assumes that \( n \) is odd in order to reach a contradiction. It uses a contrapositive and a case split with an impossible case. The difference will matter in Section 1.5.

The theorem is the key to one of the oldest proofs in mathematics. Its shape is \( \rulename{\neg I} \): the claim is negative, so we assume its opposite and look for \( \bot \). The school fact it needs is about writing fractions:

**(L)** Every rational number can be written as \( p/q \) with \( p \) and \( q \) integers, \( q \ne 0 \), and \( p \) and \( q \) **not both even**.

This holds because a fraction whose numerator and denominator are both even can be reduced by \( 2 \), and the reduction cannot go on for ever, since the denominator shrinks each time. Making "cannot go on for ever" precise needs induction, which comes in Chapter 4; we take (L) as known.

::: {#thm-sqrt2-irrational}
[Irrationality of the Square Root of Two]

There is no rational number whose square is \( 2 \). In other words, \( \sqrt{2} \) is irrational.
:::

::: {.idea}
Fix a rational number \( r \) and prove the negative statement \( r^2 \ne 2 \) by \( \rulename{\neg I} \): assume \( r^2 = 2 \) and hunt for \( \bot \). Write \( r = p/q \) as in (L), so that the equation becomes \( p^2 = 2q^2 \). The only hypothesis with any bite is "not both even", so the contradiction must come from showing that both \( p \) and \( q \) are even, and @thm-square-even-implies-even is the tool for that, used twice. *Before reading on: which line will clash with which?*
:::

::: {.proof}
Let \( r \) be a rational number, and suppose \( r^2 = 2 \) \( [\text{assumption for } \rulename{\neg I}] \). By (L), \( r = p/q \) for integers \( p \) and \( q \) with \( q \ne 0 \), not both even. Then \( p^2 = r^2 q^2 = 2q^2 \), so \( p^2 \) is even. By @thm-square-even-implies-even, \( p \) is even, say \( p = 2m \) for an integer \( m \). Then \( 4m^2 = 2q^2 \), so \( q^2 = 2m^2 \), and \( q^2 \) is even. By @thm-square-even-implies-even again, \( q \) is even. So \( p \) and \( q \) are both even \( [\rulename{\wedge I}] \), while they were chosen not both even; this is a contradiction \( [\rulename{\neg E}] \). Hence \( r^2 \ne 2 \) \( [\rulename{\neg I}] \).

Since \( r \) was an arbitrary rational number, no rational number has square \( 2 \). This proves the theorem.
:::

The last sentence passes from "the fixed but arbitrary \( r \)" to "every rational number", which is the quantifier rule \( \rulename{\forall I} \) of Chapter 2. Everything before it is propositional. Notice also what the proof does **not** need: that \( \sqrt{2} \) exists as a real number. The theorem is a statement about rational numbers only, and Chapter 8 uses it in exactly this form, as evidence that the rational numbers have a gap where \( \sqrt{2} \) should be.

## Vacuous truth

We can now answer the question that makes many readers distrust logic. Is the sentence

> if \( x^2 < 0 \), then \( x = 7 \)

true, for a real number \( x \)? The hypothesis never holds, and the conclusion has nothing to do with it. The rules give a definite answer.

::: {#prp-ex-falso}
[Contradictory Premises Prove Anything]

\( P, \; \neg P \vdash Q \).
:::

::: {.proof}
The derivation
\[
\begin{array}{r l l}
1 & P & \text{premise} \\
2 & \neg P & \text{premise} \\
3 & \bot & \rulename{\neg E}\ 1, 2 \\
4 & Q & \rulename{\bot E}\ 3
\end{array}
\]
has premises \( P \) and \( \neg P \) and last line \( Q \). This proves the proposition.
:::

::: {#prp-vacuous-implication}
[Vacuous Implication]

\( \neg P \vdash P \to Q \).
:::

::: {.proof}
The derivation
\[
\begin{array}{r l l}
1 & \neg P & \text{premise} \\
2 & \fsc \fhyp{P} & \text{assumption} \\
3 & \fsc \bot & \rulename{\neg E}\ 2, 1 \\
4 & \fsc Q & \rulename{\bot E}\ 3 \\
5 & P \to Q & \rulename{{\to}I}\ \lines{2}{4}
\end{array}
\]
has premise \( \neg P \) and last line \( P \to Q \). This proves the proposition.
:::

Apply this with \( P \): "\( x^2 < 0 \)" and \( Q \): "\( x = 7 \)". The premise \( \neg(x^2 < 0) \) holds for every real \( x \), so "if \( x^2 < 0 \), then \( x = 7 \)" is derivable, and the derivation is the ordinary proof: *suppose \( x^2 < 0 \); this contradicts \( x^2 \ge 0 \); so this case cannot occur, and in it anything holds, in particular \( x = 7 \)*. An implication whose hypothesis is false is called **vacuously true**. Nothing about it was decided by convention. It is forced by two rules that each look harmless: \( \rulename{{\to}I} \), which proves an implication by assuming its hypothesis, and \( \rulename{\bot E} \), which closes an impossible case.

*The rule \( \rulename{\bot E} \) is where the strange row of the truth table comes from.*

Everyday language agrees, once we listen to it. Suppose a friend says: "if you finish the exercises by Friday, I will buy you lunch". You do not finish them. Whatever your friend does on Friday, the promise has not been broken, and a promise that has not been broken has been kept. The implication was never tested, so it cannot have failed.

Vacuous truth is not a curiosity; it is what makes case splits work. In @prp-disjunctive-syllogism, the impossible case was closed by \( \rulename{\bot E} \). Without that rule, "\( n \) is even or odd, and not odd, so even" could not be proved. Section 1.6 reads the row of the truth table for \( \to \) with false hypothesis off exactly this rule.

::: {.check}
Is \( \neg(P \vee Q) \vdash \neg P \) true? If so, give the derivation and name its rules.
:::

::: {.solution}
Yes. The goal \( \neg P \) is a negation, so assume \( P \) and aim at \( \bot \); \( \rulename{\vee I} \) turns \( P \) into \( P \vee Q \), which clashes with the premise.
\[
\begin{array}{r l l}
1 & \neg(P \vee Q) & \text{premise} \\
2 & \fsc \fhyp{P} & \text{assumption} \\
3 & \fsc P \vee Q & \rulename{\vee I}\ 2 \\
4 & \fsc \bot & \rulename{\neg E}\ 3, 1 \\
5 & \neg P & \rulename{\neg I}\ \lines{2}{4}
\end{array}
\]
The rules are \( \rulename{\vee I} \), \( \rulename{\neg E} \) and \( \rulename{\neg I} \). In words: if neither \( P \) nor \( Q \) holds, then in particular \( P \) does not.
:::

## What the rules sound like

Here are the rows of the rule, phrase and Lean table for this section's rules. As before, the last column is for readers who use a proof assistant, and nothing depends on it.

| Rule | You write | Lean |
|------|--------------------------------------|------------------------|
| \( \rulename{\vee I} \) | "In particular, \( P \) or \( Q \)." | `left` / `right` |
| \( \rulename{\vee E} \) | "Case 1: \( P \). … so \( R \). Case 2: \( Q \). … so \( R \). In either case, \( R \)." | `rcases h with hp | hq` |
| \( \rulename{\neg I} \) | "Suppose \( P \). … This is a contradiction. Hence not \( P \)." | `intro hp` (goal `False`) |
| \( \rulename{\neg E} \) | "This contradicts \( \neg P \)." | `exact hn hp` |
| \( \rulename{\bot E} \) | "This case cannot occur." | `exfalso` / `absurd` |

In Lean, \( \neg P \) is defined to be the implication \( P \to \bot \), with \( \bot \) written `False`. That is why the same tactic `intro` performs both \( \rulename{{\to}I} \) and \( \rulename{\neg I} \), and why applying a proof `hn` of \( \neg P \) to a proof `hp` of \( P \) produces `False`, which is \( \rulename{\neg E} \).

## Exercises

### A. Check your understanding

::: {#exr-disjunction-negation-contradiction-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the rules \( \rulename{\vee E} \) and \( \rulename{\neg I} \).
2. Match each sentence, taken from proofs, with the rule it uses: \( \rulename{\vee I} \), \( \rulename{\vee E} \), \( \rulename{\neg I} \), \( \rulename{\neg E} \) or \( \rulename{\bot E} \).
    - "We have \( x < 3 \), so in particular \( x \le 3 \)."
    - "But \( n \) was assumed odd, and we have just shown it is even."
    - "In the case \( n \) even, …; in the case \( n \) odd, …. Either way, \( n^2 + n \) is even."
    - "Suppose \( 0 \) had a reciprocal \( y \). Then \( 1 = 0 \cdot y = 0 \), which is absurd. So \( 0 \) has no reciprocal."
    - "In this case \( x^2 < 0 \), which is impossible, so there is nothing to prove."
3. True or false, with a reason: to prove \( R \) from \( P \vee Q \) by cases, it is enough to derive \( R \) from \( P \).
:::
:::

::: {.solution}
(a) \( \rulename{\vee E} \): if \( P \vee Q \) stands on an available line, and there are available boxes opened by \( P \) and by \( Q \) that both contain the same statement \( R \), then we may write \( R \). \( \rulename{\neg I} \): if a box opened by \( P \) contains \( \bot \), we may close it and write \( \neg P \) (@def-rules-disjunction, @def-rules-negation).

(b) In order: \( \rulename{\vee I} \), since \( x \le 3 \) is \( (x < 3) \vee (x = 3) \); \( \rulename{\neg E} \), since "odd" is "not even", and the clash gives \( \bot \); \( \rulename{\vee E} \); \( \rulename{\neg I} \), since the conclusion is the negative statement "\( 0 \) has no reciprocal", reached by assuming the opposite; \( \rulename{\bot E} \), closing an impossible case with the desired conclusion.

(c) False. \( P \vee Q \) does not say which of \( P \), \( Q \) holds, so \( R \) must also be derived from \( Q \). For example, with \( x \) real, "\( x \ge 0 \) or \( x < 0 \)" and a derivation of \( \abs{x} = x \) from \( x \ge 0 \) does not give \( \abs{x} = x \): it fails at \( x = -1 \).
:::

### B. Practice

::: {#exr-disjunction-negation-contradiction-b1}
[B1: The other disjunctive syllogism]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( P \vee Q, \; \neg Q \vdash P \) by a derivation.
2. Let \( x \) be a real number with \( x^2 = 1 \) and \( x > 0 \). You may use that \( x^2 = 1 \) implies \( x = 1 \) or \( x = -1 \). Deduce that \( x = 1 \), naming the result you use.
:::
:::

::: {.solution}
(a) As in @prp-disjunctive-syllogism, with the roles of the boxes exchanged: now the case \( Q \) is the impossible one.
\[
\begin{array}{r l l}
1 & P \vee Q & \text{premise} \\
2 & \neg Q & \text{premise} \\
3 & \fsc \fhyp{P} & \text{assumption} \\
  & & \\[-1.5ex]
4 & \fsc \fhyp{Q} & \text{assumption} \\
5 & \fsc \bot & \rulename{\neg E}\ 4, 2 \\
6 & \fsc P & \rulename{\bot E}\ 5 \\
7 & P & \rulename{\vee E}\ 1, \lines{3}{3}, \lines{4}{6}
\end{array}
\]

(b) Since \( x^2 = 1 \), we have \( x = 1 \) or \( x = -1 \). Since \( x > 0 \), we have \( x \ne -1 \), because \( -1 < 0 \). By part (a), with \( P \): "\( x = 1 \)" and \( Q \): "\( x = -1 \)", we conclude \( x = 1 \).
:::

::: {#exr-disjunction-negation-contradiction-b2}
[B2: Distributing and over or]

Show that \( P \wedge (Q \vee R) \vdash (P \wedge Q) \vee (P \wedge R) \). Then give the instance for a real number \( x \) with \( P \): "\( x \ne 0 \)", \( Q \): "\( x > 0 \)" and \( R \): "\( x < 0 \)", in words.
:::

::: {.solution}
Take the premise apart, then split on \( Q \vee R \); each case builds one side of the goal and weakens it with \( \rulename{\vee I} \).
\[
\begin{array}{r l l}
1 & P \wedge (Q \vee R) & \text{premise} \\
2 & P & \rulename{\wedge E}\ 1 \\
3 & Q \vee R & \rulename{\wedge E}\ 1 \\
4 & \fsc \fhyp{Q} & \text{assumption} \\
5 & \fsc P \wedge Q & \rulename{\wedge I}\ 2, 4 \\
6 & \fsc (P \wedge Q) \vee (P \wedge R) & \rulename{\vee I}\ 5 \\
  & & \\[-1.5ex]
7 & \fsc \fhyp{R} & \text{assumption} \\
8 & \fsc P \wedge R & \rulename{\wedge I}\ 2, 7 \\
9 & \fsc (P \wedge Q) \vee (P \wedge R) & \rulename{\vee I}\ 8 \\
10 & (P \wedge Q) \vee (P \wedge R) & \rulename{\vee E}\ 3, \lines{4}{6}, \lines{7}{9}
\end{array}
\]
Lines 5 and 8 may cite line 2, which lies in no box.

The instance: if \( x \ne 0 \) and (\( x > 0 \) or \( x < 0 \)), then (\( x \ne 0 \) and \( x > 0 \)) or (\( x \ne 0 \) and \( x < 0 \)). In words: a non-zero number that is positive or negative is a positive non-zero number or a negative non-zero number.
:::

::: {#exr-disjunction-negation-contradiction-b3}
[B3: The larger of two numbers]

For real numbers \( a \) and \( b \), let \( \max(a, b) \coloneqq a \) if \( a \ge b \), and \( \max(a, b) \coloneqq b \) if \( a < b \). Prove that \( \max(a, b) \ge a \) and \( \max(a, b) \ge b \). Hence deduce that \( \max(a, b) \ge \frac{1}{2}(a + b) \): the larger of two numbers is at least their average.
:::

::: {.solution}
We have \( a \ge b \) or \( a < b \), and we argue by cases \( [\rulename{\vee E}] \).

*Case \( a \ge b \).* Then \( \max(a, b) = a \). So \( \max(a, b) \ge a \), since \( a = a \) and \( \ge \) allows equality \( [\rulename{\vee I}] \); and \( \max(a, b) = a \ge b \).

*Case \( a < b \).* Then \( \max(a, b) = b \). So \( \max(a, b) = b > a \), which gives \( \max(a, b) \ge a \) \( [\rulename{\vee I}] \); and \( \max(a, b) = b \ge b \).

In both cases \( \max(a, b) \ge a \) and \( \max(a, b) \ge b \) \( [\rulename{\wedge I}] \), so both hold.

Adding the two inequalities gives \( 2\max(a, b) \ge a + b \), and dividing by \( 2 > 0 \) gives \( \max(a, b) \ge \frac{1}{2}(a + b) \).
:::

::: {#exr-disjunction-negation-contradiction-b4}
[B4: The square root of three]

You may use that every integer can be written as \( 3k \), \( 3k + 1 \) or \( 3k + 2 \) with \( k \) an integer, in one way only, and that every rational number can be written as \( p/q \) with integers \( p \), \( q \), \( q \ne 0 \), and \( p \), \( q \) not both divisible by \( 3 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( n \) is an integer and \( n^2 \) is divisible by \( 3 \), then \( n \) is divisible by \( 3 \).
2. Hence prove that no rational number has square \( 3 \).
:::
:::

::: {.solution}
(a) Suppose \( n^2 \) is divisible by \( 3 \), so \( n^2 \) has the form \( 3j \). The integer \( n \) has the form \( 3k \), \( 3k + 1 \) or \( 3k + 2 \), and we argue by cases \( [\rulename{\vee E}] \).

*Case \( n = 3k \).* Then \( n \) is divisible by \( 3 \), as required.

*Cases \( n = 3k + 1 \) and \( n = 3k + 2 \).* Then
\[
\begin{aligned}
(3k + 1)^2 &= 9k^2 + 6k + 1 = 3(3k^2 + 2k) + 1, \\
(3k + 2)^2 &= 9k^2 + 12k + 4 = 3(3k^2 + 4k + 1) + 1 ,
\end{aligned}
\]
so \( n^2 \) has the form \( 3j' + 1 \) as well as the form \( 3j \). An integer has only one of the three forms, so this is a contradiction \( [\rulename{\neg E}] \), and the case cannot occur. By \( \rulename{\bot E} \), \( n \) is divisible by \( 3 \) in this case too.

All cases give that \( n \) is divisible by \( 3 \), which proves (a). The two impossible cases were closed exactly as in @prp-disjunctive-syllogism.

(b) Let \( r \) be a rational number and suppose \( r^2 = 3 \). Write \( r = p/q \) with \( p \), \( q \) not both divisible by \( 3 \). Then \( p^2 = 3q^2 \), so \( 3 \) divides \( p^2 \), and by (a), \( p = 3m \) for an integer \( m \). Then \( 9m^2 = 3q^2 \), so \( q^2 = 3m^2 \), and by (a) again, \( 3 \) divides \( q \). So \( 3 \) divides both \( p \) and \( q \), contradicting their choice \( [\rulename{\neg E}] \). Hence \( r^2 \ne 3 \) \( [\rulename{\neg I}] \). Since \( r \) was an arbitrary rational number, no rational number has square \( 3 \).
:::

### C. Going deeper

::: {#exr-disjunction-negation-contradiction-c1}
[C1: The square root of six]

Prove that no rational number has square \( 6 \). Use only the facts (E1)–(E3), (L), and @thm-square-even-implies-even, and name the rule at each logical step.

*Hint: after writing \( p = 2m \), you will need to show that \( q \) is even without knowing that \( q^2 \) is even.*
:::

::: {.solution}
Let \( r \) be a rational number and suppose \( r^2 = 6 \) \( [\text{assumption for } \rulename{\neg I}] \). By (L), \( r = p/q \) with integers \( p \), \( q \), \( q \ne 0 \), not both even. Then \( p^2 = 6q^2 = 2(3q^2) \) is even, so \( p \) is even by @thm-square-even-implies-even; write \( p = 2m \). Then \( 4m^2 = 6q^2 \), that is, \( 3q^2 = 2m^2 \), so \( 3q^2 \) is even.

We claim \( q \) is even. By (E1), \( q \) is odd or even, and we rule out odd, so that @prp-disjunctive-syllogism applies. If \( q \) is odd, then \( q^2 \) is odd by (E3), say \( q^2 = 2j + 1 \), and then \( 3q^2 = 6j + 3 = 2(3j + 1) + 1 \) is odd. But \( 3q^2 \) is even, and by (E2) no integer is both; this is \( \bot \) \( [\rulename{\neg E}] \). Hence \( q \) is not odd \( [\rulename{\neg I}] \), and so \( q \) is even.

So \( p \) and \( q \) are both even \( [\rulename{\wedge I}] \), contradicting (L) \( [\rulename{\neg E}] \). Hence \( r^2 \ne 6 \) \( [\rulename{\neg I}] \), and since \( r \) was arbitrary, no rational number has square \( 6 \).
:::

::: {#exr-disjunction-negation-contradiction-c2}
[C2: A proof that proves too much]

Here is a "proof" that \( \sqrt{4} \) is irrational, modeled on @thm-sqrt2-irrational.

> Suppose \( r \) is rational and \( r^2 = 4 \). Write \( r = p/q \) with \( p \), \( q \) integers, \( q \ne 0 \), not both divisible by \( 4 \). Then \( p^2 = 4q^2 \), so \( 4 \) divides \( p^2 \). Since \( n^2 \) divisible by \( 4 \) implies \( n \) divisible by \( 4 \), we get \( p = 4m \). Then \( 16m^2 = 4q^2 \), so \( q^2 = 4m^2 \), and as before \( 4 \) divides \( q \). This contradicts the choice of \( p \) and \( q \). Hence no rational number has square \( 4 \).

::: {.enumerate options="label=(\alph*)"}
1. Explain why the conclusion must be false.
2. Find the step that fails, and show that it fails with a specific integer.
3. Every other step is a correct use of a rule. Which rule turns the "contradiction" into the conclusion, and why is the argument still wrong?
:::
:::

::: {.solution}
(a) \( 2 = 2/1 \) is rational and \( 2^2 = 4 \).

(b) The step "\( n^2 \) divisible by \( 4 \) implies \( n \) divisible by \( 4 \)" is false: for \( n = 2 \), \( n^2 = 4 \) is divisible by \( 4 \) but \( 2 \) is not. It fails exactly on the witness of (a): with \( r = 2/1 \), we have \( p = 2 \), and the "lemma" would claim \( 4 \) divides \( 2 \).

(c) The last step is \( \rulename{\neg I} \), applied to the box opened by "\( r^2 = 4 \)". The rule is applied correctly, but the box contains a line that is not justified: the false lemma was used as if it were a premise available everywhere, through \( \rulename{{\to}E} \). A derivation is only as good as its premises. In @thm-sqrt2-irrational the corresponding lemma is @thm-square-even-implies-even, which we proved; here nothing proves it, and nothing could.
:::
