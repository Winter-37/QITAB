Using the quantum computer to propose determinants and a classical computer to diagonalize in their span.

## What this chapter is about

Sample-based quantum diagonalization (SQD) uses the quantum computer only for something classical computers find hard: generating a set of important determinants from a correlated wave function.

1. A circuit, usually LUCJ initialized from CCSD amplitudes, is run and measured many times.
2. Each measured bit string is a determinant (Chapter 2). Strings with the wrong electron number, caused by noise, are repaired by self-consistent configuration recovery.
3. The Hamiltonian is projected onto the span of the collected determinants. Spin closure makes the space suitable for an $\hat S^2$ eigenstate.
4. The projected Hamiltonian is diagonalized classically, as in selected CI.

## Why it matters

- **No energy measurement.** The energy comes from classical diagonalization, so the shot cost of measuring Pauli expectation values (the main weakness of VQE) disappears.
- **A variational upper bound.** The energy is an eigenvalue of $\hat H$ in a determinant subspace, so it bounds the full-CI energy from above, regardless of noise in the samples. Noise affects which determinants are found, not whether the bound holds.
- **It has scaled furthest on hardware.** SQD has been run with tens of qubits on IBM Heron processors, beyond the size where exact diagonalization is routine. Combined with DMET it has been applied to rings and to cyclohexane conformers.
- **It must be judged honestly.** The quantum sampler has to do better than cheap classical ways of choosing determinants, such as random sampling or CI selection heuristics. For small molecules even a random subspace can look good. Learning how to tell when the quantum samples add value is part of the method.

## Where it is used later

- [[dmet-with-quantum-solvers|DMET with SQD fragment solvers]] (Chapter 7).
- [[selected-ci-analytic-gradient|Selected-CI gradients]] (Part 4, Chapter 15), which apply to SQD because a fixed determinant list is not orbital-invariant.
- [[robledo-moreno-2025-sqd|Robledo-Moreno et al. 2025]] and [[shajan-2025-dmet-sqd|Shajan et al. 2025]] (Part 8).

## The main ideas, in order

1. **SQD.** Projection onto sampled determinants, spin closure, configuration recovery, and how to judge a sampler.
2. **The LUCJ circuit.** Products of orbital rotations and diagonal density–density operators, with parameters from CCSD. Locality restricts the density–density terms to qubits that are adjacent on the hardware, and this approximation has a cost.

## How to read it

**Path.**

1. Sample-based quantum diagonalization: projection, spin closure, configuration recovery, and how to judge a sampler.
2. The LUCJ circuit that supplies the samples, and what its locality approximation costs.

**Needs.** Chapter 2; Part 4, Chapter 9 (determinant strings, Davidson) and Chapter 11 (CCSD amplitudes).

**Leads to.** Chapter 7.

**Core (first pass).** [[sample-based-quantum-diagonalization]].

**Deep (second pass).** [[lucj-ansatz]].

**Checkpoint.** Explain why an SQD energy is an upper bound, and why a uniform-random subspace of a small molecule can look as good as a quantum one.

**Planned sections:** Quantum-selected CI (QSCI); Extended SQD (Ext-SQD); Orbital optimization in SQD.
