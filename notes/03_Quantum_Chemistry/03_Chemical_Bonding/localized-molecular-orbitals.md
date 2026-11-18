---
id: localized-molecular-orbitals
title: Localized molecular orbitals - bonds, lone pairs and hybrids from a delocalized determinant
summary: A closed-shell determinant is unchanged by any unitary mixing of its occupied orbitals, so canonical (delocalized, symmetry-adapted) and localized MOs describe the same wave function. Covers the Edmiston–Ruedenberg, Foster–Boys and Pipek–Mezey criteria, equivalent orbitals, and hybridization read from LMO coefficients. Checked - water ER LMOs in a minimal basis reproduce Liang–Taylor's expansion (0.05/0.57/0.71/0.42) and hybrid angles (94° and 123° against 95° and 122°). Also - methane C–H LMOs are sp^2.6; ER and Boys give two banana bonds in ethylene and three in N₂; the Pipek–Mezey functional is exactly flat under σ/π mixing in ethylene.
status: in-progress
kind: theory
level: intermediate
tags: [localized-orbitals, edmiston-ruedenberg, boys, pipek-mezey, hybridization, chemical-bond, banana-bonds, lone-pairs]
prerequisites: [molecular-orbitals-of-polyatomic-molecules, slater-determinants, rhf]
related: [bond-orders-and-atomic-charges, mo-and-valence-bond-theories, hartree-fock-csf-parametrization-and-canonical-conditions, unitary-matrices-exponential-logarithm]
conventions: [chemists-integrals]
order: 30
date: 2026-11-18
---

## The freedom in a closed-shell determinant

Let $\phi_1, \ldots, \phi_N$ be the doubly occupied orbitals of a closed-shell determinant, and let $\boldsymbol\phi' = \boldsymbol\phi\,\mathbf U$ with $\mathbf U$ unitary (applied to the $\alpha$ and $\beta$ columns alike). Then

$$
|\phi'_1\bar\phi'_1\cdots\phi'_N\bar\phi'_N| = (\det\mathbf U)^2\,|\phi_1\bar\phi_1\cdots\phi_N\bar\phi_N| ,
$$

a phase factor. The wave function, the density, the energy and every one-determinant property are unchanged. Levine shows the same thing by elementary column operations, which add multiples of one occupied orbital to another.

- **Canonical MOs.** Among all these equivalent sets, the canonical MOs are singled out by diagonalizing the matrix of Lagrange multipliers in $\hat F\phi_i = \sum_j \lambda_{ji}\phi_j$. They are eigenfunctions of $\hat F$, transform as symmetry species, and are delocalized ([[molecular-orbitals-of-polyatomic-molecules]]).
- **Localized MOs (LMOs).** Any other choice still satisfies the general HF equations. A localization criterion picks a set concentrated in bonds, lone pairs and cores.
- **Equivalent orbitals.** When a symmetry operation permutes equivalent bonds, the LMOs that are permuted by it are called equivalent orbitals.

**Localization criteria** (each a function of $\mathbf U$ alone):

| Criterion | Optimized quantity |
|---|---|
| Edmiston–Ruedenberg (energy localization) | minimize the interorbital repulsion $\sum_{i\ne j}(ii|jj)$, i.e. maximize the self-repulsion $\sum_i (ii|ii)$ |
| Foster–Boys | maximize $\sum_{i<j}|\langle\mathbf r\rangle_i - \langle\mathbf r\rangle_j|^2$ between orbital centroids, i.e. minimize the total spread $\sum_i(\langle r^2\rangle_i - \langle\mathbf r\rangle_i^2)$ |
| Pipek–Mezey | maximize $\sum_i\sum_A (q_A^{\,i})^2$, the squared Mulliken populations of each orbital on each atom |

For symmetric molecules the ER LMOs turn out to be equivalent orbitals, although this is not imposed. Boys is far cheaper and usually agrees with ER.

