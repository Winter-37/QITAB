---
id: energy-and-unit-conversions
title: Energy and unit conversions
summary: A full conversion table between hartree, eV, kcal/mol, kJ/mol, cm⁻¹, kelvin and MHz (CODATA 2022), plus the conversions needed for gradients, Hessians and vibrational analysis - force (E_h/a₀), force constant (E_h/a₀²), the harmonic-wavenumber prefactor 5140.49 cm⁻¹ for k in E_h/a₀² and μ in u, time, dipole and thermal energies at 298.15 K.
status: in-progress
kind: reference
level: introductory
tags: [units, conversions, energy, hartree, wavenumber, force-constant, gradient]
prerequisites: [physical-constants]
related: [atomic-units, analytic-gradients-and-force-constants, geometry-optimization]
order: 20
date: 2026-11-17
---

## Energy

One unit of the row equals the tabulated number of the column. Molar units use $N_A$; kcal is the thermochemical calorie, 4.184 J exactly; cm$^{-1}$ means $E/(hc)$; K means $E/k_B$; MHz means $E/h$.

| 1 ↓ in → | $E_h$ | eV | kcal/mol | kJ/mol | cm$^{-1}$ | K |
|---|---:|---:|---:|---:|---:|---:|
| $E_h$ | 1 | 27.211 386 | 627.509 47 | 2625.4996 | 219 474.63 | 315 775.02 |
| eV | 0.036 749 322 | 1 | 23.060 548 | 96.485 332 | 8065.5439 | 11 604.518 |
| kcal/mol | 0.001 593 601 4 | 0.043 364 104 | 1 | 4.184 | 349.755 09 | 503.219 53 |
| kJ/mol | 3.808 798 8 × 10⁻⁴ | 0.010 364 27 | 0.239 005 74 | 1 | 83.593 472 | 120.272 36 |
| cm$^{-1}$ | 4.556 335 3 × 10⁻⁶ | 1.239 842 × 10⁻⁴ | 0.002 859 143 5 | 0.011 962 657 | 1 | 1.438 776 9 |
| K | 3.166 811 6 × 10⁻⁶ | 8.617 333 × 10⁻⁵ | 0.001 987 204 3 | 0.008 314 462 6 | 0.695 034 8 | 1 |

In frequency units, 1 $E_h$ = 6.579 683 9 × 10⁹ MHz and 1 cm$^{-1}$ = 29 979.246 MHz ($c$ in cm/s).

**Useful anchors.** 1 kcal/mol ≈ 1.6 m$E_h$, so "chemical accuracy" (1 kcal/mol) is 1.6 m$E_h$ and 1 m$E_h$ ≈ 0.63 kcal/mol ≈ 2.6 kJ/mol ≈ 220 cm$^{-1}$. 1 eV ≈ 23 kcal/mol.

## Length, mass, time

| Quantity | Conversion |
|---|---|
| length | 1 $a_0$ = 0.529 177 210 5 Å; 1 Å = 1.889 726 126 $a_0$ |
| mass | 1 u (dalton) = 1822.888 486 $m_e$; $m_p$ = 1836.152 673 $m_e$ |
| time | 1 a.u. ($\hbar/E_h$) = 0.024 188 843 fs; 1 fs = 41.341 373 a.u. |
| dipole moment | 1 $ea_0$ = 2.541 746 47 D (1 D = $10^{-21}/c$ C m) |

## Gradients, Hessians and vibrational frequencies

Energy derivatives come out of a program in atomic units: gradients in $E_h/a_0$, Cartesian force constants in $E_h/a_0^2$.

| Quantity | Conversion |
|---|---|
| force / gradient | 1 $E_h/a_0$ = 82.387 235 nN = 51.422 068 eV/Å = 1185.821 05 kcal mol$^{-1}$ Å$^{-1}$ |
| force constant | 1 $E_h/a_0^2$ = 1556.893 1 N/m = 15.568 931 mdyn/Å |

**Harmonic wavenumber.** For a diatomic with force constant $k$ and reduced mass $\mu$, $\omega = \sqrt{k/\mu}$ and $\tilde\nu = \omega/(2\pi c)$. With $k$ in $E_h/a_0^2$ and $\mu$ in daltons,

$$
\tilde\nu\,[\mathrm{cm^{-1}}] = 5140.487\,\sqrt{\frac{k\,[E_h/a_0^2]}{\mu\,[\mathrm u]}},
\qquad
\tilde\nu\,[\mathrm{cm^{-1}}] = 1302.791\,\sqrt{\frac{k\,[\mathrm{mdyn/\AA}]}{\mu\,[\mathrm u]}} .
$$

For a polyatomic molecule the same prefactor converts the eigenvalues $\lambda$ of the mass-weighted Hessian ($E_h\,a_0^{-2}\,\mathrm u^{-1}$) into wavenumbers, $\tilde\nu = 5140.487\sqrt\lambda$.

!!! example "H₂ harmonic wavenumber from a force constant"
    For H₂, $\mu = m_p/2 = 0.503\,638$ u (nuclear masses; using atomic masses changes the fourth digit). A force constant $k = 0.37\,E_h/a_0^2$ gives

    $$
    \tilde\nu = 5140.487\sqrt{0.37/0.503\,638} = 4406\ \mathrm{cm^{-1}} ,
    $$

    The value of $k$ is illustrative, chosen only to exercise the formula; [[geometry-optimization]] and Part 3 compute force constants from actual surfaces.

## Thermal energies

| At $T$ = 298.15 K | Value |
|---|---|
| $k_BT$ | 9.441 849 × 10⁻⁴ $E_h$ = 0.592 485 kcal/mol = 25.692 6 meV = 207.224 6 cm$^{-1}$ |
| $R$ | 1.987 204 × 10⁻³ kcal mol$^{-1}$ K$^{-1}$ = 8.314 462 6 J mol$^{-1}$ K$^{-1}$ |

A vibrational mode with $\tilde\nu \gg 207$ cm$^{-1}$ is essentially unexcited at room temperature; low-frequency modes below about 200 cm$^{-1}$ are thermally populated.

## Source

All numbers computed from CODATA 2022 constants (`scipy.constants`, SciPy 1.18.1) in `part9_reference.py`, section B, and checked against the `scipy.constants` hartree relationships (agreement to $10^{-9}$ or better). The thermochemical calorie (4.184 J) and debye ($10^{-21}/c$ C m) are as in [[atomic-units]].
