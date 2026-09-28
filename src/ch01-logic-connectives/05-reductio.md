# Proof by Contradiction Is a Different Rule

Every rule so far either builds a statement up or takes one apart. The negation rules of @def-rules-negation do this too: \( \rulename{\neg I} \) builds \( \neg P \) from a box that starts with \( P \) and ends in \( \bot \), and \( \rulename{\neg E} \) uses \( \neg P \) only to clash with \( P \). None of them turns a refutation of \( \neg P \) into \( P \) itself. This section adds the one rule that does, **reductio ad absurdum** (RAA). It then shows that this rule proves more than the others, and finishes with advice on when a proof by contradiction should be rewritten as something else.

## Two boxes that look alike

Here are two arguments that a mathematician would both call "proof by contradiction".

The first is the proof of @thm-sqrt2-irrational. It assumes that \( \sqrt{2} \) is rational, reaches a contradiction, and concludes that \( \sqrt{2} \) is **not** rational. In the language of @def-rules-negation, it opens a box with the assumption \( P \) ("\( \sqrt 2 \) is rational"), reaches \( \bot \) inside it, and closes it to get \( \neg P \). That is \( \rulename{\neg I} \).

The second is an argument of the following kind, common in analysis.

::: {#exm-raa-zero}
[A number smaller than every positive number]

Let \( x \) be a real number with \( x \ge 0 \), and suppose that \( x \le \varepsilon \) for **every** real \( \varepsilon > 0 \). Prove that \( x = 0 \).
:::

::: {.solution}
Suppose, for a contradiction, that \( x \ne 0 \). Since \( x \ge 0 \) and \( x \ne 0 \), we have \( x > 0 \). Then \( \varepsilon \coloneqq x/2 \) is a real number with \( \varepsilon > 0 \), so the hypothesis applies to it and gives \( x \le x/2 \). Subtracting \( x/2 \) from both sides gives \( x/2 \le 0 \), so \( x \le 0 \). This contradicts \( x > 0 \). Hence \( x = 0 \).
:::

(The step "the hypothesis applies to it" uses a rule for "every", which Chapter 2 makes precise. Everything else is the rules of this chapter plus school algebra.)

Look at the shape. The box opens with the assumption \( \neg P \), where \( P \) is "\( x = 0 \)", reaches \( \bot \), and closes to give \( P \). If we tried to justify the last line with \( \rulename{\neg I} \), we would get \( \neg\neg P \) ("it is not the case that \( x \ne 0 \)"), not \( P \). The two arguments put their negation in different places. \( \rulename{\neg I} \) puts a \( \neg \) **into** the conclusion; this second argument takes one **out**.

Can the rules we have take it out? Let us try to derive \( P \) from \( \neg\neg P \), the smallest case of the problem. The premise \( \neg\neg P \) can be used only through \( \rulename{\neg E} \), and \( \rulename{\neg E} \) needs \( \neg P \) beside it, which we do not have; if we assume \( \neg P \) in a box, the box reaches \( \bot \), and \( \rulename{\neg I} \) then gives \( \neg\neg P \) back again. The goal \( P \) is a bare letter, so no introduction rule applies to it. Every attempt goes round in a circle. In fact no derivation of \( P \) from \( \neg\neg P \) exists using only the rules of §01–§04. We do not prove this here: it needs a way of reading statements other than as true or false, and Chapter 2 returns to the question. What we can do is name the missing step and add it as a rule.

## The rule RAA

*To prove \( P \), it is enough to show that "not \( P \)" leads to a contradiction.*

::: {#def-rule-raa}
[Reductio ad absurdum]

**RAA.** If a box opens with the assumption \( \neg P \) and reaches \( \bot \), then after the box closes we may write \( P \). Schematically,

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {i} {\neg P}
  \have {} {\quad \vdots}
  \have {j} {\bot}
  \close
  \have {k} {P} \raa{i-j}
\end{nd}$
\end{center}
```

The assumption \( \neg P \) is **discharged** when the box closes: like every assumption, it may be cited only by lines inside its box.
:::

In words: the box is a thought experiment in which \( P \) fails. If that experiment ends in \( \bot \), then \( P \) cannot fail, and RAA lets us assert \( P \) itself, **not** merely \( \neg\neg P \).

Set it beside \( \rulename{\neg I} \) from @def-rules-negation:

| Rule | The box opens with | The box ends with | After the box |
|---|---|---|---|
| \( \rulename{\neg I} \) | \( P \) | \( \bot \) | \( \neg P \) |
| RAA | \( \neg P \) | \( \bot \) | \( P \) |

The two rows differ only in where the \( \neg \) sits, and that is the whole difference. \( \rulename{\neg I} \) **introduces** a negation, exactly as \( \rulename{\wedge I} \) introduces a conjunction. RAA **removes** one, and nothing else among the rules can.

Nothing needs checking for well-definedness here, but one point needs saying. \( P \) may itself be any statement, including a negation or a compound one. If \( P \) is \( \neg Q \), the box opens with \( \neg\neg Q \); if \( P \) is \( Q \vee R \), the box opens with \( \neg(Q \vee R) \). The rule reads the statement as a whole.

::: {.warning}
The assumption that opens an RAA box must be the **exact** negation of the goal. To prove \( x \le 1 \) by contradiction, assume \( x > 1 \), since for real numbers \( \neg(x \le 1) \) is \( x > 1 \). Assuming \( x \ge 1 \) instead is a common slip: it is not the negation, since \( x = 1 \) satisfies both \( x \le 1 \) and \( x \ge 1 \). If \( x = 1 \) is possible, no contradiction can be reached from \( x \ge 1 \) at all, and a "contradiction" that seems to be reached hides an error.
:::

**Examples.** The first is the degenerate one. RAA can prove \( P \) from \( P \):

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

It is legal and pointless: line 1 already is the goal. We keep it because it is the purest case of a pattern we will meet in real proofs, a contradiction box whose assumption does nothing except clash with a line we already had. The last part of this section is about recognizing that pattern.

The second example is @exm-raa-zero. Read with the rules, its last sentence is RAA: the box opened with "\( x \ne 0 \)", which is \( \neg(x = 0) \), and ended with the clash between \( x \le 0 \) and \( x > 0 \), which is \( \rulename{\neg E} \).

The third example is double negation, which is where we got stuck.

::: {#prp-double-negation}
[Double Negation]

For every statement \( P \):

::: {.enumerate options="label=(\alph*)"}
1. \( P \vdash \neg\neg P \), by a derivation that does not use RAA;
2. \( \neg\neg P \vdash P \), by a derivation that uses RAA.
:::
:::

::: {.proof}
(a) Here \( \neg\neg P \) is the negation of \( \neg P \), so \( \rulename{\neg I} \) asks for a box that opens with \( \neg P \) and reaches \( \bot \):

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

(b) The goal \( P \) has no connective to introduce, so we open an RAA box with \( \neg P \):

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

Line 3 applies \( \rulename{\neg E} \) to the statement \( \neg P \) (line 2) and its negation \( \neg\neg P \) (line 1). This proves both parts.
:::

Compare the two derivations line by line. They are identical except for the last line, and the box in (a) is the very box that RAA would read in (b). What differs is the rule that closes it. So the two directions of double negation are not mirror images: one needs only the rules for \( \neg \), the other needs the new rule.

**Non-example by minimal change.** Take the derivation in (a) and change only the last line from \( \neg\neg P \) to \( P \), keeping the justification "\( \rulename{\neg I} \) 2–3". Every other line still checks. The failing clause is the conclusion of \( \rulename{\neg I} \): a box opening with \( \neg P \) gives, under \( \rulename{\neg I} \), the negation of its assumption, which is \( \neg\neg P \). To write \( P \) there, the justification must be RAA.

::: {.check}
A box opens with the assumption \( \neg(x < 0) \) and reaches \( \bot \). Which of the following may be written after it closes, and by which rule? (i) \( x < 0 \); (ii) \( \neg\neg(x < 0) \); (iii) \( x \ge 0 \).
:::

::: {.solution}
(i) By RAA: the box opened with the negation of \( x < 0 \). (ii) By \( \rulename{\neg I} \): the box opened with \( \neg(x < 0) \), and \( \rulename{\neg I} \) writes the negation of the assumption. (iii) Neither. The box shows that \( \neg(x < 0) \) is impossible, so \( x \ge 0 \), which for real numbers says the same thing as \( \neg(x < 0) \), is the one statement the box has refuted.
:::

**Why add the rule at all?** Without it, the rules of §01–§04 form a coherent and useful system in their own right, and some mathematicians work only in it. But ordinary mathematics uses RAA constantly, usually without noticing, and a number of familiar laws cannot be derived without it. The rest of this section shows the most important ones. The end of Chapter 2 tells the story of the mathematicians who refused the rule and what their mathematics looks like.

## What only RAA gives

We now derive three laws that everyday mathematics takes for granted. Each derivation uses RAA, and we will point to the exact line where it enters.

### The converse of the contrapositive

In §03 we derived @prp-contrapositive: from \( P \to Q \) we get \( \neg Q \to \neg P \), using \( \rulename{{\to}I} \) and \( \rulename{\neg I} \) only. In practice we use it the other way round. To prove "if \( n^2 \) is even then \( n \) is even", one proves "if \( n \) is not even then \( n^2 \) is not even" and declares the job done. That step goes from \( \neg Q \to \neg P \) back to \( P \to Q \).

::: {#prp-contrapositive-converse}
[Converse of the Contrapositive]

For all statements \( P \) and \( Q \), \( \neg Q \to \neg P \vdash P \to Q \).
:::

::: {.idea}
The goal is an implication, so the outer box opens with \( P \) and must reach \( Q \). Inside it, \( Q \) is a bare letter, so no introduction rule helps; but the premise speaks about \( \neg Q \), which suggests assuming \( \neg Q \) and using \( \rulename{{\to}E} \). That gives \( \neg P \), which clashes with the \( P \) of the outer box. The inner box opened with \( \neg Q \), so closing it gives \( Q \) by RAA.
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

Line 5 is available because line 2 belongs to an enclosing box that is still open. RAA enters at line 6. This proves the proposition.
:::

So the two directions of contraposition are like the two directions of double negation. Going from \( P \to Q \) to \( \neg Q \to \neg P \) is free; coming back costs one RAA. When \( Q \) is itself a negation, say \( Q = \neg R \), RAA can be avoided: the inner box may open with \( R \) and close by \( \rulename{\neg I} \), since \( R \vdash \neg\neg R \) by @prp-double-negation (a) feeds the premise \( \neg\neg R \to \neg P \).

### Excluded middle

Every integer is even or odd. Every real number is \( \ge 0 \) or \( < 0 \). Every statement is true or false. The purely logical version of these facts is the law \( P \vee \neg P \), which holds for every statement \( P \) with no premises at all.

::: {#prp-excluded-middle}
[Excluded Middle]

For every statement \( P \), \( \vdash P \vee \neg P \).
:::

::: {.idea}
The goal is a disjunction, so the natural move is \( \rulename{\vee I} \), which asks us to prove \( P \) or to prove \( \neg P \). With no premises we can do neither, so we argue by RAA on the whole disjunction: assume \( \neg(P \vee \neg P) \) and look for a clash. The assumption says that neither disjunct holds. If \( P \) held, then \( P \vee \neg P \) would hold; that clash gives \( \neg P \) by \( \rulename{\neg I} \). But then \( P \vee \neg P \) holds after all, by \( \rulename{\vee I} \), and that is the final clash.

*Before reading on: which line of the derivation is the only one that cannot be justified by the rules of §01–§04?*
:::

::: {.proof}
The derivation is:

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {\neg(P \vee \neg P)}
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

The same derivation, stopped at line 7 and closed with \( \rulename{\neg I} \) instead of RAA, proves \( \vdash \neg\neg(P \vee \neg P) \) without RAA. So even without the new rule, excluded middle cannot be **refuted**; what RAA adds is the right to assert it. Chapter 2 ends with what that difference means.

Excluded middle turns into a proof technique through \( \rulename{\vee E} \): to prove \( R \), prove it assuming \( P \), prove it again assuming \( \neg P \), and combine the two boxes with the line \( P \vee \neg P \). We use it that way in the next proof. The line \( P \vee \neg P \) is written with @prp-excluded-middle as its justification. That is a shorthand: pasting the eight lines above in its place gives a derivation that uses only the rules themselves.

### De Morgan's laws

The negation of an "and" is an "or" of negations, and the negation of an "or" is an "and" of negations. For example, a real number \( x \) fails to lie in the interval \( [0, 1] \), that is, \( \neg(0 \le x \wedge x \le 1) \), exactly when \( x < 0 \) or \( x > 1 \). Each law has two directions, so there are four derivations to give, and only one of them needs RAA.

::: {#prp-de-morgan}
[De Morgan's Laws]

For all statements \( P \) and \( Q \):

::: {.enumerate options="label=(\alph*)"}
1. \( \neg(P \vee Q) \vdash \neg P \wedge \neg Q \);
2. \( \neg P \wedge \neg Q \vdash \neg(P \vee Q) \);
3. \( \neg P \vee \neg Q \vdash \neg(P \wedge Q) \);
4. \( \neg(P \wedge Q) \vdash \neg P \vee \neg Q \).
:::

The derivations of (a), (b) and (c) below use no RAA; the derivation of (d) uses it, through @prp-excluded-middle.
:::

::: {.idea}
Read each goal's main connective. In (a) it is \( \wedge \), so we prove \( \neg P \) and \( \neg Q \) separately, each by \( \rulename{\neg I} \). In (b) and (c) it is \( \neg \), so one \( \rulename{\neg I} \) box does the work, and inside it the disjunction is used by \( \rulename{\vee E} \). In (d) it is \( \vee \), and here the direct routes fail: we cannot prove \( \neg P \) outright, nor \( \neg Q \). What we can do is split on whether \( P \) holds. If it does, then \( Q \) cannot, since \( P \wedge Q \) is ruled out; if it does not, \( \neg P \) is already the left disjunct.
:::

::: {.proof}
(a) Two \( \rulename{\neg I} \) boxes, one for each conjunct, then \( \rulename{\wedge I} \):

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

(b) One \( \rulename{\neg I} \) box that opens with \( P \vee Q \); inside it, \( \rulename{\vee E} \) splits into the two cases, and each case clashes with one half of the premise:

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
  \have {10} {\neg(P \vee Q)} \ni{4-9}
\end{nd}$
\end{center}
```

The two inner boxes sit side by side at the same depth; the underlined assumption at line 7 is where the second one begins.

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
  \have {10} {\neg(P \wedge Q)} \ni{2-9}
\end{nd}$
\end{center}
```

(d) Excluded middle for \( P \), then two cases:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg(P \wedge Q)}
  \have {2} {P \vee \neg P} \by{excluded middle}{}
  \open
  \hypo {3} {P}
  \open
  \hypo {4} {Q}
  \have {5} {P \wedge Q} \ai{3,4}
  \have {6} {\bot} \ne{5,1}
  \close
  \have {7} {\neg Q} \ni{4-6}
  \have {8} {\neg P \vee \neg Q} \oi{7}
  \close
  \open
  \hypo {9} {\neg P}
  \have {10} {\neg P \vee \neg Q} \oi{9}
  \close
  \have {11} {\neg P \vee \neg Q} \oe{2,3-8,9-10}
\end{nd}$
\end{center}
```

Line 2 is @prp-excluded-middle, and the only use of RAA is inside it. This proves all four laws.
:::

Where does the difference come from? Laws (a), (b) and (c) conclude a negation or a conjunction of negations, and \( \rulename{\neg I} \) builds negations. Law (d) concludes a **disjunction**, and to prove a disjunction by \( \rulename{\vee I} \) we must know **which** side holds. The premise \( \neg(P \wedge Q) \) says only that the two do not both hold; it does not say which one fails. Excluded middle supplies the missing decision.

::: {.remark}
In the Lean proof assistant the two negation rules are different commands for exactly this reason. Faced with a goal \( \neg P \), the command `intro h` assumes \( P \) and leaves the goal `False`, which is \( \rulename{\neg I} \); faced with any goal \( P \), the command `by_contra h` assumes \( \neg P \) and leaves `False`, which is RAA.
:::

## When a contradiction is not needed

RAA is a legitimate rule, and some proofs cannot do without it. But many proofs that are written as "suppose, for a contradiction, …" do not use the contradiction for anything. They are direct proofs or contrapositive proofs in costume, and they read better with the costume taken off. Here are the two costumes, each with a test you can run on a finished proof.

**Costume 1: a direct proof in disguise.** The first costume is the degenerate derivation from earlier in this section, dressed up.

::: {#exm-costume-direct}
[A direct proof in costume]

Here is a proof that \( x + 1/x \ge 2 \) for every real \( x > 0 \). Decide what it really uses, and rewrite it.

> Let \( x > 0 \). Suppose, for a contradiction, that \( x + 1/x < 2 \). Since \( (x - 1)^2 \ge 0 \), expanding gives \( x^2 - 2x + 1 \ge 0 \), that is, \( x^2 + 1 \ge 2x \). Dividing by \( x > 0 \) gives \( x + 1/x \ge 2 \). This contradicts our assumption. Hence \( x + 1/x \ge 2 \).
:::

::: {.solution}
The assumption "\( x + 1/x < 2 \)" is cited exactly once, in the sentence "This contradicts our assumption". The three sentences before it prove \( x + 1/x \ge 2 \) outright, from \( x > 0 \) alone. As a derivation, the RAA box contains a complete derivation of the goal, and the box's assumption is used only to clash with the goal at the last line. Deleting the box leaves a direct proof:

> Let \( x > 0 \). Since \( (x - 1)^2 \ge 0 \), expanding gives \( x^2 + 1 \ge 2x \). Dividing by \( x \), which is positive, gives \( x + 1/x \ge 2 \).

Nothing is lost, and the reader no longer has to hold a false assumption in mind for three sentences.
:::

*The test:* if the assumption of the contradiction box is cited only in the line that produces \( \bot \), the box proved the goal without it. Delete the box.

**Costume 2: a contrapositive in disguise.** The second costume is subtler, because the assumption of the box is used heavily. What is used only once is the **hypothesis** of the theorem.

::: {#exm-costume-contrapositive}
[A contrapositive in costume]

Here is a proof that, for an integer \( n \), if \( n^2 \) is even then \( n \) is even. Decide what it really uses, and rewrite it.

> Suppose \( n^2 \) is even. Suppose, for a contradiction, that \( n \) is not even. Then \( n \) is odd, say \( n = 2k + 1 \) with \( k \) an integer. Then \( n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1 \) is odd, so \( n^2 \) is not even. This contradicts the fact that \( n^2 \) is even. Hence \( n \) is even.
:::

::: {.solution}
The hypothesis "\( n^2 \) is even" is cited once, in the sentence "This contradicts …". Everything between the two "Suppose"s and that sentence is a proof, from "\( n \) is not even" alone, that \( n^2 \) is not even. So the real content is the implication \( \neg Q \to \neg P \), with \( P \) = "\( n^2 \) is even" and \( Q \) = "\( n \) is even", and the contradiction frame is @prp-contrapositive-converse done inline, which is exactly the derivation in its proof. Written openly:

> We prove the contrapositive: if \( n \) is not even, then \( n^2 \) is not even. Suppose \( n \) is not even. Then \( n \) is odd, say \( n = 2k + 1 \). Then \( n^2 = 2(2k^2 + 2k) + 1 \) is odd, and so it is not even.

The rewrite tells the reader at the start what is going to be shown, and the final clash disappears. (The proof of @thm-square-even-implies-even in §03 is organized differently, by cases on "\( n \) is even or odd", and that route needs no RAA at all.)
:::

*The test:* if everything inside the box follows from its assumption \( \neg Q \) alone, and the hypothesis \( P \) of the theorem enters only in the line that produces \( \bot \), then the box proved \( \neg Q \to \neg P \). Present it as a contrapositive.

The two tests share one smell: *the contradiction reached is with a statement we already had, or would have had without the box.* A genuine proof by contradiction uses the assumed negation throughout and only then finds a clash in some unexpected place; @exm-raa-zero, where the assumption \( x \ne 0 \) was used to produce the witness \( \varepsilon = x/2 \), is of that kind.

::: {.warning}
Not every "proof by contradiction" in a book is a use of RAA. When the statement being proved is itself a negation (irrational, "there is no largest integer", \( x \ne 5 \)), assuming the positive version and reaching a contradiction is \( \rulename{\neg I} \), and such a proof never needed RAA. The proof of @thm-sqrt2-irrational is the standard case: "irrational" means "not rational".
:::

## Exercises

### A. Check your understanding

::: {#exr-reductio-a1}
[A1]

For each argument, say whether its last step is \( \rulename{\neg I} \), RAA, or neither, and say what the box opened with.

::: {.enumerate options="label=(\alph*)"}
1. "Suppose 7 is even. Then \( 7 = 2k \) for some integer \( k \), so \( k = 3.5 \), which is not an integer. This is impossible. Hence 7 is not even."
2. "Suppose \( x^2 \le 2x - 1 \) fails, that is, \( x^2 > 2x - 1 \). Then … contradiction. Hence \( x^2 \le 2x - 1 \)."
3. "Suppose there is a largest integer \( N \). Then \( N + 1 \) is an integer larger than \( N \), a contradiction. So there is no largest integer."
4. "Assume \( P \). Then, as shown above, \( Q \). Hence \( P \to Q \)."
5. State RAA and \( \rulename{\neg I} \) side by side, and say which of the two is used in @prp-double-negation (a).
:::
:::

::: {.solution}
(a) \( \rulename{\neg I} \). The box opened with "7 is even" and the conclusion is its negation. (Here \( 7 = 2k \) forces \( k = 7/2 \), and \( 7/2 \) is not an integer because \( 3 < 7/2 < 4 \).)

(b) RAA. The box opened with the negation of \( x^2 \le 2x - 1 \), and the conclusion is \( x^2 \le 2x - 1 \) itself.

(c) \( \rulename{\neg I} \). The box opened with "there is a largest integer", and the conclusion is its negation. (The step from \( N \) to \( N + 1 \) also uses a quantifier rule, from Chapter 2.)

(d) Neither: this is \( \rulename{{\to}I} \). The box opened with \( P \), ended with \( Q \), and no \( \bot \) appears.

(e) \( \rulename{\neg I} \): a box that opens with \( P \) and reaches \( \bot \) gives \( \neg P \). RAA: a box that opens with \( \neg P \) and reaches \( \bot \) gives \( P \). The derivation of @prp-double-negation (a) uses \( \rulename{\neg I} \), with \( \neg P \) in the role of the assumption, so its conclusion is \( \neg\neg P \).
:::

### B. Practice

::: {#exr-reductio-b1}
[B1: Two short derivations]

::: {.enumerate options="label=(\alph*)"}
1. Derive \( \neg\neg\neg P \vdash \neg P \) without using RAA.
2. Derive \( \neg P \to P \vdash P \), using RAA.
3. For each derivation, write the same argument as two or three sentences of prose.
:::

*Hint: in (a), the goal is a negation. In (b), the goal is a bare letter.*
:::

::: {.solution}
(a) The goal \( \neg P \) is a negation, so we open a \( \rulename{\neg I} \) box with \( P \). Inside it, @prp-double-negation (a) suggests building \( \neg\neg P \), which then clashes with the premise:

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

Both boxes are closed by \( \rulename{\neg I} \), so no RAA is used.

(b) The goal \( P \) is a bare letter, so we open an RAA box with \( \neg P \):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P \to P}
  \open
  \hypo {2} {\neg P}
  \have {3} {P} \ie{1,2}
  \have {4} {\bot} \ne{3,2}
  \close
  \have {5} {P} \raa{2-4}
\end{nd}$
\end{center}
```

(c) For (a): "Suppose \( P \). Then \( \neg P \) is impossible, so \( \neg\neg P \) holds. This contradicts the premise \( \neg\neg\neg P \). Hence \( \neg P \)." For (b): "Suppose, for a contradiction, that \( P \) fails. Then the premise gives \( P \), which contradicts our supposition. Hence \( P \)."
:::

::: {#exr-reductio-b2}
[B2: Take off the costume]

Here is a proof that \( \frac{a + b}{2} \ge \sqrt{ab} \) for all real \( a > 0 \) and \( b > 0 \).

> Let \( a, b > 0 \). Suppose, for a contradiction, that \( \frac{a+b}{2} < \sqrt{ab} \). Since \( (\sqrt a - \sqrt b)^2 \ge 0 \), expanding gives \( a - 2\sqrt{ab} + b \ge 0 \), so \( \frac{a+b}{2} \ge \sqrt{ab} \). This contradicts our assumption. Hence \( \frac{a+b}{2} \ge \sqrt{ab} \).

::: {.enumerate options="label=(\alph*)"}
1. Which costume from this section is this? Justify your answer by saying where the assumption of the box is cited.
2. Rewrite the proof without the contradiction.
:::
:::

::: {.solution}
(a) Costume 1, a direct proof in disguise. The assumption \( \frac{a+b}{2} < \sqrt{ab} \) is cited only in "This contradicts our assumption", the line that produces \( \bot \). The two sentences before it prove the goal from \( a, b > 0 \) alone.

(b) Let \( a, b > 0 \), so that \( \sqrt a \) and \( \sqrt b \) are defined and \( \sqrt a \sqrt b = \sqrt{ab} \). Since \( (\sqrt a - \sqrt b)^2 \ge 0 \), expanding gives \( a - 2\sqrt{ab} + b \ge 0 \). Adding \( 2\sqrt{ab} \) to both sides and dividing by \( 2 \) gives \( \frac{a+b}{2} \ge \sqrt{ab} \), as claimed.
:::

### C. Going deeper

::: {#exr-reductio-c1}
[C1: Euclid without the contradiction]

Here is a common proof that there are infinitely many primes. It uses two facts about integers that we take as known here: every integer \( m \ge 2 \) has a prime divisor (Chapter 4 proves it by induction), and a prime divides no number that leaves remainder 1 on division by it.

> Suppose, for a contradiction, that there are only finitely many primes, say \( p_1, \dots, p_k \). Let \( N \coloneqq p_1 p_2 \cdots p_k + 1 \). Then \( N \ge 2 \), so \( N \) has a prime divisor \( p \). Since \( p_1, \dots, p_k \) are all the primes, \( p = p_i \) for some \( i \). But \( N \) leaves remainder 1 on division by \( p_i \), so \( p_i \) does not divide \( N \). This is a contradiction. Hence there are infinitely many primes.

::: {.enumerate options="label=(\alph*)"}
1. The statement "there are infinitely many primes" means "the set of primes is **not** finite". Is the last step of the proof RAA or \( \rulename{\neg I} \)?
2. Where is the assumption "\( p_1, \dots, p_k \) are all the primes" used? Which smell from this section does that suggest?
3. Rewrite the argument as a direct proof of the following statement: *for every finite list \( p_1, \dots, p_k \) of primes, there is a prime not in the list.*
4. Say what the rewrite gains over the original.
:::
:::

::: {.solution}
(a) \( \rulename{\neg I} \). The box opens with "the set of primes is finite", the positive statement, and the conclusion is its negation. No RAA is used.

(b) The assumption is used once, in "\( p = p_i \) for some \( i \)", which is where the clash is manufactured. Everything else (\( N \ge 2 \), the prime divisor \( p \), and the fact that no \( p_i \) divides \( N \)) holds for **any** finite list of primes, whether or not it is complete. This is the smell of Costume 1: the box's assumption does no work except to produce the contradiction.

(c) Let \( p_1, \dots, p_k \) be any finite list of primes, and let \( N \coloneqq p_1 p_2 \cdots p_k + 1 \). Each \( p_i \ge 2 \), so \( N \ge 2 \), and hence \( N \) has a prime divisor \( p \). For each \( i \), the number \( N \) leaves remainder 1 on division by \( p_i \), so \( p_i \) does not divide \( N \). Since \( p \) does divide \( N \), \( p \ne p_i \) for every \( i \). Hence \( p \) is a prime not in the list.

(d) The rewrite proves a stronger and more useful statement: given any finite list of primes, it **produces** a prime outside it, namely any prime divisor of \( N \). The original only shows that a finite list of all the primes is impossible. The rewrite also never asks the reader to reason inside a false assumption. That the primes are not finitely many follows at once: a finite set of primes, listed in any order, would miss a prime by (c).
:::

::: {#exr-reductio-c2}
[C2: Excluded middle does the work of RAA]

Suppose that, instead of adding RAA as a rule, we had added excluded middle, \( P \vee \neg P \), as a line that may be written at any point for any statement \( P \).

::: {.enumerate options="label=(\alph*)"}
1. Show that RAA would then be unnecessary: given a box that opens with \( \neg P \) and reaches \( \bot \), derive \( P \) using excluded middle, \( \rulename{\vee E} \), \( \rulename{\bot E} \) and the other rules of §01–§04, but not RAA.
2. Deduce that "RAA" and "excluded middle" are interchangeable as additions to the rules of §01–§04: each can be derived from the other.
:::

*Hint: split on \( P \vee \neg P \). One case is immediate; in the other, the box you were given can be reused.*
:::

::: {.solution}
(a) Suppose the derivation contains a box, lines \( i \) to \( j \), that opens with \( \neg P \) and ends with \( \bot \). Instead of closing it with RAA, we write excluded middle and use the box as the second case of \( \rulename{\vee E} \). Schematically, with the given box moved inside:

```{=latex}
\begin{center}
$\begin{nd}
  \have {1} {P \vee \neg P} \by{excluded middle}{}
  \open
  \hypo {2} {P}
  \close
  \open
  \hypo {3} {\neg P}
  \have {} {\quad \vdots} \by{the given box}{}
  \have {4} {\bot}
  \have {5} {P} \be{4}
  \close
  \have {6} {P} \oe{1,2-2,3-5}
\end{nd}$
\end{center}
```

The first case is a one-line box: it opens with \( P \) and already ends with the goal \( P \). The second case is the given box, extended by one line of \( \rulename{\bot E} \). Every line of the given box is still justified, because it sits in the same position relative to its own assumption. No RAA is used.

(b) Part (a) shows that, with excluded middle available, every use of RAA can be replaced. Conversely, @prp-excluded-middle derives \( P \vee \neg P \) using RAA. So adding either one to the rules of §01–§04 lets us derive the other, and the two additions prove exactly the same things. Chapter 2 adds double-negation elimination to this list.
:::
