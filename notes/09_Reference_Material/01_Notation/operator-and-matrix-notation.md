---
id: operator-and-matrix-notation
title: Operator, matrix and tensor notation
summary: The symbols used across the notebook for vectors, matrices, operators, adjoints, traces, commutators, expectation values and tensor contractions, with the places where books differ (hats on operators, A^† versus A^*, Einstein summation, NumPy einsum strings).
status: in-progress
kind: reference
level: introductory
tags: [notation, linear-algebra, operators, dirac-notation, tensors, einsum]
prerequisites: []
related: [dirac-notation, index-and-orbital-notation, second-quantization-and-density-matrix-notation, matrix-and-tensor-identities, commutator-and-anticommutator-identities]
conventions: [chemists-integrals, physicists-integrals]
order: 20
date: 2026-11-17
---

## Linear algebra

| Symbol | Meaning |
|---|---|
| $\mathbf a$, $\mathbf A$ | column vector, matrix (bold); $A_{ij}$ its elements |
| $\mathbf A^{\mathsf T}$, $\mathbf A^*$, $\mathbf A^\dagger$ | transpose, complex conjugate (element-wise), conjugate transpose $(\mathbf A^\dagger)_{ij} = A_{ji}^*$ |
| $\mathbf 1$ or $\mathbf I$ | identity matrix |
| $\operatorname{tr}\mathbf A$, $\det\mathbf A$ | trace, determinant |
| $\mathbf A\otimes\mathbf B$ | Kronecker (tensor) product; the left factor is the slow index |
| $\mathbf A\circ\mathbf B$ | element-wise (Hadamard) product |
| $\operatorname{vec}\mathbf X$ | columns of $\mathbf X$ stacked (column-major) |
| $\|\mathbf a\|$, $\|\mathbf A\|_F$ | Euclidean norm, Frobenius norm $\sqrt{\operatorname{tr}\mathbf A^\dagger\mathbf A}$ |
| $\delta_{ij}$, $\varepsilon_{ijk}$ | Kronecker delta, Levi-Civita symbol ($\varepsilon_{123}=+1$) |

Szabo and Nielsen–Chuang (Fig. 2.1) use the same symbols: $z^*$ for a complex conjugate, $\mathbf A^{\mathsf T}$, $\mathbf A^*$ and $\mathbf A^\dagger = (\mathbf A^{\mathsf T})^*$. Mathematics texts often write $\bar z$ and $\mathbf A^*$ for the adjoint; check before mixing.

## Quantum mechanics

| Symbol | Meaning |
|---|---|
| $|\psi\rangle$, $\langle\psi|$ | ket and bra ([[dirac-notation]]) |
| $\langle\phi|\psi\rangle$ | inner product, antilinear in the left argument |
| $\langle\phi|\hat A|\psi\rangle$, $A_{\phi\psi}$ | matrix element |
| $\langle\hat A\rangle$ | expectation value in the state named in the text |
| $\hat A$ | operator. Hats are used when an operator and a number share a letter ($\hat H$ and $H_{ij}$); Szabo writes the Hamiltonian as $\mathscr H$ without a hat |
| $\hat A^\dagger$ | adjoint, $\langle\phi|\hat A^\dagger|\psi\rangle = \langle\psi|\hat A|\phi\rangle^*$ |
| $[\hat A,\hat B]$, $\{\hat A,\hat B\}$ | commutator $\hat A\hat B-\hat B\hat A$, anticommutator $\hat A\hat B+\hat B\hat A$ |
| $\hat\rho$ | density operator ([[density-operators-and-mixed-states]]) |
| $\hat P$, $\hat\Pi$ | projector; $\hat\Pi$ also parity in Part 2 |
| $\sigma_x,\sigma_y,\sigma_z$ or $X,Y,Z$ | Pauli matrices ([[pauli-matrix-identities]]); $X,Y,Z$ in quantum-computing notes |
| $\hat{\mathbf L},\hat{\mathbf S},\hat{\mathbf J}$ | orbital, spin, total angular momentum; $\hat J_\pm = \hat J_x\pm i\hat J_y$ |

Atomic units ($\hbar = m_e = e = 4\pi\varepsilon_0 = 1$) are used in Parts 4 and 6 and stated at the top of each note; Part 2 keeps $\hbar$ explicit, as Griffiths and Sakurai do.

## Tensors and summation

- **No implicit summation.** Sums are written out ($\sum_{pq}h_{pq}D_{pq}$). Where a note uses the Einstein convention it says so.
- **Index order follows the definition.** $g_{pqrs} = (pq|rs)$ is chemists' order; $\langle pq|rs\rangle$ is physicists' ([[integral-notation]]). An array `eri[p,q,r,s]` has whichever order the code documents; PySCF returns chemists' order.
- **einsum strings** are used as a compact, unambiguous record of a contraction. `np.einsum("pqrs,pqrs->", eri, dm2)` is $\sum_{pqrs}g_{pqrs}d_{pqrs}$; `np.einsum("pq,qp->", h, dm1)` is $\operatorname{tr}(\mathbf h\,\mathbf D)$.
- **Reshaping.** NumPy is row-major: `A.reshape(n*n)` puts the last index fastest. $\operatorname{vec}$ above is column-major (`order="F"`). The identity $\operatorname{vec}(\mathbf{AXB}) = (\mathbf B^{\mathsf T}\otimes\mathbf A)\operatorname{vec}\mathbf X$ holds only for column-major stacking ([[matrix-and-tensor-identities]]).

## Calculus

| Symbol | Meaning |
|---|---|
| $\mathrm d\mathbf r$, $\mathrm d\mathbf x$ | volume element in space, in space and spin ($\int\mathrm d\mathbf x = \sum_\omega\int\mathrm d\mathbf r$) |
| $\partial_x$, $\nabla$, $\nabla^2$ | partial derivative, gradient, Laplacian |
| $\dfrac{\mathrm dE}{\mathrm dx}$ versus $\dfrac{\partial E}{\partial x}$ | total versus partial derivative; in Part 4, Ch. 15 a superscript marks a skeleton (integral-only) derivative |
| $f'$, $\dot f$ | derivative in space, in time |
| $O(N^k)$ | cost scaling with system size $N$ |

## Source

Notation collected from the notes it summarizes. Book conventions: Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996), Ch. 1 (matrix notation, $\mathbf A^\dagger$) and Ch. 2 ($\mathscr H$); Nielsen and Chuang, *Quantum Computation and Quantum Information* (Cambridge University Press, 10th anniversary ed., 2010), Sec. 2.1, Fig. 2.1, p. 62 (notation summary). The $\operatorname{vec}$ identity is checked in `part9_reference.py`, section C.
