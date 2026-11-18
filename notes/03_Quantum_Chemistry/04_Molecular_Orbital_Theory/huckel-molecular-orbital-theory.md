---
id: huckel-molecular-orbital-theory
title: Hückel molecular-orbital theory of conjugated π systems
summary: The π-electron approximation and Hückel's assumptions (α on the diagonal, β for bonded neighbours, zero overlap) reduce a planar conjugated hydrocarbon to the eigenvalues of its adjacency matrix. Closed forms for linear polyenes and annulenes (Frost circle, 4m+2 rule), alternant pairing, π charges and Coulson bond orders, delocalization energies, and the empirical β. Checked numerically - butadiene (0.372/0.602, p = 0.894/0.447, 0.472|β|), β = 4.62 eV from 217 nm, benzene (2|β|), annulenes C₃–C₁₀, naphthalene (Δx = 1.236 and the bond lengths of Levine's Eq. 17.57). Ab initio STO-3G benzene π MOs are exactly the symmetry-determined Hückel MOs.
status: in-progress
kind: theory
level: introductory
tags: [huckel, pi-electrons, conjugated-molecules, aromaticity, bond-order, semiempirical, benzene, butadiene]
prerequisites: [molecular-orbitals-of-polyatomic-molecules, matrix-eigenvalue-problem]
related: [one-particle-hamiltonian-models, bond-orders-and-atomic-charges, localized-molecular-orbitals]
order: 50
date: 2026-11-18
---

## The π-electron approximation and Hückel's assumptions

In a planar conjugated molecule the canonical MOs are $\sigma$ (symmetric under reflection in the plane) or $\pi$ (antisymmetric). The $\pi$ electrons are treated alone, in the field of a fixed "core" of nuclei and $\sigma$ electrons. Hückel goes further and takes the $\pi$ Hamiltonian as a sum of unspecified one-electron operators,

$$
\hat H_\pi \approx \sum_i \hat H^{\text{eff}}(i),\qquad \hat H^{\text{eff}}\phi_j = e_j\phi_j,\qquad E_\pi = \sum_j n_je_j .
$$

Each $\pi$ MO is expanded in the carbon $2p\pi$ AOs $f_r$, $\phi_j = \sum_r c_{rj}f_r$, and the integrals are parametrized:

$$
H^{\text{eff}}_{rr} = \alpha,\qquad
H^{\text{eff}}_{rs} = \begin{cases}\beta & r, s \text{ bonded}\\ 0 & \text{otherwise}\end{cases},\qquad
S_{rs} = \delta_{rs} .
$$

$\alpha$ is the Coulomb integral and $\beta$ the bond (resonance) integral. Both are negative; $\beta < 0$ follows from the nodeless MO being lowest. Neglecting the overlap of neighbouring 2p$\pi$ AOs (about 0.2-0.3 for Slater orbitals) is the crudest step.

With $\mathbf A$ the adjacency matrix of the carbon skeleton, $\mathbf H = \alpha\mathbf 1 + \beta\mathbf A$, and

$$
e_j = \alpha + x_j\beta,\qquad \mathbf A\mathbf c_j = x_j\mathbf c_j .
$$

Only the topology counts: s-cis and s-trans butadiene are the same Hückel problem. The order of the secular determinant is the number of conjugated atoms, not the number of $\pi$ electrons.

## Linear polyenes and annulenes

**Chains** $\text{CH}_2{=}(\text{CH}{-}\text{CH}{=})_s\text{CH}_2$ with $n$ carbons. $\mathbf A$ is a tridiagonal continuant, with

$$
e_j = \alpha + 2\beta\cos\frac{j\pi}{n+1},\qquad c_{rj} = \Big(\frac{2}{n+1}\Big)^{1/2}\sin\frac{rj\pi}{n+1},\qquad j = 1, \ldots, n .
$$

All levels are nondegenerate. The HOMO–LUMO gap of an even polyene is $\Delta e = 4|\beta|\sin[\pi/(2(n+1))]$.

