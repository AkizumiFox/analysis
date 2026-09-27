# The self-teaching reader: how to travel the route, and what the book should do (research record)

Written 2026-09-28. This is a research report. It changes no decision on its own: anything adopted from it goes into `decisions.md`, `STYLE.md`, `config/config.json` or the blueprints, with a reason.

**What it covers.** Evidence on learning proof-based mathematics without a teacher, and on how well self-study resources actually work. Then recommendations for this book:
- pacing and weekly plans;
- a gate exam for each Part;
- spaced and interleaved review;
- new exercise formats;
- the `reading-paths` entries;
- additions to `STYLE.md`.

**How claims are tagged.** Every recommendation is tagged:
- **[E]**: it follows from the cited evidence;
- **[E→]**: an extrapolation from evidence gathered in a different population, usually school pupils or first-year courses rather than an adult working alone through graduate analysis;
- **[O]**: opinion or design judgement.

Most of the strong evidence comes from settings unlike ours. The tags say how far each claim travels.

---

## Part A. Findings

### A1. Transition to proof: what goes wrong for a beginner

- **Three sources of difficulty.** Moore (1994) followed students in transition-to-proof courses. Their difficulties came from three places:
  - understanding concepts: knowing a definition but not how to *use* it in an argument;
  - mathematical language and notation, especially quantifiers;
  - not knowing how to start a proof.

  ([Moore 1994, *ESM* 27](https://link.springer.com/article/10.1007/BF01273731))
- **Strategic knowledge.** Students who *know* the relevant facts still fail to prove things because they lack strategic knowledge: which theorem to reach for, and which proof technique a statement's form calls for ([Weber 2001, *ESM* 48](https://link.springer.com/article/10.1023/A:1015535614355)).
  - This is the case for the chapter-level "Named moves" list that Chapter 8's index already has.
- **Scope of variables.** Dawkins and Roh's line of work finds the scope of variables to be a persistent obstacle: "fixed but arbitrary" objects, and the pairwise dependence hidden in nested quantifiers.
  - They teach logic through set-based meanings and questions about scope, not as a separate formal calculus.
  - Sources: [Dawkins & Roh, PRIMUS 2025](https://www.tandfonline.com/doi/abs/10.1080/10511970.2025.2518524); [Texas State RUME papers](https://rume.txst.edu/papers.html).
  - This supports decision 1 (logic practised inside analysis) and Part 0's eigenvariable and "δ depending on x" material.
- **Undergraduates cannot reliably tell whether an argument is a proof.**
  - Selden & Selden (2003): students attend to surface features, and their ability to judge validity is "very limited" ([JRME 34(1)](https://pubs.nctm.org/view/journals/jrme/34/1/article-p4.xml)).
  - Weber (2010): 28 mathematics majors who had *completed* a transition-to-proof course often accepted invalid deductive arguments as proofs, and most accepted a diagrammatic argument as a proof ([MTL 12](https://sites.math.rutgers.edu/~jpmejia/files/Weber_(2010MTL).pdf)).
  - **For a self-learner this is the central problem.** The person checking the proof is the person least able to check it.
- **Experts read proofs differently.**
  - In eye-tracking, mathematicians move back and forth between consecutive lines, inferring the implicit warrant for each step. Novices dwell on surface features.
  - Mathematicians also sometimes disagree about whether short purported proofs are valid.
  - Source: [Inglis & Alcock 2012, JRME 43](https://eric.ed.gov/?id=EJ977681).
- **Proof reading strategies of successful students.** Weber (2015) watched successful mathematics majors reading proofs. They used five strategies:
  1. try to prove the theorem before reading the proof;
  2. identify the proof framework;
  3. break the proof into sub-proofs;
  4. illustrate hard assertions with an example;
  5. compare the proof's method with one's own.

  Most of 83 surveyed mathematicians wanted students to use these strategies ([IJRUME 1](https://link.springer.com/article/10.1007/s40753-015-0011-0)).
- **What "understanding a proof" means.** Mejía-Ramos et al. (2012) give a seven-part model with *local* and *holistic* dimensions:
  - local: meaning of terms and statements, justification of claims, logical structure;
  - holistic: summarising the high-level idea, identifying the modular structure, transferring the general method, illustrating with examples.

  It is a ready template for comprehension questions that can be checked without a grader ([ESM 79](https://eric.ed.gov/?id=EJ948400)).

### A2. Interventions with evidence

| Intervention | Evidence | Population / caveat |
|---|---|---|
| **Self-explanation training** (a short booklet on explaining each line in terms of earlier lines and definitions) | Better proof comprehension, **d = 0.95** in Exp. 1. More back-and-forth reading in Exp. 2. A **15-minute** self-study version helped, and the effect persisted at delayed test ([Hodds, Alcock & Inglis 2014, JRME 45](https://eric.ed.gov/?id=EJ1028348); [the Loughborough booklet](https://www.lboro.ac.uk/media/media/schoolanddepartments/mathematics-education-centre/downloads/SE-booklet-guide.pdf); [Alcock et al. 2015, Notices AMS 62](https://repository.lboro.ac.uk/articles/journal_contribution/Investigating_and_improving_undergraduate_proof_comprehension/9369368)) | First-year UK undergraduates. The training is the intervention, not the prompts alone. **Directly transferable**, because it is self-study by design. |
| **Narrated or animated proofs ("e-Proofs")** | Same immediate comprehension as a static written proof, **worse retention**. Eye-tracking showed less processing effort while the narration was off ([Roy, Inglis & Alcock 2017, ESM 96](https://link.springer.com/article/10.1007/s10649-017-9754-7)) | A warning against making proofs *easier to watch*. Effortful reading is the point. |
| **Worked examples, then fading** | Removing worked steps one at a time (backward fading works best) reliably improves near transfer. Adding prompts to name the principle behind each step gave medium-to-large effects on near *and far* transfer at no extra time ([Atkinson, Renkl & Merrill 2003, JEP 95](https://asu.elsevierpure.com/en/publications/transitioning-from-studying-examples-to-solving-problems-effects-/); [Renkl et al., cognitive-load account](https://link.springer.com/article/10.1023/B:TRUC.0000021815.74806.f6)) | Mostly probability and algebra problems. For proofs: [Bickerton & Sangwin 2020/22, faded proofs in STACK](https://arxiv.org/abs/2006.01581). |
| **Expertise reversal** | Guidance that helps novices can *hurt* learners with more knowledge ([Kalyuga 2003/2007](https://link.springer.com/article/10.1007/s10648-007-9054-3)) | Scaffolding should shrink across the book: Part 0 ≠ Part VI. |
| **Retrieval practice and spacing** | Rated "high utility", the only two techniques to earn it among ten ([Dunlosky et al. 2013, PSPI](https://pubmed.ncbi.nlm.nih.gov/26173288/)). In college mathematics, spaced retrieval in precalculus improved the *later calculus course* ([Hopkins et al. 2016, EPR 28](https://link.springer.com/article/10.1007/s10648-015-9349-8)). More spacing raised end-of-term scores by about 5 points and cost immediate performance ([Lyle et al. 2020, EPR 32](https://eric.ed.gov/?id=EJ1245263)) | Engineering precalculus and calculus: procedural, not proof. |
| **Optimal gap** | The best gap between study and review grows with the retention interval: about **20–40%** of a one-week horizon, about **5–10%** of a one-year horizon ([Cepeda et al. 2008, Psych. Sci. 19](https://journals.sagepub.com/doi/abs/10.1111/j.1467-9280.2008.02209.x)) | Facts, not proofs. Treat it as a rule of thumb for scheduling. |
| **Interleaving** | A cluster-randomised trial with 787 students: interleaved practice 61% versus blocked practice 38% on a test a month later, **d = 0.83** ([Rohrer et al. 2020, JEP 112](https://eric.ed.gov/?id=EJ1237752)) | Grade 7. The mechanism, choosing the method rather than being told it, is exactly what an analysis student lacks (Weber 2001). |
| **Mastery learning** | A meta-analysis of 108 controlled evaluations found positive effects, **larger for weaker students**, and noted **increased time on task** ([Kulik, Kulik & Bangert-Drowns 1990, RER 60](https://journals.sagepub.com/doi/10.3102/00346543060002265)) | Group instruction with corrective loops. The time cost matters for an adult working alone. |
| **Productive failure** (try the problem before instruction) | Moderate advantage, **g = 0.36**, rising to 0.37–0.58 with high-fidelity designs, on conceptual knowledge and transfer ([Sinha & Kapur 2021, RER 91](https://journals.sagepub.com/doi/10.3102/00346543211019105)) | Mostly school STEM, and it reverses for young children. Consistent with Weber's strategy (i). |
| **Tutoring** | Human tutoring **d = 0.79**; step-based computer tutors **0.76**, nearly as good; answer-only systems much less ([VanLehn 2011, Ed. Psych. 46](https://eric.ed.gov/?id=EJ946764)) | Feedback on *steps*, not only on final answers, is what carries the effect. |
| **AI tutors** | A research-designed AI tutor beat an active-learning class in a Harvard physics RCT ([Kestin et al. 2025, Sci. Rep. 15](https://www.nature.com/articles/s41598-025-97652-6)). Unrestricted GPT-4 raised practice scores, but students did **17% worse** once it was withdrawn; a tutor with guardrails largely removed the harm ([Bastani et al. 2025, PNAS](https://www.pnas.org/doi/10.1073/pnas.2422633122)) | Design decides the sign of the effect. |
| **LLM grading of proofs** | In a Princeton proof-based course, LLM–TA agreement on solution quality was **63–67%**, against **87%** between two TAs. The LLM was too strict, penalised deviations from the reference solution, and got worse on later sub-parts ([Mahinpei et al. 2026](https://arxiv.org/html/2602.23635)). Problem-specific **marking schemes** make LLM graders close to experts on olympiad proofs ([ProofBench/ProofGrader 2025](https://proofgrader.github.io/); [RefGrader](https://lacuna.tiptreesystems.com/work/refgrader-automated-grading-of-mathematical-competition-proofs-using-agentic/wrk_9b1fbda008fb7660bad780522c31b166)) | An AI verdict is a second opinion, and far better when handed a rubric. |
| **Proof Blocks** (Parsons problems for proofs: put given lines in order, with distractors, graded against a dependency graph) | About as informative as written proofs as exam items. An RCT with 332 students on induction proofs studied their learning efficiency ([Poulsen et al. 2021/2023](https://arxiv.org/abs/2106.11032); [SIGCSE 2023](https://arxiv.org/pdf/2211.09609)) | Discrete mathematics. Fully auto-gradable, and the *only* auto-gradable proof-*construction* format with evidence. |

### A3. Completion: most self-learners stop

- **edX.** From 2012 to 2018, 52% of registrants never started, and completion fell to **3.13%** by 2017–18 ([Reich & Ruipérez-Valiente 2019, Science 363](https://www.science.org/doi/10.1126/science.aav7958)).
- **Devlin's *Introduction to Mathematical Thinking*** (Coursera 2013), a transition-to-proof MOOC:
  - 27,930 enrolled;
  - about 4,000 were still active in the final week;
  - 1,950 statements of accomplishment were issued (about 7%).

  Its proof exam was peer-graded against a rubric, and graders were first filtered by marking sample answers ([report](https://schmoller.net/fm.schmoller.net/2013/06/second-report-from-keith-devlins-itmt-course.html)).
- **Light-touch nudges barely help.** Plan-making prompts in 247 Harvard/MIT/Stanford courses with 250,000 students gave small effects that faded after the first weeks ([Kizilcec et al. 2020, PNAS 117](https://www.pnas.org/doi/10.1073/pnas.1921417117)).
- **Self-regulation is a weak predictor.** Across online higher education, time management (r ≈ .14), effort regulation (r ≈ .11), metacognition and critical thinking are significant but *weak* correlates of achievement ([Broadbent & Poon 2015](https://iastate.pressbooks.pub/onlinelearningtoolbox/chapter/broadbent-poon-self-regulated-learning-strategies-academic-achievement-in-online-higher-education-learning-environments-a-systematic-review/)).

**Implication [E→]:** assume most readers will not finish 72 chapters. The book should make **stopping points valuable**: each Part should be a complete course with its own certificate-like gate. Its structure, not motivational prose, should carry the reader forward.

### A4. How successful self-study resources are built (descriptive, not causal)

- **MIT OCW 18.100A.**
  - It pairs lecture notes with **12 weekly problem sets, a midterm and a final** ([OCW](https://ocw.mit.edu/courses/18-100a-real-analysis-fall-2020/pages/assignments-and-exams/)).
  - Self-learners who report success almost always treat the psets as a weekly deadline.
  - The unit is the *week*, not the chapter.
- **Tao's advice** ([career advice](https://terrytao.wordpress.com/career-advice/)):
  - "ask yourself dumb questions — and answer them";
  - "learn and relearn your field";
  - rigour first, then "post-rigorous" intuition.

  Re-reading on a spiral is a deliberate method, not a failure.
- **Rigetti's *So You Want to Study Mathematics*** ([guide](https://www.susanrigetti.com/math)) and Chicago-style bibliographies.
  - They chose books *for independent study*: complete solutions, gentle proofs, sequencing.
  - They give roadmaps, not schedules.
  - Readers of them on HN and similar forums report stalling at the first hard proof course with no feedback. Anecdotal.
- **Self-study advice** in the Math.SE and graduate-study vein ([e.g. Stange](https://math.colorado.edu/~kstange/teaching-resources/grad/gradstudy.pdf)):
  - multiple passes;
  - do not confuse familiarity with understanding;
  - work examples for every theorem;
  - pinpoint confusion by writing the question down;
  - use complete solutions, but only *after* an attempt.
- **Lean's Natural Number Game** (Buzzard): 79 levels across 9 worlds of induction and rewriting proofs, each with **instant, certain feedback**. The Lean game server now hosts 8 games, including real analysis ([Imperial](https://github.com/ImperialCollegeLondon/natural_number_game); [Lean](https://x.com/leanprover/status/2052133670434320640)). No learning-outcome RCT exists, but it is the only form of free, reliable proof feedback.
- **STACK and Numbas.**
  - They auto-grade algebraic answers and "reasoning by equivalence" chains.
  - For proof they rely on comprehension questions, faded proofs and example-generation tasks ([Sangwin 2020](https://webhomes.maths.ed.ac.uk/~csangwin/Publications/2020-Proof-Assessment.pdf)).
  - Their lesson: most of what can be checked about a proof can be asked as a question with a checkable answer.
- **Math Academy's FIRe.** Its spaced-repetition model credits *implicit* review: practising an advanced topic partly reviews the prerequisites it uses, so explicit review is scheduled only for what is not exercised downstream ([Skycak](https://www.justinmath.com/individualized-spaced-repetition-in-hierarchical-knowledge-structures/)). This book already has the graph needed for that: hard citations in `crossref_labels.json`.
- **Brilliant.** Short interactive items with instant feedback. I found no published outcome evidence for proof-level material, so nothing is drawn from it except that answer-checkable micro-items keep people moving. [O]

### A5. Summary of what works without a teacher

1. **Feedback on each step, not only on the final answer**, carries most of the benefit of tutoring (VanLehn). Without a teacher the book must supply step-level checks: Quick checks, comprehension questions, ordering and fading items, and rubrics.
2. **The self-learner cannot yet judge a proof** (Selden & Selden, Weber 2010). Train the judgement explicitly, with self-explanation, proof verification and rubrics, rather than assuming it.
3. **Retrieval, spacing and interleaving** are the best-supported general techniques, and the book as written has none of them past the section boundary. Every exercise tests the section it sits in.
4. **Completion is the binding constraint.** Weekly units, deadlines, gates and meaningful exits matter more than exhortation.

---

## Part B. Recommendations

### B1. How much work the route is (pacing)

**Basis for the estimate [O, to be calibrated].**
- **Size of a chapter.** The pilot chapters are about 25k words of prose each, in 7 sections, with about 6 exercises per section (roughly 40 per chapter, most with parts).
- **Reading.** Careful reading with self-explanation and Quick checks runs at about 15 min per 400-word page of proof-dense text. That is **12–15 h** per chapter.
- **Exercises.** At 20–45 min each, *all* the exercises are **15–30 h**.
- **Core track: ≈ 25 h per chapter.** All A items, one B and one C per section, and the chapter's exit checks.
- **Full track: ≈ 35–45 h per chapter.** Every exercise.

**Cross-check against university loads.**
- MIT 18.100A: 12 psets in about 14 weeks at 12 units, i.e. about 12 h a week or roughly 170 h per course.
- Cambridge Analysis I: 24 lectures, about 100–130 h with example sheets.
- The book's Part I has 11 chapters (8–18), about 275 h on the core track. It covers more than Analysis I (series, power series, the forms of completeness) and has no lecturer, so a factor of 1.5–2 over a lecture course is plausible.

**The plan should measure this rather than trust it:**
- ask pilot readers to log hours per section;
- publish the median on each chapter's index as "about N hours";
- update it as data comes in.

**Totals on the core track.**

| | Chapters | Core hours (≈ 25 h/ch) |
|---|---|---|
| Part 0 main (1–5) | 5 | 125 (two-year bridge: ≈ 75, reading selected sections) |
| Part I (8–18) | 11 | 275 |
| Part II (21–31) | 11 | 275 |
| Part III (32–38, 40) | 8 | 200 |
| Part IV (41–51) | 11 | 275 |
| Part V (52–59) | 8 | 200 |
| Part VI (60–66, 68–72) | 12 | 300 |
| **Main line** | **66** | **≈ 1,600–1,650** |
| Optional (6, 7, 19, 20, 39, 67) | 6 | +150 |

**Finding [O, from the table]:** stage S3 as `decisions.md` describes it (Parts IV and V in one semester) is **19 chapters, about 475 h, or about 32 h a week for 15 weeks**. Every other stage is about 18–20 h a week. The two-year route should **run IV and V one after the other** ("or after it", as `decisions.md` already allows), not in parallel.

#### Two-year route: about 20 h a week (a half-time student's load)

96 study weeks plus about 8 weeks of breaks. The weeks per Part include one gate week each.

| Weeks | Part | Chapters | Pace |
|---|---|---|---|
| 1–4 | 0 bridge | Ch 1–5, selected sections (skip Ch 2's final two sections and the Lean table's depth, and read Ch 4 §01–§04 and Ch 5 §01–§04) | ≈ 1.3 ch/wk |
| 5 | Gate 0 | | |
| 6–19 | I | Ch 8–18 | 0.8 ch/wk |
| 20 | Gate I | | |
| 21–34 | II | Ch 21–31 | 0.8 ch/wk |
| 35 | Gate II | | |
| 36–45 | III | Ch 32–38, 40 | 0.8 ch/wk |
| 46 | Gate III | | |
| 47–60 | IV | Ch 41–51 | 0.8 ch/wk |
| 61 | Gate IV | | |
| 62–71 | V | Ch 52–59 | 0.8 ch/wk |
| 72 | Gate V | | |
| 73–87 | VI | Ch 60–66, 68–72 | 0.8 ch/wk |
| 88 | Gate VI = Ch 72 §08 (mixed qual) | | |
| 89–96 | slack / qualifying-exam review (see B3) | | |

#### Three-year route: about 12–13 h a week (a working adult)

All 72 chapters, including the optional constructions, over about 140 study weeks. About 0.5 chapters a week, so a 7-section chapter takes two weeks.

| Year | Weeks | Content |
|---|---|---|
| 1 | 1–14 | Part 0, all 7 chapters, plus Gate 0 |
| 1 | 15–44 | Part I (Ch 8–18, 19–20), plus Gate I |
| 2 | 45–68 | Part II, plus Gate II |
| 2 | 69–86 | Part III (with Ch 39 optional), plus Gate III |
| 3 | 87–110 | Part IV, plus Gate IV |
| 3 | 111–126 | Part V, plus Gate V |
| 3–4 | 127–150 | Part VI (with Ch 67), plus the Gate VI capstone |

Three years at 13 h a week lands close to the two-year total. The difference is that the three-year reader has time for the **full track** (all C items) in Parts 0–I, where the habits form. [O]

#### Measure-only: about 10–12 h a week, one long semester

This reader already has, or wants only enough of, real analysis.
1. **Weeks 0–2: entry diagnostic.**
   - Take Gate I and the metric-space half of Gate II.
   - Each failed item links to sections, per B2; read exactly those, using the `measure-only` path page's list of what to read.
2. **Weeks 3–26: Part IV, Ch 40–51**, at about 0.5 chapters a week. Ch 40 is the motivation, and Ch 41 is read only as far as the path requires.
3. **Weeks 27–28: Gate IV.**

About 300 h in all. A reader starting from zero should instead take the two-year route through Part II, then Part IV. The path page shows why: its closure pulls in most of Parts I–II.

#### A week's rhythm (for every route) [E→ spacing and retrieval; O for the split]

| Session | Share | Content |
|---|---|---|
| 1–2 | 35% | Read a section. Attempt each theorem for 5–10 minutes before reading its proof (see B4.6). Do every Quick check and self-explanation prompt *in writing*. |
| 3 | 30% | Exercises: all of A, one B, one C. Attempt before looking; open the hint ladder one rung at a time. |
| 4 | 15% | **Review block** (see B3): this chapter's R items, plus the book-wide review set due this week. |
| 5 | 20% | Write up one proof in full, grade it against the rubric (B4.8), and fix it. Keep an **error log** of the rule broken or the hypothesis missed. |

**Rule for moving on [E mastery learning, capped per O].** Move on from a chapter when:
- every A item is right;
- at least one B and one C per section are done without the solution;
- one exit check, re-attempted after 48 hours or more, succeeds.

If after a week you still cannot, **move on anyway** and mark the section for the next review block. Mastery loops cost time (Kulik et al.), and for an adult working alone, stalling is the likeliest way to drop out (A3).

### B2. Checkpoints and a gate exam for each Part

**Three levels of checkpoint [O on structure; E on retrieval and feedback].**
1. **Section: Quick checks and A1 (exist).** Immediate answers with no grading.
2. **Chapter: exit checks (exist, decision 15).** Recommended additions:
   - label them **"Exit check"** in the exercise title;
   - give each a **marking scheme** (B4.8), so the reader can grade their own proof or have an AI grade it;
   - put "Re-attempt after 48 h" in the rhythm, not in the book text.
3. **Part: a Gate.** A new final section in the last main-line chapter of each Part. There is precedent: Ch 18 §06 is already "Part I review", and Ch 72 §08 is already "a mixed qualifying exam".

| Gate | Where it goes | Format |
|---|---|---|
| Gate 0 | Ch 5, new §07 | 2 h, 6 problems: formalise and negate a three-quantifier statement; a Fitch derivation turned into prose; find the error (name the rule); an induction proof; a preimage identity; a diagonal argument |
| Gate I | Ch 18 §06 (convert the existing review into a gate) | 3 h, 8 problems at the floor of the UCLA qualifying exam |
| Gate II | Ch 31, new §08 | 3 h, 8 problems |
| Gate III | Ch 40, new §08, after "The list" | 3 h, 6 problems |
| Gate IV | Ch 51, new §08 | 3 h, 8 problems, UCLA real-analysis style |
| Gate V | Ch 59, new §08 | 3 h, 8 problems, UCLA complex-analysis style |
| Gate VI | Ch 72 §08 (exists) | 3 h, mixed across Parts IV–VI |

**Each Gate page carries:**
- **Instructions:** timed and closed-book, with the solutions folded.
- **A marking scheme per problem:** key steps with points, and the common fatal errors. This is what makes self-grading or AI grading reliable (A2, ProofBench, Devlin).
- **A pass line:** for example ≥ 70% overall, with no problem at 0 among the ones marked *core*.
- **A remediation map:** each problem lists, with `@ref`, the sections it tests, so a failed item sends the reader to named sections, not "reread Part II".
- **An entry-diagnostic role:** a reader arriving by a reading path takes the gate of the Part before their target. This replaces a separate placement test.

**Caveat on originality.** Gate problems must be original (the source policy), modelled on the *style* of qualifying exams, never copied from them.

### B3. Spaced and interleaved review

**The gap.** Every exercise in the book tests its own section, so readers practise in blocks. Rohrer et al. and Hopkins et al. both show that adding **mixed, delayed** practice improves retention and transfer, and that this is cheap to add [E→].

**Recommendation.** Add a fourth exercise group, **"R. Review"**, to the **last section of each chapter** only, with 3–4 items:

- **R1: one chapter back.** A problem whose method comes from the previous chapter.
- **R2: 3–4 chapters back.** About a month on the two-year route, or two months on the three-year route: 5–10% of a one-to-two-year horizon (Cepeda).
- **R3: a Part or more back.** A spiral item, taken from the spiral table in `curriculum.md`: "You proved X on ℝ in @thm-…; prove it in a metric space" or "state what now fails".
- **R4 (optional): a method-choice item.** The problem gives no hint of which tool to use. Once the reader has chosen, the solution names the tool and says why the look-alike tools fail. This is interleaving proper (Rohrer).

**Rules for R items [O].**
- R items **never state which chapter they come from** in the problem. The solution states it with `@ref`.
- Pick targets **from the citation graph, FIRe-style.** A result that later chapters cite hardly or never as a *hard* citation is "dormant", and it is the one that needs explicit review. A heavily cited result gets implicit review for free.
  - A small tool could list, for each label, the distance in chapters since its last hard citation. `tools/reading_path.py` already loads the graph.
  - Engine work is not in scope here; this report names the idea only.
- Keep R items short (≤ 20 min). The routes above budget about 15% of a week for them.
- **Definition drills.** Once per Part, a "state it in symbols" retrieval list: every major definition of the Part, answer folded. It costs one page and is the best-supported technique there is (Dunlosky).

### B4. Exercise formats to add

In priority order. The first four can be checked with no grader at all.

1. **Self-explanation training, once [E, d = 0.95].** Put a short section or boxed interlude in Ch 1 §01 or Ch 2 §06 ("Reading and writing proofs"). It is an original rewrite of the Loughborough booklet's *method*: explain each line by earlier lines and definitions; do not paraphrase. It contrasts a good and a weak self-explanation of the same proof. The existing "*Before reading on:*" prompts then work as reminders of a trained habit, which is how the trial used them.
2. **Proof comprehension questions [E, Mejía-Ramos].** For the 2–3 key proofs of each chapter, add an A-level item. Each part has a short, checkable answer. The item's parts:
   - (a) why does line k follow;
   - (b) where is hypothesis H used;
   - (c) give the proof's idea in two sentences;
   - (d) run the proof on this specific example;
   - (e) which step fails if H is dropped?
3. **Find the error, split in two [E; exists once per chapter, extend].** Keep Alcock & Weber's two columns, "true?" and "follows?". Also include flawed proofs of **true** statements; these are harder, and Weber (2010) shows that this is where readers fail. Aim for 2 per chapter in Parts 0–I, then 1 per chapter.
4. **Proof ordering: Proof Blocks, or Parsons problems for proofs [E, Poulsen].** Give 6–10 lines of a proof, shuffled, plus 1–2 distractors (a line with the wrong quantifier order, or an ε of the wrong kind).
   - Print: the reader numbers the lines, and the folded solution gives the order and says why each distractor fails.
   - Web: a `::: {.widget}` that checks any order consistent with the dependency graph is possible later. [O]
   - Use them heavily in Part 0 and Part I, and rarely later (expertise reversal).
5. **Faded proofs [E, Atkinson, Renkl & Merrill].** The same theorem-type appears three times in a chapter or Part:
   - worked in full;
   - with the last step blank;
   - with the last half blank.

   Each blank carries a prompt to "name the move". Good candidates are the ε/2 argument, "construct a point as a sup", the 3ε argument, the diagonal argument, and density plus a uniform bound.
6. **Try it first [E→, Weber 2015 (i); Sinha & Kapur].** Before 1–2 major theorems per chapter, add: "*Try for ten minutes: which object would you build?*". The Idea block that follows serves as the "instruction" of productive failure. Keep it to 1–2 per chapter, because an unanswered attempt costs a self-learner more than a student in class. [O]
7. **Example generation [E→, Sangwin; Tall & Vinner].** "Give an example of a set that is closed and bounded but not compact in (C[0,1], sup)." Where the answer space is narrow, the answer can be checked against a stated property list. The STYLE wording already allows these; make them a named B type.
8. **Proofs with a marking scheme [E→, ProofBench; Devlin's MOOC].** Every exit check, Gate problem and harder C item gets a `**Marking scheme.**` paragraph at the end of its solution: 3–6 key steps with points, plus the named fatal errors ("δ depends on x", "used compactness of an open set"). This serves three graders equally: the reader, a study partner, and an AI.
9. **Hint ladder [O, consistent with VanLehn's step feedback].** STYLE §6 allows one hint that names a tool. For C items, allow **two folded rungs**: the tool, then the first line of the proof. The solution comes after them. Among self-learners, the documented failure is opening the full solution too early (A4).
10. **Lean, optional, Part 0 only [O].** Link the Natural Number Game and the logic worlds of the Lean game server as optional practice beside Ch 1–4's rule / phrase / Lean table. It is the only source of *certain* feedback on a whole proof. It stays "shown, never required" (Ch 1 blueprint note).

**Not recommended [E].** Narrated or animated proof walkthroughs as a replacement for reading (Roy et al. 2017: worse retention). Interactive plots stay for exploration, per STYLE §5, not for proofs.

### B5. The reader's guide to feedback without a teacher

This belongs on a front-matter page, "How to use this book alone", written once. It is the one place where the book *advises* the reader rather than teaching. Contents:

1. **The loop.**
   - Attempt the problem.
   - Write the proof in full.
   - Self-explain it line by line.
   - Grade it against the marking scheme.
   - Only then read the solution and diff your proof against it.
   - Log the error type.
2. **Using an AI tutor.**
   - **[E] Bastani et al.:** unrestricted help lowers later independent performance. **[E] Kestin et al.:** a tutor designed to withhold answers and prompt reasoning helps.
   - Give the reader a copy-paste protocol:
     - "Do not give me the proof. Ask me what the next step needs."
     - "Here is my proof and the marking scheme; for each step, say whether it is justified and which earlier result it uses."
     - "Find the first line that does not follow."
   - **[E] Mahinpei et al.:** tell the reader plainly that an AI grader disagrees with human graders about a third of the time on proofs, is usually *too strict*, and penalises valid alternative proofs. So treat a flagged line as a question to investigate, not a verdict.
3. **Humans.** Math.SE for pinpointed questions, and a study partner for exchanging proofs to grade with the marking scheme. Devlin's MOOC shows rubric-based peer grading is workable if the grader has first practised on samples.
4. **Honesty about completion.** Each Part is a complete course with its own Gate. Stopping after Part I or Part IV is a legitimate outcome. Say so.

### B6. Reading paths: the `reading-paths` entries

**First, a correction to `decisions.md` [O, grounded in the engine's own rule].** The README says a reading path should have "two or three to half a dozen" targets, and that "a profile whose path is nearly the whole book is telling you it is aimed too broadly". The **`two-year` and `three-year` entries listed in `decisions.md` violate that by construction.** They are *schedules* (orderings with weeks), not closures, and the reading-path page (sections in reading order, what can be skipped, single-proof hinges) has nothing to say about them. Recommendation:
- keep them as **routes**, written as the tables in B1, on a front-matter page ("Routes and pace");
- take them out of the `reading-paths` list in `decisions.md`.

`foundations`, `measure-only` and `complex-only` stay as reading paths, and more are added below.

**About the targets.** Only Chapters 1 and 8 exist. All other targets are **provisional**: `<chapter dir>/<planned section number>`, taken from the "Planned sections" lists in `authoring/blueprints/chNN.md`. Each must be re-checked when its chapter is drafted, and every profile must be run through `python3 tools/reading_path.py --profile <slug> --verify` once the chapters exist. **The config should not receive these entries until then**, because a target that does not exist would break the build.

Each target is the section holding the *result the reader came for*, as the README instructs.

```json
"reading-paths": [
  {
    "slug": "foundations",
    "name": "Proof and sets: the foundations",
    "description": "Learning to write proofs from nothing: the rules behind every proof step, quantifiers and their negation, sets, functions and preimages, induction, and why the real numbers cannot be listed. For a reader preparing for any proof-based course.",
    "targets": [
      "ch02-quantifiers-and-proof/06",
      "ch03-sets-and-functions/06",
      "ch04-relations-and-induction/06",
      "ch05-countable-and-uncountable/04",
      "ch05-countable-and-uncountable/05"
    ]
  },
  {
    "slug": "first-course-real-analysis",
    "name": "A first course in real analysis",
    "description": "The standard first analysis course and nothing beyond it: continuous functions on closed intervals, the mean value theorem and Taylor's theorem, the Riemann integral and the fundamental theorem of calculus, uniform convergence, and the exponential and trigonometric functions built from power series.",
    "targets": [
      "ch13-continuity-on-intervals/03",
      "ch13-continuity-on-intervals/05",
      "ch14-derivative-and-mean-value/06",
      "ch15-riemann-darboux-integral/05",
      "ch16-sequences-of-functions/06",
      "ch17-power-series/07"
    ]
  },
  {
    "slug": "metric-spaces-and-odes",
    "name": "Metric spaces and differential equations",
    "description": "Why an ODE has a solution and when it is unique: contraction mappings and Picard–Lindelöf, compactness of function families and Peano's theorem, the inverse and implicit function theorems, and the Baire category theorem.",
    "targets": [
      "ch24-contraction-picard/05",
      "ch24-contraction-picard/06",
      "ch25-arzela-ascoli-peano/06",
      "ch26-stone-weierstrass-baire/05",
      "ch28-inverse-implicit/03"
    ]
  },
  {
    "slug": "fourier-classical",
    "name": "Classical Fourier analysis",
    "description": "Fourier series and integrals with the Riemann integral: Fejér's theorem, mean-square convergence and Parseval, Fourier inversion and Plancherel on the Schwartz space, the heat and wave equations, and Fourier analysis on finite groups.",
    "targets": [
      "ch33-good-kernels-summability/03",
      "ch34-mean-square-pointwise/03",
      "ch36-fourier-transform-line/03",
      "ch37-fourier-transform-rd/03",
      "ch38-finite-fourier-analysis/06"
    ]
  },
  {
    "slug": "measure-only",
    "name": "Measure and integration",
    "description": "The Lebesgue integral and what it buys: the dominated convergence theorem, Fubini–Tonelli, completeness of Lᵖ, the Lebesgue differentiation theorem, and Radon–Nikodym. For a reader who needs measure theory for analysis, probability or PDE.",
    "targets": [
      "ch43-lebesgue-integral/03",
      "ch45-fubini-tonelli/03",
      "ch47-lp-spaces/02",
      "ch49-lebesgue-differentiation/04",
      "ch51-signed-measures-radon-nikodym/05"
    ]
  },
  {
    "slug": "measure-for-probability",
    "name": "Measure theory for probability",
    "description": "Just what a probability course assumes: constructing a measure from its values on intervals and proving it unique, Lebesgue–Stieltjes measures as distribution functions, product measures, uniform integrability and Vitali's theorem, and densities by Radon–Nikodym.",
    "targets": [
      "ch44-abstract-measure/05",
      "ch44-abstract-measure/06",
      "ch45-fubini-tonelli/03",
      "ch48-modes-of-convergence/03",
      "ch51-signed-measures-radon-nikodym/05"
    ]
  },
  {
    "slug": "complex-first-course",
    "name": "A first course in complex analysis",
    "description": "Cauchy's theorem and integral formula, Liouville and the fundamental theorem of algebra, residues and real integrals, and counting zeros with the argument principle and Rouché's theorem.",
    "targets": [
      "ch53-cauchy-theorem/04",
      "ch54-singularities-residues/06",
      "ch55-global-cauchy-theory/05"
    ]
  },
  {
    "slug": "complex-only",
    "name": "Complex analysis to qualifying-exam level",
    "description": "Everything a graduate complex-analysis exam asks: the Riemann mapping theorem, harmonic functions and Harnack, Weierstrass products and Mittag-Leffler, analytic continuation, and Picard's little theorem.",
    "targets": [
      "ch56-conformal-riemann-mapping/06",
      "ch57-harmonic-functions/05",
      "ch58-entire-functions-products/04",
      "ch59-continuation-and-picard/02",
      "ch59-continuation-and-picard/06"
    ]
  },
  {
    "slug": "functional-analysis",
    "name": "Functional analysis",
    "description": "The four theorems of Banach-space theory — Hahn–Banach, uniform boundedness, open mapping and Banach–Alaoglu — then Hilbert spaces, Lax–Milgram, and the spectral theorem for compact self-adjoint operators.",
    "targets": [
      "ch62-hahn-banach/04",
      "ch63-baire-category-operators/04",
      "ch64-weak-topologies-alaoglu/06",
      "ch65-hilbert-spaces/06",
      "ch66-compact-operators-spectral/07"
    ]
  },
  {
    "slug": "toward-pde",
    "name": "Toward PDE: the Dirichlet problem",
    "description": "Solving −Δu = f in a bounded domain the modern way: distributions, Sobolev spaces, Plancherel, Rellich compactness, weak solutions by Lax–Milgram, and the eigenbasis of the Dirichlet Laplacian.",
    "targets": [
      "ch69-tempered-distributions-fourier/03",
      "ch71-poincare-rellich/05",
      "ch72-dirichlet-capstone/03",
      "ch72-dirichlet-capstone/06"
    ]
  }
]
```

**Notes on the entries.**
- **`toward-pde`** will probably close over most of the main line. That is honest (the capstone *is* the whole book), but by the README's test it is borderline. Keep it only if its page still lists a meaningful set of skippable sections (for example Part V, Ch 38, and much of Ch 30–31 and 58–59). Otherwise drop it and let the two-year route stand for it.
- **`foundations`** is almost all of Part 0's main line. That is acceptable because the target *reader* is narrow: someone who wants a transition-to-proof course.
- **`measure-only` versus `measure-for-probability`.** Their closures will differ mainly by Ch 49–50 (maximal function, BV) and Ch 47 §5–§7. If the difference turns out small, merge them.
- **`complex-first-course` versus `complex-only`.** The split is deliberate. A one-semester undergraduate complex-analysis reader should not be sent through normal families and Picard.
- **Pair each path with a Gate.** Each path page should say which Gate to take as an entry diagnostic: `measure-only` takes Gate I and the metric half of Gate II; `complex-only` takes Gate I; `functional-analysis` takes Gate IV. This can be a sentence in the `description` until the engine grows a field for it. [O]

### B7. What STYLE.md should add

Proposed text for a new **§11, "The reader working alone"**, plus small edits to §5 and §6. [E] or [O] as marked.

1. **Self-explanation training (Chapter 1 or 2, once) [E].** "Chapter 2 §06 (or Chapter 1 §01) contains the book's one training passage on self-explanation. It shows one proof explained well (each line by earlier lines, definitions and named results) and badly (paraphrase). Later '*Before reading on*' prompts assume this training and may say '*Self-explain lines 3–5*'."
2. **Comprehension items (§6, A group) [E].** "For the two or three key proofs of a chapter, the A exercise of their section includes at least one proof-comprehension part: why line k follows, where hypothesis H is used, the idea in two sentences, the proof run on a given example, or which line fails without H. Every part has a short answer the reader can check."
3. **Find the error: extend the §10 rule [E].** "At least one flawed argument per chapter has a **true** conclusion. The solution names the line, the rule broken or hypothesis missing, and a counterexample to the illegal step, not just to the conclusion."
4. **Proof ordering and faded proofs (Parts 0–I heavily, later sparingly) [E].** "In Parts 0 and I each chapter has one proof-ordering item: shuffled lines plus one or two distractors, with a solution that gives an admissible order and says why each distractor fails. It also has one faded-proof triple for its main named move: full, last step blank, last half blank. From Part II on, use them only where a new named move appears." The expertise-reversal effect is the reason for tapering.
5. **R. Review group (§6) [E→].** "The last section of each chapter has a fourth group, `### R. Review`, with 3–4 items labelled `-r1`…:
   - one item from the previous chapter;
   - one from 3–4 chapters back;
   - one spiral item from an earlier Part;
   - optionally one item that gives no hint of its method.

   The problem text never names its source chapter; the solution does, with `@ref`. Prefer results that later chapters rarely cite in proofs."
6. **Marking schemes (§6) [E→].** "Exit checks, Gate problems and any C item a reader is likely to write up in full end their solution with `**Marking scheme.**`: 3–6 key steps with points out of 10, and the named fatal errors. Write it so that another person or a program could grade a *different* correct proof fairly: award the step, not the wording." ProofBench's marking schemes and Mahinpei et al.'s "penalises deviations" finding motivate that last sentence.
7. **Hint ladder (§6) [O].** "A C item may have two folded hints: the first names a tool or object, the second gives the first line of the proof. Neither gives the key idea's execution."
8. **Try it first (§4) [E→].** "At most two theorems per chapter are preceded by '*Try it first: …*' naming what to attempt and for how long (five to ten minutes). The Idea block that follows must start from the obstacles such an attempt meets."
9. **Time estimate on the chapter index (§2) [O].** "The chapter `index.md` gives, after **What you need**, a line '**Time.** About N hours on the core track (A, one B and one C per section, exit checks); about M for everything.' N and M come from reader logs once there are any; until then from the formula in `authoring/design/research-reader.md`, B1."
10. **Gates (§2) [O].** "The last main-line chapter of each Part ends with a Gate section: timed, closed-book, with folded solutions, a marking scheme per problem, a pass line, and a remediation map of `@ref`s to the sections each problem tests."
11. **Keep narration out of proofs (§5) [E].** "Interactive elements illustrate objects (sequences of functions, kernels, iterates), never a proof's steps. A proof is read, not watched."
12. **Taper the scaffolding (a new line in §1) [E].** "Scaffolding decreases through the book: Part 0 annotates rules and orders lines for the reader; Part VI expects the reader to supply routine ε-management. Do not carry Part 0's density of prompts into Part IV."

### B8. Follow-up work (outside this report)

- **Decisions.**
  - Stage S3 should be sequential (IV, then V) on the two-year route.
  - `two-year` and `three-year` should become routes, not reading paths.
  - A Gate section should be added in Ch 5, 31, 40, 51 and 59; Ch 18 §06 and Ch 72 §08 already exist.
  - An R group should be added.
- **Blueprints.** Add the Gate sections to `blueprint/book.yaml` and the chapter blueprints, and add a proof-ordering item, a faded-proof triple and comprehension items to the Part 0 and Part I blueprints.
- **Pilot chapters.** Retrofit Ch 1 and Ch 8 as the test:
  - add the training passage to Ch 1 §01 or leave it for Ch 2;
  - add one comprehension item per chapter, one ordering item, an R group in Ch 8 §07 (reaching back to Ch 1–5), and marking schemes on the exit checks.

  Have a test reader log hours per section before any of this is scaled to the remaining 70 chapters.
- **Engine (optional, later).**
  - A widget that checks a proof-ordering item against its dependency graph.
  - A "routes" page type.
  - A review-scheduler report built on `crossref_labels.json`, listing dormant results by chapter.
