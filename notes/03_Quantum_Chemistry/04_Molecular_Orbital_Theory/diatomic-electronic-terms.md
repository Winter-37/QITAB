---
id: diatomic-electronic-terms
title: Electronic terms of diatomic molecules - Λ, S, Σ⁺/Σ⁻, g/u, and multiplet levels
summary: How a diatomic electron configuration gives term symbols ^{2S+1}Λ^{±}_{g/u}. M_L adds algebraically, not vectorially, so πδ gives Π and Φ but no Δ. Filled shells contribute ¹Σ⁺, nonequivalent and equivalent electrons are treated separately, and the ± label is the reflection eigenvalue in a plane containing the axis. Spin–orbit levels are labelled by Λ+Σ and Ω. A determinant-based program reproduces every entry of Levine's Table 13.3. For O₂ (π_g² gives ³Σ_g⁻, ¹Δ_g, ¹Σ_g⁺), SA-CASSCF/NEVPT2 vertical excitation energies are 0.96 and 1.78 eV, against the observed 0.98 and 1.6 eV.
status: in-progress
kind: theory
level: intermediate
tags: [term-symbols, diatomic-molecules, angular-momentum, spin, o2, singlet-oxygen, spectroscopy]
prerequisites: [homonuclear-diatomic-molecular-orbitals, periodic-table-and-term-symbols, addition-of-angular-momenta]
related: [heteronuclear-diatomic-molecular-orbitals, spin-orbitals-and-antisymmetry, mcscf-and-gvb]
order: 20
date: 2026-11-18
---

## Quantum numbers of a diatomic state

For a linear molecule, $\hat L^2$ does not commute with $\hat H$, but its component $\hat L_z$ along the axis does. So does $\hat S^2$ (spin–orbit coupling neglected). A state is labelled by

- $M_L$, eigenvalue of $\hat L_z/\hbar$, the **algebraic** sum of the electrons' $m$ values. The energy depends only on $M_L^2$. With $\Lambda \equiv |M_L|$, the code letters for $\Lambda = 0, 1, 2, 3, 4$ are $\Sigma, \Pi, \Delta, \Phi, \Gamma$. Every $\Lambda > 0$ level is doubly degenerate ($M_L = \pm\Lambda$).
- $S$, with multiplicity $2S+1$ written as a left superscript.
- For $\Sigma$ terms, a superscript + or − giving the eigenvalue of $\hat\sigma_v$, reflection in a plane containing the axis.
- For homonuclear molecules, a subscript g or u. The term is u if an odd number of electrons occupy u orbitals, otherwise g.

States from the same configuration with the same $\Lambda$ and $S$ form one **term**. Under Russell–Saunders coupling, each term $^{2S+1}\Lambda$ is $(2S+1)$-fold spin-degenerate times 2 if $\Lambda > 0$.

## Deriving the terms

1. **Filled shells.** A filled $\sigma$ shell ($\sigma^2$) or filled $\pi, \delta$ shell ($\pi^4$, $\delta^4$) has $M_L = 0$ and $M_S = 0$, so it contributes only $^1\Sigma^+$. Only electrons outside filled shells matter.
2. **One electron.** $\sigma \to {}^2\Sigma^+$, $\pi \to {}^2\Pi$, $\delta \to {}^2\Delta$. A single $\sigma$ electron has no $\phi$ dependence, so it is $\Sigma^+$.
3. **Nonequivalent electrons** (different shells) carry no Pauli restriction. Combine all $m$ values and both couplings of the spins.
    - $\sigma\sigma'$: $^1\Sigma^+, {}^3\Sigma^+$.
    - $\pi\delta$: $M_L = \pm3, \pm1$, giving $^{1,3}\Phi$ and $^{1,3}\Pi$.
    - $\pi\pi'$: $M_L = \pm2$ and twice 0, giving $^{1,3}\Delta$, $^{1,3}\Sigma^+$ and $^{1,3}\Sigma^-$.
4. **Equivalent electrons** (same shell). Pauli removes states. For $\pi^2$, four of the eight $\pi\pi'$ spatial–spin combinations vanish, leaving $^3\Sigma^-$, $^1\Delta$ and $^1\Sigma^+$. A shell more than half full gives the same terms as its holes: $\pi^3$ behaves as $\pi$, and $\pi^3\delta$ as $\pi\delta$.

**Why $\pi\pi'$ gives two $\Sigma$ terms of each multiplicity.** Write $p_{\pm1}$ and $p'_{\pm1}$ for the two shells. The $M_L = 0$ space is spanned by $p_{+1}(1)p'_{-1}(2)$, $p_{+1}(2)p'_{-1}(1)$, $p_{-1}(1)p'_{+1}(2)$ and $p_{-1}(2)p'_{+1}(1)$. With $\hat\sigma_v p_{\pm1} = p_{\mp1}$, the four symmetric and antisymmetric combinations are:

- **Spatially symmetric** (go with the singlet spin function): $[p_{+1}p'_{-1}]_+ + [p_{-1}p'_{+1}]_+$ is $\Sigma^+$, and $[p_{+1}p'_{-1}]_+ - [p_{-1}p'_{+1}]_+$ is $\Sigma^-$.
- **Spatially antisymmetric** (go with the triplet): $[\,]_-+[\,]_-$ and $[\,]_- - [\,]_-$, again one $\Sigma^+$ and one $\Sigma^-$.

Here $[ab]_\pm = a(1)b(2) \pm a(2)b(1)$.

**The rule of thumb.** Hund's rule picks the highest multiplicity as the ground term in most cases: B₂ and O₂ ($\pi^2$ and $\pi_g^2$) are $^3\Sigma_g^-$. Most stable diatomics, however, have a $^1\Sigma^+$ ground term. Exceptions include B₂, Al₂, Si₂, O₂ and NO ($^2\Pi$).

