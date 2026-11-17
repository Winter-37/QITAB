Quantum circuits as a model of computation and communication: what cannot be done (copying), what entanglement makes possible (teleportation), and how measurement fits into circuits (Nielsen and Chuang, Chs. 1, 4 and 12).

## What this chapter is about

A quantum circuit is a sequence of gates on qubit wires, ending in computational-basis measurements, possibly with measurements partway through whose results control later gates. With the gates of Chapter 3 in hand, this chapter asks three questions about the model:

- **What is forbidden?** Unknown states cannot be copied (the no-cloning theorem).
- **What does entanglement enable?** One Bell pair and two classical bits move an unknown qubit (teleportation).
- **How are measurements handled?** Other bases, deferred and implicit measurement, and the Hadamard test.

## Why it matters

- **No-cloning shapes everything.** Results are extracted through repeated runs and statistics, error correction cannot use simple copies, and intermediate states cannot be inspected for free.
- **Teleportation is the template for using entanglement.** It moves states between processors, injects $T$ gates in fault-tolerant schemes, and underlies quantum networks.
- **Measurement is where the algorithm meets the data.** The Hadamard test is how a quantum computer estimates $\langle U\rangle$, overlaps and time-evolution signals. It is the primitive behind phase estimation and many energy-estimation schemes in Part 6.

## Where it is used later

- [[quantum-phase-estimation|Phase estimation]] (Chapter 5), which is the Hadamard test with many ancillas plus an inverse QFT.
- [[variational-quantum-eigensolver|VQE]] (Part 6), where Pauli strings are measured after basis rotations.
- Error correction (Chapter 6, planned), which needs no-cloning and information-free syndrome measurement.

## The main ideas, in order

1. **No-cloning.** Unitarity forces $\langle\psi|\varphi\rangle=\langle\psi|\varphi\rangle^2$, so only orthogonal states can be copied. Approximate cloning is possible, with optimal fidelity 5/6 for one qubit.
2. **Teleportation.** CNOT, $H$, a Bell measurement, two classical bits, and a Pauli correction. Nothing travels faster than light and nothing is copied.
3. **Measurement.** Changing basis before measuring, deferred measurement (classical control becomes quantum control), implicit measurement, and the Hadamard test for $\operatorname{Re}\langle U\rangle$ and $\operatorname{Im}\langle U\rangle$.

## How to read it

**Path.** [[no-cloning-theorem]], [[quantum-teleportation]], [[measurement-in-quantum-circuits]].

**Needs.** Chapter 3 ([[controlled-operations]]), Bell states from Chapter 2 ([[multi-qubit-states-and-bell-states]]), and measurement theory from Chapter 1 ([[projective-and-povm-measurements]]).

**Leads to.** Chapter 5 (algorithms) and Chapter 6 (error correction).

**Checkpoint.** Derive Bob's four conditional states in teleportation and the corrections $Z^{m_1}X^{m_2}$. Then show that the Hadamard test gives $P(0)=\tfrac12(1+\operatorname{Re}\langle U\rangle)$.

**Planned sections:** Dynamic circuits and feed-forward; Entanglement swapping.
