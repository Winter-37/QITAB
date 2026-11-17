Composite systems: tensor products of spaces and operators, the partial trace, and the Schmidt decomposition of bipartite states.

## What this chapter is about

When two systems A and B are combined, the state space of the whole is the tensor product $\mathcal H_A\otimes\mathcal H_B$, not the sum. Its dimension is the product $d_A d_B$. This chapter covers:

- how to build that space, and the vectors and operators on it, including the Kronecker-product matrices used in calculations;
- how to go back down to one part, using the partial trace;
- what a general state of two parts looks like, using the Schmidt decomposition.

## Why it matters

- **Exponential growth.** $n$ two-level systems live in a space of dimension $2^n$. Classical simulation of electrons is hard for this reason, and quantum computers are promising for the same reason.
- **Entanglement is defined here.** A state is entangled when it is not a product $|a\rangle\otimes|b\rangle$. The number of nonzero Schmidt coefficients (the Schmidt rank) measures how far it is from one.
- **Subsystems are described by reduced density matrices.** The partial trace is the only way to assign a state to part of a larger system consistently. The one- and two-particle RDMs of Part 4 are partial traces of this kind.
- **The Schmidt decomposition is an SVD.** It follows that both parts of a pure state have the same nonzero reduced-density-matrix eigenvalues. It also follows that a fragment of dimension $d$ is entangled with at most $d$ states of its environment, which is the basis of DMET.

## Where it is used later

- [[spin-one-half|Spin]] and [[addition-of-angular-momenta|addition of angular momenta]] (Part 2).
- [[exchange-symmetry-spin-and-symmetrization-principle|Identical particles]] (Part 2), whose states lie in the symmetric or antisymmetric subspace of a tensor product.
- [[one-particle-rdm|Reduced density matrices]] and [[natural-orbitals|natural orbitals]] (Part 4, Chapter 6).
- [[schmidt-decomposition-and-dmet-bath|The DMET bath]] (Part 4, Chapter 19).
- Multi-qubit registers and the [[jordan-wigner-mapping|Jordan–Wigner mapping]] (Parts 5 and 6).

## The main ideas, in order

1. **Tensor products of spaces, vectors and operators.** The rules (mixed product, adjoint, trace, eigenvalues) and the Kronecker matrix with its index-ordering convention.
2. **The partial trace.** Defined by $\operatorname{Tr}(\rho_A O_A)=\operatorname{Tr}\big(\rho\,(O_A\otimes 1_B)\big)$ for every $O_A$. The result is the only reduced state that reproduces every measurement on A.
3. **Schmidt decomposition.** $|\psi\rangle=\sum_i\lambda_i|i_A\rangle|i_B\rangle$, obtained from the SVD of the coefficient matrix.
4. **Purification.** Every mixed state is the reduced state of some pure state on a larger space.
5. **Limits.** For three or more parties no general Schmidt form exists; the W state is the counterexample.

## How to read it

**Path.** [[tensor-products-and-partial-trace]], then [[schmidt-decomposition-and-purification]].

**Needs.** Chapter 1 (Dirac notation, the spectral theorem, the singular value decomposition).

**Leads to.** Many-particle wave functions (Part 2, Chapter 5), reduced density matrices (Part 4, Chapter 6), and multi-qubit states (Part 5).

**Planned sections:** Index notation and contractions; Tensor decompositions.
