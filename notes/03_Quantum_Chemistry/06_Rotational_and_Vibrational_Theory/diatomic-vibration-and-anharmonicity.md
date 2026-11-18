---
id: diatomic-vibration-and-anharmonicity
title: Vibration of a diatomic molecule - harmonic limit, anharmonicity and dissociation energies
summary: Nuclear motion on a diatomic curve U(R) separates into translation, rotation and vibration. The harmonic limit gives ν_e = (k_e/μ)^{1/2}/2π with k_e = U''(R_e); anharmonicity adds −ω_e x_e(v+½)², shrinks level spacings and limits the number of bound levels. Covers the Morse potential, IR selection rules, fundamentals, overtones and hot bands, isotope shifts, thermal populations and D_e versus D₀. Worked examples: Levine's CO force constant and isotope shift, and the full FCI/cc-pVQZ curve of H₂ solved for its vibrational levels, which land 10-24 cm⁻¹ above experiment.
status: in-progress
kind: theory
level: intermediate
tags: [vibration, diatomic, anharmonicity, morse-potential, force-constant, dissociation-energy, zero-point-energy, isotope-effect]
prerequisites: [born-oppenheimer-approximation, harmonic-oscillator-analytic-solution, two-particle-systems-and-reduced-mass]
related: [numerov-method, rigid-rotor-and-rovibrational-levels, harmonic-vibrational-analysis, zero-point-energy-and-thermochemistry, energy-and-unit-conversions, wkb-connection-formulas-and-quantization]
order: 10
date: 2026-11-17
---

## From the electronic curve to nuclear motion

In the Born–Oppenheimer approximation ([[born-oppenheimer-approximation]]) the nuclei of a diatomic molecule move on the electronic energy $U(R)$, which includes the nuclear repulsion. The two-nucleus Schrödinger equation separates, exactly as any two-body problem with a central interaction ([[two-particle-systems-and-reduced-mass]]), into free translation of the centre of mass and internal motion of a particle of reduced mass

$$
\mu = \frac{m_am_b}{m_a + m_b}
$$

in the potential $U(R)$. Since $U$ depends only on $R$, the internal wave function is $\psi_{\text{int}} = R^{-1}F(R)\,Y_J^M(\theta,\phi)$ and

$$
-\frac{\hbar^2}{2\mu}F''(R) + \Big[U(R) + \frac{J(J+1)\hbar^2}{2\mu R^2}\Big]F(R) = E_{\text{int}}F(R) .
$$

$J$ and $M$ are rotational quantum numbers ([[rigid-rotor-and-rovibrational-levels]]); the number of nodes $v$ of $F$ is the vibrational quantum number. This note takes $J = 0$.

The most fundamental route is: compute $U$ at many $R$, fit it (splines), and solve the radial equation numerically ([[numerov-method]]). The rest of the note is the analytic approximation to that route.

## Harmonic limit

Expand $U$ about its minimum $R_e$, where $U'(R_e) = 0$:

$$
U(R) = U(R_e) + \tfrac12k_e(R - R_e)^2 + \tfrac16U'''(R_e)(R - R_e)^3 + \cdots,
\qquad k_e = U''(R_e) .
$$

Keeping the quadratic term gives a harmonic oscillator of mass $\mu$:

$$
E_{\text{vib}} \approx \big(v + \tfrac12\big)h\nu_e,\qquad \nu_e = \frac{1}{2\pi}\sqrt{\frac{k_e}{\mu}},\qquad v = 0,1,2,\dots
$$

$\nu_e$ is the equilibrium (harmonic) frequency; spectroscopists quote $\omega_e = \nu_e/c$ in cm$^{-1}$. Because $U(R)$ is independent of the nuclear masses, **isotopologues share $k_e$**, and $\nu_e\propto\mu^{-1/2}$.

## Anharmonicity

Real curves are softer than the parabola at large $R$ and harder at small $R$, so the levels crowd together as $v$ increases and only finitely many are bound. Second-order perturbation theory in the cubic and quartic terms (Levine, *Molecular Spectroscopy*, cited in Levine Sec. 13.2) gives the series

$$
G(v) = \frac{E_{\text{vib}}}{hc} = \omega_e\big(v + \tfrac12\big) - \omega_ex_e\big(v + \tfrac12\big)^2 + \omega_ey_e\big(v + \tfrac12\big)^3 - \cdots,
$$

with $\omega_ex_e > 0$ for nearly all molecules. The spacing between neighbouring levels is

$$
\Delta G\big(v + \tfrac12\big) = G(v+1) - G(v) = \omega_e - 2\omega_ex_e(v + 1) + \cdots,
$$

so the second difference is $-2\omega_ex_e$.

**Morse potential.** $U(R) = U(R_e) + D_e\big[1 - e^{-a(R - R_e)}\big]^2$ has $k_e = 2a^2D_e$, so $a = (k_e/2D_e)^{1/2} = 2\pi\nu_e(\mu/2D_e)^{1/2}$. Its Schrödinger equation is solvable, and the series above terminates exactly at the quadratic term with

$$
\omega_ex_e = \frac{\omega_e^2}{4D_e}\quad(\text{all in cm}^{-1}),\qquad
v_{\max} = \Big\lfloor\frac{2D_e}{\omega_e} - \frac12\Big\rfloor .
$$

## Spectra

- **Selection rule.** In the harmonic, linear-dipole approximation, absorption and emission require $\Delta v = \pm1$ and a dipole moment that changes with $R$. Homonuclear diatomics (H₂, N₂) have no vibrational IR spectrum.
- **Fundamental.** The $0\to1$ band lies at $\tilde\nu = \omega_e - 2\omega_ex_e$, below $\omega_e$. Measured IR bands are fundamentals, not harmonic frequencies.
- **Overtones and hot bands.** $\Delta v = 2, 3,\dots$ appear weakly through anharmonicity; $1\to2$, $2\to3$ (hot bands) appear when excited levels are populated.
- **Populations.** $N_i/N_j = (g_i/g_j)e^{-(E_i - E_j)/kT}$. At 298 K, $kT/hc = 207$ cm$^{-1}$ ([[energy-and-unit-conversions]]), so CO ($\approx2143$ cm$^{-1}$) has $N_1/N_0 = 3\times10^{-5}$, while a 214 cm$^{-1}$ vibration (the order of I₂) has $N_1/N_0 = 0.36$.

## Dissociation energies

$D_e$ is measured from the bottom of the well; $D_0$ from the $v = 0$ level:

$$
D_0 = D_e - G(0),\qquad G(0) \approx \tfrac12\omega_e - \tfrac14\omega_ex_e .
$$

$D_0$ is the observable (spectroscopic or thermochemical) bond energy; $D_e$ is what an electronic-structure calculation gives directly. The polyatomic generalization is in [[zero-point-energy-and-thermochemistry]].

## Worked examples

!!! example "Force constant of CO from its IR band (Levine Sec. 4.3)"
    The strongest IR band of $^{12}$C$^{16}$O is at 2143 cm$^{-1}$. Treating it as $\omega_e$ (harmonic approximation): $\nu = 6.425\times10^{13}$ s$^{-1}$, $\mu = (12\times15.994\,92/27.994\,92)\,\mathrm u = 1.1385\times10^{-26}$ kg, and

    $$
    k = 4\pi^2\nu^2\mu = 1855\ \mathrm{N/m}.
    $$

    The zero-point energy is $\tfrac12h\nu = 2.13\times10^{-20}$ J (1072 cm$^{-1}$). For $^{13}$C$^{16}$O, same $k$ and $\mu = 1.1910\times10^{-26}$ kg give $\nu = 6.28\times10^{13}$ s$^{-1}$. All three agree with Levine's answers.

!!! example "H₂ from first principles: FCI/cc-pVQZ curve plus Numerov"
    $U(R)$ was computed by full CI in the cc-pVQZ basis at 71 distances from 0.6 to 10 bohr and fitted by a cubic spline. Nuclear masses give $\mu = m_p/2 = 918.08\,m_e$.

    | Quantity | FCI/cc-pVQZ | Reference |
    |---|---:|---|
    | $R_e$ | 0.741 86 Å | 0.741 Å (Levine) |
    | $k_e$ | 0.369 08 $E_h/a_0^2$ | |
    | $\omega_e$ from $k_e$ | 4400.5 cm$^{-1}$ | 4403.2 (Levine) |
    | $D_e$ | 38 168 cm$^{-1}$ | 38 297 (Levine) |
    | $D_0 = D_e - G(0)$ | 35 988 cm$^{-1}$ (4.462 eV) | |

    Levels from the Numerov solution, measured from the minimum (cm$^{-1}$):

    | $v$ | 0 | 1 | 2 | 3 | 4 | 5 |
    |---|---:|---:|---:|---:|---:|---:|
    | FCI + Numerov | 2179.9 | 6343.1 | 10271.5 | 13969.7 | 17440.9 | 20685.8 |
    | experiment (Levine) | 2170.1 | 6331.2 | 10257.2 | 13952.4 | 17420.4 | 20662.0 |
    | difference | 9.9 | 11.9 | 14.3 | 17.3 | 20.4 | 23.8 |

    - **Spacings.** $\Delta G = 4163.2, 3928.3, 3698.3, 3471.2, 3244.9$ cm$^{-1}$; the second differences, $-235$ to $-226$ cm$^{-1}$, give $\omega_ex_e\approx115$ cm$^{-1}$. A cubic fit of $G(v)$, $v\le5$, gives $\omega_e = 4412.8$, $\omega_ex_e = 123.8$, $\omega_ey_e = 0.97$ cm$^{-1}$.
    - **Errors.** The computed levels lie above experiment by an amount that grows with $v$. The curve is too shallow by 130 cm$^{-1}$ in $D_e$ (basis set), and the Born–Oppenheimer curve omits adiabatic and nonadiabatic corrections, which matter for the lightest molecule. Neither error is analysed further here.
    - **Morse comparison.** The Morse curve with Levine's $D_e$ and $\omega_e$ ([[numerov-method]]) gives 2169.96 … 20389.0 cm$^{-1}$: closer for $v = 0$, but too low by 270 cm$^{-1}$ at $v = 5$, because one exponential cannot follow the true curve.

## Source

Levine, *Quantum Chemistry* (7th ed., Pearson, 2014), Sec. 4.3, pp. 71-74, Eqs. (4.58)-(4.64) and Example (CO); Sec. 13.2, pp. 347-352, Eqs. (13.13)-(13.28) and the Morse example (Morse parameters, experimental H₂ levels). Calculations in `part3_batchA.py`, sections B and C (PySCF 2.15.1).
