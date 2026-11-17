---
id: multi-qubit-states-and-bell-states
title: Two-qubit states, the Bell basis and superdense coding
summary: Product versus entangled two-qubit states, and the four Bell states |β_xy⟩ = (|0,y⟩ + (−1)^x |1,ȳ⟩)/√2, prepared from |xy⟩ by a Hadamard on qubit 1 followed by a CNOT. The Bell states form an orthonormal basis. Each is maximally entangled: Schmidt rank 2, reduced state I/2, and the same value of ⟨E⊗I⟩ for every local operator E. Superdense coding sends two classical bits by transmitting one qubit of a shared Bell pair. Alice applies Z^{b₁}X^{b₂}, and Bob undoes the Bell circuit to read |b₁b₂⟩. The note also records how Nielsen-Chuang's bit labels in Section 2.3 relate to the β labels.
status: in-progress
kind: theory
level: introductory
tags: [bell-states, entanglement, epr-pair, superdense-coding, product-state, cnot, hadamard, nielsen-chuang]
prerequisites: [qubits-and-the-bloch-sphere, tensor-products-and-partial-trace]
related: [schmidt-decomposition-and-purification, epr-and-bell-inequalities, controlled-operations, quantum-postulates-for-information]
order: 20
date: 2026-11-17
---

## Overview

Two qubits are the smallest system that shows entanglement. The four Bell states form an orthonormal basis of maximally entangled states. They are the resource behind superdense coding, teleportation and Bell-inequality violation. This note defines them, shows how a two-gate circuit prepares them, and works out superdense coding as the first protocol in which entanglement does something classical correlations cannot.

## Product and entangled states

Write a two-qubit state as $|\psi\rangle=\sum_{ij}c_{ij}|ij\rangle$. It is a **product** $|a\rangle|b\rangle$ if and only if the $2\times2$ matrix $c$ has rank 1, that is, Schmidt rank 1 ([[schmidt-decomposition-and-purification]]). Otherwise it is **entangled**. For $(|00\rangle+|11\rangle)/\sqrt2$, $c=I/\sqrt2$ has rank 2, so no single-qubit states $|a\rangle,|b\rangle$ reproduce it (N&C Exercise 2.68).

## The Bell states

Apply a Hadamard to qubit 1 and then a CNOT with qubit 1 as control ([[controlled-operations]]). Starting from the four computational basis states gives

$$
|\beta_{xy}\rangle=\mathrm{CNOT}\,(H\otimes I)\,|xy\rangle=\frac{|0,y\rangle+(-1)^x|1,\bar y\rangle}{\sqrt2},
$$

with $\bar y=1-y$:

| input | output |
|---|---|
| $\lvert00\rangle$ | $\lvert\beta_{00}\rangle=(\lvert00\rangle+\lvert11\rangle)/\sqrt2$ |
| $\lvert01\rangle$ | $\lvert\beta_{01}\rangle=(\lvert01\rangle+\lvert10\rangle)/\sqrt2$ |
| $\lvert10\rangle$ | $\lvert\beta_{10}\rangle=(\lvert00\rangle-\lvert11\rangle)/\sqrt2$ |
| $\lvert11\rangle$ | $\lvert\beta_{11}\rangle=(\lvert01\rangle-\lvert10\rangle)/\sqrt2$ |

The circuit is unitary, so the Bell states are orthonormal (N&C Exercise 2.69). Running the circuit backwards (CNOT, then $H$ on qubit 1) maps $|\beta_{xy}\rangle\to|xy\rangle$, and a computational-basis measurement after it is a **Bell measurement**. $|\beta_{11}\rangle$ is the spin singlet; the other three span the triplet ([[addition-of-angular-momenta]]).

**Maximal entanglement.** For every Bell state, the reduced state of either qubit is $I/2$, the centre of the Bloch ball. Consequently, for every operator $E$ acting on qubit 1 alone,

$$
\langle\beta_{xy}|E\otimes I|\beta_{xy}\rangle=\tfrac12\operatorname{tr}E ,
$$

independent of $x$ and $y$ (N&C Exercise 2.70). Nothing measured on one qubit distinguishes the four Bell states. The information is stored entirely in the correlations.

**Correlations.** Measuring both qubits of $|\beta_{00}\rangle$ in the computational basis gives 00 or 11 with probability $\tfrac12$ each: the results always agree. The same holds after both qubits are rotated by suitable local unitaries. The singlet is anticorrelated along every axis ([[epr-and-bell-inequalities]]).

## Superdense coding

Alice and Bob share $|\beta_{00}\rangle$, Alice holding qubit 1. To send two classical bits $b_1b_2$, Alice applies $Z^{b_1}X^{b_2}$ to her qubit alone and sends it to Bob:

$$
(Z^{b_1}X^{b_2}\otimes I)\,|\beta_{00}\rangle=|\beta_{b_1b_2}\rangle .
$$

That is, $I\to|\beta_{00}\rangle$, $X\to|\beta_{01}\rangle$, $Z\to|\beta_{10}\rangle$ and $ZX=iY\to|\beta_{11}\rangle$. Bob now holds both qubits. He applies the inverse Bell circuit and measures, which returns $|b_1b_2\rangle$ with certainty (verified for all four messages).

One transmitted qubit has carried two bits. Two caveats:

- The second qubit was delivered beforehand, so the protocol trades prior entanglement for communication. Without it, one qubit carries at most one bit (Holevo).
- An eavesdropper who intercepts Alice's qubit learns nothing. By the result above, every measurement on that qubit alone has the same statistics for all four messages.

**Labelling note.** Nielsen and Chuang list Alice's encodings as $00\to I$, $01\to Z$, $10\to X$, $11\to iY$ (Eqs. 2.134–2.137). Their labels are the $\beta$ labels with the two bits swapped: their message 01 produces $|\beta_{10}\rangle$. Both labellings work as long as Bob decodes consistently. The form $Z^{b_1}X^{b_2}$ used here makes Bob's output equal $|b_1b_2\rangle$ directly.

## Why it matters later

- **Teleportation** (planned, [[quantum-teleportation]]) runs superdense coding backwards: one shared Bell pair plus two classical bits transmits one qubit.
- **Two-qubit gate benchmarks.** Preparing $|\beta_{00}\rangle$ and measuring its fidelity is a standard hardware test.
- **Chemistry analogue.** The two-electron singlet of minimal-basis H₂ at dissociation is a Bell-like state of two spatial orbitals. Its entanglement is the static correlation that defeats RHF ([[h2-dissociation-rhf-uhf]]).

## Source

Nielsen and Chuang, *Quantum Computation and Quantum Information* (10th anniversary ed., Cambridge University Press, 2010):

- Sec. 1.2.1, pp. 16–17: the Bell state (1.7) and its correlations.
- Sec. 1.3.6, pp. 25–26: Bell states, Eqs. (1.23)–(1.27), and the circuit of Figure 1.12.
- Sec. 2.2.8, pp. 95–96: entanglement, Eq. (2.132); Exercise 2.68.
- Sec. 2.3, pp. 97–98: superdense coding, Eqs. (2.134)–(2.137); Exercises 2.69–2.70.

Page numbers are those printed in the book. The circuit identities, the decoding check and the labelling comparison are in `nielsen_chuang/part5_batch6.py` (section E).