**Rings** $\text{C}_n\text{H}_n$. $\mathbf A$ is a circulant, and its eigenvectors are fixed by the $C_n$ symmetry alone:

$$
e_k = \alpha + 2\beta\cos\frac{2\pi k}{n},\qquad c_{rk} = n^{-1/2}e^{2\pi i rk/n},\qquad k = 0, \ldots, n-1 .
$$

- **Level pattern.** Apart from the nondegenerate lowest level (and, for even $n$, the nondegenerate top level), the levels come in degenerate pairs $k$, $n-k$.
- **Frost circle.** Inscribe the regular $n$-gon, vertex down, in a circle of radius $2|\beta|$ centred at $\alpha$. The vertex heights are the levels.
- **4m+2 rule.** A closed $\pi$ shell needs $4m+2$ electrons. With $4m$ electrons the top degenerate pair is half filled, and Hund's rule predicts a triplet.

The 4m+2 rule does not depend on the Hückel parametrization: the ring MOs are the minimal-basis SCF $\pi$ MOs by symmetry. Only their energies are Hückel's.

**Alternant hydrocarbons.** If the carbons can be starred so that no two starred (or unstarred) atoms are bonded, $\mathbf A$ is bipartite. Flipping the sign of the starred coefficients maps an eigenvector with $x$ to one with $-x$, so the levels are **paired** about $\alpha$. In the neutral ground state every $\pi$ charge $q_r$ is then exactly 1. All planar conjugated hydrocarbons are alternant except those with odd-membered rings.

## Derived quantities

- **$\pi$-electron charge** (number of $\pi$ electrons near atom $r$): $q_r = \sum_j n_j|c_{rj}|^2$.
- **Coulson (mobile) bond order:** $p_{rs} = \tfrac12\sum_j n_j(c^*_{rj}c_{sj} + c^*_{sj}c_{rj})$. The total bond order is $1 + p_{rs}$, counting the $\sigma$ bond.
- **Bond length from bond order.** Assume a linear relation and fit it to ethylene ($p = 1$, 1.335 Å) and benzene ($p = \tfrac23$, 1.397 Å):

$$
R_{rs} = (1.521 - 0.186\,p_{rs})\ \text{Å}.
$$

- **Delocalization energy:** $E_\pi$ minus $2(\alpha + \beta)$ per formal double bond.
- **Excitation energy.** The longest-wavelength band is predicted at $\Delta e = e_{\text{LUMO}} - e_{\text{HOMO}}$.

!!! example "Butadiene"
    $\mathbf A$ is the 4×4 continuant, $x^4 - 3x^2 + 1 = 0$, so $x = \pm1.618, \pm0.618$ $= 2\cos(j\pi/5)$.

    - **Lowest MO.** $\phi_1 = 0.372f_1 + 0.602f_2 + 0.602f_3 + 0.372f_4$, with $e_1 = \alpha + 1.618\beta$.
    - **Energy.** $E_\pi = 2(\alpha + 1.618\beta) + 2(\alpha + 0.618\beta) = 4\alpha + 4.472\beta$, a delocalization energy of $0.472|\beta|$.
    - **Bond orders** $p_{12} = 0.894$ and $p_{23} = 0.447$, so the central bond has partial double-bond character. All $q_r = 1$.
    - **Spectroscopic $\beta$.** The gap is $1.236|\beta|$. Equating it to the observed 217 nm band (5.714 eV) gives $|\beta|$ = 4.62 eV = 37 300 cm⁻¹. With that $\beta$ the chains $n$ = 2, 4, 6, 8, 10 are predicted at 134, 217, 301, 386 and 471 nm. The trend is right, but Levine reports a mean error of 44% against the measured polyene bands. Two alternating integrals (Lennard-Jones: −3.32 eV for C–C, −4.20 eV for C=C) cut it to 9%.

