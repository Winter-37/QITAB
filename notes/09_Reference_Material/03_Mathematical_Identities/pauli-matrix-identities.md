---
id: pauli-matrix-identities
title: Pauli matrix identities
summary: The product rule σ_iσ_j = δ_ij + iε_ijkσ_k and its consequences (commutators, anticommutators, (a·σ)(b·σ)), the exponential exp(-iθ n·σ/2), traces and determinants, spin flip by σ_y, Hadamard conjugation, orthogonality and completeness of n-qubit Pauli strings, the commutation rule for Pauli strings, and SWAP = (I + XX + YY + ZZ)/2.
status: in-progress
kind: reference
level: introductory
tags: [pauli-matrices, spin-half, qubits, identities, pauli-strings]
prerequisites: [matrix-and-tensor-identities]
related: [spin-one-half, qubits-and-the-bloch-sphere, single-qubit-gates-and-rotations, jordan-wigner-mapping, pauli-measurement-and-grouping, qubit-ordering-conventions]
order: 50
date: 2026-11-17
---

## Definitions

$$
\sigma_x = X = \begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
\sigma_y = Y = \begin{pmatrix}0&-i\\i&0\end{pmatrix},\qquad
\sigma_z = Z = \begin{pmatrix}1&0\\0&-1\end{pmatrix},
$$

in the basis $(|0\rangle,|1\rangle) = (|{\uparrow}\rangle,|{\downarrow}\rangle)$, with $\sigma_z|0\rangle = +|0\rangle$. Spin-$\tfrac12$ operators are $\hat{\mathbf S} = \tfrac\hbar2\boldsymbol\sigma$ ([[spin-one-half]]).

## Algebra

**Product rule** (contains everything else):

$$
\sigma_i\sigma_j = \delta_{ij}\mathbf 1 + i\sum_k\varepsilon_{ijk}\sigma_k .
$$

Consequences:

$$
[\sigma_i,\sigma_j] = 2i\sum_k\varepsilon_{ijk}\sigma_k,\qquad
\{\sigma_i,\sigma_j\} = 2\delta_{ij}\mathbf 1,\qquad
\sigma_x\sigma_y\sigma_z = i\mathbf 1,
$$

$$
(\mathbf a\cdot\boldsymbol\sigma)(\mathbf b\cdot\boldsymbol\sigma) = (\mathbf a\cdot\mathbf b)\,\mathbf 1 + i(\mathbf a\times\mathbf b)\cdot\boldsymbol\sigma .
$$

Each $\sigma_i$ is Hermitian, unitary and traceless, with $\sigma_i^2 = \mathbf 1$, eigenvalues $\pm1$ and $\det\sigma_i = -1$. With $\hat{\mathbf S} = \boldsymbol\sigma/2$ ($\hbar = 1$), $\hat S^2 = \tfrac34\mathbf 1$.

**Exponential.** For a unit vector $\mathbf n$, $(\mathbf n\cdot\boldsymbol\sigma)^2 = \mathbf 1$, so

$$
e^{-i\theta\,\mathbf n\cdot\boldsymbol\sigma/2} = \cos\tfrac\theta2\,\mathbf 1 - i\sin\tfrac\theta2\,\mathbf n\cdot\boldsymbol\sigma .
$$

This is the rotation by $\theta$ about $\mathbf n$ for spin $\tfrac12$ and the gate $R_{\mathbf n}(\theta)$ of [[single-qubit-gates-and-rotations]]. At $\theta = 2\pi$ it equals $-\mathbf 1$.

**Conjugations.**

$$
\sigma_y\,\sigma_i^*\,\sigma_y = -\sigma_i\quad(\text{spin flip; the time-reversal structure of spin } \tfrac12),
\qquad
HXH = Z,\quad HZH = X,\quad HYH = -Y,
$$

with $H = (X + Z)/\sqrt2$ the Hadamard gate.

## Pauli strings on $n$ qubits

A Pauli string is a tensor product $P = P_1\otimes\cdots\otimes P_n$ with each $P_k\in\{I,X,Y,Z\}$. There are $4^n$ of them.

**Orthogonality and completeness.**

$$
\operatorname{tr}(P_\alpha^\dagger P_\beta) = 2^n\,\delta_{\alpha\beta},
\qquad
\hat A = \sum_\alpha c_\alpha P_\alpha,\quad c_\alpha = \frac{\operatorname{tr}(P_\alpha\hat A)}{2^n} .
$$

The $c_\alpha$ are real when $\hat A$ is Hermitian. A qubit Hamiltonian after a fermion-to-qubit mapping is such an expansion ([[jordan-wigner-mapping]]).

**Commutation.** Two Pauli strings either commute or anticommute. They **commute if and only if they differ by anticommuting single-qubit factors on an even number of sites** (sites where both are non-identity and different). Example: $XX$ and $ZZ$ commute (two such sites); $XI$ and $ZI$ anticommute (one site). This is the test used in measurement grouping ([[pauli-measurement-and-grouping]]).

**Two-qubit exchange.**

$$
\mathrm{SWAP} = \tfrac12\big(I\otimes I + X\otimes X + Y\otimes Y + Z\otimes Z\big),
$$

equivalently $\boldsymbol\sigma_1\cdot\boldsymbol\sigma_2 = 2\,\mathrm{SWAP} - \mathbf 1$, the origin of the Heisenberg exchange form $\hat{\mathbf S}_1\cdot\hat{\mathbf S}_2$.

## Checks

`part9_reference.py`, section G: all products, commutators and anticommutators; the vector identity and the exponential for random $\mathbf a,\mathbf b,\mathbf n$; the spin-flip and Hadamard relations; orthogonality of all 64 three-qubit strings; reconstruction of a random $8\times8$ Hermitian matrix from its Pauli coefficients (imaginary parts below $10^{-15}$); the even-overlap commutation rule for all 2016 pairs of three-qubit strings; and the SWAP formula.

## Source

Nielsen and Chuang, *Quantum Computation and Quantum Information* (Cambridge University Press, 10th anniversary ed., 2010), Sec. 2.1.9, Exercises 2.40-2.43, Eqs. (2.73)-(2.78) (Pauli commutators, anticommutators, product rule), Sec. 4.2, Eqs. (4.4)-(4.8) and Exercise 4.5 (rotation operators); Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 4.4.1 (spin 1/2). All identities verified numerically here.
