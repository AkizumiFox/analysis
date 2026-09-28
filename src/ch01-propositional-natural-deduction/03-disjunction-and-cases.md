# Or, and Proof by Cases

The rules for "and" and "implies" (@def-rules-conjunction, @def-rules-implication) already let us build real derivations, such as the two directions of @prp-curry. One of the commonest moves in mathematics is still missing, though: the split into cases, "if \( x \ge 0 \), then …; if \( x < 0 \), then …". This section gives the two rules for "or". The elimination rule is exactly the case split, and we use it to prove two facts about absolute values and a handful of laws of "or" that later sections quote.

## A proof that needs two cases

The absolute value of a real number is defined in two cases:
\[
\abs{x} \coloneqq
\begin{cases}
x & \text{if } x \ge 0, \\
-x & \text{if } x < 0 .
\end{cases}
\]
Suppose we want to prove that \( \abs{xy} = \abs{x}\abs{y} \) for all real numbers \( x \) and \( y \). There is no single computation to do. Which formula gives \( \abs{xy} \) depends on the sign of \( xy \), and that depends on the signs of \( x \) and \( y \). Yet once the signs are fixed, each case is one line: if \( x \ge 0 \) and \( y < 0 \), for instance, then \( \abs{xy} = -xy = x \cdot (-y) = \abs{x}\abs{y} \).

So the proof we want has the shape "every real number is \( \ge 0 \) or \( < 0 \); in the first case …; in the second case …; so in every case …". The rules so far cannot say this. Neither \( \wedge \) nor \( \to \) lets us take a statement "\( P \) or \( Q \)", which does not tell us **which** of the two holds, and still reach a definite conclusion. That is the job of the elimination rule for "or".

## The rules for "or"

*To use "\( P \) or \( Q \)", reach your goal from \( P \), and reach it again from \( Q \).*

