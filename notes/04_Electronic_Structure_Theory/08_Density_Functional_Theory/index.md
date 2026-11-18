The other mean-field route: density functional theory in the Kohn–Sham scheme.

## What this chapter is about

Hartree–Fock approximates the wave function. Density functional theory works with the electron density $\rho(\mathbf r)$ instead, a function of three variables however many electrons there are. The Hohenberg–Kohn theorem shows that the ground-state density fixes the Hamiltonian and therefore every ground-state property, and that the exact energy functional is minimized by the true density. Kohn and Sham turned this into a practical method by introducing a noninteracting reference system with the same density. Its orbitals obey one-electron equations with exactly the matrix structure of the Roothaan equations (Chapter 3), except that the exchange operator is replaced by a local exchange–correlation potential. Everything not known exactly is collected in one term, the exchange–correlation functional $E_{xc}[\rho]$, and the whole art of applied DFT lies in approximating it.

## Why it matters

- **Correlation at mean-field cost.** A Kohn–Sham calculation is an SCF calculation of the same size as Hartree–Fock, yet with a good functional it recovers most of the correlation energy that HF misses: for the atomization energy of water, B3LYP with a small basis gets 93% where HF gets 59%.
- **It is what most applied quantum chemistry uses.** Routine geometries, frequencies and reaction energies of large molecules are DFT results, and correlated wave-function methods (Chapters 9–14) are often used to calibrate it.
- **Its failures are systematic.** Self-interaction, missing dispersion, wrong orbital energies and spin-symmetry breaking in stretched bonds follow from the form of the approximate functionals. Knowing them tells you when a DFT number cannot be trusted.

## Where it is used later

- [[electronic-structure-methods-at-a-glance|The overview of methods]] (Chapter 14) places DFT alongside the wave-function methods.
- Geometry optimization and vibrational analysis (Chapter 16) work the same way with KS energies and analytic gradients.
- Exchange–correlation potentials built from the uniform electron gas connect to [[free-electron-gas|the free electron gas]] (Part 2).

## The main ideas, in order

1. **Hohenberg–Kohn.** The density determines the external potential; the energy is a functional $E_v[\rho] = \int\rho v + F[\rho]$ with a universal but unknown $F$; a variational principle for trial densities.
2. **Kohn–Sham.** A noninteracting reference with the exact density; $E = T_s + V_{Ne} + J + E_{xc}$; the KS equations with $v_{xc} = \delta E_{xc}/\delta\rho$; their basis-set form and numerical quadrature.
3. **The functional ladder.** LDA/LSDA from the uniform gas, GGAs, meta-GGAs, hybrids with exact exchange, double hybrids with MP2 correlation, and dispersion corrections.
4. **DFT against HF.** What each gets right and wrong, shown on small systems where the exact answer is known.

## How to read it

**Path.** [[kohn-sham-dft]], [[exchange-correlation-functionals]], [[dft-versus-hartree-fock]].

**Needs.** Chapter 3 (the Fock operator, the Roothaan equations and UHF), Chapter 4 (basis sets), the variational principle and the free electron gas (Part 2). MP2 (Chapter 10) is needed only for the paragraph on double hybrids.

**Leads to.** Chapter 14 (comparing methods), Chapter 16 (geometries and frequencies), and the planned excited-states chapter (Chapter 18) through time-dependent DFT.

**Core (first pass).** [[kohn-sham-dft]], [[exchange-correlation-functionals]], [[dft-versus-hartree-fock]].

**Checkpoint.** Write the KS energy of water as $T_s + V_{Ne} + J + E_{xc} + V_{NN}$ and say which term a functional approximates. Then explain why the H₂⁺ curve from PBE goes to the wrong limit although H₂⁺ has only one electron.

**Planned sections:** Range-separated hybrid functionals; Time-dependent DFT and excitation energies; Self-interaction corrections.
