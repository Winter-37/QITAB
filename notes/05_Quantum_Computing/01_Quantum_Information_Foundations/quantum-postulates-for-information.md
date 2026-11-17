---
id: quantum-postulates-for-information
title: The postulates of quantum mechanics in quantum-information form
summary: The four postulates as Nielsen and Chuang state them. A closed system is a unit vector in a Hilbert space. It evolves unitarily, U = exp(−iHt/ħ). Measurement is described by operators M_m with Σ M_m†M_m = I, outcome probability ⟨ψ|M_m†M_m|ψ⟩ and post-measurement state M_m|ψ⟩/√p(m). Composite systems live in the tensor product. Shows that a general measurement is a unitary on system plus ancilla followed by a projective measurement of the ancilla (checked numerically), that global phases are unobservable and relative phases are not, and gives the density-operator form of all four postulates.
status: in-progress
kind: theory
level: introductory
tags: [postulates, measurement-operators, unitary-evolution, composite-systems, tensor-product, global-phase, relative-phase, ancilla, entanglement, nielsen-chuang]
prerequisites: [hilbert-space-and-hermitian-operators, generalized-statistical-interpretation, tensor-products-and-partial-trace]
related: [projective-and-povm-measurements, density-operators-and-mixed-states, multi-qubit-states-and-bell-states, heisenberg-picture-and-time-translation, unitary-matrices-exponential-logarithm]
order: 10
date: 2026-11-17
---

## Overview

Part 2 states quantum mechanics in the language of wave functions and observables. Quantum information uses the same theory in a form tuned to finite-dimensional systems, controlled operations and general measurements. Nielsen and Chuang reduce it to four postulates. This note states them, proves the two facts that make them usable (measurement through an ancilla and the irrelevance of global phase), and gives the density-operator version that the rest of Part 5 uses.

**Notation.** $|0\rangle,|1\rangle$ are a fixed orthonormal basis of one qubit (the *computational basis*). $\hbar=1$ unless stated. Operators on different subsystems carry subscripts, $X_2$ meaning $X$ on qubit 2.

## The four postulates

**Postulate 1 (state space).** An isolated system is associated with a Hilbert space. Its state is a unit vector $|\psi\rangle$ in that space. For a qubit, $|\psi\rangle=a|0\rangle+b|1\rangle$ with $|a|^2+|b|^2=1$.

**Postulate 2 (evolution).** A closed system evolves by a unitary operator that depends only on the initial and final times, $|\psi'\rangle=U|\psi\rangle$. In continuous time this is the Schrödinger equation $i\hbar\,d|\psi\rangle/dt=H|\psi\rangle$ with a Hermitian Hamiltonian $H$, whose solution for constant $H$ is

$$
U(t_1,t_2)=\exp\!\big[-iH(t_2-t_1)/\hbar\big].
$$

Conversely, every unitary is $U=e^{iK}$ for a Hermitian $K=-i\log U$ (by the spectral theorem, [[spectral-decomposition-and-normal-operators]]). Discrete-time unitaries and Hamiltonians are therefore two descriptions of the same dynamics. Example: $H=\omega X$ has eigenstates $|\pm\rangle=(|0\rangle\pm|1\rangle)/\sqrt2$ with energies $\pm\omega$, so the ground state is $|-\rangle$.

**Postulate 3 (measurement).** A measurement is a set of operators $\{M_m\}$, one per outcome $m$, satisfying the completeness relation

$$
\sum_m M_m^\dagger M_m=I .
$$

On the state $|\psi\rangle$, outcome $m$ occurs with probability and leaves the state

$$
p(m)=\langle\psi|M_m^\dagger M_m|\psi\rangle ,\qquad
|\psi\rangle\ \longmapsto\ \frac{M_m|\psi\rangle}{\sqrt{p(m)}} .
$$

Completeness for all $|\psi\rangle$ is equivalent to $\sum_mp(m)=1$. Measuring a qubit in the computational basis uses $M_0=|0\rangle\langle0|$, $M_1=|1\rangle\langle1|$, which gives $p(0)=|a|^2$ and post-measurement state $(a/|a|)|0\rangle$.

**Postulate 4 (composite systems).** The state space of a composite system is the tensor product of the component spaces. If system $i$ is prepared in $|\psi_i\rangle$, the joint state is $|\psi_1\rangle\otimes\cdots\otimes|\psi_n\rangle$. A state that cannot be written as such a product is **entangled**. The standard example is $(|00\rangle+|11\rangle)/\sqrt2$, whose coefficient matrix has rank 2 ([[schmidt-decomposition-and-purification]]).

## General measurement from unitary evolution plus a projective measurement

Postulate 3 looks more general than the projective measurements of Part 2. It is not more powerful once ancillas are allowed. Let the system $Q$ have measurement operators $M_m$, and attach an ancilla $M$ with an orthonormal basis $|m\rangle$, one state per outcome, prepared in $|0\rangle$. Define

$$
U\,|\psi\rangle|0\rangle\equiv\sum_mM_m|\psi\rangle|m\rangle .
$$

