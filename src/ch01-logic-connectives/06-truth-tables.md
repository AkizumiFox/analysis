# Truth Tables Summarize the Rules

Most first courses in logic open with truth tables, and the row "if \( P \) is false, then \( P \to Q \) is true" then looks like an arbitrary convention. This chapter has gone the other way. Each connective was defined by what it takes to prove it and what we may do with it, and we have used those rules on real mathematics. This section derives the truth tables **from** the rules, so that every row, the strange one included, has a reason. It then turns the tables into a tool: a quick test that can show an argument form to be invalid, with a single row as the witness.

## Reading a table off the rules

Recall from @def-statement that a statement is true or false. When a statement is built from simpler ones by connectives, its truth should depend only on the truth of the pieces. A truth table records that dependence, one **row** for each way of assigning "true" (T) or "false" (F) to the pieces.

*A truth table is what the rules say when every piece is either known to be true or known to be false.*

The dictionary between rows and rules is this. Fix a row. Each letter the row marks T is available as a premise; for each letter the row marks F, its negation is available as a premise. Call these the **premises of the row**. The table marks a compound statement T in that row when the rules derive it from the premises of the row, and F when they derive its negation. We now read off the five connectives, one row at a time. Throughout, the rows are listed in the same order: TT, TF, FT, FF.

**Conjunction.** In the row where \( P \) and \( Q \) are both T, both are premises, so \( \rulename{\wedge I} \) derives \( P \wedge Q \) (@def-rules-conjunction). In every other row one of them, say \( P \), is F, so \( \neg P \) is a premise. Then \( P \wedge Q \) cannot be T there: if we assume \( P \wedge Q \), \( \rulename{\wedge E} \) gives \( P \), which clashes with \( \neg P \) by \( \rulename{\neg E} \), and \( \rulename{\neg I} \) closes the box with \( \neg(P \wedge Q) \). So the column is T, F, F, F.

**Implication.** This is the row that looked arbitrary.

- In row TF, the premises are \( P \) and \( \neg Q \). If \( P \to Q \) were assumed, \( \rulename{{\to}E} \) with \( P \) would give \( Q \), which clashes with \( \neg Q \). So \( \rulename{\neg I} \) gives \( \neg(P \to Q) \), and the entry is F. This is the one row in which a promise is tested and broken.
- In rows TT and FT, \( Q \) is a premise. Open a box with \( P \); since \( Q \) is available inside the box, the box reaches \( Q \), and \( \rulename{{\to}I} \) closes it with \( P \to Q \). The entry is T.
- In rows FT and FF, \( \neg P \) is a premise, and @prp-vacuous-implication gives \( \neg P \vdash P \to Q \). The entry is T.

So the column is T, F, T, T. The last two rows, the "vacuous" ones, are not a convention: they are \( \rulename{\bot E} \) at work. Inside a box that assumes \( P \) while \( \neg P \) is available, we reach \( \bot \), and from \( \bot \) we may write \( Q \).

**Negation.** In the row where \( P \) is F, the premise of the row is \( \neg P \) itself, so the entry is T. In the row where \( P \) is T, the premise is \( P \), and @prp-double-negation (a) derives \( \neg\neg P \) from it, so the entry is F. The statement \( \bot \) stands for a contradiction, and it gets the value F in every row. So \( \rulename{\neg I} \) and \( \rulename{\neg E} \) behave in the table exactly like \( \rulename{{\to}I} \) and \( \rulename{{\to}E} \) with \( \bot \) in the place of \( Q \): the column of \( \neg P \) is the column of \( P \to \bot \).

**Disjunction.** In rows TT, TF and FT, at least one of \( P \), \( Q \) is a premise, and \( \rulename{\vee I} \) derives \( P \vee Q \) (@def-rules-disjunction). In row FF, both \( \neg P \) and \( \neg Q \) are premises, and @prp-de-morgan (b) derives \( \neg(P \vee Q) \) from them. So the column is T, T, T, F. The mathematical "or" is **inclusive**, and the table shows it in row TT.

