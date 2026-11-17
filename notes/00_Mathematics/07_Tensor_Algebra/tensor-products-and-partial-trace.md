---
id: tensor-products-and-partial-trace
title: Tensor products and the partial trace
summary: How the state space of a composite system is built from those of its parts. Defines the tensor product of spaces, vectors and operators, the Kronecker-product matrix representation and its index ordering, the rules (mixed product, adjoint, trace, eigenvalues, exponential of a sum), product versus entangled states with a rank test, and the partial trace, which gives the state of a subsystem and is fixed uniquely by requiring correct local measurement statistics. All identities checked numerically.
status: in-progress
kind: theory
level: intermediate
tags: [tensor-product, kronecker-product, composite-system, partial-trace, reduced-density-operator, entanglement, product-state, qubit-ordering, nielsen-chuang]
prerequisites: [dirac-notation, matrices-and-determinants, spectral-decomposition-and-normal-operators]
related: [schmidt-decomposition-and-purification, density-operators-and-mixed-states, addition-of-angular-momenta, two-particle-systems-and-reduced-mass, jordan-wigner-mapping]
order: 10
date: 2026-11-17
---

## Tensor product of spaces and vectors

If $V$ and $W$ have dimensions $m$ and $n$, their **tensor product** $V\otimes W$ is the $mn$-dimensional space spanned by the products $|i\rangle\otimes|j\rangle$ of basis vectors. Its elements are linear combinations $\sum_{ij}c_{ij}|i\rangle\otimes|j\rangle$, and the product of two vectors is bilinear:

$$
z\big(|v\rangle\otimes|w\rangle\big) = (z|v\rangle)\otimes|w\rangle = |v\rangle\otimes(z|w\rangle) ,
$$

$$
(|v_1\rangle + |v_2\rangle)\otimes|w\rangle = |v_1\rangle\otimes|w\rangle + |v_2\rangle\otimes|w\rangle ,
$$

and likewise in the second factor. The shorthand $|v\rangle|w\rangle$, $|v,w\rangle$ or $|vw\rangle$ is common. The inner product factorizes, $\big(\langle v|\otimes\langle w|\big)\big(|v'\rangle\otimes|w'\rangle\big) = \langle v|v'\rangle\langle w|w'\rangle$, and is extended by linearity.

Dimensions multiply, they do not add. Two particles in 3D need a wave function of six variables, $\psi(\mathbf r_1,\mathbf r_2)$, not two functions of three; $n$ qubits need $2^n$ amplitudes. This exponential growth is both the difficulty of many-body quantum mechanics and the resource of quantum computing.

## Operators

For $A$ on $V$ and $B$ on $W$, $A\otimes B$ acts on $V\otimes W$ by $(A\otimes B)(|v\rangle\otimes|w\rangle) = A|v\rangle\otimes B|w\rangle$. A general operator on $V\otimes W$ is a sum of such products. An operator acting on one part only is $A\otimes1$ or $1\otimes B$.

**Matrix representation (Kronecker product).** For an $m\times n$ matrix $A$ and a $p\times q$ matrix $B$,

$$
A\otimes B = \begin{pmatrix}A_{11}B&A_{12}B&\cdots&A_{1n}B\\ A_{21}B&A_{22}B&\cdots&A_{2n}B\\ \vdots&&&\vdots\\ A_{m1}B&\cdots&&A_{mn}B\end{pmatrix}\qquad(mp\times nq) .
$$

For vectors, $(1,2)\otimes(2,3) = (2,3,4,6)$. The index of $|i\rangle\otimes|j\rangle$ is $i\,n + j$ (counting from 0), so the **first factor is the most significant**: for qubits, $|1\rangle\otimes|0\rangle = |10\rangle$ is basis vector 2. This is the convention of most quantum-computing texts and of NumPy's `kron`. Some software (Qiskit, for one) numbers qubits from the least significant end, so that qubit 0 is the last factor of the Kronecker product; check the convention before comparing matrices.

## Rules

For compatible matrices (all checked numerically with random complex matrices of dimensions 2 and 3):

