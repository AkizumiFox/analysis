# And, Implies, and the Box

The previous section ended with a plan. Proofs are made of statements (@def-statement), and every connective that builds statements comes with an introduction rule, saying how to prove a statement built with it, and an elimination rule, saying how to use one. This section carries out the plan for "and" and for "implies". The rules for "and" hold no surprises. The rules for "implies" bring in the one genuinely new idea of the chapter: a proof may **assume** something it does not know, provided it keeps track of where the assumption is in force. The device that keeps track is a box.

## The rules for "and"

We met these two rules in the previous section. Here they are in the form we will use from now on.

::: {#def-rules-conjunction}
[Rules for Conjunction]

- \( \rulename{\wedge I} \) (**and-introduction**). If \( P \) and \( Q \) both stand on earlier lines, we may write \( P \wedge Q \).
- \( \rulename{\wedge E} \) (**and-elimination**). If \( P \wedge Q \) stands on an earlier line, we may write \( P \), and we may write \( Q \).
:::

"Earlier lines" will be made more precise below, once boxes exist; not every earlier line may be used. Here is the pair at work on numbers.

::: {#exm-product-in-unit-interval}
[A product of numbers in the unit interval]

Let \( x \) and \( y \) be real numbers with \( 0 < x < 1 \) and \( 0 < y < 1 \). Show that \( 0 < xy < 1 \), and name the rule behind each logical step.
:::

::: {.solution}
The hypothesis \( 0 < x < 1 \) is the conjunction \( (0 < x) \wedge (x < 1) \). By \( [\rulename{\wedge E}] \) we have \( 0 < x \) and \( x < 1 \) separately, and likewise \( 0 < y \) and \( y < 1 \).

Since \( x > 0 \) and \( y > 0 \), the product \( xy \) is positive. Since \( y < 1 \) and \( x > 0 \), multiplying by \( x \) gives \( xy < x \); together with \( x < 1 \) this gives \( xy < 1 \). These three steps are school algebra, not logic.

Finally, from \( 0 < xy \) and \( xy < 1 \), \( [\rulename{\wedge I}] \) gives \( (0 < xy) \wedge (xy < 1) \), which is \( 0 < xy < 1 \).
:::

The solution shows the division of labor that runs through every proof in the book. The facts about numbers (a product of positive numbers is positive, multiplying by a positive number keeps an inequality) supply the content. The rules supply the joints: they take a statement apart, and they put the pieces back together.

Proofs about letters \( P \), \( Q \), \( R \) have no content of their own, only joints, and this makes them the clearest place to see the rules. We lay such a proof out as a **derivation**: numbered lines, each carrying one statement and, on the right, its justification. Here is a derivation of \( Q \wedge P \) from \( P \wedge Q \).
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge Q}
  \have {2} {P} \ae{1}
  \have {3} {Q} \ae{1}
  \have {4} {Q \wedge P} \ai{3,2}
\end{nd}$
\end{center}
```
A **premise** is a statement we are given, and the derivation shows what follows from it. The justification "\( \rulename{\wedge I}\ 3, 2 \)" says that line 4 comes from the rule \( \rulename{\wedge I} \) applied to lines 3 and 2, in that order: the statement on line 3 becomes the left half of line 4. Line 4 is a statement the rules produced from line 1 alone, without looking at what \( P \) and \( Q \) say.

## The rules for "implies", and the box

Most theorems have the shape "if …, then …". How does a mathematician prove one? Take a simple case.

> Let \( x \) be a real number. If \( x > 2 \), then \( x^2 > 4 \).

The proof everyone would write goes like this. *Suppose \( x > 2 \). Then \( x > 0 \), so multiplying \( x > 2 \) by \( x \) gives \( x^2 > 2x \). Also \( 2x > 4 \). Hence \( x^2 > 4 \).* And then, often silently: *this proves that if \( x > 2 \), then \( x^2 > 4 \).*

Look at the status of the first sentence. We do not know that \( x > 2 \); for all we know, \( x = 0 \). The sentence "suppose \( x > 2 \)" does not claim anything. It opens a temporary world in which \( x > 2 \) holds, so that we can see what else holds there. The sentences "\( x^2 > 2x \)" and "\( x^2 > 4 \)" are true **in that world**, and not in general: at \( x = 0 \) both are false. Only the final sentence leaves the temporary world, and what it carries out is not "\( x^2 > 4 \)" but the implication "if \( x > 2 \), then \( x^2 > 4 \)", which is true for every \( x \).

A derivation draws the temporary world as a **box**. The assumption opens the box, and is marked by a vertical bar to its left and a line under it. Everything derived inside the box is marked by the same bar. When the box closes, the bar stops, and the one thing allowed out is the implication from the assumption to what was reached.

*To prove "if \( P \) then \( Q \)", assume \( P \) in a box, reach \( Q \) inside it, and close the box.*

::: {#def-rules-implication}
[Rules for Implication]

- \( \rulename{{\to}I} \) (**implication-introduction**). Open a box whose first line is the **assumption** \( P \). If \( Q \) is reached as a line of that box, not inside a further box, we may close the box and write \( P \to Q \) on the next line, outside it. The justification cites the whole box as a range of lines, as in \( \rulename{{\to}I}\ \lines{3}{5} \). We say the assumption \( P \) is **discharged**.
- \( \rulename{{\to}E} \) (**implication-elimination**, or **modus ponens**). If \( P \to Q \) and \( P \) stand on earlier lines, we may write \( Q \).
:::

The elimination rule is the everyday use of a theorem. The school fact "if \( a < b \) and \( b < c \), then \( a < c \)" is an implication. Given the two specific facts \( \sqrt{2} < 1.5 \) and \( 1.5 < 2 \), it yields \( \sqrt{2} < 2 \). Every time a proof says "by Theorem so-and-so", it is applying \( \rulename{{\to}E} \) to the theorem and to the verified hypotheses.

The introduction rule is the new move. Here it is in its first full derivation, which proves that implication is transitive: from \( P \to Q \) and \( Q \to R \) we get \( P \to R \).
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {Q \to R}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \have {5} {R} \ie{2,4}
  \close
  \have {6} {P \to R} \ii{3-5}
\end{nd}$
\end{center}
```
Line 3 opens a box with the assumption \( P \). Inside it, two applications of modus ponens reach \( R \). Line 6 closes the box, and the bar stops: \( P \) and \( R \) were never established outright, and only \( P \to R \) leaves.

Now give the letters some content. Let \( x \) be a real number, and let
\[
P : x > 3, \qquad Q : x^2 > 9, \qquad R : x^2 > 4 .
\]
The premise \( P \to Q \) holds because, when \( x > 3 \), we have \( x > 0 \) and so \( x^2 = x \cdot x > 3x > 9 \). The premise \( Q \to R \) is an instance of the transitivity of \( < \): if \( 4 < 9 \) and \( 9 < x^2 \), then \( 4 < x^2 \), and \( 4 < 9 \) is true. With these premises in hand, the derivation becomes the following paragraph, one sentence per line.

| Line | Sentence |
|---|---|
| 3 | Suppose \( x > 3 \). |
| 4 | Since \( x > 3 \) implies \( x^2 > 9 \), we get \( x^2 > 9 \). |
| 5 | Since \( 4 < 9 \) and \( 9 < x^2 \), we get \( x^2 > 4 \). |
| 6 | Hence, if \( x > 3 \), then \( x^2 > 4 \). |

A practiced writer would compress this to "If \( x > 3 \), then \( x^2 > 9 > 4 \)." The compressed version is a fine proof, but it is the same derivation with its joints hidden. When a proof becomes hard to follow, expanding it back into this form is how one finds the gap.

## Derivations, precisely

We have been drawing boxes by example. Before we rely on them, we need to say exactly what is allowed, because the one thing boxes are for is to stop an assumption from being used where it does not hold.

Consider what happens without them. If a proof could say "suppose \( x > 2 \)" and later simply assert "\( x > 2 \)" as a fact, it could prove that every real number exceeds \( 2 \). The assumption is useful only because it comes with a boundary, and the boundary must be respected by every line after it. So the precise definition is mostly about which earlier lines a new line may use.

*A derivation is a list of lines in which every line is a premise, an assumption that opens a box, or the result of one rule applied to lines that are still available.*

::: {#def-derivation}
[Derivation]

A **derivation** is a finite list of numbered lines, each carrying one statement and a justification, together with a set of **boxes**. A box is a block of consecutive lines whose first line is an assumption, and any two boxes are either disjoint or **one inside the other**. A box may end after any of its lines; once ended it stays closed, and the **last line** of a derivation lies outside every box.

**The scope rule.** Line \( i \) is **available** at line \( k \) if \( i < k \) and **every** box containing line \( i \) also contains line \( k \); in other words, line \( i \) is earlier and does not lie inside a box that has closed before line \( k \). A closed box is **available** at line \( k \) if it ends before line \( k \) and every box containing it also contains line \( k \). A line may cite only available lines and available boxes.

Every line is exactly one of the following:

::: {.enumerate options="label=(D\arabic*)"}
1. a **premise**, which stands before every box;
2. an **assumption**, which may be **any** statement, and opens a new box;
3. a **repetition** of a statement on a line available at this one;
4. the conclusion of **one** rule, applied to lines and boxes available at this one.
:::
:::

In words. (D1) Premises are the givens, and they hold throughout. (D2) We may assume anything we like, but the assumption opens a box, and that is the price. (D3) A statement already established, and still in force, may be written again; this is occasionally needed to put a statement where a rule wants it. (D4) Everything else is one step of one rule.

The scope rule is the definition's real content. Line \( i \) is available at line \( k \) when every assumption that line \( i \) depended on is still in force at line \( k \). A line outside all boxes is available everywhere below it. A line inside a box is available further down that box, and inside boxes opened within it, but not after the box closes. A closed box, cited as a whole by a rule such as \( \rulename{{\to}I} \), must sit directly inside the part of the derivation where the citing line is.

With derivations defined, we can say what it means for a statement to follow from others.

::: {#def-derivable}
[Derivable]

Let \( \Gamma \) be a list of statements and \( P \) a statement. We say \( P \) is **derivable** from \( \Gamma \), and write
\[
\Gamma \vdash P ,
\]
if there is a derivation whose premises all belong to \( \Gamma \) and whose last line is \( P \). We write \( P_1, \dots, P_n \vdash P \) when \( \Gamma \) consists of \( P_1, \dots, P_n \), and \( \vdash P \) when \( \Gamma \) is empty.
:::

The symbol \( \vdash \) is read "proves" or "derives". It makes a claim about derivations, not about the truth of \( P \): \( \Gamma \vdash P \) says that a derivation exists, and exhibiting one proves the claim.

::: {#exm-derivations}
[Derivations, simplest first]

Decide whether each of the following is a derivation, and if so, what it shows.

::: {.enumerate options="label=(\alph*)"}
1. The single line \( 1 \quad P \quad \text{premise} \).
2. The two lines below, which have no premises.
```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {P}
  \close
  \have {2} {P \to P} \ii{1-1}
\end{nd}$
\end{center}
```
3. The derivation of \( P \to R \) from \( P \to Q \) and \( Q \to R \), shown after @def-rules-implication.
:::
:::

::: {.solution}
(a) Yes. Its only line is a premise (D1), and it is the last line, outside every box. It shows \( P \vdash P \): every statement is derivable from itself.

(b) Yes. Line 1 is an assumption and opens a box consisting of line 1 alone; the statement \( P \) is reached in that box, namely on line 1 itself. So \( \rulename{{\to}I} \) may close the box and write \( P \to P \). The last line lies outside the box, and there are no premises, so this shows \( \vdash P \to P \). A statement derivable from no premises at all is true however things stand, and \( P \to P \) is the simplest example.

(c) Yes. Lines 1 and 2 are premises (D1); line 3 is an assumption (D2); lines 4 and 5 apply \( \rulename{{\to}E} \) to lines that are available, since line 3 and the lines depending on it are all in the box and lines 1 and 2 are in no box; line 6 applies \( \rulename{{\to}I} \) to the box 3–5, which has just ended and is available. It shows \( P \to Q, Q \to R \vdash P \to R \).
:::

A single-line box, as in (b), is legal and occasionally useful. It is also the degenerate case that tests our reading of the definition: nothing in \( \rulename{{\to}I} \) requires the box to contain more than its assumption.

Now change that derivation of \( P \to R \) by one line, as a careless writer might.
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {Q \to R}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \have {5} {R} \ie{2,4}
  \close
  \have {6} {P \to R} \ii{3-5}
  \have {7} {R} \r{5}
\end{nd}$
\end{center}
```
Lines 1–6 are as before, and line 7 is justified by (D3), a repetition. It is illegal. Line 5 lies inside the box 3–5, which does not contain line 7, so line 5 is not available at line 7. If the line were allowed, the derivation would show \( P \to Q, Q \to R \vdash R \), which is absurd: with \( x \) a real number, take \( P \): "\( x > 3 \)", \( Q \): "\( x > 2 \)" and \( R \): "\( x > 1 \)". Both premises are true whatever \( x \) is, and at \( x = 0 \) the conclusion is false.

::: {.warning}
The assumption of a closed box is gone. Here is a typical slip. *"Suppose \( x > 1 \). Then \( x^2 = x \cdot x > 1 \cdot x > 1 \). Hence \( x > 1 \) implies \( x^2 > 1 \). Moreover \( x^3 = x \cdot x^2 > 1 \), so \( x^3 > 1 \)."* The sentence "Hence …" closed the box; the last sentence still uses \( x > 1 \), and so it asserts \( x^3 > 1 \) for every \( x \), which fails at \( x = 0 \). The assumption has left its scope. The repair is to keep the box open until everything that needs \( x > 1 \) is done, and to conclude "if \( x > 1 \), then \( x^2 > 1 \) and \( x^3 > 1 \)". Chapter 2 lists this error in its catalog of what is not allowed.
:::

::: {.check}
In the derivation below, which of lines 3 to 7 may cite line 2 individually?
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \open
  \hypo {2} {P}
  \have {3} {Q} \ie{1,2}
  \have {4} {P \wedge Q} \ai{2,3}
  \have {5} {Q \wedge P} \ai{3,2}
  \close
  \have {6} {P \to (Q \wedge P)} \ii{2-5}
  \have {7} {(P \to Q) \wedge (P \to (Q \wedge P))} \ai{1,6}
\end{nd}$
\end{center}
```
:::

::: {.solution}
Lines 3, 4 and 5. They lie in the box 2–5, which is the only box containing line 2, so line 2 is available to each of them. Line 6 cites the box 2–5 as a whole, which is what \( \rulename{{\to}I} \) requires; it does not cite line 2 by itself, and could not, since line 6 is outside the box. Line 7 may not cite line 2 either, for the same reason.
:::

## The first derived results

A derivation with letters proves more than one fact. The rules look only at the shapes of statements, at their main connectives, never at what the letters say. So if every letter in a derivation is replaced by a statement, the same letter by the same statement throughout, every line stays justified by the same rule. A derivation of \( P \wedge Q \vdash Q \wedge P \) is at the same time a derivation of \( (0 < x) \wedge (x < 1) \vdash (x < 1) \wedge (0 < x) \), and of every other instance. We record the three most useful facts of this section.

::: {#prp-and-commutes}
[Conjunction Commutes]

\( P \wedge Q \vdash Q \wedge P \).
:::

::: {.proof}
The derivation of \( Q \wedge P \) shown after @def-rules-conjunction has the single premise \( P \wedge Q \), and its last line is \( Q \wedge P \). Its lines are a premise and three rule applications, each citing line 1 or lines outside every box, so it is a derivation by @def-derivation. This proves the proposition.
:::

::: {#prp-implication-transitive}
[Implication Is Transitive]

\( P \to Q, \; Q \to R \vdash P \to R \).
:::

::: {.proof}
The derivation of \( P \to R \) shown after @def-rules-implication has premises \( P \to Q \) and \( Q \to R \), and its last line is \( P \to R \). It was checked against @def-derivation in @exm-derivations. This proves the proposition.
:::

The third result explains a habit of mathematical writing. A theorem with two hypotheses, "if \( x > 0 \) and \( y > 0 \), then \( xy > 0 \)", is often written with one hypothesis at a time: "let \( x > 0 \); then for every \( y > 0 \), \( xy > 0 \)". The two forms are \( (P \wedge Q) \to R \) and \( P \to (Q \to R) \), and they are interchangeable.

::: {#prp-curry}
[Two Hypotheses or One at a Time]

\( (P \wedge Q) \to R \vdash P \to (Q \to R) \), and \( P \to (Q \to R) \vdash (P \wedge Q) \to R \).
:::

::: {.idea}
Read each goal's main connective. For \( P \to (Q \to R) \) it is \( \to \), so assume \( P \); the new goal \( Q \to R \) is again an implication, so assume \( Q \) in a box inside the first. With both assumptions available, \( P \wedge Q \) is one application of \( \rulename{\wedge I} \) away, and the premise finishes. For the converse, assume \( P \wedge Q \) and take it apart.
:::

::: {.proof}
For the first claim, the following is a derivation with premise \( (P \wedge Q) \to R \) and last line \( P \to (Q \to R) \).
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge Q) \to R}
  \open
  \hypo {2} {P}
  \open
  \hypo {3} {Q}
  \have {4} {P \wedge Q} \ai{2,3}
  \have {5} {R} \ie{1,4}
  \close
  \have {6} {Q \to R} \ii{3-5}
  \close
  \have {7} {P \to (Q \to R)} \ii{2-6}
\end{nd}$
\end{center}
```
Line 4 may cite line 2 because the only box containing line 2, the box 2–6, also contains line 4.

For the second claim, the following is a derivation with premise \( P \to (Q \to R) \) and last line \( (P \wedge Q) \to R \).
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \to R)}
  \open
  \hypo {2} {P \wedge Q}
  \have {3} {P} \ae{2}
  \have {4} {Q} \ae{2}
  \have {5} {Q \to R} \ie{1,3}
  \have {6} {R} \ie{5,4}
  \close
  \have {7} {(P \wedge Q) \to R} \ii{2-6}
\end{nd}$
\end{center}
```
This proves both claims.
:::

In the first derivation the boxes are nested, and the inner one closes first: an assumption made later is discharged earlier. That is the general pattern, forced by @def-derivation, since two boxes are either disjoint or one inside the other.

Each derived result can now be used as a **derived rule**. If \( \Gamma \vdash P \) has been shown with letters, and instances of the statements in \( \Gamma \) stand on available lines of some later derivation, we may write the corresponding instance of \( P \), citing the result. Nothing new is being allowed: we could instead copy in the derivation of \( P \), with its letters replaced, its premises replaced by repetitions (D3) of the available lines, and its line numbers shifted. The citation is an abbreviation for that copy. For example, @prp-implication-transitive lets a later derivation pass from \( P \to Q \) and \( Q \to R \) to \( P \to R \) in one line, citing the proposition.

## What the rules sound like

Every rule is something mathematicians already say. The table below pairs each rule of this section with the sentence that uses it in a written proof, and, for readers who meet a proof assistant, with the Lean tactic that performs it. Nothing later in the book depends on the last column.

| Rule | You write | Lean |
|------|--------------------------------------|------------------------|
| \( \rulename{\wedge I} \) | "We show \( P \), and we show \( Q \)." | `constructor` |
| \( \rulename{\wedge E} \) | "In particular, \( P \)." | `h.1` (and `h.2`) |
| \( \rulename{{\to}I} \) | "Assume \( P \). … Hence \( Q \)." | `intro hp` |
| \( \rulename{{\to}E} \) | "Since \( P \) implies \( Q \), and \( P \) holds, \( Q \)." | `exact h hp` |

The sentence for \( \rulename{{\to}I} \) is the one to watch. "Assume \( P \)" opens a box, and "hence \( Q \)" is the last line inside it. The conclusion "\( P \) implies \( Q \)" is so often left unsaid that the box's closing line is invisible on the page. It is still there, and it is the line Argument B at the start of Section 1.1 gets wrong.

## Exercises

### A. Check your understanding

::: {#exr-conjunction-and-implication-a1}
[A1]

Consider the following derivation, whose justifications are missing.
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \to R)}
  \hypo {2} {Q}
  \open
  \hypo {3} {P}
  \have {4} {Q \to R} \by{(i)}{}
  \have {5} {R} \by{(ii)}{}
  \close
  \have {6} {P \to R} \by{(iii)}{}
\end{nd}$
\end{center}
```

::: {.enumerate options="label=(\alph*)"}
1. State the rules \( \rulename{{\to}I} \) and \( \rulename{{\to}E} \).
2. Fill in the justifications (i), (ii), (iii).
3. Which of lines 1–5 are available at line 6?
4. True or false, with a reason: line 5 could equally be justified as \( \rulename{{\to}E}\ 1, 2 \).
5. What does the derivation show, written with \( \vdash \)?
:::
:::

::: {.solution}
(a) \( \rulename{{\to}I} \): if a box opened by the assumption \( P \) contains \( Q \) as a line of its own, we may close the box and write \( P \to Q \). \( \rulename{{\to}E} \): from \( P \to Q \) and \( P \) on available lines, we may write \( Q \) (@def-rules-implication).

(b) The justifications are (i) \( \rulename{{\to}E}\ 1, 3 \); (ii) \( \rulename{{\to}E}\ 4, 2 \); (iii) \( \rulename{{\to}I}\ \lines{3}{5} \).

(c) Lines 1 and 2. Lines 3, 4 and 5 lie in the box 3–5, which does not contain line 6. (The box 3–5 as a whole is available at line 6, which is why (iii) may cite it.)

(d) False. \( \rulename{{\to}E} \) needs an implication and its hypothesis. Line 1 is \( P \to (Q \to R) \), whose hypothesis is \( P \), not \( Q \); applied to lines 1 and 2 the rule does not apply at all.

(e) \( P \to (Q \to R), \; Q \vdash P \to R \).
:::

### B. Practice

::: {#exr-conjunction-and-implication-b1}
[B1: Swapping inside an implication]

Show that \( \vdash (P \wedge Q) \to (Q \wedge P) \) by a derivation. Then write the argument as a paragraph of prose, one sentence per line.
:::

::: {.solution}
The goal has main connective \( \to \), so the derivation assumes \( P \wedge Q \).
```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {P \wedge Q}
  \have {2} {P} \ae{1}
  \have {3} {Q} \ae{1}
  \have {4} {Q \wedge P} \ai{3,2}
  \close
  \have {5} {(P \wedge Q) \to (Q \wedge P)} \ii{1-4}
\end{nd}$
\end{center}
```
It has no premises, and its last line lies outside the box, so it shows \( \vdash (P \wedge Q) \to (Q \wedge P) \).

In prose: *Assume \( P \) and \( Q \). In particular \( P \) holds, and in particular \( Q \) holds. Hence \( Q \) and \( P \) both hold. This proves that if \( P \) and \( Q \), then \( Q \) and \( P \).* Compared with @prp-and-commutes, the premise \( P \wedge Q \) has become an assumption, and the conclusion has become an implication that depends on nothing.
:::

::: {#exr-conjunction-and-implication-b2}
[B2: An assumption that is not used]

Show that \( \vdash P \to (Q \to P) \) by a derivation, and write it as prose. Then give the instance with \( P \): "\( x^2 \ge 0 \)" and \( Q \): "\( x > 5 \)", for a real number \( x \), as an English sentence.
:::

::: {.solution}
Both implications are proved by \( \rulename{{\to}I} \), so the derivation opens two boxes, one inside the other.
```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {P}
  \open
  \hypo {2} {Q}
  \have {3} {P} \r{1}
  \close
  \have {4} {Q \to P} \ii{2-3}
  \close
  \have {5} {P \to (Q \to P)} \ii{1-4}
\end{nd}$
\end{center}
```
Line 3 is a legal repetition (D3): the only box containing line 1 is the box 1–4, which also contains line 3. It is needed because \( \rulename{{\to}I} \) asks for \( P \) as a line of the box 2–3 itself.

In prose: *Assume \( P \). Assume further \( Q \). Then \( P \) holds, since it was assumed. Hence \( Q \) implies \( P \). This proves that \( P \) implies that \( Q \) implies \( P \).*

The instance reads: "if \( x^2 \ge 0 \), then (if \( x > 5 \), then \( x^2 \ge 0 \))". The assumption \( x > 5 \) is never used, and nothing in \( \rulename{{\to}I} \) requires it to be. An implication whose conclusion is already known holds whatever its hypothesis.
:::

::: {#exr-conjunction-and-implication-b3}
[B3: Unwinding an absolute value]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( P \to Q, \; P \to R \vdash P \to (Q \wedge R) \).
2. Let \( x \) be a real number. Use (a) to deduce "if \( \abs{x - 2} < 1 \), then \( 1 < x < 3 \)" from the two facts "if \( \abs{x - 2} < 1 \), then \( x > 1 \)" and "if \( \abs{x - 2} < 1 \), then \( x < 3 \)". Write the resulting argument as prose.
:::
:::

::: {.solution}
(a) The goal is an implication, so assume \( P \), and reach \( Q \wedge R \) by getting each half.
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {P \to R}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \have {5} {R} \ie{2,3}
  \have {6} {Q \wedge R} \ai{4,5}
  \close
  \have {7} {P \to (Q \wedge R)} \ii{3-6}
\end{nd}$
\end{center}
```

(b) Take \( P \): "\( \abs{x - 2} < 1 \)", \( Q \): "\( x > 1 \)" and \( R \): "\( x < 3 \)". The two facts are the premises \( P \to Q \) and \( P \to R \), and \( Q \wedge R \) is \( 1 < x < 3 \). By (a), with the letters replaced, the implication \( P \to (Q \wedge R) \) follows.

In prose: *Suppose \( \abs{x - 2} < 1 \). Then \( x > 1 \) by the first fact, and \( x < 3 \) by the second. Hence \( 1 < x < 3 \). This proves that \( \abs{x - 2} < 1 \) implies \( 1 < x < 3 \).*
:::

### C. Going deeper

::: {#exr-conjunction-and-implication-c1}
[C1: A line from a closed box]

A student offers the following derivation, claiming it shows \( P \to Q, \; Q \to R \vdash R \).
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {Q \to R}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \have {5} {R} \ie{2,4}
  \close
  \have {6} {P \to R} \ii{3-5}
  \have {7} {Q} \ie{1,3}
  \have {8} {R} \ie{2,7}
\end{nd}$
\end{center}
```

::: {.enumerate options="label=(\alph*)"}
1. Find the first illegal line and name the rule, or the clause of @def-derivation, that it breaks.
2. Repair the derivation, if possible, so that it proves a correct statement from the same premises.
3. Is \( R \) derivable from \( P \to Q \) and \( Q \to R \)? Justify your answer.
:::

*Hint: for (c), give the letters a meaning.*
:::

::: {.solution}
(a) Line 7 is illegal. It applies \( \rulename{{\to}E} \) to lines 1 and 3, but line 3 lies in the box 3–5, which ended at line 5 and does not contain line 7. So line 3 is not available at line 7, and clause (D4) of @def-derivation, which allows a rule to be applied only to available lines, is broken. Line 8 is illegal as a consequence, since it cites line 7.

(b) Delete lines 7 and 8. Lines 1–6 are the derivation of \( P \to R \) shown after @def-rules-implication, and they correctly show \( P \to Q, \; Q \to R \vdash P \to R \) (@prp-implication-transitive). The student's derivation had in fact reached this correct conclusion at line 6 and then tried to keep going with an assumption that had already been discharged.

(c) No. Let \( x \) be a real number, and take \( P \): "\( x > 3 \)", \( Q \): "\( x > 2 \)" and \( R \): "\( x > 1 \)". Both premises are true whatever \( x \) is: every number greater than \( 3 \) is greater than \( 2 \), and every number greater than \( 2 \) is greater than \( 1 \). At \( x = 0 \) the conclusion \( R \) is false. A derivation of \( R \) from these premises, with its letters replaced by these statements, would lead from true premises to a false conclusion, and the rules are designed never to do that (Section 1.1; Section 1.6 checks it rule by rule). So no such derivation exists. The repair in (b) is the best the premises allow.
:::

::: {#exr-conjunction-and-implication-c2}
[C2: The order of hypotheses]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( P \to (Q \to R) \vdash Q \to (P \to R) \).
2. Deduce, using (a) and @prp-curry, that \( (P \wedge Q) \to R \vdash (Q \wedge P) \to R \).
3. Let \( a \) and \( x \) be real numbers. The school fact "if \( a > 0 \), then (if \( x > 1 \), then \( ax > a \))" has the shape \( P \to (Q \to R) \). Write the fact that (a) turns it into, in English.
:::
:::

::: {.solution}
(a) The goal is an implication whose conclusion is again an implication, so we open a box for \( Q \) and inside it a box for \( P \).
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \to R)}
  \open
  \hypo {2} {Q}
  \open
  \hypo {3} {P}
  \have {4} {Q \to R} \ie{1,3}
  \have {5} {R} \ie{4,2}
  \close
  \have {6} {P \to R} \ii{3-5}
  \close
  \have {7} {Q \to (P \to R)} \ii{2-6}
\end{nd}$
\end{center}
```
Line 5 may cite line 2, because the only box containing line 2, the box 2–6, also contains line 5.

(b) Using derived rules: from the premise \( (P \wedge Q) \to R \), the first half of @prp-curry gives \( P \to (Q \to R) \); part (a) gives \( Q \to (P \to R) \); and the second half of @prp-curry, with \( P \) and \( Q \) exchanged, gives \( (Q \wedge P) \to R \). Each step is an instance of a derived result applied to the line before, so the three steps together are a derivation of \( (Q \wedge P) \to R \) from \( (P \wedge Q) \to R \).

(c) "If \( x > 1 \), then (if \( a > 0 \), then \( ax > a \))". Read aloud: for a fixed \( x > 1 \), multiplying by any positive \( a \) gives \( ax > a \). The two readings say the same thing, and a proof may present whichever one suits it.
:::
