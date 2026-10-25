# AN2 layout: Apostol's skeleton (2026-10-25)

Binding plan: math-atlas `spec/08-map-v2.md` §C3 and §C6. AN2 becomes *Integration, Series, and
Function Spaces* (subdir `integration-series-and-function-spaces`). It covers Apostol,
*Mathematical Analysis* (2e), Chapters 6–9, plus function spaces: 12 chapters, 2 in segment B and
2 optional. The CL volume is dissolved, and its chapters take the new ids AN2.9–AN2.14. The
companion file is `an1/authoring/design/layout-apostol.md`.

The blueprint files were renamed to this order. **Their bodies were not rewritten.** They follow
the old layout (old directories, "Part" wording, old prerequisites) until each chapter is
re-blueprinted. A chapter with no blueprint yet has none listed.

| Pos. | Atlas id | Title (spec/08 C3) | Directory (planned) | Blueprint | From | Apostol / reference |
|---|---|---|---|---|---|---|
| 1 | AN2.9 (new) | Functions of Bounded Variation and Rectifiable Curves | `an2/src/ch01-bounded-variation/` | — (to write) | CL.1 in the spec/08 draft | 6; Pugh 3 exercises |
| 2 | AN1.8 | The Riemann–Darboux Integral (moved in) | `an2/src/ch02-riemann-darboux-integral/` | `an2/authoring/blueprints/ch02.md` | an1 ch08 | 7.1–7.10 (Riemann case); Abbott 7 |
| 3 | AN2.10 (new) | The Riemann–Stieltjes Integral (closing: full proof of Lebesgue's criterion) | `an2/src/ch03-riemann-stieltjes-integral/` | — (to write) | CL.2 | 7.1–7.16, 7.26; PMA 6; Ross §35 |
| 4 | AN1.3 | Infinite Series (moved in) | `an2/src/ch04-infinite-series/` | `an2/authoring/blueprints/ch04.md` | an1 ch03 | 8.1–8.19 |
| 5 | AN2.12 (new) | Double Series, Infinite Products, and the Euler Product | `an2/src/ch05-double-series-and-products/` | — (to write) | CL.4 | 8.20–8.25; Pugh 3 |
| 6 | AN1.9 | Sequences and Series of Functions (moved in; takes the B(S), C(K) completeness examples) | `an2/src/ch06-sequences-of-functions/` | `an2/authoring/blueprints/ch06.md` | an1 ch09 | 9.1–9.13 |
| 7 | AN1.10 | Power Series, Taylor Series, and the Elementary Functions (moved in) | `an2/src/ch07-power-series/` | `an2/authoring/blueprints/ch07.md` | an1 ch10 | 9.14–9.20; complex exponential of Apostol 1 |
| 8 | AN2.11 (new) | Integrals with a Parameter, Euler Summation, and the Gamma Function | `an2/src/ch08-parameter-integrals-and-gamma/` | — (to write) | CL.3 | 7.17–7.20; PMA 8; Spivak 19 |
| 9 | AN2.13 (new) | Summability and Tauberian Theorems | `an2/src/ch09-summability-and-tauberian/` | — (to write) | CL.5 | 8.26, 9.21–9.23 |
| 10 | AN2.4 | Contraction Mappings and the Picard–Lindelöf Theorem | `an2/src/ch10-contraction-picard/` | `an2/authoring/blueprints/ch10.md` | an2 ch04 | reprise of 4.48 |
| 11 | AN2.5 | Equicontinuity, the Arzelà–Ascoli Theorem, and Peano's Theorem | `an2/src/ch11-arzela-ascoli-peano/` | `an2/authoring/blueprints/ch11.md` | an2 ch05 | — |
| 12 | AN2.6 | Density and Category in C(K): Stone–Weierstrass and Baire (Bernstein proof first) | `an2/src/ch12-stone-weierstrass-baire/` | `an2/authoring/blueprints/ch12.md` | an2 ch06 | 9 (Bernstein) |
| 13 | AN2.7 | Topological Spaces, Products, and Compactness (seg B) | `an2/src/ch13-topological-spaces-compactness/` | `an2/authoring/blueprints/ch13.md` | an2 ch07 | — |
| 14 | AN2.8 | Separation, Urysohn–Tietze, and Locally Compact Spaces (seg B) | `an2/src/ch14-separation-urysohn-lch/` | `an2/authoring/blueprints/ch14.md` | an2 ch08 | — |
| 15 | AN2.14 (new, opt) | The Gauge Integral | `an2/src/ch15-gauge-integral/` | — (to write) | CL.6 | Bartle–Sherbert 10; Abbott 8.1 |
| 16 | AN2.15 (new, opt) | A Gallery of Pathological Functions | `an2/src/ch16-pathological-functions/` | — (to write) | AN1.12 in the spec/08 draft | 9 (space-filling curve) |

Chapters that left AN2 for AN1: AN2.1 → AN1 ch03, AN2.2 → AN1 ch05, AN2.3 → AN1 ch08.

Notes from spec/08 C3:
- No s-edge may depend on the optional chapters AN2.14 and AN2.15. AN2.15 closes the
  pathological-functions table that starts in F4.7.
- In C5's AN2 column, Scratch Work and fading support are halved.
- The edge changes recorded in spec/08 C6 apply when each chapter is re-blueprinted: AN2.4 adds
  s AN1.9 (Banach fixed point is now proved in AN2.2); AN2.6 and AN2.8 add s AN1.9.
