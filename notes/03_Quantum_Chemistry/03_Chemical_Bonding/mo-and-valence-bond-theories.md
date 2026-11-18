---
id: mo-and-valence-bond-theories
title: Molecular-orbital and valence-bond descriptions of the chemical bond
summary: Two zeroth-order pictures of the electron-pair bond. The LCAO-MO function of H₂ weights covalent and ionic terms equally and dissociates wrongly. The Heitler–London VB function has no ionic terms. Adding ionic terms to VB (Weinbaum) and doubly excited configurations to MO give the same function, with δ = (1+γ)/(1−γ). The hierarchy Heitler–London < Coulson MO < Wang < Weinbaum < Hartree–Fock < CI is reproduced with a 22-Gaussian Slater 1s (D_e 3.16, 3.49, 3.78, 4.03 eV; δ = 0.264), matching Levine to 0.01 eV. Also covered - closed-shell repulsion (He₂, where MO and VB coincide), the eight-determinant perfect-pairing VB function of N₂ (verified to be a singlet), and ionic–covalent resonance.
status: in-progress
kind: comparison
level: introductory
tags: [valence-bond, molecular-orbitals, heitler-london, ionic-covalent, h2, weinbaum, chemical-bond]
prerequisites: [hydrogen-molecule-heitler-london, hydrogen-molecule-ion-variational, slater-determinants]
related: [h2-minimal-basis-correlation-analysis, mcscf-and-gvb, h2-dissociation-rhf-uhf, homonuclear-diatomic-molecular-orbitals, heteronuclear-diatomic-molecular-orbitals, virial-theorem-and-chemical-bonding]
order: 10
date: 2026-11-18
---

Atomic units. $a$ and $b$ are 1s Slater orbitals $\pi^{-1/2}\zeta^{3/2}e^{-\zeta r}$ on the two protons, $S = \langle a|b\rangle$. Spatial functions only; the ground state carries the singlet spin factor $2^{-1/2}(\alpha\beta - \beta\alpha)$.

## Two zeroth-order pictures

The two theories split the same Hamiltonian differently:

$$
\hat H = \underbrace{\Big(-\tfrac12\nabla_1^2 - \tfrac1{r_{a1}} - \tfrac1{r_{b1}}\Big) + \Big(-\tfrac12\nabla_2^2 - \tfrac1{r_{a2}} - \tfrac1{r_{b2}}\Big)}_{\text{MO: two H}_2^+\text{ Hamiltonians}} + \frac1{r_{12}} + \frac1R
$$

$$
\hat H = \underbrace{\Big(-\tfrac12\nabla_1^2 - \tfrac1{r_{a1}}\Big) + \Big(-\tfrac12\nabla_2^2 - \tfrac1{r_{b2}}\Big)}_{\text{VB: two H atoms}} - \frac1{r_{b1}} - \frac1{r_{a2}} + \frac1{r_{12}} + \frac1R
$$

(or with electrons 1 and 2 exchanged in the VB grouping).

- **MO zeroth order.** A product of H₂⁺-like orbitals, approximated by LCAOs; electron repulsion enters on average through SCF orbitals.
- **VB zeroth order.** Two hydrogen atoms. The two degenerate products $a(1)b(2)$ and $a(2)b(1)$ (exchange degeneracy) combine to the correct zeroth-order function.

Expanding the LCAO-MO function shows the difference:

$$
\Phi_{\text{MO}} = [a(1) + b(1)][a(2) + b(2)] = \underbrace{a(1)b(2) + b(1)a(2)}_{\text{covalent}} + \underbrace{a(1)a(2) + b(1)b(2)}_{\text{ionic: H}^-\text{H}^+,\ \text{H}^+\text{H}^-} .
$$

- **MO underestimates correlation.** It gives the ionic structures the same weight as the covalent ones, so it dissociates to a 50:50 mixture of H + H and H⁺ + H⁻ ([[h2-dissociation-rhf-uhf]]).
- **Heitler–London overestimates it.** $\Phi_{\text{HL}} = a(1)b(2) + b(1)a(2)$ simply drops the ionic terms and so excludes both electrons from ever being on the same atom. It dissociates correctly ([[hydrogen-molecule-heitler-london]]).

## Improving each, and why they meet

**VB with ionic–covalent resonance:**

$$
\Phi_{\text{VB,imp}} = a(1)b(2) + b(1)a(2) + \delta\,[a(1)a(2) + b(1)b(2)] .
$$

$\delta = 0$ is Heitler–London, $\delta = 1$ is the LCAO-MO function, and $\delta(\infty) = 0$.

**MO with configuration interaction** (the $\sigma_u^{*2}$ configuration, the only one of the right $^1\Sigma_g^+$ symmetry in this basis):

$$
\Phi_{\text{MO,imp}} = (a + b)(a + b) + \gamma\,(a - b)(a - b) .
$$

Dividing by $1 - \gamma$ and collecting terms,

$$
\Phi_{\text{MO,imp}} \propto a(1)b(2) + b(1)a(2) + \frac{1+\gamma}{1-\gamma}\,[a(1)a(2) + b(1)b(2)] ,
$$

which is $\Phi_{\text{VB,imp}}$ with $\delta = (1+\gamma)/(1-\gamma)$. Weinbaum's 1933 calculation can be read either way. In this two-function basis it is the full CI, and it is equivalent to the GVB pair ([[mcscf-and-gvb]]).