Completeness makes this inner-product preserving,
$\langle\varphi|\langle0|U^\dagger U|\psi\rangle|0\rangle=\sum_m\langle\varphi|M_m^\dagger M_m|\psi\rangle=\langle\varphi|\psi\rangle$, so it extends to a unitary on $Q\otimes M$ (N&C Exercise 2.67). Now measure the ancilla projectively with $P_m=I_Q\otimes|m\rangle\langle m|$:

$$
p(m)=\langle\psi|\langle0|U^\dagger P_mU|\psi\rangle|0\rangle=\langle\psi|M_m^\dagger M_m|\psi\rangle ,
\qquad
\text{state of }Q\ \text{afterwards}=\frac{M_m|\psi\rangle}{\sqrt{p(m)}} .
$$

Unitary dynamics, projective measurement and an ancilla therefore reproduce any measurement of Postulate 3.

!!! example "Numerical check"
    Three random $2\times2$ operators $A_m$ were made complete by $M_m=A_m\big(\sum_kA_k^\dagger A_k\big)^{-1/2}$. The isometry above satisfies $V^\dagger V=I$ to machine precision. For a random qubit state, the ancilla probabilities equal $\langle\psi|M_m^\dagger M_m|\psi\rangle$ for all three outcomes, and the conditional states of $Q$ equal $M_m|\psi\rangle/\sqrt{p(m)}$.

**Cascaded measurements.** A measurement $\{L_l\}$ followed by $\{M_m\}$ is a single measurement with operators $N_{lm}=M_mL_l$, which are again complete (N&C Exercise 2.57). Sequences of measurements need no new postulate.

## Global and relative phase

For any $\theta$, the states $e^{i\theta}|\psi\rangle$ and $|\psi\rangle$ give identical statistics, since $\langle\psi|e^{-i\theta}M_m^\dagger M_me^{i\theta}|\psi\rangle=\langle\psi|M_m^\dagger M_m|\psi\rangle$. A **global phase** is unobservable, and states are physically rays rather than vectors.

A **relative phase** is different. The states $|+\rangle=(|0\rangle+|1\rangle)/\sqrt2$ and $|-\rangle=(|0\rangle-|1\rangle)/\sqrt2$ differ only by the sign of the $|1\rangle$ amplitude. They give the same statistics in the computational basis but are orthogonal, and a measurement in the basis $\{|+\rangle,|-\rangle\}$ separates them with certainty. Relative phase is basis dependent and observable. Quantum algorithms work by manipulating relative phases.

## Density-operator form

For ensembles and subsystems (developed in [[density-operators-and-mixed-states]] and [[ensembles-and-unitary-freedom]]) the postulates read:

| Postulate | State vector | Density operator |
|---|---|---|
| 1 | unit vector $\lvert\psi\rangle$ | $\rho\ge0$, $\operatorname{tr}\rho=1$; an ensemble $\{p_i,\rho_i\}$ has state $\sum_ip_i\rho_i$ |
| 2 | $\lvert\psi\rangle\mapsto U\lvert\psi\rangle$ | $\rho\mapsto U\rho U^\dagger$ |
| 3 | $p(m)=\langle\psi\rvert M_m^\dagger M_m\lvert\psi\rangle$ | $p(m)=\operatorname{tr}(M_m^\dagger M_m\rho)$, $\ \rho\mapsto M_m\rho M_m^\dagger/p(m)$ |
| 4 | $\lvert\psi_1\rangle\otimes\lvert\psi_2\rangle$ | $\rho_1\otimes\rho_2$ |

If the outcome of a measurement is recorded nowhere, the state becomes $\sum_mM_m\rho M_m^\dagger$ (N&C Eq. 2.152). This is the simplest example of a quantum channel, the general description of noise.

## Physical interpretation

- **Closed versus driven.** Applying a gate to a qubit means the qubit is not closed. In practice an external field enters the qubit's Hamiltonian as a controllable parameter, and the qubit evolves unitarily under a time-dependent $H(t)$ to a good approximation ([[two-level-systems-and-rabi-oscillations]]).
- **Measurement is invasive.** Postulate 3 typically changes the state. Whether it can be derived from unitary evolution of system plus apparatus is still debated. Nielsen and Chuang, and this notebook, use it pragmatically.
- **Exponential state space.** By Postulate 4, $n$ qubits need $2^n$ amplitudes. This is the root of both the difficulty of simulating many electrons and the promise of quantum computers.

## Source

Nielsen and Chuang, *Quantum Computation and Quantum Information* (10th anniversary ed., Cambridge University Press, 2010):

- Sec. 2.2.1–2.2.3, pp. 80–86: Postulates 1–3, Eqs. (2.82)–(2.98); the Hamiltonian example (2.89); Exercises 2.55–2.57.
- Sec. 2.2.7, p. 93: global and relative phase, Exercise 2.65.
- Sec. 2.2.8, pp. 93–96: Postulate 4; measurement through an ancilla, Eqs. (2.122)–(2.131); Exercises 2.66–2.68.
- Sec. 2.4.1–2.4.2, pp. 99–102: density-operator form, Eqs. (2.139)–(2.161).

Page numbers are those printed in the book. All numerical statements are checked in `nielsen_chuang/part5_batch6.py` (section A).
