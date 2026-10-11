# Chapter 11 — S7 re-referee (fresh)

**Scope:** commit `7da2759` (`src`, `verify`, `authoring/STATUS.md`) against every finding of `ch10-S5-A.md`, `ch10-S5-B.md` and `ch10-S6.md` (Chapter 10 then; now `src/ch11-least-upper-bound/`), with their Resolution notes. The re-referee has not written or reviewed this chapter before. Verdicts recorded in `authoring/ledger/ch11.yaml` (stage S7r, by rereferee) on the 35 items carrying an S7 verdict.

**Gates re-run** (scratch copy, rsync without `.venv`/`_build`):
- `./build.py html`: 17/17 built. `@la:thm-field-basic-properties` renders "Linear Algebra, Theorem 0.7.1" and links to `ch00-foundations/07-fields.html`. The label resolves only when `../linear-algebra/_build/crossref_labels.json` exists next to the repo (`config/config.json`). In a copy without that sibling, the filter prints the bare label "Linear Algebra, thm-field-basic-properties" **with no warning** (`ext.available` false). This is an engine note, not a Ch 11 finding: a release build from a copy without the sibling would ship the raw label silently.
- `python3 tools/check_numbers.py`: 89 sidecars, 0 fatal, 4 advisories (Ch 1). All 50 `verify/ch11/*.py` exit 0. The `verify` hunks of the commit only change "Ch 10" to "Ch 11" in docstrings.
- `check_structure.py`: 0 fatal, 4 advisories (§07 is now 5,193 words, as the Resolution says). `check_forward_deps.py`, `check_optional.py`, `check_notation.py` and `check_rendered.py` are clean. `promises.py --reconcile`: 0 unrecorded. `ledger.py stale 11`: 0.
- The renumbering commit `41db9a3` changes only chapter numbers in Ch 11 (word diff against the old `ch10` files), so the S7 items touched only by it need no mathematical re-check.

**Counts:** 33 finding rows re-checked (4 from A, 21 from B, 8 from S6). Fixed correctly: 32. Fixed but introduced a new problem: 1 (R4, minor). Not fixed: 0 (two nits left by choice, listed at the end).

## The Archimedes proof (`thm-naturals-unbounded`), end to end

I read the rewritten proof in an arbitrary ordered field \(F\) satisfying the LUB axiom, with intuitionistic rules inside the ¬I box.

1. Assume ℕ is bounded above. 1 ∈ ℕ, so the axiom gives s = sup ℕ. Both hypotheses of the axiom are used. Correct.
2. Fix n ∈ ℕ. ℕ is inductive, so n + 1 ∈ ℕ. By (S1), n + 1 ≤ s. Adding −1 (rules (b)) gives n ≤ s − 1. Since ≤ is "< or =", this is a case split on a disjunction we already have, so it is direct. Then ∀-introduction: s − 1 is an upper bound. Correct.
3. (S2) with M = s − 1 gives s ≤ s − 1, hence 1 ≤ 0. With 0 < 1 (rules (e)), each disjunct of 1 ≤ 0 contradicts the exclusivity clause of (O1). This reaches ⊥ without excluded middle. Correct.
4. ¬I closes the box: ℕ is not bounded above.
5. Last paragraph: ¬∀n (n ≤ x) ⇒ ∃n ¬(n ≤ x) is the classical law, flagged correctly. ¬(n ≤ x) ⇒ n > x comes from trichotomy as a disjunction axiom (O1), which is intuitionistically fine.

So every step inside the box is direct, as the remark claims. The remark also says the proof has exactly **one** classical step, and that is true. The Idea matches. The ℝ(x) bullet list ("The remaining lines … use only the ordered-field axioms and that ℕ is inductive") and the sentence "the middle paragraph of the proof … with M in place of s" now match the proof word for word. Nothing else in the chapter describes the old "s − 1 is not an upper bound" route: I grepped for `s - 1`, `not an upper bound` and `thm-naturals-unbounded`. A1(d)'s answer (axiom at "ℕ has a supremum s"; inductive at "n + 1 ∈ ℕ") is still right.

**C1(a).** The model solution is the same argument. It cites (S1) for n + 1 ≤ s, which the text proof leaves implicit, and the solution is better for it. The marking scheme adds up to 1 + 2 + 2 + 1 + 1 + 2 + 1 = 10. The two (a)-steps worth 2 + 1 = 3 are exactly the direct route. The new fatal error ("omitting 'for every n'") targets the real pitfall of that route. The classical variant is accepted for the same 3 points, with a correct note that it adds a classical step inside the box. This is consistent with the remark. Nit: the solution's last sentence ("which means that every x … is exceeded") passes over the classical unwinding without naming it. That is acceptable in a model solution.

## S5 Referee A