**Hybridization from an LMO.** A localized orbital containing $a\,(2s^\#) + d\,(2p_x) + e\,(2p_y) + f\,(2p_z)$ on one atom contains the hybrid $a\,2s^\# + (d^2 + e^2 + f^2)^{1/2}\,2p_{x'}$, where $x'$ has direction cosines $\propto(d, e, f)$. Its hybridization is $sp^n$ with

$$
n = \frac{d^2 + e^2 + f^2}{a^2} .
$$

!!! example "Water: canonical → localized (ER, minimal basis)"
    RHF/STO-3G at the experimental geometry, molecule in the $yz$ plane, O 2s orthogonalized to 1s.

    | LMO | $1a_1$ | $2a_1$ | $1b_2$ | $3a_1$ | $1b_1$ | Liang–Taylor |
    |---|---:|---:|---:|---:|---:|---|
    | $b(\text{OH}_1)$ | 0.04 | 0.57 | 0.71 | 0.42 | 0 | 0.05, 0.57, 0.71, 0.42, 0 |
    | $b(\text{OH}_2)$ | 0.04 | 0.57 | −0.71 | 0.42 | 0 | 0.05, 0.57, −0.71, 0.42, 0 |
    | $l_{1,2}(\text{O})$ | 0.08 | 0.41 | 0 | −0.57 | ∓0.71 | 0.08, 0.42, 0, −0.57, ∓0.71 |
    | $i(\text{O})$ | 0.99 | −0.12 | 0 | 0.06 | 0 | |

    - **Mixing.** The $1b_1$ lone pair and the bonding $1b_2$ are each split equally ($0.71 = 2^{-1/2}$). The bonding $2a_1$ also feeds the lone pairs, and the mostly lone-pair $3a_1$ also feeds the bonds.
    - **The bond LMO.** In AOs, $b(\text{OH}_1)$ = 0.52 H$_1$ − 0.11 H$_2$ + 0.24 O2s$^\#$ + 0.40 O2p$_z$ + 0.43 O2p$_y$ (Liang–Taylor: 0.50, −0.10, 0.25, 0.407, 0.441). It is mostly an O–H bond with a small tail toward H$_2$.
    - **Hybrid angles.** The O 2p hybrid in each bond LMO makes $\arctan(0.43/0.40)$ with the axis, so the two bond hybrids are 94° apart (Levine: 95°). The lone-pair hybrids are 123° apart (122°), above and below the molecular plane.
    - **Extended basis.** With cc-pVTZ, ER and Boys both put the bond-LMO centroids 101° apart as seen from O (HOH = 104.5°) and the lone-pair centroids 123° apart. Levine quotes von Niessen's extended-basis ER values of 103° and 114°. Those are defined by the line of maximum density rather than by centroids, so the definitions differ.

!!! example "Methane: equivalent sp³-like bonds"
    By symmetry each equivalent C–H LMO has the form $a(1a_1) + b(2a_1) + c\,3^{-1/2}(\pm1t_{2x}\pm1t_{2y}\pm1t_{2z})$ with $c = \tfrac12\sqrt3$. ER localization of the RHF/STO-3G determinant gives $|a| = 0.054$ and $|b| = 0.497$, with the $t_2$ weights summing to $c^2 = 0.750$. Pitzer's values are 0.055, 0.497 and $\tfrac12$ per $t_2$ component.

    In AOs the carbon part is 0.304 C2s$^\#$ + 0.495 C2p$'$. That makes it an sp$^{2.64}$ hybrid (Pitzer: sp$^{2.7}$), close to the textbook sp³. The four bonds come from localization, not from a bond-by-bond construction.

**Double and triple bonds.** In ethylene, $\sigma$ and $\pi$ are canonical MOs, and $b_\pm = 2^{-1/2}(b_\sigma \pm \pi)$ are an alternative equivalent pair: bent, or "banana", bonds above and below the plane. Both describe the same total density.

!!! example "Ethylene and N₂"
    **Ethylene.** RHF/STO-3G, molecule in the $xy$ plane; $\langle\phi|\hat\sigma_h|\phi\rangle$ is $+1$ for $\sigma$, $-1$ for $\pi$ and 0 for a banana bond.

    - **ER and Boys** give two C–C LMOs with $\langle\hat\sigma_h\rangle = 0$, i.e. two equivalent banana bonds, as Kaldor found.
    - **Pipek–Mezey** is exactly indifferent: the PM functional is 2.990180 for pure $\sigma + \pi$, for the 45° banana pair, and for the mixture actually returned. Its value changes by less than $10^{-11}$ along the whole $\sigma$–$\pi$ rotation. The $\sigma$ + $\pi$ answer Levine attributes to PM is one member of a degenerate family here, and which one a program returns depends on its starting orbitals.

    **N₂.** RHF/STO-3G, ER and Boys. Besides two 1s cores and two lone pairs, there are three bond LMOs whose centroids sit 0.56 bohr off the axis at the bond midpoint, 120.0° apart in azimuth. They are three equivalent banana bonds rather than one $\sigma$ and two $\pi$, as Edmiston and Ruedenberg found.

## What LMOs are good for

- **Transferability.** The C–H LMO of CH₄ is nearly the same in C₂H₆ and CH₃OH. Localized bonds explain why bond properties (energies, lengths, IR frequencies) transfer between molecules while canonical MOs do not.
- **Ground-state properties** (density, dipole, geometry, heat of formation) can be computed equally well from either set. **Ionization and excitation**, which involve an open-shell state, need the canonical description; open-shell orbitals do not localize this way.
- **Correlation.** Localized orbitals make correlation local and underlie low-scaling correlated methods for large molecules. They also explain why Hartree–Fock gets the ethane rotational barrier right: pair correlations within bonds hardly change on rotation.

## Source

Levine, *Quantum Chemistry* (7th ed., Pearson, 2014), Sec. 15.8, pp. 464-470: invariance of the determinant, Eqs. (15.29)-(15.33); canonical MOs and Lagrange multipliers, Eqs. (15.34)-(15.36); equivalent orbitals; the ER criterion, Eq. (15.37); Liang–Taylor water LMOs, Eqs. (15.38)-(15.41), angles 95° and 122°, von Niessen 96°/103° and 114°; N₂ banana bonds; transferability; Boys and Pipek–Mezey. Sec. 15.9, pp. 470-479: equivalent methane LMOs, Eqs. (15.47)-(15.62); hybridization, Eq. (15.63), sp$^{2.7}$; ethane barrier and correlation; ethylene $\sigma$–$\pi$ versus banana bonds and Kaldor's ER results. Calculations in `part3_batchC.py`, section H (PySCF `lo.EdmistonRuedenberg`, `lo.Boys`, `lo.PipekMezey`).
