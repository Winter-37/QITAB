When one determinant is qualitatively wrong (bond breaking, diradicals, many transition-metal systems), both orbitals and CI coefficients are optimized.

## What this chapter is about

Hartree–Fock optimizes the orbitals of one determinant. CI optimizes the coefficients of many determinants with fixed orbitals. Multiconfigurational self-consistent field (MCSCF) does both at once:

$$
|\Psi\rangle=e^{-\hat\kappa}\sum_I c_I|\Phi_I\rangle ,
$$

with a short expansion chosen to contain the nearly degenerate configurations. In the most common choice, CASSCF, the expansion is a full CI within an active space of a few orbitals and electrons. The chapter covers:

- the parametrization and its redundancies;
- the gradient and Hessian, built from the generalized Fock matrix and the 1- and 2-RDMs;
- second-order and trust-region optimization;
- state averaging for several states at once;
- CASPT2, which adds dynamic correlation on top.

## Why it matters

- **Static correlation needs it.** When a bond breaks, the bonding and antibonding configurations become degenerate. No single determinant can describe the result without breaking spin symmetry, as Chapter 3 showed for H₂. MCSCF describes such states qualitatively correctly and with the right spin.
- **It is the reference for multireference methods.** CASPT2, NEVPT2 and MRCI add dynamic correlation to an MCSCF reference. These are standard tools for photochemistry, transition metals and reaction paths with bond breaking.
- **Optimization is genuinely hard.** Orbitals and CI coefficients are strongly coupled, the energy surface has many stationary points, and plain iterations often fail. Newton methods with trust regions and augmented Hessians are what make MCSCF reliable.
- **The active space connects to quantum computing and embedding.** Choosing a small active space with an exact solver inside it is the same idea as using a quantum computer (VQE, SQD) on an active space, or an impurity solver in DMET.

## Where it is used later

- [[state-averaged-mcscf-and-configuration-rotations|State-averaged MCSCF]], the usual starting point for the planned excited-states chapter (Chapter 18).
- [[dmet-embedding-hamiltonian|The DMET embedding Hamiltonian]] (Chapter 19), an active space defined by entanglement rather than energy.
- [[sample-based-quantum-diagonalization|SQD]] and [[variational-quantum-eigensolver|VQE]] active-space calculations (Part 6).

## The main ideas, in order

1. **GVB and MCSCF.** For H₂ the two-configuration MCSCF equals the GVB perfect-pairing wave function.
2. **Second-order optimization.** Exponential parametrization, the generalized Brillouin theorem, and Newton steps on orbitals and coefficients together.
3. **Gradient and Hessian.** The block structure (orbital–orbital, orbital–CI, CI–CI) and redundant rotations.
4. **Step control.** Level-shifted Newton, trust regions and augmented Hessians.
5. **State averaging.** Exponential rotations in configuration space, and averaging over several roots.
6. **CASPT2.** A CASSCF Fock operator as zero order, and the intruder-state problem.

## How to read it

**Path.**

1. GVB and MCSCF.
2. Second-order MCSCF and its parametrization, gradient and Hessian.
3. Trust-region and augmented-Hessian methods.
4. State averaging.
5. CASPT2, which adds dynamical correlation on top.

**Needs.** Chapters 7 and 9.

**Core (first pass).** [[mcscf-and-gvb]], [[mcscf-second-order-optimization]].

**Deep (second pass).** [[mcscf-parametrization-gradient-and-hessian]], [[mcscf-trust-region-and-augmented-hessian]], [[state-averaged-mcscf-and-configuration-rotations]], [[caspt2-and-caspt-series]].

**Checkpoint.** Show that active-active rotations are redundant in a CAS but not in a general MCSCF.

**Planned sections:** CASSCF concepts and active-space selection; RASSCF; MRCI; NEVPT2; DMRG-SCF.