## Multiplet levels

Spin–orbit coupling splits a term with $\Lambda > 0$. The axial spin projection $M_S\hbar$ is written $\Sigma$ (not the term letter). The levels are labelled by $\Lambda + \Sigma$, a right subscript running from $\Lambda + S$ down to $\Lambda - S$, and $\Omega \equiv |\Lambda + \Sigma|$.

- **Example.** $^3\Delta$ has levels $^3\Delta_3$, $^3\Delta_2$ and $^3\Delta_1$; $^4\Pi$ has $\Lambda + \Sigma = \tfrac52, \tfrac32, \tfrac12, -\tfrac12$.
- **Splitting.** The spin–orbit energy is approximately $A\Lambda\Sigma$, so the multiplet spacing is constant. It is regular for $A > 0$ and inverted for $A < 0$.
- **Multiplicity counts the levels.** For $\Lambda > 0$, the number of levels always equals $2S + 1$ (not always true in atoms). Each level stays doubly degenerate until $\Lambda$-type doubling, a coupling to molecular rotation, splits it.
- **Σ terms.** For $\Lambda = 0$ the first-order splitting vanishes and $\Omega$ is not used.

**Spectroscopic letters.** The ground term is prefixed X. Excited terms of the same multiplicity are A, B, C, …; those of different multiplicity are a, b, c, …. So O₂ has X$^3\Sigma_g^-$, a$^1\Delta_g$ and b$^1\Sigma_g^+$.

!!! example "Levine's Table 13.3, generated by counting determinants"
    **Method.** A program builds every Slater determinant of the open shells from complex orbitals $(m, m_s)$. It diagonalizes $\hat S^2 = \hat S_-\hat S_+ + \hat S_z^2 + \hat S_z\hbar$ in each $(M_L, M_S)$ block. In the $M_L = 0$ block it diagonalizes $\hat\sigma_v$ (which maps $m \to -m$ and reorders the determinant) within each spin eigenspace.

    It returns, matching Table 13.3 entry for entry:

    | Configuration | Terms |
    |---|---|
    | $\sigma$; $\sigma^2$, $\pi^4$ | $^2\Sigma^+$; $^1\Sigma^+$ |
    | $\pi$, $\pi^3$; $\delta^3$ | $^2\Pi$; $^2\Delta$ |
    | $\pi^2$ | $^3\Sigma^-$, $^1\Delta$, $^1\Sigma^+$ |
    | $\delta^2$ | $^3\Sigma^-$, $^1\Gamma$, $^1\Sigma^+$ |
    | $\sigma\sigma'$ | $^1\Sigma^+$, $^3\Sigma^+$ |
    | $\sigma\pi$ | $^1\Pi$, $^3\Pi$ |
    | $\pi\pi'$, $\pi\pi'^3$ | $^{1,3}\Sigma^+$, $^{1,3}\Sigma^-$, $^{1,3}\Delta$ |
    | $\pi\delta$, $\pi^3\delta$ | $^{1,3}\Pi$, $^{1,3}\Phi$ |

    Parities come out as stated by the g/u rule, for example $\pi_u^2 \to {}^3\Sigma_g^-, {}^1\Delta_g, {}^1\Sigma_g^+$.

!!! example "The three lowest states of O₂"
    **Method.** The ground configuration … $1\pi_g^2$ gives X$^3\Sigma_g^-$, a$^1\Delta_g$ and b$^1\Sigma_g^+$. The calculation uses R = 1.2075 Å, cc-pVTZ and a CAS(8,6) active space (the $3\sigma_g$, $1\pi_u$ and $1\pi_g$ shells plus the lowest virtual orbital; the shells up to $2\sigma_u$ stay doubly occupied). Orbitals are state-averaged over the three terms (both components of $^1\Delta_g$), followed by NEVPT2 for each state.

    | State | SA-CASSCF (eV) | NEVPT2 (eV) | Levine ($v = 0$ levels, eV) |
    |---|---:|---:|---:|
    | X$^3\Sigma_g^-$ | 0 | 0 | 0 |
    | a$^1\Delta_g$ | 0.905 | 0.963 | 0.98 |
    | b$^1\Sigma_g^+$ | 1.683 | 1.779 | 1.6 |

    - **Symmetry checks.** The two components of $^1\Delta_g$ fall in different D$_{2h}$ irreps ($A_g$ and $B_{1g}$) and come out degenerate to $4\times10^{-8}\,E_h$.
    - **Vertical versus $v = 0$.** The computed numbers are vertical (at the X-state bond length), the experimental ones refer to $v = 0$ levels, and the excited states have slightly longer bonds. The 0.18 eV gap for the b state is therefore not all method error.
    - **Hund's rule** holds here: the triplet is lowest. Singlet oxygen is an intermediate in many organic, biochemical and inorganic reactions.

## Source

Levine, *Quantum Chemistry* (7th ed., Pearson, 2014), Sec. 13.8, pp. 375-379: $\Lambda$, $M_L$ and the code letters, Eq. (13.84); filled shells; nonequivalent electrons and the $\pi\pi'$ spatial functions, Eqs. (13.85)-(13.89); $\Sigma^\pm$ and $\Lambda$-type doubling; equivalent electrons and Table 13.3; g/u rule; O₂ terms and the 0.98 and 1.6 eV levels; ground-term exceptions; X/A/a notation; spin–orbit levels, $\Omega$, Eq. (13.90). Calculations in `part3_batchC.py`, section B (term generator; PySCF SA-CASSCF and NEVPT2).
