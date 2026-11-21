---
id: hydrogen-molecule-ion-exact
title: The exact solution of H₂⁺ in confocal elliptic coordinates
summary: H₂⁺ is the one molecule whose clamped-nuclei Schrödinger equation separates exactly. In confocal elliptic coordinates (ξ, η, φ) the wave function factorizes as L(ξ)M(η)e^{imφ}, and E(R) follows from matching the separation constant of two ordinary differential equations. Covers the derivation, the quantum numbers (λ = |m|, g/u), the united-atom and separated-atom limits, and the 1σ_g and 1σ_u curves. Solved numerically here (Legendre basis for η, finite volumes for ξ) - E_el(2.0) = −1.1026345 E_h; R_e = 1.9972 bohr, U(R_e) = −0.60263 E_h, D_e = 2.793 eV, as in Levine. Also the shallow van der Waals minimum of 1σ_u at 12.6 bohr (61 μE_h), the LCAO errors, and the muonic (pμp)⁺ ion.
status: in-progress
kind: derivation
level: intermediate
tags: [h2-plus, exact-solution, elliptic-coordinates, separation-of-variables, potential-energy-curve, born-oppenheimer]
prerequisites: [born-oppenheimer-approximation, molecular-hamiltonian, atomic-units, hydrogen-atom]
related: [hydrogen-molecule-ion-variational, homonuclear-diatomic-molecular-orbitals, virial-theorem-and-chemical-bonding, classical-orthogonal-polynomials]
conventions: [atomic-units]
order: 35
date: 2026-11-20
---

Atomic units. The protons $a$ and $b$ are clamped a distance $R$ apart on the $z$ axis, with the origin at the midpoint. $r_a$ and $r_b$ are the electron's distances from them. The purely electronic Hamiltonian ([[born-oppenheimer-approximation]]) is

$$
\hat H_{\text{el}} = -\tfrac12\nabla^2 - \frac1{r_a} - \frac1{r_b},\qquad U(R) = E_{\text{el}}(R) + \frac1R .
$$

## Separation in confocal elliptic coordinates

The equation does not separate in spherical coordinates. It does in

$$
\xi = \frac{r_a + r_b}{R}\in[1, \infty),\qquad \eta = \frac{r_a - r_b}{R}\in[-1, 1],\qquad \phi\in[0, 2\pi),
$$

where $\phi$ is the azimuth about the axis. Surfaces of constant $\xi$ are ellipsoids and surfaces of constant $\eta$ are hyperboloids, both with foci at the nuclei. Inverting, $r_a = \tfrac R2(\xi + \eta)$ and $r_b = \tfrac R2(\xi - \eta)$, so the potential is

$$
-\frac1{r_a} - \frac1{r_b} = -\frac{4\xi}{R(\xi^2 - \eta^2)} .
$$

The Laplacian is

$$
\nabla^2 = \frac{4}{R^2(\xi^2 - \eta^2)}\Big[\frac{\partial}{\partial\xi}(\xi^2 - 1)\frac{\partial}{\partial\xi} + \frac{\partial}{\partial\eta}(1 - \eta^2)\frac{\partial}{\partial\eta} + \Big(\frac1{\xi^2 - 1} + \frac1{1 - \eta^2}\Big)\frac{\partial^2}{\partial\phi^2}\Big] .
$$

**The common factor makes the equation separable.** Multiply $\hat H_{\text{el}}\psi = E\psi$ by $-\tfrac12R^2(\xi^2 - \eta^2)$; the potential term becomes $2R\xi$ and the energy term $\tfrac12R^2E(\xi^2 - \eta^2)$. With $\psi = L(\xi)M(\eta)e^{im\phi}$ and $p^2 \equiv -R^2E/2 > 0$ for bound states, the equation splits into

$$
\frac{\mathrm d}{\mathrm d\xi}\Big[(\xi^2 - 1)\frac{\mathrm dL}{\mathrm d\xi}\Big] + \Big[2R\xi - p^2\xi^2 - \frac{m^2}{\xi^2 - 1}\Big]L = A\,L ,
$$

$$
\frac{\mathrm d}{\mathrm d\eta}\Big[(1 - \eta^2)\frac{\mathrm dM}{\mathrm d\eta}\Big] + \Big[p^2\eta^2 - \frac{m^2}{1 - \eta^2}\Big]M = -A\,M ,
$$

with a common separation constant $A$.

- **Quantization.** For a fixed $R$ and trial energy, each equation is an eigenvalue problem for $A$. An energy is allowed only where the two eigenvalues agree. There is no closed formula; $E_{\text{el}}(R)$ is computed numerically.
- **Quantum numbers.** $\hat L_z$ commutes with $\hat H_{\text{el}}$ but $\hat L^2$ does not. Since $m$ enters only as $m^2$, levels with $\lambda = |m| > 0$ are doubly degenerate, labelled $\sigma, \pi, \delta, \ldots$ for $\lambda = 0, 1, 2, \ldots$. Inversion through the midpoint commutes with $\hat H_{\text{el}}$, giving g/u. The nodes of $L$ and $M$ count the states.
- **Parity in $\eta$.** For identical nuclei the $\eta$ equation is even in $\eta$, so $M$ is even (g, for $m$ even) or odd.

