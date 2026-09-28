# How to Find a Derivation

We now have every rule for the connectives. Checking a derivation is mechanical, as @def-derivation makes it: for each line, which rule, which lines, and are they available. Finding one is not, since an assumption may be any statement at all. This section gives a method for finding derivations, the one a mathematician uses at the top of a blank page: write what you have, write what you want, and look at the main connectives. It runs the method on four searches that succeed, one that fails and one mathematical goal, and ends with every rule in one place.

## Partial derivations

A search builds a derivation from the outside in, so we need a name for what exists halfway. A **partial derivation** is a derivation with **gaps**: some stretches of lines are still missing, and each is marked \( \vdots \). The line just below a gap is its **current goal**, and the lines available at the current goal (in the sense of @def-derivation) are its **resources**. A search starts with a single gap, below the premises and above the conclusion, and each step replaces a gap by lines, boxes and smaller gaps.

In the snapshots below, a line carries the number it will have in the finished derivation, so that snapshots can be compared; lines whose place is not yet fixed carry no number. On paper you would number the lines at the end.

## The method

*Work from both ends: let the goal choose the boxes, let the premises choose the eliminations, and meet in the middle.*

::: {.algorithm}
**Searching for a derivation of \( \Gamma \vdash G \).**

1. **Set up.** Write the premises \( \Gamma \) at the top and \( G \) at the bottom, with a gap between.
2. **Goal-directed step.** Take the main connective of the current goal (@def-main-connective) and set up its introduction rule:
   - \( A \to B \): a box opened with \( A \); inside it, the new goal is \( B \).
   - \( A \wedge B \): two gaps, with goals \( A \) and \( B \).
   - \( A \leftrightarrow B \): two boxes, one from \( A \) to \( B \) and one from \( B \) to \( A \).
   - \( \neg A \): a box opened with \( A \); inside it, the new goal is \( \bot \).
   - \( A \vee B \): **postpone**. Do not choose a side yet.

   Repeat while the current goal is a \( \to \), \( \wedge \), \( \leftrightarrow \) or \( \neg \).
3. **Premise-directed step.** Take the main connective of a resource and apply its elimination rule: \( \rulename{\wedge E} \) freely; \( \rulename{{\to}E} \) and \( \rulename{{\leftrightarrow}E} \) when the other statement they need is a resource, or can be made a new goal; \( \rulename{\vee E} \) by opening two boxes, one per disjunct, **each ending in the current goal**; \( \rulename{\bot E} \) when \( \bot \) is a resource.
4. **Goal \( \bot \).** Look for a pair \( S \), \( \neg S \) among the resources, or make \( S \) the new goal for some resource \( \neg S \).
5. **Stuck.** Use \( \rulename{RAA} \): open a box with the negation of the current goal, whose new goal is \( \bot \). Or use \( \rulename{LEM} \) on a well-chosen statement \( S \), and split on \( S \vee \neg S \) by \( \rulename{\vee E} \). Then return to step 3.

When no gap is left, number the lines and check the derivation as @def-derivation says.
:::

The steps are listed in the order in which to try them, and the order has reasons.

**The goal-directed steps lose nothing.** Suppose the goal \( A \to B \) is derivable from the resources \( \Gamma \) at all, by some derivation \( D \). Then \( B \) is derivable from \( \Gamma \) together with \( A \): add \( A \) to the premises of \( D \) (@def-derivable only asks that the premises belong to the list), and append the line \( B \) by \( \rulename{{\to}E} \), citing the last line of \( D \) and the premise \( A \). So opening a box on \( A \) never turns a derivable gap into an underivable one. With \( \rulename{\wedge E} \), \( \rulename{\neg E} \) or \( \rulename{{\leftrightarrow}E} \) as the appended line, the same argument covers \( \wedge \), \( \neg \) and \( \leftrightarrow \). That is why step 2 may be applied without thinking.

**Choosing a side of \( \vee \) can lose everything.** A disjunction can be derivable when neither side is. From \( P \vee Q \) the goal \( Q \vee P \) is derivable (the section on disjunction derives it), but \( P \vee Q \) does not say which side holds, so a last line \( \rulename{\vee I} \) from \( Q \), or from \( P \), leaves a gap that cannot be filled (Chapter 2 makes "cannot" exact). Choosing a side is safe only once the resources decide it, typically inside a case of \( \rulename{\vee E} \).

**\( \rulename{RAA} \) also loses nothing, and still comes last.** If \( G \) is derivable from the resources, then \( \bot \) is derivable from them together with \( \neg G \), by one \( \rulename{\neg E} \), so an \( \rulename{RAA} \) box is always safe. It comes last because its goal \( \bot \) gives step 2 nothing to work with, and because a derivation that did not need the box reads worse with it (the last warning of the previous section).

::: {.check}
For each goal, with no premises, name the first rule the method aims for and the box or gaps it sets up.

::: {.enumerate options="label=(\alph*)"}
1. \( \neg(P \wedge \neg P) \)
2. \( (P \vee Q) \to (Q \vee P) \)
3. \( (P \to Q) \wedge (Q \to (P \to Q)) \)
4. \( P \vee \neg(P \wedge Q) \)
:::
:::

::: {.solution}
(a) \( \rulename{\neg I} \): a box opened with \( P \wedge \neg P \), goal \( \bot \). (b) \( \rulename{{\to}I} \): a box opened with \( P \vee Q \), goal \( Q \vee P \); that goal is a disjunction, so it is postponed, and step 3 uses the new resource \( P \vee Q \) by \( \rulename{\vee E} \). (c) \( \rulename{\wedge I} \): two gaps, with goals \( P \to Q \) and \( Q \to (P \to Q) \), each then a box. (d) Step 2 postpones the disjunction, and with no premises step 3 has nothing to use, so the search is at step 5 at once. \( \rulename{LEM} \) on \( P \) works: in the case \( P \), \( \rulename{\vee I} \) gives the left side; in the case \( \neg P \), a \( \rulename{\neg I} \) box on \( P \wedge Q \) gives \( \neg(P \wedge Q) \), and \( \rulename{\vee I} \) gives the right side.
:::

## Splitting the goal

We now run the method on four sequents. The first search uses only steps 2, 3 and 4. It is the full version of the chapter's main move, which comes back twice in the exercises with parts left blank.

