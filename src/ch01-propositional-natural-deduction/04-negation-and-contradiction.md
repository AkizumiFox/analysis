# Not, Contradiction, and the Contrapositive

With the rules for "and", "implies" and "or" (@def-rules-conjunction, @def-rules-implication, @def-rules-disjunction) we can prove that things are so, but not yet that something is **not** so: that no rational number has square \( 2 \) or that \( x^2 + 1 \) is never \( 0 \). This section gives the rules for "not" and for \( \bot \). With them we prove the contrapositive, meet the first **derived rule**, prove that \( \sqrt{2} \) is irrational, and see where the strangest feature of implication comes from.

## How to prove that something is not so

To show that no rational number has square \( 2 \), we cannot inspect the rational numbers one by one. A mathematician instead supposes the opposite and shows that it leads to something impossible: "suppose \( r \) is rational and \( r^2 = 2 \); …; this is a contradiction; hence no rational number has square \( 2 \)."

That shape, assume and reach the impossible, is the box of @def-rules-implication with a special last line. The impossible thing gets a name, the statement \( \bot \) of Section 1.1, read "contradiction". Three rules say how \( \neg \) and \( \bot \) are proved and used.

*To prove "not \( P \)", assume \( P \) and reach a contradiction.*

::: {#def-rules-negation}
[Rules for Negation and Contradiction]

- \( \rulename{\neg I} \) (**not-introduction**). Open a box with the assumption \( P \). If \( \bot \) is reached as a line of that box, not inside a further box, we may close the box and write \( \neg P \). The justification cites the box, as in \( \rulename{\neg I}\ \lines{3}{5} \).
- \( \rulename{\neg E} \) (**not-elimination**). If \( P \) and \( \neg P \) stand on available lines, we may write \( \bot \). The justification cites both lines.
- \( \rulename{\bot E} \) (**contradiction-elimination**, or **ex falso**). If \( \bot \) stands on an available line, we may write **any** statement. The justification cites that line.
:::

In words. \( \rulename{\neg I} \) says how to **prove** a negation: assume the statement being negated, reach the impossible, and discharge. The box opens with \( P \), not with \( \neg P \). \( \rulename{\neg E} \) says how to **use** a negation: \( \neg P \) is exactly what clashes with \( P \), and the clash is \( \bot \). \( \rulename{\bot E} \) says what \( \bot \) is good for. A line \( \bot \) can only be reached in a situation that cannot occur, and there anything may be written.

In derivations about numbers, the clash usually comes from a school fact. For real numbers, \( a \ge b \) is the negation of \( a < b \), since exactly one of the two holds; so \( x^2 < 0 \) and the fact \( x^2 \ge 0 \) give \( \bot \) by \( \rulename{\neg E} \). And \( a \ne b \) is \( \neg(a = b) \) by definition of the symbol.

::: {#exm-square-plus-one}
[A negative statement proved by not-introduction]

Let \( x \) be a real number. Prove that \( x^2 + 1 \ne 0 \), naming the rules.
:::

::: {.solution}
The goal \( x^2 + 1 \ne 0 \) is \( \neg(x^2 + 1 = 0) \), so we use \( \rulename{\neg I} \). Suppose \( x^2 + 1 = 0 \). Then \( x^2 = -1 \), so \( x^2 < 0 \). But \( x^2 \ge 0 \), that is, \( \neg(x^2 < 0) \), so we have a contradiction \( [\rulename{\neg E}] \). Hence \( x^2 + 1 \ne 0 \) \( [\rulename{\neg I}] \).
:::

The rules for \( \neg \) have the same shapes as rules we already know, with \( \bot \) in one slot. Put the rules for \( \neg P \) beside the rules for \( \to \) applied to the statement \( P \to \bot \):

| To … | a negation \( \neg P \) | an implication \( P \to \bot \) |
|---|---|---|
| prove it | box from \( P \) to \( \bot \), then \( \rulename{\neg I} \) | box from \( P \) to \( \bot \), then \( \rulename{{\to}I} \) |
| use it, given \( P \) | \( \bot \) by \( \rulename{\neg E} \) | \( \bot \) by \( \rulename{{\to}E} \) |

::: {.remark}
Row by row, \( \neg P \) behaves exactly like \( P \to \bot \): "not \( P \)" means "\( P \) leads to contradiction". Some presentations of logic take this as the definition of \( \neg \). This book keeps \( \neg \) as a connective with its own rules, and Chapter 4 returns to the reading \( \neg P \approx P \to \bot \) when it asks what a proof of a negation provides.
:::

::: {.warning}
\( \rulename{\neg I} \) proves **negative** statements only. Its box opens with \( P \) and ends by writing \( \neg P \). A proof that says "suppose \( x \) is **not** positive; …; contradiction; hence \( x \) is positive" has a box opened by \( \neg(x > 0) \), and \( \rulename{\neg I} \) applied to that box gives \( \neg\neg(x > 0) \), not \( x > 0 \). Getting from there to \( x > 0 \) needs a rule we have not met. It is the subject of Section 1.6, which contrasts the two kinds of box in full.
:::

## First derivations with negation

The first two derivations are short, and they show the two ways a \( \neg \) enters a derivation: as a goal, proved by \( \rulename{\neg I} \), and as a premise, used by \( \rulename{\neg E} \).

::: {#exm-double-negation-introduction}
[Two negations from one premise]

Show that \( P \vdash \neg\neg P \), and that \( (P \vee Q) \to \neg P \vdash \neg P \).
:::

::: {.solution}
For the first, the goal \( \neg\neg P \) is the negation of \( \neg P \). So by \( \rulename{\neg I} \) we assume \( \neg P \) and aim at \( \bot \), which the premise supplies at once.
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \open
  \hypo {2} {\neg P}
  \have {3} {\bot} \ne{1,2}
  \close
  \have {4} {\neg\neg P} \ni{2-3}
\end{nd}$
\end{center}
```
For the second, the goal is \( \neg P \), so we assume \( P \). To use the premise we need its hypothesis \( P \vee Q \), and \( \rulename{\vee I} \) makes it from \( P \). The premise then gives \( \neg P \), which clashes with the assumption.
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \vee Q) \to \neg P}
  \open
  \hypo {2} {P}
  \have {3} {P \vee Q} \oi{2}
  \have {4} {\neg P} \ie{1,3}
  \have {5} {\bot} \ne{2,4}
  \close
  \have {6} {\neg P} \ni{2-5}
\end{nd}$
\end{center}
```
In the second derivation, line 4 already says \( \neg P \), but it lies inside the box of \( P \) and depends on that assumption, so it cannot be the conclusion. Line 6 is the same statement outside the box, where it depends on the premise alone.
:::

The first derivation adds two negations. The reverse passage, from \( \neg\neg P \) to \( P \), would have to **remove** two, and no rule so far removes a negation: \( \rulename{\neg E} \) only turns a clash into \( \bot \). Section 1.6 returns to this.

::: {.check}
Is \( \neg(P \vee Q) \vdash \neg P \)? If so, give the derivation and name its rules.
:::

::: {.solution}
Yes. The goal \( \neg P \) is a negation, so assume \( P \) and aim at \( \bot \); \( \rulename{\vee I} \) turns \( P \) into \( P \vee Q \), which clashes with the premise.
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg(P \vee Q)}
  \open
  \hypo {2} {P}
  \have {3} {P \vee Q} \oi{2}
  \have {4} {\bot} \ne{3,1}
  \close
  \have {5} {\neg P} \ni{2-4}
\end{nd}$
\end{center}
```
The rules are \( \rulename{\vee I} \), \( \rulename{\neg E} \) and \( \rulename{\neg I} \). In words: if neither \( P \) nor \( Q \) holds, then in particular \( P \) does not.
:::

## The contrapositive, and the first derived rule

With negation available we can prove the most useful single fact about implication. An implication \( P \to Q \) promises \( Q \) whenever \( P \). So if \( Q \) fails, \( P \) must have failed too, or the promise would have been broken.

::: {#prp-contrapositive}
[Contrapositive]

\( P \to Q \vdash \neg Q \to \neg P \).
:::

::: {.idea}
Read the skeleton off the goal. It is an implication, so open a box with \( \neg Q \). The new goal \( \neg P \) is a negation, so inside it open a box with \( P \) and aim at \( \bot \). With \( P \) available, the premise gives \( Q \), which clashes with \( \neg Q \).
:::

::: {.proof}
The following is a derivation with premise \( P \to Q \) and last line \( \neg Q \to \neg P \).
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \open
  \hypo {2} {\neg Q}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \have {5} {\bot} \ne{4,2}
  \close
  \have {6} {\neg P} \ni{3-5}
  \close
  \have {7} {\neg Q \to \neg P} \ii{2-6}
\end{nd}$
\end{center}
```
Line 5 may cite line 2, since the only box containing line 2, the box \( \lines{2}{6} \), also contains line 5. This proves the proposition.
:::

The statement \( \neg Q \to \neg P \) is the **contrapositive** of \( P \to Q \). The derivation uses \( \rulename{{\to}I} \), \( \rulename{{\to}E} \), \( \rulename{\neg I} \) and \( \rulename{\neg E} \), and nothing else. The reverse passage, from \( \neg Q \to \neg P \) back to \( P \to Q \), must produce the positive statement \( Q \) from negative information, and Section 1.6 shows what that needs. The contrapositive is how one proves an implication whose hypothesis is hard to use directly, as in Argument A of Section 1.1.

A second fact about implication and negation is used so often that it has a name.

::: {#prp-modus-tollens}
[Modus Tollens]

\( P \to Q, \; \neg Q \vdash \neg P \).
:::

::: {.proof}
The following is a derivation with premises \( P \to Q \) and \( \neg Q \), and last line \( \neg P \).
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {\neg Q}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \have {5} {\bot} \ne{4,2}
  \close
  \have {6} {\neg P} \ni{3-5}
\end{nd}$
\end{center}
```
This proves the proposition.
:::

The name is Latin for "the mode that takes away": denying the consequence takes away the hypothesis. Its partner, from \( P \to Q \) and \( P \) to \( Q \), is \( \rulename{{\to}E} \), traditionally *modus ponens*, "the mode that puts".

Lines 3–6 of the derivation of @prp-modus-tollens are, line for line, lines 3–6 of the derivation of @prp-contrapositive. Rewriting the same lines every time would hide the argument behind bookkeeping. So once a sequent has been derived, we allow ourselves to use it as a single step.

::: {#def-derived-rule}
[Derived Rule]

Suppose a sequent \( P_1, \dots, P_n \vdash Q \) has been derived. In a later derivation, replace each letter in \( P_1, \dots, P_n, Q \) by a statement, the **same** statement for every occurrence of the same letter. If the resulting instances of \( P_1, \dots, P_n \) stand on available lines, we may write the resulting instance of \( Q \) on one line. The justification names the result and cites those lines, as in "\( \rulename{MT}\ 1, 2 \)". A sequent used in this way is a **derived rule**.
:::

In words: a proved sequent is a new rule. Its premises become the lines the rule cites, its conclusion the line it writes, and its letters may be replaced by any statements, since they stood for arbitrary statements (@def-derivable).

A derived rule adds **convenience, not power**. Its line abbreviates a piece of derivation we could write out in full: repeat each cited line by (D3) of @def-derivation, then copy the derivation of the sequent below the repetitions, with its letters replaced, its premises replaced by the repetitions, and its line numbers shifted. Every citation inside the copy points inside the copy or to a repetition, all in the current box, so all are available; and the copy's boxes close before its last line, the instance of \( Q \). If the copy itself uses derived rules, expand those lines in the same way; this stops, because each derivation cites only results proved before it. So whatever is derivable with derived rules is derivable with the primitive rules alone.

We name the derived rules of this chapter by short tags: \( \rulename{MT} \) for @prp-modus-tollens and \( \rulename{CP} \) for @prp-contrapositive, and more to come in Sections 1.6 and 1.7. Here is the first *use* of one. With \( \rulename{CP} \) available as a rule, modus tollens has a two-step proof.
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {\neg Q}
  \have {3} {\neg Q \to \neg P} \by{CP}{1}
  \have {4} {\neg P} \ie{3,2}
\end{nd}$
\end{center}
```
Line 3 is the instance of @prp-contrapositive with \( P \), \( Q \) replaced by themselves; line 4 is modus ponens on it. Written out in full, line 3 would become a repetition of line 1 followed by lines 2–7 of the derivation of @prp-contrapositive.

::: {#exm-modus-tollens-instance}
[Modus tollens on numbers]

Let \( x \) be a real number with \( x^2 \le 4 \). Use the implication "if \( x > 2 \), then \( x^2 > 4 \)" to show that \( x \le 2 \), naming the derived rule.
:::

::: {.solution}
Take \( P \): "\( x > 2 \)" and \( Q \): "\( x^2 > 4 \)". The implication is \( P \to Q \). (It holds because \( x > 2 > 0 \) gives \( x^2 = x \cdot x > 2x > 4 \).) The hypothesis \( x^2 \le 4 \) is \( \neg Q \), since \( x^2 \le 4 \) and \( x^2 > 4 \) are exact negations of each other. By \( \rulename{MT} \) (@prp-modus-tollens), \( \neg P \), that is, \( \neg(x > 2) \), which is \( x \le 2 \).
:::

Two misuses are ruled out by @def-derived-rule. A derived rule may be used only **after** its sequent has been derived. And the replacement must be uniform: from \( P \to Q \) and \( \neg R \), \( \rulename{MT} \) gives nothing, since no single statement in place of \( Q \) turns the pair into \( P \to Q \) and \( \neg Q \).

## Disjunctive syllogism: the impossible case

Argument A of Section 1.1 also used a second pattern: a case split in which one case is impossible. "Every integer is odd or even; \( n \) is not odd; so \( n \) is even." This pattern is common enough to record.

::: {#prp-disjunctive-syllogism}
[Disjunctive Syllogism]

\( P \vee Q, \; \neg P \vdash Q \).
:::

::: {.proof}
The following is a derivation with premises \( P \vee Q \) and \( \neg P \), and last line \( Q \).
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee Q}
  \hypo {2} {\neg P}
  \open
  \hypo {3} {P}
  \have {4} {\bot} \ne{3,2}
  \have {5} {Q} \be{4}
  \close
  \open
  \hypo {6} {Q}
  \close
  \have {7} {Q} \oe{1,3-5,6-6}
\end{nd}$
\end{center}
```
The two boxes \( \lines{3}{5} \) and \( \lines{6}{6} \) are separate; the second consists of its assumption alone, which is already the statement \( Q \) that \( \rulename{\vee E} \) needs. This proves the proposition.
:::

In the first box, the case \( P \) is impossible given \( \neg P \), and \( \rulename{\bot E} \) turns that impossibility into the required conclusion. This is how "this case cannot occur" is written as a rule: a case that cannot occur may be closed with any conclusion we like, in particular the one the other case reaches. Its tag as a derived rule is \( \rulename{DS} \).

## Even squares, and the square root of two

We can now prove the fact from Section 1.1, with every rule named. Three school facts about integers enter as premises. An integer \( n \) is **even** if \( n = 2k \) for some integer \( k \), and **odd** if \( n = 2k + 1 \) for some integer \( k \); and

::: {.enumerate options="label=(E\arabic*)"}
1. every integer is odd or even;
2. no integer is both even and odd;
3. the square of an odd integer is odd.
:::

The third is a computation: if \( n = 2k + 1 \) for an integer \( k \), then
\[
n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1 ,
\]
and \( 2k^2 + 2k \) is an integer. Naming the integer \( k \) is a step about "there exists" ("there is a \( k \) with \( n = 2k + 1 \); take one"), and the rules for such steps come in Chapter 3.

::: {#thm-square-even-implies-even}
[Even Square, Even Number]

Let \( n \) be an integer. If \( n^2 \) is even, then \( n \) is even.
:::

::: {.idea}
The hypothesis "\( n^2 \) is even" hands us nothing to compute with, while "\( n \) is odd" hands us \( n = 2k + 1 \). So we turn (E3) around by @prp-contrapositive: an integer whose square fails to be odd fails to be odd itself. Then "odd or even", with one option ruled out, leaves "even".
:::

::: {.proof}
Suppose \( n^2 \) is even \( [\text{assumption for } \rulename{{\to}I}] \). If \( n^2 \) were odd, it would be both even and odd, contradicting (E2) \( [\rulename{\neg E}] \); hence \( n^2 \) is not odd \( [\rulename{\neg I}] \). By (E3), if \( n \) is odd then \( n^2 \) is odd, so @prp-contrapositive gives: if \( n^2 \) is not odd, then \( n \) is not odd \( [\rulename{CP}] \). Hence \( n \) is not odd \( [\rulename{{\to}E}] \). By (E1), \( n \) is odd or \( n \) is even, and \( n \) is not odd, so @prp-disjunctive-syllogism gives that \( n \) is even \( [\rulename{DS}] \). This proves that if \( n^2 \) is even, then \( n \) is even \( [\rulename{{\to}I}] \).
:::

Every step is a primitive rule or one of the derived rules \( \rulename{CP} \) and \( \rulename{DS} \). The argument feels like "suppose not", and written out in full it does contain one: \( \rulename{CP} \) assumes that \( n \) is odd, reaches \( \bot \), and concludes that \( n \) is **not** odd. What it never does is assume that \( n \) is not even and conclude from a contradiction that \( n \) **is** even. Every negation in it is introduced; none is removed. The difference will matter in Section 1.6.

The theorem is the key to one of the oldest proofs in mathematics. Its shape is \( \rulename{\neg I} \): the claim is negative, so we assume its opposite and look for \( \bot \). The school fact it needs is about writing fractions:

**(L)** Every rational number can be written as \( p/q \) with \( p \) and \( q \) integers, \( q \ne 0 \), and \( p \) and \( q \) **not both even**.

This holds because a fraction whose numerator and denominator are both even can be reduced by \( 2 \), and the reduction cannot go on for ever, since the denominator shrinks in absolute value each time. Making "cannot go on for ever" precise needs the well-ordering of the natural numbers, which comes in Chapter 6; here we take (L) as known.

::: {#thm-sqrt2-irrational}
[Irrationality of the Square Root of Two]

There is no rational number whose square is \( 2 \). In other words, \( \sqrt{2} \) is irrational.
:::

::: {.idea}
Fix a rational number \( r \) and prove the negative statement \( r^2 \ne 2 \) by \( \rulename{\neg I} \): assume \( r^2 = 2 \) and hunt for \( \bot \). Write \( r = p/q \) as in (L), so that the equation becomes \( p^2 = 2q^2 \). The only hypothesis with any bite is "not both even", so the contradiction must come from showing that \( p \) and \( q \) **are** both even, and @thm-square-even-implies-even is the tool for that, used twice. *Before reading on: the second use of @thm-square-even-implies-even needs the line "\( q^2 \) is even". From which two earlier lines of the proof will it come?*
:::

::: {.proof}
Let \( r \) be a rational number, and suppose \( r^2 = 2 \) \( [\text{assumption for } \rulename{\neg I}] \). By (L), \( r = p/q \) for integers \( p \) and \( q \) with \( q \ne 0 \), not both even. Then \( p^2 = r^2 q^2 = 2q^2 \), so \( p^2 \) is even. By @thm-square-even-implies-even, \( p \) is even \( [\rulename{{\to}E}] \), say \( p = 2m \) for an integer \( m \). Then \( 4m^2 = 2q^2 \), so \( q^2 = 2m^2 \), and \( q^2 \) is even. By @thm-square-even-implies-even again, \( q \) is even \( [\rulename{{\to}E}] \). So \( p \) and \( q \) are both even \( [\rulename{\wedge I}] \), while they were chosen not both even; this is a contradiction \( [\rulename{\neg E}] \). Hence \( r^2 \ne 2 \) \( [\rulename{\neg I}] \).

Since \( r \) was an arbitrary rational number, no rational number has square \( 2 \). This proves the theorem.
:::

::: {.check}
In the proof, which step is \( \rulename{\neg E} \), and which two statements does it cite?
:::

::: {.solution}
The step "this is a contradiction". It cites "\( p \) and \( q \) are both even", derived inside the box of \( r^2 = 2 \) by \( \rulename{\wedge I} \), and "\( p \) and \( q \) are not both even", which (L) supplied when \( p \) and \( q \) were chosen. In the skeleton below these are lines 11 and 2, and the step is line 12.
:::

The propositional part of the proof fits in a derivation. Fix \( r \) and the integers \( p \), \( q \) that (L) supplies. Lines 1 and 2 record what (L) says about them; lines 3 and 4 are @thm-square-even-implies-even for \( n = p \) and \( n = q \); the lines marked "algebra" are the computations of the proof.
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {r = p/q,\ q \neq 0}
  \hypo {2} {\neg(p \text{ even} \wedge q \text{ even})}
  \hypo {3} {p^2 \text{ even} \to p \text{ even}}
  \hypo {4} {q^2 \text{ even} \to q \text{ even}}
  \open
  \hypo {5} {r^2 = 2}
  \have {6} {p^2 = 2q^2} \by{algebra}{1,5}
  \have {7} {p^2 \text{ even}} \by{def.\ of even}{6}
  \have {8} {p \text{ even}} \ie{3,7}
  \have {9} {q^2 \text{ even}} \by{algebra}{6,8}
  \have {10} {q \text{ even}} \ie{4,9}
  \have {11} {p \text{ even} \wedge q \text{ even}} \ai{8,10}
  \have {12} {\bot} \ne{11,2}
  \close
  \have {13} {\neg(r^2 = 2)} \ni{5-12}
\end{nd}$
\end{center}
```
Line 13 is \( r^2 \ne 2 \). Two steps of the proof lie outside the skeleton: choosing \( p \), \( q \) and \( m \), and passing from the arbitrary \( r \) to every rational number. Both are quantifier rules, which come in Chapter 3.

Notice also what the proof does **not** need: that \( \sqrt{2} \) exists as a real number. The theorem is a statement about rational numbers only. Chapter 10 uses it in exactly this form, as evidence that the rational numbers have a gap where \( \sqrt{2} \) should be.

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
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \hypo {2} {\neg P}
  \have {3} {\bot} \ne{1,2}
  \have {4} {Q} \be{3}
\end{nd}$
\end{center}
```
has premises \( P \) and \( \neg P \) and last line \( Q \). This proves the proposition.
:::

::: {#prp-vacuous-implication}
[Vacuous Implication]

\( \neg P \vdash P \to Q \).
:::

::: {.proof}
The derivation
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P}
  \open
  \hypo {2} {P}
  \have {3} {\bot} \ne{2,1}
  \have {4} {Q} \be{3}
  \close
  \have {5} {P \to Q} \ii{2-4}
\end{nd}$
\end{center}
```
has premise \( \neg P \) and last line \( P \to Q \). This proves the proposition.
:::

Apply @prp-vacuous-implication with \( P \): "\( x^2 < 0 \)" and \( Q \): "\( x = 7 \)". The premise \( \neg(x^2 < 0) \) holds for every real \( x \), so "if \( x^2 < 0 \), then \( x = 7 \)" is derivable, and the derivation is the ordinary proof: *suppose \( x^2 < 0 \); this contradicts \( x^2 \ge 0 \); so this case cannot occur, and in it anything holds, in particular \( x = 7 \).* An implication whose hypothesis is false is called **vacuously true**. Nothing about it was decided by convention. It is forced by two rules that each look harmless: \( \rulename{{\to}I} \), which proves an implication by assuming its hypothesis, and \( \rulename{\bot E} \), which closes an impossible case.

Everyday language agrees. A friend says: "if you finish the exercises by Friday, I will buy you lunch". You do not finish them. Whatever your friend does on Friday, the promise has not been broken. *A promise never tested is never broken.*

Vacuous truth is not a curiosity; it is what makes case splits work. The impossible case in the derivation of @prp-disjunctive-syllogism was closed by \( \rulename{\bot E} \), at line 5. When Chapter 2 gives each connective a truth table, the rows of \( \to \) with a false hypothesis are the ones that \( \rulename{\bot E} \) and @prp-vacuous-implication force.

::: {.warning}
"True" is not "useful". The statements "if \( x^2 < 0 \), then \( x = 7 \)" and "if \( x^2 < 0 \), then \( x \ne 7 \)" are both true, by @prp-vacuous-implication, and neither says anything about \( 7 \). Likewise "if \( n \) is an even prime greater than \( 2 \), then \( n = 17 \)" is true and empty. When a hypothesis turns out to be impossible, suspect the hypothesis; do not believe the conclusion.
:::

## What the rules sound like

Here are the rows of the rule, phrase and Lean table for this section's rules. As before, the last column is for readers who use a proof assistant, and nothing depends on it.

| Rule | You write | Lean |
|------|--------------------------------------|------------------------|
| \( \rulename{\neg I} \) | "Suppose \( P \). … This is a contradiction. Hence not \( P \)." | `intro hp` (goal `False`) |
| \( \rulename{\neg E} \) | "This contradicts \( \neg P \)." | `exact hn hp` |
| \( \rulename{\bot E} \) | "This case cannot occur." | `exfalso` |
| \( \rulename{MT} \) | "Since \( Q \) fails, so does \( P \)." | `mt h hnq` |

In Lean, \( \neg P \) is defined to be \( P \to \bot \), with \( \bot \) written `False`, the reading of the remark in the first subsection; so `intro` performs both \( \rulename{{\to}I} \) and \( \rulename{\neg I} \).

## Exercises

### A. Check your understanding

::: {#exr-negation-and-contradiction-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the rules \( \rulename{\neg I} \) and \( \rulename{\bot E} \).
2. Match each sentence, taken from proofs, with the rule it uses: \( \rulename{\neg I} \), \( \rulename{\neg E} \) or \( \rulename{\bot E} \).
    - "But \( n \) was assumed odd, and we have just shown it is even."
    - "Suppose \( 0 \) had a reciprocal \( y \). Then \( 1 = 0 \cdot y = 0 \), which is absurd. So \( 0 \) has no reciprocal."
    - "In this case \( x^2 < 0 \), which is impossible, so there is nothing to prove."
3. In the proof of @thm-sqrt2-irrational, the sentence "\( p \) is even" follows from "\( p^2 \) is even". Which result and which rule justify it?
4. Where in the proof of @thm-sqrt2-irrational is (L) used, and what would go wrong if (L) said only "\( r = p/q \) with \( q \ne 0 \)"?
5. Run the proof of @thm-sqrt2-irrational with \( 4 \) in place of \( 2 \): assume \( r^2 = 4 \) and write \( r = p/q \) as in (L). Which step can no longer be justified? (The conclusion "no rational number has square \( 4 \)" is false, so some step must fail.)
:::
:::

::: {.solution}
(a) \( \rulename{\neg I} \): if a box opened by the assumption \( P \) contains \( \bot \) as a line of its own, we may close it and write \( \neg P \). \( \rulename{\bot E} \): from a line \( \bot \) we may write any statement (@def-rules-negation).

(b) In order: \( \rulename{\neg E} \), since "odd" and "even" clash by (E2), giving \( \bot \); \( \rulename{\neg I} \), since the conclusion is the negative statement "\( 0 \) has no reciprocal", reached by assuming the opposite; \( \rulename{\bot E} \), closing an impossible case with whatever the case needs.

(c) @thm-square-even-implies-even, instantiated at \( n = p \), is the implication "if \( p^2 \) is even, then \( p \) is even"; together with "\( p^2 \) is even" it gives "\( p \) is even" by \( \rulename{{\to}E} \) (line 8 of the skeleton, citing lines 3 and 7).

(d) The fact (L) supplies the line "\( p \) and \( q \) are not both even" (line 2 of the skeleton), which the final \( \rulename{\neg E} \) cites. Without that clause the proof still derives "both even", but it contradicts nothing (\( 2 = 4/2 \) has both even), and no \( \bot \) is reached.

(e) With \( r^2 = 4 \) we get \( p^2 = 4q^2 = 2(2q^2) \), so \( p^2 \) is even and \( p \) is even, \( p = 2k \). Then \( 4k^2 = 4q^2 \), so \( q^2 = k^2 \). This is where the proof stalls: nothing says \( q^2 \) is even, so @thm-square-even-implies-even cannot be applied to \( q \). Indeed for \( r = 2 = 2/1 \) we have \( q = 1 \), which is odd. Every step before the stall is valid; the proof simply fails to reach \( \bot \).
:::

### B. Practice

::: {#exr-negation-and-contradiction-b1}
[B1: The other disjunctive syllogism]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( P \vee Q, \; \neg Q \vdash P \) by a derivation from the primitive rules.
2. Let \( x \) be a real number with \( x^2 = 1 \) and \( x > 0 \). You may use that \( x^2 = 1 \) implies \( x = 1 \) or \( x = -1 \). Deduce that \( x = 1 \), naming the result you use.
:::
:::

::: {.solution}
(a) As in @prp-disjunctive-syllogism, with the roles of the boxes exchanged: now the case \( Q \) is the impossible one.
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee Q}
  \hypo {2} {\neg Q}
  \open
  \hypo {3} {P}
  \close
  \open
  \hypo {4} {Q}
  \have {5} {\bot} \ne{4,2}
  \have {6} {P} \be{5}
  \close
  \have {7} {P} \oe{1,3-3,4-6}
\end{nd}$
\end{center}
```

(b) Since \( x^2 = 1 \), we have \( x = 1 \) or \( x = -1 \). Since \( x > 0 \) and \( -1 < 0 \), we have \( x \ne -1 \). By part (a), with \( P \): "\( x = 1 \)" and \( Q \): "\( x = -1 \)", used as a derived rule (@def-derived-rule), we conclude \( x = 1 \).
:::

::: {#exr-negation-and-contradiction-b2}
[B2: Putting a derivation in order]

Here are nine lines, each a statement with its justification. Seven of them, in the right order and with the right boxes, form a derivation of \( P \to Q \vdash \neg Q \to \neg P \). Give the order, and say where each box opens and closes. Then say why each of the other two lines cannot be used.

::: {.enumerate options="label=(\roman*)"}
1. \( \neg Q \to \neg P \), by \( \rulename{{\to}I} \) on the box from \( \neg Q \) to \( \neg P \).
2. \( Q \), by \( \rulename{{\to}E} \) from \( P \to Q \) and \( P \).
3. \( P \to Q \), premise.
4. \( \neg P \), by \( \rulename{\neg I} \) on the box from \( P \) to \( \bot \).
5. \( \neg Q \), assumption.
6. \( \bot \), by \( \rulename{\neg E} \) from \( Q \) and \( \neg Q \).
7. \( P \), assumption.
8. \( \neg P \), assumption, opening the box for the \( \rulename{\neg I} \) that proves \( \neg P \).
9. \( Q \), by \( \rulename{{\to}E} \) from \( P \to Q \) and the assumption \( P \) of (vii), written directly below (iv).
:::
:::

::: {.solution}
The order is (iii), (v), (vii), (ii), (vi), (iv), (i), with one box opened by (v) and closed after (iv), and a second box inside it, opened by (vii) and closed after (vi). This is the derivation of @prp-contrapositive. It is the only admissible order. The premise comes first. (i) needs a box from \( \neg Q \) to \( \neg P \), so (v) opens a box whose last line is (iv). (iv) needs a box from \( P \) to \( \bot \) inside it, so (vii) opens a box whose last line is (vi). Inside that box, (ii) needs (vii), and (vi) needs (ii) and (v).

(viii) cannot be used. \( \rulename{\neg I} \) proves \( \neg P \) from a box opened by \( P \), the statement being negated. A box opened by \( \neg P \) and ending in \( \bot \) would give \( \neg\neg P \). (ix) cannot be used where it is placed. Directly below (iv), the box opened by (vii) has closed, so the assumption \( P \) is not available (@def-derivation). Placed inside that box, the same line is (ii).
:::

::: {#exr-negation-and-contradiction-b3}
[B3: The square root of three]

You may use that every integer can be written as \( 3k \), \( 3k + 1 \) or \( 3k + 2 \) with \( k \) an integer, in one way only, and that every rational number can be written as \( p/q \) with integers \( p \), \( q \), \( q \ne 0 \), and \( p \), \( q \) not both divisible by \( 3 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( n \) is an integer and \( n^2 \) is divisible by \( 3 \), then \( n \) is divisible by \( 3 \).
2. Hence prove that no rational number has square \( 3 \).
:::
:::

::: {.solution}
(a) Suppose \( n^2 \) is divisible by \( 3 \), so \( n^2 \) has the form \( 3j \) with \( j \) an integer. The integer \( n \) has the form \( 3k \), \( 3k + 1 \) or \( 3k + 2 \), and we argue by cases \( [\rulename{\vee E}] \).

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

(b) Let \( r \) be a rational number and suppose \( r^2 = 3 \) \( [\text{assumption for } \rulename{\neg I}] \). Write \( r = p/q \) with \( p \), \( q \) not both divisible by \( 3 \). Then \( p^2 = 3q^2 \), so \( 3 \) divides \( p^2 \), and by (a), \( p = 3m \) for an integer \( m \). Then \( 9m^2 = 3q^2 \), so \( q^2 = 3m^2 \), and by (a) again, \( 3 \) divides \( q \). So \( 3 \) divides both \( p \) and \( q \), contradicting their choice \( [\rulename{\neg E}] \). Hence \( r^2 \ne 3 \) \( [\rulename{\neg I}] \). Since \( r \) was an arbitrary rational number, no rational number has square \( 3 \).
:::

::: {#exr-negation-and-contradiction-b4}
[B4: A premise that turns on itself]

Show that \( P \to Q, \; Q \to \neg P \vdash \neg P \). Then say in one sentence what the sequent means.
:::

::: {.solution}
The goal \( \neg P \) is a negation, so assume \( P \). The two premises, used in turn, turn \( P \) into \( \neg P \), and the clash gives \( \bot \).
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {Q \to \neg P}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \have {5} {\neg P} \ie{2,4}
  \have {6} {\bot} \ne{3,5}
  \close
  \have {7} {\neg P} \ni{3-6}
\end{nd}$
\end{center}
```
In words: if \( P \) leads to \( Q \), and \( Q \) rules \( P \) out, then \( P \) refutes itself, and so \( P \) fails. Line 5 is the moment of self-refutation: the assumption has produced its own negation.
:::

### C. Going deeper

::: {#exr-negation-and-contradiction-c1}
[C1: The square root of six]

Prove that no rational number has square \( 6 \). Use only the facts (E1)–(E3), (L), and @thm-square-even-implies-even, and name the rule at each logical step.
:::

::: {.solution}
[Hint 1]

Follow the proof of @thm-sqrt2-irrational. After writing \( p = 2m \), you will need to show that \( q \) is even without knowing that \( q^2 \) is even.
:::

::: {.solution}
[Hint 2]

You will reach \( 3q^2 = 2m^2 \), so \( 3q^2 \) is even. The proof of @thm-square-even-implies-even passed from "\( n^2 \) is even" to "\( n \) is even"; imitate its shape for \( 3q^2 \) and \( q \).
:::

::: {.solution}
Let \( r \) be a rational number and suppose \( r^2 = 6 \) \( [\text{assumption for } \rulename{\neg I}] \). By (L), \( r = p/q \) with integers \( p \), \( q \), \( q \ne 0 \), not both even. Then \( p^2 = 6q^2 = 2(3q^2) \) is even, so \( p \) is even by @thm-square-even-implies-even \( [\rulename{{\to}E}] \); write \( p = 2m \). Then \( 4m^2 = 6q^2 \), that is, \( 3q^2 = 2m^2 \), so \( 3q^2 \) is even.

We claim \( q \) is even. By (E1), \( q \) is odd or even, and we rule out odd, so that @prp-disjunctive-syllogism applies. Suppose \( q \) is odd \( [\text{assumption for } \rulename{\neg I}] \). Then \( q^2 \) is odd by (E3), say \( q^2 = 2j + 1 \), and then \( 3q^2 = 6j + 3 = 2(3j + 1) + 1 \) is odd. But \( 3q^2 \) is even, and by (E2) no integer is both; this is \( \bot \) \( [\rulename{\neg E}] \). Hence \( q \) is not odd \( [\rulename{\neg I}] \), and so \( q \) is even \( [\rulename{DS}] \).

So \( p \) and \( q \) are both even \( [\rulename{\wedge I}] \), contradicting (L) \( [\rulename{\neg E}] \). Hence \( r^2 \ne 6 \) \( [\rulename{\neg I}] \), and since \( r \) was arbitrary, no rational number has square \( 6 \).

**Marking scheme.** (10 points)
- 2: opens with \( \rulename{\neg I} \): a fixed rational \( r \), the assumption \( r^2 = 6 \), and \( r = p/q \) with \( p \), \( q \) not both even from (L).
- 2: derives \( p \) even from \( p^2 = 2(3q^2) \) by @thm-square-even-implies-even.
- 3: derives \( q \) even from \( 3q^2 = 2m^2 \), with the odd case ruled out by a correct parity computation and (E2).
- 2: reaches \( \bot \) by clashing "both even" with (L), and concludes \( r^2 \ne 6 \) by \( \rulename{\neg I} \).
- 1: rules named at the logical steps, and the passage from the arbitrary \( r \) to every rational number.
Fatal errors (0 for the step): applying @thm-square-even-implies-even to \( q \) with only \( 3q^2 \) known to be even; using "\( 6 \mid n^2 \Rightarrow 6 \mid n \)" without proof.
A proof that works with divisibility by \( 3 \) instead (using the facts of B3) earns full marks if every step is justified from facts it states.
:::

::: {#exr-negation-and-contradiction-c2}
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

(b) The step "\( n^2 \) divisible by \( 4 \) implies \( n \) divisible by \( 4 \)" is a false lemma: for \( n = 2 \), \( n^2 = 4 \) is divisible by \( 4 \), but \( 2 \) is not. It fails exactly on the witness of (a): with \( r = 2/1 \) we have \( p = 2 \), and the lemma would claim that \( 4 \) divides \( 2 \).

(c) The last step is \( \rulename{\neg I} \), applied to the box opened by "\( r^2 = 4 \)". The rule is applied correctly, but the box contains a line that is not justified: the false lemma was used as if it were a premise available everywhere, through \( \rulename{{\to}E} \). A derivation is only as good as its premises. In @thm-sqrt2-irrational the corresponding lemma is @thm-square-even-implies-even, which we proved; here nothing proves the lemma, and nothing could. Compare part (e) of A1, where the honest proof stalls without reaching \( \bot \); here \( \bot \) is "reached" through a false line.
:::

<!-- dependency ledger
exm-square-plus-one (example): x^2 >= 0 for real x; a >= b is the negation of a < b (exactly one holds); a != b means not(a = b) | school algebra, taken as known (ch01 blueprint, Allowed prerequisites), stated in prose; Ch 10 re-proves the order facts (prose pointer)
def-derived-rule (claim): pasting a derivation (repetitions, shifted line numbers) keeps every citation available | argued inline in the paraphrase, from def-derivation's scope rule
exm-modus-tollens-instance (example): x > 2 implies x^2 > 4; x^2 <= 4 is the negation of x^2 > 4 | school algebra, shown inline
thm-square-even-implies-even (proof): (E1) every integer is odd or even; (E2) no integer is both; (E3) odd squared is odd | (E1), (E2) school facts (ch01 blueprint, Allowed prerequisites), stated in the text; (E3) computed inline
thm-square-even-implies-even (proof): naming k with n = 2k + 1 (a there-exists step) | used as school reasoning; its rule comes in Ch 3 (prose pointer)
thm-sqrt2-irrational (proof): (L) every rational is p/q with q != 0, p and q not both even | school fact taken as known, stated as (L) in the text; justified informally in prose; precise proof by well-ordering in Ch 6 (prose pointer, nothing in Ch 1 depends on that proof)
thm-sqrt2-irrational (proof): p^2 = r^2 q^2; 4m^2 = 2q^2 gives q^2 = 2m^2; "r arbitrary, so every rational" | school algebra; the last step is a quantifier step (Ch 3, prose pointer)
exr-negation-and-contradiction-b1 (solution): -1 < 0 | school algebra; x^2 = 1 gives x = 1 or x = -1 is supplied by the item
exr-negation-and-contradiction-b3 (solution): every integer is 3k, 3k+1 or 3k+2 in one way only; the mod-3 form of (L) | stated in the item as usable facts
exr-negation-and-contradiction-c1 (solution): parity computations 3(2j+1) = 2(3j+1)+1 | school algebra, shown inline
exr-negation-and-contradiction-c2 (solution): 2 is not divisible by 4 | arithmetic
-->