::: {#def-rules-disjunction}
[Rules for Disjunction]

- \( \rulename{\vee I} \) (**or-introduction**). If \( P \) stands on an available line, we may write \( P \vee Q \), and we may write \( Q \vee P \), for **any** statement \( Q \).
- \( \rulename{\vee E} \) (**or-elimination**, or **proof by cases**). Suppose \( P \vee Q \) stands on an available line, and there are two available boxes: one opened by the assumption \( P \), the other opened by the assumption \( Q \), each containing the **same** statement \( R \) as a line of its own, not inside a further box. Then we may write \( R \). The justification cites **three** things: the disjunction and both boxes, as in \( \rulename{\vee E}\ 1, \lines{3}{5}, \lines{6}{8} \).
:::

As a pattern, with letters \( i, j, \dots \) standing for line numbers:
```{=latex}
\begin{center}
$\begin{nd}[schema]
  \hypo {i} {P \vee Q}
  \open
  \hypo {j} {P}
  \have {} {\vdots}
  \have {k} {R}
  \close
  \open
  \hypo {l} {Q}
  \have {} {\vdots}
  \have {m} {R}
  \close
  \have {n} {R} \oe{i,j-k,l-m}
\end{nd}$
\end{center}
```

In words. \( \rulename{\vee I} \) weakens a statement. Knowing \( x = 0 \), we know "\( x < 0 \) or \( x = 0 \)", which is \( x \le 0 \). We have thrown information away, but sometimes the weaker form is exactly what a definition or a goal asks for.

\( \rulename{\vee E} \) is the case split, clause by clause:

- **The disjunction.** Some line must say \( P \vee Q \). The cases are not ours to invent: they are the two halves of a disjunction we already have.
- **Two boxes.** The disjunction does not say which of \( P \), \( Q \) holds, so we must be ready for both. Each case's assumption is temporary, so each case gets its own box, and neither box may use the other's assumption.
- **The same last line.** Both boxes must end in the same statement \( R \). The rule writes \( R \) outside both boxes, where neither \( P \) nor \( Q \) is in force. That is only honest if \( R \) was reached whichever case we are in.

Here are the first derivations.

::: {#exm-disjunction-first-derivations}
[First derivations with "or"]

Show that \( P \vee Q \vdash Q \vee P \), and that \( P \vee P \vdash P \).
:::

::: {.solution}
For the first, the goal \( Q \vee P \) is reached in each case by \( \rulename{\vee I} \), once from the right-hand disjunct and once from the left.
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee Q}
  \open
  \hypo {2} {P}
  \have {3} {Q \vee P} \oi{2}
  \close
  \open
  \hypo {4} {Q}
  \have {5} {Q \vee P} \oi{4}
  \close
  \have {6} {Q \vee P} \oe{1,2-3,4-5}
\end{nd}$
\end{center}
```
The two boxes are separate: the break in the vertical bar between lines 3 and 4 shows where the first closes and the second opens. Both end in \( Q \vee P \), and line 6 cites the disjunction on line 1 and the boxes \( \lines{2}{3} \) and \( \lines{4}{5} \).

For the second, both cases are already the goal, so each box consists of its assumption alone.
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee P}
  \open
  \hypo {2} {P}
  \close
  \open
  \hypo {3} {P}
  \close
  \have {4} {P} \oe{1,2-2,3-3}
\end{nd}$
\end{center}
```
This is the degenerate case split, in which the two cases are the same case. It is worth seeing once, because one-line boxes come back in Section 1.4: a box whose assumption is already the statement \( R \) is a legal box that ends in \( R \).
:::

Change one line of the first derivation and it stops being a derivation. Suppose the second box stops at its assumption \( Q \), and the last line still claims \( Q \vee P \):
```{=latex}
% expect-invalid
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee Q}
  \open
  \hypo {2} {P}
  \have {3} {Q \vee P} \oi{2}
  \close
  \open
  \hypo {4} {Q}
  \close
  \have {5} {Q \vee P} \oe{1,2-3,4-4}
\end{nd}$
\end{center}
```
Everything cited exists and is available: the disjunction, a box opened by \( P \), a box opened by \( Q \). What fails is the clause about the last lines. The box \( \lines{4}{4} \) ends in \( Q \), the box \( \lines{2}{3} \) ends in \( Q \vee P \), and \( \rulename{\vee E} \) needs one statement that ends both. The repair is the missing line 5 of the correct derivation.

Why is the rule built like this? Drop the second box, and from "\( x \ge 0 \) or \( x < 0 \)" and a derivation of \( \abs{x} = x \) from \( x \ge 0 \) we could conclude \( \abs{x} = x \) for every real \( x \), which fails at \( x = -1 \). Allow the two boxes to end in different statements \( R_1 \) and \( R_2 \), and ask what may be written after them: all we honestly know is "\( R_1 \) or \( R_2 \)", and that is already reachable with the rule as it stands, by \( \rulename{\vee I} \) at the end of each box (exercise B3 does this). So the rule asks for one common last line and loses nothing.

::: {.check}
A derivation contains a line \( P \vee Q \) and a box opened by \( P \) that ends in \( R \). No box is opened by \( Q \). Which clause of \( \rulename{\vee E} \) stops us writing \( R \)? What single change to the derivation would allow it?
:::

::: {.solution}
The rule needs **two** boxes, one opened by each disjunct, and the box opened by \( Q \) is missing. Adding a box opened by \( Q \) whose last line is \( R \) (a derivation of \( R \) from \( Q \) and the available lines) allows \( \rulename{\vee E} \), citing the disjunction and both boxes.
:::

## Cases about real numbers

The facts about \( \le \) and the absolute value used below are school algebra: every real number \( a \) satisfies \( a \ge 0 \) or \( a < 0 \); the rules of signs for products; adding two inequalities of the same direction. Chapter 10 proves all of them from the axioms of an ordered field. Here we take them as known.

In the language of this chapter, "every real number \( a \) satisfies \( a \ge 0 \) or \( a < 0 \)" is a supply of disjunctions. For each number we meet, it gives a line \( (a \ge 0) \vee (a < 0) \) that \( \rulename{\vee E} \) may cite.

::: {#exm-abs-product-cases}
[The absolute value of a product]

Let \( x \) and \( y \) be real numbers. Prove that \( \abs{xy} = \abs{x}\abs{y} \).
:::

::: {.solution}
We use that \( \abs{a} = -a \) whenever \( a \le 0 \): for \( a < 0 \) this is the definition, and for \( a = 0 \) both sides are \( 0 \).

The number \( x \) satisfies \( x \ge 0 \) or \( x < 0 \), and we argue by cases \( [\rulename{\vee E}] \). Inside each case, \( y \ge 0 \) or \( y < 0 \), and we argue by cases again.

*Case \( x \ge 0 \), \( y \ge 0 \).* Then \( xy \ge 0 \), so \( \abs{xy} = xy = \abs{x}\abs{y} \).

*Case \( x \ge 0 \), \( y < 0 \).* Then \( xy \le 0 \), so \( \abs{xy} = -xy = x \cdot (-y) = \abs{x}\abs{y} \).

*Case \( x < 0 \), \( y \ge 0 \).* Then \( xy \le 0 \), so \( \abs{xy} = -xy = (-x) \cdot y = \abs{x}\abs{y} \).

*Case \( x < 0 \), \( y < 0 \).* Then \( xy > 0 \), so \( \abs{xy} = xy = (-x)(-y) = \abs{x}\abs{y} \).

Each inner case split reaches \( \abs{xy} = \abs{x}\abs{y} \), so each outer case does, and hence the equation holds.
:::

The structure is two uses of \( \rulename{\vee E} \), one inside each box of the other: two outer boxes (the sign of \( x \)), each containing two inner boxes (the sign of \( y \)), and every one of the four inner boxes ending in the same equation. The second and third cases needed the remark about \( a \le 0 \). When \( x = 0 \) and \( y < 0 \), the product is \( 0 \), not negative, and without the remark the case would have a hole at exactly that point.

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

Two case splits appear here, one after the other rather than one inside the other. The first proves a small lemma for an arbitrary number \( a \); the second uses both halves of the lemma, for \( a = x \) and for \( a = y \). Splitting on the sign of \( x + y \) instead of the signs of \( x \) and \( y \) is what saves two cases: the absolute value in the goal is \( \abs{x + y} \), and its sign is the only one the goal's left side cares about.

::: {.warning}
A case split must cover every possibility. A common faulty proof of the triangle inequality treats "\( x \ge 0 \) and \( y \ge 0 \)" and "\( x < 0 \) and \( y < 0 \)", checks both, and stops. The disjunction of these two cases is not a fact: \( x = 1 \), \( y = -1 \) satisfies neither. So there is no line \( P \vee Q \) for \( \rulename{\vee E} \) to cite, and the rule was never legally applied. The missing mixed-sign cases are the interesting ones: at \( x = 1 \), \( y = -1 \) the inequality reads \( 0 \le 2 \), and it is strict.
:::

The warning is about the first thing \( \rulename{\vee E} \) cites. The disjunction must itself be on an available line, derived or known, before the boxes are opened. Writing "Case 1 … Case 2 …" does not create it.

::: {.warning}
Cases must **exhaust**, and a split that silently drops a value is a missing case in disguise. "Every real \( x \) satisfies \( x > 0 \) or \( x < 0 \)" is false: \( x = 0 \) satisfies neither. A proof that splits into \( x > 0 \) and \( x < 0 \) cites a disjunction that is not available, and proves nothing about \( x = 0 \). The true disjunctions are \( x \ge 0 \) or \( x < 0 \), and \( x > 0 \) or \( x = 0 \) or \( x < 0 \).
:::

Cases may overlap, however. "\( x \ge 0 \) or \( x \le 0 \)" is true for every real \( x \), and \( x = 0 \) lies in both cases. Nothing in \( \rulename{\vee E} \) forbids this: the rule asks that the goal be reached in each case, not that the cases be disjoint. (This is the inclusive "or" of Section 1.1.)

::: {.check}
Each of the following begins a proof that \( x^2 \ge 0 \) for every real number \( x \). Which case splits are exhaustive, so that \( \rulename{\vee E} \) may be applied?

::: {.enumerate options="label=(\roman*)"}
1. Case \( x \ge 0 \); case \( x < 0 \).
2. Case \( x > 0 \); case \( x < 0 \).
3. Case \( x \ge 0 \); case \( x \le 0 \).
:::
:::

::: {.solution}
(i) Exhaustive: every real number is \( \ge 0 \) or \( < 0 \). (ii) Not exhaustive: \( x = 0 \) is in neither case, so the disjunction cited is false. The claim is still true at \( 0 \), but this split never proves it there. (iii) Exhaustive. The cases overlap at \( x = 0 \), which does no harm: \( x^2 = 0 \ge 0 \) is reached in both.
:::

## Laws of "or"

Case splits are not only about numbers. The same two rules prove the laws that let us rearrange "and" and "or". The first says that "and" distributes over "or", in both directions.

::: {#prp-distributivity}
[Distributivity]

\( P \wedge (Q \vee R) \vdash (P \wedge Q) \vee (P \wedge R) \), and \( (P \wedge Q) \vee (P \wedge R) \vdash P \wedge (Q \vee R) \).
:::

::: {.idea}
In the first sequent the only disjunction in sight is \( Q \vee R \), inside the premise. So take the premise apart by \( \rulename{\wedge E} \), then split on \( Q \vee R \). In each case one side of the goal can be built by \( \rulename{\wedge I} \) and weakened to the whole goal by \( \rulename{\vee I} \). In the second sequent the premise itself is the disjunction, so split on it at once. Each case is a conjunction containing \( P \), and \( \rulename{\vee I} \) turns its other half into \( Q \vee R \).
:::

::: {.proof}
For the first sequent, the following is a derivation with premise \( P \wedge (Q \vee R) \) and last line \( (P \wedge Q) \vee (P \wedge R) \).
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge (Q \vee R)}
  \have {2} {P} \ae{1}
  \have {3} {Q \vee R} \ae{1}
  \open
  \hypo {4} {Q}
  \have {5} {P \wedge Q} \ai{2,4}
  \have {6} {(P \wedge Q) \vee (P \wedge R)} \oi{5}
  \close
  \open
  \hypo {7} {R}
  \have {8} {P \wedge R} \ai{2,7}
  \have {9} {(P \wedge Q) \vee (P \wedge R)} \oi{8}
  \close
  \have {10} {(P \wedge Q) \vee (P \wedge R)} \oe{3,4-6,7-9}
\end{nd}$
\end{center}
```
Lines 5 and 8 may cite line 2, which lies in no box and so is available everywhere below it.

For the second sequent, the following is a derivation with premise \( (P \wedge Q) \vee (P \wedge R) \) and last line \( P \wedge (Q \vee R) \).
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge Q) \vee (P \wedge R)}
  \open
  \hypo {2} {P \wedge Q}
  \have {3} {P} \ae{2}
  \have {4} {Q} \ae{2}
  \have {5} {Q \vee R} \oi{4}
  \have {6} {P \wedge (Q \vee R)} \ai{3,5}
  \close
  \open
  \hypo {7} {P \wedge R}
  \have {8} {P} \ae{7}
  \have {9} {R} \ae{7}
  \have {10} {Q \vee R} \oi{9}
  \have {11} {P \wedge (Q \vee R)} \ai{8,10}
  \close
  \have {12} {P \wedge (Q \vee R)} \oe{1,2-6,7-11}
\end{nd}$
\end{center}
```
This proves both sequents.
:::

In the second derivation, line 8 derives \( P \) a second time instead of citing line 3. It has to: line 3 lies in the box \( \lines{2}{6} \), which has closed, so line 3 is not available at line 8. Each case must earn its own \( P \).

For a real number \( x \), take \( P \): "\( x \ne 0 \)", \( Q \): "\( x > 0 \)" and \( R \): "\( x < 0 \)". The first sequent then reads: a non-zero number that is positive or negative is a positive non-zero number or a negative non-zero number. The law is dull in words, which is as it should be. Its use is in derivations, where it moves a case split from inside a conjunction to the outside.

The next derivation shows a case split **inside** a case: \( \rulename{\vee E} \) applied within one box of another \( \rulename{\vee E} \).

::: {#exm-disjunction-regroup}
[Regrouping a disjunction]

Show that \( P \vee (Q \vee R) \vdash (P \vee Q) \vee R \).
:::

::: {.solution}
Split on the premise. The case \( P \) is two weakenings. The case \( Q \vee R \) is itself a disjunction, so we split on it inside that box.
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee (Q \vee R)}
  \open
  \hypo {2} {P}
  \have {3} {P \vee Q} \oi{2}
  \have {4} {(P \vee Q) \vee R} \oi{3}
  \close
  \open
  \hypo {5} {Q \vee R}
  \open
  \hypo {6} {Q}
  \have {7} {P \vee Q} \oi{6}
  \have {8} {(P \vee Q) \vee R} \oi{7}
  \close
  \open
  \hypo {9} {R}
  \have {10} {(P \vee Q) \vee R} \oi{9}
  \close
  \have {11} {(P \vee Q) \vee R} \oe{5,6-8,9-10}
  \close
  \have {12} {(P \vee Q) \vee R} \oe{1,2-4,5-11}
\end{nd}$
\end{center}
```
Line 11 is the inner case split. It cites the disjunction on line 5 and the boxes \( \lines{6}{8} \) and \( \lines{9}{10} \), all of which sit inside the box \( \lines{5}{11} \), as line 11 does. Line 12 is the outer case split. Its second box is \( \lines{5}{11} \), whose last line, line 11, is a line of that box itself and not of a further box inside it, as @def-rules-disjunction requires.
:::

Finally, a case split can sit on the hypothesis of an implication. To prove "if \( P \) or \( Q \), then \( R \)", a mathematician proves "if \( P \), then \( R \)" and "if \( Q \), then \( R \)". For example, to show that an integer that is one more or three more than a multiple of \( 4 \) is odd, one treats \( n = 4k + 1 \) and \( n = 4k + 3 \) separately. The two derivations below show that the two forms say the same thing.

::: {#exm-cases-on-hypothesis}
[Cases on a hypothesis are two implications]

Show that \( (P \to R) \wedge (Q \to R) \vdash (P \vee Q) \to R \), and that \( (P \vee Q) \to R \vdash (P \to R) \wedge (Q \to R) \).
:::

::: {.solution}
For the first sequent, the goal is an implication, so we open a box with \( P \vee Q \) (@def-rules-implication), and inside it we split on that assumption.
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \to R) \wedge (Q \to R)}
  \open
  \hypo {2} {P \vee Q}
  \open
  \hypo {3} {P}
  \have {4} {P \to R} \ae{1}
  \have {5} {R} \ie{4,3}
  \close
  \open
  \hypo {6} {Q}
  \have {7} {Q \to R} \ae{1}
  \have {8} {R} \ie{7,6}
  \close
  \have {9} {R} \oe{2,3-5,6-8}
  \close
  \have {10} {(P \vee Q) \to R} \ii{2-9}
\end{nd}$
\end{center}
```
For the second, the goal is a conjunction of two implications, so we build each implication in its own box. Inside, \( \rulename{\vee I} \) turns the assumption into the premise's hypothesis.
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \vee Q) \to R}
  \open
  \hypo {2} {P}
  \have {3} {P \vee Q} \oi{2}
  \have {4} {R} \ie{1,3}
  \close
  \have {5} {P \to R} \ii{2-4}
  \open
  \hypo {6} {Q}
  \have {7} {P \vee Q} \oi{6}
  \have {8} {R} \ie{1,7}
  \close
  \have {9} {Q \to R} \ii{6-8}
  \have {10} {(P \to R) \wedge (Q \to R)} \ai{5,9}