**Biconditional.** By @def-rules-biconditional, \( \rulename{{\leftrightarrow}I} \) needs two boxes, one from \( P \) to \( Q \) and one from \( Q \) to \( P \). In row TT each box reaches its goal because the goal is a premise. In row FF each box reaches \( \bot \) at once (its assumption clashes with a premise) and then its goal by \( \rulename{\bot E} \). So the entry is T in both. In rows TF and FT, assuming \( P \leftrightarrow Q \) and applying \( \rulename{{\leftrightarrow}E} \) to whichever side is true gives the other side, which clashes with its negation; \( \rulename{\neg I} \) then gives \( \neg(P \leftrightarrow Q) \). So the column is T, F, F, T.

::: {#def-truth-table}
[Truth tables]

A **row** for a list of statement letters is an assignment of T or F to each letter. A list of \( n \) letters has \( 2^n \) rows. The connectives take the following values in each row:

\[
\begin{array}{cc|ccccc}
P & Q & \neg P & P \wedge Q & P \vee Q & P \to Q & P \leftrightarrow Q \\
\hline
\mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{F} \\
\mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} \\
\mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T}
\end{array}
\]

The statement \( \bot \) is F in every row. The **value** of a compound statement in a row is found by working from the inside out, using this table at each connective. Its **truth table** lists its value in every row.
:::

In words: to evaluate a statement in a row, first evaluate the letters (the row tells you), then each connective whose pieces are already evaluated, until you reach the main connective. The main connective's column is the statement's truth table.

::: {#exm-truth-table-modus-ponens}
[A table built column by column]

Find the truth table of \( (P \wedge (P \to Q)) \to Q \).
:::

::: {.solution}
The main connective is the second \( \to \). Its left side is \( P \wedge (P \to Q) \), so we need the column of \( P \to Q \) first:

\[
\begin{array}{cc|ccc}
P & Q & P \to Q & P \wedge (P \to Q) & (P \wedge (P \to Q)) \to Q \\
\hline
\mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{T} \\
\mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{T} \\
\mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{T}
\end{array}
\]

The last column is T in every row. The statement is the rule \( \rulename{{\to}E} \) written as a single implication, and the table confirms that it cannot fail.
:::

## Tautologies and equivalence

The last column of that example is special: it does not depend on the row. Statements with this property are the propositional laws, the ones that hold whatever their letters mean.

::: {#def-tautology}
[Tautology, contradiction, equivalence]

A statement built from letters by connectives is a **tautology** if its value is T in **every** row, and a **contradiction** if its value is F in every row. Two such statements \( A \) and \( B \) are **equivalent** if they have the same value in **every** row of the letters that occur in either of them.
:::

In words: a tautology cannot be made false by any choice of truth values for its letters; a contradiction cannot be made true. Two statements are equivalent when no row tells them apart. Comparing the columns of \( A \), \( B \) and \( A \leftrightarrow B \) shows that \( A \) and \( B \) are equivalent exactly when \( A \leftrightarrow B \) is a tautology, since the \( \leftrightarrow \) column is T precisely in the rows where the two values agree.

**Examples.**

- The smallest tautology is \( P \to P \). It has one letter, so two rows, and in each the two sides agree, so the \( \to \) column is T, T. It matters because it is the table's version of the one-line box: open a box with \( P \); it already ends with \( P \); close it by \( \rulename{{\to}I} \).
- \( P \vee \neg P \) is a tautology: in row T the left disjunct is T, and in row F the right one is. This is @prp-excluded-middle seen through the table.
- \( P \wedge \neg P \) is a contradiction: in each row one conjunct is F. So is \( P \leftrightarrow \neg P \).
- \( P \) and \( \neg\neg P \) are equivalent: negating twice returns the original column. Compare @prp-double-negation.

**Non-example by minimal change.** Swap \( P \) and \( Q \) in the outer positions of @exm-truth-table-modus-ponens to get \( (Q \wedge (P \to Q)) \to P \). The rows TT, TF and FF still give T. Row FT fails: there \( Q \) and \( P \to Q \) are both T, so the left side is T, while \( P \) is F. So the statement is not a tautology, and row FT is the witness. We meet this statement again below under its traditional name.

The standard equivalences of mathematical writing are now a matter of checking columns.

::: {#prp-standard-equivalences}
[Standard Equivalences]

For all statements \( P \), \( Q \) and \( R \), the following pairs are equivalent:

::: {.enumerate options="label=(\alph*)"}
1. \( P \to Q \) and \( \neg Q \to \neg P \) (contrapositive);
2. \( \neg(P \wedge Q) \) and \( \neg P \vee \neg Q \) (De Morgan);
3. \( \neg(P \vee Q) \) and \( \neg P \wedge \neg Q \) (De Morgan);
4. \( P \wedge (Q \vee R) \) and \( (P \wedge Q) \vee (P \wedge R) \) (distributivity);
5. \( P \to Q \) and \( \neg P \vee Q \).
:::
:::

::: {.proof}
For (a), (b), (c) and (e) we compute the columns over the four rows of \( P \), \( Q \):

\[
\begin{array}{cc|ccc}
P & Q & P \to Q & \neg Q \to \neg P & \neg P \vee Q \\
\hline
\mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} \\
\mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T}
\end{array}
\]

and

\[
\begin{array}{cc|cccc}
P & Q & \neg(P \wedge Q) & \neg P \vee \neg Q & \neg(P \vee Q) & \neg P \wedge \neg Q \\
\hline
\mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} \\
\mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} \\
\mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} \\
\mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T}
\end{array}
\]

