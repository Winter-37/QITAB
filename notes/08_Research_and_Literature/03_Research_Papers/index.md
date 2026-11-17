Summaries of research papers, in the order DMET → gradients (DMET, selected CI) → SQD → DMET-SQD → quantum geometry optimization.

## What this chapter is about

One page per paper, written to the paper template:

- the problem the paper addresses;
- the method, in the notebook's notation;
- the key results and numbers;
- the limitations;
- links to the theory notes it relies on.

## Why the order

The papers are arranged so each builds on the previous ones:

1. **Practical DMET.** Implementation-level molecular DMET.
2. **Gradients.** The analytic gradient of multi-fragment DMET, and the analytic gradient of selected CI, where a truncated determinant list is not orbital-invariant.
3. **SQD.** Sample-based quantum diagonalization at scale on quantum hardware.
4. **DMET-SQD.** SQD as the fragment solver in DMET.
5. **Geometry optimization.** Co-optimizing geometry and circuit parameters in DMET-VQE.

## How to read it

**Core (first pass).** [[wouters-2016-practical-dmet]], [[li-2023-dmet-gradient]], [[coe-2023-sci-gradient]], [[robledo-moreno-2025-sqd]], [[shajan-2025-dmet-sqd]], [[hao-2026-dmet-vqe-geometry]].