::: {#exm-search-distribute}
[Splitting the goal, then using the premise]

Find a derivation of \( P \to \neg Q \vdash \neg(P \wedge Q) \wedge (Q \to \neg P) \).
:::

::: {.solution}
*Goal-directed.* The goal's main connective is \( \wedge \), so step 2 splits it into two gaps, with goals \( \neg(P \wedge Q) \) and \( Q \to \neg P \), joined at the end by \( \rulename{\wedge I} \):

```{=latex}
% schema (a partial derivation: gaps are unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {P \to \neg Q}
  \have[\ ][0] {} {\vdots}
  \have[][7] {7} {\neg (P \wedge Q)}
  \have[\ ][0] {} {\vdots}
  \have[][13] {13} {Q \to \neg P}
  \have {14} {\neg (P \wedge Q) \wedge (Q \to \neg P)} \ai{7,13}
\end{nd}$
\end{center}
```

Both new goals have a connective, so step 2 applies again. The goal \( \neg(P \wedge Q) \) asks for a \( \rulename{\neg I} \) box opened with \( P \wedge Q \) and ending in \( \bot \). The goal \( Q \to \neg P \) asks for a \( \rulename{{\to}I} \) box opened with \( Q \); inside it the goal \( \neg P \) asks for a \( \rulename{\neg I} \) box opened with \( P \). Every gap now has the goal \( \bot \):

```{=latex}
% schema (a partial derivation: gaps are unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {P \to \neg Q}
  \open
  \hypo {2} {P \wedge Q}
  \have[\ ][0] {} {\vdots}
  \have[][6] {6} {\bot}
  \close
  \have {7} {\neg (P \wedge Q)} \ni{2-6}
  \open
  \hypo {8} {Q}
  \open
  \hypo {9} {P}
  \have[\ ][0] {} {\vdots}
  \have[][11] {11} {\bot}
  \close
  \have {12} {\neg P} \ni{9-11}
  \close
  \have {13} {Q \to \neg P} \ii{8-12}
  \have {14} {\neg (P \wedge Q) \wedge (Q \to \neg P)} \ai{7,13}
\end{nd}$
\end{center}
```

*Premise-directed.* In the first gap the resources are lines 1 and 2. Step 3 splits line 2 into \( P \) and \( Q \) by \( \rulename{\wedge E} \); then \( P \) is the antecedent of line 1, so \( \rulename{{\to}E} \) gives \( \neg Q \); and step 4 finds the pair \( Q \), \( \neg Q \). In the second gap the resources are lines 1, 8 and 9: \( \rulename{{\to}E} \) on lines 1 and 9 gives \( \neg Q \), which clashes with line 8. Both gaps close:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to \neg Q}
  \open
  \hypo {2} {P \wedge Q}
  \have {3} {P} \ae{2}
  \have {4} {Q} \ae{2}
  \have {5} {\neg Q} \ie{1,3}
  \have {6} {\bot} \ne{4,5}
  \close
  \have {7} {\neg (P \wedge Q)} \ni{2-6}
  \open
  \hypo {8} {Q}
  \open
  \hypo {9} {P}
  \have {10} {\neg Q} \ie{1,9}
  \have {11} {\bot} \ne{8,10}
  \close
  \have {12} {\neg P} \ni{9-11}
  \close
  \have {13} {Q \to \neg P} \ii{8-12}
  \have {14} {\neg (P \wedge Q) \wedge (Q \to \neg P)} \ai{7,13}
\end{nd}$
\end{center}
```

*What the method did.* The goal-directed steps wrote nine of the fourteen lines, every box among them, before the premise was used; the premise-directed steps wrote four, lines 3, 4, 5 and 10. The premise itself was used once in each gap, by the same \( \rulename{{\to}E} \). Line 10 cites line 1 from inside two boxes, which is legal because line 1 is a premise and so is available everywhere below it.
:::

## Cases must end in the goal

When the goal gives nothing, the premises must. The next search is driven by a disjunction among the premises.

::: {#exm-search-cases}
[Proof by cases, found by the method]

Find a derivation of \( P \vee Q, \ P \to R, \ Q \to R \vdash R \).
:::

::: {.solution}
The goal \( R \) is a letter, so step 2 has nothing to do. Step 3 looks at the resources. \( \rulename{{\to}E} \) on \( P \to R \) needs \( P \), and making \( P \) a new goal is hopeless: from \( P \vee Q \) we know that one of \( P \), \( Q \) holds, not which. The disjunction itself is the resource to use, by \( \rulename{\vee E} \), with two boxes that each end in the current goal \( R \):

```{=latex}
% schema (a partial derivation: gaps are unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee Q}
  \hypo {2} {P \to R}
  \hypo {3} {Q \to R}
  \open
  \hypo {4} {P}
  \have[\ ][0] {} {\vdots}
  \have[][5] {5} {R}
  \close
  \open
  \hypo {6} {Q}
  \have[\ ][0] {} {\vdots}
  \have[][7] {7} {R}
  \close
  \have {8} {R} \oe{1,4-5,6-7}
\end{nd}$
\end{center}
```

Inside the first box, \( P \) is a resource, so \( \rulename{{\to}E} \) on line 2 closes the gap at once; the second box is the same with line 3:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee Q}
  \hypo {2} {P \to R}
  \hypo {3} {Q \to R}
  \open
  \hypo {4} {P}
  \have {5} {R} \ie{2,4}
  \close
  \open
  \hypo {6} {Q}
  \have {7} {R} \ie{3,6}
  \close
  \have {8} {R} \oe{1,4-5,6-7}
\end{nd}$
\end{center}
```

*Why the boxes end in the current goal.* \( \rulename{\vee E} \) (@def-rules-disjunction) gives, after the two boxes, their common last line and nothing else. A box that ends in anything but the current goal leaves that goal still to be reached, and two boxes that end in different statements cannot be combined at all. The word **current** matters: had the goal been \( S \to R \), step 2 would first open a box on \( S \), the current goal inside it would be \( R \), and the two case boxes, opened inside the box of \( S \), would end in \( R \), not in \( S \to R \).
:::

## Postponing a disjunction

The third search has a disjunction as its goal, and it shows why step 2 postpones it.

::: {#exm-search-postpone-or}
[Choosing a side too early]

Find a derivation of \( P \to (Q \vee R) \vdash (P \to Q) \vee (P \to R) \).
:::

::: {.solution}
*The tempting start.* The goal is a disjunction, and it is tempting to choose a side at once, say \( P \to Q \), and finish with \( \rulename{\vee I} \). The new goal is an implication, so we open a box on \( P \); then \( \rulename{{\to}E} \) gives \( Q \vee R \), and \( \rulename{\vee E} \) splits into the cases \( Q \) and \( R \), each to end in the current goal \( Q \). The first case ends at once. The second is a dead end:

```{=latex}
% schema (a partial derivation with a gap that cannot be filled)
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \vee R)}
  \open
  \hypo {2} {P}
  \have {3} {Q \vee R} \ie{1,2}
  \open
  \hypo {4} {Q}
  \close
  \open
  \hypo {5} {R}
  \have[\ ][0] {} {\vdots}
  \have[\ ][0] {} {Q}
  \close
  \have[\ ][0] {} {Q} \oe{}
  \close
  \have[\ ][0] {} {P \to Q} \ii{}
  \have[\ ][0] {} {(P \to Q) \vee (P \to R)} \oi{}
\end{nd}$
\end{center}
```

In the case \( R \) the resources are \( P \to (Q \vee R) \), \( P \), \( Q \vee R \) and \( R \), and none of them says anything that yields \( Q \). Choosing the right side instead fails in the mirror image, in the case \( Q \). In fact neither side follows from the premise alone: with \( P \) and \( Q \) true and \( R \) false the premise is true and \( P \to R \) is false, and with \( P \) and \( R \) true and \( Q \) false the premise is true and \( P \to Q \) is false. (Chapter 2 turns such rows into proofs that no derivation exists.)

*The diagnosis.* Each case of the dead end knew which side it wanted: the case \( Q \) wanted \( P \to Q \), and the case \( R \) wanted \( P \to R \). But those cases were opened inside the box of \( P \), too late to choose the side of a disjunction that stands outside it. The side must be decided **before** any box is opened, and the premise does not decide it: that is step 5. The dead end also names the statement to split on. If \( Q \) holds, the left side is easy; if \( Q \) fails, then from \( P \) the premise gives \( Q \vee R \) with its left side excluded. So we use \( \rulename{LEM} \) on \( Q \):

```{=latex}
% schema (a partial derivation: gaps are unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \vee R)}
  \have {2} {Q \vee \neg Q} \lem{}
  \open
  \hypo {3} {Q}
  \have[\ ][0] {} {\vdots}
  \have[][7] {7} {(P \to Q) \vee (P \to R)}
  \close
  \open
  \hypo {8} {\neg Q}
  \have[\ ][0] {} {\vdots}
  \have[][13] {13} {(P \to Q) \vee (P \to R)}
  \close
  \have {14} {(P \to Q) \vee (P \to R)} \oe{2,3-7,8-13}
\end{nd}$
\end{center}
```

Now each case decides the side. In the case \( Q \), the goal is \( P \to Q \): a box on \( P \) whose last line repeats \( Q \). In the case \( \neg Q \), the goal is \( P \to R \): a box on \( P \), then \( Q \vee R \) by \( \rulename{{\to}E} \), then \( R \) by @prp-disjunctive-syllogism used as a derived rule (\( \rulename{DS} \)), citing \( Q \vee R \) and \( \neg Q \). Then \( \rulename{\vee I} \), on the correct side each time:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \vee R)}
  \have {2} {Q \vee \neg Q} \lem{}
  \open
  \hypo {3} {Q}
  \open
  \hypo {4} {P}
  \have {5} {Q} \r{3}
  \close
  \have {6} {P \to Q} \ii{4-5}
  \have {7} {(P \to Q) \vee (P \to R)} \oi{6}
  \close
  \open
  \hypo {8} {\neg Q}
  \open
  \hypo {9} {P}
  \have {10} {Q \vee R} \ie{1,9}
  \have {11} {R} \ds{10,8}
  \close
  \have {12} {P \to R} \ii{9-11}
  \have {13} {(P \to Q) \vee (P \to R)} \oi{12}
  \close
  \have {14} {(P \to Q) \vee (P \to R)} \oe{2,3-7,8-13}
