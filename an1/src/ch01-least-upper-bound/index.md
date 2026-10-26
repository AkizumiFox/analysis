# Ordered Fields and the Least Upper Bound Axiom

Calculus is full of theorems that feel too obvious to need proof. A continuous function that is negative at one end of an interval and positive at the other must vanish somewhere in between. An increasing sequence that stays below some fixed number must settle down to a limit. Both statements are **false** if "number" means "rational number". The polynomial \( x^2 - 2 \) is negative at \( 1 \) and positive at \( 2 \), yet no rational \( x \) makes it zero, because \( \sqrt 2 \) is irrational (@fd1:thm-sqrt2-irrational). The rational numbers \( 1, 1.4, 1.41, 1.414, 1.4142, \dots \), each the largest decimal of its length whose square is below \( 2 \), increase and never pass \( 1.5 \); yet there is no rational number for them to approach, since its square would have to be \( 2 \). The rational line has a gap where \( \sqrt 2 \) should be, and calculus falls into it.

This chapter finds the one property that separates the real numbers from the rationals: in \( \nR \), every nonempty set that is bounded above has a **least upper bound**. We take this property as an axiom and learn to use it. The main tool is a test for recognizing a least upper bound using small positive numbers \( \varepsilon \), which will be used throughout the book. From the axiom we derive the first facts that the rationals lack or that need the axiom: the natural numbers are unbounded, the rationals are dense, positive numbers have square roots and \( n \)-th roots, nested closed intervals always share a point, and the real numbers cannot be listed. We do not construct \( \nR \) here. *Number Systems: From \(\nN\) to \(\nR\)*, Chapter 5 builds it from \( \nQ \) by Cauchy sequences and proves the axiom as a theorem, as *Axiomatic Set Theory* does by Dedekind cuts; Chapter 11 of this volume shows that several other "no gaps" properties are equivalent to it.

**What you need.** From *Logic and Proof*, Chapter 1: proof by cases (@fd1:def-rules-disjunction). From *Logic and Proof*, Chapter 2: the irrationality of \( \sqrt 2 \) (@fd1:thm-sqrt2-irrational), the rules for negation (@fd1:def-rules-negation), and the contrapositive (@fd1:prp-contrapositive). From *Logic and Proof*, Chapters 4–8, and *Sets and Functions*, Chapters 1–4: induction (@fd1:ax-induction), quantifiers and how to negate them (*Logic and Proof*, Chapters 5 and 6), sets and images of sets (*Sets and Functions*, Chapters 1 and 2), the well-ordering of \( \nN \), definition by recursion, and the arithmetic of \( \nN \) and \( \nZ \) (*Sets and Functions*, Chapter 3), and countable sets (*Sets and Functions*, Chapter 4). No linear algebra is needed. The elementary rules of field arithmetic are either cited from the linear-algebra companion, Chapter 0, whose field axioms are ours, or proved in the first section.

**Time.** About 30 hours on the core track (all of A, one B, and one C per section, the exit checks); about 45 hours for everything.

## Roadmap

- **Ordered fields and the gap in the rationals.** The axioms that \( \nQ \) and \( \nR \) share, the rules for inequalities they imply, and absolute value with the triangle inequality.
- **Upper bounds, maxima and suprema.** The vocabulary for sets of numbers, and a proof that a bounded set of rationals can have no rational supremum.
- **The least upper bound axiom.** The single assumption that distinguishes \( \nR \) from \( \nQ \), and why infima then come free.
- **Working with the supremum.** The \( \varepsilon \) characterization of the supremum, sup approximation, and the rules for suprema of scaled sets and sums.
- **The Archimedean property.** Where \( \nN \) sits in \( \nR \), and the Archimedean property: \( \nN \) is not bounded above, which fails in some ordered fields.
- **Density of \( \nQ \) and the existence of roots.** A rational between any two reals, and \( \sqrt 2 \) (and every \( n \)-th root) constructed as a supremum.
- **Nested intervals, and why \( \nR \) is uncountable.** Shrinking closed intervals share a point, and no list contains every real number.

## Named moves

- **Split the supremum into its two properties.** To prove \( s = \sup A \), prove that \( s \) is an upper bound, and then that it is the least one.
- **Sup approximation.** "\( \sup A - \varepsilon \) is not an upper bound, so some \( a \in A \) exceeds it." With \( \varepsilon = \frac1n \) this gives \( a_n \in A \) with \( a_n > \sup A - \frac1n \).
- **Equality of suprema by two inequalities.** Prove \( \le \) by exhibiting an upper bound, then prove \( \ge \) with an \( \varepsilon \), splitting the budget as \( \varepsilon/2 + \varepsilon/2 \) when two sets are involved.
- **Construct a point as a supremum.** Define the set of points where "things are still fine", take its supremum, and rule out each way it could fail. The existence of \( \sqrt 2 \) is the first instance; the intermediate value theorem and the Heine–Borel theorem are proved the same way.
