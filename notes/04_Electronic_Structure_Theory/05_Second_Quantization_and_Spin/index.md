The language of every method from Chapter 7 on.

## What this chapter is about

Second quantization rewrites the determinant algebra of Chapter 2 as operator algebra. A creation operator $a_p^\dagger$ adds an electron to spin orbital $p$, and an annihilation operator $a_p$ removes one. They obey

$$
\{a_p^\dagger,a_q\}=\delta_{pq},\qquad \{a_p,a_q\}=\{a_p^\dagger,a_q^\dagger\}=0 ,
$$

and antisymmetry is built into these anticommutators. The Hamiltonian takes a form that does not depend on the number of electrons:

$$
\hat H=\sum_{pq}h_{pq}\,a_p^\dagger a_q+\tfrac12\sum_{pqrs}g_{pqrs}\,a_p^\dagger a_r^\dagger a_s a_q .
$$

The chapter then develops:

- spin-adapted excitation operators $\hat E_{pq}$;
- spin tensor operators and genealogical spin coupling;
- normal ordering and Wick's theorem, which turn long operator strings into short sums;
- the generalization to nonorthogonal orbitals.

## Why it matters

- **Derivations get shorter and more reliable.** Matrix elements that need careful sign bookkeeping with determinants become mechanical anticommutator manipulations.
- **Modern methods are written this way.** Coupled cluster's $e^{\hat T}$, orbital rotations $e^{\hat\kappa}$, MCSCF Hessians, response theory, propagators and the Lagrangian approach to gradients are all formulated in second quantization. Without this chapter the deep notes elsewhere cannot be read.
- **Quantum computing starts here.** Fermion-to-qubit mappings such as Jordan–Wigner translate exactly these operators into Pauli strings. The Hamiltonian above, with integrals from a Hartree–Fock calculation, is the input to VQE and SQD.
- **Spin symmetry can be handled exactly.** Spin tensor operators and configuration state functions keep wave functions as eigenfunctions of $\hat S^2$, which determinant-based methods otherwise lose.

## Where it is used later

- [[orbital-rotations|Orbital rotations]] (Chapter 7) and [[mcscf-parametrization-gradient-and-hessian|MCSCF]] (Chapter 13).
- [[coupled-cluster-second-quantization|Coupled cluster]] (Chapter 11) and [[perturbation-theory-second-quantization|perturbation theory]] (Chapter 10), where Wick's theorem is used heavily.
- [[density-matrices-second-quantization|Density matrices]] (Chapter 6).
- [[jordan-wigner-mapping|The Jordan–Wigner mapping]] (Part 6).

## How to read it

**Path.**

1. Creation and annihilation operators, operators in second quantization, and the finite-basis picture.
2. Spin-tensor operators and singlet excitation operators $\hat E_{pq}$. With them come genealogical spin coupling and the symmetry properties exact wave functions should keep.
3. Normal ordering and Wick's theorem, needed for perturbation theory and coupled cluster.
4. Second quantization in a nonorthogonal basis.

**Needs.** Chapter 2.

**Reading.** Second-pass chapter. Skip it on a first reading; read it before any deep note elsewhere, since second quantization underlies them.

**Checkpoint.** Derive $\hat H = \sum h_{pq}\hat E_{pq} + \tfrac12\sum g_{pqrs}\hat e_{pqrs}$ and evaluate $\langle\text{HF}|\hat H|\text{HF}\rangle$ in this language.
