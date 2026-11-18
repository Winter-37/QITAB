---
id: reading-order-quantum-computing
title: Reading order - quantum computing and quantum computational chemistry
summary: A staged path from the postulates of quantum information through gates, circuits and phase estimation (Part 5, Nielsen–Chuang) to the molecular Hamiltonian on qubits, VQE, QPE and sample-based quantum diagonalization (Part 6), with the mathematics, quantum mechanics and electronic-structure notes each stage needs.
status: in-progress
kind: reference
level: introductory
tags: [reading-guide, study-plan, quantum-computing, quantum-chemistry, curriculum, overview]
prerequisites: []
related: [reading-order-quantum-mechanics, reading-order-electronic-structure, qubit-ordering-conventions, pauli-matrix-identities]
order: 30
date: 2026-11-17
---

## How to use this guide

Part 5 (quantum computing) is written from Nielsen–Chuang and assumes only linear algebra and the basic quantum mechanics of Part 2. Part 6 (quantum computational chemistry) puts the electronic-structure problem of Part 4 on a quantum computer and needs both. Stages 1-4 cover Part 5 and stages 5-8 cover Part 6. The chapters of Part 5 numbered 6-11 and several chapters of Part 6 are still planned; the guide covers what exists.

**Conventions.** Qubit order differs between Nielsen–Chuang and Qiskit ([[qubit-ordering-conventions]]); Pauli algebra is collected in [[pauli-matrix-identities]].

## Stage 1 - Linear algebra and quantum mechanics for qubits

**Mathematics.** [[dirac-notation]], [[spectral-decomposition-and-normal-operators]], [[polar-and-singular-value-decompositions]], [[tensor-products-and-partial-trace]], [[schmidt-decomposition-and-purification]].

**Quantum mechanics.** [[spin-one-half]], [[density-operators-and-mixed-states]], [[two-level-systems-and-rabi-oscillations]].

**Checkpoint.** Compute the reduced density matrix of one qubit of a Bell state, and its Schmidt coefficients.

## Stage 2 - Postulates, qubits and measurement

1. [[quantum-postulates-for-information]] - the postulates in the form used for information processing.
2. [[qubits-and-the-bloch-sphere]] and [[multi-qubit-states-and-bell-states]] - single and multiple qubits, entanglement.
3. [[projective-and-povm-measurements]] - measurement beyond projectors.
4. [[ensembles-and-unitary-freedom]] - when two ensembles give the same density operator.
5. [[epr-and-bell-inequalities]] - what entanglement rules out.

**Checkpoint.** Show that a POVM element need not be a projector, and give one for unambiguous discrimination of two non-orthogonal states.

## Stage 3 - Gates and circuits

1. [[single-qubit-gates-and-rotations]] - rotations, Euler decomposition.
2. [[controlled-operations]] - CNOT, controlled-$U$, Toffoli.
3. [[universal-gate-sets]] - why a finite gate set suffices.
4. [[no-cloning-theorem]], [[quantum-teleportation]], [[measurement-in-quantum-circuits]] - what circuits can and cannot do, and deferred measurement.

**Checkpoint.** Write the CNOT matrix in Nielsen–Chuang order and in Qiskit order, and the permutation that relates them.

## Stage 4 - Algorithms

**Mathematics.** The discrete Fourier transform in [[fourier-transforms-and-the-dirac-delta]].

1. [[deutsch-jozsa-and-quantum-parallelism]] - interference as a resource.
2. [[quantum-fourier-transform]] - the circuit and its cost.
3. [[quantum-phase-estimation]] - the subroutine behind every exact quantum energy algorithm.
4. [[simulation-of-quantum-systems]] - Trotterization of $e^{-i\hat Ht}$.

**Checkpoint.** Show the success probability of phase estimation for a phase that is not an exact $t$-bit fraction.

## Stage 5 - The molecular Hamiltonian on qubits

**Electronic structure first.** [[second-quantization-in-a-finite-basis]], [[creation-and-annihilation-operators]], [[second-quantized-operators]], [[integral-notation]], [[full-ci]] (Part 4, chapters 2, 5 and 9).

1. [[molecular-hamiltonian-in-the-mo-basis]] and [[frozen-core-and-active-space-hamiltonians]] - the fermionic Hamiltonian that will be mapped.
2. [[jordan-wigner-mapping]], [[parity-and-bravyi-kitaev-mappings]], [[qubit-tapering]] - from fermions to Pauli strings, and how symmetries remove qubits.

**Checkpoint.** Map minimal-basis H₂ to qubits with Jordan–Wigner and recover the FCI energy by diagonalizing the qubit Hamiltonian.

## Stage 6 - Variational algorithms

**Mathematics.** [[probability-and-random-variables]], [[concentration-inequalities-and-sampling]] (shot counts).

1. [[variational-quantum-eigensolver]] and [[vqe-ansatze]] - the hybrid loop and the choice of circuit.
2. [[pauli-measurement-and-grouping]] - how many measurements an energy costs.
3. [[adapt-vqe]] - growing the ansatz operator by operator.
4. [[error-mitigation-for-vqe]] - extracting usable energies from noisy hardware.

**Electronic structure alongside.** [[variational-and-unitary-coupled-cluster]] (Part 4, Ch. 12) for the UCC ansatz.

**Checkpoint.** Estimate the number of shots for a 1 m$E_h$ standard error from the Pauli coefficients of H₂.

## Stage 7 - Phase estimation for molecules

1. [[qpe-for-molecular-energies]] and [[iterative-phase-estimation]].
2. [[qpe-state-preparation-and-overlap]] - why the initial state decides the success probability.
3. [[trotter-error-in-qpe-energies]] and [[qpe-cost-and-resource-estimates]] - what it costs to reach chemical accuracy.

**Checkpoint.** Relate the probability of obtaining the ground-state energy to the overlap of the input state with the ground state.

## Stage 8 - Sample-based methods and embedding

**Electronic structure first.** [[ci-in-practice]], [[determinant-strings-and-direct-ci]] (selected determinant spaces), and Part 4, Ch. 19 for embedding.

1. [[sample-based-quantum-diagonalization]] and [[lucj-ansatz]] - sampling determinants on hardware and diagonalizing classically.
2. [[dmet-with-quantum-solvers]] - quantum solvers inside an embedding.

**Checkpoint.** Show, from the linear variation method ([[linear-variation-method]]), that diagonalizing $\hat H$ in any sampled set of determinants gives an upper bound to the full-CI energy of the same active space.

## Source

Organizes the notebook's own notes. Part 5 is built on Nielsen and Chuang, *Quantum Computation and Quantum Information* (10th anniversary ed., Cambridge University Press, 2010); Part 6 on the reviews and papers cited in each note.