\end{nd}$
\end{center}
```
:::

The second derivation is the one place in this section where \( \rulename{\vee I} \) manufactures the hypothesis of a premise: it builds the hypothesis \( P \vee Q \) that the premise needs before \( \rulename{{\to}E} \) can fire. Weakening is how a strong fact is fed to a rule that asks for a weaker one.

## What the rules sound like

Here are the rows of the rule, phrase and Lean table for this section's rules. As before, the last column is for readers who use a proof assistant, and nothing depends on it. Chapter 4 gives the full dictionary.

| Rule | You write | Lean |
|------|--------------------------------------|------------------------|
| \( \rulename{\vee I} \) | "In particular, \( P \) or \( Q \)." | `left` / `right` |
| \( \rulename{\vee E} \) | "Case 1: \( P \). … so \( R \). Case 2: \( Q \). … so \( R \). In either case, \( R \)." | `Or.elim h` |

The phrase for \( \rulename{\vee E} \) has three parts, and a written proof often drops the first: "we argue by cases" without saying which disjunction supplies them. When the disjunction is a standard fact ("\( x \ge 0 \) or \( x < 0 \)"), that is harmless. When it is not, the reader should ask for it, because it is the line the rule cites first.

## Exercises

### A. Check your understanding

::: {#exr-disjunction-and-cases-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the rule \( \rulename{\vee E} \), and name the three things its justification cites.
2. Match each sentence, taken from proofs, with the rule it uses, \( \rulename{\vee I} \) or \( \rulename{\vee E} \).
    - "We have \( x < 3 \), so in particular \( x \le 3 \)."
    - "If \( n \) is even, then \( n^2 + n = n(n + 1) \) is even; if \( n \) is odd, then \( n + 1 \) is even and so is \( n(n + 1) \). Either way, \( n^2 + n \) is even."
    - "We found that \( a = 0 \). So \( a = 0 \) or \( b = 0 \), and therefore \( ab = 0 \)."
    - "Both possibilities for the sign of \( t \) give \( t^2 \ge 0 \)."
3. True or false, with a reason: to prove \( R \) from \( P \vee Q \) by cases, it is enough to derive \( R \) from \( P \).
4. The following is offered as a derivation of \( P \vee Q, \; P \to R \vdash R \). Name the line that is not justified and the clause of @def-rules-disjunction it violates.
   ```{=latex}
   % expect-invalid
   \begin{center}
   $\begin{nd}
     \hypo {1} {P \vee Q}
     \hypo {2} {P \to R}
     \open
     \hypo {3} {P}
     \have {4} {R} \ie{2,3}
     \close
     \have {5} {R} \oe{1,3-4}
   \end{nd}$
   \end{center}
   ```
:::
:::

::: {.solution}
(a) If \( P \vee Q \) stands on an available line, and there are two available boxes, one opened by \( P \) and one opened by \( Q \), each containing the same statement \( R \) as a line of its own, then we may write \( R \) (@def-rules-disjunction). The justification cites the disjunction and the two boxes.

(b) In order: \( \rulename{\vee I} \), since \( x \le 3 \) is \( (x < 3) \vee (x = 3) \) and we know the left disjunct; \( \rulename{\vee E} \), on "\( n \) is even or \( n \) is odd", with both cases ending in "\( n^2 + n \) is even"; \( \rulename{\vee I} \), which weakens \( a = 0 \) to "\( a = 0 \) or \( b = 0 \)", the form in which the fact about products asks for it; \( \rulename{\vee E} \), on "\( t \ge 0 \) or \( t < 0 \)", with both cases ending in \( t^2 \ge 0 \).

(c) False. \( P \vee Q \) does not say which of \( P \), \( Q \) holds, so \( R \) must also be derived from \( Q \). For example, with \( x \) real, from "\( x \ge 0 \) or \( x < 0 \)" and a derivation of \( \abs{x} = x \) from \( x \ge 0 \), we may not conclude \( \abs{x} = x \): it fails at \( x = -1 \).

(d) Line 5. \( \rulename{\vee E} \) needs two boxes, one opened by each disjunct; line 5 cites only the box opened by \( P \), and no box opened by \( Q \) exists. Nothing available reaches \( R \) from \( Q \) either, so the gap cannot be filled from these premises. An instance shows the claim itself fails (informally: a derivation never leads from true premises to a false conclusion, which Chapter 2 proves): for a real number \( x \), take \( P \): "\( x > 1 \)", \( Q \): "\( x < 1 \)", \( R \): "\( x > 0 \)". At \( x = -1 \) both premises hold and \( R \) does not.
:::

### B. Practice

::: {#exr-disjunction-and-cases-b1}
[B1: The other distributive law]

Show that \( (P \vee Q) \wedge (P \vee R) \vdash P \vee (Q \wedge R) \).

*Hint: after taking the premise apart, you will need a case split inside a case.*
:::

::: {.solution}
The premise gives two disjunctions. Split on \( P \vee Q \). In the case \( P \), the goal is one weakening away. In the case \( Q \), we still lack \( R \), so we split on \( P \vee R \) inside that box: its case \( P \) weakens as before, and its case \( R \) combines with \( Q \).
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \vee Q) \wedge (P \vee R)}
  \have {2} {P \vee Q} \ae{1}
  \have {3} {P \vee R} \ae{1}
  \open
  \hypo {4} {P}
  \have {5} {P \vee (Q \wedge R)} \oi{4}
  \close
  \open
  \hypo {6} {Q}
  \open
  \hypo {7} {P}
  \have {8} {P \vee (Q \wedge R)} \oi{7}
  \close
  \open
  \hypo {9} {R}
  \have {10} {Q \wedge R} \ai{6,9}
  \have {11} {P \vee (Q \wedge R)} \oi{10}
  \close
  \have {12} {P \vee (Q \wedge R)} \oe{3,7-8,9-11}
  \close
  \have {13} {P \vee (Q \wedge R)} \oe{2,4-5,6-12}
\end{nd}$
\end{center}
```
Line 10 cites line 6, the assumption of the enclosing box, which is still open at line 10. Line 12 cites line 3, which lies in no box. Splitting on \( P \vee R \) first, with the roles of \( Q \) and \( R \) exchanged, works equally well.
:::