!!! example "Benzene and the other annulenes"
    - **Benzene.** $x = 2, 1, 1, -1, -1, -2$; $E_\pi = 6\alpha + 8\beta$, a delocalization energy of $2|\beta|$, and every bond order is $\tfrac23$.
    - **Thermochemical $\beta$.** The hydrogenation enthalpy of benzene ($-49.8$ kcal/mol) against three times that of cyclohexene ($3\times(-28.6)$) gives 36 kcal/mol, so $|\beta|$ = 18 kcal/mol = 0.78 eV. This is far from the spectroscopic value: $\beta$ is not transferable between properties.
    - **Rings $n$ = 3 to 10.** For each, the Hückel levels equal the Frost-circle values to $10^{-12}$. The neutral is closed-shell exactly for $n$ = 6 and 10 ($4m+2$). C₅H₅⁻ and C₇H₇⁺ are the closed-shell ions. Real cyclobutadiene is a rectangular singlet, and planar C₈H₈ is avoided by a tub structure, so the simple rule is not the whole story.
    - **Ab initio check.** In RHF/STO-3G benzene (R(CC) = 1.397 Å) the three occupied $\pi$ MOs lie at −0.455 and −0.279 (×2) $E_h$. The $a_{2u}$ MO has identical 2p$_z$ coefficients on all six carbons. The $e_{1g}$ pair spans exactly the Hückel $e_{1g}$ space (principal-angle cosine 1 to $10^{-15}$). Symmetry fixes the MOs; Hückel only approximates the energies.

!!! example "Naphthalene"
    Numbering 1-8 around the rings and 9, 10 for the bridgeheads, the ten levels are

    $$
    x = \pm2.303,\ \pm1.618,\ \pm1.303,\ \pm1.000,\ \pm0.618 .
    $$

    They are paired, as for any alternant, and the HOMO–LUMO gap is $\Delta x = 1.236$.

    | Bond | $p_{rs}$ | $R$ from Eq. above (Å) | Levine | Experiment (gas, Levine) |
    |---|---:|---:|---:|---:|
    | 1–2 | 0.725 | 1.386 | 1.386 | 1.371 |
    | 2–3 | 0.603 | 1.409 | 1.409 | 1.410 |
    | 1–9 | 0.555 | 1.418 | 1.418 | 1.421 |
    | 9–10 | 0.518 | 1.425 | 1.425 | 1.420 |

    The rings are not regular hexagons, and the simple bond-order/length relation captures this to about 0.015 Å.

**Limits.** Hückel neglects electron repulsion. It cannot separate singlets from triplets, and the total energy is not the sum of orbital energies in a real SCF calculation. Fitted parameters (for benzenoid absorption bands, $\Delta\tilde\nu = a + |\beta|\Delta x/hc$ with $a$ = 8200 cm⁻¹ and $|\beta|/hc$ = 21 900 cm⁻¹) improve agreement without proving the model. For the same model used as a test bed for many-electron methods, see [[one-particle-hamiltonian-models]].

## Source

Levine, *Quantum Chemistry* (7th ed., Pearson, 2014), Sec. 17.1, pp. 600-601 ($\pi$-electron approximation); Sec. 17.2, pp. 601-619: Hückel assumptions, Eqs. (17.3)-(17.16); butadiene, Eqs. (17.17)-(17.27); polyenes, Eqs. (17.28)-(17.31), the 217 nm $\beta$, Lennard-Jones's two-$\beta$ model; benzene, Eqs. (17.32)-(17.42); annulenes, Eqs. (17.43)-(17.46), Frost circle, 4m+2 rule, cyclobutadiene and cyclooctatetraene; naphthalene and alternant pairing; Heilbronner–Murrell fit (17.49); delocalization energies, Eqs. (17.50)-(17.51), and the thermochemical $\beta$; charges and bond orders, Eqs. (17.52)-(17.56); bond-length relation (17.57) and the naphthalene bond lengths. Calculations in `part3_batchC.py`, section E (NumPy; PySCF for benzene).
