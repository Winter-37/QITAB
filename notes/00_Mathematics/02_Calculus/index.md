Calculus of one and several variables: functions, limits and continuity, derivatives, and integrals. These are the tools every later chapter uses without comment.

## What this chapter is about

The chapter builds the calculus that the rest of the notebook takes for granted:

- the vocabulary of functions (domain, inverse, parity, the elementary functions);
- the limit, which defines continuity, the derivative, the integral and the sum of a series;
- differentiation, including partial derivatives, Jacobians, stationary points and Lagrange multipliers;
- integration, including the Gamma function, differentiation under the integral sign and multiple integrals with a change of variables;
- calculus with matrices: differentials of inverses, determinants, square roots and exponentials, and derivatives of eigenvalues and eigenvectors;
- calculus of variations: stationary functionals, the Euler–Lagrange equation, constraints, Rayleigh–Ritz, and functional derivatives.

Fourier transforms, which used to sit in this chapter, are now in Chapter 4 next to Fourier series.

## Why it matters

- **Derivatives are physics.** Forces are gradients of energies, response properties are derivatives with respect to fields, and the Hessian classifies minima and transition states.
- **Lagrange multipliers turn constraints into equations.** Orthonormality constraints in Hartree–Fock produce the orbital energies as multipliers.
- **Gaussian and Slater integrals are Gamma functions.** Every radial integral in a basis-set code reduces to $\Gamma(z)$, and every Gaussian moment follows from one integral by differentiating under the integral sign.
- **Changes of variables carry Jacobians.** The $r^2\sin\theta$ of spherical coordinates is the reason radial probability densities have an $r^2$.
- **Analytic gradients are matrix calculus.** $d(\mathbf X^{-1}) = -\mathbf X^{-1}d\mathbf X\,\mathbf X^{-1}$, the derivative of $\mathbf S^{-1/2}$, and the eigenvector derivative with its $1/(\varepsilon_k - \varepsilon_j)$ denominators are behind every U matrix, energy-weighted density and orbital-response equation.
- **Quantum mechanics is a variational problem.** The Schrödinger equation is the Euler–Lagrange equation of the energy at fixed normalization, every basis-set method is Rayleigh–Ritz, and every DFT potential is a functional derivative.

## The main ideas, in order

1. **Functions.** Domain and range, injectivity and inverses, principal branches, even and odd parts, and the elementary functions.
2. **Limits and continuity.** The ε–δ definition, standard limits, continuity theorems, and $O$ and $o$ notation.
3. **Differential calculus.** Differentiation rules, the mean value theorem, L'Hôpital's rule, partial derivatives, total differentials, the cyclic relation, Jacobians, Hessians, Lagrange multipliers.
4. **Integral calculus.** Riemann sums, the fundamental theorem, substitution, parts, partial fractions, improper integrals, the Gamma and Beta functions, the Leibniz rule, multiple integrals.
5. **Matrix calculus.** Differentials of traces, inverses and determinants (Jacobi's formula), $\mathbf S^{\pm1/2}$ by a Sylvester equation, the derivative of $e^{\mathbf K}$, divided differences for any matrix function.
6. **Eigenvalue and eigenvector derivatives.** Hellmann–Feynman for matrices, second derivatives, phase, near-degeneracy, degenerate levels, and the generalized problem $\mathbf{Hc} = \varepsilon\mathbf{Sc}$.
7. **Calculus of variations.** Functionals, the Euler–Lagrange equation and Beltrami identity, Hamilton's principle, constraints, the Schrödinger equation as a constrained variation, Rayleigh–Ritz.
8. **Functional derivatives.** Definition, local and gradient-dependent functionals, the Hartree potential and kernel, derivatives with respect to orbitals, the Euler equation of DFT.

## How to read it

**Path.**

1. [[functions]]
2. [[limits-and-continuity]]
3. [[differential-calculus]]
4. [[integral-calculus]]
5. [[matrix-calculus]]
6. [[eigenvalue-and-eigenvector-derivatives]]
7. [[calculus-of-variations-and-the-euler-lagrange-equation]]
8. [[functional-derivatives]]

**Needs.** School algebra and trigonometry for sections 1–4; Chapter 1 (matrices, the eigenvalue problem, functions of matrices) for sections 5–6.

**Leads to.** Vector calculus (Chapter 3), series and expansions (Chapter 4), differential equations (Chapter 6), constrained optimization and the Lagrangian method (Chapter 9), analytic energy derivatives (Part 4, Chapter 15), density functional theory (Part 4, Chapter 8), and every physics part.

**Planned sections:** Second variation and sufficient conditions (Legendre and Jacobi conditions).
