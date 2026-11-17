Electronic-structure theory is mostly linear algebra in disguise.

## What this chapter is about

Once a basis is chosen, every operator becomes a matrix and every state a column of numbers. This chapter collects the finite-dimensional linear algebra that the rest of the notebook uses:

- matrices and determinants, written in Dirac notation;
- how matrices change under a change of basis;
- the Hermitian eigenvalue problem;
- functions of matrices;
- the decompositions that say what a general operator looks like (spectral, polar, singular value);
- the exponential form of unitary matrices and the commutator expansions that go with it.

The last note carries the same ideas over from vectors to functions, where the sums become integrals.

## Why it matters

The central equations of quantum chemistry are matrix equations:

$$
\mathbf{F}\mathbf{C} = \mathbf{S}\mathbf{C}\boldsymbol\varepsilon \quad(\text{Hartree–Fock}),
\qquad
\mathbf{H}\mathbf{c} = E\,\mathbf{c} \quad(\text{CI}),
\qquad
\mathbf U = e^{\boldsymbol\kappa},\ \boldsymbol\kappa^\dagger = -\boldsymbol\kappa \quad(\text{orbital rotations}).
$$

Several recurring tricks are statements from this chapter:

- **Orthogonalization.** The overlap matrix is turned into the identity with $\mathbf S^{-1/2}$, a function of a matrix.
- **Orbital optimization.** Unitary rotations are parametrized by unconstrained anti-Hermitian generators.
- **Coupled cluster.** The similarity-transformed Hamiltonian is evaluated with the Baker–Campbell–Hausdorff series.
- **Natural orbitals and the DMET bath.** Both come from diagonalizing or decomposing a density matrix.

Knowing which result is being used, and its conditions, is what makes those derivations readable.

## Where it is used later

- [[basis-orthogonalization|Löwdin and canonical orthogonalization]] and the [[rhf|Roothaan equations]] in Part 4, Chapter 3.
- [[orbital-rotations|Orbital rotations]] and the [[generalized-fock-matrix-and-orbital-hessian|orbital Hessian]] in Part 4, Chapter 7.
- [[coupled-cluster-second-quantization|Coupled cluster in second quantization]] (Part 4, Chapter 11), which needs the BCH expansion.
- [[natural-orbitals|Natural orbitals]] and the [[schmidt-decomposition-and-dmet-bath|DMET bath]], which use the eigen- and singular value decompositions.
- The resolvent $(z-\mathbf H)^{-1}$, the starting point of [[one-particle-greens-function|Green's functions]].

## The main ideas, in order

1. **Representation.** A basis turns kets into columns and operators into matrices. A change between orthonormal bases is unitary, and traces, determinants and eigenvalues do not change.
2. **The Hermitian eigenvalue problem.** Eigenvalues are real and eigenvectors can be chosen orthonormal, so a single unitary diagonalizes the matrix. The secular determinant $\det(\mathbf A-\lambda\mathbf 1)=0$ gives the eigenvalues.
3. **Functions of matrices.** Diagonalize, apply $f$ to the eigenvalues, transform back: $f(\mathbf A)=\mathbf U f(\mathbf a)\mathbf U^\dagger$.
4. **Which operators can be diagonalized.** Exactly the normal ones ($\mathbf A\mathbf A^\dagger=\mathbf A^\dagger\mathbf A$) can be diagonalized by a unitary change of basis. Every operator, normal or not, has a polar decomposition and a singular value decomposition.
5. **Unitary matrices as exponentials.** Every unitary matrix is $e^{\mathbf X}$ with $\mathbf X$ anti-Hermitian, and the commutator series give $e^{\mathbf A}\mathbf B e^{-\mathbf A}$.
6. **Function spaces.** A complete orthonormal set of functions behaves like a basis with infinitely many components, and completeness is expressed by the Dirac delta.

## How to read it

**Path.** Matrices and determinants, then Dirac notation and changes of basis. The Hermitian eigenvalue problem comes next, then functions of matrices ($\mathbf S^{-1/2}$, $e^{\mathbf A}$), the spectral theorem for normal operators with simultaneous diagonalization, and the polar and singular value decompositions. The Baker-Campbell-Hausdorff expansion and the exponential parametrization of unitary matrices follow. The chapter ends by carrying all of this over from vectors to function spaces.

**Leads to.** Part 2 (operators and observables) and Part 4, Chapters 3, 5 and 7.

**Core (first pass).** [[matrices-and-determinants]], [[dirac-notation]], [[change-of-basis]], [[matrix-eigenvalue-problem]], [[functions-of-matrices]], [[orthonormal-functions-and-operators]].

**Deep (second pass).** [[spectral-decomposition-and-normal-operators]], [[polar-and-singular-value-decompositions]], [[baker-campbell-hausdorff]], [[unitary-matrices-exponential-logarithm]].

**Checkpoint.** Diagonalize a 2 × 2 Hermitian matrix by hand. Then build $\mathbf S^{-1/2}$ for a two-function overlap matrix.

**Planned sections:** Iterative diagonalization (Davidson, Lanczos).
