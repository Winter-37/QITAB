How to build antisymmetric many-electron wave functions and evaluate the Hamiltonian between them.

## What this chapter is about

The electronic Hamiltonian of Chapter 1 acts on functions of $N$ electron coordinates, and those functions must change sign when two electrons are exchanged. This chapter supplies the basic building blocks:

- **Spin orbitals.** A spatial orbital times $\alpha$ or $\beta$.
- **Slater determinants.** Antisymmetrized products of $N$ spin orbitals,
$$
\Phi = \frac{1}{\sqrt{N!}}\det\big[\chi_1\chi_2\cdots\chi_N\big] .
$$
- **Excited determinants.** Determinants obtained by replacing occupied spin orbitals with virtual ones. In a finite basis the exact wave function is a linear combination of all of them (full CI).
- **The Slater–Condon rules.** These give $\langle\Phi_I|\hat H|\Phi_J\rangle$ in terms of one- and two-electron integrals, depending only on how many spin orbitals the two determinants differ in.

## Why it matters

- **Every wave-function method is built from these pieces.** Hartree–Fock is one determinant, CI is a linear combination, and coupled cluster is an exponential of excitations. In each case the energy is a sum of Slater–Condon matrix elements.
- **Integral notation is a constant source of error.** Physicists' $\langle ij|kl\rangle$ and chemists' $(ij|kl)$ order the indices differently. Antisymmetrized integrals $\langle ij||kl\rangle$ and the reduction from spin to spatial orbitals each introduce factors of 2 and sign conventions. Fixing them once here prevents errors later.
- **Spin needs care.** The Hamiltonian is spin-free, so exact states are eigenfunctions of $\hat S^2$, but a single open-shell determinant usually is not. Spin-adapted configurations restore the correct spin. This is the origin of spin contamination in UHF.
- **A small model to check everything.** Minimal-basis H₂ has four spin orbitals and a 2×2 full-CI problem. Each new idea in Chapters 3–13 can be checked on it by hand.

## Where it is used later

- [[hartree-fock-equations|Hartree–Fock]] (Chapter 3), [[full-ci|full CI]] and [[cisd|CISD]] (Chapter 9).
- [[creation-and-annihilation-operators|Second quantization]] (Chapter 5), which encodes the same rules algebraically.
- [[h2-dissociation-rhf-uhf|H₂ dissociation]] and [[h2-minimal-basis-correlation-analysis|minimal-basis correlation analysis]], which both use the H₂ model.

## The main ideas, in order

1. **Spin orbitals and antisymmetry.** Spin enters through two orthonormal functions; the antisymmetry principle restricts which many-electron functions are allowed.
2. **Determinants.** Hartree products distinguish electrons; determinants do not. Normalization, overlaps and the notation for excited determinants follow.
3. **Matrix elements.** The Slater–Condon rules for zero, one and two differences, and zero for more than two.
4. **Spin.** Integrating out spin for restricted orbitals; $\hat S^2$ for many electrons; singlet and triplet combinations of open-shell determinants.
5. **The running example.** Minimal-basis H₂.

## How to read it

**Path.**

1. Spin orbitals, and the integral notation used in every later chapter.
2. Slater determinants and excited determinants.
3. The Slater-Condon rules: every method below is built from these matrix elements.
4. Integrating out spin, spin operators, and spin-adapted configurations.
5. The minimal-basis H$_2$ model, which serves as the running example from here to Chapter 13.

**Leads to.** Chapter 3.

**Core (first pass).** [[spin-orbitals-and-antisymmetry]], [[integral-notation]], [[slater-determinants]], [[excited-determinants]], [[slater-condon-rules]], [[spin-orbital-to-spatial-orbital]], [[spin-operators]], [[spin-adapted-configurations]], [[minimal-basis-h2-model]].

**Checkpoint.** Prove the variational bound by eigenfunction expansion. Show that a two-electron determinant changes sign under exchange. Derive $\langle\Psi_0|\hat H|\Psi_0\rangle$ for minimal-basis H₂ from the Slater-Condon rules.