::: {#exr-disjunction-and-cases-b2}
[B2: The larger of two numbers]

For real numbers \( a \) and \( b \), let \( \max(a, b) \coloneqq a \) if \( a \ge b \), and \( \max(a, b) \coloneqq b \) if \( a < b \). Prove that \( \max(a, b) \ge a \) and \( \max(a, b) \ge b \). Hence deduce that \( \max(a, b) \ge \frac{1}{2}(a + b) \): the larger of two numbers is at least their average.
:::

::: {.solution}
We have \( a \ge b \) or \( a < b \), and we argue by cases \( [\rulename{\vee E}] \).

*Case \( a \ge b \).* Then \( \max(a, b) = a \). So \( \max(a, b) \ge a \), since \( a = a \) and \( \ge \) allows equality \( [\rulename{\vee I}] \); and \( \max(a, b) = a \ge b \).

*Case \( a < b \).* Then \( \max(a, b) = b \). So \( \max(a, b) = b > a \), which gives \( \max(a, b) \ge a \) \( [\rulename{\vee I}] \); and \( \max(a, b) = b \ge b \).

In both cases \( \max(a, b) \ge a \) and \( \max(a, b) \ge b \) \( [\rulename{\wedge I}] \), so both hold.

Adding the two inequalities gives \( 2\max(a, b) \ge a + b \), and dividing by \( 2 > 0 \) gives \( \max(a, b) \ge \frac{1}{2}(a + b) \). For instance, \( \max(3, -5) = 3 \ge -1 = \frac{1}{2}(3 + (-5)) \).
:::

::: {#exr-disjunction-and-cases-b3}
[B3: Two cases, two conclusions]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( P \vee Q, \; P \to R, \; Q \to S \vdash R \vee S \).
2. Use (a) to prove: for every integer \( n \), \( n^2 \) is a multiple of \( 4 \) or \( n^2 \) is one more than a multiple of \( 4 \). You may use that every integer is even or odd.
:::
:::

::: {.solution}
(a) Split on \( P \vee Q \). In each case the matching implication gives one of \( R \), \( S \), and \( \rulename{\vee I} \) weakens it to the common last line \( R \vee S \).
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee Q}
  \hypo {2} {P \to R}
  \hypo {3} {Q \to S}
  \open
  \hypo {4} {P}
  \have {5} {R} \ie{2,4}
  \have {6} {R \vee S} \oi{5}
  \close
  \open
  \hypo {7} {Q}
  \have {8} {S} \ie{3,7}
  \have {9} {R \vee S} \oi{8}
  \close
  \have {10} {R \vee S} \oe{1,4-6,7-9}
\end{nd}$
\end{center}
```

(b) Take \( P \): "\( n \) is even", \( Q \): "\( n \) is odd", \( R \): "\( n^2 \) is a multiple of \( 4 \)", \( S \): "\( n^2 \) is one more than a multiple of \( 4 \)". The premise \( P \vee Q \) is the fact we may use. For \( P \to R \): if \( n = 2k \) for an integer \( k \), then \( n^2 = 4k^2 \). For \( Q \to S \): if \( n = 2k + 1 \), then \( n^2 = 4k^2 + 4k + 1 = 4(k^2 + k) + 1 \). By (a), \( R \vee S \). For instance, \( 6^2 = 36 = 4 \cdot 9 \) and \( 7^2 = 49 = 4 \cdot 12 + 1 \).
:::

### C. Going deeper

::: {#exr-disjunction-and-cases-c1}
[C1: The reverse triangle inequality]

Let \( x \) and \( y \) be real numbers. Prove that
\[
\bigl\lvert \abs{x} - \abs{y} \bigr\rvert \le \abs{x - y}
\]
by splitting into the two cases \( \abs{x} \ge \abs{y} \) and \( \abs{x} < \abs{y} \), using in each case the triangle inequality of @exm-triangle-inequality-cases. Then explain why these two cases exhaust all possibilities, and why a split on the signs of \( x \) and \( y \) would need four cases.
:::

::: {.solution}
[Hint 1]

The triangle inequality bounds \( \abs{u + v} \). Write \( x \) as a sum of two numbers whose absolute values appear in the goal.
:::

::: {.solution}
[Hint 2]

In the case \( \abs{x} \ge \abs{y} \), the left side is \( \abs{x} - \abs{y} \). Start from \( x = (x - y) + y \).
:::

::: {.solution}
We use two school facts: for real numbers \( a \), \( b \), either \( a \ge b \) or \( a < b \); and \( \abs{-a} = \abs{a} \) for every real \( a \) (if \( a \ge 0 \) then \( -a \le 0 \), so \( \abs{-a} = a \); if \( a < 0 \) then \( -a > 0 \), so \( \abs{-a} = -a = \abs{a} \)).

By the first fact, \( \abs{x} \ge \abs{y} \) or \( \abs{x} < \abs{y} \), and we argue by cases \( [\rulename{\vee E}] \).

*Case \( \abs{x} \ge \abs{y} \).* Then \( \abs{x} - \abs{y} \ge 0 \), so \( \bigl\lvert \abs{x} - \abs{y} \bigr\rvert = \abs{x} - \abs{y} \). By @exm-triangle-inequality-cases applied to the numbers \( x - y \) and \( y \),
\[
\abs{x} = \abs{(x - y) + y} \le \abs{x - y} + \abs{y} ,
\]
so \( \abs{x} - \abs{y} \le \abs{x - y} \), which is the goal in this case.

*Case \( \abs{x} < \abs{y} \).* Then \( \abs{x} - \abs{y} < 0 \), so \( \bigl\lvert \abs{x} - \abs{y} \bigr\rvert = \abs{y} - \abs{x} \). By @exm-triangle-inequality-cases applied to \( y - x \) and \( x \),
\[
\abs{y} = \abs{(y - x) + x} \le \abs{y - x} + \abs{x} ,
\]
so \( \abs{y} - \abs{x} \le \abs{y - x} = \abs{-(x - y)} = \abs{x - y} \).

Both cases reach the goal, which proves the inequality.

The two cases exhaust all possibilities because they are the two halves of the disjunction "\( a \ge b \) or \( a < b \)" with \( a = \abs{x} \), \( b = \abs{y} \), and that disjunction holds for all real numbers. The split was chosen by the goal: the outer absolute value is of \( \abs{x} - \abs{y} \), and its formula depends only on the sign of that difference.

A split on signs would decide \( \abs{x} \) and \( \abs{y} \) separately: \( x \ge 0 \) or \( x < 0 \) gives the formula for \( \abs{x} \), and inside each case \( y \ge 0 \) or \( y < 0 \) gives the formula for \( \abs{y} \). That is a case split inside each box of another, with \( 2 \cdot 2 = 4 \) inner boxes, as in @exm-abs-product-cases. Fewer would not do for that method: with only the sign of \( x \) fixed, \( \abs{y} \) still has no formula.

**Marking scheme.** (10 points)
- 2: states the disjunction \( \abs{x} \ge \abs{y} \) or \( \abs{x} < \abs{y} \) and says it holds for all reals.
- 3: in the first case, removes the outer absolute value correctly and derives \( \abs{x} - \abs{y} \le \abs{x - y} \) from the triangle inequality for \( (x - y) + y \).
- 3: in the second case, the same with the roles exchanged, including \( \abs{y - x} = \abs{x - y} \).
- 2: explains the four sign cases as a split inside each case of another.
Fatal errors (0 for the step): using \( \bigl\lvert \abs{x} - \abs{y} \bigr\rvert = \abs{x} - \abs{y} \) in both cases; applying the triangle inequality to a difference as if \( \abs{u - v} \le \abs{u} - \abs{v} \).
A proof that squares both sides instead, or splits on signs, earns the 6 points of the two middle lines if every case is complete.
:::

::: {#exr-disjunction-and-cases-c2}
[C2: Find the error]

Here is a proof, by four cases, that \( \abs{x - y} \le \abs{x} + \abs{y} \) for all real numbers \( x \) and \( y \).

> *Case 1: \( x \ge 0 \).* Then \( \abs{x} = x \).
>
> *Case 1a: \( y \ge 0 \).* Then \( \abs{y} = y \), and \( \abs{x - y} \) is \( x - y \) or \( y - x \). Since \( x - y \le x \le x + y \) and \( y - x \le y \le x + y \), we get \( \abs{x - y} \le x + y = \abs{x} + \abs{y} \).
>
> *Case 1b: \( y < 0 \).* Then \( \abs{y} = -y \), and \( x - y > 0 \), so \( \abs{x - y} = x - y = \abs{x} + \abs{y} \).
>
> *Case 2: \( x < 0 \).* Then \( \abs{x} = -x \).
>
> *Case 2a: \( y \ge 0 \).* Then \( \abs{y} = y \), and \( x - y < 0 \), so \( \abs{x - y} = y - x = \abs{y} + \abs{x} \).
>
> *Case 2b: \( y < 0 \).* Then \( \abs{y} = -y \). Since \( x \ge 0 \) and \( y < 0 \), we have \( x - y > 0 \), so \( \abs{x - y} = x - y \le \abs{x} + \abs{y} \), because \( x \le \abs{x} \) and \( -y = \abs{y} \).
>
> All four cases give \( \abs{x - y} \le \abs{x} + \abs{y} \).

::: {.enumerate options="label=(\alph*)"}
1. Is the statement true?
2. Find the line that is not justified, and name the rule whose conditions it breaks.
3. Show with specific numbers that the step fails.
4. Repair Case 2b.
:::
:::

::: {.solution}
(a) Yes. For instance, it follows from @exm-triangle-inequality-cases applied to \( x \) and \( -y \), since \( \abs{-y} = \abs{y} \). So the question is not whether the conclusion holds but whether this argument proves it.

(b) The sentence "Since \( x \ge 0 \) and \( y < 0 \), we have \( x - y > 0 \)" in Case 2b. The assumption \( x \ge 0 \) is the assumption of Case 1. In derivation terms, it opens the first box of the outer \( \rulename{\vee E} \), and Case 2b lies inside the **second** box, which is opened by \( x < 0 \). Once the first box has closed, its lines are not available (@def-derivation), so Case 2b may not cite \( x \ge 0 \): the rule broken is the scope rule, inside the second box of \( \rulename{\vee E} \). The sentence is the reasoning of Case 1b copied into Case 2b, where its assumption is no longer in force. So the box of Case 2 does not reach the goal from the lines available to it, and the final \( \rulename{\vee E} \) has no right to cite it.

(c) Take \( x = -3 \) and \( y = -1 \), which is Case 2b. Then \( x - y = -2 \), which is not \( > 0 \), and \( \abs{x - y} = 2 \ne -2 = x - y \). The conclusion of Case 2b still holds here (\( 2 \le 3 + 1 \)), but the step used to reach it is false.

(d) In Case 2b, \( x < 0 \) and \( y < 0 \), so \( \abs{x} = -x \) and \( \abs{y} = -y \). The number \( \abs{x - y} \) is \( x - y \) or \( y - x \). Since \( x < 0 \), we have \( x - y < -y = \abs{y} \le \abs{x} + \abs{y} \). Since \( y < 0 \), we have \( y - x < -x = \abs{x} \le \abs{x} + \abs{y} \). So in either case \( \abs{x - y} \le \abs{x} + \abs{y} \), using only the assumptions of Case 2b.
:::

<!-- dependency ledger
exm-abs-product-cases (example): every real a satisfies a >= 0 or a < 0; sign rules for products; |a| = -a for a <= 0 | school algebra, taken as known (ch01 blueprint, Allowed prerequisites); stated in prose before the example; Ch 10 re-proves (prose pointer)
exm-triangle-inequality-cases (example): adding two inequalities of the same direction; -a <= 0 <= a for a >= 0 | school algebra, taken as known; stated in prose before exm-abs-product-cases
exr-disjunction-and-cases-a1 (solution): x <= 3 means (x < 3 or x = 3); a = 0 or b = 0 gives ab = 0; every integer is even or odd; t^2 >= 0 | school facts
exr-disjunction-and-cases-a1 (solution): (d) a derivation never leads from true premises to a false conclusion | forward pointer to ch02 (thm-soundness), flagged in the text as proved there; the answer (line 5) does not use it
exr-disjunction-and-cases-b2 (solution): a >= b or a < b; dividing an inequality by 2 > 0 | school algebra, taken as known
exr-disjunction-and-cases-b3 (solution): every integer is even or odd (stated in the item); n = 2k or n = 2k + 1 with k an integer (naming k is a quantifier step, Ch 3) | stated in the item; school fact
exr-disjunction-and-cases-c1 (solution): a >= b or a < b; |-a| = |a| | school algebra; |-a| = |a| proved inline by cases
exr-disjunction-and-cases-c2 (solution): order facts for x, y < 0 | school algebra, taken as known
-->
