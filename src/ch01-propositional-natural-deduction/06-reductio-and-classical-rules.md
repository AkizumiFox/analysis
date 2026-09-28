# Proof by Contradiction and the Classical Rules

Every rule so far either builds a statement or takes one apart, and the negation rules of @def-rules-negation are no exception: \( \rulename{\neg I} \) builds \( \neg P \) from a box that opens with \( P \) and ends in \( \bot \). No rule so far turns a refutation of \( \neg P \) into \( P \) itself. This section adds the rule that does, reductio ad absurdum, derives from it the classical laws that mathematics uses without noticing, and shows that three of them are one principle in three forms.

## Two boxes that look alike

Here are two arguments that a mathematician would both call "proof by contradiction".

The first is the proof of @thm-sqrt2-irrational. It assumes that \( \sqrt 2 \) is rational, reaches a contradiction, and concludes that \( \sqrt 2 \) is **not** rational. In the language of @def-rules-negation, it opens a box with the assumption \( P \) ("\( \sqrt 2 \) is rational"), reaches \( \bot \) inside it, and closes the box to get \( \neg P \). That is \( \rulename{\neg I} \).

The second is an argument of a kind that analysis uses constantly.

::: {#exm-raa-zero}
[A number below every positive number]

Let \( x \) be a real number with \( x \ge 0 \), and suppose that \( x \le \varepsilon \) for **every** real number \( \varepsilon > 0 \). Prove that \( x = 0 \).
:::

::: {.solution}
Suppose, for a contradiction, that \( x \ne 0 \). Since \( x \ge 0 \) and \( x \ne 0 \), we have \( x > 0 \). Then \( \varepsilon \coloneqq x/2 \) is a real number with \( \varepsilon > 0 \), so the hypothesis applies to it and gives \( x \le x/2 \). Subtracting \( x/2 \) from both sides gives \( x/2 \le 0 \), and multiplying by \( 2 \) gives \( x \le 0 \). This contradicts \( x > 0 \). Hence \( x = 0 \).
:::

(The step "the hypothesis applies to it" uses a rule for "every", which Chapter 3 makes precise; the facts about \( \le \) are school algebra, which Chapter 10 derives from axioms.)

Look at its shape. The box opens with the assumption \( \neg P \), where \( P \) is "\( x = 0 \)", reaches \( \bot \), and closes to give \( P \). If we tried to justify the last line with \( \rulename{\neg I} \), we would get \( \neg\neg P \), "it is not the case that \( x \ne 0 \)", and not \( P \). The two arguments put their negations in different places: \( \rulename{\neg I} \) puts a \( \neg \) **into** the conclusion, and this second argument takes one **out**.

Can the rules we have take it out? Try the smallest case, \( P \) from \( \neg\neg P \). The goal \( P \) is a bare letter, so no introduction rule applies. The premise can be used only by \( \rulename{\neg E} \), which needs \( \neg P \) beside it, so we assume \( \neg P \) in a box. The box reaches \( \bot \) at once, and \( \rulename{\neg I} \) closes it with \( \neg\neg P \): the premise again. Every attempt goes round this circle, and in fact no derivation of \( P \) from \( \neg\neg P \) uses only the rules of the earlier sections. Chapter 2 proves that, by reading statements with more than two truth values. Here we name the missing step and add it as a rule.

## The rule RAA

*To prove \( P \), it is enough to show that "not \( P \)" leads to a contradiction.*

::: {#def-rule-raa}
[Reductio ad absurdum]

**RAA** (**reductio ad absurdum**). Open a box with the assumption \( \neg P \). If \( \bot \) is reached as a line of that box, not inside a further box, we may close the box and write \( P \). Schematically:

```{=latex}
% schema (a schema: lines i, j, k are placeholders, set with fitch.sty's numbering options)
\begin{center}
$\begin{nd}
  \open
  \hypo[i][0] {i} {\neg P}
  \have[\ ][0] {} {\vdots}
  \have[j][0] {j} {\bot}
  \close
  \have[k][0] {k} {P} \raa{i-j}
\end{nd}$
\end{center}
```

The assumption \( \neg P \) is **discharged** when the box closes: like every assumption, it may be cited only by lines inside its box.
:::

In words: the box is a thought experiment in which \( P \) fails. If the experiment ends in \( \bot \), then \( P \) cannot fail, and RAA lets us write \( P \) itself, **not** merely \( \neg\neg P \). The justification cites the box as a range, as \( \rulename{\neg I} \) does.

Set the two rules side by side:

| Rule | The box opens with | The box ends with | After the box |
|---|---|---|---|
| \( \rulename{\neg I} \) | \( P \) | \( \bot \) | \( \neg P \) |
| RAA | \( \neg P \) | \( \bot \) | \( P \) |

The rows differ only in where the \( \neg \) sits, and that makes RAA different in kind. Every other primitive rule is the introduction or the elimination rule of one connective (\( \rulename{\bot E} \) is the elimination rule of \( \bot \)); repetition is a clause of @def-derivation, not a rule for a connective. RAA belongs to no connective: it applies to every statement \( P \), whatever its main connective.

The box opens with the negation of the **whole** of \( P \): if \( P \) is \( Q \vee R \), the box opens with \( \neg(Q \vee R) \), not with \( \neg Q \vee R \). If \( P \) is itself a negation \( \neg Q \), the box opens with \( \neg\neg Q \), and then RAA can always be avoided: open a \( \rulename{\neg I} \) box with \( Q \) instead, derive \( \neg\neg Q \) from \( Q \) inside it as in @exm-double-negation-introduction, and continue as the RAA box did, citing that line wherever the RAA box cited its assumption. So RAA is never needed to prove a **negation**; it earns its place on the other goals.

::: {.warning}
The assumption that opens an RAA box must be the **exact** negation of the goal. To prove \( x \le 1 \) by contradiction, assume \( x > 1 \), since for real numbers "not \( x \le 1 \)" says \( x > 1 \). Assuming \( x \ge 1 \) instead is a common slip: it is not the negation, because \( x = 1 \) satisfies both \( x \le 1 \) and \( x \ge 1 \). A box opened with \( x \ge 1 \) cannot reach \( \bot \) when \( x = 1 \) is possible, and a "contradiction" that seems to be reached hides an error.
:::

**Examples.** The first is the degenerate one: RAA can prove \( P \) from \( P \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \open
  \hypo {2} {\neg P}
  \have {3} {\bot} \ne{1,2}
  \close
  \have {4} {P} \raa{2-3}
\end{nd}$
\end{center}
```

It is legal and pointless, since line 1 already is the goal. It is the purest case of a pattern that turns up in real proofs, a contradiction box whose assumption does nothing except clash with a line we already had; the last warning of this section returns to it.

The second example is @exm-raa-zero. Its box opens with \( \neg(x = 0) \), and its clash, between \( x \le 0 \) and \( x > 0 \) (which says "not \( x \le 0 \)"), is a \( \rulename{\neg E} \).

The third example is the one on which we got stuck.

::: {#prp-double-negation}
[Double Negation]

For every statement \( P \):

::: {.enumerate options="label=(\alph*)"}
1. \( P \vdash \neg\neg P \), by a derivation that does not use RAA;
2. \( \neg\neg P \vdash P \), by a derivation that uses RAA.
:::
:::

::: {.idea}
In (a) the goal \( \neg\neg P \) is the negation of \( \neg P \), so \( \rulename{\neg I} \) asks for a box that opens with \( \neg P \) and reaches \( \bot \). In (b) the goal \( P \) has no connective to introduce, so we open an RAA box, which also opens with \( \neg P \). Both boxes clash with line 1 at once.
:::

::: {.proof}
(a) This is the first derivation of @exm-double-negation-introduction, which uses the rules of @def-rules-negation alone; we repeat it to set it beside (b).

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

(b) An RAA box on \( \neg P \):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg\neg P}
  \open
  \hypo {2} {\neg P}
  \have {3} {\bot} \ne{2,1}
  \close
  \have {4} {P} \raa{2-3}
\end{nd}$
\end{center}
```

Line 3 applies \( \rulename{\neg E} \) to the statement \( \neg P \) on line 2 and to its negation \( \neg\neg P \) on line 1. This proves both parts.
:::

In both derivations lines 2 and 3 form a box that opens with \( \neg P \) and reaches \( \bot \) by a clash with line 1. Only the rule that closes the box differs, and with it the last line. So the two directions are not mirror images: one needs only the rules for \( \neg \), the other needs the new rule.

**Non-example by minimal change.** Change only the last line of (a), from \( \neg\neg P \) to \( P \), keeping the justification \( \rulename{\neg I}\ \lines{2}{3} \). Lines 1–3 still check. What fails is the conclusion of \( \rulename{\neg I} \), which must be the negation of the box's assumption, here \( \neg\neg P \). To write \( P \), the justification must be RAA.

From now on both parts are derived rules in the sense of @def-derived-rule: a line \( \neg\neg P \) may be justified by "\( \rulename{\neg\neg I} \) \( i \)", citing a line \( P \), and a line \( P \) by "\( \rulename{\neg\neg E} \) \( i \)", citing a line \( \neg\neg P \).

::: {.check}
A box opens with the assumption \( \neg(x < 0) \) and reaches \( \bot \). Which of the following may be written after it closes, and by which rule? (i) \( x < 0 \); (ii) \( \neg\neg(x < 0) \); (iii) \( x \ge 0 \).
:::

::: {.solution}
(i) By RAA: the box opened with the negation of \( x < 0 \). (ii) By \( \rulename{\neg I} \): the box opened with \( \neg(x < 0) \), and \( \rulename{\neg I} \) writes the negation of its assumption. (iii) Neither. For real numbers \( x \ge 0 \) says the same as \( \neg(x < 0) \), which is exactly the statement the box has refuted.
:::

**Why add the rule at all?** Without RAA the rules of the earlier sections form a coherent system, and some mathematicians have chosen to work only in it; Chapter 4 tells that story. Ordinary mathematics, though, uses RAA constantly, usually without noticing, and so do the laws derived next.

## The converse of the contrapositive

Each of the next four results has a part whose derivation uses RAA, directly or through excluded middle, and we point to the line where it enters.

@prp-contrapositive derives \( \neg Q \to \neg P \) from \( P \to Q \) with \( \rulename{{\to}I} \) and \( \rulename{\neg I} \) only. In practice we use it the other way round: to prove "if \( n^2 \) is even then \( n \) is even", one proves "if \( n \) is not even then \( n^2 \) is not even", and that step goes from \( \neg Q \to \neg P \) back to \( P \to Q \).

::: {#prp-contrapositive-converse}
[Converse of the Contrapositive]

For all statements \( P \) and \( Q \), \( \neg Q \to \neg P \vdash P \to Q \).
:::

::: {.idea}
The goal is an implication, so the outer box opens with \( P \) and must reach \( Q \). Inside it the goal \( Q \) is a bare letter, and no introduction rule helps. But the premise speaks about \( \neg Q \), which suggests assuming \( \neg Q \) and applying \( \rulename{{\to}E} \). That gives \( \neg P \), which clashes with the \( P \) of the outer box. The inner box opened with \( \neg Q \), so RAA closes it with \( Q \).
:::

::: {.proof}
The derivation is:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg Q \to \neg P}
  \open
  \hypo {2} {P}
  \open
  \hypo {3} {\neg Q}
  \have {4} {\neg P} \ie{1,3}
  \have {5} {\bot} \ne{2,4}
  \close
  \have {6} {Q} \raa{3-5}
  \close
  \have {7} {P \to Q} \ii{2-6}
\end{nd}$
\end{center}
```

Line 5 may cite line 2 because line 2 lies in a box that is still open. RAA enters at line 6. This proves the proposition.
:::

So contraposition behaves like double negation: going from \( P \to Q \) to \( \neg Q \to \neg P \) is free, and coming back costs one RAA. When \( Q \) is itself a negation, the inner goal is a negation and, as noted after @def-rule-raa, the RAA can be avoided.

## Excluded middle

Every integer is even or odd. Every real number is \( \ge 0 \) or \( < 0 \). The purely logical form of such facts is the law \( P \vee \neg P \), which holds for every statement \( P \) with no premises at all.

::: {#prp-excluded-middle}
[Excluded Middle]

For every statement \( P \), \( \vdash P \vee \neg P \).
:::

::: {.idea}
The natural last line, \( \rulename{\vee I} \), needs \( P \) or \( \neg P \), and with no premises we can derive neither. So we argue by RAA on the whole disjunction: assume \( \neg(P \vee \neg P) \), which says that neither side holds, and look for a clash. If \( P \) held, then \( P \vee \neg P \) would hold, against the assumption; so \( \neg P \), by \( \rulename{\neg I} \). But then \( P \vee \neg P \) holds after all, by \( \rulename{\vee I} \), and that is the final clash.
:::

::: {.proof}
The derivation is:

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {\neg (P \vee \neg P)}
  \open
  \hypo {2} {P}
  \have {3} {P \vee \neg P} \oi{2}
  \have {4} {\bot} \ne{3,1}
  \close
  \have {5} {\neg P} \ni{2-4}
  \have {6} {P \vee \neg P} \oi{5}
  \have {7} {\bot} \ne{6,1}
  \close
  \have {8} {P \vee \neg P} \raa{1-7}
\end{nd}$
\end{center}
```

The derivation has no premises, so it shows \( \vdash P \vee \neg P \). RAA is used once, at line 8. This proves the proposition.
:::

Excluded middle becomes a derived rule with no premises: a line \( P \vee \neg P \) may be written anywhere, for any \( P \), justified by LEM with no line cited; pasting in the eight lines above would replace it. Its use is **proof by cases on a statement**: to derive \( R \), derive it once in a box that assumes \( P \) and once in a box that assumes \( \neg P \), and combine the two boxes with the line \( P \vee \neg P \) by \( \rulename{\vee E} \). The next two results use it that way.

## De Morgan's laws

The negation of an "and" is an "or" of negations, and the negation of an "or" is an "and" of negations. For example, a real number \( x \) fails to lie in the interval \( [0, 1] \), that is, \( \neg(0 \le x \wedge x \le 1) \), exactly when \( x < 0 \) or \( x > 1 \). Each law has two directions, so there are four derivations to give.

::: {#prp-de-morgan}
[De Morgan's Laws]

For all statements \( P \) and \( Q \):

::: {.enumerate options="label=(\alph*)"}
1. \( \neg(P \vee Q) \vdash \neg P \wedge \neg Q \);
2. \( \neg P \wedge \neg Q \vdash \neg(P \vee Q) \);
3. \( \neg P \vee \neg Q \vdash \neg(P \wedge Q) \);
4. \( \neg(P \wedge Q) \vdash \neg P \vee \neg Q \).
:::
:::

*Try it first (ten minutes): look for a derivation of (d) with the rules of the earlier sections. Which rule would give its last line, and what would that rule need?*

::: {.idea}
Parts (a)–(c) yield to their goals: in (a) two \( \rulename{\neg I} \) boxes, one per conjunct; in (b) and (c) one \( \rulename{\neg I} \) box, with the disjunction used inside it by \( \rulename{\vee E} \).

Part (d) resists. Its goal is a disjunction, so the natural last line is \( \rulename{\vee I} \), from \( \neg P \) or from \( \neg Q \). But neither follows from the premise alone: with \( P \) true and \( Q \) false the premise is true and \( \neg P \) false, with \( P \) false and \( Q \) true the premise is true and \( \neg Q \) false, and the rules never lead from true premises to a false conclusion (Chapter 2 proves this). The premise itself can be used only by \( \rulename{\neg E} \), against \( P \wedge Q \), which we do not have. So we go round the goal by RAA: assume \( \neg(\neg P \vee \neg Q) \), which says that neither \( \neg P \) nor \( \neg Q \) holds. It gives \( P \) and \( Q \), each by a small RAA box of its own, and together they clash with the premise.
:::

::: {.proof}
(a) Two \( \rulename{\neg I} \) boxes, one for each conjunct, then \( \rulename{\wedge I} \):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \vee Q)}
  \open
  \hypo {2} {P}
  \have {3} {P \vee Q} \oi{2}
  \have {4} {\bot} \ne{3,1}
  \close
  \have {5} {\neg P} \ni{2-4}
  \open
  \hypo {6} {Q}
  \have {7} {P \vee Q} \oi{6}
  \have {8} {\bot} \ne{7,1}
  \close
  \have {9} {\neg Q} \ni{6-8}
  \have {10} {\neg P \wedge \neg Q} \ai{5,9}
\end{nd}$
\end{center}
```

(b) One \( \rulename{\neg I} \) box that opens with \( P \vee Q \). Inside it, \( \rulename{\vee E} \) splits into two cases, and each case clashes with one half of the premise:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P \wedge \neg Q}
  \have {2} {\neg P} \ae{1}
  \have {3} {\neg Q} \ae{1}
  \open
  \hypo {4} {P \vee Q}
  \open
  \hypo {5} {P}
  \have {6} {\bot} \ne{5,2}
  \close
  \open
  \hypo {7} {Q}
  \have {8} {\bot} \ne{7,3}
  \close
  \have {9} {\bot} \oe{4,5-6,7-8}
  \close
  \have {10} {\neg (P \vee Q)} \ni{4-9}
\end{nd}$
\end{center}
```

(c) The same shape as (b), with the roles of \( \wedge \) and \( \vee \) exchanged:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P \vee \neg Q}
  \open
  \hypo {2} {P \wedge Q}
  \have {3} {P} \ae{2}
  \have {4} {Q} \ae{2}
  \open
  \hypo {5} {\neg P}
  \have {6} {\bot} \ne{3,5}
  \close
  \open
  \hypo {7} {\neg Q}
  \have {8} {\bot} \ne{4,7}
  \close
  \have {9} {\bot} \oe{1,5-6,7-8}
  \close
  \have {10} {\neg (P \wedge Q)} \ni{2-9}
\end{nd}$
\end{center}
```

(d) RAA on the goal, and inside it two smaller RAA boxes:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \wedge Q)}
  \open
  \hypo {2} {\neg (\neg P \vee \neg Q)}
  \open
  \hypo {3} {\neg P}
  \have {4} {\neg P \vee \neg Q} \oi{3}
  \have {5} {\bot} \ne{4,2}
  \close
  \have {6} {P} \raa{3-5}
  \open
  \hypo {7} {\neg Q}
  \have {8} {\neg P \vee \neg Q} \oi{7}
  \have {9} {\bot} \ne{8,2}
  \close
  \have {10} {Q} \raa{7-9}
  \have {11} {P \wedge Q} \ai{6,10}
  \have {12} {\bot} \ne{11,1}
  \close
  \have {13} {\neg P \vee \neg Q} \raa{2-12}
\end{nd}$
\end{center}
```

The derivations of (a), (b) and (c) close every box by \( \rulename{\neg I} \) or \( \rulename{\vee E} \) and use no RAA. The derivation of (d) uses RAA at lines 6, 10 and 13. This proves all four laws.
:::

Laws (a)–(c) conclude negations, and \( \rulename{\neg I} \) builds negations. Law (d) concludes a **disjunction**, and \( \rulename{\vee I} \) needs to know **which** side holds, while the premise says only that \( P \) and \( Q \) do not both hold. RAA gets round the missing decision without making it. Excluded middle makes it instead: split on \( P \vee \neg P \); in the case \( P \), a \( \rulename{\neg I} \) box on \( Q \) clashes with the premise through \( P \wedge Q \), giving \( \neg Q \); in the case \( \neg P \) there is nothing to do; and \( \rulename{\vee I} \) finishes each case. Both routes use a classical rule. That no derivation of (d) avoids one is true, but we state it without proof, and nothing in this book depends on it.

::: {.check}
Suppose RAA were deleted from the list of rules. Which of the four derivations in the proof of @prp-de-morgan would still be correct, and what is the first line of the others that would lose its justification?
:::

::: {.solution}
The derivations of (a), (b) and (c) would still be correct: they use \( \rulename{\neg I} \), \( \rulename{\neg E} \), \( \rulename{\vee I} \), \( \rulename{\vee E} \), \( \rulename{\wedge I} \) and \( \rulename{\wedge E} \) only. In the derivation of (d), line 6 is the first to lose its justification: it closes the box that opened with \( \neg P \) and writes \( P \), which is RAA. (Lines 10 and 13 lose theirs too.)
:::

## Implication as a disjunction

In everyday mathematics "if \( P \) then \( Q \)" and "either \( P \) fails or \( Q \) holds" are used interchangeably. One direction of that exchange is free, and the other uses a classical rule.

::: {#prp-implication-as-disjunction}
[Implication as a Disjunction]

For all statements \( P \) and \( Q \):

::: {.enumerate options="label=(\alph*)"}
1. \( \neg P \vee Q \vdash P \to Q \), by a derivation that does not use RAA;
2. \( P \to Q \vdash \neg P \vee Q \), by a derivation that uses LEM.
:::
:::

::: {.idea}
(a) The premise is a disjunction, so we use it by cases, and in each case the goal \( P \to Q \) is an implication, so we open a box with \( P \). In the case \( \neg P \), the box clashes at once and \( \rulename{\bot E} \) gives \( Q \); this is the derivation behind @prp-vacuous-implication. In the case \( Q \), the box repeats \( Q \). (b) The goal is a disjunction and the premise needs \( P \) before it gives anything, so we decide \( P \) first, by excluded middle.
:::

::: {.proof}
(a) \( \rulename{\vee E} \) on the premise, with an implication built in each case:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P \vee Q}
  \open
  \hypo {2} {\neg P}
  \open
  \hypo {3} {P}
  \have {4} {\bot} \ne{3,2}
  \have {5} {Q} \be{4}
  \close
  \have {6} {P \to Q} \ii{3-5}
  \close
  \open
  \hypo {7} {Q}
  \open
  \hypo {8} {P}
  \have {9} {Q} \r{7}
  \close
  \have {10} {P \to Q} \ii{8-9}
  \close
  \have {11} {P \to Q} \oe{1,2-6,7-10}
\end{nd}$
\end{center}
```

Line 9 repeats line 7 inside the box of line 8, because \( \rulename{{\to}I} \) needs \( Q \) as a line of that box itself.

(b) Cases on \( P \):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \have {2} {P \vee \neg P} \lem{}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \have {5} {\neg P \vee Q} \oi{4}
  \close
  \open
  \hypo {6} {\neg P}
  \have {7} {\neg P \vee Q} \oi{6}
  \close
  \have {8} {\neg P \vee Q} \oe{2,3-5,6-7}
\end{nd}$
\end{center}
```

Line 2 is @prp-excluded-middle used as a derived rule, and the only RAA is inside it. This proves both parts.
:::

## One principle in three forms

RAA gave us \( \neg\neg \)E and excluded middle. Had we added one of those two as the new primitive rule instead of RAA, would we have proved less?

To say this exactly, we need two rule forms and one notion. **\( \neg\neg \)E taken as a rule** says: if \( \neg\neg P \) stands on an available line, we may write \( P \). **LEM taken as a rule** says: we may write \( P \vee \neg P \) on any line, for any statement \( P \), citing nothing. Given a list of rules, a rule \( \mathsf{X} \) **derives** a rule \( \mathsf{Y} \) over that list if every use of \( \mathsf{Y} \) in a derivation can be replaced by a fragment that uses only \( \mathsf{X} \) and the rules of the list, without changing the premises or the last line. Then every sequent derivable with \( \mathsf{Y} \) is derivable with \( \mathsf{X} \) instead.

::: {#thm-classical-rules-interderivable}
[The Classical Rules Are Interderivable]

Over the primitive rules other than RAA, each of the three rules RAA, \( \neg\neg \)E and LEM derives the other two. In particular, adding any one of the three to the other primitive rules gives the same derivable sequents.
:::

::: {.idea}
Replacements can be chained, so it is enough to go once round a cycle. ① RAA derives the other two: that is @prp-excluded-middle and @prp-double-negation (b). ② \( \neg\neg \)E derives RAA: \( \rulename{\neg I} \) closes an RAA box, which runs from \( \neg P \) to \( \bot \), with \( \neg\neg P \), and \( \neg\neg \)E finishes. ③ LEM derives \( \neg\neg \)E: split on \( P \vee \neg P \); the case \( P \) is the goal, and the case \( \neg P \) clashes with \( \neg\neg P \).

*Before reading on: in the fragment for ③ below, which rule does line \( k + 4 \) use, and why may line \( k + 3 \) cite line \( m \)?*
:::

::: {.proof}
① Suppose a derivation uses \( \neg\neg \)E at line \( k \), writing \( P \) and citing a line \( m \) that holds \( \neg\neg P \). Replace line \( k \) by the last three lines of the derivation in @prp-double-negation (b), with its premise replaced by line \( m \): a box opening with \( \neg P \), the line \( \bot \) by \( \rulename{\neg E} \) citing the assumption and line \( m \), and then \( P \) by RAA. A use of LEM, writing \( P \vee \neg P \), is replaced by the eight lines of the derivation in @prp-excluded-middle, which has no premises. So RAA derives \( \neg\neg \)E and LEM.

② Suppose a derivation uses RAA at line \( k \), closing a box, lines \( i \) to \( j \), that opens with \( \neg P \) and ends with \( \bot \). Keep the box and replace line \( k \) by two lines:

```{=latex}
% schema (a schema: placeholder line numbers set with fitch.sty's numbering options)
\begin{center}
$\begin{nd}
  \open
  \hypo[i][0] {i} {\neg P}
  \have[\ ][0] {} {\vdots}
  \have[j][0] {j} {\bot}
  \close
  \have[k][0] {k} {\neg\neg P} \ni{i-j}
  \have {k1} {P} \nne{k}
\end{nd}$
\end{center}
```

Line \( k \) is correct by \( \rulename{\neg I} \), since the box opens with \( \neg P \) and \( \neg\neg P \) is the negation of that assumption. Both rules ask for \( \bot \) as a line of the box itself, so the box needs no change. So \( \neg\neg \)E derives RAA.

③ Suppose a derivation uses \( \neg\neg \)E at line \( k \), writing \( P \) and citing a line \( m \) that holds \( \neg\neg P \). Replace line \( k \) by six lines:

```{=latex}
% schema (a schema: placeholder line numbers set with fitch.sty's numbering options)
\begin{center}
$\begin{nd}
  \have[m][0] {m} {\neg\neg P}
  \have[\ ][0] {} {\vdots}
  \have[k][0] {k} {P \vee \neg P} \lem{}
  \open
  \hypo {k1} {P}
  \close
  \open
  \hypo {k2} {\neg P}
  \have {k3} {\bot} \ne{k2,m}
  \have {k4} {P} \be{k3}
  \close
  \have {k5} {P} \oe{k,k1-k1,k2-k4}
\end{nd}$
\end{center}
```

The first case is a one-line box: it opens with \( P \) and so already ends with the goal. In the second case, line \( k + 3 \) may cite line \( m \), because line \( m \) was available at the old line \( k \) and every new line sits in the same boxes as the old line \( k \) or in boxes opened after it. No rule other than LEM and the rules of the list is used. So LEM derives \( \neg\neg \)E.

In each replacement the later lines are renumbered, and a later citation of the old line \( k \) now cites the fragment's last line, which holds the same statement in the same boxes. The premises and the last line of the derivation are unchanged.

Finally, replacements can be chained. LEM derives RAA: replace each use of RAA by the fragment of ②, and then each use of \( \neg\neg \)E so created by the fragment of ③. \( \neg\neg \)E derives LEM: replace each use of LEM by the derivation of ①, and then each use of RAA in it by the fragment of ②. With ①, ② and ③ this shows that each of the three rules derives the other two, as claimed.
:::

So the classical part of our rules is **one** extra principle, whichever of its three forms we write down. Chapter 4 tells the history of the mathematicians who declined it, and what their mathematics looks like.

::: {.remark}
Some books call exactly our RAA "proof by contradiction" or PBC, and some take \( \neg\neg \)E as their primitive rule and derive RAA from it. By @thm-classical-rules-interderivable nothing changes: all these choices prove the same sequents.
:::

::: {.remark}
\( \rulename{\bot E} \) could have been dropped from the primitive rules, since RAA and repetition derive it (@exr-reductio-and-classical-rules-b3 asks for the derivation). We keep it so that the primitive rules other than RAA form a system of their own, the one Chapter 4 studies.
:::

::: {.warning}
An RAA box on \( \neg P \) whose assumption is used **only at its last step**, against a \( P \) derived without it, is legal, but it is a direct proof in disguise: the lines before the clash already derive \( P \), so the box can be deleted. The degenerate derivation of \( P \vdash P \) above is the smallest case. Chapter 4 shows how to spot this costume in written proofs and take it off. (A box that reaches \( \bot \) without using its assumption at all is a different matter: the same lines, written before the box, derive \( \bot \) without it, and \( \rulename{\bot E} \) then gives the goal at once.)
:::

## What the rules sound like

Written mathematics carries these rules in a handful of phrases. The Lean column is for readers who use that proof assistant; nothing later depends on it, and the full dictionary is in Chapter 4.

| Rule | You write | Lean |
|---|---|---|
| RAA | "Suppose, for a contradiction, that \( P \) fails. … This is impossible. Hence \( P \)." | `by_contra h` |
| \( \rulename{\neg\neg E} \) | "It cannot be that \( P \) fails; so \( P \)." | `not_not.mp h` |
| LEM | "Either \( P \) or not. If \( P \), … If not, … In either case, …" | `by_cases h : P` |

The phrase "for a contradiction" does not by itself tell \( \rulename{\neg I} \) from RAA. To tell them apart, look at what is assumed and what is concluded. The proof of @thm-sqrt2-irrational assumes the positive statement and concludes its negation, so it is \( \rulename{\neg I} \); @exm-raa-zero assumes a negation and concludes the positive statement, so it is RAA.

## Exercises

### A. Check your understanding

::: {#exr-reductio-and-classical-rules-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. "Suppose \( 7 \) is even. Then \( 7 = 2k \) for some integer \( k \), so \( k = 7/2 \), which is not an integer. This is impossible. Hence \( 7 \) is not even." Is the last step \( \rulename{\neg I} \), RAA or neither? What did the box open with?
2. "Let \( x \) be real. Suppose \( x^2 \ge 2x - 1 \) fails, that is, \( x^2 < 2x - 1 \). Then \( (x - 1)^2 < 0 \), which is impossible. Hence \( x^2 \ge 2x - 1 \)." Same questions.
3. "Assume \( P \). Then, as shown above, \( Q \). Hence \( P \to Q \)." Same questions.
4. State RAA and \( \rulename{\neg I} \) side by side, and say which of the two the derivation of @prp-double-negation (a) uses.
5. In the derivation of @prp-de-morgan (d), why can the last line not be \( \rulename{\vee I} \) applied to a line derived from the premise?
6. In the same derivation, the assumption \( \neg(\neg P \vee \neg Q) \) on line 2 is cited twice. Name the two lines that cite it, and the rule each uses.
:::
:::

::: {.solution}
(a) \( \rulename{\neg I} \): the box opened with "\( 7 \) is even", and the conclusion is its negation. (\( 7/2 \) is not an integer because \( 3 < 7/2 < 4 \).)

(b) RAA: the box opened with the negation of \( x^2 \ge 2x - 1 \), and the conclusion is \( x^2 \ge 2x - 1 \) itself. (The clash: \( x^2 < 2x - 1 \) rearranges to \( (x - 1)^2 < 0 \), and squares are non-negative.)

(c) Neither: this is \( \rulename{{\to}I} \). The box opened with \( P \) and ended with \( Q \); no \( \bot \) appears.

(d) \( \rulename{\neg I} \): a box that opens with \( P \) and reaches \( \bot \) gives \( \neg P \). RAA: a box that opens with \( \neg P \) and reaches \( \bot \) gives \( P \). The derivation of @prp-double-negation (a) uses \( \rulename{\neg I} \), with \( \neg P \) as the assumption, so its conclusion is the negation of \( \neg P \), namely \( \neg\neg P \).

(e) \( \rulename{\vee I} \) would need \( \neg P \) or \( \neg Q \) on a line derived from the premise. Neither can be derived from \( \neg(P \wedge Q) \) alone: with \( P \) true and \( Q \) false the premise is true and \( \neg P \) is false, and with \( P \) false and \( Q \) true the premise is true and \( \neg Q \) is false, while the rules never lead from true premises to a false conclusion (proved in Chapter 2).

(f) Line 5 cites it, by \( \rulename{\neg E} \) against line 4, \( \neg P \vee \neg Q \); and line 9 cites it, by \( \rulename{\neg E} \) against line 8, the same statement. Both lines lie in boxes inside the box of line 2, which is still open, so the citations are legal.
:::

### B. Practice

::: {#exr-reductio-and-classical-rules-b1}
[B1: Two short derivations]

::: {.enumerate options="label=(\alph*)"}
1. Derive \( \neg\neg\neg P \vdash \neg P \) without using RAA.
2. Derive \( \neg P \to Q, \ \neg P \to \neg Q \vdash P \), using RAA.
:::

*Hint: in (a) the goal is a negation; in (b) it is a bare letter.*
:::

::: {.solution}
(a) The goal \( \neg P \) is a negation, so we open a \( \rulename{\neg I} \) box with \( P \). Inside it, @prp-double-negation (a) suggests building \( \neg\neg P \), which clashes with the premise:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg\neg\neg P}
  \open
  \hypo {2} {P}
  \open
  \hypo {3} {\neg P}
  \have {4} {\bot} \ne{2,3}
  \close
  \have {5} {\neg\neg P} \ni{3-4}
  \have {6} {\bot} \ne{5,1}
  \close
  \have {7} {\neg P} \ni{2-6}
\end{nd}$
\end{center}
```

Both boxes are closed by \( \rulename{\neg I} \), so no RAA is used. (Lines 3–5 could be replaced by the one line \( \neg\neg P \), "\( \rulename{\neg\neg I} \) 2".)

(b) The goal \( P \) is a bare letter and both premises want \( \neg P \), so we open an RAA box with \( \neg P \):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P \to Q}
  \hypo {2} {\neg P \to \neg Q}
  \open
  \hypo {3} {\neg P}
  \have {4} {Q} \ie{1,3}
  \have {5} {\neg Q} \ie{2,3}
  \have {6} {\bot} \ne{4,5}
  \close
  \have {7} {P} \raa{3-6}
\end{nd}$
\end{center}
```

In words: "Suppose, for a contradiction, that \( P \) fails. Then the premises give both \( Q \) and \( \neg Q \), which is impossible. Hence \( P \)."
:::

::: {#exr-reductio-and-classical-rules-b2}
[B2: Back from negated sides]

Derive \( \neg P \leftrightarrow \neg Q \vdash P \leftrightarrow Q \). Say where RAA enters and why.
:::

::: {.solution}
The goal is a biconditional, so by @def-rules-biconditional we need two boxes, one from \( P \) to \( Q \) and one from \( Q \) to \( P \). In the first, the goal \( Q \) is a bare letter and the premise speaks about \( \neg Q \), so we assume \( \neg Q \) and argue by RAA; the second is symmetric.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P \leftrightarrow \neg Q}
  \open
  \hypo {2} {P}
  \open
  \hypo {3} {\neg Q}
  \have {4} {\neg P} \bie{1,3}
  \have {5} {\bot} \ne{2,4}
  \close
  \have {6} {Q} \raa{3-5}
  \close
  \open
  \hypo {7} {Q}
  \open
  \hypo {8} {\neg P}
  \have {9} {\neg Q} \bie{1,8}
  \have {10} {\bot} \ne{7,9}
  \close
  \have {11} {P} \raa{8-10}
  \close
  \have {12} {P \leftrightarrow Q} \bi{2-6,7-11}
\end{nd}$
\end{center}
```

RAA enters at lines 6 and 11: each inner goal is a bare letter, and the premise produces only negations. In the converse, \( P \leftrightarrow Q \vdash \neg P \leftrightarrow \neg Q \) (@exm-iff-negations), the inner goals are negations, \( \rulename{\neg I} \) builds them, and no RAA is used.
:::

::: {#exr-reductio-and-classical-rules-b3}
[B3: The redundant rule]

Show that \( \rulename{\bot E} \) is derivable from RAA and repetition: given a line \( \bot \), derive an arbitrary statement \( P \) in one box, without \( \rulename{\bot E} \).
:::

::: {.solution}
Open an RAA box with \( \neg P \) and repeat the \( \bot \) inside it:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\bot}
  \open
  \hypo {2} {\neg P}
  \have {3} {\bot} \r{1}
  \close
  \have {4} {P} \raa{2-3}
\end{nd}$
\end{center}
```

The repetition at line 3 is needed because RAA asks for \( \bot \) as a line of the box itself. So every use of \( \rulename{\bot E} \) can be replaced by these three lines; the book keeps the rule for the reason given in the remark after @thm-classical-rules-interderivable.
:::

::: {#exr-reductio-and-classical-rules-b4}
[B4: Part ② on an example]

Here is a proof by RAA about a real number \( x \).

> Suppose \( x^2 \le x \). Suppose, for a contradiction, that \( x \le 1 \) fails, that is, \( x > 1 \). Then \( x > 0 \), and multiplying \( x > 1 \) by \( x \) gives \( x^2 > x \), which contradicts \( x^2 \le x \). Hence \( x \le 1 \).

Let \( P \) be the statement "\( x \le 1 \)".

::: {.enumerate options="label=(\alph*)"}
1. Which lines of the argument form the RAA box, and what are its assumption and its last line?
2. Apply part ② of the proof of @thm-classical-rules-interderivable to this use of RAA. Write the statement that the new line \( k \) asserts, in symbols and in words.
3. Which rule justifies the new line \( k \), and which rule the line after it?
4. Which lines of the original argument are unchanged by the replacement?
:::
:::

::: {.solution}
(a) The box opens with "\( x \le 1 \) fails", that is \( \neg P \), and runs through the sentence ending "which contradicts \( x^2 \le x \)"; its last line is \( \bot \), the clash between \( x^2 > x \) and the hypothesis \( x^2 \le x \). The last sentence, "Hence \( x \le 1 \)", is the RAA step.

(b) The new line \( k \) is \( \neg\neg P \), that is \( \neg\neg(x \le 1) \): "it is not the case that \( x \le 1 \) fails". The line after it is \( P \), "\( x \le 1 \)".

(c) Line \( k \) is \( \rulename{\neg I} \), closing the box that opened with \( \neg P \); the next line is \( \rulename{\neg\neg E} \), citing line \( k \).

(d) Every line of the box is unchanged: the assumption \( x > 1 \), the steps \( x > 0 \) and \( x^2 > x \), and the clash. Only the closing step becomes two lines. For real numbers "not not \( x \le 1 \)" and "\( x \le 1 \)" mean the same, but for the rules they are different statements, joined by \( \rulename{\neg\neg E} \).
:::

### C. Going deeper

::: {#exr-reductio-and-classical-rules-c1}
[C1: Excluded middle does the work of RAA directly]

Suppose that, instead of RAA, we had LEM as a rule: \( P \vee \neg P \) may be written on any line, for any statement \( P \).

::: {.enumerate options="label=(\alph*)"}
1. Given a box that opens with \( \neg P \) and reaches \( \bot \), derive \( P \) using LEM, \( \rulename{\vee E} \), \( \rulename{\bot E} \) and the other primitive rules, but neither RAA nor \( \neg\neg \)E. Write the case \( \neg P \) as the given box, extended.
2. Which two parts of the proof of @thm-classical-rules-interderivable does your fragment shortcut, and which line of their composite does it save?
:::
:::

::: {.solution}
(a) Write excluded middle for \( P \) just before the given box, and use the box as the second case of \( \rulename{\vee E} \), extended by one line:

```{=latex}
% schema (a schema: placeholder line numbers set with fitch.sty's numbering options)
\begin{center}
$\begin{nd}
  \have[h][0] {h} {P \vee \neg P} \lem{}
  \open
  \hypo {h1} {P}
  \close
  \open
  \hypo[i][0] {i} {\neg P}
  \have[\ ][0] {} {\vdots}
  \have[j][0] {j} {\bot}
  \have {j1} {P} \be{j}
  \close
  \have[k][0] {k} {P} \oe{h,h1-h1,i-j1}
\end{nd}$
\end{center}
```

Here \( h + 1 = i - 1 \). The first case is a one-line box that already ends with the goal. The second case is the given box with one more line, \( \rulename{\bot E} \) on its \( \bot \); its lines are unchanged and cite what they cited before, since the box has not moved into or out of any other box. No RAA and no \( \neg\neg \)E is used.

(b) It shortcuts ② followed by ③. Part ② closes the box by \( \rulename{\neg I} \), giving \( \neg\neg P \), then applies \( \neg\neg \)E; part ③ replaces that \( \neg\neg \)E by a split on \( P \vee \neg P \) whose \( \neg P \) case clashes with the line \( \neg\neg P \). The fragment in (a) uses the given box itself as the \( \neg P \) case, so it never writes \( \neg\neg P \): it saves that line and the separate \( \neg P \) box of ③.
:::

::: {#exr-reductio-and-classical-rules-c2}
[C2: Find the error]

A student derives \( \neg(\neg P \wedge \neg Q) \vdash P \vee Q \) as follows.

```{=latex}
% expect-invalid (a deliberately flawed derivation: find the error)
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (\neg P \wedge \neg Q)}
  \have {2} {P \vee \neg P} \lem{}
  \open
  \hypo {3} {P}
  \have {4} {P \vee Q} \oi{3}
  \close
  \open
  \hypo {5} {\neg P}
  \have {6} {\bot} \ne{3,5}
  \have {7} {Q} \be{6}
  \have {8} {P \vee Q} \oi{7}
  \close
  \have {9} {P \vee Q} \oe{2,3-4,5-8}
\end{nd}$
\end{center}
```

::: {.enumerate options="label=(\alph*)"}
1. Is the sequent \( \neg(\neg P \wedge \neg Q) \vdash P \vee Q \) derivable?
2. Does the student's derivation derive it? Name the first line that fails and the rule or clause it breaks.
3. Show that the illegal step, if it were allowed, would prove too much: use the same move to "derive" \( P \vee Q \vdash P \), and say why that sequent must not be derivable.
4. Give a correct derivation.
:::
:::

::: {.solution}
(a) Yes: (d) gives a derivation. The conclusion is true, and the argument is still wrong.

(b) No. Line 6 fails: it cites line 3, the assumption of the first case box, lines 3–4, which closed before line 5. By the scope rule of @def-derivation, line 3 is not available at line 6. The form of \( \rulename{\neg E} \) is right; what is broken is availability. In words, the student used the assumption of one case inside the other case, where it has not been assumed.

(c) The same move derives \( P \vee Q \vdash P \): split on the premise by \( \rulename{\vee E} \), with a first box that opens with \( P \) and ends there, and a second box that opens with \( Q \) and "repeats" \( P \) from the first. That sequent must not be derivable: with \( P \) false and \( Q \) true the premise is true and the conclusion false, and Chapter 2 proves that no derivation leads from true premises to a false conclusion. So citing a line of a sibling box is illegal in general, not just unlucky here.

(d) Keep lines 1–5, and in the case \( \neg P \) argue for \( Q \) by RAA, using the premise:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (\neg P \wedge \neg Q)}
  \have {2} {P \vee \neg P} \lem{}
  \open
  \hypo {3} {P}
  \have {4} {P \vee Q} \oi{3}
  \close
  \open
  \hypo {5} {\neg P}
  \open
  \hypo {6} {\neg Q}
  \have {7} {\neg P \wedge \neg Q} \ai{5,6}
  \have {8} {\bot} \ne{7,1}
  \close
  \have {9} {Q} \raa{6-8}
  \have {10} {P \vee Q} \oi{9}
  \close
  \have {11} {P \vee Q} \oe{2,3-4,5-10}
\end{nd}$
\end{center}
```

Line 7 cites line 5, the assumption of the enclosing case box, which is still open: the legal version of what the student wanted.
:::

<!-- dependency ledger
exm-raa-zero (example): x >= 0 and x != 0 give x > 0; subtracting x/2 and multiplying by 2 preserve <= | school algebra, an allowed prerequisite of ch01 (blueprint); ch10 derives it from axioms (prose pointer only)
exm-raa-zero (example): the hypothesis "x <= eps for every eps > 0" applies to eps = x/2 | informal reading of "every"; the rule is ch03's, flagged in prose; the example illustrates the shape of RAA and nothing cites it
def-rule-raa (claim): no derivation of P from not-not-P uses only the rules of s01-s05 | forward pointer to ch02 (thm-raa-independent, optional there), flagged in prose; the motivation for RAA, nothing proved from it
exm-raa-zero (example): for real numbers x > 0 says the same as "not x <= 0" (used to read the clash as not-E) | school algebra (trichotomy), allowed prerequisite
prp-double-negation (proof): (a) is exm-double-negation-introduction (s04) | cited with @ref and repeated in full here
prp-de-morgan (idea): no derivation reaches not-P from not(P and Q) alone, because a row makes the premise true and not-P false | forward pointer to ch02 (thm-soundness), flagged in the text as proved there; motivation only, the proof does not use it
prp-de-morgan (claim): no derivation of (d) avoids RAA | stated without proof and marked so; nothing depends on it
thm-classical-rules-interderivable (proof): replacing a line by a fragment keeps every citation available and the premises and last line unchanged | inline (argued in the proof)
exr-reductio-and-classical-rules-a1 (solution): squares are non-negative; 3 < 7/2 < 4 | school algebra
exr-reductio-and-classical-rules-a1 (solution): the rules never lead from true premises to a false conclusion | forward pointer to ch02 (thm-soundness), flagged in the solution as proved there; blueprint-mandated comprehension part
exr-reductio-and-classical-rules-b4 (solution): x > 1 gives x > 0 and x^2 > x | school algebra
exr-reductio-and-classical-rules-c2 (solution): P or Q |- P is not derivable (the row P false, Q true) | forward pointer to ch02 (thm-soundness, cor-refuting-row), flagged in the solution; the find-the-error verdict does not depend on it
-->
