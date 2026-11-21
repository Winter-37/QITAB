---
id: hydrogen-molecule-heitler-london
title: The hydrogen molecule in the Heitler-London approximation
summary: The two-electron covalent bond. One electron is assigned to each proton and the product is symmetrized (singlet) or antisymmetrized (triplet). The energy is −1 E_h plus (Q ± A)/(1 ± S²), with a Coulomb term Q and an exchange term A built from four integrals in closed form. The singlet binds, with a minimum at 1.64 a0 and 3.16 eV against 1.40 a0 and 4.75 eV; the triplet is repulsive at every separation. Scaling the exponent gives 1.41 a0 and 3.79 eV. The function dissociates correctly into two atoms.
status: in-progress
kind: derivation
level: intermediate
tags: [hydrogen-molecule, heitler-london, valence-bond, covalent-bond, exchange-integral, singlet-triplet, variational-principle, dissociation, griffiths]
prerequisites: [hydrogen-molecule-ion-variational, exchange-symmetry-spin-and-symmetrization-principle, variational-principle]
related: [bosons-fermions-and-exchange-forces, minimal-basis-h2-model, h2-dissociation-rhf-uhf, mcscf-and-gvb, standard-models-h2-and-water, helium-ground-state-variational]
conventions: [chemists-integrals]
order: 70
date: 2026-11-14
---

## Setup

Two protons $a$ and $b$ are clamped a distance $R$ apart. In atomic units

$$
H = h(1) + h(2) + \frac1{r_{12}} + \frac1R ,\qquad
h = -\tfrac12\nabla^2 - \frac1{r_a} - \frac1{r_b} .
$$

The reference energy is that of two separated hydrogen atoms, $-1\ E_h$. Let $\phi_a$ and $\phi_b$ be 1s functions on the two protons, as in [[hydrogen-molecule-ion-variational]], with overlap $S = \langle\phi_a|\phi_b\rangle = e^{-R}(1 + R + R^2/3)$.

## Trial functions

Assign one electron to each proton and impose exchange symmetry ([[exchange-symmetry-spin-and-symmetrization-principle]]):

$$
\psi_\pm(\mathbf r_1,\mathbf r_2) = \frac{\phi_a(1)\phi_b(2) \pm \phi_b(1)\phi_a(2)}{\sqrt{2(1\pm S^2)}} .
$$

The total wave function of two electrons is antisymmetric, so the symmetric $\psi_+$ goes with the spin singlet and the antisymmetric $\psi_-$ with the triplet. The Hamiltonian contains no spin, yet the energy depends on the total spin through the symmetry of the spatial function. This trial function is the Heitler-London, or valence-bond, function. It contains no terms with both electrons on the same proton.

## Energy

Two matrix elements are needed. Because $h\phi_a = (-\tfrac12 - 1/r_b)\phi_a$,

$$
\langle\phi_a|h|\phi_a\rangle = -\tfrac12 - D ,\qquad \langle\phi_a|h|\phi_b\rangle = -\tfrac12S - X ,
$$

with $D = 1/R - (1 + 1/R)e^{-2R}$ and $X = (1 + R)e^{-R}$ from the H₂⁺ calculation. The electron repulsion contributes two two-electron integrals, written in charge-cloud notation as

$$
J = (aa|bb) = \int\!\!\int\frac{\phi_a^2(1)\,\phi_b^2(2)}{r_{12}}\,d^3r_1d^3r_2 ,
\qquad
K = (ab|ab) = \int\!\!\int\frac{\phi_a(1)\phi_b(1)\,\phi_a(2)\phi_b(2)}{r_{12}}\,d^3r_1d^3r_2 .
$$

$J$ is the repulsion of the two atomic charge clouds and $K$ the self-repulsion of the overlap density. Then

$$
\langle\phi_a\phi_b|H|\phi_a\phi_b\rangle = -1 + Q ,\qquad
\langle\phi_a\phi_b|H|\phi_b\phi_a\rangle = -S^2 + A ,
$$

$$
Q = -2D + J + \frac1R ,\qquad A = -2SX + K + \frac{S^2}{R} ,
$$

and

$$
\boxed{\,E_\pm(R) = -1 + \frac{Q \pm A}{1 \pm S^2}\,}
$$

- $Q$, the **Coulomb term**, is the classical electrostatic interaction of two undistorted atoms: electron-proton attraction across the bond, cloud-cloud repulsion and proton-proton repulsion. It nearly cancels, staying below 0.02 $E_h$ in magnitude for $R\geq1.4\,a_0$.
- $A$, the **exchange term**, exists only because the function is symmetrized. It is negative, dominated by $-2SX$, the attraction of the overlap density to the protons. The bond is almost entirely an exchange effect: $A$ lowers the singlet and raises the triplet. This is the "exchange force" of [[bosons-fermions-and-exchange-forces]] in a real system.

The integrals $J$ and $K$ have closed forms,

$$
J = \frac1R - e^{-2R}\Big(\frac1R + \frac{11}{8} + \frac{3R}{4} + \frac{R^2}{6}\Big) ,
$$

$$
K = \frac15\Big[-e^{-2R}\Big(-\frac{25}{8} + \frac{23R}{4} + 3R^2 + \frac{R^3}{3}\Big)
+ \frac6R\Big(S^2(\gamma + \ln R) + S'^2\,\mathrm{Ei}(-4R) - 2SS'\,\mathrm{Ei}(-2R)\Big)\Big] ,
$$

