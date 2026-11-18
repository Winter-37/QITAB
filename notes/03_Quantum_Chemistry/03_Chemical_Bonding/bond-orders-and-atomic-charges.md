---
id: bond-orders-and-atomic-charges
title: Bond orders, atomic charges and the molecular electrostatic potential
summary: Reading bonding from an SCF density matrix. Covers Mulliken net, overlap and gross populations, overlap populations as a bonding/antibonding test, and Mayer bond orders. Also the molecular electrostatic potential (MEP) and charge schemes beyond Mulliken - ESP-fitted, Hirshfeld, NPA, AIM, CM5. Checked - Levine's (CCCBDB) table of Mulliken H charges in CH₄, NH₃, H₂O and HF is reproduced for four basis sets. HF/6-31G* Mayer bond orders are 2.80 (N₂), 1.98 (C₂H₄), 1.45 (benzene) and 0.97 (C₂H₆). For water from STO-3G to aug-cc-pVTZ, Mulliken and Löwdin O charges wander by 0.4-1.8 e, ESP charges by 0.08 e and Hirshfeld charges by 0.015 e.
status: in-progress
kind: theory
level: intermediate
tags: [population-analysis, bond-order, mayer, atomic-charges, electrostatic-potential, hirshfeld, esp-charges, mulliken]
prerequisites: [population-analysis, molecular-orbitals-of-polyatomic-molecules]
related: [localized-molecular-orbitals, huckel-molecular-orbital-theory, one-particle-rdm, heteronuclear-diatomic-molecular-orbitals]
order: 40
date: 2026-11-18
---

Closed-shell SCF, real orbitals $\phi_i = \sum_r c_{ri}\chi_r$ with occupations $n_i$. $\mathbf P$ is the AO density matrix, $P_{rs} = \sum_i n_ic_{ri}c_{si}$, $\mathbf S$ the overlap matrix and $A, B$ atoms. The definitions of net, overlap and gross Mulliken populations and of Löwdin populations are in [[population-analysis]]; here they are used to read bonding.

## Populations as a bonding test

Integrating $|\phi_i|^2$ splits one electron into net populations $c_{ri}^2$ and overlap populations $2c_{ri}c_{si}S_{rs}$. For one MO, the **interatomic overlap population**,

$$
n_{\text{inter}}(i) = n_i\sum_{r\in A}\sum_{s\in B\ne A}2c_{ri}c_{si}S_{rs}\quad(\text{summed over atom pairs}),
$$

is substantially positive for a bonding MO, negative for an antibonding one, and near zero for a nonbonding one. In water ([[molecular-orbitals-of-polyatomic-molecules]]) it is +0.55 ($2a_1$), +0.47 ($1b_2$), −0.06 ($3a_1$) and 0 ($1b_1$) at STO-3G, against Pitzer–Merrifield's 0.53, 0.50, −0.03 and 0. So $3a_1$ is a lone pair despite its partial H character.

**Mayer bond order:**

$$
B_{AB} = \sum_{t\in A}\sum_{u\in B}(\mathbf P\mathbf S)_{tu}(\mathbf P\mathbf S)_{ut} ,
$$

It is usually close to the Lewis-structure bond order. Hückel's mobile bond order ([[huckel-molecular-orbital-theory]]) is the analogue for orthonormal $\pi$ AOs.

!!! example "Mayer bond orders, HF/6-31G* (6d)"
    | Molecule | Bond | $B_{AB}$ | Lewis |
    |---|---|---:|---:|
    | N₂ | N≡N | 2.80 | 3 |
    | CO | C≡O | 2.30 | 3 |
    | C₂H₄ | C=C | 1.98 | 2 |
    | C₆H₆ | C–C | 1.45 | 1.5 |
    | C₂H₆ | C–C | 0.97 | 1 |
    | C₂H₄, C₂H₆ | C–H | 0.96 | 1 |
    | H₂O | O–H | 0.79 | 1 |
    | H₂O | H···H | −0.004 | 0 |

    Nonpolar bonds come out near their formal orders. Polar bonds come out lower (C≡O, O–H): an electron pair shared unequally counts as less than a full bond.

## Atomic charges: no unique answer

There is no operator for "the charge on an atom", so every scheme is a convention.

**Mulliken charges** split each overlap population equally, $q_A = Z_A - \sum_{r\in A}(\mathbf P\mathbf S)_{rr}$. The equal split is arbitrary, and the results depend erratically on the basis set.