\end{nd}$
\end{center}
```

\( \rulename{LEM} \) on \( P \), the first split one thinks of, also succeeds, but less well: in the case \( P \) the premise gives \( Q \vee R \), and a second \( \rulename{\vee E} \), with two more implication boxes, is needed inside it.
:::

::: {.warning}
**Do not choose a disjunct early.** A goal \( A \vee B \) tempts us to pick a side and prove it, and the choice usually fails, as the first attempt above did: neither \( P \to Q \) nor \( P \to R \) follows from the premise. Postpone the \( \vee \) goal, use the resources first, and choose a side only inside a case that decides it.
:::

## A law with no negation that needs \( \rulename{RAA} \)

The fourth search needs step 5 on a statement that contains no \( \neg \) at all.

::: {#prp-peirce}
[Peirce's Law]

For all statements \( P \) and \( Q \), \( \vdash ((P \to Q) \to P) \to P \).
:::

*Try it first (ten minutes): run the method on this goal until it stalls. At which gap does it stall, and which step of the method is left?*

::: {.idea}
Step 2 opens a box on \( (P \to Q) \to P \) with the goal \( P \), a letter. Step 3 can use the new resource if we produce its antecedent, so \( P \to Q \) becomes a new goal, and step 2 opens a box on \( P \) with the goal \( Q \). There the search stalls: nothing among \( (P \to Q) \to P \) and \( P \) produces \( Q \). Step 5 remains. \( \rulename{RAA} \) on the goal \( P \) of the outer box adds the resource \( \neg P \), and that is exactly what the stalled gap lacked: inside the box on \( P \), the pair \( P \), \( \neg P \) gives \( \bot \), and \( \rulename{\bot E} \) gives \( Q \). Then \( P \to Q \), then \( P \) by \( \rulename{{\to}E} \), which clashes with \( \neg P \).
:::

::: {.proof}
The derivation is:

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {(P \to Q) \to P}
  \open
  \hypo {2} {\neg P}
  \open
  \hypo {3} {P}
  \have {4} {\bot} \ne{3,2}
  \have {5} {Q} \be{4}
  \close
  \have {6} {P \to Q} \ii{3-5}
  \have {7} {P} \ie{1,6}
  \have {8} {\bot} \ne{7,2}
  \close
  \have {9} {P} \raa{2-8}
  \close
  \have {10} {((P \to Q) \to P) \to P} \ii{1-9}
\end{nd}$
\end{center}
```

The derivation has no premises, and \( \rulename{RAA} \) enters at line 9. This proves the proposition.
:::

The assumption \( \neg P \) of line 2 is used twice: at line 4 it makes the inner box contradictory, and at line 8 it clashes with the \( P \) that line 7 obtained. Peirce's law contains no \( \neg \), yet its derivation uses \( \rulename{RAA} \): the classical rule is about more than negation. (That every derivation of it must use \( \rulename{RAA} \) or one of its equivalents from @thm-classical-rules-interderivable is true; we do not prove it.)

## A search that fails

The method is not a machine that always succeeds. Here it fails, and the failure is instructive.

Try \( P \to Q \vdash Q \to P \). Step 2 opens a box on \( Q \) with the goal \( P \):

```{=latex}
% schema (a partial derivation that the method cannot complete)
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \open
  \hypo {2} {Q}
  \have[\ ][0] {} {\vdots}
  \have[\ ][0] {} {P}
  \close
  \have[\ ][0] {} {Q \to P} \ii{}
\end{nd}$
\end{center}
```

The goal \( P \) is a letter. Step 3: \( \rulename{{\to}E} \) on line 1 needs \( P \), the goal itself. Step 5, \( \rulename{RAA} \): assume \( \neg P \); the only negation among the resources is \( \neg P \), and step 4 would need \( P \) against it, the goal again. \( \rulename{LEM} \) on \( P \): the case \( \neg P \) needs \( P \) again. \( \rulename{LEM} \) on \( Q \): the case \( \neg Q \) clashes with line 2, and the case \( Q \) is where we started. Every route returns to one gap, "\( P \) from \( P \to Q \) and \( Q \)", which is the converse error of Argument B in the chapter's opening section.

But notice what we have **not** shown. A search that fails proves nothing about derivations in general: an assumption may be any statement at all, by (D2) of @def-derivation, so there are infinitely many derivations to consider, and a cleverer one might exist. To show that **no** derivation of \( Q \to P \) from \( P \to Q \) exists we need a different tool.

That is the question this chapter leaves open. *We show that something is derivable by exhibiting a derivation; how could we ever show that something is not?* Chapter 2 answers it. It gives each statement a truth value and proves that the rules never lead from true premises to a false conclusion; the assignment with \( P \) false and \( Q \) true, which makes \( P \to Q \) true and \( Q \to P \) false, then settles this search for good.

## A mathematical goal

The method reads the frame of a proof off the goal whether the statements are letters or facts about numbers. In ordinary mathematics its payoff is that the first and last sentences of a proof, and its division into parts, are fixed before any mathematics is done.