| Finding | Verdict | Evidence |
|---|---|---|
| 05:86 `thm-naturals-unbounded` (error) | fixed correctly | See the section above. The preferred fix was taken, and the remark is now true. |
| 05:300/311 C1(a) solution and scheme | fixed correctly | See the section above. |
| 05:157 `exm-nonarchimedean-field` (minor) | fixed correctly | 05:153 now says the example uses the ordered-field rules in ℝ(x) and so rests on @exr-archimedean-property-c2. There is a ledger line. It is an example, not a proof, so STYLE's no-proof-on-exercise rule is respected. |
| 01:381 `exr-ordered-fields-c1` (minor) | fixed correctly | (m + n)·1 = m·1 + n·1 by induction on n. The base case is the recursive definition. Step: ((m + n) + 1)·1 = (m + n)·1 + 1 = m·1 + n·1 + 1 = m·1 + (n + 1)·1 (definition, induction hypothesis, (F2), definition). Valid. Ledger lines added (ch03 for induction, ch07 for (m + n) + 1 = m + (n + 1)). |

## S5 Referee B

| Finding | Verdict | Evidence |
|---|---|---|
| R1 (gap) promise bookkeeping | fixed correctly | The STATUS rows for Ch 3 (induction), Ch 6 (intersection of a family), Ch 7 (§01, §03, §05, §06, §07 items), Ch 8 (union of two countable sets, countable subsets) and Ch 14/16 (§07 C4) are present. `promises.py --reconcile`: 0 unrecorded. The targets exist in the blueprints: `ax-induction` (ch03), `def-family-union-intersection` (ch06), `prp-union-two-countable` and `prp-countable-subset` (ch08, with explicit pay rows for Ch 11 §07). |
| R2 induction credited to Ch 7 | fixed correctly | 05:58, index, §01 C1 hint and 02:169 now say Chapter 3. The Ch 3 blueprint states `ax-induction` as a basic property, and Ch 7 proves well-ordering (`thm-well-ordering`). The ledger sources were switched to `ch03`. The Ch 7 → Ch 11 `def-supremum` clause is recorded in STATUS. |
| R3 promises to Ch 12 | fixed correctly | 04:123 reworded. The Ch 12 blueprint line 7 names "Cauchy completeness" and "sup approximation", so 03:28 and 04:123 are both backed. |
| R4 `lem-field-algebra` re-proves LA | **fixed, new problem (minor)** | The citation resolves (LA Theorem 0.7.1). LA's (F1)–(F9) match @def-ordered-field item for item, and LA's (a), (c), (d), (f) cover the dropped parts (a), (b), (d). The −(−a) = a line is correct. **New problem:** LA proves in its text only the uniqueness of 0 and of −a, cancellation, 0·a = 0 and (f). The uniqueness of **1** and of **a⁻¹** is left to LA's `exr-fields-b1` (LA 07-fields.md:76, 426–431). So "the proofs there apply verbatim" is not accurate for those two parts, and part (a) now rests, one step removed, on an exercise (STYLE checklist: "No proof … rests on an exercise"). The chapter uses uniqueness of inverses, for example (ε⁻¹)⁻¹ = ε in `cor-archimedean-epsilon` via rules (f), and in the fraction arithmetic "used without comment". The old proof covered these ("the same arguments with (F5)–(F8)"). **Fix:** prove the two in one line each inside the proof, mirroring −(−a) = a (e.g. 1′ = 1′·1 = 1·1′ = 1; b = b(a c) = (b a) c = c for two inverses b, c of a), and cite LA only for 0, −a, 0·a and (d). Nit: the Idea's "Part (a) is the uniqueness, and the other parts use it" now describes LA's proofs more than this one. |
| R5 notation | fixed correctly | (a) The table row reads "positive q with q² < 2". (b) The NOTATION rows are routed to the coordinator in STATUS, and lc is defined where it is used (05:347, 07:323). This is acceptable at S7, since NOTATION is the coordinator's file. |
| R6 blueprint deviations | fixed correctly | Recorded in STATUS "Blueprint deviations". The new §07 C2(c) is correct: if (x, y) ⊆ C, then (x, y) is countable as a subset of a countable set, which contradicts (a). The item is fair, a two-line corollary of (a) in the pattern of (b), and (b) is the case C = ℚ as stated. |
| R7 roadmap | fixed correctly | index: "The Archimedean property." |
| R9 nits | fixed correctly | Titles now "C2: Exit check: sums of sets" and "C1: Exit check: the Archimedean property, and a circular proof". (ii) and (iii) were left by choice, which is permitted (optional). |
| 07:454 R3 | fixed correctly | Cites @exm-ordered-fields-q-r. Ledger line added. R2's (t²)² = t⁴ is ledgered (ch07 power laws). |
| 07:324, 330 C3 | fixed correctly | Both choices cite @thm-naturals-unbounded. The polynomial degree and lc facts are ledgered. |
| 07:260 C1 | fixed correctly | Ledger adds the induction of (b) (ch03), ℕ inside F (@exr-ordered-fields-c1) and 2 > 0 (rules (h)). |
| 07:211 B1 | fixed correctly | Ledger line "no integer strictly between k and k + 1" (ch07, recalled in the §05 remark). |
| 07:138 remark | fixed correctly | "√2 + q for rational q (the proof of @cor-irrationals-dense)". That proof does show √2 + q is irrational. |
| 06:204 and related | fixed correctly | Pointer to the §05 remark ("a positive integer is a natural number" is proved there). "⌊nx⌋ + 1, an integer, since sums of integers are integers" is ledgered. Σ by recursion is ledgered. |
| 05:155 naturals of ℝ(x) | fixed correctly | Two inclusions. The constants {n : n ∈ ℕ} form an inductive subset of ℝ(x), so ℕ_{ℝ(x)} ⊆ constants. For any inductive I ⊆ ℝ(x), {n ∈ ℕ : n ∈ I} is an inductive subset of ℝ, hence all of ℕ. Valid. The ledger source is updated. |
| 03:26 | fixed correctly | "…together with the logic and set theory of Part 0 (including, where it is flagged, a choice principle)". This is now consistent with 04:123. |
| 02:117 | fixed correctly | Three failure modes named. "The rest of this section shows the last two" is true: ∅ at 02:174 and the gap at @thm-no-rational-sup-sqrt2. |
| 01:398 | fixed correctly | As in A above. |
| 03:139 | fixed correctly | The test "holds in every ordered field" (true, 04:56). The sup pattern is claimed for Archimedes (set ℕ), roots and nested intervals (α = sup{aₙ}), and each fits. Density "with no new supremum" is true. |
| 02:7 | fixed correctly | Points to Case 1 of the proof and to @exr-suprema-c1, which proves the claim. |
| Nits 02:3, 01:285, 01:167, 01:252 | fixed correctly | "(as @thm-sqrt2-exists will prove)"; "can be strict"; "in this chapter"; \|4 − 3x\| = \|−3\|\|x − 4/3\| by rules (b), a correct citation. |

