# Chapter 10 — S5 Referee A (proofs)

**Scope:** `src/ch10-least-upper-bound/` §01–§07 and index (read-only), against `authoring/blueprints/ch10.md` and the curriculum node "The least upper bound axiom node"; STYLE §4, §10, §11; NOTATION; kwok-proof `ana.md` §1.
**Referee:** A (proofs), blind to Referee B. Verdicts recorded in `authoring/ledger/ch10.yaml` (stage S5a, by refereeA).

**Method.**
- Every proof read step by step with the reason for each step; quantifier order and dependence of every constant (h, C, N, n, δ, ε-splits) written out; one dropped-hypothesis counterexample per theorem (evidence column).
- All 50 sidecars in `verify/ch10/` run with `.venv/bin/python`: 0 failures.
- Own exact-rational checks (script in scratchpad, not the sidecars): √2 constants on a 2000-point grid of s ∈ [1,2] (both cases); √3 faded proof; n-th-root constants C = n(s+1)^(n−1), h = min{1/2, |sⁿ−a|/(2C)} on 3000 random (a, n, s); the power estimate yᵏ−xᵏ ≤ k yᵏ⁻¹(y−x) (2000 cases); x₀ = a/(1+a) ∈ S; C4 cubic identities and both h's on a 1000-point grid, g(0.68), g(0.69); all decimal/fraction arithmetic (1/408, 577/408, 1/190, 267²; 1.25³, 1.26³, 1.70³, 1.71³, 1.4143²; 334/3334; 12√2 floor; m₁ = 14, m₂ = 141 and decimal nesting for n ≤ 10); thirds construction A1(e) and 200 random lists; bisection intervals; absolute-value solution sets, max/min formulas and the max-Lipschitz bound; ε-witnesses of §04.

**Counts:** correct 120 · minor 2 · gap 0 · error 1 (123 ledger items).

## Flagged claims

| Claim | Verdict | Evidence |
|---|---|---|
| 05:86 "The contradiction step is ¬I, not RAA" | correct | Outer step assumes "ℕ bounded above", reaches ⊥, concludes the negation. |
| 05:86 "The proof does contain a classical step, but it comes after the ¬I, in the proof's last paragraph" | **error** | 05:78 passes from "s − 1 is not an upper bound" to "there is n ∈ ℕ with n > s − 1": the same not-all ⇒ some-not law, inside the ¬I box. So the proof as written has two classical steps, one before the ¬I closes. Fix (preferred): replace 05:78 by the RAA-free step already used at 05:179: for every n ∈ ℕ, n + 1 ∈ ℕ so n + 1 ≤ s, i.e. n ≤ s − 1; so s − 1 is an upper bound and (S2) gives s ≤ s − 1, contradiction. Then the remark is true as stated. Else reword the remark. Same pattern in the 05 C1(a) model solution (05:300) and marking scheme line 311, which should be kept consistent with whichever fix is chosen. |
| 04:123 forming (aₙ) is countable choice; the corollary itself needs none | correct | One existential instantiation per n; the sequence needs CC(ℝ) in general. |
| 07:126 uncountability intervals by recursion, "no choice principle is involved" | correct | I₁ explicit; I_(n+1) = L or R by a decidable-in-classical-logic explicit rule from (Iₙ, x_(n+1)); recursion theorem suffices. |
| 05 ℝ(x) order is an ordered-field order | correct | Well-definedness αβ·β′² = α′β′·β² (05:151); C2 solution verifies P + P ⊆ P (degree cases), P·P ⊆ P, exactly one of f, −f ∈ P; O1–O4 follow. Constants ordered as in ℝ. |
| 05:179 failing line in ℝ(x) is "By the axiom, ℕ has a supremum" | correct | Any upper bound M gives the smaller upper bound M − 1; every other line is ordered-field algebra. |
| 07 table ℝ(x) column | correct | (x, x+1) has no rational; p² = xq² parity of degrees; [n, x/n] proved empty in C3 (checked). |

## Findings (every ledger item)

