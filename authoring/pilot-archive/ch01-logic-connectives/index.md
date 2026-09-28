# The Grammar of Proof I: Connectives and Natural Deduction

A proof is an argument in which every step is licensed. Most readers meet proofs long before anyone tells them what the licenses are, and learn them the way a child learns grammar: by imitation, with no way to settle a doubt. The doubt comes soon enough. Here is an argument in which every sentence is true; why is it not a proof? Here is a "proof by contradiction"; what exactly was contradicted, and what did that establish? Why is "if \( x^2 < 0 \), then \( x = 7 \)" true?

This chapter answers such questions for the five connectives: "and", "or", "implies", "not" and "if and only if". Each connective comes with two rules, one saying how to prove a statement built with it and one saying how to use such a statement once we have it. The rules are the moves careful mathematicians already make in prose, "assume \( P \) … hence \( Q \)", "in either case …", "this is a contradiction", so learning them changes how one reads proofs more than how one writes them. By the end of the chapter we can write, read and check any argument whose logic is built from connectives, and name the rule that each sentence uses or breaks. Truth tables, the usual starting point, come at the end, as a summary of the rules. Chapter 2 adds the quantifiers "for every" and "there exists", which is where analysis really lives.

**What you need.** Nothing beyond school algebra. Examples use facts about integers and real numbers, such as \( x^2 \ge 0 \) and "every integer is even or odd", as known; Chapter 8 proves the facts about real numbers from axioms.

## Roadmap

- **What a proof is made of.** Statements, the connectives and how to parse them, and the idea that every connective has a way to prove it and a way to use it.
- **And, implies, and the box.** The rules for conjunction and implication; assumptions, boxes and their scope; derivations and the notation \( \Gamma \vdash P \).
- **Or, not, and contradiction.** Proof by cases, the rules for negation and contradiction, the contrapositive, the irrationality of \( \sqrt{2} \), and where vacuous truth comes from.
- **Iff, and what a definition says.** The rules for "if and only if", proofs in two directions, why a definition's "if" means "iff", and proving several conditions equivalent by a cycle.
- **Proof by contradiction is a different rule.** Reductio ad absurdum, the one rule that removes a negation, and what only it can prove.
- **Truth tables summarize the rules.** Each connective's table read off its rules, tautologies and equivalence, and refuting an argument with a single row.
- **Reading the proof off the goal.** The goal's main connective chooses the skeleton of its proof; the full table of rules, phrases and their Lean counterparts; checking proofs line by line.

## Named moves

- **Read the skeleton off the goal.** Find the goal's main connective; it decides the first and last sentences of the proof.
- **Open a box, close a box.** "Assume \( P \)" opens a box in which \( P \) may be used; the box closes when its conclusion is drawn, and \( P \) may not be used after that.
- **Prove "not \( P \)" by assuming \( P \).** Assume \( P \), reach a contradiction, conclude \( \neg P \) (\( \rulename{\neg I} \)).
- **Prove by cases.** Use "\( P \) or \( Q \)" by reaching the same conclusion from \( P \) and from \( Q \) (\( \rulename{\vee E} \)); an impossible case is closed by \( \rulename{\bot E} \).
- **Use the contrapositive.** From "if \( P \) then \( Q \)" we get "if not \( Q \) then not \( P \)"; when a hypothesis gives nothing to compute with, work with the contrapositive of a fact that does.
