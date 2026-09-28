# Reading the Proof off the Goal

We now have every rule for the connectives: the introduction and elimination rules of §02–§04, and RAA from §05. This section turns them into a working method. Faced with a statement to prove, the first question is not "what do I know about the mathematics?" but "what is the main connective of the goal?", because that alone fixes the outer frame of the proof: which boxes to open and what the last line will be. We call that frame the proof's **skeleton**. The section then collects every rule in one reference table, practices translating between derivations and mathematical prose in both directions, and ends with the skill of checking someone else's proof line by line.

## The skeletons

Each introduction rule tells us how a statement of its shape is proved. Read the other way, it tells us how a proof of that shape must **start** and **end**. For example, a goal \( P \to Q \) is proved by \( \rulename{{\to}I} \), so the proof opens a box with the assumption \( P \) and must close it with \( Q \); the first sentence is "Assume \( P \)" and the last is "Hence \( Q \)". Only the middle is left to invent.

*The main connective of the goal chooses the skeleton; the skeleton gives the first and last sentences for free.*

Here are the skeletons for each shape of goal, together with the sentences that carry them in writing.

| Goal | Skeleton | First sentence | Last sentence |
|---|---|---|---|
| \( P \wedge Q \) | \( \rulename{\wedge I} \): two separate proofs | "We prove \( P \) and \( Q \) in turn." | "…so \( P \) and \( Q \)." |
| \( P \to Q \), direct | \( \rulename{{\to}I} \): box from \( P \) to \( Q \) | "Assume \( P \)." | "Hence \( Q \)." |
| \( P \to Q \), contrapositive | \( \rulename{{\to}I} \), then a box from \( \neg Q \) to \( \neg P \) | "We prove the contrapositive. Suppose not \( Q \)." | "Hence not \( P \)." |
| \( \neg P \) | \( \rulename{\neg I} \): box from \( P \) to \( \bot \) | "Suppose \( P \)." | "…a contradiction. Hence not \( P \)." |
| any \( P \), by contradiction | RAA: box from \( \neg P \) to \( \bot \) | "Suppose, for a contradiction, that not \( P \)." | "…a contradiction. Hence \( P \)." |
| \( P \vee Q \) | \( \rulename{\vee I} \): prove one side | "We show \( P \)." | "In particular, \( P \) or \( Q \)." |
| \( P \leftrightarrow Q \) | \( \rulename{{\leftrightarrow}I} \): two boxes | "\( (\Rightarrow) \) Assume \( P \)." | "\( (\Leftarrow) \) … Hence \( P \)." |

Two more skeletons are driven not by the goal but by a hypothesis:

- **Cases (\( \rulename{\vee E} \)).** If a hypothesis or a known fact has the form \( A \vee B \), prove the goal twice, once assuming \( A \) and once assuming \( B \). "We consider two cases. *Case 1:* \( A \). … *Case 2:* \( B \). … In either case, the goal holds."
- **Cases on a statement (excluded middle, then \( \rulename{\vee E} \)).** If no disjunction is at hand, @prp-excluded-middle supplies one: every statement \( A \) gives the cases \( A \) and \( \neg A \).

Three rows of the table need a comment.

**The contrapositive row.** The inner box goes from \( \neg Q \) to \( \neg P \). To reach \( Q \) from it inside the outer box that assumed \( P \), we need one more step. By @prp-contrapositive-converse, whose derivation is exactly this pattern, the step is: \( \neg P \) clashes with \( P \), and RAA closes the box that assumed \( \neg Q \). When \( Q \) is itself a negation \( \neg R \), the inner box can open with \( R \) instead and close by \( \rulename{\neg I} \), and no RAA is needed. In prose none of this shows: "We prove the contrapositive" announces the whole maneuver.

**The disjunction row.** Often neither side of \( P \vee Q \) can be proved outright; it depends on the case. Then the skeleton is: split into cases (by a known fact or by excluded middle) and use \( \rulename{\vee I} \) differently in each case. A common classical variant is "Suppose \( \neg P \); we show \( Q \)". It is justified by excluded middle: in the case \( P \), \( \rulename{\vee I} \) gives \( P \vee Q \); in the case \( \neg P \), the box proves \( Q \), and \( \rulename{\vee I} \) gives \( P \vee Q \) again.

**Nesting.** A skeleton leaves a gap, and the gap has a goal of its own. Its main connective chooses the next skeleton, inside the first. Repeat until the goal inside the innermost box is a statement with no connective (an **atomic** statement, such as "\( n \) is even" or "\( x > 0 \)"). At that point the goal gives no more help, and the work turns to the hypotheses: take them apart with the elimination rules, and bring in the mathematics.

::: {.algorithm}
To set up a proof of a goal \( G \) from hypotheses \( \Gamma \):

