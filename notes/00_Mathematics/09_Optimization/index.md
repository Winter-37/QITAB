Constrained stationary points and the derivatives of optimized quantities. Hartree–Fock, MCSCF, coupled cluster, VQE and geometry optimization all look for stationary points, usually under constraints, and their analytic gradients all differentiate a quantity that was optimized or defined by equations. This chapter states the mathematics behind both once, so that the method chapters can refer to it. The unconstrained algorithms (Newton and quasi-Newton steps, line searches, trust regions) are in Part 7, Chapter 2, starting from [[optimality-conditions-and-convergence-rates]].

## What this chapter is about

Two questions:

- **Where is a constrained stationary point, and what kind is it?** Lagrange multipliers turn a constrained problem into stationarity of a Lagrangian. The projected Hessian of that Lagrangian decides minimum, maximum or saddle. Inequality constraints add sign and complementarity conditions (KKT).
- **How does an optimized or constrained quantity change with an external parameter?** If the quantity is stationary in its internal parameters, their response drops out (the envelope theorem, of which Hellmann–Feynman is a case). If the internal parameters are fixed by other equations, adding those equations with multipliers makes the quantity stationary again. One adjoint solve then replaces a response solve per perturbation.

## Why it matters

- **Orbital energies are Lagrange multipliers.** Orthonormality constraints on the orbitals produce a symmetric multiplier matrix. Diagonalizing it gives the canonical Hartree–Fock and Kohn–Sham equations. The exponential parametrization removes the constraints instead.
- **Multipliers are sensitivities.** The temperature is the multiplier of the energy constraint in maximum entropy, the chemical potential the multiplier of electron number in DFT, and the level shift of a trust-region step the multiplier of the step-length bound.
- **Excited states are saddle points.** The projected Hessian of the energy has one negative direction per lower state, which is why variational optimizers collapse to the ground state.
- **Gradients of nonvariational methods cost one extra solve, not one per coordinate.** The Lagrangian (Z-vector, adjoint) method is what makes analytic gradients of MP2, CC, CI on SCF orbitals, selected CI and embedding schemes affordable. Its stationarity also gives the 2n + 1 rule.

## The main ideas, in order

1. **Equality constraints and Lagrange multipliers.** The geometric condition, LICQ, the multiplier as sensitivity, second-order conditions with the projected Hessian, matrix constraints (orthonormal orbitals) and the alternative of parametrizing them away, inequality constraints and the KKT conditions.
2. **Derivatives of optimized quantities.** The envelope theorem and Hellmann–Feynman, second derivatives and the response equation, the Lagrangian for quantities defined by equations, the adjoint interchange and its cost, the 2n + 1 rule.

## How to read it

**Path.**

1. [[lagrange-multipliers-and-kkt-conditions]]
2. [[envelope-theorem-and-the-lagrangian-method]]

**Needs.** Chapter 2 ([[differential-calculus]], [[matrix-calculus]], [[eigenvalue-and-eigenvector-derivatives]]) and Chapter 4 ([[multivariable-taylor-expansion]]: the quadratic model).

**Leads to.**

- The Hartree–Fock equations (Part 4, Chapter 3) and Kohn–Sham theory (Part 4, Chapter 8).
- Orbital optimization (Part 4, Chapter 7).
- Analytic energy derivatives, the Z-vector method and the Lagrangian of nonvariational energies (Part 4, Chapter 15).
- Variational quantum algorithms (Part 6).

**Planned sections:** Duality and convex optimization; Optimization on manifolds (orbital rotations on the Grassmann manifold).
