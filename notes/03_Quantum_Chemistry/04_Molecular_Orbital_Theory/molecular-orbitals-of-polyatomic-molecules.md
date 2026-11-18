---
id: molecular-orbitals-of-polyatomic-molecules
title: Molecular orbitals of polyatomic molecules - symmetry orbitals, H₂O and CH₄
summary: Canonical MOs transform as irreducible representations of the point group. Building symmetry-adapted combinations of equivalent AOs block-diagonalizes the Roothaan equations, and only AOs of the same symmetry and similar energy mix. Worked in full for H₂O in a minimal basis (blocks of 4×4 a₁, 2×2 b₂ and 1×1 b₁; the bonding, lone-pair and core character of 1a₁ … 1b₁) and for CH₄ (a₁ and t₂ shells). STO-3G reproduces Pitzer–Merrifield's minimal-STO coefficients to about 0.02. Near-Hartree–Fock −ε of water are within 0.1 eV of Levine's values and 1-3 eV above the measured ionization energies.
status: in-progress
kind: theory
level: introductory
tags: [molecular-orbitals, symmetry-orbitals, point-groups, water, methane, ethylene, canonical-orbitals, koopmans]
prerequisites: [homonuclear-diatomic-molecular-orbitals, groups-representations-and-characters, rhf]
related: [localized-molecular-orbitals, bond-orders-and-atomic-charges, koopmans-theorem, population-analysis, huckel-molecular-orbital-theory]
order: 40
date: 2026-11-18
---

## Symmetry orbitals block-diagonalize the problem

The Fock operator commutes with every symmetry operation of the nuclear framework. Let $\chi_r$ and $\chi_s$ be eigenfunctions of a symmetry operator with different eigenvalues, so that they belong to different symmetry species. Then

$$
F_{rs} = \langle\chi_r|\hat F|\chi_s\rangle = 0,\qquad S_{rs} = \langle\chi_r|\chi_s\rangle = 0 ,
$$

by the theorem that matrix elements of an operator commuting with a Hermitian operator vanish between its eigenfunctions of different eigenvalue. For degenerate species (E, T) group theory gives the same conclusion. So:

1. Form **symmetry orbitals**: AOs that already transform as a species (AOs on an atom lying on every symmetry element), plus linear combinations of equivalent AOs that are permuted by the operations.
2. In this basis the secular determinant $\det(F_{rs} - \varepsilon S_{rs})$ breaks into one block per species.
3. Each canonical MO is a combination of symmetry orbitals of a single species and is labelled by it (lower case for orbitals, capitals for states).

**Rule of thumb for qualitative MO diagrams.** Only symmetry orbitals of the same species combine, and only AOs of comparable energy contribute appreciably to a given MO.

## Water

Water is in the $yz$ plane, with the $C_2$ axis along $z$ and the hydrogens on the $+z$ side. Point group $C_{2v}$; the minimal basis is O 1s, 2s, 2p$_{x,y,z}$ and H$_1$1s, H$_2$1s.

| Symmetry orbital | H$_1$1s + H$_2$1s | O1s | O2s | O2p$_z$ | H$_1$1s − H$_2$1s | O2p$_y$ | O2p$_x$ |
|---|---|---|---|---|---|---|---|
| Species | $a_1$ | $a_1$ | $a_1$ | $a_1$ | $b_2$ | $b_2$ | $b_1$ |

The 7×7 problem becomes a 4×4 $a_1$ block, a 2×2 $b_2$ block and a 1×1 $b_1$ block. Four MOs are $a_1$, two are $b_2$, and one, the O 2p$_x$ orbital itself, is $b_1$. The ground configuration is $(1a_1)^2(2a_1)^2(1b_2)^2(3a_1)^2(1b_1)^2$, a $^1A_1$ state.

!!! example "Canonical MOs of water, minimal basis"
    **Setup.** RHF/STO-3G at the experimental geometry (0.9578 Å, 104.5°), with the O 2s replaced by the orthogonalized $2s^\# = (2s - S\,1s)/\sqrt{1-S^2}$. In the symmetry-orbital basis the off-block elements of $\mathbf F$ and $\mathbf S$ vanish to $10^{-15}$.

    | MO | $\varepsilon$ ($E_h$) | O1s | O2s$^\#$ | O2p$_z$ | O2p$_y$ | H$_1$ | H$_2$ | interatomic overlap population |
    |---|---:|---:|---:|---:|---:|---:|---:|---:|
    | $1a_1$ | −20.242 | 1.000 | 0.026 | 0.004 | | −0.006 | −0.006 | −0.003 |
    | $2a_1$ | −1.268 | −0.035 | 0.810 | 0.129 | | 0.159 | 0.159 | 0.551 |
    | $1b_2$ | −0.618 | | | | 0.606 | 0.445 | −0.445 | 0.472 |
    | $3a_1$ | −0.453 | −0.024 | −0.521 | 0.777 | | 0.278 | 0.278 | −0.060 |
    | $1b_1$ | −0.391 | | | | (O2p$_x$ = 1) | | | 0.000 |

    **Comparison.** Pitzer and Merrifield's minimal Slater basis with optimized exponents gives $\varepsilon$ = −20.56, −1.28, −0.62, −0.47 and −0.40 $E_h$. Their coefficients are $2a_1$: −0.027, 0.820, 0.132, 0.152; $1b_2$: 0.624 and ±0.424; $3a_1$: −0.026, −0.502, 0.787, 0.264. The interatomic overlap populations are 0.53 ($2a_1$), 0.50 ($1b_2$) and −0.03 ($3a_1$) (Levine Sec. 15.6).

    **Character of each MO.**
    - $1a_1$ is the O 1s core.
    - $2a_1$ (O 2s with some 2p$_z$, in phase with both H) and $1b_2$ (O 2p$_y$ with H$_1$ − H$_2$) are the bonding MOs. Their interatomic overlap populations are large and positive.
    - In $3a_1$ the O 2s–2p$_z$ hybrid points away from the hydrogens. Its antibonding O 2s/H and bonding O 2p$_z$/H overlaps nearly cancel, so it is mainly a lone pair.
    - $1b_1$ is a pure O 2p$_x$ lone pair.

    The two bonding MOs are spread over the whole molecule. Neither is an O–H bond; [[localized-molecular-orbitals]] recovers the bonds by an orbital rotation that leaves the wave function unchanged.

