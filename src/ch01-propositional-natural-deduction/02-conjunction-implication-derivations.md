# And, Implies, and Derivations

The previous section set up the vocabulary: statements (@def-statement), the sequent as a claim about the form of an argument (@def-sequent), and the plan that every connective comes with a rule to prove it and a rule to use it. This section gives the rules for "and" and for "implies", and then says exactly what a derivation is, which makes the sequent an exact claim. The rules for "implies" bring in the one genuinely new idea of the chapter: a proof may **assume** something it does not know, provided it keeps track of where the assumption is in force. The device that keeps track is a box.

## The rules for "and"

We met these two rules in the previous section. Here they are in the form used from now on.

::: {#def-rules-conjunction}
[Rules for Conjunction]

- \( \rulename{\wedge I} \) (**and-introduction**). If \( P \) and \( Q \) both stand on available lines, we may write \( P \wedge Q \).
- \( \rulename{\wedge E} \) (**and-elimination**). If \( P \wedge Q \) stands on an available line, we may write \( P \), and we may write \( Q \).
:::

For now, "available" means "earlier". Once boxes exist, not every earlier line is available, and @def-derivation below says which ones are. Here is the pair at work on numbers.

::: {#exm-product-in-unit-interval}
[A product of numbers in the unit interval]

Let \( x \) and \( y \) be real numbers with \( 0 < x < 1 \) and \( 0 < y < 1 \). Show that \( 0 < xy < 1 \), and name the rule behind each logical step.
:::

::: {.solution}
The hypothesis \( 0 < x < 1 \) is the conjunction \( (0 < x) \wedge (x < 1) \). By \( \rulename{\wedge E} \) we have \( 0 < x \) and \( x < 1 \) separately, and likewise \( 0 < y \) and \( y < 1 \).

Since \( x > 0 \) and \( y > 0 \), the product \( xy \) is positive. Since \( y < 1 \) and \( x > 0 \), multiplying by \( x \) gives \( xy < x \); together with \( x < 1 \) this gives \( xy < 1 \). These three steps are school algebra, not logic.

Finally, from \( 0 < xy \) and \( xy < 1 \), \( \rulename{\wedge I} \) gives \( (0 < xy) \wedge (xy < 1) \), which is \( 0 < xy < 1 \).
:::

The facts about numbers supply the content of the solution; the rules supply the joints, taking statements apart and putting the pieces back together.

A proof about letters \( P \), \( Q \), \( R \) has no content of its own, only joints, which makes it the clearest place to see the rules. We lay such a proof out as a **derivation**: numbered lines, each carrying one statement and, on the right, its justification. Here is a derivation of \( Q \wedge P \) from \( P \wedge Q \).

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

Line 1 is a **premise**, a statement we are given; the short rule under it marks where the givens end. The justification "\( \rulename{\wedge I} \) 3, 2" says that line 4 comes from \( \rulename{\wedge I} \) applied to lines 3 and 2, in that order, so line 3 becomes the left half. Nothing in the derivation looks at what \( P \) and \( Q \) say.

## The rules for "implies", and the box

Most theorems have the shape "if …, then …". How does a mathematician prove one? Take a simple case.

> Let \( x \) be a real number. If \( x > 2 \), then \( x^2 > 4 \).

The proof everyone would write goes like this. *Suppose \( x > 2 \). Then \( x > 0 \), so multiplying \( x > 2 \) by \( x \) gives \( x^2 > 2x \). Also \( 2x > 4 \). Hence \( x^2 > 4 \).* And then, often silently: *this proves that if \( x > 2 \), then \( x^2 > 4 \).*

Look at the first sentence. We do not know that \( x > 2 \), and "suppose \( x > 2 \)" claims nothing. It starts a thought experiment: in a situation where \( x > 2 \), what else holds? The sentences "\( x^2 > 2x \)" and "\( x^2 > 4 \)" are true **inside the experiment**, not in general; at \( x = 0 \) both are false. Only the last sentence leaves the experiment, and what it carries out is not "\( x^2 > 4 \)" but the implication "if \( x > 2 \), then \( x^2 > 4 \)", which is true for every \( x \).

A thought experiment is only safe if it has a boundary. A derivation draws the boundary as a **box**. The assumption opens the box and is marked by a vertical bar to its left and a short rule under it. Everything derived inside the box carries the same bar. When the box closes, the bar stops, and the one thing allowed out is the implication from the assumption to what was reached.

*To prove "if \( P \), then \( Q \)", assume \( P \) in a box, reach \( Q \) inside it, and close the box.*

::: {#def-rules-implication}
[Rules for Implication]

- \( \rulename{{\to}I} \) (**implication-introduction**). Open a box whose first line is the **assumption** \( P \). When the box's last line is \( Q \), a line of that box itself and not of a further box inside it, we may close the box and write \( P \to Q \) on a line after it, outside it. The justification cites the whole box as a range of lines, as in \( \rulename{{\to}I}\ \lines{3}{5} \). We say the assumption \( P \) is **discharged**.
- \( \rulename{{\to}E} \) (**implication-elimination**, or **modus ponens**). If \( P \to Q \) and \( P \) stand on available lines, we may write \( Q \).
:::

The elimination rule is the everyday use of a theorem. The school fact "if \( a < b \) and \( b < c \), then \( a < c \)" is an implication. Given the two specific facts \( \sqrt{2} < 1.5 \) and \( 1.5 < 2 \), it yields \( \sqrt{2} < 2 \). Every time a proof says "by Theorem so-and-so", it applies \( \rulename{{\to}E} \) to the theorem and to its verified hypotheses.

The introduction rule is the new move. Here it is in its first full derivation, which shows that implication is transitive: from \( P \to Q \) and \( Q \to R \) we get \( P \to R \).

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
The premise \( P \to Q \) holds because, when \( x > 3 \), we have \( x > 0 \) and so \( x^2 = x \cdot x > 3x > 9 \). The premise \( Q \to R \) is an instance of the transitivity of \( < \): if \( 4 < 9 \) and \( 9 < x^2 \), then \( 4 < x^2 \), and \( 4 < 9 \) is true. With the premises in hand, lines 3–6 become a paragraph, one sentence per line.

| Line | Sentence |
|---|---|
| 3 | Suppose \( x > 3 \). |
| 4 | Since \( x > 3 \) implies \( x^2 > 9 \), we get \( x^2 > 9 \). |
| 5 | Since \( 4 < 9 \) and \( 9 < x^2 \), we get \( x^2 > 4 \). |
| 6 | Hence, if \( x > 3 \), then \( x^2 > 4 \). |

A practiced writer would compress this to "If \( x > 3 \), then \( x^2 > 9 > 4 \)": the same derivation with its joints hidden. When a proof is hard to follow, expanding it back into this form is how one finds the gap.

::: {.warning}
The box of \( \rulename{{\to}I} \) opens with the **hypothesis** of the implication to be proved, never with its conclusion. Argument B of Section 1.1 had to prove \( Q \to P \), with \( Q \): "\( n^2 \) is even" and \( P \): "\( n \) is even". It opened its box with \( P \), the conclusion, and reached \( Q \). Every line inside the box is correct, but a box from \( P \) to \( Q \) gives \( P \to Q \), the converse, and B's last sentence cited it for \( Q \to P \).
:::

## Derivations, precisely

We have been drawing boxes by example. Before relying on them we need to say exactly what is allowed. If a proof could say "suppose \( x > 2 \)" and later simply assert "\( x > 2 \)" as a fact, it could prove that every real number exceeds \( 2 \). So the precise definition is mostly about which earlier lines a new line may use.

*A derivation is a list of lines in which every line is a premise, an assumption that opens a box, or the result of one rule applied to lines that are still available.*

::: {#def-derivation}
[Derivation]

A **derivation** is a finite list of numbered lines, each carrying one statement and a justification, together with a set of **boxes**. A box is a block of consecutive lines whose first line is an assumption, and any two boxes are either disjoint or **one inside the other**. A box ends at one of its lines and is **closed** after it; the **last line** of a derivation lies outside every box.

**The scope rule.** Line \( i \) is **available** at line \( k \) if \( i < k \) and **every** box containing line \( i \) also contains line \( k \). A box is **available** at line \( k \) if it ends before line \( k \) and the boxes containing it are **exactly** the boxes containing line \( k \). A line may cite only lines and boxes available at it.

Every line is exactly one of the following:

::: {.enumerate options="label=(D\arabic*)"}
1. a **premise**, which stands above every box;
2. an **assumption**, which may be **any** statement, and opens a new box;
3. a **repetition** of the statement on a line available at this one;
4. the conclusion of **one** rule, applied to lines and boxes available at this one.
:::
:::

In words. (D1) Premises are the givens, and they hold throughout. (D2) We may assume anything we like, but the assumption opens a box, and that is the price. (D3) A statement already established, and still in force, may be written again; this is needed to put a statement where a rule wants it, and its justification is "R" followed by the line repeated. (D4) Everything else is one step of one rule.

The scope rule is the definition's real content. Line \( i \) is available at line \( k \) when every assumption that line \( i \) was derived under is still in force at line \( k \). A line outside all boxes is available everywhere below it. A line inside a box is available further down that box, and inside boxes opened within it, but not after the box closes. A closed box, cited as a whole by a rule such as \( \rulename{{\to}I} \), must sit directly in the part of the derivation where the citing line is: the citing line may not lie outside a box that contains the cited box (that box has closed), nor inside a further box opened after the cited box ended.

Two more words will be needed in Chapter 2, where the rules are proved trustworthy. The **length** of a derivation is its number of lines. The **context** of a line is the list of the premises together with the assumptions of every box containing that line: the statements the line depends on. The last column of the table in the next subsection lists the contexts in a derivation. The context of the last line is always just the premises, since the last line lies in no box.

With derivations defined, we can say what it means for a statement to follow from others.

::: {#def-derivable}
[Derivable]

Let \( \Gamma \) be a list of statements and \( P \) a statement. We say \( P \) is **derivable** from \( \Gamma \), and write
\[
\Gamma \vdash P ,
\]
if there is a derivation whose premises all belong to \( \Gamma \) and whose last line is \( P \). We write \( P_1, \dots, P_n \vdash P \) when \( \Gamma \) consists of \( P_1, \dots, P_n \), and \( \vdash P \) when \( \Gamma \) is empty.
:::

This makes the sequent of @def-sequent exact: the claim \( P_1, \dots, P_n \vdash Q \) holds exactly when some derivation has its premises among \( P_1, \dots, P_n \) and its last line \( Q \). A derivation need not use every statement in \( \Gamma \), and it proves the claim by existing. Because \( P \), \( Q \), \( R \) stand for arbitrary statements, a derivation written with letters proves infinitely many sequents at once, one for each way of putting statements in for the letters; Chapter 2 makes this precise.

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
3. The derivation of \( Q \wedge P \) from \( P \wedge Q \) shown after @def-rules-conjunction.
:::
:::

::: {.solution}
(a) Yes. Its only line is a premise (D1), and it is the last line, outside every box. It shows \( P \vdash P \): every statement is derivable from itself.

(b) Yes. Line 1 is an assumption (D2) and opens a box consisting of line 1 alone, whose last line is \( P \). So \( \rulename{{\to}I} \) may write \( P \to P \), citing the box, which ends before line 2 and, like line 2, lies in no other box. There are no premises, so this shows \( \vdash P \to P \): a statement derivable from nothing at all.

(c) Yes. Line 1 is a premise (D1). Lines 2, 3 and 4 each apply one rule (D4) to lines that lie in no box, and a line in no box is available at every later line. The last line lies in no box. It shows \( P \wedge Q \vdash Q \wedge P \).
:::

The single-line box of (b) is the degenerate case, and it is legal: nothing in \( \rulename{{\to}I} \) asks the box to contain more than its assumption.

Now change the derivation of \( P \to R \) by one line, as a careless writer might.

```{=latex}
\begin{center}
% expect-invalid: a deliberately flawed derivation (line 7 repeats a line of a closed box)
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

Lines 1–6 are as before, and line 7 claims to be a repetition (D3). It is illegal. Line 5 lies inside the box \( \lines{3}{5} \), which does not contain line 7, so line 5 is not available at line 7. If the line were allowed, the derivation would show \( P \to Q, \ Q \to R \vdash R \), and that would be a disaster: with \( x \) a real number, take \( P \): "\( x > 3 \)", \( Q \): "\( x > 2 \)" and \( R \): "\( x > 1 \)". Both premises are true whatever \( x \) is, and at \( x = 0 \) the conclusion is false.

::: {.warning}
The assumption of a closed box is gone, and so is everything derived from it. Here is a typical slip. *"Suppose \( x > 1 \). Then \( x^2 = x \cdot x > 1 \cdot x > 1 \). Hence \( x > 1 \) implies \( x^2 > 1 \). Moreover \( x^3 = x \cdot x^2 > 1 \), so \( x^3 > 1 \)."* The sentence "Hence …" closed the box; the last sentence still uses \( x > 1 \), and so it asserts \( x^3 > 1 \) with no hypothesis, which fails at \( x = 0 \). The repair is to keep the box open until everything that needs \( x > 1 \) is done, and conclude "if \( x > 1 \), then \( x^2 > 1 \) and \( x^3 > 1 \)".
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
Lines 3, 4 and 5. They lie in the box \( \lines{2}{5} \), the only box containing line 2, so line 2 is available to each of them. Line 6 cites the box \( \lines{2}{5} \) as a whole, which is what \( \rulename{{\to}I} \) requires; it does not cite line 2 by itself, and could not, since line 6 is outside the box. Line 7 may not cite line 2 either, for the same reason.
:::

## How to check a derivation

Finding a derivation can take an idea; checking one never does. For each line after the premises, ask three questions.

1. **Which rule?** Name it, and check that the line has the shape the rule produces: \( \rulename{{\to}E} \) produces the conclusion of the implication it cites, \( \rulename{{\to}I} \) an implication from the box's assumption to the box's last line.
2. **Which lines or boxes does it cite?** They must be the ones the rule asks for, of the right shapes: \( \rulename{{\to}E} \) cites an implication and its hypothesis, \( \rulename{{\to}I} \) one box.
3. **Are they available here?** Apply the scope rule of @def-derivation to each cited line and box.

A line that passes all three is correct, whatever it says. Here is the check run on the derivation of \( P \to R \) from \( P \to Q \) and \( Q \to R \), with the context of each line in the last column.

| Line | Which rule? | Cites | Available? | Context |
|---|---|---|---|---|
| 1, 2 | premises (D1) | — | — | \( P \to Q \), \( Q \to R \) |
| 3 | assumption (D2); opens the box 3–5 | — | — | \( P \to Q \), \( Q \to R \), \( P \) |
| 4 | \( \rulename{{\to}E} \): \( Q \) from \( P \to Q \) and \( P \) | 1, 3 | 1 is in no box; 3 is in box 3–5, which contains 4 | \( P \to Q \), \( Q \to R \), \( P \) |
| 5 | \( \rulename{{\to}E} \): \( R \) from \( Q \to R \) and \( Q \) | 2, 4 | 2 is in no box; 4 is in box 3–5, which contains 5 | \( P \to Q \), \( Q \to R \), \( P \) |
| 6 | \( \rulename{{\to}I} \): \( P \to R \) from the box | box 3–5 | the box ended at 5; neither it nor 6 lies in another box | \( P \to Q \), \( Q \to R \) |

Every line passes, and the last line lies in no box.

## The first results

We record the first derived results. Each proof exhibits a derivation.

::: {#prp-and-commutes}
[Conjunction Commutes]

\( P \wedge Q \vdash Q \wedge P \).
:::

::: {.proof}
The derivation shown after @def-rules-conjunction is a derivation by @exm-derivations (c); its only premise is \( P \wedge Q \) and its last line is \( Q \wedge P \). This proves the proposition.
:::

::: {#prp-implication-transitive}
[Implication Is Transitive]

\( P \to Q, \ Q \to R \vdash P \to R \).
:::

::: {.proof}
The derivation of \( P \to R \) shown after @def-rules-implication has premises \( P \to Q \) and \( Q \to R \), and its last line is \( P \to R \). It was checked line by line against @def-derivation in the table above. This proves the proposition.
:::

The next result explains a habit of mathematical writing. A theorem with two hypotheses, "if \( x > 0 \) and \( y > 0 \), then \( xy > 0 \)", is often written with one hypothesis at a time: "let \( x > 0 \); then, if \( y > 0 \), \( xy > 0 \)". The two forms are \( (P \wedge Q) \to R \) and \( P \to (Q \to R) \), and each can be derived from the other.

::: {#prp-curry}
[Two Hypotheses or One at a Time]

\( (P \wedge Q) \to R \vdash P \to (Q \to R) \), and \( P \to (Q \to R) \vdash (P \wedge Q) \to R \).
:::

::: {.idea}
Read each goal's main connective. For \( P \to (Q \to R) \) it is \( \to \), so open a box with \( P \); the new goal \( Q \to R \) is again an implication, so open a box with \( Q \) inside the first. With both assumptions available, \( P \wedge Q \) is one application of \( \rulename{\wedge I} \) away, and the premise finishes. For the converse, the goal \( (P \wedge Q) \to R \) asks for one box, with \( P \wedge Q \); take the assumption apart and feed the halves to the premise one at a time.
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

Line 4 may cite line 2 because the only box containing line 2, the box \( \lines{2}{6} \), also contains line 4. Line 6 may cite the box \( \lines{3}{5} \) because both lie in the box \( \lines{2}{6} \) and in no other.

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

By @def-derivable, the two derivations prove the two claims.
:::

In the first derivation the boxes are nested, and the inner one closes first: an assumption made later is discharged earlier. That is the general pattern, forced by @def-derivation, since two boxes are either disjoint or one inside the other. Section 1.5 gives a name to a pair of statements that, like these two, can each be derived from the other.

The same nesting proves that the order of two hypotheses does not matter: \( P \to (Q \to R) \vdash Q \to (P \to R) \). The goal asks for a box with \( Q \) and, inside it, a box with \( P \).

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

For real numbers \( a \) and \( x \), this derivation turns "if \( a > 0 \), then (if \( x > 1 \), then \( ax > a \))" into "if \( x > 1 \), then (if \( a > 0 \), then \( ax > a \))".

Repetition (D3) is for a rule that needs a statement as a line of a particular box when it stands only outside it. The shortest example is \( \vdash P \to (Q \to P) \).

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

The goal asks for a box with \( P \) and, inside it, a box with \( Q \) whose last line is \( P \). The statement \( P \) is available inside that box, on line 1, but \( \rulename{{\to}I} \) wants it as a line **of the box \( \lines{2}{3} \) itself**. Line 3 puts it there, legally, because the only box containing line 1 also contains line 3. The assumption \( Q \) is never used, and nothing in \( \rulename{{\to}I} \) requires it to be: an implication whose conclusion is already known holds whatever its hypothesis.

::: {.check}
To show \( P \to (Q \wedge R) \vdash (P \to Q) \wedge (P \to R) \), does the derivation need one box or two?
:::

::: {.solution}
Two. The goal's main connective is \( \wedge \), which opens no box, so the goal splits into the two implications \( P \to Q \) and \( P \to R \). Each is proved by \( \rulename{{\to}I} \), with its own box opened by \( P \): inside it, \( \rulename{{\to}E} \) on the premise gives \( Q \wedge R \), and \( \rulename{\wedge E} \) gives the half that box needs.
:::

Every derivation in this section was built from the rules alone. Section 1.4 lets a sequent already proved be used as a single line of a later derivation; until then, a derivation that needs a result proved earlier must repeat its steps.

## What the rules sound like

Every rule is something mathematicians already say. The table pairs each rule of this section with the sentence that uses it in a written proof and, for readers who meet a proof assistant, with the Lean code that performs it (`h.1` names the left half of `h`). Nothing later depends on the last column.

| Rule | You write | Lean |
|------|--------------------------------------|------------------------|
| \( \rulename{\wedge I} \) | "We show \( P \), and we show \( Q \)." | `constructor` |
| \( \rulename{\wedge E} \) | "In particular, \( P \)." | `h.1` (and `h.2`) |
| \( \rulename{{\to}I} \) | "Assume \( P \). … Hence \( Q \)." | `intro hp` |
| \( \rulename{{\to}E} \) | "Since \( P \) implies \( Q \), and \( P \) holds, \( Q \)." | `exact h hp` |

The sentence for \( \rulename{{\to}I} \) is the one to watch. "Assume \( P \)" opens a box, and "hence \( Q \)" is its last line. The conclusion "\( P \) implies \( Q \)" is often left unsaid, so the closing line is invisible on the page; it is still there, and it is the line Argument B gets wrong. Chapter 4 extends the table to every rule and turns it into a dictionary between derivations and prose.

## Exercises

### A. Check your understanding

::: {#exr-conjunction-implication-derivations-a1}
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
3. Which of lines 1–5 are available at line 6? What is the context of line 5?
4. True or false, with a reason: line 5 could equally be justified as \( \rulename{{\to}E} \) 1, 2.
5. What does the derivation show, written with \( \vdash \)?
6. Someone extends the derivation by a line 7, the statement \( R \) justified by \( \rulename{{\to}E} \) 6, 3. Is the result a derivation? If not, name the clause of @def-derivation that line 7 breaks.
:::
:::

::: {.solution}
(a) \( \rulename{{\to}I} \): if a box opened by the assumption \( P \) has \( Q \) as its last line, a line of the box itself, we may close the box and write \( P \to Q \) after it. \( \rulename{{\to}E} \): from \( P \to Q \) and \( P \) on available lines, we may write \( Q \) (@def-rules-implication).

(b) The justifications are (i) \( \rulename{{\to}E} \) 1, 3; (ii) \( \rulename{{\to}E} \) 4, 2; (iii) \( \rulename{{\to}I} \) \( \lines{3}{5} \).

(c) Lines 1 and 2. Lines 3, 4 and 5 lie in the box \( \lines{3}{5} \), which does not contain line 6. (The box \( \lines{3}{5} \) as a whole is available at line 6, which is why (iii) may cite it.) The context of line 5 is \( P \to (Q \to R) \), \( Q \), \( P \): the two premises and the assumption of the one box containing it.

(d) False. \( \rulename{{\to}E} \) needs an implication and its hypothesis. Line 1 is \( P \to (Q \to R) \), whose hypothesis is \( P \), not \( Q \); applied to lines 1 and 2 the rule does not apply at all.

(e) \( P \to (Q \to R), \ Q \vdash P \to R \).

(f) No. Line 6 is available at line 7, but line 3 is not: it lies in the box \( \lines{3}{5} \), which does not contain line 7. So line 7 applies a rule to a line that is not available, which (D4) forbids.
:::

### B. Practice

::: {#exr-conjunction-implication-derivations-b1}
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

::: {#exr-conjunction-implication-derivations-b2}
[B2: An assumption that is not used]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( Q \vdash P \to Q \), and say which line needs repetition.
2. Show that \( \vdash (P \wedge Q) \to (R \to Q) \).
3. Let \( x \) be a real number. Write the instance of (a) with \( Q \): "\( x^2 \ge 0 \)" and \( P \): "\( x > 5 \)" as an English sentence, and say which hypothesis its proof never uses.
:::
:::

::: {.solution}
(a) The goal is an implication, so open a box with \( P \); its last line must be \( Q \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {Q}
  \open
  \hypo {2} {P}
  \have {3} {Q} \r{1}
  \close
  \have {4} {P \to Q} \ii{2-3}
\end{nd}$
\end{center}
```

Line 3 needs repetition: \( \rulename{{\to}I} \) wants \( Q \) as a line of the box \( \lines{2}{3} \) itself. It is legal because line 1 lies in no box.

(b) Two implications, so two nested boxes: one with \( P \wedge Q \), and inside it one with \( R \).

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {P \wedge Q}
  \have {2} {Q} \ae{1}
  \open
  \hypo {3} {R}
  \have {4} {Q} \r{2}
  \close
  \have {5} {R \to Q} \ii{3-4}
  \close
  \have {6} {(P \wedge Q) \to (R \to Q)} \ii{1-5}
\end{nd}$
\end{center}
```

Line 4 is legal: the only box containing line 2 also contains line 4. (Applying \( \rulename{\wedge E} \) to line 1 inside the inner box works as well.)

(c) "\( x^2 \ge 0 \); therefore, if \( x > 5 \), then \( x^2 \ge 0 \)". The hypothesis \( x > 5 \) is never used: its box only repeats what was known.
:::

::: {#exr-conjunction-implication-derivations-b3}
[B3: Unwinding an absolute value]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( P \to Q, \ P \to R \vdash P \to (Q \wedge R) \).
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

(b) Take \( P \): "\( \abs{x - 2} < 1 \)", \( Q \): "\( x > 1 \)" and \( R \): "\( x < 3 \)". The two facts are the premises \( P \to Q \) and \( P \to R \), and \( Q \wedge R \) is \( 1 < x < 3 \). The derivation in (a), with these statements put in for the letters, is a derivation of \( P \to (Q \wedge R) \) from the two facts.

In prose: *Suppose \( \abs{x - 2} < 1 \). Then \( x > 1 \) by the first fact, and \( x < 3 \) by the second. Hence \( 1 < x < 3 \). This proves that \( \abs{x - 2} < 1 \) implies \( 1 < x < 3 \).*
:::

### C. Going deeper

::: {#exr-conjunction-implication-derivations-c1}
[C1: A line from a closed box]

A student wants to show \( (P \wedge Q) \to R \vdash (P \to (Q \to R)) \wedge (Q \to (P \to R)) \), and offers the following derivation. Lines 1–7 are the first derivation in the proof of @prp-curry.

```{=latex}
\begin{center}
% expect-invalid: a deliberately flawed derivation (line 10 repeats a line of a closed box)
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
  \open
  \hypo {8} {Q}
  \open
  \hypo {9} {P}
  \have {10} {R} \r{5}
  \close
  \have {11} {P \to R} \ii{9-10}
  \close
  \have {12} {Q \to (P \to R)} \ii{8-11}
  \have {13} {(P \to (Q \to R)) \wedge (Q \to (P \to R))} \ai{7,12}
\end{nd}$
\end{center}
```

::: {.enumerate options="label=(\alph*)"}
1. Find the first illegal line, and name the clause of @def-derivation that it breaks.
2. Is the student's conclusion derivable from the premise? Justify your answer.
3. The student defends line 10: "at line 10, both \( P \) and \( Q \) are assumed, exactly as they were at line 5, so \( R \) holds there too." Explain why @def-derivation does not accept this defense, and show by an instance with real numbers that the move "repeat a line of a closed box" cannot be allowed.
:::
:::

::: {.solution}
[Hint 1]

For (a), check each line's citations against the scope rule; for (b), keep the student's idea and change one step.
:::

::: {.solution}
[Hint 2]

For (b), inside the box of \( P \) at line 9, the assumptions \( Q \) (line 8) and \( P \) (line 9) are both available. What did lines 4 and 5 do with such a pair?
:::

::: {.solution}
(a) Line 10 is the first illegal line. It claims to repeat line 5 by (D3), but line 5 lies in the boxes \( \lines{2}{6} \) and \( \lines{3}{5} \), and neither contains line 10. So line 5 is not available at line 10, and (D3) allows repeating only an available line. Lines 1–9 are correct, and lines 11–13 would be correct if line 10 were.

(b) Yes: the sequent holds. Replace line 10 by two lines that do inside the new boxes what lines 4 and 5 did inside the old ones.

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
  \open
  \hypo {8} {Q}
  \open
  \hypo {9} {P}
  \have {10} {P \wedge Q} \ai{9,8}
  \have {11} {R} \ie{1,10}
  \close
  \have {12} {P \to R} \ii{9-11}
  \close
  \have {13} {Q \to (P \to R)} \ii{8-12}
  \have {14} {(P \to (Q \to R)) \wedge (Q \to (P \to R))} \ai{7,13}
\end{nd}$
\end{center}
```

Every box containing line 8 or line 9 contains line 10, and line 1 lies in no box; the other lines check as before. The student's derivation was wrong and its conclusion right: a flawed argument can have a true conclusion.

(c) Availability is about **boxes**, not about which statements happen to be assumed. The boxes \( \lines{8}{11} \) and \( \lines{9}{10} \) are new; that their assumptions repeat those of the old boxes gives line 10 no access to what was derived inside them. And the move, once allowed, can be used anywhere. Used outside every box, as a line 8 "\( R \), R 5" after lines 1–7, it would derive \( (P \wedge Q) \to R \vdash R \). Let \( x \) be a real number, and take \( P \): "\( x > 2 \)", \( Q \): "\( x > 3 \)" and \( R \): "\( x > 1 \)". The premise "if \( x > 2 \) and \( x > 3 \), then \( x > 1 \)" is true whatever \( x \) is, and at \( x = 0 \) the conclusion \( x > 1 \) is false. A move that leads from a true premise to a false conclusion cannot be a step of proof.

**Marking scheme.** (10 points)

- 3: names line 10, because line 5 lies in boxes that do not contain it.
- 3: gives any correct derivation of the sequent, every citation available.
- 1: says the conclusion is derivable although the argument is wrong.
- 3: explains that availability depends on boxes, not on repeated assumptions, with an instance where the move leads from a true premise to a false conclusion.

Fatal errors (0 for the step): naming line 5 or line 9; claiming the sequent is not derivable; refuting the conclusion instead of the move.
:::

::: {#exr-conjunction-implication-derivations-c2}
[C2: A hypothesis inside a hypothesis]

Show that \( (P \to Q) \to (P \to R) \vdash P \to (Q \to R) \). Then say, in one sentence, why the premise cannot be used until a third box is opened.
:::

::: {.solution}
[Hint 1]

Read the boxes off the goal. The premise's hypothesis is \( P \to Q \): what would you need to derive it?
:::

::: {.solution}
[Hint 2]

Inside the boxes of \( P \) and \( Q \), the hypothesis \( P \to Q \) is itself an implication. Which rule proves an implication, and what does that rule need?
:::

::: {.solution}
The goal \( P \to (Q \to R) \) asks for a box with \( P \) and, inside it, a box with \( Q \) whose last line is \( R \). The premise gives \( P \to R \) as soon as we have \( P \to Q \), and \( P \to R \) with the available \( P \) gives \( R \). So the task is to derive \( P \to Q \) inside the box of \( Q \), and that takes a third box.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \to Q) \to (P \to R)}
  \open
  \hypo {2} {P}
  \open
  \hypo {3} {Q}
  \open
  \hypo {4} {P}
  \have {5} {Q} \r{3}
  \close
  \have {6} {P \to Q} \ii{4-5}
  \have {7} {P \to R} \ie{1,6}
  \have {8} {R} \ie{7,2}
  \close
  \have {9} {Q \to R} \ii{3-8}
  \close
  \have {10} {P \to (Q \to R)} \ii{2-9}
\end{nd}$
\end{center}
```

Line 5 is a legal repetition: both boxes containing line 3 contain line 5. Line 8 may cite line 2 because the box \( \lines{2}{9} \) contains line 8.

The premise's hypothesis is the implication \( P \to Q \), which \( \rulename{{\to}E} \) needs on an available line, and an implication is derived by \( \rulename{{\to}I} \), which needs a box of its own. (That box assumes \( P \) again although line 2 already did: \( \rulename{{\to}I} \) needs the box, not new information.)

**Marking scheme.** (10 points)

- 2: opens a box with \( P \) and inside it a box with \( Q \), read off the goal.
- 3: derives \( P \to Q \) inside the box of \( Q \) by a box whose last line is \( Q \).
- 2: obtains \( P \to R \), then \( R \), by \( \rulename{{\to}E} \) on available lines.
- 2: closes the boxes inner first, each \( \rulename{{\to}I} \) citing an available box.
- 1: the sentence says \( P \to Q \) must be a line, hence needs a box.

Fatal errors (0 for the step): citing a line outside the box that contains it; writing \( P \to Q \) with no box.
:::

<!-- dependency ledger
exm-product-in-unit-interval (solution): a product of positive reals is positive; multiplying an inequality by a positive number keeps it; transitivity of < | school algebra, allowed as a fact by the Chapter 1 blueprint (Allowed prerequisites); marked "school algebra, not logic" in the text
def-rules-implication (example): if x > 3 then x^2 > 9 (x > 0, x^2 = x*x > 3x > 9); 4 < 9 and transitivity of <; sqrt(2) < 1.5 < 2 | school algebra (Allowed prerequisites); checked by verify/ch01/def-rules-implication.py
def-rules-implication (example): x > 2 implies x^2 > 4 (the hook paragraph) | school algebra (Allowed prerequisites), argued inline
def-derivation (example): the flawed derivation's instance: x > 3 implies x > 2, x > 2 implies x > 1, and 0 > 1 is false | school algebra; checked by verify/ch01/def-rules-implication.py
def-derivation (example): the warning's x^3 > 1 fails at x = 0; x > 1 implies x^2 > 1 | school algebra; checked by verify/ch01/def-rules-implication.py
exr-conjunction-implication-derivations-c1 (solution): (x > 2 and x > 3) implies x > 1 for every real x, and 0 > 1 is false | school algebra; checked by verify/ch01/exr-conjunction-implication-derivations-c1.py
prp-curry (example): if a > 0 and x > 1 then ax > a | school algebra (Allowed prerequisites); stated as the instance's content, not used in a proof
-->
