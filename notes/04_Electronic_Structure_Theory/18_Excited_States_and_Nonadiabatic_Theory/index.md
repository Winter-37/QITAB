States above the ground state and what happens between them: excitation energies and intensities, excited-state surfaces, and the couplings that break the Born–Oppenheimer picture.

## What this chapter is about

Absorption spectra, fluorescence, photochemistry and excited-state dynamics all need states above the ground state. Earlier chapters already contain several routes to them:

- CIS as the Tamm-Dancoff limit of TDHF (Chapter 17);
- linear response of a mean field, TDHF (Chapter 17) and TDDFT (this chapter);
- EOM-CC as the poles of the coupled-cluster response function (Chapters 12 and 17);
- state-averaged multiconfigurational methods (Chapter 13).

This chapter collects them as excited-state methods: how each describes an excited state, what it gets right, and where it fails. Where two potential energy surfaces approach each other, the Born–Oppenheimer separation fails. Nonadiabatic couplings and conical intersections then govern radiationless decay and photochemistry.

## Why it matters

- **TDDFT is the workhorse.** Most computed UV-vis spectra of molecules beyond a few atoms come from TDDFT. Its structure is TDHF with an exchange-correlation kernel. Its failures (charge transfer, double excitations, triplet instabilities with too much exact exchange) follow from that structure.
- **Excited states are harder than the ground state.** There is no variational principle for an individual excited state in response theory. Errors of 0.2–0.5 eV are common, and states of different character (valence, Rydberg, charge transfer) need different treatment.
- **Excited-state gradients and couplings.** Optimizing an excited-state geometry, or following photodynamics, needs excited-state gradients and derivative couplings. These are Lagrangian problems of the same kind as Chapter 15.
- **Connections.** Excited-state DMET and quantum-subspace methods (Part 6) target the same quantities, and are judged against the methods here.

## Where it is used later

- Quantum excited-state methods (Part 6, Chapter 8, planned).
- Electronic excitations from a chemical point of view (Part 3, Chapter 7, planned).

## The main ideas, in order

1. **TDDFT linear response.** The Kohn–Sham quasienergy, the adiabatic approximation, the exchange-correlation kernel in the $\mathbf A$ and $\mathbf B$ matrices, and triplet stability.
2. **Vibronic band shapes.** Franck–Condon factors, Duschinsky rotation, the generating function, Huang–Rhys factors and the Poisson progression, the linear coupling (vertical gradient) model, Herzberg–Teller intensity borrowing.
3. Planned: CIS and EOM-CC as excited-state methods; excited-state CI; conical intersections; nonadiabatic couplings; state tracking.

## How to read it

**Path.** [[tddft-linear-response]], [[vibronic-band-shapes-franck-condon-and-herzberg-teller]], then the planned sections.

**Needs.** Chapters 8 (Kohn-Sham DFT), 9, 12, 13 and 17 (linear response for variational wave functions); time-dependent theory and the Berry phase (Part 2, Chapter 11). The vibronic section also needs harmonic analysis and electronic absorption from Chapter 16.

**Checkpoint.** From the closed-shell $\mathbf A$ and $\mathbf B$ matrices, show that $\mathbf A-\mathbf B$ is the same for singlets and triplets, and explain why a large Coulomb coupling in the triplet $\mathbf A$ makes Hartree–Fock but not B3LYP unstable for beryllium.

**Planned sections:** Excited-state wave functions; CIS and EOM-CC; Excited-state CI; Conical intersections; Nonadiabatic couplings; State tracking.
