Treating a fragment of a molecule with a correlated method while its environment is described by a mean field. This chapter covers density matrix embedding theory (DMET) in its molecular, one-shot form, up to its analytic nuclear gradient.

## What this chapter is about

Accurate solvers (full CI, CCSD(T), DMRG, or a quantum computer) are limited to small orbital spaces. Real molecules are large. Embedding splits the problem: a small fragment that needs high accuracy, and an environment that only needs to be roughly right.

DMET makes the split with the Schmidt decomposition. For a mean-field (Slater-determinant) state of the whole molecule, a fragment of $n$ orbitals is entangled with at most $n$ environment orbitals, the bath. The rest of the environment is an unentangled core. The fragment plus its bath, with the core folded in as a frozen mean field, gives a small embedding Hamiltonian of at most $2n$ orbitals. A high-level solver treats it exactly. Fragment energies are then recombined, with a global chemical potential keeping the total electron count right.

## Why it matters

- **High-level accuracy where it is needed, at low cost.** The expensive solver only ever sees $2n$ orbitals. The total cost grows with the number of fragments, not exponentially with system size.
- **The bath is exact in a well-defined sense.** Built from the exact many-body state, the Schmidt decomposition would reproduce the exact fragment properties. In practice the bath comes from a mean-field state, and the error comes from that substitution. Self-consistency through a correlation potential reduces it.
- **Strong correlation in large systems.** DMET was designed for lattice models and bond breaking, where single-reference methods fail and full multireference treatment of the whole system is impossible.
- **A natural home for quantum solvers.** Present quantum hardware can treat active spaces of a few tens of orbitals at most, roughly the size of one embedding space. DMET with VQE or SQD solvers is one of the most direct ways to apply them to whole molecules.
- **Gradients make it a geometry tool.** The analytic gradient turns DMET from an energy method into one that can optimize structures and run dynamics. Its Lagrangian has terms for the solver, the bath construction and the mean-field orbitals.

## Where it is used later

- [[dmet-with-quantum-solvers|DMET with quantum solvers]] (Part 6, Chapter 7).
- [[hao-2026-dmet-vqe-geometry|DMET-VQE geometry optimization]] (paper note, Part 8).
- [[wouters-2016-practical-dmet|Wouters 2016]], [[shajan-2025-dmet-sqd|Shajan 2025]] and [[li-2023-dmet-gradient|Li 2023]] (paper notes, Part 8).

## The main ideas, in order

1. **The bath from the Schmidt decomposition.** For an idempotent 1-RDM, the fragment–environment block determines the bath orbitals and their singular values.
2. **The embedding Hamiltonian.** Project onto fragment plus bath, with the core contributing a frozen Coulomb–exchange potential.
3. **Energies from overlapping fragments.** Democratic partitioning, the two energy functionals, and the global chemical potential.
4. **Self-consistency.** A one-body correlation potential fitted to match 1-RDMs, and when one-shot DMET is enough.
5. **The analytic gradient.** A Lagrangian that removes all implicit dependences on the nuclear coordinates.

## How to read it

**Path.**

1. The Schmidt decomposition and the bath orbitals of a Slater determinant.
2. The embedding Hamiltonian: fragment plus bath, with the core as a frozen mean field, and Form B.
3. Combining fragments: democratic partitioning, two energy functionals, and the global chemical potential.
4. Self-consistency with a correlation potential, and when one-shot DMET is enough.
5. The analytic nuclear gradient as a Lagrangian.

**Needs.** Chapter 3 (RHF), Chapter 6 (density matrices and natural orbitals), Chapter 9 (FCI). Section 5 needs Chapter 15 (CPHF, Z-vector, CP-CI).

**Leads to.** Part 6, Chapter 7 (DMET with quantum solvers).

**Core (first pass).** [[schmidt-decomposition-and-dmet-bath]], [[dmet-embedding-hamiltonian]], [[dmet-energy-functionals-and-chemical-potential]].

**Deep (second pass).** [[dmet-self-consistency-and-correlation-potential]], [[dmet-analytic-nuclear-gradient]].

**Checkpoint.** For a two-atom fragment of an H$_6$ ring, show from $\gamma^2=\gamma$ that the bath singular values are $\sqrt{n(1-n)}$ and that the embedding space holds 4 electrons. Then explain why DMET with three-atom fragments reproduces FCI exactly.

**Planned sections:** Bootstrap embedding; Embedded wave function (EWF) and MP2 bath natural orbitals; DMFT; Projection-based wave-function-in-DFT embedding.
