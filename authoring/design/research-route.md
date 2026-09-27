# Is this the best route through analysis? (research record)

Research done on 2026-09-28 against `blueprint/book.yaml` (72 chapters, about 3,745 planned pages), `decisions.md` and `curriculum.md`. The planning research of 2026-09-27 already covered Cambridge, Oxford, Princeton (Stein–Shakarchi, MAT 215), MIT 18.102, ETH, the UCLA and Berkeley quals, and NTU. This file adds Chicago, Stanford, Harvard (55, 112, 113/114), Bonn, ENS Paris (L3/M1), Moscow State (mechmath), Berkeley 202AB, MIT 18.101, Northwestern's prelim syllabus, Tao's UCLA 245ABC, and the orderings of Stein–Shakarchi, Folland, Pugh, Tao (*Analysis II*), Amann–Escher and Zorich. It then works through the sequencing questions one at a time and ends with concrete recommendations.

**How to read the evidence labels.** *Strong* means that most comparable programmes and standard texts agree, or that a later chapter of this book logically depends on the point. *Moderate* means there is a clear majority or a strong downstream need, but respectable counterexamples exist. *Opinion* means the recommendation is a judgement call that the sources leave open. No empirical education research compares one analysis *ordering* with another; the Tall–Vinner, Weber and Selden studies cited in `curriculum.md` concern how concepts and proofs are learned, not the order of topics. The route question is therefore settled by curricular consensus plus the dependency structure of the mathematics itself.

Not verified: I found no public syllabus for the Chicago REU or the Independent University of Moscow. Moscow State's mechmath track (FMMP) stands in for the Russian tradition, with Zorich as its textbook.

---

## 1. The current route in numbers

| Part | Chapters | Pages | Share | Optional chapters |
|---|---|---|---|---|
| 0 Logic, sets, constructions | 1–7 | 368 | 9.8% | 6–7 on the two-year path |
| I Real line | 8–20 | 759 | 20.3% | 19, 20 |
| II Metric spaces, several variables, topology | 21–31 | 559 | 14.9% | — |
| III Fourier (Riemann) | 32–40 | 439 | 11.7% | 39 |
| IV Measure | 41–51 | 542 | 14.5% | — |
| V Complex | 52–59 | 414 | 11.1% | — |
| VI Functional analysis, distributions, Sobolev | 60–72 | 664 | 17.7% | 67 |

The route in one line: ℝ fully → metric/ℝⁿ (with ODE and topological spaces) → Riemann-setting Fourier as the engine that motivates Lebesgue → measure on ℝᵈ, then abstract measure → complex analysis (parallel to IV) → functional analysis → distributions → Sobolev → the Dirichlet capstone.

---

## 2. Findings by programme and text

