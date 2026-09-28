# Drafting brief (shared by all section-drafting agents)

You are drafting sections of a comprehensive, reader-caring textbook (Pandoc Markdown -> static site + PDF). The repository root is the book; `./build.py` builds it.

Drafting is stage **S3** of the per-chapter pipeline (`authoring/PIPELINE.md`). Before you start, the chapter's blueprint has been expanded (S1) and verified (S2) and is **frozen**: its statements, hypotheses and proof routes have been checked by a referee who hunted for counterexamples. After you finish, mechanical gates (S4), two blind referees (S5) and an exercise verifier (S6) read what you wrote. They also read your sidecar scripts and your dependency ledger, so write those for them.

## Read before writing
1. `authoring/STYLE.md`: the writing standard. Follow it exactly: explain template, Idea/Proof registers, Quick checks, warnings, A/B/C (and R) exercises with complete solutions, the dependency-ledger and meta-claim rules of §9, and the reader-alone formats of §11.
2. `authoring/NOTATION.md`: fixed notation and the typesetting rules for logic; `latex/macros.tex` for available macros; `latex/fitch-book.sty` for derivations (Part 0).
3. `~/coding/book-template/src/ch00-demo/01-every-environment.md`: the markup of every environment. The approved exemplar chapter named in `authoring/STATUS.md` shows it in use in this book; imitate its register, density and exercise design.
4. `authoring/blueprints/chNN.md`: your chapter's **frozen** blueprint is the spec: content, labels to create, statements with all hypotheses, proof routes, examples, exercises with intended answers, key proofs, exit checks, where the §11 items go, and the promises to pay. `authoring/design/decisions.md` and `curriculum.md` explain why the book is shaped as it is; read the parts about your chapter.
5. The earlier chapters' label lists: `grep -rho "{#[a-z]*-[^} ]*" src/chNN-*/` for each earlier chapter. Read the specific earlier results you cite, so your recall of them is accurate.
6. The promise table in `authoring/STATUS.md` (and `tools/promises.py`'s list for your chapter): the promises your chapter must pay.
7. Old versions of your files (if any), to preserve labels.

## Rules
- **Original prose only.** Do not copy from any textbook. A reference work may be consulted only to check that a statement is true or that coverage is complete. Never paraphrase its text, examples or exercises. Copyrighted material is never committed to this repository.
- **Follow the frozen blueprint.** If you find it wrong (a false statement, a missing hypothesis, a route citing a label that does not say what the route needs), write the correct mathematics in your draft and report it under "Blueprint deviations" with a counterexample or the reason. The coordinator sends it back to S2's referee.
- **Displays.** Keep every display inside the text column: a formula wider than about 60 characters of ordinary math is broken with `aligned` or `cases` (a `\tag` goes after `\end{aligned}`, never inside). No blank line inside a `\[ ... \]`.
- **Structure.** Section length ~2,500–5,000 prose words (math spans count as one word). Complete: opening frame; notions per the explain template; theorems with lead-in / Idea / Proof / aftermath; ≥1 `::: {.check}` followed (not nested) by a `::: {.solution}` block; ≥1 `::: {.warning}`; `## Exercises` with `### A. Check your understanding` / `### B. Practice` / `### C. Going deeper`, and `### R. Review` in the chapter's **last** section only; each exercise `::: {#exr-<section-slug>-a1}` titled `[A1]` (`-r1` titled `[R1]`, and so on) followed by a complete `::: {.solution}`. A Gate section follows STYLE §11.10 instead.
- **Math.** `\( \)` and `\[ \]` only. Relation symbols are typeset, never unicode characters: proof-direction tags are `\( (\Rightarrow) \)`, `\( (\Leftarrow) \)`, `\( (\subseteq) \)`, `\( (\supseteq) \)`, and a chain reads `(a) \( \Rightarrow \) (b)`. Pandoc fenced divs must be closed, with blank lines around them.
- **Derivations (Part 0)** are fitch.sty `nd` environments in a raw LaTeX block, as `latex/fitch-book.sty` and NOTATION.md describe: `\hypo`, `\have`, `\open`/`\close`, the rule macros (`\ai{…}`, `\ie{…}`, `\raa{…}`, …) or `\by{text}{refs}`. Never `array`s. A deliberately invalid derivation (a find-the-error item) carries the marker that `tools/check_fitch.py` documents, so the checker expects its failure.
- **Labels** are globally unique: grep `src/` before creating one. Keep every "keep label" exactly.
- **References.** `@label` refs only to earlier material (earlier chapters, earlier sections of this chapter, or earlier in your file). Forward pointers in prose say "in Chapter N" without an `@ref`. No proof, idea or claim may rest on an exercise, and every result is either proved or plainly marked as not proved here, with nothing depending on it.
- **Sidecar scripts.** Every non-trivial computation and every chosen constant (N, δ, r, a bound, a numeric answer) is checked by `verify/chNN/<label>.py`, named after the block that quotes the values. Put the values the text quotes in a dict `QUOTED = {...}` at the top, then `assert` each one from an independent computation (sympy, exact fractions, or a numeric check of a constant on several values). The script exits non-zero on failure and runs with `.venv/bin/python` from the repo root. One script may cover several values of one block. Never mention the scripts, or any software, in the book text (runnable `{.python .run}` cells are the only exception).
- **Dependency ledger.** Every section file ends with the `<!-- dependency ledger … -->` comment of STYLE §9: every fact a proof, idea, claim, solution or example uses without an `@ref`, with its source; `none:` if there are none. Be honest. An unledgered fact that a referee finds is a finding against the section; a ledgered one is a note.
- **Meta-claims.** Every sentence about the book's own text ("the classical step comes after the proof", "everything else fails in ℚ") points at something on the page and is true of it (STYLE §9). If you cannot make one checkable, cut it.
- **Reader-alone items** (STYLE §11) go where the blueprint puts them: comprehension parts for key proofs; find-the-error with a true conclusion; proof ordering and faded proofs (Parts 0–I, later only for new moves); try-it-first (at most two per chapter); hint ladders on C items; and a `**Marking scheme.**` ending every exit check's and write-up C item's solution.
- **index.md.** If you write the chapter's `index.md`, write it last, against the delivered sections. It has the **Time** line (STYLE §2), computed from your sections' prose word counts and exercise counts by the formula in `authoring/design/research-reader.md` B1.
- **Spelling.** American spelling. Add genuine new words to `spelling.txt` (append only).
- **Scope.** Do not delete or rename files other than those assigned; do not edit other sections, the config, or `authoring/STATUS.md` (report promises instead).

## When done
1. Run your sidecars: `for f in verify/chNN/*.py; do .venv/bin/python "$f" || echo "FAIL $f"; done`.
2. Run the first-tranche gates on your files, as each tool's `--help` documents: `tools/check_structure.py`, `tools/check_fitch.py` (Part 0), `tools/promises.py`. Fix everything they report in YOUR files.
3. Build in your own copy (see below): `./build.py html 2>&1 | grep -i "warn\|error" | head -30`, then `tools/check_rendered.py` on that build. Fix warnings originating in your files; ignore issues from files that are not yours.
4. Run `.venv/bin/python blueprint/originality.py <chapter>` and rewrite any flagged prose.

**Reply with**, in this order:
- **Files written**, with prose word counts per section.
- **Labels created.**
- **Sidecars:** the scripts written, and confirmation that all pass.
- **Dependency ledger:** the number of ledger lines per section, and every line whose source is `chNN (promised)`, verbatim.
- **Promises opened:** each prose pointer, with file, line and target chapter.
- **Promises paid:** each promise from STATUS's table that you paid, with the paying label.
- **Blueprint deviations** and why, with a counterexample where the blueprint was wrong.
- **Gate results:** each tool's result on your files.
- **Claims you were unsure about**, with file and line.

## Building while other agents work

Several drafting agents may run at once, and **the scratchpad directory is shared between all of them**. Never build in the shared source tree (concurrent builds corrupt `_build/cache`), and never build in a generically named scratch folder such as `scratchpad/repo/`: in one chapter two agents used the same one and one `rsync --delete`d the other's copy. Copy the repo into a directory named after your own sections, for example `scratchpad/ch17-s05-s07/repo/`, and build there.
