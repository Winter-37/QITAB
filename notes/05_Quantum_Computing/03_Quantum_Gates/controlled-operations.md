---
id: controlled-operations
title: Controlled operations - CNOT, controlled-U, the Toffoli gate and qubit ordering
summary: The CNOT gate |c,t⟩ → |c, t⊕c⟩ is |0⟩⟨0|⊗I + |1⟩⟨1|⊗X. Covers CZ = (I⊗H)CNOT(I⊗H), which is symmetric in its two qubits; phase kickback, where in the ± basis the roles of control and target exchange; and SWAP as three CNOTs. Any controlled-U needs two CNOTs plus single-qubit gates, via U = e^{iα}AXBXC with ABC = I and a phase on the control. A doubly controlled C²(U) needs controlled-V gates with V² = U. The Toffoli gate is built exactly from 6 CNOTs, 7 T/T† gates and 2 Hadamards. CNOT conjugation rules for Pauli operators are given, and the matrix of a gate depends on the qubit-ordering convention (Nielsen-Chuang versus Qiskit). Every circuit identity is verified numerically.
status: in-progress
kind: theory
level: intermediate
tags: [cnot, controlled-u, controlled-z, toffoli, swap, phase-kickback, clifford, qubit-ordering, circuit-identities, nielsen-chuang]
prerequisites: [single-qubit-gates-and-rotations, multi-qubit-states-and-bell-states]
related: [universal-gate-sets, jordan-wigner-mapping, lucj-ansatz, qubits-and-the-bloch-sphere]
order: 20
date: 2026-11-17
---

## Overview

Single-qubit gates cannot create entanglement, so a quantum computer needs at least one two-qubit gate. The standard choice is the controlled-NOT: "if the control is 1, flip the target." This note shows how every controlled operation, including the three-qubit Toffoli gate, is assembled from CNOTs and single-qubit gates. It also gives the circuit identities used to simplify circuits. These constructions are the building blocks of every chemistry circuit in Part 6. For example, exponentials of Jordan–Wigner Pauli strings are built from CNOT ladders.

**Convention.** $|c\,t\rangle=|c\rangle\otimes|t\rangle$, with the first qubit the most significant bit ([[qubits-and-the-bloch-sphere]]). $P_0=|0\rangle\langle0|$ and $P_1=|1\rangle\langle1|$.

## CNOT and its relatives

$$
\mathrm{CNOT}\,|c,t\rangle=|c,\,t\oplus c\rangle,\qquad
\mathrm{CNOT}=P_0\otimes I+P_1\otimes X=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix}.
$$

- **Controlled-$U$** in general is $C(U)=P_0\otimes I+P_1\otimes U$.
- **Controlled-$Z$.** $\mathrm{CZ}=\mathrm{diag}(1,1,1,-1)=(I\otimes H)\,\mathrm{CNOT}\,(I\otimes H)$ (Exercise 4.17). CZ is symmetric under exchanging its two qubits: "control" and "target" are labels, not physics.
- **Phase kickback (Exercise 4.20).** $(H\otimes H)\,\mathrm{CNOT}\,(H\otimes H)$ is the CNOT with control and target exchanged. In the $\pm$ basis,

$$
|{+}{+}\rangle\to|{+}{+}\rangle,\quad|{-}{+}\rangle\to|{-}{+}\rangle,\quad|{+}{-}\rangle\to|{-}{-}\rangle,\quad|{-}{-}\rangle\to|{+}{-}\rangle .
$$

The target is unchanged and the control flips when the target is $|-\rangle$. This is how phase estimation and the Deutsch–Jozsa algorithm read information out through the control register.
- **SWAP = three CNOTs** with alternating direction (Eq. 1.20): $|a,b\rangle\to|a,a\oplus b\rangle\to|b,a\oplus b\rangle\to|b,a\rangle$.
- **Controlled global phase.** $C(e^{i\alpha}I)=\mathrm{diag}(1,e^{i\alpha})\otimes I$, a phase gate on the control alone (Eq. 4.28). A global phase of $U$ becomes a relative phase once $U$ is controlled.

## Controlled-U from two CNOTs

Write $U=e^{i\alpha}AXBXC$ with $ABC=I$ ([[single-qubit-gates-and-rotations]]). Then the circuit

1. $C$ on the target,
2. CNOT,
3. $B$ on the target,
4. CNOT,
5. $A$ on the target,
6. $\mathrm{diag}(1,e^{i\alpha})$ on the control,

