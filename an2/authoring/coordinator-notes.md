
## AN2.5 (ch11) S1, 2026-10-25

- `authoring/STATUS.md`: AN2.5 row → "blueprint (S1 done, S2a next)"; blueprint `an2/authoring/blueprints/ch11.md`.
- Labels cited with † from AN2.3, AN2.4, AN1.9, AN1.4, AN1.7, AN2.9 are provisional (those chapters are not yet re-blueprinted); reconcile at their S1 or at AN2.5 S2a.
- AN2.4's blueprint should provide `thm-ivp-integral-equation` for **continuous** f (not only Lipschitz) and keep the y^{1/3} example and the blow-up alternative; AN2.5 relies on all three.
- `NOTATION.md`: add `Lip(f)` (best Lipschitz constant) if AN2.4 does not.
- Registry (math-atlas, no change required): `thm-arzela-ascoli` (AN2.5) kept with edge `uses thm-metric-compact-equiv`; downstream s-edges CA.5, FA.7, PDE.5 served by `thm-arzela-ascoli`, `thm-arzela-ascoli-compact`, `lem-diagonal-extraction`, `exm-integral-operator-compact`.

## ch14 (AN2.8 Separation, Urysohn–Tietze, LCH), S1, 2026-10-25

- STATUS.md: AN2.8 row → "S1 blueprint (deepen) written; S2a next"; directory `an2/src/ch14-separation-urysohn-lch/`.
- NOTATION.md rows: \( X_\infty \) one-point compactification (not \( X^* \), reserved for duals in FA); \( K \prec f \prec U \); \( C_b(X) \), \( C_0(X) \) next to the existing `C_c` row; convention "regular and normal include T1".
- AN2.7 (ch13) label names are assumed in ch14's "Assumed AN2.7 labels" list; reconcile when ch13 is re-blueprinted (pasting lemma: if ch13 lacks it, ch14 §05 proves `lem-pasting-closed`).
- AN1 re-cut dependency: ch14 cites the metric Urysohn function and the non-compact unit ball (ℓ²) from AN2.3 if the AN1 rewrite of an1 ch08 keeps them; ch14 proves `prp-metric-normal` locally either way, so no break if they go. Please tell the AN1 workflow not to reuse the labels listed in ch14.
- AN2.6 (ch12): ch14 §02 makes a meta-claim that AN2.6's Stone–Weierstrass proof uses only compactness and point separation (so it holds for compact Hausdorff K). Keep that route in ch12, or ch14 weakens the remark (S2a item 6).
- Registry (math-atlas, not edited here): AN2.8 s-edges already [AN2.7, AN2.2, AN1.9]. Suggested soft edges: AN2.8 see AN2.6; FA.5 revisits AN2.8; AM.1 see AN2.8 (continuous partitions of unity before smooth ones); CA.1 see AN2.8 (ℝ²_∞ ≅ S², Riemann sphere).

## ch15 (AN2.14 The Gauge Integral, opt) — S1, 2026-10-25

- **Label clash avoided:** `def-gauge` is MA.18's (Minkowski functional, registry/terms.yaml); this chapter uses `def-interval-gauge`. Registry terms to add when drafted: gauge (on an interval) → `def-interval-gauge@AN2.14`, δ-fine → `def-delta-fine`, gauge integral / Henstock–Kurzweil integral → `def-gauge-integral`, Cousin's lemma → `thm-cousin`, Saks–Henstock lemma → `lem-saks-henstock`, Hake's theorem → `thm-hake`.
- **Edges:** keep `AN2.14: {s: [AN2.10]}`. Suggested soft edge `see: [AN1.9, AN2.9]` (uniform convergence restated in one remark/B exercise; Cantor function in one warning). Suggested soft pointers *to* AN2.14 (never s): AN2.15 (Volterra's derivative is gauge integrable), MT (Lebesgue = absolutely gauge integrable).
- **Exam targets:** AN2.14 serves no §E1 target item; do not add it to any target's `chapters`.
- **AN2.10 dependency:** blueprint assumes labels `def-tagged-partition`, `def-riemann-sum`, `def-mesh`, `thm-riemann-sum-criterion` (mesh form, α(x) = x), `def-measure-zero`, `thm-lebesgue-criterion`; reconcile when AN2.10's blueprint lands.
- **AN2.9 dependency (soft):** §03 warning uses the Cantor function (continuous, increasing, φ′ = 0 off C); ask AN2.9 to build it or the warning states the properties.
- **NOTATION.md rows:** gauge δ: [a, b] → (0, ∞); "δ-fine"; δ₁ ∧ δ₂ (pointwise min of gauges); (R)∫ vs (G)∫ when compared.
- **STATUS.md:** AN2.14 row → "S1 blueprint written (ch15.md); S2a next".
