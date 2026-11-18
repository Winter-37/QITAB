---
id: homonuclear-diatomic-molecular-orbitals
title: Molecular orbitals of homonuclear diatomic molecules - LCAO shapes, correlation diagram, configurations and bond orders
summary: H₂⁺-like LCAO molecular orbitals (σ_g1s, σ_u*1s, ..., π_u2p, σ_g2p, π_g*2p, σ_u*2p), their labels (λ, g/u, bonding/antibonding) and three naming schemes. The united-atom/separated-atom correlation diagram and the noncrossing rule, the filling order, and the ground configurations and bond orders of H₂ to Ne₂. Checked - the filling order reproduces every bond order in Levine's Table 13.2, which correlates with D_e (r = 0.97) and R_e (r = −0.82) for Li₂–Ne₂. The order of σ_g2p and π_u2p switches between N₂ and O₂; EOM-IP-CCSD confirms it, while Hartree–Fock orbital energies get it wrong for both N₂ and F₂.
status: in-progress
kind: theory
level: introductory
tags: [molecular-orbitals, lcao, diatomic-molecules, bond-order, correlation-diagram, homonuclear, mo-theory]
prerequisites: [hydrogen-molecule-ion-variational, slater-determinants, orbital-angular-momentum]
related: [diatomic-electronic-terms, heteronuclear-diatomic-molecular-orbitals, koopmans-theorem, eom-ccsd-and-size-extensivity, mo-and-valence-bond-theories, h2-dissociation-rhf-uhf]
order: 10
date: 2026-11-18
---

Nuclei $a$ and $b$ lie on the $z$ axis. Orbitals are real unless stated, and $\phi_a$ is an atomic orbital (AO) on nucleus $a$.

## One-electron molecular orbitals

For H₂⁺ the operator $\hat L_z$ commutes with $\hat H$. Its eigenvalue $m\hbar$ labels the orbitals by $\lambda = |m| = 0, 1, 2, \ldots$, written $\sigma, \pi, \delta, \ldots$. Levels with $\lambda > 0$ are doubly degenerate ($m = \pm\lambda$). For two identical nuclei, inversion through the midpoint also commutes with $\hat H$, so every orbital is even (g) or odd (u).

Approximate MOs for many-electron diatomics are taken as H₂⁺-like LCAOs. Two AOs of the same type, one on each nucleus, give one combination of each parity:

$$
\phi_a \pm \phi_b \quad (\phi = 1s, 2s, 2p_z, \ldots),\qquad
(2p_x)_a \pm (2p_x)_b,\qquad (2p_y)_a \pm (2p_y)_b .
$$

- **Bonding and antibonding.** A combination that builds up charge between the nuclei is bonding. One with a nodal plane perpendicular to the axis, midway between the nuclei, is antibonding (star).
- **Parity depends on the AO.** For $s$ and $p_z$, the + combination is $\sigma_g$ (bonding) and the − combination is $\sigma_u^*$. For $p_x$ and $p_y$ it is the other way round: $(2p_x)_a + (2p_x)_b$ is $\pi_u$ (bonding) and the difference is $\pi_g^*$.
- **Complex and real forms.** The complex $\pi$ MOs $(2p_{\pm1})_a \pm (2p_{\pm1})_b$ are eigenfunctions of $\hat L_z$ with a probability density symmetric about the axis. The real $\pi_x$, $\pi_y$ are not eigenfunctions of $\hat L_z$, but they are eigenfunctions of reflection in a plane containing the axis. Either pair spans the same degenerate level.

Because 2s and 2p are close in energy, the real $\sigma$ MOs mix 2s and 2p$_z$ (and 1s) on each atom, so "$\sigma_g2s$" and "$\sigma_g2p$" are labels, not compositions. Only AOs of the same $\lambda$ contribute to a given MO, and only AOs of similar energy contribute much.

| Separated atoms | United atom | By symmetry |
|---|---|---|
| $\sigma_g1s$ | $1s\sigma_g$ | $1\sigma_g$ |
| $\sigma_u^*1s$ | $2p\sigma_u^*$ | $1\sigma_u$ |
| $\sigma_g2s$ | $2s\sigma_g$ | $2\sigma_g$ |
| $\sigma_u^*2s$ | $3p\sigma_u^*$ | $2\sigma_u$ |
| $\pi_u2p$ | $2p\pi_u$ | $1\pi_u$ |
| $\sigma_g2p$ | $3s\sigma_g$ | $3\sigma_g$ |
| $\pi_g^*2p$ | $3d\pi_g^*$ | $1\pi_g$ |
| $\sigma_u^*2p$ | $4p\sigma_u^*$ | $3\sigma_u$ |

The third column numbers the MOs of each symmetry in order of energy. It makes no claim about atomic parentage, so it is the safest.

## Correlation diagram and filling order

As $R\to0$ each MO goes over into an AO of the united atom with the same $\lambda$ and parity. Even AOs ($s, d$) correlate with g MOs and odd ones ($p, f$) with u MOs. **Noncrossing rule:** in a many-electron diatomic, the energies of two MOs of the same symmetry (same $\lambda$ and same g/u) cannot cross as $R$ varies. The lowest MO of each symmetry therefore joins the lowest united-atom AO of that symmetry, and so on upwards.

MO energies vary with $R$ and from molecule to molecule, so there is no universal order. The order in which the shells fill across the first row is

$$
\sigma_g1s < \sigma_u^*1s < \sigma_g2s < \sigma_u^*2s < \pi_u2p < \sigma_g2p < \pi_g^*2p < \sigma_u^*2p .
$$