In the first table the last three columns agree in every row, which gives (a) and (e). In the second, the columns of \( \neg(P \wedge Q) \) and \( \neg P \vee \neg Q \) agree, which gives (b), and the last two columns agree, which gives (c). For (d) there are three letters and so eight rows:

\[
\begin{array}{ccc|ccccc}
P & Q & R & Q \vee R & P \wedge (Q \vee R) & P \wedge Q & P \wedge R & (P \wedge Q) \vee (P \wedge R) \\
\hline
\mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{T} \\
\mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{T} \\
\mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} \\
\mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} \\
\mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} \\
\mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} \\
\mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F}
\end{array}
\]

The columns of \( P \wedge (Q \vee R) \) and \( (P \wedge Q) \vee (P \wedge R) \) agree in every row. This proves all five equivalences.
:::

Each of these equivalences was, or can be, derived by the rules as well. Direction by direction, (a) is @prp-contrapositive together with @prp-contrapositive-converse, and (b) and (c) are @prp-de-morgan. The table checks all directions at once and in a few seconds, but it cannot tell us which directions needed RAA. That is information the rules carry and the table does not.

::: {.content-visible when-format="html"}
The small program below prints the truth table of any statement you type as a Python function; `imp` is \( \to \). Change the last line to check your own tables.

```{.python .run #cell-truth-table}
from itertools import product

def imp(a, b):
    return (not a) or b

def table(f, letters):
    for values in product([True, False], repeat=len(letters)):
        row = dict(zip(letters, values))
        cells = ["T" if v else "F" for v in values]
        print(*cells, "|", "T" if f(**row) else "F")

table(lambda P, Q: imp(imp(P, Q), imp(not Q, not P)), "PQ")
```
:::

## Why the table can be trusted

Why should the tables and the rules agree at all? The rules were chosen so that each one **preserves truth**.