**Virtual orbitals.** The unoccupied $4a_1$ and $2b_2$ have opposite-sign O and H coefficients and are antibonding. They are only rough models of the orbitals of excited states, since every orbital changes when the configuration changes.

!!! example "Orbital energies and ionization energies of water"
    | | $1a_1$ | $2a_1$ | $1b_2$ | $3a_1$ | $1b_1$ |
    |---|---:|---:|---:|---:|---:|
    | $-\varepsilon$, HF/aug-cc-pV5Z (eV) | 559.6 | 36.8 | 19.5 | 15.9 | 13.9 |
    | $-\varepsilon$, near-HF (Rosenberg–Shavitt, via Levine) | 559.5 | 36.7 | 19.5 | 15.9 | 13.8 |
    | vertical IP, experiment (Levine) | 539.7 | 32.2 | 18.5 | 14.7 | 12.6 |

    - **Agreement.** The large-basis orbital energies agree with Levine's near-HF values to 0.1 eV.
    - **Errors.** They overestimate every ionization energy: by 1.0-1.3 eV for the three outer valence levels, 4.6 eV for $2a_1$ and 20 eV for the core. Orbital relaxation on ionization, which Koopmans' theorem neglects, is largest for the core hole ([[koopmans-theorem]]).

## Methane

In $T_d$ the carbon 1s and 2s are $a_1$. The carbon 2p$_{x,y,z}$ transform like $x, y, z$ and form a triply degenerate $t_2$ set. With H$_1$…H$_4$ at $(q,q,q)$, $(q,-q,-q)$, $(-q,q,-q)$ and $(-q,-q,q)$, the hydrogen symmetry orbitals are

$$
a_1:\ \mathrm H_1 + \mathrm H_2 + \mathrm H_3 + \mathrm H_4 ;\qquad
t_2:\ \mathrm H_1 + \mathrm H_2 - \mathrm H_3 - \mathrm H_4,\ \ \mathrm H_1 - \mathrm H_2 + \mathrm H_3 - \mathrm H_4,\ \ \mathrm H_1 - \mathrm H_2 - \mathrm H_3 + \mathrm H_4 .
$$

The three $t_2$ combinations behave like $x$, $y$ and $z$ respectively. The ground configuration is $(1a_1)^2(2a_1)^2(1t_2)^6$, $^1A_1$.

!!! example "Canonical MOs of methane, minimal basis"
    RHF/STO-3G at $R$(CH) = 1.085 Å gives $\varepsilon$ = −11.03, −0.911 and −0.520 (×3) $E_h$; the $t_2$ level is degenerate to $10^{-15}$. Pitzer's optimized minimal STO basis gives −11.20, −0.93 and −0.54.

    - $2a_1$ = −0.065 C1s + 0.608 C2s$^\#$ + 0.181 (H$_1$+H$_2$+H$_3$+H$_4$). Pitzer: −0.064, 0.584, 0.186.
    - $1t_{2x}$ = 0.572 C2p$_x$ + 0.301 (H$_1$+H$_2$−H$_3$−H$_4$). Pitzer: 0.554, 0.318.

    **What it means.** There is one $a_1$ bonding level and one triply degenerate $t_2$ bonding level, not four equivalent C–H bond orbitals. The equivalent bonds come from localization (sp$^{2.6}$ hybrids, [[localized-molecular-orbitals]]).

## Planar molecules: σ and π

For a planar molecule every canonical MO is symmetric ($\sigma$) or antisymmetric ($\pi$) under reflection in the molecular plane. In ethylene ($D_{2h}$, eight one-dimensional species) the ground configuration is

$$
(1a_g)^2(1b_{1u})^2(2a_g)^2(2b_{1u})^2(1b_{2u})^2(3a_g)^2(1b_{3g})^2(1b_{3u})^2 ,
$$

with $1b_{3u}$, the C 2p$_\pi$ combination, the single occupied $\pi$ MO. This $\sigma$–$\pi$ separation is the basis of [[huckel-molecular-orbital-theory]]. For nonlinear molecules, unlike linear ones, $\sigma$/$\pi$ refers only to the reflection and has nothing to do with degeneracy or angular momentum.

## Source

Levine, *Quantum Chemistry* (7th ed., Pearson, 2014), Sec. 15.5, pp. 449-456 (symmetry orbitals of H₂O, Eqs. (15.13)-(15.16), block diagonalization; Pitzer–Merrifield minimal-STO MOs, Eqs. (15.18)-(15.22); Fig. 15.5; Koopmans' theorem and photoelectron ionization energies of water); Sec. 15.6, pp. 456-459 (interatomic overlap populations of the water MOs); Sec. 15.9, pp. 470-479 (methane symmetry functions, Eqs. (15.42)-(15.46), Pitzer's MOs; ethylene species and configuration, Table 15.3). Calculations in `part3_batchC.py`, section D (PySCF 2.15.1).