1. Write \( \Gamma \) at the top and \( G \) at the bottom, with a gap between.
2. If \( G \) has a main connective, open the boxes of its skeleton, write the first and last sentences, and let the gap's new goal be \( G \). Repeat this step.
3. When the goal is atomic, look at the hypotheses available in the gap. A conjunction can be split (\( \rulename{\wedge E} \)); an implication whose antecedent you have can be applied (\( \rulename{{\to}E} \)); a disjunction calls for cases (\( \rulename{\vee E} \)); a negation can be used to reach \( \bot \) (\( \rulename{\neg E} \)).
4. If you are stuck on an atomic goal and nothing applies, try RAA: assume its negation, and look for a clash.
:::

::: {#exm-skeleton-odd-product}
[Building a skeleton]

Let \( m \) and \( n \) be integers. Prove that if \( mn \) is odd, then \( m \) is odd and \( n \) is odd.
:::

::: {.solution}
*The skeleton.* The main connective is "if … then", so the outer skeleton is \( \rulename{{\to}I} \): "Assume \( mn \) is odd. … Hence \( m \) is odd and \( n \) is odd." The new goal is a conjunction, so inside the box the skeleton is \( \rulename{\wedge I} \): two separate proofs, one that \( m \) is odd and one that \( n \) is odd. Each is atomic. Nothing in the hypothesis "\( mn \) is odd" can be taken apart further, so we try the contrapositive of the claim "\( mn \) odd implies \( m \) odd", which asks for "\( m \) even implies \( mn \) even", a statement we can compute with.

*The proof.* Assume \( mn \) is odd. We show that \( m \) is odd and that \( n \) is odd.

To see that \( m \) is odd, suppose that \( m \) is not odd. Then \( m \) is even, since every integer is even or odd, say \( m = 2k \) with \( k \) an integer. Then \( mn = 2(kn) \) is even, and so it is not odd, since no integer is both. This contradicts the assumption that \( mn \) is odd. Hence \( m \) is odd.

Exchanging the roles of \( m \) and \( n \) in the previous paragraph shows that \( n \) is odd. Hence \( m \) and \( n \) are both odd.

*What the skeleton did.* It dictated the first sentence, the split into two paragraphs, and the final sentence before any mathematics was done. The only mathematical idea is the one line \( mn = 2(kn) \).
:::

::: {.check}
Name the skeleton, and write the first sentence, for a proof of each goal.

::: {.enumerate options="label=(\alph*)"}
1. For real \( x \): \( x \le \abs{x} \) and \( -x \le \abs{x} \).
2. \( \sqrt{3} \) is irrational.
3. For an integer \( n \): \( n \) is even if and only if \( n^2 \) is even.
:::
:::

::: {.solution}
(a) \( \rulename{\wedge I} \): "We prove the two inequalities in turn." (b) \( \rulename{\neg I} \), since "irrational" means "not rational": "Suppose \( \sqrt 3 \) is rational." (c) \( \rulename{{\leftrightarrow}I} \): "\( (\Rightarrow) \) Assume \( n \) is even."
:::

::: {.warning}
The skeleton is read off the **goal**, not off the hypotheses, and reading it off the wrong statement is the commonest way to prove the wrong thing. For the goal "if \( n^2 \) is even then \( n \) is even", the box must open with "\( n^2 \) is even". A proof that opens with "suppose \( n \) is even" has built the skeleton of the converse, and whatever follows cannot prove the goal. Proof B in the last part of this section is exactly this mistake.
:::

## The rules in one table

Here is every rule of this chapter, with the phrase that carries it in mathematical writing and its counterpart in the Lean proof assistant. The Lean column is for readers who know Lean or want to try it; nothing in the book depends on it.

| Rule | From | Infer | You write | Lean |
|---|---|---|---|---|
| \( \rulename{\wedge I} \) | \( P \); \( Q \) | \( P \wedge Q \) | "We show \( P \) and we show \( Q \)." | `constructor` |
| \( \rulename{\wedge E} \) | \( P \wedge Q \) | \( P \) (or \( Q \)) | "In particular, \( P \)." | `h.1`, `h.2` |
| \( \rulename{{\to}I} \) | box from \( P \) to \( Q \) | \( P \to Q \) | "Assume \( P \). … Hence \( Q \)." | `intro hp` |
| \( \rulename{{\to}E} \) | \( P \to Q \); \( P \) | \( Q \) | "Since \( P \to Q \) and \( P \) holds, \( Q \)." | `exact h hp` |
| \( \rulename{\vee I} \) | \( P \) (or \( Q \)) | \( P \vee Q \) | "Since \( P \), in particular \( P \) or \( Q \)." | `left`, `right` |
| \( \rulename{\vee E} \) | \( P \vee Q \); box from \( P \) to \( R \); box from \( Q \) to \( R \) | \( R \) | "*Case 1:* \( P \). … *Case 2:* \( Q \). … In either case, \( R \)." | `rcases h with hp \| hq` |
| \( \rulename{\neg I} \) | box from \( P \) to \( \bot \) | \( \neg P \) | "Suppose \( P \). … Contradiction. Hence not \( P \)." | `intro hp` (goal `False`) |
| \( \rulename{\neg E} \) | \( P \); \( \neg P \) | \( \bot \) | "This contradicts \( P \)." | `exact hn hp` |
| \( \rulename{\bot E} \) | \( \bot \) | any \( Q \) | "This case cannot occur." | `exfalso`, `absurd` |
| RAA | box from \( \neg P \) to \( \bot \) | \( P \) | "Suppose, for a contradiction, that not \( P \). … Hence \( P \)." | `by_contra h` |
| \( \rulename{{\leftrightarrow}I} \) | box from \( P \) to \( Q \); box from \( Q \) to \( P \) | \( P \leftrightarrow Q \) | "\( (\Rightarrow) \) … \( (\Leftarrow) \) …" | `constructor` |
| \( \rulename{{\leftrightarrow}E} \) | \( P \leftrightarrow Q \); \( P \) | \( Q \) (and conversely) | "Since \( P \) if and only if \( Q \), and \( P \) holds, \( Q \)." | `h.mp hp`, `h.mpr hq` |

Two derived patterns are used so often that they deserve rows of their own, although they are not new rules:

| Pattern | Justified by | You write | Lean |
|---|---|---|---|
| contrapositive | \( \rulename{{\to}I} \) with an inner box, @prp-contrapositive-converse | "We prove the contrapositive." | `contrapose!` (Mathlib) |
| cases on \( A \) | @prp-excluded-middle, then \( \rulename{\vee E} \) | "Either \( A \) or not \( A \)." | `by_cases h : A` |

The "You write" column is a set of models, not a script. "Therefore", "Thus", "So" and "It follows that" all mark \( \rulename{{\to}E} \); "Suppose" and "Let" and "Assume" all open boxes. What matters is that the reader can see which rule each sentence uses. That is the subject of the next part.

## From proof to rules, and back

A written proof and a derivation are two views of one argument. The derivation shows every rule and every line cited, and it is easy to check but tiring to read. The prose hides the bookkeeping, and it is pleasant to read but hides its errors just as easily. A working mathematician moves between them: reading a proof, one reconstructs the rules in one's head; writing one, one starts from a skeleton and dresses it in sentences. We practice both directions.

### Annotating a proof

::: {#exm-annotate-abs}
[Label every sentence]

Here is a short proof. Label each sentence with the rule it uses.

> **Claim.** For a real number \( x \), if \( \abs{x - 1} < 1 \) then \( x > 0 \).
>
> *Proof.* (1) Assume \( \abs{x - 1} < 1 \). (2) Either \( x \ge 1 \) or \( x < 1 \). (3) Suppose first that \( x \ge 1 \). (4) Then \( x \ge 1 > 0 \). (5) Suppose instead that \( x < 1 \). (6) Then \( x - 1 < 0 \), so \( \abs{x - 1} = 1 - x \). (7) Hence \( 1 - x < 1 \), that is, \( x > 0 \). (8) In either case \( x > 0 \), which proves the claim.
:::

::: {.solution}
| Sentence | What it does | Rule |
|---|---|---|
| (1) | opens a box with the antecedent | assumption for \( \rulename{{\to}I} \) |
| (2) | states a fact about real numbers | a known fact (school algebra), used as a line |
| (3) | opens the first case box | assumption for \( \rulename{\vee E} \) |
| (4) | \( x \ge 1 \) and \( 1 > 0 \) give \( x > 0 \) | \( \rulename{{\to}E} \), with the fact "\( a \ge b \) and \( b > c \) imply \( a > c \)" |
| (5) | opens the second case box | assumption for \( \rulename{\vee E} \) |
| (6) | computes \( \abs{x - 1} \) | \( \rulename{{\to}E} \) twice, with the facts "\( x < 1 \) implies \( x - 1 < 0 \)" and "\( a < 0 \) implies \( \abs a = -a \)" |
| (7) | uses the box assumption of (1) | \( \rulename{{\to}E} \) with the fact "\( 1 - x < 1 \) implies \( x > 0 \)", after substituting (6) into (1) |
| (8) | combines the two cases, then closes the outer box | \( \rulename{\vee E} \) on (2), (3)–(4), (5)–(7); then \( \rulename{{\to}I} \) on (1)–(8) |

Three things stand out. Sentence (7) uses the assumption made in (1); it may, because the box opened in (1) is still open. The facts of school algebra enter as implications, and each is used by \( \rulename{{\to}E} \). And sentence (8) does two jobs at once, which is normal: a single closing sentence often closes several boxes.
:::

### Writing a proof from a derivation

::: {#exm-write-from-derivation}
[From a derivation to a paragraph]

Let \( n \) be an integer. Write \( E \) for "\( n \) is even", \( O \) for "\( n \) is odd", \( F \) for "\( n + 1 \) is even", and \( G \) for "\( n(n+1) \) is even". The following derivation uses four facts about integers as premises. Write the paragraph a mathematician would write for it.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {E \vee O} \by{(every integer is even or odd)}{}
  \hypo {2} {E \to G} \by{(an even factor makes a product even)}{}
  \hypo {3} {O \to F} \by{(odd plus one is even)}{}
  \hypo {4} {F \to G} \by{(an even factor again)}{}
  \open
  \hypo {5} {E}
  \have {6} {G} \ie{2,5}
  \close
  \open
  \hypo {7} {O}
  \have {8} {F} \ie{3,7}
  \have {9} {G} \ie{4,8}
  \close
  \have {10} {G} \oe{1,5-6,7-9}
\end{nd}$
\end{center}
```
:::

::: {.solution}
> Every integer is even or odd, so we consider two cases. If \( n \) is even, then \( n(n+1) \) has an even factor, and so it is even. If \( n \) is odd, then \( n + 1 \) is even, so again \( n(n+1) \) has an even factor and is even. In either case \( n(n+1) \) is even.

Compare the two. The paragraph keeps one sentence for each box and each rule that matters: line 1 becomes "we consider two cases", the two boxes become the two "If" sentences, and line 10 becomes "In either case". It drops the line numbers and the rule names, and it merges the two \( \rulename{{\to}E} \) steps of lines 8 and 9 into one sentence joined by "so". It also leaves the premises unproved; each is one line of algebra (for instance, \( n = 2k \) gives \( n(n+1) = 2(k(n+1)) \)), and a careful write-up would include those lines. What it never does is skip a box: the reader can still see both cases and see them combined.
:::

## Checking a proof

A proof is correct when every line is licensed: each line is an assumption in an open box, a known fact, or one application of one rule to lines that are still available. So checking a proof means asking two questions of every line:

- **Is it true?** Is the statement on this line correct, in every situation the proof is considering at that point?
- **Does it follow, and by which rule?** Is this line obtained from available earlier lines by one rule, and which one?

The two columns catch different errors. A line can be true and yet not follow (a correct fact that the proof has not earned), and a line can follow from a false line. A proof is correct only if every line passes the second test; the first test is a fast way to find where to look. Below are four short proofs as a student might write them. Two are correct and two are not. For each we run the two-column check and give a verdict, and for a wrong proof we name the first line that fails.

::: {#exm-verify-cases}
[Proof A]

> **Claim.** For a real number \( x \), if \( x^2 - 3x + 2 < 0 \) then \( 1 < x < 2 \).
>
> (1) Assume \( x^2 - 3x + 2 < 0 \). (2) Then \( (x - 1)(x - 2) < 0 \). (3) A product of two real numbers is negative only when one factor is positive and the other negative, so either \( x - 1 > 0 \) and \( x - 2 < 0 \), or \( x - 1 < 0 \) and \( x - 2 > 0 \). (4) In the first case, \( 1 < x < 2 \). (5) In the second case, \( x < 1 \) and \( x > 2 \), which is impossible. (6) Hence \( 1 < x < 2 \).
:::

::: {.solution}
| Line | True? | Follows? By which rule? |
|---|---|---|
| (1) | assumption | opens the \( \rulename{{\to}I} \) box |
| (2) | yes: \( (x-1)(x-2) = x^2 - 3x + 2 \) | \( \rulename{{\to}E} \) with the algebraic identity |
| (3) | yes | \( \rulename{{\to}E} \) with the stated fact about signs; gives a disjunction of two conjunctions |
| (4) | yes, in this case | \( \rulename{\vee E} \), case 1: \( \rulename{\wedge E} \) gives \( x > 1 \) and \( x < 2 \) |
| (5) | the case is impossible | \( \rulename{\vee E} \), case 2: \( \rulename{\wedge E} \) gives \( x < 1 \) and \( x > 2 \); these give \( 2 < x < 1 \), a contradiction (\( \rulename{\neg E} \)); the case reaches \( 1 < x < 2 \) by \( \rulename{\bot E} \) |
| (6) | yes | \( \rulename{\vee E} \) on (3), (4), (5); then \( \rulename{{\to}I} \) on (1)–(6) |

**Verdict: correct.** Line (5) is the one to look at twice. "Which is impossible" is doing real work: it is \( \rulename{\bot E} \), the rule that lets a case which cannot occur reach any goal. Without it, the second case would not end with \( 1 < x < 2 \), and \( \rulename{\vee E} \) could not combine the cases.
:::

::: {#exm-verify-converse}
[Proof B]

> **Claim.** For an integer \( n \), if \( n^2 \) is even then \( n \) is even.
>
> (1) Suppose \( n \) is even. (2) Then \( n = 2k \) for some integer \( k \). (3) So \( n^2 = 4k^2 = 2(2k^2) \). (4) Hence \( n^2 \) is even. (5) Therefore, if \( n^2 \) is even then \( n \) is even.
:::

::: {.solution}
| Line | True? | Follows? By which rule? |
|---|---|---|
| (1) | assumption | opens a box, with "\( n \) is even" |
| (2) | yes, given (1) | the definition of "even" |
| (3) | yes | algebra |
| (4) | yes, given (1) | the definition of "even" |
| (5) | the statement is true, but … | **does not follow**: \( \rulename{{\to}I} \) on the box (1)–(4) gives "if \( n \) is even then \( n^2 \) is even", not (5) |

**Verdict: wrong; line (5) fails.** Every line is true, and lines (1)–(4) are a perfectly good proof of the converse. The error is in the one rule used at the end. \( \rulename{{\to}I} \) turns a box from \( P \) to \( Q \) into \( P \to Q \), with the box's assumption on the **left**. Here the box went from "\( n \) is even" to "\( n^2 \) is even", so \( \rulename{{\to}I} \) gives exactly the converse of the claim. Writing the claim instead is the invalid step from \( Q \to P \) to \( P \to Q \), which §06 refuted with a single row in the discussion after @exm-affirming-the-consequent. This is the flawed argument from the start of §01, and this is its diagnosis: **the \( \rulename{{\to}I} \) rule was used with the assumption and the conclusion swapped.** The claim is true, and @thm-square-even-implies-even proves it correctly, inside a box that opens with "\( n^2 \) is even".
:::

::: {#exm-verify-negation}
[Proof C]

> **Claim.** For an integer \( n \), the number \( n^2 - 2 \) is not divisible by 4.
>
> (1) Suppose \( n^2 - 2 \) is divisible by 4, say \( n^2 - 2 = 4k \) with \( k \) an integer. (2) Then \( n^2 = 4k + 2 = 2(2k + 1) \), so \( n^2 \) is even. (3) By @thm-square-even-implies-even, \( n \) is even, say \( n = 2m \) with \( m \) an integer. (4) Then \( n^2 = 4m^2 \), so \( 4m^2 = 4k + 2 \), and hence \( 1 = 2(m^2 - k) \). (5) So 1 is even. (6) But 1 is odd, and no integer is both even and odd; this is a contradiction. (7) Hence \( n^2 - 2 \) is not divisible by 4.
:::

::: {.solution}
| Line | True? | Follows? By which rule? |
|---|---|---|
| (1) | assumption | opens the \( \rulename{\neg I} \) box, with "4 divides \( n^2 - 2 \)" |
| (2) | yes, given (1) | algebra, then the definition of "even" |
| (3) | yes, given (2) | \( \rulename{{\to}E} \) with @thm-square-even-implies-even and (2) |
| (4) | yes, given (1) and (3) | algebra: subtract \( 4k \), divide by 2 |
| (5) | yes, given (4) | the definition of "even", with \( m^2 - k \) an integer |
| (6) | yes | \( \rulename{\neg E} \): (5) against "1 is not even" (since \( 1 = 2 \cdot 0 + 1 \) is odd) |
| (7) | yes | \( \rulename{\neg I} \) on the box (1)–(6) |

**Verdict: correct.** The goal is a negation, so the skeleton is \( \rulename{\neg I} \), and it is correctly built: the box opens with the positive statement and closes with its negation. Although it reads as a "proof by contradiction", no RAA is used. Line (3) cites an earlier theorem, which is always allowed; line (4) is the only real computation, and dividing by 2 is legitimate since \( 2 \ne 0 \).
:::

::: {#exm-verify-scope}
[Proof D]

> **Claim.** For a real number \( x \): if \( x > 1 \) then \( x^2 > x \); and \( x^2 + 1 > x \).
>
> (1) Suppose \( x > 1 \). (2) Multiplying both sides by \( x \), which is positive, gives \( x^2 > x \). (3) Hence if \( x > 1 \) then \( x^2 > x \). (4) For the second part, \( x^2 + 1 > x^2 \), and \( x^2 > x \) by (2), so \( x^2 + 1 > x \).
:::

::: {.solution}
| Line | True? | Follows? By which rule? |
|---|---|---|
| (1) | assumption | opens the \( \rulename{{\to}I} \) box for the first conjunct |
| (2) | yes, given (1) | \( \rulename{{\to}E} \) with the fact "multiplying by a positive number keeps \( > \)"; \( x > 0 \) since \( x > 1 > 0 \) |
| (3) | yes | \( \rulename{{\to}I} \) on the box (1)–(2) |
| (4) | "\( x^2 > x \)" is **false** for \( x = 1/2 \) | **does not follow**: it cites (2), which lies inside the box closed at (3) |

**Verdict: wrong; line (4) fails.** The claim is a conjunction, so the skeleton is \( \rulename{\wedge I} \) with two separate proofs. The first proof is fine. The second is meant to hold for every real \( x \), but it cites line (2), which was derived inside the box that assumed \( x > 1 \); once that box closed at line (3), line (2) is no longer available. The rule broken is the scope of the \( \rulename{{\to}I} \) box (@def-derivation). The first column confirms it: at \( x = 1/2 \), \( x^2 = 1/4 < 1/2 = x \), so the cited statement is false in the situation line (4) is supposed to cover.

The claim itself is true, so the proof can be repaired. For every real \( x \),

\[
x^2 - x + 1 = \left(x - \tfrac12\right)^2 + \tfrac34 > 0,
\]

since a square is non-negative, and so \( x^2 + 1 > x \). This proof uses nothing from the closed box.
:::

What the four checks show together: in Proofs B and D every sentence **sounds** right, and in Proof B every sentence **is** true. The errors are in the connections between sentences, which is exactly what the rules govern. Reading for "is each step plausible?" would have passed both; reading for "which rule, from which available lines?" catches both.

## Exercises

### A. Check your understanding

::: {#exr-proof-skeletons-a1}
[A1]

For each goal, name its main connective, name the skeleton, and write the first sentence of a proof.

::: {.enumerate options="label=(\alph*)"}
1. For real \( x \): if \( x^3 < 0 \) then \( x < 0 \).
2. There is no integer \( n \) with \( 2n = 7 \).
3. For real \( x \) and \( y \): \( \abs{xy} = \abs{x}\abs{y} \) and \( \abs{x + y} \le \abs x + \abs y \).
4. For an integer \( n \): \( n \) is odd if and only if \( n^2 \) is odd.
5. For real \( x \): \( x \ge 0 \) or \( x < 0 \), proved from the fact that every real number is either positive, zero or negative.
:::
:::

::: {.solution}
(a) \( \to \); direct \( \rulename{{\to}I} \) (or contrapositive): "Assume \( x^3 < 0 \)." (Contrapositive version: "We prove the contrapositive. Suppose \( x \ge 0 \).")

(b) \( \neg \) (the claim is "not: there is an integer \( n \) with \( 2n = 7 \)"); \( \rulename{\neg I} \): "Suppose \( n \) is an integer with \( 2n = 7 \)." (The step from "there is" to naming \( n \) is a quantifier rule from Chapter 2.)

(c) \( \wedge \); \( \rulename{\wedge I} \): "We prove the two statements in turn."

(d) \( \leftrightarrow \); \( \rulename{{\leftrightarrow}I} \): "\( (\Rightarrow) \) Assume \( n \) is odd."

(e) \( \vee \); cases on the given fact (\( \rulename{\vee E} \)), then \( \rulename{\vee I} \) in each case: "Every real number is positive, zero or negative; we consider the three cases."
:::

### B. Practice

For each exercise, name the skeleton before writing the proof.

::: {#exr-proof-skeletons-b1}
[B1: A disjunction as a goal]

Let \( m \) and \( n \) be integers such that \( m^2 + n^2 \) is even. Prove that \( m \) and \( n \) are both even or both odd.
:::

::: {.solution}
*Skeleton.* The goal is a disjunction, "(\( m \) even and \( n \) even) or (\( m \) odd and \( n \) odd)", and neither side can be proved outright, so we split into cases on the fact "every integer is even or odd", first for \( m \) and then for \( n \), and use \( \rulename{\vee I} \) in each case that can occur. The two mixed cases are closed by \( \rulename{\bot E} \).

*Proof.* Every integer is even or odd; we consider the cases for \( m \) and, inside each, the cases for \( n \).

*Case 1:* \( m \) is even. If \( n \) is even, then \( m \) and \( n \) are both even, so in particular the disjunction holds. If \( n \) is odd, write \( m = 2a \) and \( n = 2b + 1 \) with \( a, b \) integers; then
\[
m^2 + n^2 = 4a^2 + 4b^2 + 4b + 1 = 2(2a^2 + 2b^2 + 2b) + 1
\]
is odd, and so not even, since no integer is both. This contradicts the hypothesis, so this case cannot occur.

*Case 2:* \( m \) is odd. If \( n \) is odd, then both are odd, and the disjunction holds. If \( n \) is even, exchanging the roles of \( m \) and \( n \) in the computation of Case 1 shows that \( m^2 + n^2 \) is odd, a contradiction; this case cannot occur.

In every case that can occur, \( m \) and \( n \) are both even or both odd. This proves the claim. (No RAA is used: the impossible cases are closed by \( \rulename{\bot E} \).)
:::

::: {#exr-proof-skeletons-b2}
[B2: A conjunction inside an implication]

Prove that for every real number \( x \), if \( x^2 \le x \) then \( 0 \le x \le 1 \).
:::

::: {.solution}
*Skeleton.* \( \rulename{{\to}I} \), then \( \rulename{\wedge I} \) for the two inequalities \( 0 \le x \) and \( x \le 1 \); the second uses cases.

*Proof.* Let \( x \) be real and assume \( x^2 \le x \). We prove \( 0 \le x \) and \( x \le 1 \) in turn.

Since a square is non-negative, \( 0 \le x^2 \le x \), so \( 0 \le x \).

For the second inequality, since \( 0 \le x \) we have \( x = 0 \) or \( x > 0 \). If \( x = 0 \), then \( x \le 1 \). If \( x > 0 \), dividing \( x^2 \le x \) by the positive number \( x \) gives \( x \le 1 \). In either case \( x \le 1 \).

Hence \( 0 \le x \le 1 \).
:::

::: {#exr-proof-skeletons-b3}
[B3: An iff between inequalities]

Prove that for every real number \( x \), \( x^2 - 5x + 6 < 0 \) if and only if \( 2 < x < 3 \).
:::

::: {.solution}
*Skeleton.* \( \rulename{{\leftrightarrow}I} \): two boxes. Both use the factorization \( x^2 - 5x + 6 = (x - 2)(x - 3) \); the direction \( (\Rightarrow) \) uses cases on the signs, as in @exm-verify-cases.

*Proof.* Let \( x \) be real. Note that \( x^2 - 5x + 6 = (x - 2)(x - 3) \).

\( (\Rightarrow) \) Assume \( (x - 2)(x - 3) < 0 \). A product of two real numbers is negative only when one factor is positive and the other negative. In the case \( x - 2 > 0 \) and \( x - 3 < 0 \), we get \( 2 < x < 3 \). In the case \( x - 2 < 0 \) and \( x - 3 > 0 \), we get \( x < 2 \) and \( x > 3 \), so \( 3 < x < 2 \), which is impossible; this case cannot occur. Hence \( 2 < x < 3 \).

\( (\Leftarrow) \) Assume \( 2 < x < 3 \). Then \( x - 2 > 0 \) and \( x - 3 < 0 \), and the product of a positive and a negative number is negative, so \( (x - 2)(x - 3) < 0 \), that is, \( x^2 - 5x + 6 < 0 \).

This proves the equivalence.
:::

### C. Going deeper

::: {#exr-proof-skeletons-c1}
[C1: Derivation and prose]

::: {.enumerate options="label=(\alph*)"}
1. Give a derivation of \( (P \to Q) \wedge (Q \to R) \vdash P \to R \).
2. Let \( x \) be a real number. Take \( P \) to be "\( x > 2 \)", \( Q \) to be "\( x^2 > 4 \)" and \( R \) to be "\( x^2 + 1 > 5 \)". Check that \( P \to Q \) and \( Q \to R \) are true for every real \( x \), and write the argument of (a) as a short paragraph of prose.
:::
:::

::: {.solution}
(a) The goal is an implication, so the skeleton is \( \rulename{{\to}I} \); inside, the premise is a conjunction, so \( \rulename{\wedge E} \) takes it apart.

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

(b) If \( x > 2 \), then \( x > 0 \), and multiplying \( x > 2 \) by the positive number \( x \) gives \( x^2 > 2x > 4 \); so \( P \to Q \) holds. If \( x^2 > 4 \), adding 1 gives \( x^2 + 1 > 5 \); so \( Q \to R \) holds. The prose version of (a):

> Assume \( x > 2 \). Then \( x^2 > 4 \), and so \( x^2 + 1 > 5 \). Hence if \( x > 2 \) then \( x^2 + 1 > 5 \).

Lines 2 and 3 of the derivation (the two \( \rulename{\wedge E} \) steps) leave no trace in the prose: a reader who is told both implications uses them without announcing that the conjunction has been split.
:::

::: {#exr-proof-skeletons-c2}
[C2: Label the lines]

Label each sentence of the following proof with the rule it uses, as in @exm-annotate-abs. Say which sentence uses RAA and which uses one of @prp-de-morgan.

> **Claim.** For real numbers \( x \) and \( y \), if \( x + y > 2 \) then \( x > 1 \) or \( y > 1 \).
>
> (1) Assume \( x + y > 2 \). (2) Suppose, for a contradiction, that it is not the case that \( x > 1 \) or \( y > 1 \). (3) Then \( x > 1 \) fails and \( y > 1 \) fails. (4) So \( x \le 1 \) and \( y \le 1 \). (5) Adding, \( x + y \le 2 \). (6) This contradicts \( x + y > 2 \). (7) Hence \( x > 1 \) or \( y > 1 \), which proves the claim.
:::

::: {.solution}
| Sentence | Rule |
|---|---|
| (1) | assumption, opening the \( \rulename{{\to}I} \) box |
| (2) | assumption \( \neg(x > 1 \vee y > 1) \), opening an RAA box |
| (3) | @prp-de-morgan (a), \( \neg(A \vee B) \vdash \neg A \wedge \neg B \), applied to (2) |
| (4) | \( \rulename{\wedge E} \) on (3), twice, then \( \rulename{{\to}E} \) with the fact "for real numbers, \( \neg(a > 1) \) implies \( a \le 1 \)", twice; then \( \rulename{\wedge I} \) |
| (5) | \( \rulename{\wedge E} \) on (4), then \( \rulename{{\to}E} \) with the fact "\( a \le 1 \) and \( b \le 1 \) imply \( a + b \le 2 \)" |
| (6) | \( \rulename{\neg E} \): (1) and (5), since \( x + y \le 2 \) is the negation of \( x + y > 2 \) |
| (7) | RAA on the box (2)–(6); then \( \rulename{{\to}I} \) on (1)–(7) |

RAA is used in (7): the box opened with the negation of the goal \( x > 1 \vee y > 1 \) and closed with the goal itself. Sentence (3) uses De Morgan law (a), a direction that needs no RAA. By the second test of §05 this is a contrapositive in costume: everything in the box follows from (2) alone, and the hypothesis (1) enters only at the clash in (6). The open version reads: "We prove the contrapositive: if \( x \le 1 \) and \( y \le 1 \), then \( x + y \le 2 \)." The rewrite is clearer, but it does not remove RAA: passing from the contrapositive back to the claim is @prp-contrapositive-converse, which uses it.
:::

::: {#exr-proof-skeletons-c3}
[C3: Four proofs to check]

Each of the following is a student's proof. For each, decide whether it is correct. If it is not, give the first line that fails, and name the rule that is broken or the step that is not licensed. If the claim itself is false, give a witness.

::: {.enumerate options="label=(\alph*)"}
1. **Claim.** If \( x \) is rational and \( y \) is irrational, then \( x + y \) is irrational. (1) Assume \( x \) is rational and \( y \) is irrational. (2) Suppose \( x + y \) is rational. (3) Then \( y = (x + y) - x \) is a difference of two rational numbers, so \( y \) is rational. (4) This contradicts the fact that \( y \) is irrational. (5) Hence \( x + y \) is irrational.
2. **Claim.** For real \( x \), if \( x^2 > 4 \) then \( x > 2 \). (1) Suppose \( x > 2 \). (2) Then \( x > 0 \), so multiplying by \( x \) gives \( x^2 > 2x \), and \( 2x > 4 \). (3) So \( x^2 > 4 \). (4) Hence if \( x^2 > 4 \) then \( x > 2 \).
3. **Claim.** For real \( x \), \( \abs{x - 1} \le \abs x + 1 \). (1) Either \( x \ge 1 \) or \( x \le 0 \). (2) If \( x \ge 1 \), then \( \abs{x - 1} = x - 1 \le x + 1 = \abs x + 1 \). (3) If \( x \le 0 \), then \( \abs{x - 1} = 1 - x = 1 + \abs x \). (4) In either case, \( \abs{x - 1} \le \abs x + 1 \).
4. **Claim.** For real \( x \), if \( x^2 = x \) then \( x = 1 \). (1) Assume \( x^2 = x \). (2) Dividing both sides by \( x \) gives \( x = 1 \). (3) Hence if \( x^2 = x \) then \( x = 1 \).
:::

*Hint: run the two-column check on every line. In (c), ask what \( \rulename{\vee E} \) needs from line (1).*
:::

::: {.solution}
(a) **Correct.** The goal after (1) is "\( x + y \) is irrational", that is, "not rational", so the skeleton is \( \rulename{\neg I} \): the box (2)–(4) opens with "\( x + y \) is rational" and reaches \( \bot \) at (4) by \( \rulename{\neg E} \), and (5) is \( \rulename{\neg I} \). Line (3) uses the fact that a difference of rational numbers is rational, which is school algebra: \( \frac ab - \frac cd = \frac{ad - bc}{bd} \) with \( bd \ne 0 \). Then \( \rulename{{\to}I} \) closes the box of (1).

(b) **Wrong; line (4) fails, and the claim is false.** Lines (1)–(3) prove "if \( x > 2 \) then \( x^2 > 4 \)", the converse; \( \rulename{{\to}I} \) on the box (1)–(3) gives exactly that, with the box's assumption on the left. Line (4) swaps assumption and conclusion, as in @exm-verify-converse. Here the swap does more than spoil the proof: the claim is false. Witness: \( x = -3 \), for which \( x^2 = 9 > 4 \) but \( x > 2 \) fails.

(c) **Wrong; line (1) fails.** "Either \( x \ge 1 \) or \( x \le 0 \)" is false for \( x = 1/2 \), so line (1) is not a known fact, and the \( \rulename{\vee E} \) in (4) combines two cases that do not cover all real numbers. The rule broken is \( \rulename{\vee E} \): its first input must be a disjunction that has been established, and this one has not. The claim is true, and adding the missing case repairs the proof: if \( 0 < x < 1 \), then \( \abs{x - 1} = 1 - x < 1 < \abs x + 1 \). The three cases \( x \ge 1 \), \( 0 < x < 1 \) and \( x \le 0 \) do cover every real number.

(d) **Wrong; line (2) fails, and the claim is false.** Dividing by \( x \) uses the fact "if \( x \ne 0 \), then \( x^2 = x \) implies \( x = 1 \)". Applying it is \( \rulename{{\to}E} \), which needs the antecedent \( x \ne 0 \) as an available line, and no line provides it. So (2) is an application of \( \rulename{{\to}E} \) without its antecedent. Witness: \( x = 0 \) satisfies \( x^2 = x \) but not \( x = 1 \). The correct statement, proved by cases on \( x = 0 \) or \( x \ne 0 \), is: if \( x^2 = x \) then \( x = 0 \) or \( x = 1 \).
:::
