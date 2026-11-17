Separation of variables gives stationary states; the exactly solvable one-dimensional problems then show the features that recur everywhere (Griffiths Ch. 2).

## What this chapter is about

For a time-independent potential the Schrödinger equation separates. The solutions $\Psi(x,t)=\psi(x)e^{-iEt/\hbar}$ are *stationary states*: their probability density does not change in time and their energy is sharp. The spatial part obeys

$$
\hat H\psi = E\psi .
$$

The rest of the chapter solves this equation exactly for the standard one-dimensional potentials:

- the infinite square well;
- the harmonic oscillator, solved twice (algebraically and by power series);
- the free particle;
- the delta-function well;
- the finite square well;
- general one-dimensional scattering.

## Why it matters

These few models contain almost every qualitative feature of quantum systems:

- **Quantization from boundary conditions.** Only certain energies allow a normalizable solution.
- **Nodes and orthogonality.** The $n$th state has $n-1$ nodes, and different eigenstates are orthogonal and complete. This is the structure behind every basis expansion.
- **Ladder operators.** The oscillator is solved purely algebraically, by factorizing $\hat H$ with $a_\pm$. This is the first appearance of creation and annihilation operators, which become second quantization in Part 4.
- **Bound states versus scattering states.** States with $E<V(\pm\infty)$ are discrete and normalizable. States above are continuous, need wave packets, and come with reflection and transmission probabilities.
- **Tunnelling and the deep-well and shallow-well limits.** A one-dimensional attractive well, however shallow, always has at least one bound state.

The oscillator in particular is everywhere. It describes molecular vibrations, normal modes, the coherent states of light, and the expansion of any potential around a minimum.

## Where it is used later

- [[harmonic-oscillator-ladder-operators|Ladder operators]] → [[creation-and-annihilation-operators|creation and annihilation operators]] (Part 4, Chapter 5).
- [[infinite-square-well|The particle in a box]] → the [[free-electron-gas|free electron gas]] (Chapter 5) and basis-set intuition.
- [[delta-function-potential|The delta well]] and [[one-dimensional-scattering-and-transfer-matrix|1D scattering]] → [[band-structure-and-the-dirac-comb|band structure]] (Chapter 5) and three-dimensional scattering (Chapter 10).
- [[finite-square-well|The finite well]] → WKB tunnelling (Chapter 9) and the scattering length (Chapter 10).

## The main ideas, in order

1. **Stationary states.** Separation of variables gives the time-independent equation. The general solution is $\sum_n c_n\psi_n e^{-iE_nt/\hbar}$, with $|c_n|^2$ the probability of energy $E_n$.
2. **The box.** Energies $n^2\pi^2\hbar^2/2ma^2$, sine eigenfunctions, and Fourier's trick for finding the coefficients $c_n$.
3. **The oscillator, two ways.** The ladder operators give $(n+\tfrac12)\hbar\omega$ algebraically. The power series reaches the same spectrum because normalizability forces the series to terminate, which produces the Hermite polynomials.
4. **Free particles.** Plane waves cannot be normalized, so physical states are wave packets that move at the group velocity.
5. **Bound and scattering states.** The delta and finite wells show bound states, and reflection and transmission coefficients. The S-matrix and transfer matrix describe one-dimensional scattering in general.

## How to read it

**Path.** [[stationary-states]], [[infinite-square-well]], [[harmonic-oscillator-ladder-operators]], [[harmonic-oscillator-analytic-solution]], [[free-particle-and-wave-packets]], [[delta-function-potential]], [[finite-square-well]], [[one-dimensional-scattering-and-transfer-matrix]].

**Needs.** Chapter 1. Fourier transforms (Part 0, Chapter 2) and Hermite polynomials (Part 0, Chapter 3: [[classical-orthogonal-polynomials|orthogonal polynomials]]).

**Leads to.** Chapter 3 (the formalism that generalizes these examples), Chapter 4 (three dimensions), and the scattering and tunnelling chapters (9 and 10).

**Planned sections:** none at present.