::: {#exm-skeleton-odd-product}
[Building a skeleton]

Let \( m \) and \( n \) be integers. Prove that if \( mn \) is odd, then \( m \) is odd and \( n \) is odd.
:::

::: {.solution}
*The skeleton.* The main connective is "if … then", so step 2 opens a \( \rulename{{\to}I} \) box: "Assume \( mn \) is odd. … Hence \( m \) is odd and \( n \) is odd." The new goal is a conjunction, so step 2 again: two separate proofs, one that \( m \) is odd and one that \( n \) is odd. Each is atomic, and the one resource, "\( mn \) is odd", cannot be taken apart. So we bring in facts we can compute with: "if \( m \) is even then \( mn \) is even" is one, and @prp-contrapositive turns it into "if \( mn \) is not even then \( m \) is not even", which the resource can feed.

*The proof.* Assume \( mn \) is odd. We show that \( m \) is odd and that \( n \) is odd.

First, if \( m \) is even, say \( m = 2k \) with \( k \) an integer, then \( mn = 2(kn) \) is even. By the contrapositive (@prp-contrapositive), if \( mn \) is not even, then \( m \) is not even. Now \( mn \) is odd, so it is not even, since no integer is both; hence \( m \) is not even. Since every integer is even or odd, \( m \) is odd, by @prp-disjunctive-syllogism.

Exchanging the roles of \( m \) and \( n \) in the previous paragraph shows that \( n \) is odd. Hence \( m \) and \( n \) are both odd.

*What the method did.* It fixed the first sentence, the two paragraphs and the last sentence; the only computation is \( mn = 2(kn) \). No step uses \( \rulename{RAA} \): the classical-looking move from "\( m \) is not even" to "\( m \) is odd" is disjunctive syllogism on the fact that every integer is even or odd. (The phrase "say \( m = 2k \)" names a witness, which is a rule for "there exists" from Chapter 3.)
:::

::: {.warning}
**Do not assume what you want to prove.** To derive a goal \( G \), it is tempting to open a box with \( G \). The box reaches \( G \) at once, but after it closes it gives \( G \to G \), not \( G \), and its assumption is gone. An assumption is useful when the goal asks for it: the antecedent of an implication (step 2), the negated goal of \( \rulename{RAA} \) (step 5), a disjunct of a resource (step 3). Opening the box on the conclusion of an implication is the converse error of the chapter's opening argument.
:::

## The rules in one place

This is the reference sheet for the chapter. Letters in the number column stand for line numbers. Each box rule needs the box's last line as a line of that box itself, not inside a further box, and every cited line must be available (@def-derivation).

**Conjunction and implication** (@def-rules-conjunction, @def-rules-implication).

```{=latex}
% schema (rule schemata: placeholder line numbers set with fitch.sty's numbering options)
\begin{center}
% schema
$\begin{nd}
  \have[i][0] {i} {P}
  \have[j][0] {j} {Q}
  \have[k][0] {k} {P \wedge Q} \ai{i,j}
\end{nd}$
\qquad
% schema
$\begin{nd}
  \have[i][0] {i} {P \wedge Q}
  \have[k][0] {k} {P} \ae{i}
  \have[l][0] {l} {Q} \ae{i}
\end{nd}$
\\[3ex]
% schema
$\begin{nd}
  \open
  \hypo[i][0] {i} {P}
  \have[\ ][0] {} {\vdots}
  \have[j][0] {j} {Q}
  \close
  \have[k][0] {k} {P \to Q} \ii{i-j}
\end{nd}$
\qquad
% schema
$\begin{nd}
  \have[i][0] {i} {P \to Q}
  \have[j][0] {j} {P}
  \have[k][0] {k} {Q} \ie{i,j}
\end{nd}$
\end{center}
```

**Disjunction** (@def-rules-disjunction). The two boxes of \( \rulename{\vee E} \) end in the same statement \( R \).

```{=latex}
% schema (rule schemata: placeholder line numbers set with fitch.sty's numbering options)
\begin{center}
% schema
$\begin{nd}
  \have[i][0] {i} {P}
  \have[k][0] {k} {P \vee Q} \oi{i}
  \have[l][0] {l} {Q \vee P} \oi{i}
\end{nd}$
\qquad
% schema
$\begin{nd}
  \have[h][0] {h} {P \vee Q}
  \open
  \hypo[i][0] {i} {P}
  \have[\ ][0] {} {\vdots}
  \have[j][0] {j} {R}
  \close
  \open
  \hypo[k][0] {k} {Q}
  \have[\ ][0] {} {\vdots}
  \have[l][0] {l} {R}
  \close
  \have[m][0] {m} {R} \oe{h,i-j,k-l}
\end{nd}$
\end{center}
```

**Negation and contradiction** (@def-rules-negation), **and \( \rulename{RAA} \)** (@def-rule-raa). \( \rulename{\bot E} \) may write **any** statement \( Q \).

```{=latex}
% schema (rule schemata: placeholder line numbers set with fitch.sty's numbering options)
\begin{center}
% schema
$\begin{nd}
  \open
  \hypo[i][0] {i} {P}
  \have[\ ][0] {} {\vdots}
  \have[j][0] {j} {\bot}
  \close
  \have[k][0] {k} {\neg P} \ni{i-j}
\end{nd}$
\qquad
% schema
$\begin{nd}
  \have[i][0] {i} {P}
  \have[j][0] {j} {\neg P}
  \have[k][0] {k} {\bot} \ne{i,j}
\end{nd}$
\qquad
% schema
$\begin{nd}
  \have[i][0] {i} {\bot}
  \have[k][0] {k} {Q} \be{i}
\end{nd}$
\\[3ex]
% schema
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

**Biconditional** (@def-rules-biconditional), **and repetition**, clause (D3) of @def-derivation.

```{=latex}
% schema (rule schemata: placeholder line numbers set with fitch.sty's numbering options)
\begin{center}
% schema
$\begin{nd}
  \open
  \hypo[i][0] {i} {P}
  \have[\ ][0] {} {\vdots}
  \have[j][0] {j} {Q}
  \close
  \open
  \hypo[k][0] {k} {Q}
  \have[\ ][0] {} {\vdots}
  \have[l][0] {l} {P}
  \close
  \have[m][0] {m} {P \leftrightarrow Q} \bi{i-j,k-l}
\end{nd}$
\\[3ex]
% schema
$\begin{nd}
  \have[i][0] {i} {P \leftrightarrow Q}
  \have[j][0] {j} {P}
  \have[k][0] {k} {Q} \bie{i,j}
\end{nd}$
\qquad
% schema
$\begin{nd}
  \have[i][0] {i} {P}
  \have[\ ][0] {} {\vdots}
  \have[k][0] {k} {P} \r{i}
\end{nd}$
\end{center}
```

\( \rulename{{\leftrightarrow}E} \) works in both directions: from \( P \leftrightarrow Q \) and \( Q \) it gives \( P \).

**Derived rules.** Each is a proved sequent, used as one line that cites the lines holding its premises (@def-derived-rule). Where a rule has no short name, the justification names the result.

| In a justification | Sequent | Proved in | Its derivation uses \( \rulename{RAA} \) |
|---|---|---|---|
| (and commutes) | \( P \wedge Q \vdash Q \wedge P \) | @prp-and-commutes | no |
| (implication is transitive) | \( P \to Q, \ Q \to R \vdash P \to R \) | @prp-implication-transitive | no |
| (curry) | \( (P \wedge Q) \to R \dashv\vdash P \to (Q \to R) \) | @prp-curry | no |
| (or commutes) | \( P \vee Q \vdash Q \vee P \) | @exm-disjunction-first-derivations | no |
| (distributivity) | \( P \wedge (Q \vee R) \dashv\vdash (P \wedge Q) \vee (P \wedge R) \) | @prp-distributivity | no |
| (cases on a hypothesis) | \( (P \to R) \wedge (Q \to R) \dashv\vdash (P \vee Q) \to R \) | @exm-cases-on-hypothesis | no |
| \( \rulename{\neg\neg I} \) | \( P \vdash \neg\neg P \) | @prp-double-negation (a) | no |
| \( \rulename{\neg\neg E} \) | \( \neg\neg P \vdash P \) | @prp-double-negation (b) | yes |
| \( \rulename{MT} \) | \( P \to Q, \ \neg Q \vdash \neg P \) | @prp-modus-tollens | no |
| \( \rulename{CP} \) | \( P \to Q \vdash \neg Q \to \neg P \) | @prp-contrapositive | no |
| (converse of \( \rulename{CP} \)) | \( \neg Q \to \neg P \vdash P \to Q \) | @prp-contrapositive-converse | yes |
| \( \rulename{DS} \) | \( P \vee Q, \ \neg P \vdash Q \) | @prp-disjunctive-syllogism | no |
| (\( \rulename{DS} \), other disjunct) | \( P \vee Q, \ \neg Q \vdash P \) | @exr-negation-and-contradiction-b1 (a) | no |
| (ex falso) | \( P, \ \neg P \vdash Q \) | @prp-ex-falso | no |
| (vacuous implication) | \( \neg P \vdash P \to Q \) | @prp-vacuous-implication | no |
| (iff as two implications) | \( P \leftrightarrow Q \dashv\vdash (P \to Q) \wedge (Q \to P) \) | @prp-iff-two-implications | no |
| (iff of negations) | \( P \leftrightarrow Q \vdash \neg P \leftrightarrow \neg Q \) and its converse | @exm-iff-negations; the converse @exr-reductio-and-classical-rules-b2 | the converse only |
| (equivalence cycle) | \( P \to Q, \ Q \to R, \ R \to P \vdash P \leftrightarrow Q \) | @prp-equivalence-cycle | no |
| \( \rulename{LEM} \) | \( \vdash P \vee \neg P \) | @prp-excluded-middle | yes |
| \( \rulename{DM} \) | the four laws of @prp-de-morgan | @prp-de-morgan | (d) only |
| (implication as disjunction) | \( \neg P \vee Q \vdash P \to Q \) and its converse | @prp-implication-as-disjunction | the converse only, through \( \rulename{LEM} \) |
| (Peirce) | \( \vdash ((P \to Q) \to P) \to P \) | @prp-peirce | yes |

::: {.warning}
**Cite only what is already proved.** A derived rule is an abbreviation for its derivation, so it may be used only after that derivation exists, and never inside it. For example, the second route to @prp-de-morgan (d) splits on excluded middle; a proof of excluded middle that used De Morgan's law (d) along that route would be circular. In this book the check is simple: cite only labels that appear earlier.
:::

## Exercises

### A. Check your understanding

::: {#exr-finding-derivations-a1}
[A1]

For (a)–(d), name the goal's main connective, the first rule the method aims for, and the first sentence of a proof. For (e)–(f), name the elimination rule the premise invites, and what it needs.

::: {.enumerate options="label=(\alph*)"}
1. For real \( x \): if \( x^3 < 0 \) then \( x < 0 \).
2. There is no integer \( n \) with \( 2n = 7 \).
3. For real \( x \) and \( y \): \( \abs{xy} = \abs{x}\abs{y} \) and \( \abs{x + y} \le \abs{x} + \abs{y} \).
4. For an integer \( n \): \( n \) is odd if and only if \( n^2 \) is odd.
5. The premise \( (P \wedge Q) \to R \), with the goal \( R \) and the resources \( P \) and \( Q \).
6. The premise \( \neg(P \vee Q) \), with the goal \( \bot \) and the resource \( Q \).
:::
:::

::: {.solution}
(a) \( \to \); \( \rulename{{\to}I} \): "Assume \( x^3 < 0 \)." (Starting "Suppose \( x \ge 0 \)" inside that frame is an \( \rulename{RAA} \) box on the goal \( x < 0 \), not the contrapositive; a proof through the contrapositive replaces the frame, proving "if \( x \ge 0 \) then \( x^3 \ge 0 \)" and then applying \( \rulename{CP} \).)

(b) \( \neg \), since the claim is "not: there is an integer \( n \) with \( 2n = 7 \)"; \( \rulename{\neg I} \): "Suppose \( n \) is an integer with \( 2n = 7 \)." (Naming \( n \) uses a rule for "there exists", from Chapter 3.)

(c) \( \wedge \); \( \rulename{\wedge I} \): "We prove the two statements in turn."

(d) \( \leftrightarrow \); \( \rulename{{\leftrightarrow}I} \): "\( (\Rightarrow) \) Assume \( n \) is odd."

(e) \( \rulename{{\to}E} \), which needs the antecedent \( P \wedge Q \): make it a new goal, reached by \( \rulename{\wedge I} \) from \( P \) and \( Q \); then \( \rulename{{\to}E} \) gives \( R \).

(f) \( \rulename{\neg E} \), which needs \( P \vee Q \) beside \( \neg(P \vee Q) \): make \( P \vee Q \) the new goal (step 4), reached by \( \rulename{\vee I} \) from \( Q \).
:::

### B. Practice

::: {#exr-finding-derivations-b1}
[B1: Three searches]

For each sequent, name the first goal-directed step, then find a derivation.

::: {.enumerate options="label=(\alph*)"}
1. \( P \wedge (Q \to R) \vdash Q \to (P \wedge R) \).
2. \( \neg(P \to Q) \vdash P \wedge \neg Q \). Which conjunct needs \( \rulename{RAA} \)?
3. \( \neg P \to Q \vdash P \vee Q \).
:::

*Hint: in (c), use \( \rulename{LEM} \) on \( P \).*
:::

::: {.solution}
(a) The goal is an implication: a box on \( Q \) with the goal \( P \wedge R \), which splits into \( P \) and \( R \). Step 3 splits the premise, and \( \rulename{{\to}E} \) gives \( R \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge (Q \to R)}
  \open
  \hypo {2} {Q}
  \have {3} {P} \ae{1}
  \have {4} {Q \to R} \ae{1}
  \have {5} {R} \ie{4,2}
  \have {6} {P \wedge R} \ai{3,5}
  \close
  \have {7} {Q \to (P \wedge R)} \ii{2-6}
\end{nd}$
\end{center}
```

(b) The goal is a conjunction: two gaps, with goals \( P \) and \( \neg Q \). The premise can be used only by \( \rulename{\neg E} \), against \( P \to Q \), so in each gap we aim to produce \( P \to Q \). The goal \( \neg Q \) is a negation: a box on \( Q \), where \( P \to Q \) follows by a box that repeats \( Q \), and it clashes with the premise. The goal \( P \) is a letter, and the resources give nothing, so step 5: \( \rulename{RAA} \) on \( \neg P \). Then \( P \to Q \) follows, since from \( P \) and \( \neg P \) anything follows. **The conjunct \( P \) is where \( \rulename{RAA} \) enters**; \( \neg Q \) needs none. (That no derivation of \( P \) from the premise avoids \( \rulename{RAA} \) is true, but we do not prove it.)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \to Q)}
  \open
  \hypo {2} {\neg P}
  \open
  \hypo {3} {P}
  \have {4} {\bot} \ne{3,2}
  \have {5} {Q} \be{4}
  \close
  \have {6} {P \to Q} \ii{3-5}
  \have {7} {\bot} \ne{6,1}
  \close
  \have {8} {P} \raa{2-7}
  \open
  \hypo {9} {Q}
  \open
  \hypo {10} {P}
  \have {11} {Q} \r{9}
  \close
  \have {12} {P \to Q} \ii{10-11}
  \have {13} {\bot} \ne{12,1}
  \close
  \have {14} {\neg Q} \ni{9-13}
  \have {15} {P \wedge \neg Q} \ai{8,14}
