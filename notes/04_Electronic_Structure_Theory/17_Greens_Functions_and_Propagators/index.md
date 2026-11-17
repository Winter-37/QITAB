Ionization energies and excitation spectra directly from propagators, without computing each state separately.

## What this chapter is about

Methods so far compute one state at a time: the ground state, then each excited or ionized state as a separate calculation. Spectroscopy measures *differences* between states. Propagators, or many-body Green's functions, target those differences directly. A propagator $\langle\langle\hat A;\hat B\rangle\rangle_E$ is a function of energy with:

- **poles** at the energy differences between the reference state and other states;
- **residues** equal to products of transition matrix elements.

Two cases matter most:

- the **one-particle Green's function** (electron propagator), with $\hat A,\hat B$ creation and annihilation operators. Its poles are ionization energies and electron affinities.
- the **polarization propagator**, with $\hat A,\hat B$ one-body excitation operators. Its poles are excitation energies and its residues give oscillator strengths.

## Why it matters

- **Corrections to Koopmans' theorem.** The electron propagator, with the self-energy $\Sigma(E)$ in the Dyson equation $G^{-1}=G_0^{-1}-\Sigma$, adds orbital relaxation and correlation to frozen-orbital ionization energies. Second order is already a large improvement.
- **RPA and TDHF.** The polarization propagator at the Hartree–Fock level is the random-phase approximation. It gives excitation energies, dynamic polarizabilities and the stability conditions of Chapter 7 in one framework. TDDFT has the same structure.
- **It is the language of response theory and of $GW$.** Linear-response CC, ADC and the $GW$ method used in materials science are propagator methods. The superoperator formalism here is a common starting point for all of them.
- **It connects to the single-particle Green's function of Part 2.** It is the same resolvent idea, $(E-\hat H)^{-1}$, applied to a many-electron system.

## Where it is used later

- The planned excited-states chapter (Chapter 18): TDDFT, EOM and response.
- [[eom-ccsd-and-size-extensivity|EOM-CC]] (Chapter 12), the coupled-cluster counterpart of the polarization propagator.

## The main ideas, in order

1. **The superoperator formalism.** Propagators, their spectral representation, and the moment expansion.
2. **The electron propagator.** The Dyson equation, the self-energy, and second-order ionization energies with orbital relaxation and pair correlation.
3. **The polarization propagator.** TDHF/RPA, its stability, coupled Hartree–Fock, and length and velocity forms of transition moments.

## How to read it

**Path.**

1. The superoperator formalism.
2. The one-particle Green's function and second-order self-energy for ionization potentials.
3. The polarization propagator and RPA.

**Needs.** Chapters 3, 10 and 15.

**Reading.** Second-pass chapter: skip it on a first reading and come back after the core chapters (Chapter 5 first; it is the prerequisite for almost every deep note).