!!! example "Mulliken charge on H, HF at the optimized geometry of each basis"
    | Basis | CH₄ | NH₃ | H₂O | HF |
    |---|---:|---:|---:|---:|
    | STO-3G | 0.07 | 0.15 | 0.17 | 0.19 |
    | 3-21G | 0.20 | 0.29 | 0.37 | 0.45 |
    | 6-31G* | 0.17 | 0.33 | 0.43 | 0.52 |
    | 6-31G** | 0.12 | 0.26 | 0.34 | 0.39 |

    This reproduces Levine's CCCBDB table to 0.01. The single difference is CH₄ at 6-31G* (0.17 against 0.16). The match needs Cartesian (6d) $d$ functions for the 6-31G* sets; spherical $d$ shifts the polar molecules' charges by up to 0.02. Within one basis the ordering follows electronegativity (C < N < O < F). Across bases, the C–H bond at 3-21G looks more polar than the F–H bond at STO-3G.

**The molecular electrostatic potential** is a genuine observable:

$$
\phi(\mathbf r) = \sum_A\frac{Z_A}{|\mathbf r - \mathbf R_A|} - \int\frac{\rho(\mathbf r')}{|\mathbf r - \mathbf r'|}\,\mathrm d\mathbf r'
$$

(atomic units; chemists often quote $e N_A\phi$, the molar energy of a proton at $\mathbf r$).

- **Insensitivity.** It is only weakly sensitive to basis set and correlation, and is routinely computed at HF/6-31G* or DFT.
- **Sign.** It is positive inside a molecule (the nuclei dominate). It is negative outside lone pairs and $\pi$ clouds, which is where electrophiles attack, ignoring polarization.
- **Surfaces.** Mapped onto an isodensity surface ($\rho$ = 0.001 or 0.002 e/bohr³, comparable in area to the van der Waals surface), it is the molecular surface electrostatic potential used in modelling intermolecular interactions.

**Other charge schemes** (Levine Secs. 15.6-15.7):

- **ESP charges** (Merz–Singh–Kollman, CHELPG, RESP). Point charges on the nuclei, fitted by constrained least squares to $\phi$ on points outside the van der Waals surface. Charges of buried atoms are poorly determined.
- **Hirshfeld.** $\rho_A(\mathbf r) = \rho_{\text{mol}}(\mathbf r)\,\rho_A^0(\mathbf r)/\sum_B\rho_B^0(\mathbf r)$, sharing the density in proportion to free-atom densities placed at the nuclei. Iterative Hirshfeld-I improves it.
- **NPA.** Natural population analysis, from natural atomic orbitals. Much less basis-dependent than Mulliken.
- **AIM (Bader).** Space is divided by surfaces of zero flux in $\nabla\rho$. The charges are often criticized as too large.
- **CM1–CM5.** Mulliken, Löwdin or Hirshfeld charges corrected by a parametrized charge transfer fitted to experimental dipole moments.

!!! example "The charge on oxygen in water, six bases"
    RHF at the experimental geometry.

    - **ESP charges** use points on shells at 1.4, 1.6, 1.8 and 2.0 times the Bondi radii, about 1 point/Å², with a total-charge constraint.
    - **Hirshfeld charges** use spherically averaged free-atom RHF densities in the same basis.

    | Basis | Mulliken | Löwdin | Hirshfeld | ESP | $\mu$ (D) |
    |---|---:|---:|---:|---:|---:|
    | STO-3G | −0.37 | −0.25 | −0.24 | −0.62 | 1.73 |
    | 3-21G | −0.73 | −0.46 | −0.35 | −0.87 | 2.44 |
    | 6-31G* | −0.87 | −0.78 | −0.36 | −0.81 | 2.23 |
    | 6-31G** | −0.67 | −0.53 | −0.36 | −0.79 | 2.19 |
    | cc-pVTZ | −0.48 | +0.37 | −0.35 | −0.74 | 2.03 |
    | aug-cc-pVTZ | −0.44 | +1.03 | −0.34 | −0.73 | 1.98 |

    - **Spread.** From 6-31G* to aug-cc-pVTZ the O charge spreads by 0.43 (Mulliken), 1.82 (Löwdin), 0.015 (Hirshfeld) and 0.080 (ESP).
    - **Löwdin.** It is even less stable and gives a positive oxygen in the two largest bases.
    - **ESP.** It is fitted to the potential outside the molecule and tracks the dipole moment; the rms fit residual is 0.6-3 m$E_h$/e.
    - **Hirshfeld.** It is nearly basis-independent but gives small charges.
    - **Absolute values differ by a factor of two between schemes.** Compare charges only within one scheme and one basis.

## Source

Levine, *Quantum Chemistry* (7th ed., Pearson, 2014), Sec. 15.6, pp. 456-460 (Mulliken net, overlap and gross populations, Eqs. (15.24)-(15.25); the bonding test and the water overlap populations; Pitzer–Merrifield charges; the CCCBDB table of H charges; NPA and Löwdin; Mayer bond order, Eq. (15.26)); Sec. 15.7, pp. 460-464 (MEP, Eq. (15.28); isodensity and van der Waals surfaces; ESP, AIM, CM1-CM5 and Hirshfeld charges). Calculations in `part3_batchC.py`, section I (PySCF 2.15.1; geomeTRIC optimizations; own ESP fit and Hirshfeld partition).