\end{nd}$
\end{center}
```

Lines 3–6 are the derivation of @prp-vacuous-implication; citing it as a derived rule would shorten this to twelve lines.

(c) The goal is a disjunction, so step 2 postpones it; the premise needs \( \neg P \), which is not a resource. Step 5, \( \rulename{LEM} \) on \( P \): in the case \( P \), \( \rulename{\vee I} \) gives the left side; in the case \( \neg P \), the premise gives \( Q \) and \( \rulename{\vee I} \) the right side.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P \to Q}
  \have {2} {P \vee \neg P} \lem{}
  \open
  \hypo {3} {P}
  \have {4} {P \vee Q} \oi{3}
  \close
  \open
  \hypo {5} {\neg P}
  \have {6} {Q} \ie{1,5}
  \have {7} {P \vee Q} \oi{6}
  \close
  \have {8} {P \vee Q} \oe{2,3-4,5-7}
\end{nd}$
\end{center}
```
:::

::: {#exr-finding-derivations-b2}
[B2: The last step]

A search for \( P \to Q, \ R \to \neg Q \vdash P \to \neg R \) has reached the stage below; only the last line is missing. *Name the move, then complete it.*

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {R \to \neg Q}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \open
  \hypo {5} {R}
  \have {6} {\neg Q} \ie{2,5}
  \have {7} {\bot} \ne{4,6}
  \close
  \have {8} {\neg R} \ni{5-7}
  \close
  \have {9} {\;\textbf{?}} \by{?}{}
\end{nd}$
\end{center}
```
:::

::: {.solution}
The move is the chapter's main one: the skeleton was read off the goal, and the gap was filled from both ends. The goal \( P \to \neg R \) is an implication, so the outer box opened with \( P \) (line 3); its new goal \( \neg R \) is a negation, so the inner box opened with \( R \) (line 5). The premises then met the goal in the middle: \( \rulename{{\to}E} \) at lines 4 and 6 gave \( Q \) and \( \neg Q \), and the clash at line 7. The inner box was closed at line 8. What remains is to close the outer box on its goal, by \( \rulename{{\to}I}\ \lines{3}{8} \):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {R \to \neg Q}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \open
  \hypo {5} {R}
  \have {6} {\neg Q} \ie{2,5}
  \have {7} {\bot} \ne{4,6}
  \close
  \have {8} {\neg R} \ni{5-7}
  \close
  \have {9} {P \to \neg R} \ii{3-8}
\end{nd}$
\end{center}
```

The box runs from its assumption \( P \), line 3, to its last line \( \neg R \), line 8, which lies in the outer box itself and not in the inner one, as \( \rulename{{\to}I} \) requires.
:::

### C. Going deeper

::: {#exr-finding-derivations-c1}
[C1: The second half]

A search for \( P \vee (Q \wedge R) \vdash (P \vee Q) \wedge (P \vee R) \) has used the premise by \( \rulename{\vee E} \) and finished the first case; the second case is blank. *Name the move, then complete it.*

```{=latex}
% schema (a partial derivation: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee (Q \wedge R)}
  \open
  \hypo {2} {P}
  \have {3} {P \vee Q} \oi{2}
  \have {4} {P \vee R} \oi{2}
  \have {5} {(P \vee Q) \wedge (P \vee R)} \ai{3,4}
  \close
  \open
  \hypo {6} {Q \wedge R}
  \have[\ ][0] {} {\vdots}
  \have[][11] {11} {(P \vee Q) \wedge (P \vee R)}
  \close
  \have {12} {(P \vee Q) \wedge (P \vee R)} \oe{1,2-5,6-11}
\end{nd}$
\end{center}
```
:::

::: {.solution}
[Hint 1]

The current goal of the blank box is a conjunction. What does step 2 do with it, and what does step 3 do with the box's assumption?
:::

::: {.solution}
[Hint 2]

Line 7 is \( Q \), by \( \rulename{\wedge E} \) from line 6.
:::

::: {.solution}
The move is the chapter's main one again: read the skeleton off the goal, then work from both ends. The current goal \( (P \vee Q) \wedge (P \vee R) \) is a conjunction, so step 2 splits it into the goals \( P \vee Q \) and \( P \vee R \), to be joined by \( \rulename{\wedge I} \). Both are disjunctions, so they are postponed, and step 3 turns to the resource \( Q \wedge R \): \( \rulename{\wedge E} \) gives \( Q \) and \( R \). Now each disjunction has a side that is a resource, so \( \rulename{\vee I} \) is safe.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee (Q \wedge R)}
  \open
  \hypo {2} {P}
  \have {3} {P \vee Q} \oi{2}
  \have {4} {P \vee R} \oi{2}
  \have {5} {(P \vee Q) \wedge (P \vee R)} \ai{3,4}
  \close
  \open
  \hypo {6} {Q \wedge R}
  \have {7} {Q} \ae{6}
  \have {8} {R} \ae{6}
  \have {9} {P \vee Q} \oi{7}
  \have {10} {P \vee R} \oi{8}
  \have {11} {(P \vee Q) \wedge (P \vee R)} \ai{9,10}
  \close
  \have {12} {(P \vee Q) \wedge (P \vee R)} \oe{1,2-5,6-11}
\end{nd}$
\end{center}
```

Both boxes end in the current goal of the \( \rulename{\vee E} \), as that rule requires. Here \( \rulename{\vee I} \) adds \( P \) on the left of \( Q \) and of \( R \); in the first case it added \( Q \) and \( R \) on the right of \( P \). Citing line 2 inside the second box would be the scope error of the previous section's find-the-error item.
:::

::: {#exr-finding-derivations-c2}
[C2: A disjunction from nothing]

::: {.enumerate options="label=(\alph*)"}
1. Derive \( \vdash (P \to Q) \vee (Q \to P) \).
2. In a paragraph, say which step of your derivation uses \( \rulename{RAA} \) or \( \rulename{LEM} \), and why the method cannot avoid step 5 on this goal.
:::
:::

::: {.solution}
[Hint 1]

The goal is a disjunction and there are no premises. Which steps of the method does that leave?
:::

::: {.solution}
[Hint 2]

Begin with \( Q \vee \neg Q \), by \( \rulename{LEM} \).
:::

::: {.solution}
(a) \( \rulename{LEM} \) on \( Q \). In the case \( Q \), the implication \( P \to Q \) holds by a box that repeats \( Q \). In the case \( \neg Q \), the implication \( Q \to P \) holds by a box on \( Q \) that clashes with \( \neg Q \), followed by \( \rulename{\bot E} \).

```{=latex}
\begin{center}
$\begin{nd}
  \have {1} {Q \vee \neg Q} \lem{}
  \open
  \hypo {2} {Q}
  \open
  \hypo {3} {P}
  \have {4} {Q} \r{2}
  \close
  \have {5} {P \to Q} \ii{3-4}
  \have {6} {(P \to Q) \vee (Q \to P)} \oi{5}
  \close
  \open
  \hypo {7} {\neg Q}
  \open
  \hypo {8} {Q}
  \have {9} {\bot} \ne{8,7}
  \have {10} {P} \be{9}
  \close
  \have {11} {Q \to P} \ii{8-10}
  \have {12} {(P \to Q) \vee (Q \to P)} \oi{11}
  \close
  \have {13} {(P \to Q) \vee (Q \to P)} \oe{1,2-6,7-12}
\end{nd}$
\end{center}
```

\( \rulename{LEM} \) on \( P \) works equally well, with the roles of the two sides exchanged.

(b) \( \rulename{LEM} \) is used at line 1, and \( \rulename{RAA} \) only inside it. The method cannot avoid step 5 here. Step 2 postpones the \( \vee \) goal; with no premises, step 3 has nothing to eliminate and step 4 nothing to clash; and \( \rulename{\vee I} \) cannot come first, because neither side is derivable from no premises (with \( P \) true and \( Q \) false, \( P \to Q \) is false; with \( P \) false and \( Q \) true, \( Q \to P \) is false; Chapter 2 turns such rows into proofs). So a resource must be created from nothing, and only step 5 does that. This shows that the **method** needs step 5; that every derivation of the sequent uses \( \rulename{RAA} \) or an equivalent is a stronger claim, which we do not prove.

**Marking scheme.** (10 points)
- 3: a correct split by \( \rulename{LEM} \) (on \( Q \) or on \( P \)), with two case boxes combined by \( \rulename{\vee E} \), or a correct \( \rulename{RAA} \) box on the negated goal.
- 2: in one case, the implication by a box that repeats the case assumption.
- 2: in the other case, the implication by a box that clashes with the case assumption, then \( \rulename{\bot E} \).
- 1: \( \rulename{\vee I} \) on the correct side in each case, every citation available.
- 2: the paragraph names the \( \rulename{LEM} \) line (or the \( \rulename{RAA} \) line) and explains why no other step of the method applies.

Fatal errors (0 for the step): choosing a side of the goal before the split; citing one case's assumption in the other case.
A correct derivation by \( \rulename{RAA} \) on the negated goal earns full marks: its 2 + 2 + 1 points go to the two implications derived inside the \( \rulename{RAA} \) box (one by a box that repeats an assumption, one by a clash and \( \rulename{\bot E} \)) and to the \( \rulename{\vee I} \) lines that clash with the \( \rulename{RAA} \) assumption.
:::

::: {#exr-finding-derivations-c3}
[C3: Exit check: derivations]

Derive each sequent, justifying every line.

::: {.enumerate options="label=(\alph*)"}
1. \( (P \to Q) \wedge (Q \to R) \vdash P \to R \).
2. \( \neg(P \wedge Q), \ P \vdash \neg Q \).
3. \( \neg(P \wedge \neg Q), \ P \vdash Q \). Say which rule of your derivation is classical.
:::
:::

::: {.solution}
(a) A box on \( P \), with the premise split by \( \rulename{\wedge E} \):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \to Q) \wedge (Q \to R)}
  \have {2} {P \to Q} \ae{1}
  \have {3} {Q \to R} \ae{1}
  \open
  \hypo {4} {P}
  \have {5} {Q} \ie{2,4}
  \have {6} {R} \ie{3,5}
  \close
  \have {7} {P \to R} \ii{4-6}
\end{nd}$
\end{center}
```

(b) The goal is a negation: a \( \rulename{\neg I} \) box on \( Q \), in which \( P \wedge Q \) clashes with the first premise.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \wedge Q)}
  \hypo {2} {P}
  \open
  \hypo {3} {Q}
  \have {4} {P \wedge Q} \ai{2,3}
  \have {5} {\bot} \ne{4,1}
  \close
  \have {6} {\neg Q} \ni{3-5}
