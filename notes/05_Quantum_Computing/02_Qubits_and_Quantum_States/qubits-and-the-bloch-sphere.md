---
id: qubits-and-the-bloch-sphere
title: Qubits and the Bloch sphere
summary: A qubit is a unit vector a|0⟩ + b|1⟩ in C². Removing the unobservable global phase leaves two real parameters, cos(θ/2)|0⟩ + e^{iφ} sin(θ/2)|1⟩, which label a point on the unit sphere with Bloch vector (sin θ cos φ, sin θ sin φ, cos θ). The eigenstates of X, Y and Z sit at ±x, ±y and ±z. Orthogonal states are antipodal, |⟨s|t⟩|² = (1 + r_s·r_t)/2. A measurement yields one bit, although the state has a continuum of values. n qubits need 2ⁿ amplitudes, and measuring a subset of them renormalizes the rest. Links the qubit to spin ½ and to the Bloch ball of mixed states.
status: in-progress
kind: theory
level: introductory
tags: [qubit, bloch-sphere, bloch-vector, computational-basis, global-phase, multiple-qubits, spin-half, nielsen-chuang]
prerequisites: [quantum-postulates-for-information, spin-one-half]
related: [density-operators-and-mixed-states, single-qubit-gates-and-rotations, multi-qubit-states-and-bell-states, projective-and-povm-measurements, ensembles-and-unitary-freedom]
order: 10
date: 2026-11-17
---

## Overview

The qubit is the unit of quantum information, as the bit is of classical information. Physically it is any two-level system, such as two polarizations of a photon, a spin ½ in a field, or two electronic levels of an atom or a superconducting circuit. Abstractly it is a unit vector in $\mathbb C^2$. This note fixes the notation used throughout Part 5 and introduces the Bloch sphere, the geometric picture of single-qubit states and gates.

## One qubit

With a fixed orthonormal **computational basis** $|0\rangle,|1\rangle$,

$$
|\psi\rangle=\alpha|0\rangle+\beta|1\rangle,\qquad |\alpha|^2+|\beta|^2=1 .
$$

Measuring in the computational basis gives 0 with probability $|\alpha|^2$ and 1 with probability $|\beta|^2$, and leaves $|0\rangle$ or $|1\rangle$ ([[quantum-postulates-for-information]]). Two other bases are used constantly:

$$
|\pm\rangle=\frac{|0\rangle\pm|1\rangle}{\sqrt2},\qquad |{\pm i}\rangle=\frac{|0\rangle\pm i|1\rangle}{\sqrt2}.
$$

These are the eigenstates of $X$ and $Y$, as $|0\rangle,|1\rangle$ are of $Z$.

## The Bloch sphere

Normalization leaves three real parameters, and the global phase is unobservable, so any state can be written

$$
|\psi\rangle=e^{i\gamma}\Big(\cos\tfrac\theta2\,|0\rangle+e^{i\varphi}\sin\tfrac\theta2\,|1\rangle\Big)
\ \simeq\ \cos\tfrac\theta2\,|0\rangle+e^{i\varphi}\sin\tfrac\theta2\,|1\rangle ,
\qquad 0\le\theta\le\pi,\ 0\le\varphi<2\pi .
$$

The pair $(\theta,\varphi)$ is a point on the unit sphere, with **Bloch vector**

$$
\mathbf r=(\sin\theta\cos\varphi,\ \sin\theta\sin\varphi,\ \cos\theta)=\big(\langle X\rangle,\langle Y\rangle,\langle Z\rangle\big).
$$

The second equality, checked for random states, makes $\mathbf r$ the vector of Pauli expectation values. It is the same construction as the spin-½ polarization of [[spin-one-half]].

!!! example "Landmarks (N&C Exercise 4.1)"

    | state | Bloch vector |
    |---|---|
    | $\lvert0\rangle,\ \lvert1\rangle$ | $+\hat z,\ -\hat z$ |
    | $\lvert+\rangle,\ \lvert-\rangle$ | $+\hat x,\ -\hat x$ |
    | $\lvert{+i}\rangle,\ \lvert{-i}\rangle$ | $+\hat y,\ -\hat y$ |

