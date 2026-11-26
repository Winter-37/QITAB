Composite systems (tensor products of spaces and operators, the partial trace, and the Schmidt decomposition of bipartite states), Cartesian tensors under rotation (isotropic tensors and orientational averages), and low-rank decompositions of arrays with many indices (CP, Tucker, tensor trains).

## What this chapter is about

When two systems A and B are combined, the state space of the whole is the tensor product $\mathcal H_A\otimes\mathcal H_B$, not the sum. Its dimension is the product $d_A d_B$. This chapter covers:

- how to build that space, and the vectors and operators on it, including the Kronecker-product matrices used in calculations;
- how to go back down to one part, using the partial trace;
- what a general state of two parts looks like, using the Schmidt decomposition;
- how a Cartesian property tensor transforms under rotation, and what survives when it is averaged over all orientations;
- how a tensor with many indices can be stored and approximated with far fewer numbers.

## Why it matters

- **Exponential growth.** $n$ two-level systems live in a space of dimension $2^n$. Classical simulation of electrons is hard for this reason, and quantum computers are promising for the same reason.
- **Entanglement is defined here.** A state is entangled when it is not a product $|a\rangle\otimes|b\rangle$. The number of nonzero Schmidt coefficients (the Schmidt rank) measures how far it is from one.
- **Subsystems are described by reduced density matrices.** The partial trace is the only way to assign a state to part of a larger system consistently. The one- and two-particle RDMs of Part 4 are partial traces of this kind.
- **Compression decides what is computable.** Integrals with four indices, CI vectors with one index per orbital and many-qubit states are too large to store. Low-rank formats (Cholesky and density fitting for integrals, tensor hypercontraction, matrix product states for DMRG) make them tractable when the right structure exists.
- **The Schmidt decomposition is an SVD.** It follows that both parts of a pure state have the same nonzero reduced-density-matrix eigenvalues. It also follows that a fragment of dimension $d$ is entangled with at most $d$ states of its environment, which is the basis of DMET.

## Where it is used later

- [[spin-one-half|Spin]] and [[addition-of-angular-momenta|addition of angular momenta]] (Part 2).
- [[exchange-symmetry-spin-and-symmetrization-principle|Identical particles]] (Part 2), whose states lie in the symmetric or antisymmetric subspace of a tensor product.
- [[one-particle-rdm|Reduced density matrices]] and [[natural-orbitals|natural orbitals]] (Part 4, Chapter 6).
- [[schmidt-decomposition-and-dmet-bath|The DMET bath]] (Part 4, Chapter 19).
- Multi-qubit registers and the [[jordan-wigner-mapping|Jordan–Wigner mapping]] (Parts 5 and 6).
- [[density-fitting-and-cholesky-decomposition|Density fitting and Cholesky decomposition]] of the electron-repulsion integrals (Part 4, Chapter 4), and DMRG (Part 4, Chapter 20).

## The main ideas, in order

1. **Tensor products of spaces, vectors and operators.** The rules (mixed product, adjoint, trace, eigenvalues) and the Kronecker matrix with its index-ordering convention.
2. **The partial trace.** Defined by $\operatorname{Tr}(\rho_A O_A)=\operatorname{Tr}\big(\rho\,(O_A\otimes 1_B)\big)$ for every $O_A$. The result is the only reduced state that reproduces every measurement on A.
3. **Schmidt decomposition.** $|\psi\rangle=\sum_i\lambda_i|i_A\rangle|i_B\rangle$, obtained from the SVD of the coefficient matrix.
4. **Purification.** Every mixed state is the reduced state of some pure state on a larger space.
5. **Limits.** For three or more parties no general Schmidt form exists; the W state is the counterexample.
6. **Rotational averages.** A rank-$n$ Cartesian tensor transforms with $n$ direction-cosine matrices. Its orientational average is an isotropic tensor, built from $\delta$ and $\epsilon$; ranks 2–4 give the invariants of refraction, optical rotation, Raman and two-photon spectra.
7. **Tensor decompositions.** CP (sums of rank-one terms; rank hard to compute, best approximations may not exist), Tucker and the higher-order SVD (one subspace per index), and tensor trains or matrix product states (built by successive SVDs; ranks are Schmidt ranks, errors add).

## How to read it

**Path.** [[tensor-products-and-partial-trace]], then [[schmidt-decomposition-and-purification]], then [[tensor-decompositions]], which uses the Schmidt decomposition at every cut. [[rotational-averages-and-isotropic-tensors]] is independent of the others and can be read on its own.

**Needs.** Chapter 1 (Dirac notation, the spectral theorem, the singular value decomposition, change of basis).

**Leads to.** Many-particle wave functions (Part 2, Chapter 5), reduced density matrices (Part 4, Chapter 6), integral factorization (Part 4, Chapter 4), multi-qubit states (Part 5), isotropic spectroscopic invariants (Part 4, Chapter 16), and tensor-network methods (Part 4, Chapter 20).

**Planned sections:** Index notation, contractions and contraction order.