\end{nd}$
\end{center}
```

(c) The goal \( Q \) is a letter, and the resources give nothing directly, so \( \rulename{RAA} \): a box on \( \neg Q \), in which \( P \wedge \neg Q \) clashes with the first premise.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \wedge \neg Q)}
  \hypo {2} {P}
  \open
  \hypo {3} {\neg Q}
  \have {4} {P \wedge \neg Q} \ai{2,3}
  \have {5} {\bot} \ne{4,1}
  \close
  \have {6} {Q} \raa{3-5}
\end{nd}$
\end{center}
```

The classical rule is \( \rulename{RAA} \) at line 6. The derivations of (b) and (c) have the same shape, and the difference is the goal: in (b) it is a negation, which \( \rulename{\neg I} \) builds; in (c) it is a letter, and \( \rulename{\neg I} \) on the box of \( \neg Q \) would give only \( \neg\neg Q \), which needs \( \rulename{\neg\neg E} \) to become \( Q \).

**Marking scheme.** (10 points)
- 2: (a) a \( \rulename{{\to}I} \) box opened with \( P \) and closed on \( R \).
- 2: (a) the \( \rulename{\wedge E} \) and \( \rulename{{\to}E} \) steps, each justified.
- 2: every citation in (a)–(c) is available.
- 2: (b) a \( \rulename{\neg I} \) box on \( Q \) whose \( \bot \) comes from \( \rulename{\neg E} \) against the premise.
- 2: (c) a correct derivation, by \( \rulename{RAA} \) on \( \neg Q \) or by \( \rulename{\neg I} \) to \( \neg\neg Q \) and then \( \rulename{\neg\neg E} \), with the classical rule named.

