Quantum solvers inside DMET, for energies and for geometries.

## What this chapter is about

DMET (Part 4, Chapter 19) replaces one large correlated problem by several fragment-plus-bath problems. For a fragment of $n$ spatial orbitals the embedding space has at most $2n$ orbitals, and with Jordan–Wigner $4n$ qubits. This chapter treats the quantum computer as the high-level solver for those problems:

- why the fragment problems match the size of current devices;
- what changes when the solver is noisy and sample-based instead of exact;
- how DMET-SQD has been run on hardware;
- two published routes to geometry optimization:
  - nested loops, converging the solver at every geometry;
  - co-optimization of nuclear coordinates and circuit parameters together.

## Why it matters

- **It is the most direct way to apply quantum solvers to whole molecules.** No current device can treat a full molecule of chemical interest at a useful basis size. Embedding reduces the qubit count to that of one fragment.
- **Noise interacts with the embedding.** The chemical-potential fit and any self-consistency loop use the solver's 1-RDM. Statistical noise in that density propagates into the total energy, and into gradients for geometry optimization.
- **Geometries need forces.** Geometry optimization with a quantum solver needs gradients of the embedded energy. Those inherit every implicit dependence of the classical DMET gradient, plus whatever the solver adds.

## Where it is used later

- [[shajan-2025-dmet-sqd|Shajan et al. 2025]] (DMET-SQD on hardware) and [[hao-2026-dmet-vqe-geometry|Hao et al. 2026]] (DMET-VQE geometry optimization), in Part 8.
- [[dmet-analytic-nuclear-gradient|The classical DMET gradient]] (Part 4, Chapter 19), which a quantum-solver gradient must extend.

## How to read it

**Path.** Why fragment problems suit near-term devices; DMET-SQD on hardware; two routes to geometry optimization (nested loops, co-optimization).

**Needs.** Part 4, Chapter 19; Chapters 3 and 5.

**Core (first pass).** [[dmet-with-quantum-solvers]].

**Planned sections:** DMET-VQE; Embedding with Ext-SQD for excited states.
