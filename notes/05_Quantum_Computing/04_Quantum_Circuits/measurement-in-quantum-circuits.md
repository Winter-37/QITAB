---
id: measurement-in-quantum-circuits
title: Measurement in quantum circuits - deferred and implicit measurement, other bases, and the Hadamard test
summary: Circuits measure only in the computational basis; any other projective measurement is a unitary change of basis followed by that measurement. A Bell measurement, for example, is CNOT then H. Two principles simplify circuits. Deferred measurement says mid-circuit measurements whose results control later gates can be moved to the end, with classical controls becoming quantum controls. Implicit measurement says unmeasured qubits may be taken as measured, since an unrecorded measurement of one qubit never changes another's reduced state. An observable that is both Hermitian and unitary is measured with an ancilla, H, controlled-U and H; this circuit is the Hadamard test. For a general unitary the test gives P(0) = (1 + Re⟨U⟩)/2, or (1 + Im⟨U⟩)/2 with an S† added. This is how overlaps, energies and phase estimation are read out. All verified numerically.
status: in-progress
kind: theory
level: intermediate
tags: [measurement, deferred-measurement, implicit-measurement, bell-measurement, hadamard-test, ancilla, mid-circuit-measurement, nielsen-chuang]
prerequisites: [projective-and-povm-measurements, controlled-operations]
related: [quantum-teleportation, quantum-phase-estimation, multi-qubit-states-and-bell-states, variational-quantum-eigensolver]
order: 30
date: 2026-11-17
---

## Overview

In the circuit model the only measurement is projective, on single qubits, in the computational basis, drawn as a meter. Everything else must be built from it. This note shows how to:

- measure in other bases, including the Bell basis;
- move measurements around a circuit without changing its output;
- measure an operator rather than a basis.

The last construction, the **Hadamard test**, is how a quantum computer estimates expectation values and overlaps, and how phase estimation extracts eigenvalues.

## Measuring in another basis

To measure in an orthonormal basis $\{|b_k\rangle\}$, apply the unitary $W$ that maps $|b_k\rangle\mapsto|k\rangle$, then measure in the computational basis. The POVM elements are $W^\dagger|k\rangle\langle k|W=|b_k\rangle\langle b_k|$.

- **Single qubit.** Measuring $X$ means applying $H$ then measuring. Measuring $Y$ means applying $S^\dagger$, then $H$, then measuring. This is how Pauli strings are measured in VQE: rotate each qubit into the $Z$ basis, then measure ([[variational-quantum-eigensolver]]).
- **Bell measurement (Exercise 4.33).** The Bell circuit is $H$ on qubit 1 followed by a CNOT, so its inverse, a CNOT then $H$ on qubit 1, maps $|\beta_{xy}\rangle\to|xy\rangle$. A computational measurement after it has POVM elements $|\beta_{xy}\rangle\langle\beta_{xy}|$ (verified). The measurement operators are $|xy\rangle\langle xy|\,(H\otimes I)\,\mathrm{CNOT}$, which leave the qubits in $|xy\rangle$ rather than in the Bell state.

## Two principles

**Deferred measurement.** Measurements in the middle of a circuit, whose results control later gates, can always be moved to the end. Each classically controlled gate is replaced by the same gate quantum-controlled on the unmeasured qubit. The output statistics are unchanged. Teleportation in deferred form is the standard example ([[quantum-teleportation]]).

The reason is that **measurement commutes with controls** (Exercise 4.35). Two orders give identical outcome probabilities and post-measurement states (verified for a random controlled-$U$):

- measure the control, then apply $U$ to the target if the result is 1;
- apply controlled-$U$, then measure the control.

Deferred measurement matters for proofs: every circuit becomes a single unitary followed by measurement. In practice, mid-circuit measurement with feed-forward can save qubits and gates on hardware that supports it.

**Implicit measurement.** Qubits left unmeasured at the end can be treated as if they were measured. If qubit 2 of $\rho$ is measured and the result discarded, the state becomes

$$
\rho'=P_0\rho P_0+P_1\rho P_1,\qquad P_m=I\otimes|m\rangle\langle m| ,
$$

and $\operatorname{tr}_2\rho'=\operatorname{tr}_2\rho$ (Exercise 4.32, verified). Measuring one subsystem never changes the statistics of another. This is the no-signalling property again.

**Measurement and irreversibility.** A measurement usually destroys quantum information. It need not when the outcome reveals nothing about the state, as in teleportation (uniformly random outcomes) and syndrome measurements in error correction. A measurement can be undone only if it carries no information about the state measured.

## Measuring an operator: the Hadamard test

Let $U$ be both Hermitian and unitary, so its eigenvalues are $\pm1$. Examples are a Pauli string and $\hat n\cdot\boldsymbol\sigma$. To measure $U$ as an observable (Exercise 4.34):

1. Start the ancilla in $|0\rangle$ and the system in $|\psi\rangle$.
2. Apply $H$ to the ancilla.
3. Apply controlled-$U$, with the ancilla as control.
4. Apply $H$ to the ancilla and measure it.

Writing $P_\pm=(I\pm U)/2$, the joint state before measurement is $|0\rangle P_+|\psi\rangle+|1\rangle P_-|\psi\rangle$. Outcome 0 occurs with probability $\langle\psi|P_+|\psi\rangle$ and leaves the system in the $+1$ eigenspace. This is a projective measurement of $U$ made through phase kickback, without diagonalizing $U$. Verified for $U=\hat n\cdot\boldsymbol\sigma$ with a random axis.

**General unitaries.** The same circuit works for any unitary $U$, not necessarily Hermitian. It then estimates the expectation value rather than projecting:

$$
P(0)=\tfrac12\big(1+\operatorname{Re}\langle\psi|U|\psi\rangle\big),
$$

and with $S^\dagger$ on the ancilla before the last Hadamard,

$$
P(0)=\tfrac12\big(1+\operatorname{Im}\langle\psi|U|\psi\rangle\big).
$$

Verified for random $4\times4$ unitaries. The general form is my addition, a standard construction not stated in Nielsen and Chuang. Uses:

- **Overlaps and matrix elements.** With $U$ the circuit that prepares one state from another, the test gives overlaps. Quantum subspace methods and non-orthogonal VQE use it to build Hamiltonian and overlap matrices.
- **Time evolution.** With $U=e^{-iHt}$, it measures $\langle e^{-iHt}\rangle$, the signal from which energies are extracted in single-ancilla phase-estimation variants.
- **Phase estimation.** Phase estimation is the Hadamard test run with many ancillas and powers $U^{2^j}$, followed by an inverse QFT ([[quantum-phase-estimation]]).

## Source

Nielsen and Chuang, *Quantum Computation and Quantum Information* (10th anniversary ed., Cambridge University Press, 2010), Sec. 4.4, pp. 185–188:

- the measurement symbol, Figure 4.14;
- the principle of deferred measurement and Figure 4.15;
- the principle of implicit measurement;
- the remark on irreversibility;
- Exercises 4.32–4.35, Eq. (4.40).

Exercise 5.9 (p. 225) connects Exercise 4.34 to phase estimation. Page numbers are those printed in the book. All checks are in `nielsen_chuang/part5_batch7.py` (section C).