Fatal errors (0 for the step): citing a line of a closed box; writing \( Q \) where only \( \neg\neg Q \) has been derived, without \( \rulename{\neg\neg E} \).
:::

::: {#exr-finding-derivations-c4}
[C4: Exit check: search]

Find a derivation of \( P \to (Q \to R) \vdash (P \to Q) \to (P \to R) \), and describe the search in three sentences, naming its goal-directed and premise-directed steps.
:::

::: {.solution}
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \to R)}
  \open
  \hypo {2} {P \to Q}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{2,3}
  \have {5} {Q \to R} \ie{1,3}
  \have {6} {R} \ie{5,4}
  \close
  \have {7} {P \to R} \ii{3-6}
  \close
  \have {8} {(P \to Q) \to (P \to R)} \ii{2-7}
\end{nd}$
\end{center}
```

The search: the goal is an implication, so a goal-directed step opens a box on \( P \to Q \) with the goal \( P \to R \), and a second goal-directed step opens a box on \( P \) with the goal \( R \). Inside both boxes \( P \) is a resource, so premise-directed steps apply \( \rulename{{\to}E} \) to it twice, giving \( Q \) from \( P \to Q \) and \( Q \to R \) from the premise. A last \( \rulename{{\to}E} \) gives \( R \), and the two boxes close in reverse order of opening.

**Marking scheme.** (10 points)
- 2: a \( \rulename{{\to}I} \) box on \( P \to Q \), read off the goal.
- 2: inside it, a \( \rulename{{\to}I} \) box on \( P \), read off the new goal \( P \to R \).
- 3: \( Q \) and \( Q \to R \) by \( \rulename{{\to}E} \) from available lines, then \( R \).
- 1: both boxes closed in the right order, every citation available.
- 2: the three sentences name at least one goal-directed and one premise-directed step correctly.

Fatal errors (0 for the step): a box opened on the consequent (the converse error); citing a line of a closed box. A derivation found by another order of the same steps earns full marks.
:::

### R. Review

::: {#exr-finding-derivations-r1}
[R1]

Let \( x \) be a real number. Write \( N \) for "\( x < 0 \)", \( G \) for "\( x > 1 \)" and \( S \) for "\( x = 7 \)". Translate the argument below into a sequent in these letters, and derive it.

> \( x \) is neither negative nor greater than \( 1 \). Therefore \( x \) is not negative, and if \( x \) is greater than \( 1 \), then \( x = 7 \).
:::

::: {.solution}
"Neither \( N \) nor \( G \)" says that \( N \vee G \) fails, so the premise is \( \neg(N \vee G) \), not \( \neg N \vee G \). The conclusion is a conjunction whose second part is an implication. The sequent (@def-sequent) is
\[
\neg(N \vee G) \vdash \neg N \wedge (G \to S).
\]
The goal is a conjunction; the first conjunct is a negation (a \( \rulename{\neg I} \) box on \( N \)), and the second an implication (a box on \( G \)). In both boxes \( \rulename{\vee I} \) builds \( N \vee G \), which clashes with the premise; in the second box \( \rulename{\bot E} \) then gives \( S \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (N \vee G)}
  \open
  \hypo {2} {N}
  \have {3} {N \vee G} \oi{2}
  \have {4} {\bot} \ne{3,1}
  \close
  \have {5} {\neg N} \ni{2-4}
  \open
  \hypo {6} {G}
  \have {7} {N \vee G} \oi{6}
  \have {8} {\bot} \ne{7,1}
  \have {9} {S} \be{8}
  \close
  \have {10} {G \to S} \ii{6-9}
  \have {11} {\neg N \wedge (G \to S)} \ai{5,10}
\end{nd}$
\end{center}
```