## Solving it

!!! example "Numerical solution for 1σ_g and 1σ_u"
    **Method** ($m = 0$).
    - **$\eta$ equation.** It is diagonalized in normalized Legendre polynomials of one parity (40 functions; the $\eta^2$ matrix is computed by 200-point Gauss–Legendre quadrature). Its largest eigenvalue is $-A$.
    - **$\xi$ equation.** It is discretized by finite volumes in $t = \xi - 1$ on a grid $t = s^2$ (4000 cells to $t = 50/p$). The flux vanishes at $\xi = 1$, where $\xi^2 - 1 = 0$, and $L = 0$ at the outer edge. Its largest eigenvalue is $A$.
    - **Energy.** $p$ is found by Brent's method where the two separation constants agree.

    | Quantity | This work | Levine |
    |---|---:|---:|
    | $E_{\text{el}}$ at $R = 2.0$ bohr | −1.1026345 $E_h$ | |
    | $R_e$ | 1.9972 bohr = 1.0569 Å | 1.9972 bohr |
    | $E_{\text{el}}(R_e)$ | −1.10334 $E_h$ | −1.1033 |
    | $U(R_e)$ | −0.60263 $E_h$ | −0.6026 |
    | $D_e$ | 0.10263 $E_h$ = 2.793 eV | 0.1026 $E_h$ = 2.79 eV |

    **The two curves** (energies in $E_h$):

    | $R$ (bohr) | 1 | 2 | 4 | 8 | 12.5 |
    |---|---:|---:|---:|---:|---:|
    | $U$, 1σ_g | −0.45179 | −0.60263 | −0.54609 | −0.50257 | −0.50013 |
    | $U$, 1σ_u | +0.43519 | −0.16754 | −0.44555 | −0.49861 | −0.50006 |

    - **Limits.** As $R\to0$, $E_{\text{el}}$ approaches the united-atom value of He⁺, $-Z^2/2 = -2\,E_h$ ($-1.994$ at $R = 0.05$). As $R\to\infty$, $U$ approaches the separated-atom value of H + H⁺, $-0.5\,E_h$.
    - **1σ_u.** The curve is repulsive at chemical distances but has a very shallow minimum near $R = 12.6$ bohr, 61 μ$E_h$ deep (Levine: 12.5 bohr and 0.00006 $E_h$). It is attributable to the long-range attraction between H⁺ and the dipole it induces in the H atom.

## What the exact numbers teach

- **One electron suffices to bind.** H₂⁺ is a stable molecule, held together by a single electron.
- **Binding energy is a small difference of large numbers.** $D_e$ is only 17% of $|U(R_e)|$ here. For heavier molecules, bond energies stay a few eV while total energies grow enormously, so small relative errors in $E$ become large errors in $D_e$.
- **Calibration of approximations.** The LCAO function $N(1s_a + 1s_b)$ of [[hydrogen-molecule-ion-variational]] gives $D_e$ = 1.76 eV with exponent 1 and 2.35 eV with the exponent optimized ($\zeta$ = 1.238, $R_e$ = 2.003 bohr; [[virial-theorem-and-chemical-bonding]]). The exact value is 2.79 eV, so even the optimized-exponent LCAO misses 0.44 eV of the bond.
- **Muonic H₂⁺.** Replacing the electron by a muon ($m_\mu \approx 207\,m_e$) scales all lengths by $1/207$. The $(p\mu p)^+$ ion then has $R_e$ = 0.0051 Å. The nuclei are close enough that, with D and T, the muon catalyses fusion.

## Source

Levine, *Quantum Chemistry* (7th ed., Pearson, 2014), Sec. 13.4, pp. 353-357: Hamiltonian (13.31)-(13.32); confocal elliptic coordinates (13.33)-(13.35); $\hat L_z$ commutes and $\hat L^2$ does not, (13.36); separated form (13.37); limits; $R_e$ = 1.9972 bohr, $E_{\text{el}}$ = −1.1033, $U$ = −0.6026, $D_e$ = 2.79 eV; Figs. 13.4-13.5 including the 1σ_u minimum at 12.5 bohr; $\lambda$ and g/u labels; muon-catalysed fusion. The Laplacian and the two separated equations are derived here rather than taken from Levine (he omits them), and both were checked by the agreement of the numerical results. Calculations in `part2_levine_gaps.py`, section E (NumPy/SciPy); the LCAO values come from `part3_batchC.py`, section G.
