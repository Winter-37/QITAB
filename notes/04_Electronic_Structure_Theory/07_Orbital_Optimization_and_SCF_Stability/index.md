Hartree–Fock revisited as an optimization problem, in second quantization.

## What this chapter is about

Chapter 3 found the Hartree–Fock orbitals by solving an eigenvalue equation self-consistently. This chapter treats the same problem as a minimization. Any set of orthonormal orbitals can be reached from a reference set by a unitary rotation,

$$
|\tilde 0\rangle = e^{-\hat\kappa}|0\rangle,\qquad
\hat\kappa=\sum_{p>q}\kappa_{pq}\big(\hat E_{pq}-\hat E_{qp}\big),
$$

with the parameters $\kappa_{pq}$ unconstrained. The energy $E(\boldsymbol\kappa)$ then has a gradient, which is the antisymmetric part of the generalized Fock matrix. Its Hessian is the orbital Hessian. Hartree–Fock is the point where the gradient vanishes, and stability means the Hessian there is positive definite.

## Why it matters

- **SCF convergence becomes understandable.** Roothaan iterations are a fixed-point method that converges linearly at best and can oscillate. DIIS extrapolates, and Newton and trust-region steps use the Hessian to converge quadratically and safely. Knowing why each works helps when a calculation fails.
- **A converged SCF is not necessarily the right answer.** A solution with zero gradient can be a saddle point. Stability analysis checks the Hessian for negative eigenvalues: singlet instabilities (toward another RHF solution) and triplet instabilities (toward UHF). Multiple solutions exist in stretched bonds, radicals and transition-metal systems.
- **The same machinery serves later methods.** The generalized Fock matrix and the orbital Hessian return unchanged in MCSCF. The linear equations of coupled-perturbed Hartree–Fock for gradients are the Hessian applied to a response vector.
- **Large systems.** Working with the density matrix instead of orbital coefficients gives formulations whose cost can scale linearly with system size.

## Where it is used later

- [[mcscf-parametrization-gradient-and-hessian|MCSCF gradient and Hessian]] and [[mcscf-second-order-optimization|second-order MCSCF]] (Chapter 13).
- [[cphf-closed-shell|Coupled-perturbed Hartree–Fock]] and [[rhf-analytic-hessian|the RHF Hessian]] (Chapter 15).
- [[h2-dissociation-rhf-uhf|The RHF → UHF instability of H₂]] (Chapter 3), seen here as a negative Hessian eigenvalue.

## The main ideas, in order

1. **Orbital rotations.** $e^{\hat\kappa}$ transforms creation operators unitarily; rotations within the occupied space or within the virtual space are redundant for a single determinant.
2. **Gradient and Hessian.** The generalized Fock matrix (with inactive and active parts) and the orbital Hessian, defined for any wave function.
3. **Second-order SCF.** The Newton step and its link to stability; Brillouin's theorem as the stationarity condition.
4. **Production convergence.** Roothaan–Hall iterations, DIIS, integral-direct SCF, and Newton with a trust region.
5. **Density-based Hartree–Fock.** An idempotent AO density with an exponential parametrization.
6. **Instabilities and multiple solutions.** Singlet and triplet instabilities, symmetry breaking, and how to find the lowest solution.

## How to read it

**Path.**

1. Orbital rotations $e^{\hat\kappa}$, and the HF state's parametrization with its redundancies.
2. The generalized Fock matrix and the orbital Hessian.
3. Second-order SCF and stability.
4. Production convergence: DIIS and Newton, and density-based HF.
5. Instabilities and multiple solutions.

**Leads to.** The same tools return for MCSCF (Chapter 13) and in CPHF (Chapter 15).

**Reading.** Second-pass chapter: skip it on a first reading and come back after the core chapters (Chapter 5 first; it is the prerequisite for almost every deep note).

**Planned sections:** Localized orbitals.
