---
id: qubit-ordering-conventions
title: Qubit-ordering conventions (Nielsen–Chuang versus Qiskit)
summary: Nielsen–Chuang writes |x₁x₂…xₙ⟩ with qubit 1 as the most significant bit and the leftmost tensor factor (big-endian); Qiskit numbers qubits from 0 and makes qubit 0 the least significant bit and the rightmost factor (little-endian). Consequences for basis-state indices, bitstring labels, Pauli-string labels and gate matrices, with the bit-reversal permutation that converts between them. All statements checked with Qiskit 2.6.
status: in-progress
kind: comparison
level: introductory
tags: [qubits, endianness, qiskit, conventions, tensor-products, comparison]
prerequisites: [multi-qubit-states-and-bell-states]
related: [controlled-operations, quantum-fourier-transform, pauli-matrix-identities, matrix-and-tensor-identities, jordan-wigner-mapping]
order: 40
date: 2026-11-17
---

A circuit diagram does not depend on any convention. Its state vector and its matrix do: they depend on which qubit is the **leftmost tensor factor** and which bit of the basis-state index belongs to which qubit.

## The two conventions

| | Nielsen–Chuang (big-endian) | Qiskit (little-endian) |
|---|---|---|
| qubit labels | $1,2,\dots,n$ | $0,1,\dots,n-1$ |
| basis ket | $|x_1x_2\cdots x_n\rangle = |x_1\rangle\otimes|x_2\rangle\otimes\cdots\otimes|x_n\rangle$ | $|q_{n-1}\cdots q_1q_0\rangle = |q_{n-1}\rangle\otimes\cdots\otimes|q_0\rangle$ |
| index of the basis state | $x = x_12^{n-1} + x_22^{n-2} + \cdots + x_n$ | $k = q_0 + 2q_1 + \cdots + 2^{n-1}q_{n-1}$ |
| bitstring as printed | $x_1x_2\cdots x_n$ (qubit 1 first) | $q_{n-1}\cdots q_1q_0$ (qubit 0 **last**) |
| operator $A\otimes B$ | $A$ on qubit 1, $B$ on qubit 2 | $A$ on qubit 1, $B$ on qubit 0 |
| Pauli label `"XZ"` | $X$ on qubit 1, $Z$ on qubit 2 | $X$ on qubit 1, $Z$ on qubit 0 |

In both, the printed bitstring is read as a binary number with the most significant bit on the left; they differ in **which qubit** that left bit belongs to.

## Consequences

**Basis states.** In Qiskit, $X$ on qubit 0 of a three-qubit register gives the state with index 1, printed `'001'`; $X$ on qubit 2 gives index 4, printed `'100'`.

**Gate matrices.** The Nielsen–Chuang CNOT (control on the first qubit) is

$$
\mathrm{CNOT}_{\text{NC}} = \begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix}.
$$

Qiskit's `cx(0, 1)` (control 0, target 1) has the matrix

$$
\begin{pmatrix}1&0&0&0\\0&0&0&1\\0&0&1&0\\0&1&0&0\end{pmatrix},
$$

and it is `cx(1, 0)` whose matrix equals $\mathrm{CNOT}_{\text{NC}}$. The physics is the same; the labels of the rows differ.

**Converting.** The two matrices of one circuit are related by the bit-reversal permutation $\pi$ that reverses the order of the $n$ bits of an index:

$$
U^{\text{Qiskit}}_{kl} = U^{\text{NC}}_{\pi(k)\pi(l)} .
$$

In Qiskit, `Operator(circuit.reverse_bits())` returns the Nielsen–Chuang (big-endian) matrix of `circuit`.

**Algorithms written in binary.** The quantum Fourier transform in Nielsen–Chuang uses $j = j_12^{n-1} + \cdots + j_n$ with qubit 1 holding $j_1$ ([[quantum-fourier-transform]]). Implemented in Qiskit with $j_1$ on qubit 0, the circuit produces the bit-reversed result unless the final swaps are adjusted; this is the usual source of "my QFT is reversed".

**Fermion-to-qubit mappings.** A mapping also fixes which spin orbital sits on which qubit (for example all $\alpha$ orbitals first, or $\alpha$ and $\beta$ interleaved), and the Jordan–Wigner $Z$ string runs over the qubits "before" the target in that order ([[jordan-wigner-mapping]]). The ordering used by a given library must be read from its documentation; it is independent of the endianness above but compounds with it.

!!! warning "Checklist when comparing a derivation with a library"
    1. Which qubit is the leftmost tensor factor?
    2. Is the printed bitstring big- or little-endian?
    3. In which order are spin orbitals assigned to qubits?
    Fix all three before comparing state vectors, unitaries or Pauli coefficients.

## Checks

`part9_reference.py`, section K (Qiskit 2.6.2): statevector index and label for $X$ on qubits 0 and 2; `Operator` of `cx(0,1)` and `cx(1,0)` against $\mathrm{CNOT}_{\text{NC}}$; `SparsePauliOp("XZ")` against `np.kron(X, Z)`; and a three-qubit circuit (H, CNOT, $R_y$, CNOT) whose big-endian matrix was built by hand from Kronecker products and compared with both `Operator(circuit.reverse_bits())` and the bit-reversal permutation of `Operator(circuit)`.

## Source

Nielsen and Chuang, *Quantum Computation and Quantum Information* (Cambridge University Press, 10th anniversary ed., 2010), Sec. 5.1, p. 218 (binary representation $j = j_12^{n-1} + \cdots + j_n2^0$); CNOT matrix as in [[controlled-operations]]. Qiskit's ordering from its behaviour in the checks above (Qiskit 2.6.2); it is also described in the Qiskit documentation.
