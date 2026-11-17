What the orbitals are expanded in, and how the integrals are computed.

## What this chapter is about

The Hartree–Fock equations become matrix equations only after the orbitals are expanded in a finite set of known functions, $\phi_i=\sum_\mu C_{\mu i}\chi_\mu$. This chapter is about those functions $\chi_\mu$:

- Slater-type and Gaussian-type functions;
- how they are contracted into the standard basis sets;
- how the energy converges as the basis grows;
- how the overlap, kinetic, nuclear-attraction and electron-repulsion integrals over Gaussians are computed in practice.

## Why it matters

- **The basis is part of the method.** Every result is "method/basis". A large method in a small basis can be worse than a modest method in a good one. Correlation energies in particular converge slowly, because Gaussians cannot reproduce the electron–electron cusp.
- **Gaussians are a compromise for integrals.** Slater functions have the right cusp at the nucleus and the right exponential tail. Gaussians have neither, but the product of two Gaussians on different centres is a single Gaussian on a third centre. That one property makes multicentre integrals fast enough for practical use.
- **Integral evaluation dominates the cost.** There are formally $O(K^4)$ two-electron integrals. McMurchie–Davidson, Obara–Saika and Rys quadrature evaluate them efficiently, and Schwarz screening and multipole methods show that only $O(K^2)$ are significant in large systems.
- **Basis sets have known pathologies.** Superposition error in weakly bound complexes, near-linear dependence in diffuse sets, and the difference between Cartesian and spherical $d$ functions all affect results in ways that should be recognized.

## Where it is used later

- [[basis-orthogonalization|Canonical orthogonalization]] handles near-linear dependence (Chapter 3).
- [[basis-set-superposition-error|Basis-set superposition error]] (Chapter 14).
- [[coulomb-cusp-and-helium-expansions|The Coulomb cusp]] and slow correlation convergence (Chapter 9).
- [[derivative-integrals-and-u-matrices|Derivative integrals]] for analytic gradients (Chapter 15).

## The main ideas, in order

1. **Gaussian functions and contraction.** STO-$n$G fits, and the Pople family (STO-3G, 4-31G, 6-31G\*, 6-31G\*\*).
2. **Angular and radial parts.** Solid harmonics for the angular part. For the radial part, the requirements a good basis must meet: systematic completeness, fast convergence, easy integrals.
3. **Convergence.** Even-tempered and correlation-consistent ideas, and Hartree–Fock trends across bases for small molecules.
4. **Integrals.** Gaussian overlap distributions and the product rule; the Boys function; the McMurchie–Davidson, Obara–Saika and Rys schemes.
5. **Large systems.** Screening and multipole methods.

## How to read it

**Path.**

1. Gaussian functions and contracted Pople sets.
2. Angular (solid-harmonic) and radial parts.
3. Convergence of the energy with basis size, and HF trends across bases.
4. Integral evaluation: overlap distributions, the McMurchie-Davidson, Obara-Saika and Rys schemes for electron repulsion, and screening with multipoles.

**Needs.** Chapter 3. Basis-set convergence of correlation energies is taken up again in Chapter 9 (the cusp).

**Core (first pass).** [[gaussian-basis-functions]], [[pople-basis-sets]], [[hf-closed-shell-basis-set-trends]].

**Deep (second pass).** [[solid-harmonics-angular-basis]], [[radial-basis-functions-slater-and-gaussian]], [[gaussian-basis-sets-and-convergence]], [[gaussian-overlap-distributions-and-one-electron-integrals]], [[electron-repulsion-integrals-md-os-rys]], [[multipole-methods-and-integral-screening]].

**Planned sections:** Density fitting (RI) and Cholesky decomposition; Effective core potentials; Integral symmetries.
