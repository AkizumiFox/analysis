# Propositional Logic and Natural Deduction

A proof is an argument in which every step is licensed. Most readers meet proofs long before anyone tells them what the licenses are, and they learn them the way a child learns grammar: by imitation, with no way to settle a doubt. The doubts come soon enough. Here is an argument in which every sentence is true; why is it not a proof? Here is a "proof by contradiction"; what exactly was contradicted, and what did that establish? Why is "if \( x^2 < 0 \), then \( x = 7 \)" true, when no real \( x \) has \( x^2 < 0 \) and \( 7 \) has nothing to do with it?

This chapter answers such questions for the connectives "and", "or", "implies", "not" and "if and only if". It is a **calculus**: each connective gets a rule for proving it and a rule for using it, a proof becomes a derivation whose every line is checked against a rule, and the question "does this follow?" becomes "is there a derivation?". We learn the rules, learn to build derivations, and above all learn to search for them. The next three chapters build on this one. Chapter 3 asks whether the rules are *right*, and proves that they derive exactly what the truth tables say they should; Chapter 4 adds "for every" and "there exists"; Chapter 5 turns derivations back into the prose mathematicians write. From then on the rules go silent, but underneath, every proof in the book is still doing this.

**What you need.** School algebra only. Examples use facts about integers and real numbers, such as \( x^2 \ge 0 \) and "every integer is even or odd, and not both", as known; Chapter 11 proves the facts about real numbers from axioms.

**Time.** About 35 hours on the core track (all of A, one B and one C per section, the exit checks); about 45 hours for everything.

## Roadmap

- **Statements, connectives and the form of an argument.** What the sentences of a proof are, how connectives build them, how to find a statement's main connective, and the sequent as a claim about the form of an argument.
- **And, implies, and derivations.** The rules for conjunction and implication, boxes and their scope, the exact definition of a derivation and of \( \Gamma \vdash P \), and how to check a derivation line by line.
- **Or, and proof by cases.** The rules for disjunction, proof by cases on absolute values, and why the cases must exhaust.
- **Not, contradiction, and the contrapositive.** The rules for negation and contradiction, the first derived rules, the irrationality of \( \sqrt{2} \), and where vacuous truth comes from.
- **Iff, equivalence, and what a definition says.** The rules for the biconditional, provable equivalence, why a definition's "if" means "iff", and cycles of implications.
- **Proof by contradiction and the classical rules.** Reductio ad absurdum, double negation, excluded middle and De Morgan's laws, and why reductio, double-negation elimination and excluded middle stand or fall together.
- **How to find a derivation.** A goal-directed search method, worked searches, the rules in one place, and a search that fails, which leaves the question Chapter 3 answers.

## Named moves

- **Read the skeleton off the goal.** The goal's main connective chooses the introduction rule, and so the box to open.
- **Use a premise by its main connective.** Its elimination rule says what you may do with it.
- **Open a box, close a box.** An assumption lives exactly as long as its box.
- **Work from both ends.** Premises at the top, the goal at the bottom; fill the gap from both sides.
- **When stuck, assume the negation of the goal** (\( \rulename{RAA} \)), and hunt for a clash among the available lines.
- **Use a derived rule as one line.** A sequent already proved is a new rule.