### Chicago
- **MATH 20300–20400–20500 (Analysis in ℝⁿ I–III)** is the standard majors' sequence. 20500 covers integration in ℝⁿ, Fubini, line and surface integrals, **differential forms and the theorems of Green, Gauss and Stokes**, and the catalogue calls the sequence "the basis for all advanced courses in analysis and topology". [catalog](http://collegecatalog.uchicago.edu/search/?P=MATH+20300-20400-20500), [Coursicle 20500](https://www.coursicle.com/uchicago/courses/MATH/20500/)
- **MATH 20700–20800–20900 (Honors Analysis)** is "at a level equivalent to a graduate course at many universities". It covers metric spaces, normed linear spaces, the Lebesgue integral and its convergence theorems, differential calculus in Euclidean space, complex functions, **Fourier series and integrals, and calculus on manifolds**, all in one year. [application sheet (PDF)](https://d3qi0qp55mx5f5.cloudfront.net/mathematics/i/basic_pages/20700app.pdf?mtime=1588972130)
- *Lesson:* even the most compressed elite route keeps **manifolds/Stokes** in the core. Fourier comes *with or after* Lebesgue, not before it.

### Stanford
- **Math 171** is honours analysis with an early metric-space emphasis: the Riemann integral, convergence in metric spaces, compact metric spaces and basic point-set topology. **Math 172** covers Lebesgue measure on ℝᵈ, the Lebesgue integral, Lᵖ, **the Fourier transform, the Hardy–Littlewood maximal function and Lebesgue differentiation**. **205A** is graduate measure theory (modes of convergence, Lᵖ, Radon–Nikodym, products, differentiation). [Math 171 overview (SUMO)](https://sumo.stanford.edu/pdfs/Pset0/Math171.pdf), [172 bulletin](https://bulletin.stanford.edu/courses/2089891), [205A syllabus](https://web.stanford.edu/~montanar/TEACHING/Math205A/syllabus.html)
- *Lesson:* the undergraduate measure course already contains **maximal function + Fourier transform**, the harmonic-analysis entry kit. Measure is done on ℝᵈ first.

### Harvard
- **Math 55a/55b.** 55a is abstract and linear algebra, with the real and complex number systems and basic point-set topology. 55b covers metric topology, "combined with tools from linear algebra studied in 55a", differential and integral calculus, and an introduction to complex analysis. [Elkies 55a handout (PDF)](https://people.math.harvard.edu/~elkies/M55a.10/h1.pdf), [55b notes](https://people.math.harvard.edu/~elkies/M55b.16/index.html)
- **Math 112** covers set theory and the reals, metric spaces, compactness, the Riemann integral, the implicit function theorems and the first Lebesgue theory. [112 syllabus](https://people.math.harvard.edu/~ctm/home/text/class/harvard/112/02/html/syl.html)
- **Math 114** (Lurie's version) runs: Lebesgue measure on Euclidean space → the integral, DCT, Fubini → **L² and Hilbert spaces → Banach spaces, Lᵖ duality → Fourier series and Plancherel → open mapping, closed graph, uniform boundedness**. The syllabus says: "Complex analysis is not a prerequisite; this course and Math 113 may be taken independently." The catalogue version also lists **general topology** inside 114. [Lurie 114 syllabus (PDF)](https://people.math.harvard.edu/~lurie/114notes/syllabus.pdf), [Harvard course page](https://www.math.harvard.edu/course/mathematics-114/)
- *Lessons:* (i) complex analysis and measure are **independent**; (ii) **Hilbert before Banach**; (iii) general topology is taught **inside** the measure/functional-analysis course, not before it; (iv) linear algebra precedes several-variable analysis.

### UCLA: Tao 245ABC
- **245A:** abstract σ-algebras *and* Lebesgue measure on ℝᵈ (Tao's own text builds Lebesgue measure on ℝᵈ concretely first), the convergence theorems, Fubini–Tonelli, Lebesgue differentiation, absolute continuity; Radon–Nikodym is "likely deferred" to 245B. [announcement](https://terrytao.wordpress.com/2010/08/31/course-announcement-245a-real-analysis/), [245A page](https://www.math.ucla.edu/~tao/245a.1.10f/)
- **245B:** point-set topology and functional analysis (Lᵖ, Hilbert, Hahn–Banach, Baire, Riesz representation). [245B](https://www.math.ucla.edu/~tao/245b.1.09w/)
- **245C:** **interpolation (Riesz–Thorin, Marcinkiewicz), Fourier analysis, distributions, Sobolev spaces, Hausdorff dimension**. [245C](https://www.math.ucla.edu/~tao/245c.1.11s)
- *Lessons:* point-set topology sits **next to functional analysis**, after measure. The endpoint (distributions + Sobolev) matches our Part VI, **plus interpolation and Hausdorff dimension**, which we do not have.

### Berkeley 202AB (the graduate "tool courses")
- **202A:** metric and general topological spaces, **Tychonoff, Urysohn, Tietze, locally compact spaces**, then general measure and integration and the beginnings of Banach spaces. **202B:** product measures, Radon–Nikodym, differentiation, **Hausdorff measures**, the Fourier transform, topological vector spaces, Banach and Hilbert spaces, the Banach theorems, Lᵖ duality. [Rieffel 202A](https://math.berkeley.edu/~rieffel/202AannF24.html), [grad courses page](https://math.berkeley.edu/research/research-areas/mathematical-analysis/mathematical-analysis-graduate-courses)
- *Lesson:* general topology is taught **in one block, immediately before measure/functional analysis**, including the LCH material. It is not split three ways.

### Bonn (BSc; German Analysis I–III tradition)
- **Analysis I:** one variable, Riemann integral, power series, elementary functions over ℂ.
- **Analysis II:** several variables, the implicit function theorem, normed spaces, Banach's fixed point theorem, **ODE: Picard–Lindelöf and linear first- and second-order equations**.
- **Analysis III:** the Lebesgue integral on ℝⁿ, monotone and dominated convergence, Fubini, **the transformation formula, surfaces and surface integrals, Gauss's and Stokes's theorems**.
- Separate modules follow. Complex analysis runs to Weierstrass, Mittag-Leffler, Runge, Hadamard and Riemann mapping. "PDEs and Functional Analysis" covers **Lax–Milgram, Sobolev spaces with embedding and trace theorems, weak compactness, the spectral theorem for operators with compact inverse, and L²-regularity**. Probability is a separate module (LLN, CLT).
- [Standard course content (PDF)](https://www.mathematics.uni-bonn.de/studium/medienordner-studium-1/dateien/dokumente/bscmath-vorlesungsinhalte-en.pdf/@@download/file/BScMath_Standard-course-content.pdf)
- *Lessons:* the **divergence theorem belongs with Lebesgue and the change of variables** (Analysis III). ODE sits with several-variable calculus and includes linear systems. Bonn's FA/PDE module is almost exactly our Part VI + capstone, **with L²-regularity proved**.

### ENS Paris (L3 → M1)
- **Semester 1:** *Topologie et calcul différentiel* covers metric and topological spaces, completeness, compactness, connectedness, Ascoli, Stone–Weierstrass; Banach–Steinhaus, open mapping, closed graph, Hahn–Banach, Hilbert projection; differential calculus, local inversion, implicit functions; **ODE: existence and uniqueness, regularity of the flow, Gronwall**. *Intégration et probabilités* begins with dice sequences to motivate the existence of measures, builds product and Lebesgue measure, and ends with the **strong law of large numbers and the CLT** (reference: Billingsley).
- **Semester 2:** *Analyse complexe* (Cauchy theory, Runge, Weierstrass, Riemann mapping, Picard, residues, the saddle-point method, elliptic/modular functions, Dirichlet series). *Analyse fonctionnelle* (M1) covers locally convex spaces, weak topologies, Hahn–Banach, Banach–Alaoglu, reflexivity and uniform convexity, **the topology of spaces of measures with applications to probability**, then distributions and the Fourier transform, then **Sobolev spaces with embeddings and elliptic PDE**.
- [ENS brochure 2023–24 (PDF)](https://www.math.ens.psl.eu/wp-content/uploads/2023/08/Brochure-2023-2024.pdf), [Topologie et calcul différentiel](https://www.math.ens.psl.eu/formations/topologie-et-calcul-differentiel/)
- *Lessons:* (i) **measure is taught together with probability**, with SLLN and CLT as the payoff; (ii) complex analysis comes **after** measure but does not use it; (iii) the functional-analysis endpoint is the same as ours (distributions → Sobolev → elliptic PDE); (iv) ODE includes **flows and Gronwall**.

### Moscow State (mechmath, FMMP track; Zorich's tradition)
- **Semester 2** covers series, improper integrals, Γ and B, uniform convergence, power series, **metric and normed spaces**, several-variable differentiation, inverse and implicit functions, extrema and Lagrange. **Semester 4** covers σ-algebras, Lebesgue measure on ℝ and ℝⁿ, the Lebesgue integral and limit theorems, product measures and Fubini, **BV and AC functions, Fourier series and transform, Banach and Hilbert spaces**. Complex analysis (ТФКП) and functional analysis are separate courses. [Analysis-2](https://fmmp.math.msu.ru/courses/matematicheskij-analiz-(vtoroj-semestr)), [Analysis-4](https://fmmp.math.msu.ru/courses/matematicheskij-analiz-(chetvertyij-semestr))
- **Zorich, *Mathematical Analysis II*:** continuous maps (general theory) → differential calculus from a general viewpoint → multiple integrals → **surfaces and differential forms → line and surface integrals → vector analysis → forms on manifolds** → uniform convergence → parameter integrals → Fourier series and transform → asymptotic expansions (distributions appear in appendices). [TOC](https://catalog.lib.uchicago.edu/vufind/Record/11252931/TOC), [Springer](https://link.springer.com/book/10.1007/978-3-662-48993-2)
- *Lesson:* the Russian route puts **forms/Stokes in the second-year core**, and teaches Fourier in the Riemann setting before or alongside measure, as we do.

### MIT (beyond 18.102)
- **18.101 Analysis and Manifolds** (prerequisites 18.100 and linear algebra) covers submanifolds of ℝⁿ, forms, orientation, integration on manifolds and **Stokes**, from Munkres and Spivak. It is followed by 18.952 on differential forms. [18.101](https://math.mit.edu/classes/18.101/fa18/)

### Oxford (detail beyond `curriculum.md`)
- The second-year core is **Metric Spaces and Complex Analysis**; **Integration** (Lebesgue) is an option. The third-year **B8.1 Probability, Measure and Martingales** takes abstract measure, product measure, conditional expectation and martingales. **B4.1 Functional Analysis I** lists Part A Integration as essential and expects both metric spaces and complex analysis. [B8.1](https://courses.maths.ox.ac.uk/course/view.php?id=4980), [B4.1](https://courses.maths.ox.ac.uk/course/view.php?id=6073), [Part A synopses (PDF)](https://www.maths.ox.ac.uk/system/files/attachments/Part%20A%20Mathematics%20Synopses%202024-25.pdf)

### Cambridge (detail beyond `curriculum.md`)
- **Part II Probability and Measure** proves the strong law, and covers the Fourier transform of finite measures, characteristic functions, weak convergence, Lévy's continuity theorem and the CLT, as well as measure-preserving maps and ergodic theorems. So the Cambridge *measure* course *is* a probability course. [Breuillard notes (PDF)](https://www.dpmms.cam.ac.uk/study/II/Probability+Measure/2019-2020/lecture-notes-1-16.pdf), [Norris notes (PDF)](https://www.statslab.cam.ac.uk/~jrn10//Lectures/pm.pdf)

### Northwestern prelim (a second qual benchmark besides UCLA/Berkeley)
- The syllabus covers measure (to AC functions and FTC), functional analysis (Hilbert, Banach, Hahn–Banach, spectral theory, Radon measures, Fourier) and complex analysis (to harmonic and subharmonic functions and Riemann mapping). It does **not** include forms/Stokes, ODE, probability, Hausdorff measure, interpolation or Sobolev. [syllabus](https://www.math.northwestern.edu/graduate/prelims/analysis-syllabus.html)
- *Lesson:* our Parts IV–V already **exceed** the qual floor. Every addition recommended below is justified by what comes *after* the qual (branches), not by the qual itself.

### Texts: ordering
| Text | Order |
|---|---|
| Stein–Shakarchi I–IV | Fourier (Riemann) → Complex → Real (measure on ℝᵈ, Hilbert, **Hausdorff measure** in III ch. 7) → Functional (Lᵖ, **interpolation, Hilbert transform**, distributions, Baire, **probability and Brownian motion**, several complex variables, oscillatory integrals). The foreword says Fourier comes first because of "its central role within the historical development and contemporary practice of analysis". [Wikipedia](https://en.wikipedia.org/wiki/Princeton_Lectures_in_Analysis) |
| Folland, *Real Analysis* | Measures → Integration → Signed measures & differentiation → **Point-set topology (ch. 4, after measure)** → Elements of FA → Lᵖ → Radon measures → Fourier → Distributions → **Probability** → More measures (Hausdorff, surface measure). [TOC](https://catdir.loc.gov/catdir/toc/onix03/98037260.html) |
| Pugh | Reals (with cuts) → **metric topology early (ch. 2)** → one-variable functions → function spaces (Arzelà–Ascoli, Baire, contraction/ODE, Stone–Weierstrass) → multivariable calculus **including forms and Stokes** → Lebesgue. [Springer](https://link.springer.com/book/10.1007/978-0-387-21684-3) |
| Tao, *Analysis II* | Metric spaces → continuity → uniform convergence → power series → **Fourier series (Riemann)** → several-variable differential calculus → Lebesgue measure → Lebesgue integration (**no multivariable Riemann integral**). [Springer](https://link.springer.com/book/10.1007/978-981-19-7284-3) |
| Amann–Escher III | Measure and Lebesgue (Bochner) integral → the transformation theorem → **manifolds, forms, Stokes** (Gauss–Green after Lebesgue). [Springer](https://link.springer.com/book/10.1007/978-3-7643-7480-8) |
| Zorich II | See Moscow above: forms/Stokes before Fourier; measure deferred. |
| Bressoud, *A Radical Approach to Lebesgue's Theory* | Historical: the failures of the Riemann integral with Fourier series → Lebesgue. The same motivational engine as our Part III → Part IV. [CUP](https://www.cambridge.org/9780521884747) |
| Bartle, "Return to the Riemann integral" (AMM 1996) | Argues for the Henstock–Kurzweil integral in place of Lebesgue at undergraduate level. A minority position that nobody surveyed adopted. [MAA](https://maa.org/programs/maa-awards/writing-awards/return-to-the-riemann-integral) |

---

## 3. Comparison table

✓ = in the core route, (✓) = optional/elective, — = absent, "after/before" refer to measure theory (M).

| Programme / text | ℝ fully before metric? | Fourier vs M | Complex vs M | General topology placement | Forms / divergence thm | ODE scope | Probability with M | Endpoint |
|---|---|---|---|---|---|---|---|---|
| **This book** | yes | Fourier **before** (Riemann) | parallel/after, independent | **3 places**: end II, start IV, VI | **deferred**; Green on rectangle/disc only | Picard, Peano, Gronwall | — (branch) | Sobolev + Dirichlet capstone |
| Cambridge | yes (Analysis I → IB) | Fourier in Methods; theory after M | complex **before** (IB) | IB Analysis & Topology (metric-led) | Methods (vector calculus) only | Methods | **✓ (P&M)** | Part II FA / Analysis of Functions |
| Oxford | yes | after | complex **before/with** | Part A/B topology separate | — (core) | Prelims/Part A | **✓ (B8.1)** | B4 FA |
| Princeton (S–S) | MAT 215 | **before** | **before** | minimal, as needed | Green only | — | (✓) in vol. IV | distributions, probability |
| Chicago honors | fast, ℝⁿ | with/after | same year | inside the sequence | **✓ manifolds** | — | — | FA basics |
| Chicago 203–205 | yes | — | — | — | **✓ Green/Gauss/Stokes** | — | — | — |
| Stanford | 171 metric-heavy | **after** (172) | independent (116) | 171 basic | — | — | — | maximal fn, Fourier transform |
| Harvard 55 / 112–114 | 55: metric early | **after** (114) | **independent** (113 ∥ 114) | **inside 114** | (✓) varies by instructor (not verified) | — | — | Banach, Fourier, Plancherel |
| Tao 245ABC | assumed | **after** (245C) | separate (246) | **245B, with FA** | — | — | — | interpolation, distributions, Sobolev, Hausdorff |
| Berkeley 202AB | assumed | after | separate (185/205) | **one block, before M** | — | — | — | FA, Hausdorff, Fourier |
| Bonn | yes | — (PDE module) | **after** | separate geometry/topology module | **✓ in Analysis III, after Lebesgue** | **✓ Picard + linear** | separate module | **Lax–Milgram, Sobolev, L²-regularity** |
| ENS | assumed (prépa) | after | **after**, independent | **with metric/diff. calc.** | M1 geometry | **✓ flows, Gronwall** | **✓ SLLN, CLT** | **distributions, Sobolev, elliptic PDE** |
| Moscow (MSU/Zorich) | yes | **with/before** | separate | with metric spaces | **✓ core (Zorich II)** | separate course | — | Banach/Hilbert basics |
| MIT | 18.100 | 18.103 after M | separate | 18.901 | **✓ 18.101** | separate | — | 18.102 (Dirichlet-type) |
| Folland | — | after | — | **ch. 4, after M, before FA** | (✓) ch. 11 surface measure | — | **✓ ch. 10** | distributions |
| Pugh | **no** (metric ch. 2) | — | — | ch. 2 | **✓ ch. 5** | contraction/Picard | — | Lebesgue |

---

## 4. The sequencing questions, one by one

### 4.1 The real line fully, then metric spaces? — **Keep.** (strong)
Cambridge, Oxford, Bonn, Moscow, Abbott and Tao (*Analysis I* → *II*) all do ℝ first. Rudin, Pugh, Harvard 55 and Stanford 171 bring metric topology in early, but those courses are for students who have already written proofs. Our reader has never written one (decisions: "The reader"), so the majority route fits. The spiral design (decisions 6) needs ℝ as the first turn anyway.

### 4.2 Fourier before Lebesgue? — **Keep, but cap it.** (moderate)
For: Stein–Shakarchi, Zorich/Moscow, Tao *Analysis II* (Riemann Fourier series before Lebesgue), and Bressoud's historical argument. It is also this book's own design rule (decisions 7): *every abstraction is forced by a concrete problem*, and Part III → ch. 40 "What the Riemann Integral Lacks" is exactly that engine. Against: Harvard 114, Stanford 172, Tao 245C, Folland, Berkeley and Oxford all do Fourier after Lebesgue, and they avoid doing the Fourier transform twice (Part III ch. 36–37 and Part VI ch. 69). Verdict: the motivational payoff is worth it. But Part III is 11.7% of the book, **more than complex analysis**. Its ℝᵈ material (Kirchhoff, descent, Radon) and its number-theory material do not feed Part IV, so they should be optional (see R7).

### 4.3 Complex before or after measure? — **Keep independent; say so in the reading paths.** (strong)
The evidence is unanimous that the two are **logically independent**: Harvard says so explicitly, Cambridge and Princeton put complex first, ENS and Bonn put it after, and Oxford teaches it alongside metric spaces. Our Part V needs only Parts I–III (see `book.yaml` coverage notes: Green, Arzelà–Ascoli, Poisson/Abel from Part III). What depends on order is **optional enrichment**: after measure, the Poisson integral of Lᵖ functions and of measures, the Herglotz representation and Fatou's theorem on boundary values (Rudin *RCA* ch. 11). This is the real bridge from complex analysis to harmonic analysis (see C3).

### 4.4 Point-set topology placement — **Consolidate; don't split three ways.** (moderate)
No programme or text surveyed splits general topology across three places. Berkeley 202A teaches one block (including Urysohn, Tietze and LCH) right before measure and functional analysis. Tao 245B, Harvard 114 and Folland ch. 4 put it **after measure, next to functional analysis**. ENS puts it with metric spaces and differential calculus. Cambridge and Oxford keep it metric-led early and treat general topology as a separate course. Our Part II ch. 30–31 (110 pp.) teach abstract topology at the end of S2, where nothing uses it:
- Part III works on 𝕋 as periodic functions.
- Part V's homotopy is done in ch. 55 itself (its note says so).
- Part IV's two uses (Lusin, density of C_c) work in ℝᵈ, where ch. 41's own outline notes that "Urysohn is free" via the distance function.

The genuine consumers are Riesz–Markov (ch. 61) and weak/weak* topologies with Tychonoff (ch. 64), both in Part VI. See R2.

### 4.5 Where differential forms and Stokes belong — **Add the divergence theorem to the main line; forms stay optional.** (strong for the divergence theorem, moderate for forms)
Stokes/forms are in the core at Chicago (both sequences), MIT 18.101, Bonn Analysis III, Zorich, Pugh and Amann–Escher. Cambridge, Oxford, Stein–Shakarchi, Stanford and the quals omit them. That part of the question is genuinely split, which is why decision 12 deferred them. But the *divergence theorem on C¹ domains* is not optional for the capstone's audience:
- Evans's *PDE* lists Gauss–Green, polar coordinates and coarea as assumed calculus (Appendix C) ([TOC](https://proofwiki.org/wiki/Book:Lawrence_C._Evans/Partial_Differential_Equations)).
- Our ch. 71 wants traces on C¹ domains.
- Ch. 72 wants Green's identities and "back to classical solutions".
- The capstone's dependency note already asks for a "divergence theorem for smooth compactly supported fields".
- Harmonic functions in ℝⁿ (mean value property, fundamental solution) need it.

Bonn and Amann–Escher place the divergence theorem **after Lebesgue and the change of variables**, which is exactly where our ch. 46 sits. See R1.

### 4.6 ODE placement and scope — **Keep in Part II, add linear systems and flows.** (moderate)
Our ch. 24–25 already cover Picard, Gronwall, continuous dependence, maximal solutions and Peano. Missing, compared with Bonn Analysis II and ENS: **linear systems and the matrix exponential, variation of constants, and C¹ dependence on initial data (the flow)**. The flow is used by characteristics and transport (PDE), by geometric flows, and by the Sturm–Liouville picture behind ch. 66's vibrating string. See R4.

### 4.7 How much linear and abstract algebra, and when — **Keep "just in time"; publish gates.** (moderate)
Harvard 55a (linear algebra before 55b analysis), Bonn (LA I–II in parallel with Analysis I–II) and MIT 18.101 (linear algebra is a prerequisite) all agree that LA I must precede several-variable calculus and LA II (inner products, spectral theorem) must precede Hilbert-space material. Abstract algebra appears nowhere in the analysis core except groups for Fourier and ideals for Gelfand, which matches decision 13. See R8.

### 4.8 Hilbert before Banach? — **Consider.** (moderate/opinion)
Stein–Shakarchi (III ch. 4 before IV), Lurie's 114 and Rudin *RCA* (ch. 4 before 5) put Hilbert first. Brezis and Folland put Banach first. Our Part III (ℓ², Bessel, Parseval) and Part IV (the L² toolkit for Radon–Nikodym) already preview Hilbert space, so either order works. See C5.

---

## 5. What "modern analysis" readers need next

| Branch | What the entry courses assume (evidence) | Have it? | Gap |
|---|---|---|---|
| **Harmonic analysis** | maximal function, Lebesgue differentiation, weak Lᵖ, Plancherel; **Riesz–Thorin and Marcinkiewicz** (Tao 245C; S–S IV ch. 2; Folland §6.4–6.5); Hilbert transform on L² | mostly | **interpolation**; Hilbert transform preview; Poisson integrals of measures |
| **PDE** | Sobolev, Lax–Milgram, Rellich, distributions, **Gauss–Green on domains**, polar coordinates (Evans App. C); interior **L²/H² regularity** (Bonn V3B1, Evans §6.3) | mostly | **divergence theorem**; regularity only "outline"; linear ODE / flows for characteristics |
| **Probability** | abstract measure, product measure / independence, Borel–Cantelli, LLN, **characteristic functions, weak convergence of measures, CLT** (Cambridge P&M, ENS, Oxford B8.1, Folland ch. 10, S–S IV ch. 5–6) | foundations only | **no probability at all on the main line** |
| **Geometric analysis / GMT** | divergence theorem, forms, **Hausdorff measure**, area/coarea (Folland ch. 11, S–S III ch. 7, Berkeley 202B, Tao 245C) | no | divergence theorem; Hausdorff measure |
| **Spectral theory / math. physics** | compact self-adjoint spectral theorem, Fredholm; bounded self-adjoint functional calculus | compact only | bounded case (Gelfand is optional) |
| **Calculus of variations** | weak lower semicontinuity, reflexivity, Sobolev, Rellich (the direct method) | yes (ch. 64, 70–72) | — (name it as a branch) |
| **Ergodic theory** | measure-preserving maps, the L² projection (von Neumann), maximal inequality (Birkhoff) | yes | — |

**The capstone is right.** The Dirichlet problem via Lax–Milgram, Rellich and the eigenbasis is the endpoint of Bonn's FA/PDE module, ENS M1 *Analyse fonctionnelle*, MIT 18.102 and Cambridge Part II. It uses every Part: the whole spiral (compactness, completeness, duality) converges on it. Its one weakness is the last step, "back to classical solutions (outline)". The programmes that end here prove L²/H² interior regularity, because without it the weak solution never becomes a function you can evaluate (see C2).

---

## 6. Recommendations

Chapter numbers refer to the current `book.yaml`. Page figures are rough targets.

### Change now

**R1. Add a main-line chapter "Surfaces, surface measure and the divergence theorem" to Part IV, directly after ch. 46 `change-of-variables`.** (evidence: **strong** for the divergence theorem, **moderate** for its placement)
- Content:
  - C¹ hypersurfaces as local graphs, via ch. 28's implicit function theorem;
  - surface measure (unifying ch. 46's σ on S^{d−1});
  - C¹ domains and the outward normal;
  - Gauss–Green via a smooth partition of unity, Fubini and the FTC;
  - integration by parts and Green's identities on domains;
  - harmonic functions in ℝⁿ: the mean value property by the divergence theorem, and the fundamental solution as a preview for ch. 68/72.
- Moves Green's theorem (rectangle and disc) out of ch. 29 into this chapter as its first example. Part V's uses are motivation only, and ch. 57's Green's identities can cite the new chapter, or keep the disc case inline if Part V is read before IV.
- Supplies what ch. 71 (traces) and ch. 72 (Green's identities, regularity) currently lack.
- ~45 pp. Amend decision 12 to read "the divergence theorem is on the main line; general Stokes and forms are an optional chapter".
- Sources: Bonn Analysis III, Amann–Escher III, Chicago 20500, Evans App. C.

**R2. Consolidate point-set topology: move ch. 30 `topological-spaces`, ch. 31 `compactness-quotients` and ch. 41 `urysohn-tietze` into a two-chapter topology block at the start of Part VI, immediately before ch. 61 `riesz-markov`.** (evidence: **moderate**)
- In Part IV, Lusin and the density of C_c(ℝᵈ) in Lᵖ use the metric Urysohn function d(x,A)/(d(x,A)+d(x,B)) and a metric Tietze. Add these as one section to ch. 23 or to ch. 42.
- Merge ch. 30 + 31 + 41 into:
  1. "Topological spaces, products and compactness";
  2. "Separation, Urysohn–Tietze and locally compact spaces".
- The quotient-gluing material (Möbius, Klein bottle, projective plane) becomes an optional section: nothing in analysis uses it.
- Savings: ~40 pp. S2 (Part II) gets ~110 pp. lighter, which pays for R4. Topology is then learned right before it is used (decision 13's just-in-time principle, applied to topology).
- Tychonoff can stay in ch. 64 or join the block.
- Amend decision 8 from three placements to two: metric in Part II, general in Part VI.
- Sources: Berkeley 202A, Tao 245B, Harvard 114, Folland ch. 4.

**R3. Add a main-line chapter "Probability on measure spaces" at the end of Part IV (after ch. 51), and an optional section in Part VI on characteristic functions.** (evidence: **strong** that measure courses carry probability; **moderate** for making it main line in an analysis book)
- Part IV chapter (~40 pp.):
  - random variables as measurable maps and distributions as push-forwards;
  - independence via product measures (ch. 45);
  - Borel–Cantelli; Kolmogorov's 0–1 law;
  - the weak law by Chebyshev and the strong law (the L⁴ proof, then Etemadi as an exercise);
  - **the CLT by Lindeberg's replacement method**, which needs only Taylor's theorem and so no Fourier;
  - Rademacher functions and the normal numbers theorem as the bridge to Part I's binary expansions.
- Part VI optional section, after ch. 69: characteristic functions, weak convergence of measures (the weak* topology of ch. 64 plus Riesz–Markov), Lévy continuity, Prokhorov.
- This turns the "probability" branch in `curriculum.md` from "entry nodes only" into a real on-ramp.
- Sources: Cambridge Part II P&M, ENS L3 Intégration et probabilités, Oxford B8.1, Folland ch. 10, Stein–Shakarchi IV ch. 5–6.

**R4. Extend ODE in Part II: add a chapter "Linear systems, the matrix exponential and the flow" after ch. 28 `inverse-implicit`** (or fold it into an expanded ch. 24 if pages are tight). (evidence: **moderate**)
- Content:
  - e^{A} via the operator norm (ch. 27) and power series (ch. 17);
  - fundamental matrices and variation of constants;
  - linear constant-coefficient systems and the Jordan form cited from the companion linear-algebra book;
  - **C¹ dependence on initial data**, proved with the implicit function theorem or Gronwall on the variational equation;
  - the local flow and its group property;
  - a preview of the Sturm–Liouville problem −u″ = λu with Dirichlet conditions, linked forward to ch. 66 and ch. 72.
- ~35 pp., paid for by R2.
- Sources: Bonn Analysis II, ENS Topologie et calcul différentiel.

**R5. Add interpolation as the harmonic-analysis on-ramp.** (evidence: **moderate**)
- (a) Add the Marcinkiewicz interpolation theorem, for the diagonal case, to ch. 49 `lebesgue-differentiation`. It gives the Lᵖ bound on the maximal function as a corollary, instead of the ad hoc layer-cake argument. Alternatively put it in ch. 48, where weak Lᵖ is defined.
- (b) Add a Part VI section or short chapter after ch. 69: the Riesz–Thorin theorem by Hadamard's three-lines lemma (a cross-link to Part V ch. 55's Phragmén–Lindelöf), Young's convolution inequality, Hausdorff–Young, and the Hilbert transform on L² via Plancherel as a preview.
- ~25 pp. total. `curriculum.md`'s own branch table names interpolation as the first milestone, so the book should deliver it.
- Sources: Tao 245C, Folland §6.4–6.5, Stein–Shakarchi IV ch. 2.

**R6. Add a `complex-early` reading path (0 → I → II → V) to `config.json`, and state in the Part V opener that Part V needs nothing from Parts III–IV except the Poisson/Abel link.** (evidence: **strong**; cost: near zero)
- Wherever Part V cites a Part III or R1 node, provide a self-contained fallback (the disc case) so that the path is valid.
- Sources: Harvard ("may be taken independently"), Cambridge IB, Stein–Shakarchi II.

**R7. Make the non-motivating parts of Part III optional.** (evidence: **opinion/moderate**)
- Mark ch. 38 `finite-fourier-analysis` optional, alongside ch. 39 (already optional). Nothing on the main line after Part III needs finite abelian groups: Gelfand (ch. 67) is optional too.
- Mark ch. 37's Kirchhoff/descent/Radon sections optional. Keep the ℝᵈ transform, inversion and Plancherel on 𝒮.
- Main-line Part III drops to about 330 pp. and stays focused on the list in ch. 40.
- Groups still arrive just in time for readers who take the optional chapters (decision 13 unchanged in spirit).

**R8. Publish linear-algebra gates in the reading paths and Part openers.** (evidence: **moderate**)
- Companion LA through determinants and eigenvalues **before ch. 27**.
- Inner products, the spectral theorem and SVD **before ch. 34** (orthogonal projection) and ch. 28's second-derivative test.
- Alternating multilinear forms **before the optional forms chapter** (see C4).
- Sources: Harvard 55a → 55b, Bonn, MIT 18.101 prerequisites.

### Consider

**C1. Optional chapter "Hausdorff measure and dimension" after ch. 44 `abstract-measure`.** (evidence: **moderate**) Ch. 44 already builds metric outer measures, so Hausdorff measure is one step on. Content: the Cantor set has dimension log 2/log 3 (a spiral back to Part I ch. 11), self-similar sets, and H^d = c·m on ℝᵈ (statement). This is the entry node for geometric analysis. Sources: Stein–Shakarchi III ch. 7, Berkeley 202B, Tao 245C, Folland ch. 11.

**C2. Strengthen the capstone's last step: prove interior H² regularity** by Nirenberg's difference quotients, on ℝⁿ or on the torus first. Then bootstrap with ch. 70's embedding Hˢ ⊂ C for s > n/2 to get smooth eigenfunctions. If ch. 72 cannot absorb ~15 pp., split it in two: "Weak solutions and the eigenbasis" and "Regularity and classical solutions". (evidence: **moderate**; Bonn V3B1 "L²-regularity theory", Evans §6.3)

**C3. Complex–measure bridge (optional sections of ch. 57, marked "requires Part IV").** Poisson integrals of Lᵖ functions and of measures, Herglotz, and Fatou's theorem on radial limits. This is the classic place where complex analysis, measure and harmonic analysis meet (Rudin *RCA* ch. 11). (evidence: **moderate**)

**C4. Optional chapter "Differential forms and the general Stokes theorem"** after R1's chapter: forms on open sets of ℝⁿ, pullback, d, Stokes on manifolds with boundary embedded in ℝⁿ, and the Brouwer fixed point theorem as the payoff. It needs alternating multilinear algebra from the companion book. (evidence: **moderate**: Chicago, MIT 18.101, Bonn, Zorich, Pugh, Amann–Escher; but Cambridge, Stein–Shakarchi and the quals omit it, hence optional.)

**C5. Reorder Part VI so that Hilbert comes first:** ch. 65 → 60 → 62 → 63 → topology block (R2) → 61 → 64 → 66–72. Lax–Milgram and the projection theorem then arrive early. Part IV's L² toolkit becomes a spiral step rather than a detour, and the Banach theory reads as "what survives without an inner product". This goes against the current note on ch. 65, which chose Banach first deliberately. (evidence: **moderate/opinion**; Stein–Shakarchi, Harvard 114 and Rudin *RCA* put Hilbert first, while Brezis and Folland put Banach first.)

**C6. Trim ch. 29 `riemann-integral-rn` to what Part III actually uses:** Darboux sums on rectangles, content zero, Fubini for continuous functions, linear change of variables and differentiation under the integral sign. Green moves to R1. Keep Jordan content lean. (evidence: **opinion**; Tao *Analysis II* and Stanford skip the multivariable Riemann integral entirely, but our Fourier-on-ℝᵈ-before-Lebesgue route needs a thin version.)

**C7. Bounded self-adjoint spectral theorem.** Either make ch. 67's continuous functional calculus (C*-algebra version) the main-line payoff, or add a section to ch. 66 proving the spectral theorem for bounded self-adjoint operators via polynomial functional calculus. This is needed by the spectral-theory, mathematical-physics and Markov-semigroup branches. (evidence: **opinion**; not on the quals surveyed.)

**C8. Update the branch table in `curriculum.md`:**
- add **Geometric analysis / GMT** (entry nodes: R1, C1, C4, Sobolev);
- add **Spectral theory** (entry nodes: ch. 66, 67, C7);
- add **Calculus of variations** (entry nodes: ch. 64 weak lsc, ch. 70–72);
- upgrade **Probability** to point at R3.

(evidence: **moderate**, from the branch-entry table in §5.)

### Keep as is (checked, no change)
- ℝ before metric spaces (§4.1, strong).
- The optional placement of Part 0's constructions and the end-of-Part-I Dedekind chapters (settled; no programme contradicts it).
- **Lebesgue measure on ℝᵈ before abstract measure** (ch. 42–43 → 44). This matches Stein–Shakarchi III, Tao 245A, Stanford 172, Moscow and Bonn (strong).
- Moving Lᵖ duality, Riesz–Markov and weak topologies into Part VI (Tao 245B, Harvard 114, ENS M1: strong).
- The complex-analysis "second layer" (Bonn, ENS and the UCLA qual all go to Weierstrass, Mittag-Leffler, Riemann mapping and Picard).
- The Dirichlet capstone as the endpoint (§5, strong).

### Page budget of the "change now" set
Net cost: +45 (R1) +40 (R3) +35 (R4) +25 (R5) −40 (R2 merge) −~110 main-line pages from R7 (optional, still printed). Main-line length therefore falls slightly. Part IV grows from 542 to about 590 pp. main line (ch. 41 leaves, R1 and R3 arrive). S3 is then the heaviest semester, so if needed, move R3's probability chapter to a "Summer 2" slot or read it after Part VI.

---

## 7. Sources

- Chicago: [catalog 20300–20500](http://collegecatalog.uchicago.edu/search/?P=MATH+20300-20400-20500), [MATH 20500](https://www.coursicle.com/uchicago/courses/MATH/20500/), [Honors Analysis sheet](https://d3qi0qp55mx5f5.cloudfront.net/mathematics/i/basic_pages/20700app.pdf?mtime=1588972130)
- Stanford: [Math 171 (SUMO)](https://sumo.stanford.edu/pdfs/Pset0/Math171.pdf), [Math 172](https://bulletin.stanford.edu/courses/2089891), [205A](https://web.stanford.edu/~montanar/TEACHING/Math205A/syllabus.html)
- Harvard: [55a handout](https://people.math.harvard.edu/~elkies/M55a.10/h1.pdf), [55b](https://people.math.harvard.edu/~elkies/M55b.16/index.html), [112](https://people.math.harvard.edu/~ctm/home/text/class/harvard/112/02/html/syl.html), [114 (Lurie)](https://people.math.harvard.edu/~lurie/114notes/syllabus.pdf), [114 course page](https://www.math.harvard.edu/course/mathematics-114/)
- UCLA: [Tao 245A announcement](https://terrytao.wordpress.com/2010/08/31/course-announcement-245a-real-analysis/), [245A](https://www.math.ucla.edu/~tao/245a.1.10f/), [245B](https://www.math.ucla.edu/~tao/245b.1.09w/), [245C](https://www.math.ucla.edu/~tao/245c.1.11s)
- Berkeley: [202A (Rieffel)](https://math.berkeley.edu/~rieffel/202AannF24.html), [graduate analysis courses](https://math.berkeley.edu/research/research-areas/mathematical-analysis/mathematical-analysis-graduate-courses)
- Bonn: [standard course content](https://www.mathematics.uni-bonn.de/studium/medienordner-studium-1/dateien/dokumente/bscmath-vorlesungsinhalte-en.pdf/@@download/file/BScMath_Standard-course-content.pdf)
- ENS: [brochure 2023–24](https://www.math.ens.psl.eu/wp-content/uploads/2023/08/Brochure-2023-2024.pdf), [Topologie et calcul différentiel](https://www.math.ens.psl.eu/formations/topologie-et-calcul-differentiel/)
- Moscow State: [Analysis-2](https://fmmp.math.msu.ru/courses/matematicheskij-analiz-(vtoroj-semestr)), [Analysis-4](https://fmmp.math.msu.ru/courses/matematicheskij-analiz-(chetvertyij-semestr)); Zorich II [TOC](https://catalog.lib.uchicago.edu/vufind/Record/11252931/TOC)
- MIT: [18.101](https://math.mit.edu/classes/18.101/fa18/)
- Oxford: [B8.1](https://courses.maths.ox.ac.uk/course/view.php?id=4980), [B4.1](https://courses.maths.ox.ac.uk/course/view.php?id=6073), [Part A synopses](https://www.maths.ox.ac.uk/system/files/attachments/Part%20A%20Mathematics%20Synopses%202024-25.pdf)
- Cambridge: [P&M notes (Breuillard)](https://www.dpmms.cam.ac.uk/study/II/Probability+Measure/2019-2020/lecture-notes-1-16.pdf), [P&M notes (Norris)](https://www.statslab.cam.ac.uk/~jrn10//Lectures/pm.pdf)
- Northwestern: [analysis prelim syllabus](https://www.math.northwestern.edu/graduate/prelims/analysis-syllabus.html)
- Texts: [Princeton Lectures in Analysis](https://en.wikipedia.org/wiki/Princeton_Lectures_in_Analysis), [Folland TOC](https://catdir.loc.gov/catdir/toc/onix03/98037260.html), [Pugh](https://link.springer.com/book/10.1007/978-0-387-21684-3), [Tao Analysis II](https://link.springer.com/book/10.1007/978-981-19-7284-3), [Amann–Escher III](https://link.springer.com/book/10.1007/978-3-7643-7480-8), [Bressoud](https://www.cambridge.org/9780521884747), [Bartle 1996](https://maa.org/programs/maa-awards/writing-awards/return-to-the-riemann-integral), [Evans PDE TOC](https://proofwiki.org/wiki/Book:Lawrence_C._Evans/Partial_Differential_Equations)