From O₂ on, $\sigma_g2p$ lies **below** $\pi_u2p$.

**Bond order** is half the number of bonding electrons minus antibonding electrons. Since inner shells overlap very little, $\sigma_g1s$ and $\sigma_u^*1s$ stay near the 1s AO energy and are written KK.

| Molecule | Valence configuration | Ground term | Bond order | $D_e$ (eV) | $R_e$ (Å) |
|---|---|---|---:|---:|---:|
| H₂ | $\sigma_g1s^2$ | $^1\Sigma_g^+$ | 1 | 4.75 | 0.741 |
| He₂ | $\sigma_g1s^2\sigma_u^*1s^2$ | $^1\Sigma_g^+$ | 0 | 0.0009 | 2.97 |
| Li₂ | KK $\sigma_g2s^2$ | $^1\Sigma_g^+$ | 1 | 1.07 | 2.67 |
| Be₂ | KK $\sigma_g2s^2\sigma_u^*2s^2$ | $^1\Sigma_g^+$ | 0 | 0.115 | 2.45 |
| B₂ | … $\pi_u2p^2$ | $^3\Sigma_g^-$ | 1 | 3.1 | 1.59 |
| C₂ | … $\pi_u2p^4$ | $^1\Sigma_g^+$ | 2 | 6.3 | 1.24 |
| N₂ | … $\pi_u2p^4\sigma_g2p^2$ | $^1\Sigma_g^+$ | 3 | 9.91 | 1.10 |
| O₂ | … $\sigma_g2p^2\pi_u2p^4\pi_g^*2p^2$ | $^3\Sigma_g^-$ | 2 | 5.21 | 1.21 |
| F₂ | … $\pi_g^*2p^4$ | $^1\Sigma_g^+$ | 1 | 1.66 | 1.41 |
| Ne₂ | … $\pi_g^*2p^4\sigma_u^*2p^2$ | $^1\Sigma_g^+$ | 0 | 0.0036 | 3.1 |

- **Bonding π electrons.** B₂ is held by two π electrons in degenerate $\pi_{u}$ orbitals. With one electron in each and parallel spins, Hund's rule gives a triplet, as observed.
- **Paramagnetic O₂.** The same argument for its two $\pi_g^*$ electrons explains the paramagnetism of O₂, an early success of MO theory. The resulting terms are worked out in [[diatomic-electronic-terms]].
- **Ionization.** Removing a bonding electron weakens the bond: N₂ → N₂⁺ lowers $D_e$ from 9.91 to 8.85 eV. Removing an antibonding electron strengthens it: O₂ → O₂⁺ raises $D_e$ from 5.21 to 6.78 eV. Either electron still lowers the total energy; ionization always costs energy.
- **Bond order zero is not zero binding.** He₂, Be₂ and Ne₂ have bond order 0 but shallow minima from dispersion, an electron-correlation effect that no single-configuration MO picture contains. Be₂ is unusually short (2.45 Å) for such a molecule, which Levine attributes to 2s–2p hybridization.

!!! example "Bond order against bond strength, and where σ_g2p sits"
    The filling order reproduces all 14 bond orders of Levine's Table 13.2 (H₂⁺ to Ne₂, ions included). Over Li₂–Ne₂, bond order correlates with $D_e$ ($r = 0.97$) and anticorrelates with $R_e$ ($r = -0.82$).

    Hartree–Fock orbital energies are not a reliable guide to the $\sigma_g2p$/$\pi_u2p$ order. The order of the ionization energies is, and getting it right needs electron correlation. Calculations at the Table 13.2 $R_e$, cc-pVTZ:

    | | HF $-\varepsilon$ ($3\sigma_g$) | HF $-\varepsilon$ ($1\pi_u$) | EOM-IP-CCSD, $3\sigma_g^{-1}$ | EOM-IP-CCSD, $1\pi_u^{-1}$ |
    |---|---:|---:|---:|---:|
    | N₂ | 17.20 eV | 16.63 eV | 15.57 eV | 17.17 eV |
    | F₂ | 20.42 eV | 22.03 eV | 21.07 eV | 18.84 eV |

    - **N₂.** The lowest ionization removes a $3\sigma_g$ electron, so $3\sigma_g$ is the highest occupied shell, above $1\pi_u$, as the filling order says.
    - **F₂.** The order is reversed: $1\pi_u$ ionizes before $3\sigma_g$, so $3\sigma_g$ lies below.
    - **Koopmans fails both ways.** Hartree–Fock orbital energies put $1\pi_u$ above $3\sigma_g$ in N₂ and $3\sigma_g$ above $1\pi_u$ in F₂, wrong in both cases (see [[koopmans-theorem]] for the relaxation analysis). The F₂ $\pi_g^{-1}$ ionization comes first at 15.50 eV.

## Source

Levine, *Quantum Chemistry* (7th ed., Pearson, 2014), Sec. 13.6, pp. 365-369 (LCAO MOs of H₂⁺ excited states, $\pi$ MOs, real and complex forms, 2s–2p mixing); Sec. 13.7, pp. 369-375 (Table 13.1 nomenclature, Fig. 13.16 correlation diagram, noncrossing rule, filling order, configurations, Table 13.2, ionization trends, van der Waals molecules); Sec. 13.14, p. 392 (rules for which AOs contribute). Calculations in `part3_batchC.py`, section A (PySCF 2.15.1; HF/ROHF and EOM-IP-CCSD, cc-pVTZ).