**Half angles.** For two pure states,

$$
|\langle s|t\rangle|^2=\tfrac12\big(1+\mathbf r_s\cdot\mathbf r_t\big),
$$

so orthogonal states are **antipodal**, not perpendicular. The angle on the sphere is twice the angle in Hilbert space, which is why $\theta/2$ appears in the parametrization and in the rotation operators $e^{-i\theta\,\mathbf n\cdot\boldsymbol\sigma/2}$ ([[single-qubit-gates-and-rotations]]). The identity is my addition, checked numerically.

**Measurement along an axis.** Measuring $\mathbf v\cdot\boldsymbol\sigma$ gives $+1$ with probability $(1+\mathbf v\cdot\mathbf r)/2$ ([[projective-and-povm-measurements]]). For $|0\rangle$ this is $(1+v_3)/2$.

**Mixed states** fill the interior. $\rho=(I+\mathbf r\cdot\boldsymbol\sigma)/2$ is a valid state if and only if $|\mathbf r|\le1$, with $|\mathbf r|=1$ exactly for pure states and $\mathbf r=0$ for $I/2$ ([[density-operators-and-mixed-states]], [[ensembles-and-unitary-freedom]]).

## How much information is in a qubit?

A qubit state has a continuum of possible values $(\theta,\varphi)$, but a measurement returns one bit and destroys the rest by collapsing the state. Determining $\alpha$ and $\beta$ requires many identically prepared copies, and the statistical error of each estimated expectation value falls only as $1/\sqrt{\text{copies}}$ ([[concentration-inequalities-and-sampling]]). Holevo's bound, planned for later chapters, makes this precise: one qubit can carry at most one bit of accessible classical information.

## Many qubits

Two qubits have the computational basis $|00\rangle,|01\rangle,|10\rangle,|11\rangle$ and a general state $\sum_x\alpha_x|x\rangle$. Measuring only the first qubit gives 0 with probability $|\alpha_{00}|^2+|\alpha_{01}|^2$, and leaves

$$
\frac{\alpha_{00}|00\rangle+\alpha_{01}|01\rangle}{\sqrt{|\alpha_{00}|^2+|\alpha_{01}|^2}} .
$$

For $n$ qubits the basis states are $|x_1x_2\cdots x_n\rangle$, and a general state needs $2^n$ complex amplitudes. For $n=500$ that is more than the estimated number of atoms in the universe. There is no Bloch sphere for several qubits: most of the state space consists of entangled states ([[multi-qubit-states-and-bell-states]]).

**Ordering convention.** In this notebook $|x_1x_2\cdots x_n\rangle=|x_1\rangle\otimes\cdots\otimes|x_n\rangle$, with qubit 1 the most significant bit, as in Nielsen and Chuang. Qiskit uses the opposite order, with qubit 0 as the least significant bit, written rightmost. The same circuit then has a permuted matrix, so ordering must be checked whenever matrices are compared across sources ([[controlled-operations]]).

## Connection to chemistry

Under the Jordan–Wigner mapping, each qubit stores the occupation of one spin orbital, with $|1\rangle$ meaning occupied. A computational basis state is then a Slater determinant written as an occupation-number string ([[jordan-wigner-mapping]]).

## Source

Nielsen and Chuang, *Quantum Computation and Quantum Information* (10th anniversary ed., Cambridge University Press, 2010):

- Sec. 1.2, pp. 13–16: the qubit, Eqs. (1.1)–(1.4), the Bloch sphere (Figure 1.3) and the information content of a qubit.
- Sec. 1.2.1, pp. 16–17: multiple qubits, Eqs. (1.5)–(1.7).
- Sec. 4.2, p. 174: the Bloch vector; Exercise 4.1.
- Sec. 2.2.5, p. 90: Exercises 2.59–2.61.

Page numbers are those printed in the book. The qubit-ordering remark about Qiskit is from general knowledge of the library, not from the book. Numerical checks are in `nielsen_chuang/part5_batch6.py` (section D).