Lines 2–5 are half of @prp-de-morgan (a), which turns "neither … nor" into \( \neg N \wedge \neg G \). The implication \( G \to S \) is vacuously true, as in @prp-vacuous-implication: the premise rules out \( G \), and a promise never tested is never broken, whatever \( S \) says.
:::

::: {#exr-finding-derivations-r2}
[R2]

For real numbers \( a \) and \( b \), let \( \max(a, b) \coloneqq a \) and \( \min(a, b) \coloneqq b \) if \( a \ge b \), and \( \max(a, b) \coloneqq b \) and \( \min(a, b) \coloneqq a \) if \( a < b \). Prove that \( \max(a, b) + \min(a, b) = a + b \).
:::

::: {.solution}
Since \( a \ge b \) or \( a < b \), and these two cases cover every pair of real numbers, we argue by cases (\( \rulename{\vee E} \), @def-rules-disjunction), as in @exm-abs-product-cases.

*Case \( a \ge b \).* Then \( \max(a, b) = a \) and \( \min(a, b) = b \), so \( \max(a, b) + \min(a, b) = a + b \).

*Case \( a < b \).* Then \( \max(a, b) = b \) and \( \min(a, b) = a \), so \( \max(a, b) + \min(a, b) = b + a = a + b \).

In either case the equation holds, which proves it. Both cases end in the same statement, the goal, as \( \rulename{\vee E} \) requires.
:::

::: {#exr-finding-derivations-r3}
[R3]

Is \( (P \to Q) \to R \vdash P \to (Q \to R) \) derivable? And is its converse, \( P \to (Q \to R) \vdash (P \to Q) \to R \)?
:::

::: {.solution}
The first is derivable, by the search method of this section. The goal gives a box on \( P \), then a box on \( Q \), with the goal \( R \). The premise gives \( R \) by \( \rulename{{\to}E} \) once we produce \( P \to Q \), a new goal: a box on \( P \) whose last line repeats \( Q \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \to Q) \to R}
  \open
  \hypo {2} {P}
  \open
  \hypo {3} {Q}
  \open
  \hypo {4} {P}
  \have {5} {Q} \r{3}
  \close
  \have {6} {P \to Q} \ii{4-5}
  \have {7} {R} \ie{1,6}
  \close
  \have {8} {Q \to R} \ii{3-7}
  \close
  \have {9} {P \to (Q \to R)} \ii{2-8}
\end{nd}$
\end{center}
```

The repetition at line 5 puts \( Q \) inside the box of line 4, as \( \rulename{{\to}I} \) requires. Two look-alike tools do not apply. @prp-curry moves a **conjunction** in and out of an antecedent, \( (P \wedge Q) \to R \dashv\vdash P \to (Q \to R) \), and the premise here has \( P \to Q \), not \( P \wedge Q \), in that place. And @prp-implication-transitive chains two implications, which we do not have.

The converse is not derivable, but a search can only stall, not show it. With \( P \) and \( R \) false (and \( Q \) either way), the premise \( P \to (Q \to R) \) is true because \( P \) is false, while \( P \to Q \) is true and \( R \) is false, so the conclusion is false. Chapter 2 proves that such a row rules out every derivation: the chapter's open question, in a new place.
:::

<!-- dependency ledger
prp-peirce (claim): every derivation of Peirce's law uses RAA or an equivalent | stated without proof and marked so in the text; nothing depends on it
exm-search-postpone-or (example): neither disjunct follows from the premise (two rows) | informal, with a pointer to ch02 (thm-soundness); the example does not depend on it
exm-search-postpone-or (example): LEM on P also succeeds, with a nested or-E | inline description; not used
exm-skeleton-odd-product (example): every integer is even or odd, and not both; m = 2k gives mn = 2(kn) | school algebra, an allowed prerequisite of ch01 (blueprint)
exm-skeleton-odd-product (example): "say m = 2k" names a witness | informal reading of "there exists"; the rule is ch03's, flagged in prose
finding-derivations-method (claim): the goal-directed steps and RAA never turn a derivable gap into an underivable one | inline (argued in the text from def-derivable and one elimination step)
finding-derivations-method (claim): P or Q |- Q or P is derivable but neither disjunct follows from P or Q alone | derivability: s03 (the derivation of P or Q |- Q or P); non-derivation of the disjuncts: informal, ch02 makes it exact; nothing depends on it
finding-derivations-failed-search (claim): no derivation of Q -> P from P -> Q exists | not claimed as proved; forward pointer to ch02 (cor-refuting-row), which is the chapter's closing question
exr-finding-derivations-a1 (solution): (b) naming n uses a rule for "there exists" | informal; ch03 (flagged in prose)
exr-finding-derivations-b1 (solution): no derivation of P from not(P -> Q) avoids RAA | stated without proof and marked so; nothing depends on it
exr-finding-derivations-c2 (solution): neither disjunct is derivable from no premises (rows) | informal, pointer to ch02; the solution says it proves only that the method needs step 5
exr-finding-derivations-r2 (solution): a >= b or a < b for real numbers; b + a = a + b | school algebra, an allowed prerequisite
exr-finding-derivations-r3 (solution): the converse is not derivable (row P = R = false) | forward pointer to ch02 (cor-refuting-row), flagged in the solution
-->