equals $C(U)$ (N&C Figure 4.6). If the control is 0, the target sees $ABC=I$. If the control is 1, it sees $AXBXC=e^{-i\alpha}U$, and the phase gate restores $e^{i\alpha}$. Verified for 10 random $U$. So **every controlled single-qubit gate costs two CNOTs**.

## Two controls: C²(U) and the Toffoli gate

$C^2(U)$ applies $U$ to qubit 3 only if qubits 1 and 2 are both 1. Choose $V$ with $V^2=U$. The sequence

1. $C(V)$ from qubit 2 to qubit 3,
2. CNOT from qubit 1 to qubit 2,
3. $C(V^\dagger)$ from qubit 2 to qubit 3,
4. CNOT from qubit 1 to qubit 2,
5. $C(V)$ from qubit 1 to qubit 3,

implements $C^2(U)$ (Figure 4.8). Count the net power of $V$ on qubit 3 for each control pattern:

| control pattern | net power |
|---|---|
| 11 | $V\cdot V=U$ |
| 10 | $VV^\dagger=I$ |
| 01 | $V^\dagger V=I$ |
| 00 | nothing |

Verified for a random $U$ and for the **Toffoli** gate ($U=X$, $V=(1-i)(I+iX)/2$, which satisfies $V^2=X$).

**Toffoli from Clifford+T.** Label the qubits $a,b$ (controls) and $c$ (target), and apply in order:

$$
H_c,\ \mathrm{CX}_{bc},\ T_c^\dagger,\ \mathrm{CX}_{ac},\ T_c,\ \mathrm{CX}_{bc},\ T_c^\dagger,\ \mathrm{CX}_{ac},\ T_b,\ T_c,\ H_c,\ \mathrm{CX}_{ab},\ T_a,\ T_b^\dagger,\ \mathrm{CX}_{ab}.
$$

This equals the Toffoli exactly, with no global phase, using 6 CNOTs, 7 $T$-type gates and 2 Hadamards. Nielsen and Chuang give a circuit of the same composition (Figure 4.9, Exercise 4.24); the sequence above was checked numerically rather than read off their figure.

The Toffoli is universal for reversible classical computation, so quantum circuits contain classical circuits. Unlike the classical case, one- and two-qubit gates suffice to build it. With more controls, $C^n(U)$ uses a ladder of Toffolis into $n-1$ work qubits, giving $O(n)$ gates (Figure 4.10).

## Pauli propagation through CNOT

With $C$ the CNOT (qubit 1 control) and subscripts for qubits (Exercise 4.31):

$$
CX_1C=X_1X_2,\quad CY_1C=Y_1X_2,\quad CZ_1C=Z_1,\quad CX_2C=X_2,\quad CY_2C=Z_1Y_2,\quad CZ_2C=Z_1Z_2 .
$$

$X$ errors spread from control to target, and $Z$ errors spread from target to control. CNOT maps Pauli strings to Pauli strings, so it is a **Clifford** gate. These rules underlie stabilizer error correction and the "CNOT ladder" used to exponentiate a Pauli string: $e^{-i\theta Z_1Z_2\cdots Z_k/2}$ is a ladder of CNOTs onto the last qubit, $R_z(\theta)$ there, and the ladder reversed. This is how Jordan–Wigner terms are implemented in VQE circuits ([[jordan-wigner-mapping]]). Also, $R_z$ on the control and $R_x$ on the target commute with CNOT (Eqs. 4.38–4.39).

## Qubit ordering

A circuit diagram is convention-free, but its matrix is not. In the Nielsen–Chuang order the CNOT with control on the first qubit is the matrix above. In Qiskit's little-endian order, a CNOT with control on qubit 0 and target on qubit 1 has the matrix of the *reversed* CNOT, $\begin{pmatrix}1&0&0&0\\0&0&0&1\\0&0&1&0\\0&1&0&0\end{pmatrix}$ (checked). When comparing statevectors or unitaries between a library and a derivation, fix the convention first. The Qiskit statement is from general knowledge of the library, not from the book.

## Source

Nielsen and Chuang, *Quantum Computation and Quantum Information* (10th anniversary ed., Cambridge University Press, 2010):

- Sec. 1.3.2, pp. 20–22: CNOT and Eq. (1.18).
- Sec. 1.3.4, p. 23: SWAP from three CNOTs, Eq. (1.20).
- Sec. 4.3, pp. 177–185:
  - Eqs. (4.23)–(4.39) and Figures 4.3–4.13;
  - Exercises 4.16–4.31, of which 4.17, 4.20, 4.21, 4.24 and 4.31 are verified here.

Page numbers are those printed in the book. All identities and both Toffoli constructions are checked in `nielsen_chuang/part5_batch6.py` (section H).
