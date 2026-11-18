---
id: heteronuclear-diatomic-molecular-orbitals
title: Molecular orbitals of heteronuclear diatomic molecules - CO, BF, HF and polarity
summary: Without inversion symmetry the g/u label disappears, and the MOs of CO are renumbered from those of isoelectronic N₂. The two-AO secular equation always gives one MO below both AO energies and one above. Which AOs contribute depends on how far apart the valence AO energies are (N₂ against CO against BF). The HF molecule is shown as a minimal-basis example (STO-3G coefficients agree with Ransil's minimal-STO values to 0.01), with covalent–ionic VB resonance and why NaCl dissociates to atoms. Checked numerically - near-Hartree–Fock dipoles are good for LiH (6.00 D) but give CO the wrong polarity (0.27 D, C⁺O⁻), which CCSD(T) reverses to 0.13 D C⁻O⁺.
status: in-progress
kind: theory
level: introductory
tags: [molecular-orbitals, heteronuclear, co, hydrogen-fluoride, dipole-moment, ionic-covalent, electronegativity]
prerequisites: [homonuclear-diatomic-molecular-orbitals]
related: [diatomic-electronic-terms, mo-and-valence-bond-theories, population-analysis, bond-orders-and-atomic-charges, hjo-calibration-structures-and-dipoles]
order: 30
date: 2026-11-18
---

## Labels without inversion symmetry

When the nuclei differ, $\hat H$ no longer commutes with inversion and the g/u label disappears. The MOs of each $\lambda$ are numbered in order of energy. For CO, isoelectronic with N₂, the correspondence is

| N₂ | $1\sigma_g$ | $1\sigma_u$ | $2\sigma_g$ | $2\sigma_u$ | $1\pi_u$ | $3\sigma_g$ | $1\pi_g$ | $3\sigma_u$ |
|---|---|---|---|---|---|---|---|---|
| CO | $1\sigma$ | $2\sigma$ | $3\sigma$ | $4\sigma$ | $1\pi$ | $5\sigma$ | $2\pi$ | $6\sigma$ |

CO's ground configuration is $1\sigma^22\sigma^23\sigma^24\sigma^21\pi^45\sigma^2$. Here $1\sigma$ is essentially O 1s and $2\sigma$ C 1s.

!!! example "Where the CO HOMO lives"
    RHF/cc-pVTZ at $R_e$ = 1.1283 Å puts the $5\sigma$ HOMO at $-0.554\,E_h$, with 93% of its Mulliken population on carbon: largely a carbon lone pair.

## The two-orbital model

Take one AO on each atom, $\phi_a$ and $\phi_b$, with energies $H_{aa} > H_{bb}$ (so $b$ is on the more electronegative atom), coupling $H_{ab}$ and overlap $S_{ab}$. The secular equation is

$$
f(W) \equiv (H_{aa} - W)(H_{bb} - W) - (H_{ab} - WS_{ab})^2 = 0 .
$$

- **The roots straddle both AO energies.** The coefficient of $W^2$ is $1 - S_{ab}^2 > 0$, so $f(\pm\infty) = +\infty$. At $W = H_{aa}$ and at $W = H_{bb}$ the first product vanishes, so $f < 0$ there. By continuity one root lies below $H_{bb}$ and the other above $H_{aa}$: one bonding MO below both AOs and one antibonding MO above both.
- **Composition.** The bonding MO $c_1\phi_a + c_2\phi_b$ has $c_2 > c_1 > 0$ and is concentrated on the more electronegative atom. The antibonding MO has coefficients of opposite sign and is concentrated on the other atom.
- **Limit of a large energy difference.** The further apart $H_{aa}$ and $H_{bb}$ lie, the less the AOs mix, and the bond becomes ionic.

!!! example "The rule on a real Fock matrix"
    For HF/STO-3G, the H 1s / F 2p$_z$ block of the converged Fock matrix has diagonal elements −0.603 and −0.365 $E_h$. Its generalized eigenvalues are −0.807 and +0.168 $E_h$: one below both, one above both.

This picture is crude for molecules with $s$ and $p$ valence AOs. If the valence AOs of the two atoms are close in energy (CO), the homonuclear pattern of MOs survives, with each AO of the more electronegative atom shifted down. If they are far apart, AOs mix across the usual $s$/$p$ boundaries.

- **BF.** In a minimal basis, the $4\sigma$ MO is mainly F 2p$\sigma$ with substantial B 2s and F 2s.
- **BF's $5\sigma$** is mainly B 2s with B and F 2p$\sigma$ admixture.
- **Contrast with N₂.** In N₂ the corresponding MOs are built mainly from 2s and from 2p$\sigma$ respectively.
- **What survives.** The valence $\sigma$/$\pi$ sequence $\sigma < \sigma < \pi < \sigma < \pi < \sigma$ usually still holds and gives plausible ground terms, even though the AO make-up of each MO is hard to guess.

## Diatomic hydrides: HF

H has only a 1s valence AO, so only $\sigma$ MOs involve hydrogen. The F 2p$\pi$ pair has no partner and becomes the nonbonding $1\pi$ (lone pairs). F 1s and 2s, far below H 1s in energy, stay nearly atomic. The bond is the $3\sigma$ MO, a polar combination of H 1s and F 2p$\sigma$. The configuration is $1\sigma^22\sigma^23\sigma^21\pi^4$.

!!! example "HF, minimal basis"
    RHF/STO-3G at R = 0.9168 Å. The F 2s is Schmidt-orthogonalized to 1s, $2s^\# = (2s - S\,1s)/\sqrt{1-S^2}$, and $2p\sigma$ points toward H. Ransil's values are from a minimal Slater basis with optimized exponents.

    | MO | $\varepsilon$ ($E_h$) | F 1s | F 2s$^\#$ | F 2p$\sigma$ | H 1s | Ransil |
    |---|---:|---:|---:|---:|---:|---|
    | $1\sigma$ | −25.900 | 1.000 | 0.022 | 0.003 | −0.006 | 1.000, 0.012, 0.002, −0.003 |
    | $2\sigma$ | −1.471 | −0.026 | 0.909 | 0.090 | 0.158 | −0.018, 0.914, 0.090, 0.154 |
    | $3\sigma$ | −0.585 | −0.021 | −0.422 | 0.702 | 0.521 | −0.023, −0.411, 0.711, 0.516 |
    | $1\pi$ | −0.464 | | | (pure F 2p$\pi$) | | |

    The bonding $3\sigma$ is not a two-AO MO: F 2s contributes substantially. The Mulliken charges are H +0.21 and F −0.21.

**VB description.** The covalent Heitler–London function pairs H 1s with F 2p$\sigma$,

$$
\Phi_{\text{cov}} = |\cdots 1s_\text{H}\overline{2p\sigma_\text{F}}| - |\cdots \overline{1s_\text{H}}2p\sigma_\text{F}| .
$$

The ionic structure H⁺F⁻ is $\Phi_{\text{ion}} = |\cdots 2p\sigma_\text{F}\overline{2p\sigma_\text{F}}|$, and the trial function $c_1\Phi_{\text{cov}} + c_2\Phi_{\text{ion}}$ ("ionic–covalent resonance") is optimized variationally. H⁻F⁺ contributes little.

**Highly ionic molecules still dissociate to atoms.** For NaCl the Na ionization energy (5.1 eV) exceeds the Cl electron affinity (3.6 eV), so Na + Cl lies below Na⁺ + Cl⁻ in the gas phase. As $R$ grows, $c_2/c_1$ must fall to zero, and the molecule turns covalent where the Coulomb attraction drops below 1.5 eV. Even Cs (IE 3.9 eV) and Cl (EA 3.6 eV, the largest) do not reverse this. Only if the nuclei separate faster than the electrons can follow do ions result.

## Accuracy of SCF dipole moments

One-electron properties such as the dipole moment are usually good at the Hartree–Fock limit (typical error about 0.2 D) but fail when the moment is small.

!!! example "LiH and CO dipoles"
    | | HF/aug-cc-pVQZ | Levine (near-HF) | CCSD(T)/aug-cc-pVTZ (finite field) | Experiment (Levine) |
    |---|---:|---:|---:|---:|
    | LiH (R = 1.5949 Å) | 6.00 D, Li⁺H⁻ | 6.00 D | | 5.83 D |
    | CO (R = 1.1283 Å) | 0.27 D, **C⁺O⁻** | 0.27 D, C⁺O⁻ | 0.13 D, C⁻O⁺ | 0.11 D, C⁻O⁺ |

    The near-HF CO moment points the wrong way, and correlation is needed to reverse it. Levine quotes a CI value of 0.12 D with the correct polarity. Here the finite-field CCSD(T) dipole is $-\partial E/\partial F$ from $\pm 5\times10^{-4}$ au fields. HF/aug-cc-pVTZ gives 0.267 D, C⁺O⁻, on the same footing (0.266 D with aug-cc-pVQZ), so the basis is converged for HF.

Hartree–Fock dissociation energies are far worse: about 5.3 eV for N₂ against 9.9 eV (Levine).

## Valence-electron approximation

For heavy molecules one treats only the valence electrons. The core is replaced either by point charges with the valence orbitals constrained orthogonal to core orbitals (otherwise they collapse into the core), or by an effective repulsive potential. The approximation is widely used in approximate treatments of polyatomic molecules.

## Source

Levine, *Quantum Chemistry* (7th ed., Pearson, 2014), Sec. 13.14, pp. 390-393 (minimal and extended STO bases, orthogonalized 2s, Eq. (13.124); dipole accuracy, LiH 6.00/5.83 D, CO 0.27 D C⁺O⁻ versus 0.11 D C⁻O⁺ and CI 0.12 D; N₂ HF $D_e$); Sec. 13.15, pp. 393-396 (N₂/CO correspondence, Ransil's CO, BF and HF minimal-basis MOs, two-AO secular equation (13.125) and Fig. 13.22); Sec. 13.16, p. 396 (VB of HF, Eqs. (13.126)-(13.127), NaCl and CsCl dissociation); Sec. 13.17, pp. 396-397 (valence-electron approximation). Calculations in `part3_batchC.py`, section C (PySCF 2.15.1).
