Gradients, Hessians and properties as derivatives of the energy.

## What this chapter is about

Most molecular properties are derivatives of the energy with respect to a parameter $x$:

- forces (nuclear coordinates);
- force constants (second derivatives in nuclear coordinates);
- dipole moments (an electric field);
- polarizabilities and magnetic properties (second derivatives in fields).

Finite differences need many energy calculations and lose precision. Analytic derivatives give the exact derivative of the approximate energy at roughly the cost of one more energy calculation. The difficulty is that the energy depends on $x$ both explicitly, through the integrals, and implicitly, through the orbitals and amplitudes that were optimized for it. For a variational parameter the implicit dependence drops out. For a non-variational one it has to be computed or avoided.

## Why it matters

- **Geometry optimization and dynamics need forces.** Every optimized structure, transition state and ab initio molecular dynamics step uses gradients. Hessians give vibrational frequencies and characterize stationary points.
- **The orbital response problem.** Hartree–Fock is variational in its orbitals, so the RHF gradient needs no orbital response. Correlated methods on HF orbitals (CI, MP2, CC) are not variational in those orbitals. Their gradients contain the orbital response $U^x$, which must come from the coupled-perturbed Hartree–Fock (CPHF) equations.
- **One linear solve instead of many.** The Z-vector method (Handy–Schaefer) and its general form, the Lagrangian, replace one CPHF solve per coordinate with a single perturbation-independent solve. This makes correlated gradients practical and is the template for every modern gradient implementation.
- **The same machinery serves embedding.** The DMET gradient in Chapter 19 is a Lagrangian with multipliers for the solver, the bath construction and the mean field. It is assembled from exactly the pieces in this chapter.

## Where it is used later

- [[geometry-optimization|Geometry optimization]] (Chapter 16).
- [[dmet-analytic-nuclear-gradient|The DMET analytic gradient]] (Chapter 19) and the gradient analysis in [[li-2023-dmet-gradient|Li et al. 2023]] (Part 8).
- Quantum-algorithm gradients (planned, Part 6, Chapter 9).

## The main ideas, in order

1. **Properties as response.** Expectation values, transition moments and response properties; nuclear displacements as a perturbation, with Hellmann–Feynman and Pulay terms.
2. **Bookkeeping.** Derivative integrals and the $U$ matrices that describe how MO coefficients respond.
3. **Hartree–Fock.** The RHF gradient (energy-weighted density, no response), CPHF from differentiating the Brillouin condition, and the RHF Hessian by the $2n+1$ rule.
4. **Correlated energies.** The CI gradient (CI coefficients drop out, orbital response does not), the Z-vector method, and the selected-CI gradient, where a truncated determinant list breaks orbital invariance.
5. **The general Lagrangian.** Any non-variational energy made stationary with multipliers. CPCI and the CI Hessian.

## How to read it

**Path.**

1. **The framework.** Properties as response, and nuclear displacements as a perturbation (Hellmann-Feynman and Pulay terms).
2. **Bookkeeping.** Derivative integrals and the U matrices.
3. **Hartree-Fock.** The RHF gradient (no response needed), CPHF, and the RHF Hessian.
4. **Correlated, non-variational energies.** The CI gradient, the Z-vector method, the selected-CI gradient (where every orbital pair responds), the Lagrangian form, and CPCI with the CI Hessian.

**Needs.** Chapters 3, 7 and 9.

**Reading.** Second-pass chapter: skip it on a first reading and come back after the core chapters (Chapter 5 first; it is the prerequisite for almost every deep note).

**Planned sections:** Orbital-relaxed CC gradients; MCSCF (CASSCF) gradients; ROHF and UHF derivatives.