::: {#thm-soundness}
[Soundness]

Let \( A_1, \dots, A_n \) and \( B \) be statements built from letters by connectives. If \( A_1, \dots, A_n \vdash B \), then every row in which \( A_1, \dots, A_n \) are all T is a row in which \( B \) is T.
:::

::: {.idea}
Each line of a derivation depends on the premises and on the assumptions of the boxes it sits in. The claim to check, line by line, is: *in every row where those premises and assumptions are all T, the line itself is T.* Every rule keeps this true. For \( \rulename{\wedge I} \), if \( P \) and \( Q \) are T in a row then so is \( P \wedge Q \), by the \( \wedge \) column. For \( \rulename{{\to}E} \), a row with \( P \) and \( P \to Q \) both T is row TT, so \( Q \) is T. For \( \rulename{{\to}I} \), the box says that every row making \( P \) (and the outer assumptions) T makes \( Q \) T; in the remaining rows \( P \) is F, and there \( P \to Q \) is T by its vacuous rows. For \( \rulename{\bot E} \), no row makes \( \bot \) true, so there is nothing to check. For RAA, a box from \( \neg P \) to \( \bot \) says that no row makes \( \neg P \) true along with the outer assumptions, so every such row makes \( P \) true. The remaining rules are checked in the same way.
:::

We do not write out the full proof here. It is an induction on the number of lines of a derivation, and induction is the subject of Chapter 4; the Idea above contains every case that is not a repetition of another.

What soundness gives us is a way to show that something is **not** derivable. If a row makes all the premises T and the conclusion F, no derivation of the conclusion from the premises can exist, because by @thm-soundness it would force the conclusion to be T in that row.

::: {.remark}
The converse also holds, with RAA among the rules: if every row that makes \( A_1, \dots, A_n \) true makes \( B \) true, then \( A_1, \dots, A_n \vdash B \). This is the **completeness theorem** for propositional logic, and we do not prove it. Without RAA the converse fails: \( P \vee \neg P \) is a tautology, yet, like \( P \) from \( \neg\neg P \) in §05, it cannot be derived from the other rules, a fact we do not prove here. A truth table cannot see this, because the table itself assumes that every statement is T or F, which is exactly the classical principle that RAA encodes.
:::

## Using tables to refute

The rules are the tool for **proving** that an argument is correct: a derivation is a certificate. Tables are the fast tool for the opposite job.

::: {#def-valid-argument}
[Valid argument form]

An argument form with premises \( A_1, \dots, A_n \) and conclusion \( B \) is **valid** if every row in which all of \( A_1, \dots, A_n \) are T is a row in which \( B \) is T. A row in which all the premises are T and \( B \) is F is a **refuting row**.
:::

In words: an argument form is valid when no assignment of truth values can make its premises true and its conclusion false. A single refuting row shows that the form is invalid, and by @thm-soundness, that no derivation of \( B \) from \( A_1, \dots, A_n \) exists.

The most common invalid form in mathematical writing has a traditional name.

::: {#exm-affirming-the-consequent}
[Affirming the consequent]

Show that the argument form with premises \( P \to Q \) and \( Q \), and conclusion \( P \), is invalid. Then give a mathematical instance where the premises are true and the conclusion is false.
:::

::: {.solution}
In row FT, the premise \( Q \) is T, and \( P \to Q \) is T by its third row; the conclusion \( P \) is F. So FT is a refuting row, and the form is invalid.

For an instance, let \( x = -2 \), let \( P \) be "\( x = 2 \)" and let \( Q \) be "\( x^2 = 4 \)". Then \( P \to Q \) is true (if \( x = 2 \) then \( x^2 = 4 \)), and \( Q \) is true since \( (-2)^2 = 4 \), but \( P \) is false. This is row FT in real life.
:::

This is the error behind the plausible-looking argument at the start of §01. There the goal was \( P \to Q \), with \( P \) = "\( n^2 \) is even" and \( Q \) = "\( n \) is even". The argument assumed \( Q \) and derived \( P \), so what it established was \( Q \to P \). Passing from \( Q \to P \) to \( P \to Q \) is invalid: in row TF the premise \( Q \to P \) is T and the conclusion \( P \to Q \) is F. That the statement \( P \to Q \) happens to be true for integers (it is @thm-square-even-implies-even) does not rescue the argument. A valid form never leads from true premises to a false conclusion, and this form does, as the instance with \( x = -2 \) shows once "\( x = 2 \)" and "\( x^2 = 4 \)" are put in the roles of \( Q \) and \( P \).

::: {.check}
Find a refuting row for the argument form with premises \( P \to Q \) and \( \neg P \), and conclusion \( \neg Q \). (It is called **denying the antecedent**.)
:::

::: {.solution}
Row FT. There \( P \to Q \) is T (third row of the \( \to \) column) and \( \neg P \) is T, while \( \neg Q \) is F. In the instance above: "if \( x = 2 \) then \( x^2 = 4 \)" and "\( x \ne 2 \)" are both true at \( x = -2 \), but "\( x^2 \ne 4 \)" is false.
:::

::: {.warning}
A truth table checks **propositional form** only; it cannot see inside a statement. "Every real \( x \) has \( x^2 \ge 0 \); hence \( 3^2 \ge 0 \)" is a correct argument, but to a table it is two unrelated letters \( A \) and \( B \), and the row \( A \) = T, \( B \) = F "refutes" it. So a refuting row refutes the **form**, not the argument. Arguments whose force lies in "every" and "there is", such as "for every \( \varepsilon > 0 \) there is an \( N \)", need the quantifier rules of Chapter 2, and no table can check them.
:::

## Exercises

### A. Check your understanding

::: {#exr-truth-tables-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Write out the truth table of \( \neg(P \wedge \neg Q) \). Which connective of \( P \) and \( Q \) has the same column?
2. Write out the truth table of \( (P \vee Q) \to P \). Is it a tautology?
3. Show that \( P \leftrightarrow \neg P \) is a contradiction.
4. Decide whether \( (P \to Q) \vee (Q \to P) \) is a tautology.
5. Which rule of §02–§03 is responsible for the value T of \( P \to Q \) in row FF?
:::
:::

::: {.solution}
(a) In rows TT, TF, FT, FF, the column of \( \neg Q \) is F, T, F, T; of \( P \wedge \neg Q \) it is F, T, F, F; so \( \neg(P \wedge \neg Q) \) is T, F, T, T. This is the column of \( P \to Q \).

(b) \( P \vee Q \) is T, T, T, F, and \( P \) is T, T, F, F, so \( (P \vee Q) \to P \) is T, T, F, T. It is not a tautology: row FT is F.

(c) In row T, \( P \) is T and \( \neg P \) is F; in row F, \( P \) is F and \( \neg P \) is T. The two sides differ in both rows, so the \( \leftrightarrow \) column is F, F.

(d) Yes. In rows TT, FT and FF, \( P \to Q \) is already T. In row TF, \( Q \) is F, so \( Q \to P \) is T. Either way the disjunction is T.

(e) \( \rulename{\bot E} \), through @prp-vacuous-implication: from \( \neg P \), a box assuming \( P \) reaches \( \bot \) by \( \rulename{\neg E} \), then \( Q \) by \( \rulename{\bot E} \), and \( \rulename{{\to}I} \) closes it.
:::

### B. Practice

::: {#exr-truth-tables-b1}
[B1: Valid or not]

Determine which of the following argument forms are valid. For each valid one give a derivation; for each invalid one give a refuting row.

::: {.enumerate options="label=(\alph*)"}
1. Premises \( P \to Q \), \( \neg Q \); conclusion \( \neg P \).
2. Premises \( P \vee Q \), \( P \); conclusion \( \neg Q \).
3. Premises \( P \to R \), \( Q \to R \); conclusion \( (P \vee Q) \to R \).
4. Premise \( (P \wedge Q) \to R \); conclusion \( P \to R \).
:::
:::

::: {.solution}
(a) Valid:

\[
\begin{array}{r l l}
1 & P \to Q & \text{premise} \\
2 & \neg Q & \text{premise} \\
3 & \fsc \fhyp{P} & \text{assumption} \\
4 & \fsc Q & \rulename{{\to}E}\ 1, 3 \\
5 & \fsc \bot & \rulename{\neg E}\ 4, 2 \\
6 & \neg P & \rulename{\neg I}\ \lines{3}{5}
\end{array}
\]

(b) Invalid. In row TT both premises are T and \( \neg Q \) is F. The form would be valid only if "or" were exclusive, and the mathematical \( \vee \) is not.

(c) Valid:

\[
\begin{array}{r l l}
1 & P \to R & \text{premise} \\
2 & Q \to R & \text{premise} \\
3 & \fsc \fhyp{P \vee Q} & \text{assumption} \\
4 & \fsc \fsc \fhyp{P} & \text{assumption} \\
5 & \fsc \fsc R & \rulename{{\to}E}\ 1, 4 \\
& \fsc & \\[-1.5ex]
6 & \fsc \fsc \fhyp{Q} & \text{assumption} \\
7 & \fsc \fsc R & \rulename{{\to}E}\ 2, 6 \\
8 & \fsc R & \rulename{\vee E}\ 3, \lines{4}{5}, \lines{6}{7} \\
9 & (P \vee Q) \to R & \rulename{{\to}I}\ \lines{3}{8}
\end{array}
\]

(d) Invalid. In the row \( P \) = T, \( Q \) = F, \( R \) = F, the premise is T (its left side \( P \wedge Q \) is F) and the conclusion \( P \to R \) is F.
:::

::: {#exr-truth-tables-b2}
[B2: Implication as a disjunction]

::: {.enumerate options="label=(\alph*)"}
1. Show by a truth table that \( P \to Q \) and \( \neg P \vee Q \) are equivalent.
2. Derive \( \neg P \vee Q \vdash P \to Q \) without RAA.
3. Derive \( P \to Q \vdash \neg P \vee Q \). Which rule does your derivation use that the one in (b) does not?
:::
:::

::: {.solution}
(a) In rows TT, TF, FT, FF, the column of \( \neg P \) is F, F, T, T, so \( \neg P \vee Q \) is T, F, T, T, which is the column of \( P \to Q \).

(b) The goal is an implication, so open a box with \( P \); inside it, use the disjunction by cases.

\[
\begin{array}{r l l}
1 & \neg P \vee Q & \text{premise} \\
2 & \fsc \fhyp{P} & \text{assumption} \\
3 & \fsc \fsc \fhyp{\neg P} & \text{assumption} \\
4 & \fsc \fsc \bot & \rulename{\neg E}\ 2, 3 \\
5 & \fsc \fsc Q & \rulename{\bot E}\ 4 \\
& \fsc & \\[-1.5ex]
6 & \fsc \fsc \fhyp{Q} & \text{assumption} \\
7 & \fsc Q & \rulename{\vee E}\ 1, \lines{3}{5}, \lines{6}{6} \\
8 & P \to Q & \rulename{{\to}I}\ \lines{2}{7}
\end{array}
\]

The box at line 6 has one line: it opens with \( Q \), which is already its goal.

(c) The goal is a disjunction, but we cannot tell which side holds, so we split on excluded middle:

\[
\begin{array}{r l l}
1 & P \to Q & \text{premise} \\
2 & P \vee \neg P & \text{excluded middle} \\
3 & \fsc \fhyp{P} & \text{assumption} \\
4 & \fsc Q & \rulename{{\to}E}\ 1, 3 \\
5 & \fsc \neg P \vee Q & \rulename{\vee I}\ 4 \\
& & \\[-1.5ex]
6 & \fsc \fhyp{\neg P} & \text{assumption} \\
7 & \fsc \neg P \vee Q & \rulename{\vee I}\ 6 \\
8 & \neg P \vee Q & \rulename{\vee E}\ 2, \lines{3}{5}, \lines{6}{7}
\end{array}
\]

Line 2 is @prp-excluded-middle, whose derivation uses RAA. So this direction uses RAA and the direction in (b) does not. (In fact every derivation of this direction must use RAA; we do not prove that here.)
:::

::: {#exr-truth-tables-b3}
[B3: Implication is not associative]

Determine whether \( (P \to Q) \to R \) and \( P \to (Q \to R) \) are equivalent. Justify your answer.
:::

::: {.solution}
They are not. Take the row \( P \) = F, \( Q \) = F, \( R \) = F. Then \( P \to Q \) is T, so \( (P \to Q) \to R \) is T \( \to \) F, which is F. On the other side, \( P \) is F, so \( P \to (Q \to R) \) is T by a vacuous row. The two values differ, so the statements are not equivalent. (The row \( P \) = F, \( Q \) = T, \( R \) = F is a second witness.) Hence parentheses around implications cannot be dropped.
:::

### C. Going deeper

::: {#exr-truth-tables-c1}
[C1: Two connectives are enough]

A **truth function of two variables** is any assignment of T or F to each of the four rows TT, TF, FT, FF; there are \( 2^4 = 16 \) of them. Say that a set of connectives **expresses** a truth function if some statement built from \( P \) and \( Q \) using only those connectives has that column.

::: {.enumerate options="label=(\alph*)"}
1. Using only \( \neg \) and \( \wedge \), write statements with the columns of \( P \vee Q \), \( P \to Q \) and \( P \leftrightarrow Q \).
2. Prove that \( \{\neg, \wedge\} \) expresses all 16 truth functions of two variables.
3. Is the same true of \( \{\wedge, \vee\} \)? Justify your answer.
:::

*Hint: for (b), first build, for each row, a statement that is T in that row only.*
:::

::: {.solution}
(a) By @prp-standard-equivalences (c), \( P \vee Q \) has the column of \( \neg\neg(P \vee Q) \), which is that of \( \neg(\neg P \wedge \neg Q) \). By (e) and the previous sentence, \( P \to Q \) has the column of \( \neg P \vee Q \), hence of \( \neg(P \wedge \neg Q) \) (compare Exercise A1(a)). Finally \( P \leftrightarrow Q \) is T exactly when both \( P \to Q \) and \( Q \to P \) are, so it has the column of \( \neg(P \wedge \neg Q) \wedge \neg(Q \wedge \neg P) \). Each claim can be checked row by row.

(b) For each row define a **row statement**, T in that row and F in the other three:

\[
\begin{aligned}
\text{TT}: \ & P \wedge Q, & \text{TF}: \ & P \wedge \neg Q, \\
\text{FT}: \ & \neg P \wedge Q, & \text{FF}: \ & \neg P \wedge \neg Q.
\end{aligned}
\]

Each is a conjunction, so it is T exactly in the row where both of its conjuncts are T, and that is the row named. Now let \( f \) be a truth function. If \( f \) is F in every row, the statement \( P \wedge \neg P \) has its column. Otherwise, let \( S_1, \dots, S_k \) be the row statements of the rows where \( f \) is T, with \( 1 \le k \le 4 \). The disjunction \( S_1 \vee \dots \vee S_k \) is T in a row exactly when one of the \( S_i \) is, that is, exactly in the rows where \( f \) is T. So it has the column of \( f \). It uses \( \vee \), but by (a) each \( \vee \) can be replaced by \( \neg \) and \( \wedge \) without changing any column. Hence \( \{\neg, \wedge\} \) expresses \( f \).

(c) No. We claim that every statement built from \( P \) and \( Q \) using only \( \wedge \) and \( \vee \) is T in row TT. The letters are T there, and by the table, \( \wedge \) and \( \vee \) of two T statements are T; building up from the letters, every statement stays T in row TT. So the truth function \( \neg P \), whose value in row TT is F, is not expressed.
:::

::: {#exr-truth-tables-c2}
[C2: The rows of implication are forced]

Suppose someone proposes a different table for \( \to \), changing exactly one of the two vacuous rows.

::: {.enumerate options="label=(\alph*)"}
1. Suppose row FF of \( P \to Q \) were F instead of T. Show that \( P \to P \) would then fail in some row, although \( \vdash P \to P \) is derivable.
2. Suppose instead row FT were F. Find a statement derivable with no premises that would fail in some row.
3. Explain why, given @thm-soundness, neither change is possible so long as \( \rulename{{\to}I} \) remains a rule.
:::
:::

::: {.solution}
(a) In the row where \( P \) is F, \( P \to P \) is the case "F \( \to \) F", which would be F. But \( \vdash P \to P \): open a box with \( P \); it already ends with \( P \); close it by \( \rulename{{\to}I} \).

(b) Take \( Q \to (P \to Q) \). It is derivable with no premises: open a box with \( Q \), open a box inside it with \( P \); inside both, \( Q \) is available, so the inner box reaches \( Q \), and two uses of \( \rulename{{\to}I} \) close the boxes. Under the proposed table, in the row \( P \) = F, \( Q \) = T, the inner \( P \to Q \) is "F \( \to \) T", which would be F, and then \( Q \to (P \to Q) \) is "T \( \to \) F", which is F.

(c) @thm-soundness says every statement derivable with no premises is T in every row. Each change in (a) and (b) makes a derivable statement F in some row. Both derivations use only \( \rulename{{\to}I} \), so as long as \( \rulename{{\to}I} \) is a rule, the vacuous rows must be T. The table is not a convention layered on top of the rules: the rules force it.
:::
