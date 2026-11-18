---
id: rigid-rotor-and-rovibrational-levels
title: Rigid rotor and rovibrational levels of a diatomic molecule
summary: The two-particle rigid rotor (E = J(J+1)ħ²/2μd², 2J+1-fold degenerate, no zero-point rotation), the rotational constant B and the microwave selection rule ΔJ = ±1, bond lengths from rotational lines, and the corrections for a real molecule - vibration–rotation coupling B_v = B_e − α_e(v+½) and centrifugal distortion −DJ²(J+1)². Levine's CS and CO bond lengths are reproduced, and B₀, α_e and D for H₂ are computed from the FCI/cc-pVQZ curve by solving the radial equation with the centrifugal term.
status: in-progress
kind: theory
level: intermediate
tags: [rigid-rotor, rotational-spectroscopy, rotational-constant, centrifugal-distortion, vibration-rotation-coupling, diatomic]
prerequisites: [diatomic-vibration-and-anharmonicity, orbital-angular-momentum, central-potentials-and-spherical-harmonics]
related: [numerov-method, two-particle-systems-and-reduced-mass, zero-point-energy-and-thermochemistry, energy-and-unit-conversions]
order: 20
date: 2026-11-17
---

## The two-particle rigid rotor

Two masses $m_1$, $m_2$ held at fixed distance $d$ by a massless rod have, after separating the centre of mass, only rotational kinetic energy. With $r = d$ fixed the radial derivatives drop out of the Laplacian, and

$$
\hat H = \frac{\hat L^2}{2\mu d^2},\qquad \mu = \frac{m_1m_2}{m_1 + m_2} .
$$

The eigenfunctions are the spherical harmonics $Y_J^M(\theta,\phi)$ ([[central-potentials-and-spherical-harmonics]]), with

$$
E_J = \frac{J(J+1)\hbar^2}{2I},\qquad I = \mu d^2 = m_1r_1^2 + m_2r_2^2,\qquad J = 0,1,2,\dots
$$

where $r_1$, $r_2$ are the distances of the masses from the centre of mass. Each level is $(2J+1)$-fold degenerate ($M = -J,\dots,J$, different orientations of the angular momentum in space). The lowest level has $E = 0$: there is no rotational zero-point energy, and no conflict with the uncertainty principle since $\mathbf L = 0$ is then known exactly.

## Rotational spectrum

Pure rotational transitions require a permanent dipole moment and obey $\Delta J = \pm1$. With the **rotational constant**

$$
B = \frac{h}{8\pi^2I}\ \ (\text{frequency}),\qquad \tilde B = \frac{h}{8\pi^2cI}\ \ (\text{cm}^{-1}),
$$

the levels are $E_J = hBJ(J+1)$ and the absorption lines $J\to J+1$ fall at

$$
\nu = 2B(J + 1) = 2B,\ 4B,\ 6B,\dots
$$

equally spaced by $2B$, in the microwave or far infrared. Many $J$ levels are populated at room temperature because the spacings are comparable to $kT$. Measuring one line gives $B$, hence $I$ and the bond length.

## A real (non-rigid) diatomic

Including the centrifugal term in the radial equation of [[diatomic-vibration-and-anharmonicity]],

$$
-\frac{\hbar^2}{2\mu}F'' + \Big[U(R) + \frac{J(J+1)\hbar^2}{2\mu R^2}\Big]F = EF,
$$

and replacing $1/R^2$ by $1/R_e^2$ gives the harmonic-oscillator, rigid-rotor energy $E\approx U(R_e) + (v+\tfrac12)h\nu_e + hB_eJ(J+1)$. Two corrections follow from perturbation theory:

- **Vibration–rotation coupling.** In level $v$ the molecule samples larger $R$ (anharmonicity), so the effective constant is the average of $\hbar^2/2\mu R^2$:
$$
B_v = \Big\langle v\Big|\frac{\hbar^2}{2\mu R^2}\Big|v\Big\rangle \approx B_e - \alpha_e\big(v + \tfrac12\big),\qquad \alpha_e > 0,\ \alpha_e\ll B_e .
$$
- **Centrifugal distortion.** Rotation stretches the bond, adding $-hDJ^2(J+1)^2$; for a harmonic bond $D = 4B_e^3/\nu_e^2$ (Kratzer relation).

