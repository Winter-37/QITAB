The qubit, registers of qubits, entanglement and mixed states (Nielsen and Chuang, Chs. 1–2).

## What this chapter is about

A qubit is a unit vector $\alpha|0\rangle+\beta|1\rangle$ in $\mathbb C^2$. Up to a global phase it is a point on the Bloch sphere. Registers of $n$ qubits live in a $2^n$-dimensional space, most of which consists of entangled states. This chapter covers:

- the single-qubit picture;
- two-qubit states and the Bell basis, with superdense coding as the first protocol that needs entanglement;
- the freedom in describing a mixed state by ensembles.

## Why it matters

- **The Bloch sphere is the working picture of single-qubit physics.** Gates are rotations, measurements are projections onto axes, and noise shrinks the vector into the ball.
- **Exponential state space.** $n$ qubits need $2^n$ amplitudes. This is the same growth that makes full CI expensive, and the reason a qubit register can hold a full-CI vector with one qubit per spin orbital.
- **Entanglement is the resource.** Bell pairs power superdense coding, teleportation and the CHSH violation. Entanglement between fragment and environment is what DMET's bath captures.
- **Mixed states have no preferred ensemble.** Different preparations with the same $\rho$ cannot be distinguished. This matters for interpreting reduced density matrices, noise and purifications.

## Where it is used later

- [[single-qubit-gates-and-rotations|Single-qubit gates]] and [[controlled-operations|controlled operations]] (Chapter 3).
- [[epr-and-bell-inequalities|Bell inequalities]] (Chapter 1).
- [[jordan-wigner-mapping|The Jordan–Wigner mapping]] (Part 6), where bit strings are determinants.
- [[schmidt-decomposition-and-dmet-bath|The DMET bath]] (Part 4, Chapter 19), an entanglement construction.

## The main ideas, in order

1. **One qubit.** Computational basis, Bloch parametrization, antipodal orthogonal states, the information content of a qubit, multi-qubit registers and the ordering convention.
2. **Two qubits.** Product versus entangled states, the Bell basis prepared by $H$ and CNOT, maximal entanglement, and superdense coding.
3. **Mixed states.** Theorem 2.6: two ensembles give the same $\rho$ if and only if they are related by a unitary. The Bloch ball and minimal ensembles.

## How to read it

**Path.** [[qubits-and-the-bloch-sphere]], [[multi-qubit-states-and-bell-states]], [[ensembles-and-unitary-freedom]].

**Needs.** Chapter 1 ([[quantum-postulates-for-information]]). Spin ½ (Part 2, Chapter 4). Tensor products and the Schmidt decomposition (Part 0, Chapter 10). Density operators (Part 2, Chapter 3).

**Leads to.** Chapter 3 (gates), and teleportation in Chapter 4.

**Checkpoint.** Derive $|\beta_{xy}\rangle=\mathrm{CNOT}(H\otimes I)|xy\rangle$. Then find the unitary relating $\{\tfrac34,|0\rangle;\tfrac14,|1\rangle\}$ to the equal mixture of $\sqrt{3/4}\,|0\rangle\pm\sqrt{1/4}\,|1\rangle$.

**Planned sections:** Entanglement measures; Multipartite entanglement (GHZ and W states).