| identity | comment |
|---|---|
| $(A\otimes B)(C\otimes D) = AC\otimes BD$ | mixed-product rule; the basis of everything else |
| $(A\otimes B)^\dagger = A^\dagger\otimes B^\dagger$ | so products of Hermitian, unitary, positive or projection operators are of the same kind |
| $\mathrm{tr}(A\otimes B) = \mathrm{tr}A\;\mathrm{tr}B$ | |
| eigenvalues of $A\otimes B$ are $a_ib_j$ | eigenvectors $|a_i\rangle\otimes|b_j\rangle$ |
| eigenvalues of $A\otimes1 + 1\otimes B$ are $a_i + b_j$ | the spectrum of non-interacting subsystems |
| $e^{A\otimes1 + 1\otimes B} = e^A\otimes e^B$ | because $A\otimes1$ and $1\otimes B$ commute |
| $\det(A\otimes B) = (\det A)^{\dim W}(\det B)^{\dim V}$ | |
| $A\otimes B\neq B\otimes A$ in general | related by the swap operator: $\mathrm{SWAP}(A\otimes B)\mathrm{SWAP} = B\otimes A$ |

The fourth and fifth lines are why the energy of two non-interacting systems is the sum of their energies, and why the eigenfunctions of a separable Hamiltonian are products.

## Product and entangled states

A state of $V\otimes W$ is a **product state** if it can be written $|v\rangle\otimes|w\rangle$, and **entangled** otherwise. Writing $|\psi\rangle = \sum_{ij}c_{ij}|i\rangle|j\rangle$, the coefficients form an $m\times n$ matrix $C$, and

$$
|\psi\rangle\ \text{is a product state}\iff\mathrm{rank}\,C = 1 ,
$$

since a product state has $c_{ij} = v_iw_j$, an outer product. A random state of a qubit and a qutrit has rank 2 (entangled); the product test case has rank 1. The Bell state $(|00\rangle + |11\rangle)/\sqrt2$ has $C = \mathbb 1/\sqrt2$, rank 2. The rank of $C$ is the Schmidt number of [[schmidt-decomposition-and-purification]].

## The partial trace

The state of a composite system is a density operator $\rho^{AB}$ on $V_A\otimes V_B$ ([[density-operators-and-mixed-states]]). The state of $A$ alone is the **reduced density operator**

$$
\rho^A = \mathrm{tr}_B\,\rho^{AB} ,
$$

where the partial trace is defined on products by

$$
\mathrm{tr}_B\big(|a_1\rangle\langle a_2|\otimes|b_1\rangle\langle b_2|\big) = |a_1\rangle\langle a_2|\;\langle b_2|b_1\rangle
$$

and extended by linearity. In components, $(\rho^A)_{ii'} = \sum_j\rho^{AB}_{ij,i'j}$: reshape the $mn\times mn$ matrix into a four-index array and contract the two $B$ indices. (In NumPy: `rho.reshape(m,n,m,n)` followed by `einsum('ijkj->ik')`.)

**Why this is the right definition.** For any observable $M$ of $A$, measured on the composite system as $M\otimes1$, we need

$$
\mathrm{tr}\big(M\rho^A\big) = \mathrm{tr}\big((M\otimes1)\rho^{AB}\big) .
$$

The partial trace satisfies this, and it is the only linear map that does so for every $M$: expanding $f(\rho^{AB})$ in an orthonormal basis of operators on $A$, the condition fixes every coefficient. So the reduced density operator is not a convention; it is the unique description of $A$ that reproduces all measurements made on $A$ alone.

**Examples.**

- For a product $\rho\otimes\sigma$, $\mathrm{tr}_B(\rho\otimes\sigma) = \rho\,\mathrm{tr}\sigma = \rho$.
- For the Bell state, $\rho^A = \tfrac12\mathbb 1$: the pair is in a pure state, and each qubit separately is completely random. Purity $\mathrm{tr}(\rho^A)^2 = \tfrac12$ is the minimum for a qubit.
- For a random $6\times6$ density matrix on a qubit and a qutrit, $\rho^A$ is positive with unit trace and satisfies the defining identity for a random observable $M$.

The partial trace is how reduced density matrices of electrons are defined ([[density-operators-and-mixed-states]] and Part 4), and how the effect of an environment on a system is described.

## Source

Nielsen and Chuang, *Quantum Computation and Quantum Information* (10th anniversary ed., Cambridge University Press, 2010), Sec. 2.1.7, pp. 71-74 (tensor products, Eqs. (2.42)-(2.49), the Kronecker product (2.50)-(2.51), Exercises 2.26-2.33); Sec. 2.4.3, pp. 105-108 (the reduced density operator and partial trace, Eqs. (2.177)-(2.184), Box 2.6 on why the partial trace is the unique correct choice). Page numbers are those printed in the book.

The table of rules, the rank test and the remarks on qubit ordering are my own summary; every identity is checked in `mathematics/part0_batch5.py` (section H).
