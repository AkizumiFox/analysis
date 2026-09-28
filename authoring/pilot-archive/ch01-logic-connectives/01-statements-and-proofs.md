# What a Proof Is Made Of

This is where the book starts, and it starts with a question every reader of mathematics eventually asks: when is an argument a proof? A proof is not a list of true sentences, and it is not an argument that merely sounds convincing. This section takes the first steps towards a precise answer. It says what the sentences of a proof are, how they are built from smaller ones, and what the one idea is that the rest of the chapter develops.

## Two arguments about squares

Here is a fact about whole numbers that we will prove properly later in this chapter.

> For every integer \( n \), if \( n^2 \) is even, then \( n \) is even.

Read the following two arguments for it. Each one is written in the style of a textbook proof, and each sentence in each of them is true.

**Argument A.** Suppose \( n \) is odd, say \( n = 2k + 1 \) for an integer \( k \). Then \( n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1 \), so \( n^2 \) is odd, and in particular \( n^2 \) is not even. So an odd \( n \) never has an even square. Since every integer is even or odd, an integer with an even square must be even.

**Argument B.** Suppose \( n \) is even, say \( n = 2k \) for an integer \( k \). Then \( n^2 = 4k^2 = 2(2k^2) \), and \( 2k^2 \) is an integer, so \( n^2 \) is even. Hence if \( n^2 \) is even, then \( n \) is even.

Argument A is a correct proof. Argument B is not, although no individual sentence in it is false. It starts from "\( n \) is even" and arrives at "\( n^2 \) is even". That is a perfectly good proof of a different statement, "if \( n \) is even, then \( n^2 \) is even". The claim asks for the journey in the opposite direction, from the square back to the number. The last sentence of B announces a conclusion that the argument never reached.

Seeing this is easy once it is pointed out. Saying in general what went wrong is harder, and that is the purpose of this chapter. By the end of it we will be able to name the error exactly: B uses the rule for proving an "if … then" statement with the assumption and the conclusion swapped. To say that, we need to know what the rules are. First we need to know what they act on.

## Statements

A proof is written in sentences, but not every sentence can appear in one. "Is 91 prime?" cannot be a step of an argument, because it asserts nothing; neither can "Let us now turn to the case \( n = 0 \)." The sentences that can serve as steps are the ones that make a claim.

*A statement is a sentence that is either true or false.*