| file:line | item | verdict | evidence |
|---|---|---|---|
| 01:17 | `def-ordered-field` | correct | F1-F9, O1-O4 standard; <-primitive; derived <= chain rule at 01:55 checked |
| 01:59 | `lem-field-algebra` | correct | drop F8 (Z): (a)-(c),(e) hold, (d) holds in Z too; statement uses only F1-F9 as claimed |
| 01:77 | `proof:lem-field-algebra` | correct | each axiom citation checked; (e) uses F6 to move ab(1+1) to 2ab (cited) |
| 01:95 | `exm-ordered-fields-q-r` | correct | assumptions stated honestly; Q order via pq'<p'q with q,q'>0 |
| 01:107 | `exm-integers-not-a-field` | correct | 2m=1 has no integer solution; F8 is the only failing field axiom |
| 01:127 | `thm-ordered-field-rules` | correct | drop a,b>=0 in (g): a=-2,b=1; drop c>0 in (c): c=-1; each part's hypothesis used |
| 01:148 | `proof:thm-ordered-field-rules` | correct | (a)-(h) step reasons checked; (f) a^-1 = a(a^-1)^2; (g) <= uses both signs hypotheses; (h) 1+1>1>0 |
| 01:175 | `check:01-ordered-fields:1` | correct | 1>0 => 1+1>1>0 => 0>0 in F_2; independent of chosen < |
| 01:189 | `def-absolute-value` | correct | well defined by trichotomy |
| 01:206 | `prp-absolute-value-rules` | correct | all four parts checked on grid (sidecar + own); (d) strict/non-strict both |
| 01:223 | `proof:prp-absolute-value-rules` | correct | (b) both sides in {xy,-xy}, non-negative, non-zero when xy!=0: correct |
| 01:243 | `exm-solve-abs-inequality` | correct | own check on 600 rationals: /4-3x/<2 iff 2/3<x<2; /4-3x/=3/x-4/3/ |
| 01:257 | `thm-triangle-inequality` | correct | no hypothesis beyond ordered field; equality iff xy>=0 checked |
| 01:272 | `proof:thm-triangle-inequality` | correct | adds sandwiches by rules (b), then abs-rules (d) with r=/x/+/y/; (b) via x=(x-y)+y |
| 01:296 | `exr-ordered-fields-a1` | correct | (a) O3/F3/hyp/O2; (b) a=-2,b=1; (c) true; (d) F8 |
| 01:319 | `exr-ordered-fields-b1` | correct | (b) ac<=ad<bd with a=0 case; (c) trichotomy on b |
| 01:339 | `exr-ordered-fields-b2` | correct | (b) squares equal iff 2xy=2/xy/ (2!=0) iff xy>=0 |
| 01:362 | `exr-ordered-fields-b3` | correct | own grid check: (-1,4) and (0,inf) |
| 01:381 | `exr-ordered-fields-c1` | minor | 01:398 (c) asserts n->n.1 'respects addition' without proof ((m+n).1=m.1+n.1 needs an induction); not needed for injectivity; rest correct |
| 01:401 | `exr-ordered-fields-c2` | correct | formulas and Lipschitz bound checked on 2000 random rational quadruples |
| 02:13 | `def-upper-bound` | correct | negation via trichotomy correct; vacuous case via prp-vacuous-implication |
| 02:35 | `def-bounded-above` | correct | witness max{M,0}+1 > M correct; quantifier-swap remark correct |
| 02:53 | `def-maximum` | correct | uniqueness of max by two <= and trichotomy |
| 02:85 | `def-supremum` | correct | S1/S2 in F; symbols match |
| 02:107 | `thm-sup-unique` | correct | no hypothesis to drop; in any ordered field |
| 02:113 | `proof:thm-sup-unique` | correct | S1 of one vs S2 of other, swap, trichotomy |
| 02:121 | `def-infimum` | correct | mirror of def-supremum |
| 02:134 | `exm-sup-finite-and-closed` | correct | max is sup argument correct |
| 02:148 | `exm-sup-open-interval` | correct | M<1 upper bound => M>=1/2>0, midpoint (M+1)/2 in (0,1) beats M; valid in Q |
| 02:162 | `exm-sup-one-minus-reciprocal` | correct | n>0 by induction, 1-1/n<1-1/(n+1); deferral of S2 correct |
| 02:186 | `check:02-suprema:1` | correct | max=sup=1/2, min=inf=-1 |
| 02:200 | `thm-no-rational-sup-sqrt2` | correct | drop 'in Q' (work in R): conclusion false (sup=sqrt2); exact-rational grid of 2000 s in [1,2]: case1 h in (0,1/6], (s+h)^2<2; case2 (s-h)^2>2, s-h>0 |
| 02:216 | `proof:thm-no-rational-sup-sqrt2` | correct | s>=1 from 1 in A used for h<=1/6; (g) applied with s-h>0; both h rational; every step reasoned |
| 02:258 | `exr-suprema-a1` | correct | (e) h=1/408, 577/408, 577^2=2*408^2+1 exact; (f) correct: only thm-sqrt2-irrational line fails |
| 02:295 | `exr-suprema-b1` | correct | correct |
| 02:315 | `exr-suprema-b2` | correct | negation of S1 and S2 correct; witness M=1 |
| 02:341 | `exr-suprema-b3` | correct | x=M/(1-M)+1 gives x/(x+1)>M: checked for M in [1/2,1) grid |
| 02:361 | `exr-suprema-c1` | correct | (b) Case 1 needs s>=1: supplied by 1 in B; (c) b>=1 as largest element; correct |
| 02:382 | `exr-suprema-c2` | correct | U(empty)=F no min; U(F)=empty |
| 03:11 | `ax-least-upper-bound` | correct | both hypotheses shown necessary (empty set; [0,inf)) |
| 03:41 | `exm-lub-first-use` | correct | bound 2 via (g); 1<=s<=2 |
| 03:63 | `check:03-the-axiom:1` | correct | sup=3=max |
| 03:81 | `thm-inf-neg-sup` | correct | holds in any ordered field; no hypothesis to drop |
| 03:98 | `proof:thm-inf-neg-sup` | correct | (a) via rules (a); (b) both directions use (a) with m=-M; final clause correct |
| 03:110 | `thm-greatest-lower-bound` | correct | drop non-empty: empty set; drop bounded below: (-inf,0] |
| 03:119 | `proof:thm-greatest-lower-bound` | correct | correct; alternative via sup of lower bounds also correct (03:123) |
| 03:145 | `exr-the-axiom-a1` | correct | (b) x=/M/+1, x^2>=x>M; (c) midpoint M/2 |
| 03:170 | `exr-the-axiom-b1` | correct | correct |
| 03:180 | `exr-the-axiom-b2` | correct | correct incl. equality case |
| 03:194 | `exr-the-axiom-c1` | correct | (b) thm-inf-neg-sup (a),(b) applied to -A correctly; (c) correct |
| 03:212 | `exr-the-axiom-c2` | correct | (b) q in U and least => sup in Q, contradiction |
| 04:11 | `thm-sup-epsilon` | correct | drop 's upper bound': A=(0,1), s=1/2 (remark 04:59); valid in any ordered field |
| 04:50 | `proof:thm-sup-epsilon` | correct | eps:=s-M>0 depends only on M,s; quantifier order eps then a correct |
| 04:68 | `check:04-epsilon-characterization:1` | correct | (ii) iff s in A: correct |
| 04:86 | `exm-sup-squares-epsilon` | correct | backwards Idea/forward proof; h=min{1/2,eps/2} depends on eps only; checked for 208 eps values |
| 04:110 | `cor-sup-approximation` | correct | claim of countable choice only for forming the sequence: accurate; corollary itself needs none |
| 04:119 | `proof:cor-sup-approximation` | correct | n>0, 1/n>0, thm-sup-epsilon |
| 04:129 | `thm-sup-monotone` | correct | drop A non-empty: empty set; drop B bounded above: B=[0,inf), no sup B |
| 04:135 | `proof:thm-sup-monotone` | correct | correct |
| 04:147 | `thm-sup-scaling` | correct | drop c>0 in (a): c=-1, A=(0,1] (04:175) |
| 04:162 | `proof:thm-sup-scaling` | correct | (a) two inequalities via 1/c>0; (b) (-c)A=-(cA) and thm-inf-neg-sup |
| 04:185 | `thm-sup-sum` | correct | drop B non-empty: A+B empty; drop B bounded: A+B unbounded |
| 04:206 | `proof:thm-sup-sum` | correct | eps/2 depends on eps only; a,b depend on eps; final eps:=supA+supB-sup(A+B) valid |
| 04:240 | `exr-epsilon-characterization-a1` | correct | (a) max{0,5-eps/2}; (c) max{3,4-eps/2}; (e) 24/25, 5.96>5.9 exact |
| 04:269 | `exr-epsilon-characterization-b1` | correct | h=min{1,eps/4}, x=2-h in [1,2): checked numerically |
| 04:285 | `exr-epsilon-characterization-b2` | correct | correct |
| 04:295 | `exr-epsilon-characterization-b3` | correct | A={0},B=[0,1] example correct |
| 04:315 | `exr-epsilon-characterization-c1` | correct | (a) [-2,-1]^2 contains 4; (b) positivity used in both halves; correct |
| 04:351 | `exr-epsilon-characterization-c2` | correct | (a)-(c) correct; scheme 1+2+3+2+2=10; alternative split earns 5 |
| 04:387 | `exr-epsilon-characterization-c3` | correct | (a) false claim, line 2; (b) TRUE claim, line 2 flawed, A=B=(0,1) defeats it; flawed exactly there |
| 05:9 | `def-inductive-set` | correct | examples/non-example checked |
| 05:45 | `exm-naturals-at-least-one` | correct | [1,inf) inductive => N subset; 0<1/n<=1 |
| 05:65 | `thm-naturals-unbounded` | error | ERROR in remark 05:86: says the classical step 'comes after the negI, in the proof's last paragraph', but 05:78 ('s-1 is not an upper bound ... Hence there is n with n>s-1') is the same not-all=>some-not law inside the negI box. Fix: either say so, or replace 05:78 by the RAA-free step 'for every n, n+1<=s, so n<=s-1; s-1 is an upper bound; S2 gives s<=s-1' (the argument of 05:179). The negI-not-RAA claim for the outer step is right. Dropped hypothesis: in R(x) (no LUB) N bounded. |
| 05:75 | `proof:thm-naturals-unbounded` | correct | mathematically correct; both hypotheses of axiom used (1 in N, assumption) |
| 05:91 | `cor-archimedean-epsilon` | correct | n depends on eps (n>1/eps); moreover clause via rules (f) |
| 05:99 | `proof:cor-archimedean-epsilon` | correct | correct |
| 05:107 | `check:05-archimedean-property:1` | correct | 334 and 3334 exact |
| 05:119 | `exm-sup-one-minus-reciprocal-finished` | correct | 100/101>0.99 exact |
| 05:157 | `exm-nonarchimedean-field` | minor | order is a genuine ordered-field order (checked via exr C2: P closed under +,x; exactly one of f,-f in P; well-defined by alpha beta'^2 identity). Minor: the example's use of rules (f) in R(x) rests on ordered-field axioms that are only verified in exercise C2 (05:153 defers them); failing line correctly identified as the LUB line (05:179), M-1 argument correct |
| 05:199 | `exr-archimedean-property-a1` | correct | (b) [1/2,inf), Z inductive; [0,10], N u {1/2} not |
| 05:222 | `exr-archimedean-property-b1` | correct | correct |
| 05:236 | `exr-archimedean-property-b2` | correct | n>y/a, multiply by a>0 |
| 05:248 | `exr-archimedean-property-b3` | correct | correct |
| 05:262 | `exr-archimedean-property-b4` | correct | order iii,i,iv,vii,ii,vi,viii admissible; (v) quantifier swap fails; (ix) eps chosen after n, conflicts with (i) |
| 05:290 | `exr-archimedean-property-c1` | correct | (a) correct; (b) circularity correct; no integer >= x in R(x); scheme sums to 10 |
| 05:320 | `exr-archimedean-property-c2` | correct | (a)-(d) correct: degree cases in (c) right; trichotomy uses 0 not in P |
| 05:368 | `exr-archimedean-property-c3` | correct | r=m/k<=m<m+1; Q Archimedean, fails LUB |
| 06:9 | `thm-sqrt2-exists` | correct | drop the axiom (work in Q): false; constants verified on 2000-point rational grid |
| 06:27 | `proof:thm-sqrt2-exists` | correct | S2 in case 2, S1 in case 1, s>=1 used for h<=1/6, uniqueness via (g) |
| 06:70 | `thm-nth-root` | correct | drop a>0: a=0 no positive root, a<0 n even none; constants C=n(s+1)^(n-1), h=min{1/2,/s^n-a//(2C)} checked on 3000 random (a,n,s) exact rationals |
| 06:94 | `proof:thm-nth-root` | correct | claim: y^k-x^k<=k y^(k-1)(y-x) checked 2000 cases; case 2 s-h>0 via h<s/(2n) uses a>0; x0=a/(1+a) in S checked |
| 06:160 | `exm-cube-root-bounds` | correct | 1.25^3, 1.26^3 exact |
| 06:182 | `lem-integer-part` | correct | drop Archimedes: fails in R(x) (exr C1) |
| 06:194 | `proof:lem-integer-part` | correct | T non-empty via p,j; j0=1 and j0>=2 cases; uniqueness via positive integer in N |
| 06:211 | `thm-rationals-dense` | correct | fails in R(x) (x,x+1) |
| 06:235 | `proof:thm-rationals-dense` | correct | n depends on y-x (stated); m=floor(nx)+1; chain nx<m<=nx+1<ny |
| 06:243 | `exm-rational-between` | correct | n=12 least (31/22)^2<2; floor(12 sqrt2)=16; 17/12 exact |
| 06:259 | `cor-irrationals-dense` | correct | correct |
| 06:263 | `proof:cor-irrationals-dense` | correct | shift by sqrt2; difference of rationals rational |
| 06:269 | `check:06-density-and-roots:1` | correct | 1.4143^2=2.00024449 exact; sqrt2*1e-7 |
| 06:289 | `exr-density-and-roots-a1` | correct | (d) false correctly argued; (f) h=1/190, 267^2=71289<72200 exact |
| 06:324 | `exr-density-and-roots-b1` | correct | correct |
| 06:336 | `exr-density-and-roots-b2` | correct | faded proof: given case correct (h<=1/3, (3+s^2)/2<3); completion h=(s^2-3)/(2s) checked on grid |
| 06:362 | `exr-density-and-roots-b3` | correct | 1.70^3=4.913, 1.71^3=5.000211 exact |
| 06:376 | `exr-density-and-roots-c1` | correct | correct; scheme sums 10; alternative h=min{1,(2-s^2)/6} valid since 2s+1<=5 |
| 06:410 | `exr-density-and-roots-c2` | correct | 2^k>k induction; m=floor(2^k x)+1 |
| 06:430 | `exr-density-and-roots-c3` | correct | true conclusion; line (2) is exactly the flaw (x=0: q/2); repair via R_n correct |
| 07:18 | `thm-nested-intervals` | correct | table rows 07:58-64 each a genuine failure; closed (0,1/n), bounded [n,inf), nested [n,n+1], field Q, shrinking [-1/n,1+1/n] |
| 07:32 | `proof:thm-nested-intervals` | correct | claim a_m<=a_k<=b_k<=b_n; alpha in I_n by S1/S2; uniqueness via eps=v-u |
| 07:78 | `check:07-nested-intervals:1` | correct | (0,1/n] correct witness |
| 07:92 | `thm-reals-uncountable` | correct | recursion with explicit rule: 'no choice principle' accurate; thirds disjoint 2d/3<d; checked 200 random lists x 20 steps |
| 07:106 | `proof:thm-reals-uncountable` | correct | x_{n+1} not in I_{n+1} in both cases; only existence half used (claim 07:135 true) |
| 07:166 | `exr-nested-intervals-a1` | correct | (e) I1=[1,2], I2=[5/3,2], I3=[5/3,16/9] recomputed; (f) correct |
| 07:197 | `exr-nested-intervals-b1` | correct | (b) 10m_n<=m_{n+1}<=10m_n+9 verified n<=10; m1=14,m2=141 |
| 07:218 | `exr-nested-intervals-b2` | correct | correct |
| 07:234 | `exr-nested-intervals-c1` | correct | (b) induction correct; (c) n>(M-a)/(y-s) works incl. M=a; scheme sums 10 |
| 07:278 | `exr-nested-intervals-c2` | correct | L=[x+d/4,x+d/3], R=[y-d/3,y-d/4] disjoint, inside (x,y) |
| 07:293 | `exr-nested-intervals-c3` | correct | (b),(c) degree cases correct; N>lc(p)/lc(q), n>lc(q)/lc(p) work; (d) correct |
| 07:335 | `exr-nested-intervals-c4` | correct | identities checked on 500 rational pairs; h=(1-g)/16 and (g-1)/10 checked on 1000-point grid; g(0.68),g(0.69) exact; scheme 10 |
| 07:400 | `exr-nested-intervals-r1` | correct | (ii)=>(iii) via Archimedes, n depends on s-u |
| 07:424 | `exr-nested-intervals-r2` | correct | t^2 positive root of 2 by uniqueness |
| 07:441 | `exr-nested-intervals-r3` | correct | negI correctly labelled (irrational = not rational); sqrt2 sqrt3 = sqrt6 by uniqueness |
| 07:459 | `exr-nested-intervals-r4` | correct | equality iff (1-x)(1+x)>=0 iff x in [-1,1]; own grid check |

## Resolution (S7, reviser, 2026-09-28)

The chapter is now `src/ch11-least-upper-bound/` (ledger `authoring/ledger/ch11.yaml`). Ledger: each item below has an S7 verdict `correct` by `reviser`, awaiting the S7 re-referee.

| Finding | Resolution |
|---|---|
| 05:86 `thm-naturals-unbounded` (error) | Preferred fix taken. The proof's middle paragraph is now the direct step of 05:179: for every \( n \), \( n + 1 \in \nN \) and \( n + 1 \le s \), so \( n \le s - 1 \); hence \( s - 1 \) is an upper bound and (S2) gives \( s \le s - 1 \). The Idea says the same. The remark now says every step inside the \( \neg I \) box is direct, and that the proof does not use "s − 1 is not an upper bound, so some n exceeds it", which would need the classical law; the one classical step is the last paragraph. The §05 list "The line of the proof that fails" and the sentence after it match (the ℝ(x) argument is now literally the middle paragraph with \( M \) for \( s \)). |
| 05:300/311 C1(a) model solution and scheme | Model solution uses the direct step. Scheme: "2: shows \( s - 1 \) is an upper bound (inductive + (S1), for every n)"; "1: applies (S2) to \( s - 1 \), contradiction, concludes". New fatal error: dropping "for every n". The classical variant ("by (S2) or @thm-sup-epsilon with ε = 1, some n > s − 1") is accepted explicitly for the same 3 points, with a note that it adds a classical step inside the box. |
| 05:157 `exm-nonarchimedean-field` (minor) | The text before the example now says that the example uses the ordered-field rules in ℝ(x) and so rests on @exr-archimedean-property-c2; ledgered. |
| 01:381 `exr-ordered-fields-c1` (minor) | (c) now proves \( (m + n)\cdot 1 = m\cdot 1 + n\cdot 1 \) by induction on \( n \). |