where $S' = e^{R}(1 - R + R^2/3)$, $\gamma$ is Euler's constant and $\mathrm{Ei}$ is the exponential integral. Griffiths defines the corresponding direct and exchange integrals $D_2$ and $X_2$ and leaves their evaluation to a problem. The two formulas above are standard results quoted from memory; both were checked numerically (see the example).

## Results

- **Singlet.** $E_+$ has a minimum at $R = 1.64\,a_0$ with $E_+ = -1.1160\ E_h$, a binding energy of 3.16 eV. The measured values are $1.40\,a_0$ and 4.75 eV.
- **Triplet.** $E_-$ decreases monotonically with $R$ and lies above $-1$ everywhere. Two hydrogen atoms with parallel spins repel.
- **Dissociation.** As $R\to\infty$, $S$, $Q$ and $A$ vanish and both curves tend to $-1\ E_h$, two neutral atoms. The molecular-orbital (restricted Hartree-Fock) function does not have this property, because it contains ionic terms H⁺H⁻ with weight one half at every $R$ ([[h2-dissociation-rhf-uhf]]).

**Scaling.** With 1s exponent $\zeta$ in both orbitals, the minimum moves to $R = 1.414\,a_0$, $\zeta = 1.166$, $E_+ = -1.1391\ E_h$: the bond length is nearly right and the binding energy rises to 3.79 eV. The orbitals contract in the molecule, as they did in H₂⁺.

**Relation to other functions.** The molecular-orbital function $\sigma_g(1)\sigma_g(2)$ is the Heitler-London function plus an equal amount of the ionic function $\phi_a\phi_a + \phi_b\phi_b$. Letting the covalent-ionic ratio vary gives the full-CI function of the minimal basis ([[minimal-basis-h2-model]]); the generalized valence-bond function of [[mcscf-and-gvb]] is the same idea with optimized orbitals. Missing altogether at large $R$ is the dispersion attraction, which falls as $R^{-6}$ and needs excited atomic states.

!!! example "The curves in numbers"

    Unit exponent, energies in $E_h$.

    | $R/a_0$ | $S^2$ | $Q$ | $A$ | $E_+$ (singlet) | $E_-$ (triplet) | $E_+$, optimal $\zeta$ |
    |---|---|---|---|---|---|---|
    | 1.0 | 0.73683 | $+0.09586$ | $-0.08965$ | $-0.99642$ | $-0.29509$ | $-1.08859$ ($\zeta = 1.286$) |
    | 1.4 | 0.56692 | $-0.00227$ | $-0.16300$ | $-1.10547$ | $-0.62888$ | $-1.13905$ (1.169) |
    | 1.6425 | 0.46966 | $-0.01676$ | $-0.15368$ | $-1.11597$ | $-0.74184$ | $-1.13230$ (1.118) |
    | 2.0 | 0.34393 | $-0.01908$ | $-0.12009$ | $-1.10355$ | $-0.84604$ | $-1.10804$ (1.062) |
    | 3.0 | 0.12146 | $-0.00692$ | $-0.03982$ | $-1.04167$ | $-0.96256$ | $-1.04170$ (0.995) |
    | 4.0 | 0.03582 | $-0.00161$ | $-0.01008$ | $-1.01129$ | $-0.99121$ | $-1.01136$ (0.992) |
    | 6.0 | 0.00222 | $-0.00006$ | $-0.00045$ | $-1.00051$ | $-0.99961$ | $-1.00051$ (0.999) |

    | Function | $R_e/a_0$ | $E(R_e)$ | $D_e$ (eV) |
    |---|---|---|---|
    | Heitler-London, $\zeta = 1$ | 1.643 | $-1.11597$ | 3.16 |
    | Heitler-London, $\zeta = 1.166$ | 1.414 | $-1.13908$ | 3.79 |
    | Measured | 1.40 | | 4.75 |

    At $R = 1.4\,a_0$ the scaled Heitler-London energy, $-1.1391$, is already below the Hartree-Fock energy in a large basis, $-1.1335$, and 35 m$E_h$ above the full-CI value $-1.1738$ (both cc-pVQZ numbers from [[standard-models-h2-and-water]]). A two-determinant valence-bond function with one parameter beats the best single determinant.

    **Check of the integrals.** At $R = 1.4$ the formulas give $S = 0.752943$, $J = 0.503521$, $K = 0.323291$. An independent evaluation, with each 1s function replaced by a least-squares fit of 14 even-tempered Gaussians and the integrals taken from PySCF, gives $0.752926$, $0.503532$, $0.323292$; the one-electron elements agree to $10^{-5}$ as well.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 8.4, Eqs. (8.54)-(8.69), Figs. 8.8 and 8.9 (described); Problems 8.12-8.14. Page numbers are not given because the PDF used is an e-book rendering without print pagination. Griffiths reports a bond length of 1.64 Bohr radii and a binding energy of 3.15 eV, and quotes 1.40 Bohr radii and 4.75 eV as measured.

Sakurai has no section on the hydrogen molecule, so the note rests on Griffiths.

The split into $Q$ and $A$ follows the usual valence-bond convention instead of Griffiths' notation. The closed forms for $J$ and $K$ are standard results quoted from memory (original references to verify); their numerical check, the scaled-exponent results and all tables are computed in `griffiths/ch08_variational.py`.

Companion reading in Levine, *Quantum Chemistry* (7th ed., Pearson, 2014): Sec. 13.10, pp. 382-384 (the valence-bond treatment of H₂); comparison with MO theory in [[mo-and-valence-bond-theories]].