::: {#def-statement}
[Statement]

A **statement** is a declarative sentence that is **either true or false**, and not both.
:::

In words: a statement makes a claim, and the claim is either correct or incorrect. The definition asks that one of the two is the case. It does **not** ask that we know which one. A statement whose truth nobody has settled is still a statement.

::: {#exm-statements}
[Statements and non-statements]

Decide which of the following are statements.

::: {.enumerate options="label=(\alph*)"}
1. \( 7 \) is a prime number.
2. \( 0.999 > 1 \).
3. Every even integer greater than \( 2 \) is the sum of two primes.
4. Is \( 2^{11} - 1 \) prime?
5. \( x > 2 \).
6. \( 3 > 2 \).
:::
:::

::: {.solution}
(a) This is a statement, and it is true.

(b) This is a statement, and it is false: a false sentence is as much a statement as a true one.

(c) This is a statement. It is known as Goldbach's conjecture, and at the time of writing nobody knows whether it is true or false. It is certainly one or the other, which is all the definition requires.

(d) This is a question, so it is not a statement. The sentence "\( 2^{11} - 1 \) is prime" is a statement, and a false one, since \( 2^{11} - 1 = 2047 = 23 \cdot 89 \).

(e) This is not a statement. Its truth depends on what \( x \) is: it is true when \( x = 3 \) and false when \( x = 0 \), and as written nothing says which. Such a sentence is called an **open sentence**.

(f) This is the same sentence with \( x \) replaced by \( 3 \), and it is a true statement.
:::

Items (e) and (f) differ by one symbol, and the difference is the whole point. The open sentence \( x > 2 \) becomes a statement in two ways. We can put a number in for \( x \), as in (f). Or we can say which \( x \) we mean in some other way, as in "for every real number \( x \), \( x > 2 \)" (a false statement) or "for some real number \( x \), \( x > 2 \)" (a true one). The words "for every" and "for some" are the **quantifiers**. They are the subject of Chapter 2.

Mathematics is full of open sentences, and we cannot wait until Chapter 2 to use them. So we adopt a convention for this chapter. When an example says "let \( x \) be a real number" and then talks about \( x \), the letter \( x \) names **one fixed** number, not further specified. Every sentence about that \( x \) is then a statement, true or false according to which number \( x \) is. "Let \( x \) be a real number with \( x > 2 \); then \( x^2 > 4 \)" is an argument about one number, which happens to work whatever the number is. Chapter 2 explains why an argument of that kind proves a statement about every \( x \) at once.

::: {.remark}
The book reserves the words "proposition" and "theorem" for proved results, so it calls the sentences of logic **statements**. Other books call them propositions, which is where the name "propositional logic" for the subject of this chapter comes from.
:::

## The connectives

Most statements in mathematics are built from smaller ones. "\( 0 < x \) and \( x < 1 \)" is built from "\( 0 < x \)" and "\( x < 1 \)" with the word "and". "If \( n^2 \) is even, then \( n \) is even" is built from two statements with "if … then". The words that do the building are the **connectives**, and there are five of them. We write \( P \), \( Q \), \( R \), … for statements whose inner structure we are ignoring at the moment. In the last column of the table, \( x \) is a real number, \( P \) is "\( x > 0 \)" and \( Q \) is "\( x < 1 \)".

| Symbol | Name | Read | Example |
|--------|------------|---------------------|--------------------------------|
| \( P \wedge Q \) | conjunction | \( P \) and \( Q \) | \( x > 0 \) and \( x < 1 \), that is, \( 0 < x < 1 \) |
| \( P \vee Q \) | disjunction | \( P \) or \( Q \) | \( x > 0 \) or \( x < 1 \) |
| \( P \to Q \) | implication | if \( P \), then \( Q \) | if \( x > 0 \), then \( x < 1 \) |
| \( P \leftrightarrow Q \) | biconditional | \( P \) if and only if \( Q \) | \( x > 0 \) if and only if \( x < 1 \) |
| \( \neg P \) | negation | not \( P \) | \( x \) is not positive, that is, \( x \le 0 \) |

To these we add one statement with no parts at all, written \( \bot \) and read "contradiction". It stands for a statement that is false no matter what: \( 0 = 1 \) will do. A proof that reaches \( \bot \) has shown that the situation it was working in cannot occur. That is the heart of proof by contradiction, and \( \bot \) is how the rules of Section 1.3 handle it.

A few words about the readings. In \( P \to Q \), the statement \( P \) is the **hypothesis** (or antecedent) and \( Q \) the **conclusion** (or consequent). English has many ways of saying \( P \to Q \): "\( P \) implies \( Q \)", "\( Q \) if \( P \)", "\( Q \) whenever \( P \)", "\( P \) only if \( Q \)", "\( P \) is sufficient for \( Q \)" and "\( Q \) is necessary for \( P \)" all mean the same thing, and the exercises ask you to check this. "If and only if" is often shortened to **iff**. Several English words become \( \wedge \): "but", "although" and "while" all assert both parts, and add only a tone of contrast that logic ignores. "\( f \) is continuous at \( a \) but not differentiable there" is a conjunction.

Chained inequalities are conjunctions in disguise. \( 0 < x < 1 \) abbreviates \( (0 < x) \wedge (x < 1) \), and \( a \le b \le c \) abbreviates \( (a \le b) \wedge (b \le c) \). The symbol \( \le \) itself hides a disjunction: \( a \le b \) means \( (a < b) \vee (a = b) \). We will use both facts often.

In theorem statements the book writes \( \Rightarrow \) and \( \Longleftrightarrow \), as mathematicians usually do, and in running prose it says "implies" and "if and only if". The arrows \( \to \) and \( \leftrightarrow \) are kept for the formal derivations that start in the next section. Nothing but typography separates the two pairs.

::: {.warning}
In everyday English, "or" is often exclusive: "soup or salad" on a menu means one but not both. In mathematics, \( P \vee Q \) is **inclusive**: it is true when \( P \) is true, when \( Q \) is true, and when both are. For a real number \( x \), the statement "\( x \ge 0 \) or \( x \le 0 \)" is true for every \( x \); at \( x = 0 \) both parts are true, and that does not spoil it. If an exclusive "or" is meant, it must be said: "\( P \) or \( Q \), but not both", which is \( (P \vee Q) \wedge \neg (P \wedge Q) \).
:::

## Reading a statement: precedence and the main connective

Connectives can be combined without limit, and a string of symbols is only useful if it can be read in exactly one way. Consider \( \neg P \wedge Q \). Does it deny \( P \) and then assert \( Q \), or does it deny the whole of \( P \wedge Q \)? These are different claims. With \( P \): "\( n \) is even" and \( Q \): "\( n > 0 \)", the first says that \( n \) is odd and positive, while the second says only that \( n \) is not a positive even number, which \( n = -4 \) satisfies.

Parentheses settle every such question, and a few conventions let us drop the ones that would only add clutter.

::: {.enumerate options="label=(\arabic*)"}
1. \( \neg \) binds most tightly: it applies to the smallest complete statement that follows it. So \( \neg P \wedge Q \) means \( (\neg P) \wedge Q \), and to deny \( P \wedge Q \) we write \( \neg(P \wedge Q) \).
2. \( \wedge \) and \( \vee \) bind more tightly than \( \to \) and \( \leftrightarrow \). So \( P \wedge Q \to R \) means \( (P \wedge Q) \to R \).
3. Otherwise we write the parentheses. In particular we never write \( P \wedge Q \vee R \) or \( P \to Q \to R \) without them.
:::

Every statement built with connectives has a **main connective**: the one applied last when the statement is built up from its parts. It is found by undoing the construction from the outside. Take
\[
\neg(P \wedge Q) \to R .
\]
By convention (1), the \( \neg \) applies only to the parenthesized \( P \wedge Q \); by convention (2), the \( \to \) takes everything to its left as its hypothesis. So the last step joined \( \neg(P \wedge Q) \) and \( R \) with \( \to \), and \( \to \) is the main connective. Its hypothesis \( \neg(P \wedge Q) \) has main connective \( \neg \), applied to \( P \wedge Q \), whose main connective is \( \wedge \). The construction can be drawn as a tree, with the main connective at the root and the letters at the leaves.

\begin{center}
\begin{tikzpicture}[level distance=11mm, sibling distance=26mm, every node/.style={font=\normalsize}]
  \node {$\to$}
    child { node {$\neg$}
      child { node {$\wedge$}
        child { node {$P$} }
        child { node {$Q$} }
      }
    }
    child { node {$R$} };
\end{tikzpicture}
\end{center}

Reading the tree from the top: the statement is an implication; its hypothesis is a negation; what is negated is a conjunction. Reading from the bottom retraces how the statement was built.

The main connective is not a matter of grammar for its own sake. It is the first thing to find when a proof has to be written, because it decides how the proof begins. To prove "if \( 0 < x < 1 \), then \( x^2 < x \)", whose main connective is \( \to \), a proof starts "Suppose \( 0 < x < 1 \)." To prove "\( x^2 + 1 > 0 \) and \( x^2 + 1 \ne 0 \)", whose main connective is \( \wedge \), a proof has two parts, one for each side. The last section of this chapter makes this into a method.

::: {.check}
Find the main connective of each statement.

::: {.enumerate options="label=(\alph*)"}
1. \( \neg P \vee Q \)
2. \( \neg (P \vee Q) \)
3. \( (P \to Q) \wedge (Q \to P) \)
:::
:::

::: {.solution}
(a) \( \vee \): by convention (1) the \( \neg \) applies only to \( P \), so the statement is the disjunction of \( \neg P \) and \( Q \).

(b) \( \neg \): the parentheses make the whole disjunction the thing denied.

(c) \( \wedge \): each parenthesized implication is complete, and the last step joins them with "and".
:::

## Each connective, two rules

We now come to the idea that organizes the whole chapter. Think about what a mathematician actually does with the word "and". There are exactly two things to do with it.

- To **prove** a statement of the form \( P \wedge Q \), prove \( P \) and prove \( Q \).
- To **use** a statement of the form \( P \wedge Q \) that is already known, take either half.

Nobody needs to be taught these two moves. They are also, and this is the point, **all** there is to know about "and" for the purpose of writing proofs. Every other fact about \( \wedge \), such as that \( P \wedge Q \) and \( Q \wedge P \) say the same thing, follows from the two moves, as the next section shows. The first move is called the **introduction rule** for \( \wedge \), written \( \rulename{\wedge I} \), because it is how a \( \wedge \) gets into a proof. The second is the **elimination rule**, \( \rulename{\wedge E} \), because it is how a \( \wedge \) is taken apart.

| Rule | What it allows | What a proof says |
|------|---------------------------|--------------------------------------|
| \( \rulename{\wedge I} \) | from \( P \) and \( Q \), conclude \( P \wedge Q \) | "We have shown \( x > 0 \) and \( x < 1 \). Hence \( 0 < x < 1 \)." |
| \( \rulename{\wedge E} \) | from \( P \wedge Q \), conclude \( P \); also \( Q \) | "Since \( 0 < x < 1 \), in particular \( x > 0 \)." |

Every connective works the same way. Each comes with an introduction rule, saying how to prove a statement with that main connective, and an elimination rule, saying what a statement with that main connective lets us conclude. The rules for \( \to \) come in Section 1.2, the rules for \( \vee \), \( \neg \) and \( \bot \) in Section 1.3, and the rules for \( \leftrightarrow \) in Section 1.4. Two slogans summarize the plan.

*Each connective comes with a way to prove it and a way to use it.*

*A proof is a chain in which every line is an assumption or one application of a rule.*

The rules are chosen so that they never lead from true statements to a false one. For \( \wedge \) this is plain: if \( P \) and \( Q \) are both true, so is \( P \wedge Q \), and if \( P \wedge Q \) is true, so is \( P \). For the other connectives it takes a sentence or two each time, and Section 1.6 collects the argument.

The second slogan is what makes a proof possible to check. To find a proof may need an idea. To check one needs none: go through it line by line and ask of each line which rule produced it and whether that rule was applied to lines that really are there. A reader who has lost the thread of a long argument can always fall back on that question, and it is the question we will learn to ask of Argument B. For the rest of Part 0 we will ask it explicitly. From Part I on, the rules are applied silently, the way a fluent reader applies grammar, but they are the same rules.

The order of this chapter differs from that of many logic books, which begin with truth tables: a table that lists, for instance, when \( P \to Q \) is true. There, the row "if \( P \) is false, then \( P \to Q \) is true" has to be accepted as a convention, and it looks arbitrary. Here, that row will come out as a consequence of how proofs work (Section 1.3), and the tables arrive in Section 1.6 as a summary of rules we already understand.

## Exercises

### A. Check your understanding

::: {#exr-statements-and-proofs-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the definition of a statement. Is "\( 10^{100} + 1 \) is prime" a statement?
2. Let \( x \) be a real number. Is "\( x^2 - 1 = 0 \)" a statement? Is "\( 0^2 - 1 = 0 \)"?
3. With \( P \): "\( n \) is even" and \( Q \): "\( n \) is prime", write "\( n \) is prime but not even" in symbols.
4. Find the main connective of \( P \wedge Q \to \neg R \), and write the statement with all its parentheses.
5. True or false, with a reason: if \( P \) and \( Q \) are both true, then \( P \vee Q \) is false.
:::
:::

::: {.solution}
(a) A statement is a declarative sentence that is either true or false, and not both (@def-statement). Yes: \( 10^{100} + 1 \) is a definite integer, so it either is prime or is not. The definition does not ask us to know which.

(b) With \( x \) fixed, as in this chapter's convention, "\( x^2 - 1 = 0 \)" is a statement about that one number: true if \( x \) is \( 1 \) or \( -1 \), false otherwise. Without such a convention it would be an open sentence. The sentence "\( 0^2 - 1 = 0 \)" is a statement outright, and it is false, since \( 0^2 - 1 = -1 \).

(c) \( Q \wedge \neg P \). The word "but" is a conjunction.

(d) By convention (2), \( \wedge \) binds more tightly than \( \to \), and by convention (1), \( \neg \) applies only to \( R \). So the statement is \( (P \wedge Q) \to (\neg R) \), and its main connective is \( \to \).

(e) False. The mathematical "or" is inclusive, so \( P \vee Q \) is true when both parts are true.
:::

### B. Practice

::: {#exr-statements-and-proofs-b1}
[B1: Translating analysis]

Translate each sentence into symbols, using the atomic statements given. You do not need to know what the words mean; only the grammar matters.

::: {.enumerate options="label=(\alph*)"}
1. "\( f \) is continuous at \( a \) but not differentiable there", with \( C \): "\( f \) is continuous at \( a \)" and \( D \): "\( f \) is differentiable at \( a \)".
2. "If the sequence \( (a_n) \) converges, it is bounded", with \( V \): "\( (a_n) \) converges" and \( B \): "\( (a_n) \) is bounded".
3. "\( x \) is rational or irrational", with \( R \): "\( x \) is rational". (A real number is irrational when it is not rational.)
4. "The set \( F \) is closed if and only if its complement is open", with \( K \): "\( F \) is closed" and \( U \): "the complement of \( F \) is open".
:::
:::

::: {.solution}
(a) \( C \wedge \neg D \). "But" asserts both parts; "not differentiable there" is the negation of \( D \).

(b) \( V \to B \). The pronoun "it" refers to \( (a_n) \), so the conclusion is the statement \( B \).

(c) \( R \vee \neg R \). "Irrational" means "not rational", so the second part is \( \neg R \), not a new atomic statement.

(d) \( K \leftrightarrow U \).
:::

::: {#exr-statements-and-proofs-b2}
[B2: Parsing]

For each statement, insert all the parentheses that the conventions allow us to omit, and name the main connective.

::: {.enumerate options="label=(\alph*)"}
1. \( \neg P \to Q \)
2. \( P \vee \neg Q \leftrightarrow \neg R \)
3. \( \neg\neg P \wedge (Q \to R) \)
:::

Then let \( x \) and \( y \) be real numbers, with \( P \): "\( x > 0 \)", \( Q \): "\( y > 0 \)" and \( R \): "\( xy > 0 \)". Write \( P \wedge Q \to R \) as an English sentence, and say whether it is true whatever the numbers \( x \) and \( y \) are.
:::

::: {.solution}
(a) \( (\neg P) \to Q \), main connective \( \to \).

(b) \( (P \vee (\neg Q)) \leftrightarrow (\neg R) \), main connective \( \leftrightarrow \). Each \( \neg \) applies to the single letter after it, and \( \vee \) binds more tightly than \( \leftrightarrow \).

(c) \( (\neg(\neg P)) \wedge (Q \to R) \), main connective \( \wedge \). The first \( \neg \) applies to the statement \( \neg P \), which is the smallest complete statement following it.

The statement \( P \wedge Q \to R \) is \( (P \wedge Q) \to R \): "if \( x > 0 \) and \( y > 0 \), then \( xy > 0 \)". It is true for all real \( x \) and \( y \), since the product of two positive numbers is positive.
:::

### C. Going deeper

::: {#exr-statements-and-proofs-c1}
[C1: "Only if" and "unless"]

Let \( P \) and \( Q \) be statements.

::: {.enumerate options="label=(\alph*)"}
1. Explain why "\( P \) only if \( Q \)" means \( P \to Q \), and not \( Q \to P \). *(Ask: which situation would make "\( P \) only if \( Q \)" false?)*
2. Explain why "\( P \) unless \( Q \)" means \( \neg Q \to P \).
3. Let \( x \) be a real number. Decide whether each sentence is true for every real \( x \). Justify your answer, giving a value of \( x \) that makes it false where there is one.
    - "\( x^2 = 4 \) if \( x = 2 \)."
    - "\( x^2 = 4 \) only if \( x = 2 \)."
    - "\( x^2 > 0 \) unless \( x = 0 \)."
:::
:::

::: {.solution}
(a) "\( P \) only if \( Q \)" says that \( P \) does not happen without \( Q \). It is broken exactly when \( P \) holds and \( Q \) fails. That is also exactly when \( P \to Q \) is broken: an implication promises \( Q \) whenever \( P \), and the promise fails only when \( P \) holds without \( Q \). So the two say the same thing. By contrast, \( Q \to P \) is broken when \( Q \) holds and \( P \) fails, a different situation. For example, "a number is divisible by \( 4 \) only if it is even" is true, while "a number is even only if it is divisible by \( 4 \)" is false (take \( 2 \)).

(b) "\( P \) unless \( Q \)" says that \( P \) holds in every situation except possibly those where \( Q \) holds. So once we know \( Q \) fails, we may conclude \( P \), which is \( \neg Q \to P \). For instance, "the equation \( ax = 1 \) has a solution unless \( a = 0 \)" says: if \( a \ne 0 \), then \( ax = 1 \) has a solution.

(c) The first sentence is \( (x = 2) \to (x^2 = 4) \). It is true for every \( x \): when \( x = 2 \), \( x^2 = 4 \), and when \( x \ne 2 \) it promises nothing.

The second is \( (x^2 = 4) \to (x = 2) \), the same two parts in the opposite direction. It is false for \( x = -2 \), where \( x^2 = 4 \) but \( x \ne 2 \).

The third is \( \neg(x = 0) \to (x^2 > 0) \), by (b). It is true for every \( x \): a non-zero real number is positive or negative, and in both cases its square is positive.

The first two sentences differ by one word, and they are implications in opposite directions. Confusing them is exactly the mistake in Argument B at the start of this section.
:::

::: {#exr-statements-and-proofs-c2}
[C2: Necessary and sufficient]

Let \( x \) be a real number.

::: {.enumerate options="label=(\alph*)"}
1. Write "\( x > 1 \) is sufficient for \( x^2 > 1 \)" and "\( x > 1 \) is necessary for \( x^2 > 1 \)" as implications.
2. Decide which of the two is true for every real \( x \), and give a value of \( x \) that makes the other false.
3. Find a condition on \( x \), written with \( \vee \), that is both necessary and sufficient for \( x^2 > 1 \). You may use that \( x^2 > 1 \) exactly when \( \abs{x} > 1 \).
:::
:::

::: {.solution}
(a) "\( P \) is sufficient for \( Q \)" means that \( P \) is enough to guarantee \( Q \), that is, \( P \to Q \). "\( P \) is necessary for \( Q \)" means that \( Q \) cannot hold without \( P \), that is, \( Q \to P \). So the two sentences are \( (x > 1) \to (x^2 > 1) \) and \( (x^2 > 1) \to (x > 1) \).

(b) The first is true for every \( x \): if \( x > 1 \), then \( x > 0 \), so \( x^2 = x \cdot x > 1 \cdot x = x > 1 \), where multiplying \( x > 1 \) by the positive number \( x \) keeps the inequality. The second is false for \( x = -2 \): then \( x^2 = 4 > 1 \) but \( x < 1 \).

(c) \( (x > 1) \vee (x < -1) \). It is sufficient: if \( x > 1 \) then \( \abs{x} = x > 1 \), and if \( x < -1 \) then \( \abs{x} = -x > 1 \); either way \( x^2 > 1 \). It is necessary: if \( x^2 > 1 \), then \( \abs{x} > 1 \), and \( \abs{x} \) is \( x \) or \( -x \), so \( x > 1 \) or \( -x > 1 \), the latter meaning \( x < -1 \).
:::
