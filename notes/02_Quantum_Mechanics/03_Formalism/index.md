The general structure behind Chapter 2: Hilbert space, Hermitian operators, the measurement postulate in full, representations, the uncertainty principles, and density operators (Griffiths Ch. 3, Sakurai Sec. 3.4).

## What this chapter is about

Chapter 2 solved particular equations. This chapter states the theory they are examples of:

- **States** are vectors $|\Psi\rangle$ in a Hilbert space.
- **Observables** are Hermitian operators.
- **A measurement** of $\hat Q$ returns an eigenvalue $q_n$ with probability $|\langle f_n|\Psi\rangle|^2$.
- **Wave functions are components.** $\Psi(x)$, $\Phi(p)$ and the coefficients $c_n$ are the components of one vector in three different bases.

The chapter ends by moving from single states to ensembles. A density operator $\hat\rho$ describes a system whose state is known only statistically.

## Why it matters

- **This is the language of every later chapter.** Matrix representations, changes of basis, commutators and eigenvalue problems are how Hartree–Fock, CI and coupled cluster are written. The function-space ideas here map directly onto the finite-basis linear algebra of Part 0, Chapter 1.
- **Hermiticity is not optional.** Real expectation values require Hermitian operators. Hermitian operators bring real eigenvalues, orthogonal eigenvectors and completeness, which make basis expansions possible.
- **Compatibility decides what can be known together.** Observables that commute share eigenstates. For incompatible ones the Robertson inequality bounds the product of uncertainties. Quantum numbers are labels from a set of commuting observables.
- **Density operators are unavoidable.** A subsystem of an entangled state, a thermal ensemble, or a noisy qubit has no state vector. The density operator is the general description, and reduced density matrices are its many-electron form.

## Where it is used later

- The [[matrix-eigenvalue-problem|matrix eigenvalue problem]] of every finite-basis method (Part 4).
- [[symmetry-conservation-and-degeneracy|Symmetry and conservation laws]] (Chapter 6), which rest on commutators with $\hat H$.
- [[one-particle-rdm|Reduced density matrices]] (Part 4, Chapter 6), which are partial traces of a density operator.
- Mixed states, noise and measurement in quantum computing (Part 5).

## The main ideas, in order

1. **Hilbert space and Hermitian operators.** Wave functions live in $L^2$, and observables are Hermitian because expectation values must be real.
2. **Eigenfunctions.** Hermitian operators have real eigenvalues and orthogonal eigenfunctions. Discrete spectra are normalized to Kronecker deltas, continuous spectra to Dirac deltas.
3. **The generalized statistical interpretation.** Measurement probabilities are squared overlaps, and the state collapses afterwards.
4. **Representations.** Position, momentum and energy bases are three views of one ket. Resolutions of the identity move between them.
5. **Uncertainty.** The Robertson inequality $\sigma_A^2\sigma_B^2\ge\big(\langle[\hat A,\hat B]\rangle/2i\big)^2$ and the energy–time relation. Coherent states saturate the position–momentum bound for all time.
6. **Ensembles.** $\hat\rho=\sum_i w_i|\alpha_i\rangle\langle\alpha_i|$, with averages $\operatorname{tr}(\hat\rho\hat A)$ and purity $\operatorname{tr}\hat\rho^2$.

## How to read it

**Path.** [[hilbert-space-and-hermitian-operators]], [[eigenfunctions-of-hermitian-operators]], [[generalized-statistical-interpretation]], [[position-momentum-and-energy-representations]], [[generalized-uncertainty-principle]], [[energy-time-uncertainty-principle]], [[harmonic-oscillator-coherent-states]], then [[density-operators-and-mixed-states]], which extends the formalism from single states to ensembles (Sakurai Sec. 3.4).

**Needs.** Chapters 1 and 2.

**Leads to.** Every later chapter. Density operators return in the canonical ensemble and path integrals (Chapter 6), in reduced density matrices (Part 4, Chapter 6) and in quantum information (Part 5).

**Planned sections:** none at present.