## S6

| Finding | Verdict | Evidence |
|---|---|---|
| 1 `exr-ordered-fields-c1` (c) | fixed correctly | As above. |
| 2 `exr-ordered-fields-b3` (b) | fixed correctly | New paragraph "Comparing by squaring": (g) needs a, b ≥ 0, and both absolute values are ≥ 0 by abs-rules (a). \|u\|² = u² is abs-rules (b). The chain \|x − 2\| < \|x\| ⇔ (x − 2)² < x² ⇔ 4 < 4x ⇔ x > 1 is correct, and every step is an equivalence. It models B2(b) and B3(b) without answering them: B3(b) is \|x − 1\| < \|x + 1\|, answer (0, ∞). |
| 3 `exr-the-axiom-c1` (a) | fixed correctly | 03:35 no longer names the witness. C1(a) now asks "exactly a witness, or adapted?", and the solution answers it (no adaptation needed). Fair. |
| 4 `exr-epsilon-characterization-c1` Hint 2 | fixed correctly | The hint now names tools by role only. The key step (b·sup A ≤ sup(AB), then vary b) is left to the reader. |
| 5 `check:07-nested-intervals:1` | fixed correctly | (0, 1/n] is a witness: x ≤ 0 is not in (0, 1], and for x > 0, @cor-archimedean-epsilon gives 1/n < x. [0, 1/n) is not a witness: 0 is in every interval, and it is nested, bounded and not closed. The table gives neither answer. Correct and fair. |
| 6 `exr-nested-intervals-c1` Hint 2 | fixed correctly | Now a question. It no longer chooses n. |
| 7 C1 scheme allowance | fixed correctly | "through the backward direction of @thm-sup-epsilon, rerun in F … citing it as a theorem about ℝ is not enough". The backward direction's proof (04:50–58) uses only ordered-field steps, so rerunning it in F is valid. |
| 8 `exr-nested-intervals-c3` Hint 2 | fixed correctly | Cut to "suppose deg p ≤ deg q, and look for an N ∈ ℕ with f < N". The choice of N stays in the solution, where it now cites @thm-naturals-unbounded. |

## Open after this re-check

- **R4 (minor, new):** prove the uniqueness of 1 and a⁻¹ inline in `proof:lem-field-algebra` (or change the wording so the proof no longer rests on LA's exercise). Re-referee that one hunk.
- Nits left by choice (no action required): R9 (ii)/(iii). R10's nit, that Ch 1 says "non-negative" reals have square roots while `thm-nth-root` is stated for a > 0 (a = 0 is trivial but unstated), has no Resolution entry. It is a Ch 1 / Ch 11 seam item for S8.
- Engine note for the coordinator: a missing `../linear-algebra/_build/crossref_labels.json` makes `@la:` references render as bare labels without a warning.
