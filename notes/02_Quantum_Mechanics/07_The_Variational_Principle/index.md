Every wave-function method in Part 4 is either variational or measured against a variational bound, so this chapter is the entry point to electronic-structure theory.

## What this chapter is about

The Schrödinger equation can rarely be solved exactly, but the ground-state energy always obeys one inequality. For any normalized trial state $|\tilde\Psi\rangle$,

$$
E_0 \;\le\; \langle\tilde\Psi|\hat H|\tilde\Psi\rangle .
$$

This turns an equation we cannot solve into a minimization we can attempt. Choose a family of trial functions, compute the energy, and lower it by varying the parameters. The lowest value found is the best estimate within that family, and it is guaranteed not to undershoot. When the trial function is a linear combination of fixed basis functions, the minimization becomes exactly a matrix eigenvalue problem, the secular equation.

## Why it matters

- **It is the logic of most of quantum chemistry.** Hartree–Fock minimizes over single determinants. CI minimizes over linear combinations of determinants. MCSCF minimizes over both orbitals and coefficients. VQE minimizes over the parameters of a quantum circuit. Each is the variational principle applied to a different trial space.
- **Bounds make methods comparable.** A larger trial space can only lower the minimum. This gives a strict ordering, for example $E_\text{RHF}\ge E_\text{UHF}\ge E_\text{FCI}\ge E_0$ when each is a global minimum in the same basis. It is also why adding functions to a basis can only lower a variational energy.
- **Excited states are bounded too.** The Hylleraas–Undheim–MacDonald interlacing theorem shows that the $k$th root of a linear variational problem is an upper bound to the $k$th exact level. This justifies reading excited states off a CI calculation.
- **The first bonds.** The hydrogen molecule ion and the Heitler–London treatment of H₂ explain chemical bonding as a variational energy lowering from overlap and exchange.

The principle has a limit: a good energy does not guarantee a good wave function. An error of first order in the wave function gives only a second-order error in the energy, which is both why the method works and why other properties converge more slowly.

## Where it is used later

- [[hartree-fock-equations|The Hartree–Fock equations]] and [[full-ci|full CI]] (Part 4).
- [[mcscf-and-gvb|MCSCF]] (Part 4, Chapter 13).
- [[variational-quantum-eigensolver|VQE]] (Part 6).
- The non-variational methods, MP2 and coupled cluster, which give up the bound. The [[lagrangian-for-nonvariational-energies|Lagrangian technique]] restores the stationarity that the bound would have provided.

## The main ideas, in order

1. **The principle.** Expand the trial state in exact eigenstates. Every component above the ground state can only raise the energy.
2. **Using it.** Rank trial functions, optimize their parameters, and estimate how far the result is from the true ground state.
3. **Linear variation.** A fixed basis turns minimization into diagonalization of the Hamiltonian matrix. All roots are stationary points.
4. **Upper bounds and interlacing.** The Hessian at the $K$th root has $K-1$ negative directions. Adding a basis function interlaces the old and new roots.
5. **Applications.** Helium with an effective nuclear charge, H₂⁺ as the one-electron bond, and H₂ in the Heitler–London picture with singlet and triplet.

## How to read it

**Path.** [[variational-principle]], [[variation-method]], [[linear-variation-method]], [[upper-bounds-and-interlacing]], then the applications [[helium-ground-state-variational]] (effective nuclear charge), [[hydrogen-molecule-ion-variational]] (the one-electron bond) and [[hydrogen-molecule-heitler-london]] (the two-electron bond, singlet against triplet).

**Needs.** Chapter 3 (expansion in eigenstates) and Chapter 5 (helium, exchange symmetry). The Hermitian eigenvalue problem (Part 0, Chapter 1: [[matrix-eigenvalue-problem|the matrix eigenvalue problem]]).

**Leads to.** Chapter 8 (perturbation theory, the other general approximation). Part 4, Chapters 2–3 (determinants and Hartree–Fock) and Chapter 9 (CI).

**Planned sections:** none at present.