!!! example "The H₂ hierarchy with a variable Slater exponent"
    **Method.** The Slater 1s is represented by a least-squares fit of 22 Gaussians (H-atom energy $-0.4999997\,E_h$) and scaled by $\zeta$. For each function, $R$ and $\zeta$ are optimized together; $D_e = -1 - E_{\min}$.

    | Function | $R_e$ (Å) | $\zeta$ | $D_e$ (eV) | Levine |
    |---|---:|---:|---:|---|
    | Heitler–London ($\zeta = 1$) | 0.869 | 1 | 3.16 | 0.87 Å, 3.15 eV |
    | LCAO-MO (Coulson) | 0.733 | 1.193 | 3.49 | 0.732 Å, 1.197, 3.49 eV |
    | Heitler–London–Wang | 0.748 | 1.166 | 3.78 | 0.744 Å, 1.166, 3.78 eV |
    | MO-CI = VB + ionic (Weinbaum) | 0.757 | 1.194 | 4.03 | 0.757 Å, 1.19, 4.03 eV |
    | Hartree–Fock limit (Kolos–Roothaan) | | | | 0.732 Å, 3.64 eV |
    | exact | | | | 0.741 Å, 4.75 eV |

    - **Weinbaum's coefficients.** In normalized MOs the CI vector is $(0.9933, -0.1154)$. With $\sigma_g = (a+b)/\sqrt{2(1+S)}$ and $\sigma_u = (a-b)/\sqrt{2(1-S)}$ this gives $\gamma = -0.582$ and $\delta = 0.264$ (Levine: 0.26).
    - **Equivalence checked.** Evaluating the VB function with that $\delta$ directly reproduces the CI energy to $10^{-15}\,E_h$. With $\delta = 1$ it reproduces the LCAO-MO energy.
    - **Readings.** Optimizing $\zeta$ is worth more than the choice of picture. Once $\zeta$ is optimized, the covalent function (3.78 eV) beats the MO function (3.49 eV), because $\delta$ is much nearer 0 than 1. Even Weinbaum's function leaves 0.7 eV, which needs more configurations or $r_{12}$-dependent terms (James–Coolidge 4.72 eV; Kolos–Wolniewicz reproduce $D_0$ to spectroscopic accuracy).

## Many-electron molecules

**Closed shells repel.** For He₂ each atom has $1s^2$, with no unpaired electron to form a bond. The VB function is $|1s_a\overline{1s_a}1s_b\overline{1s_b}|$. In MO form, with $\sigma_g = a + b$ and $\sigma_u = a - b$,

$$
|\sigma_g\overline{\sigma_g}\sigma_u\overline{\sigma_u}| = \big[\det\begin{pmatrix}1 & 1\\ 1 & -1\end{pmatrix}\big]^2\,|a\bar a b\bar b| = 4\,|a\bar a b\bar b| .
$$

The two descriptions coincide. This holds generally for atoms with completely filled subshells, and both predict repulsion, the Pauli repulsion of the two pairs.

**Lone pairs and bonds in VB.** Li₂ pairs the two 2s electrons, with the 1s pairs as in He₂:

$$
|1s_a\overline{1s_a}1s_b\overline{1s_b}2s_a\overline{2s_b}| - |1s_a\overline{1s_a}1s_b\overline{1s_b}\overline{2s_a}2s_b| .
$$

For N₂ ($^4S$ atoms, one electron in each 2p) the triple bond pairs $2p_{xa}$–$2p_{xb}$, $2p_{ya}$–$2p_{yb}$ and $2p_{za}$–$2p_{zb}$. Each pair can carry its opposite spins in two ways, giving $2^3 = 8$ determinants. The **perfect-pairing rule** gives each determinant a coefficient $+1$ or $-1$ according as an even or odd number of spin interchanges generates it from $D_1$. The result is a singlet.

!!! example "The N₂ perfect-pairing function is a singlet"
    Applying $\hat S^2 = \hat S_-\hat S_+ + \hat S_z^2 + \hat S_z$ to the signed sum of the eight determinants gives exactly zero, coefficient by coefficient. With all coefficients $+1$ the result is not an eigenfunction of $\hat S^2$.

The MO function of N₂ is a single determinant. The economy of one determinant per closed-shell state, against a combination of determinants that grows with the number of bonds, is why MO theory displaced VB for computation. The VB function is closer to the chemist's localized bonds; [[localized-molecular-orbitals]] shows how the MO determinant expresses the same bonds.

**Polar bonds.** In VB a polar bond is a resonance $c_1\Phi_{\text{cov}} + c_2\Phi_{\text{ion}}$ between H–F and H⁺F⁻ ([[heteronuclear-diatomic-molecular-orbitals]]). This is not a time-dependent oscillation between structures but a single, stationary mixture.

## Source

Levine, *Quantum Chemistry* (7th ed., Pearson, 2014), Sec. 13.9, pp. 379-382 (Coulson LCAO-MO: 0.732 Å, 3.49 eV, ζ = 1.197; Hartree–Fock limit 3.64 eV; Weinbaum CI 0.757 Å, 4.03 eV; James–Coolidge, Kolos–Wolniewicz); Sec. 13.10, pp. 382-384 (Heitler–London 3.15 eV, 0.87 Å; Wang ζ = 1.166, 3.78 eV, 0.744 Å; Rosen); Sec. 13.11, pp. 384-386 (covalent and ionic terms, Eqs. (13.106)-(13.109), δ = 0.26, equivalence with MO-CI, the two Hamiltonian partitions); Sec. 13.12, pp. 386-389 (He₂, Eqs. (13.110)-(13.113); Li₂ and N₂ VB functions, the perfect-pairing sign rule). Calculations in `part3_batchC.py`, section F (PySCF integrals over the 22-Gaussian Slater fit).