The term value of a rovibrational level is therefore

$$
\frac{E(v,J)}{hc} = G(v) + \tilde B_vJ(J+1) - \tilde DJ^2(J+1)^2 .
$$

A bond length from $B_0$ is an average over the $v = 0$ vibration ($r_0$), slightly longer than $R_e$. Isotopologues have the same $R_e$ but different $I$, hence different lines.

## Worked examples

!!! example "Bond lengths from rotational lines (Levine Sec. 6.4)"
    - $^{12}$C$^{32}$S, lowest line ($J = 0\to1$) at 48 991.0 MHz: $h\nu = 2\cdot\hbar^2/2\mu d^2$, so $d = [h/(4\pi^2\nu\mu)]^{1/2}$. With $\mu = 1.448\,85\times10^{-26}$ kg, $d = 1.5377$ Å.
    - $^{12}$C$^{16}$O, $J = 1\to2$ at 230.538 GHz ($\nu = 4B$): $d = 1.1309$ Å.
    - For CO Levine quotes $B_0 = 57\,636$ MHz, $\alpha_e = 540$ MHz and $D = 0.18$ MHz. Then $B_e = B_0 + \alpha_e/2 = 57\,906$ MHz (1.9315 cm$^{-1}$), $r_e = 1.1282$ Å and $r_0 = 1.1309$ Å: the vibrationally averaged length is 0.003 Å longer. The Kratzer estimate $4B_e^3/\nu^2$ with $\nu$ from the 2143 cm$^{-1}$ band gives $D = 0.188$ MHz, close to the quoted 0.18 MHz.

!!! example "H₂: rotational constants from the FCI/cc-pVQZ curve"
    Same curve and Numerov solver as in [[diatomic-vibration-and-anharmonicity]], now with the centrifugal term.

    | Quantity | Value (cm$^{-1}$) | How obtained |
    |---|---:|---|
    | $\tilde B_e$ | 60.818 | $\hbar^2/(2\mu R_e^2)$ at $R_e = 1.401\,92\,a_0$ |
    | $\tilde B_v$, $v = 0,1,2,3$ | 59.307, 56.360, 53.474, 50.630 | $\langle v|\hbar^2/2\mu R^2|v\rangle$ |
    | $\alpha_e$ | 2.892 | linear fit of $\tilde B_v$ |
    | $E(0,1) - E(0,0)$ | 118.432 | Numerov with $J = 1$ ($2\tilde B_0 = 118.614$) |
    | $E(0,2) - E(0,0)$ | 354.210 | Numerov with $J = 2$ ($6\tilde B_0 = 355.841$) |
    | $\tilde D$ from $J = 1, 2$ | 0.0452 | solving $F(J) = BJ(J+1) - DJ^2(J+1)^2$ |
    | Kratzer $4\tilde B_e^3/\omega_e^2$ | 0.0465 | with $\omega_e = 4400.5$ |

    - **Centrifugal distortion is visible.** For $J = 5$ the Numerov level lies 1739.43 cm$^{-1}$ above $J = 0$; the rigid rotor ($30\tilde B_0$) gives 1779.2, and adding $-900\tilde D$ gives 1738.5.
    - **H₂ is an extreme case.** Its tiny reduced mass makes $B$, $\alpha_e$ and $D$ unusually large. Relative to $B$, the corrections are much smaller for CO: $\alpha_e/B_e$ is 0.048 for H₂ and 0.009 for CO, and $D/B_0$ is $7.6\times10^{-4}$ for H₂ and $3.1\times10^{-6}$ for CO. H₂ has no permanent dipole, so these levels are seen in Raman and quadrupole spectra, not in microwave absorption.

## Source

Levine, *Quantum Chemistry* (7th ed., Pearson, 2014), Sec. 6.4, pp. 124-128, Eqs. (6.44)-(6.55), Example (CS) and Exercise (CO), and the CO constants $B_0$, $\alpha_e$, $D$; Sec. 13.2, pp. 347-350, Eqs. (13.16)-(13.28). The Kratzer relation is standard (not derived in Levine). Calculations in `part3_batchA.py`, sections B and C.
