---
id: electromagnetic-units-and-magnitudes
title: Dimensions, units and magnitudes of electromagnetic quantities - SI and atomic units of fields, moments and response properties, and conversion to Gaussian (esu) values
summary: Starting from the Lorentz force and Maxwell's equations, the dimensions in mass, charge, length and time of every quantity in this chapter follow: E, B, ε₀, μ₀, φ, A, P, D, M, H, S, and the multipoles. The atomic units of fields, moments and response properties (α, β, γ, magnetizability) are given with their SI values. The atomic field units are enormous: 5.14 × 10¹¹ V m⁻¹ (a laser intensity of 3.5 × 10¹⁶ W cm⁻²) and 2.35 × 10⁵ T. The conversion of polarizabilities and hyperpolarizabilities to the Gaussian (esu) values still common in the literature is derived from the dipole and field factors. Checked: the dimensional relations, 1 au of α, β, γ in esu, and a dimensional slip in NRS's magnetic-field unit.
status: in-progress
kind: reference
level: introductory
tags: [units, dimensional-analysis, atomic-units, gaussian-units, esu, field-strength, hyperpolarizability-units, magnetizability, unit-conversion]
prerequisites: [maxwell-equations-in-matter, atomic-units]
related: [energy-and-unit-conversions, physical-constants, polarizabilities-and-dispersion-coefficients, electric-and-magnetic-multipole-moments, charged-particle-in-an-electromagnetic-field]
conventions: [si-units, atomic-units]
order: 110
date: 2026-11-25
---

This note bridges two unit systems: SI, and SI-based (Hartree) atomic units with $4\pi\varepsilon_0 = 1$. Equations of this chapter are in SI. Dimensions are written in mass M, charge Q, length L, time T. $[X]$ denotes the dimension of $X$.

## Dimensions

**The fields.** From the Lorentz force $\mathbf F = q(\mathbf E + \mathbf v\times\mathbf B)$ ([[charged-particle-in-an-electromagnetic-field]]), with $[\mathbf F] = \mathrm{M\,L\,T^{-2}}$:

$$
[\mathbf E] = \mathrm{M\,Q^{-1}L\,T^{-2}},\qquad [\mathbf B] = \mathrm{M\,Q^{-1}T^{-1}}.
$$

**Constants and auxiliary fields.** The inhomogeneous Maxwell equations, with $[\rho] = \mathrm{Q\,L^{-3}}$ and $[\mathbf j] = \mathrm{Q\,L^{-2}T^{-1}}$, then fix the rest (NRS Sec. 3.5.6):

| quantity | dimension | SI unit | how it follows |
|---|---|---|---|
| $\varepsilon_0$ | $\mathrm{M^{-1}Q^2L^{-3}T^2}$ | F m⁻¹ | $\nabla\cdot\mathbf E = \rho/\varepsilon_0$ |
| $\mu_0$ | $\mathrm{M\,Q^{-2}L}$ | H m⁻¹ = N A⁻² | $\nabla\times\mathbf B - \varepsilon_0\mu_0\partial_t\mathbf E = \mu_0\mathbf j$ |
| $\varepsilon_0\mu_0$ | $\mathrm{L^{-2}T^2}$ | s² m⁻² | $= 1/c^2$ |
| $\mathbf P$, $\mathbf D$ | $\mathrm{Q\,L^{-2}}$ | C m⁻² | surface charge density |
| $\mathbf M$, $\mathbf H$ | $\mathrm{Q\,L^{-1}T^{-1}}$ | A m⁻¹ | surface current density |
| $\phi$ | $\mathrm{M\,Q^{-1}L^2T^{-2}}$ | V | $\mathbf E = -\nabla\phi - \partial_t\mathbf A$ |
| $\mathbf A$ | $\mathrm{M\,Q^{-1}L\,T^{-1}}$ | T m = V s m⁻¹ | $\mathbf B = \nabla\times\mathbf A$ |
| $\mathbf S$, intensity | $\mathrm{M\,T^{-3}}$ | W m⁻² | energy per area per time |
| electric $2^n$-pole | $\mathrm{Q\,L^n}$ | C mⁿ | $\int\rho\,r^n$ |
| magnetic $2^n$-pole | $\mathrm{Q\,L^{n+1}T^{-1}}$ | A mⁿ⁺¹ | $\int\mathbf r^{n-1}(\mathbf r\times\mathbf j)$ |

The magnetic dipole ($n = 1$) has dimension Q L² T⁻¹, i.e. A m² = J T⁻¹, as a current loop of area L² should.

## Atomic units of electromagnetic quantities

**Base units.** Mass $m_e$, charge $e$, length $a_0$, time $\hbar/E_h$. Every quantity below is a product of these. Values are from CODATA 2022.

| quantity | atomic unit | SI value |
|---|---|---|
| electric field | $E_h/(ea_0)$ | $5.142207\times10^{11}$ V m⁻¹ |
| magnetic field | $\hbar/(ea_0^2)$ | $2.350518\times10^{5}$ T |
| electric dipole | $ea_0$ | $8.478354\times10^{-30}$ C m = 2.541746 D |
| electric quadrupole | $ea_0^2$ | $4.486552\times10^{-40}$ C m² |
| magnetic dipole | $e\hbar/m_e$ (= $2\mu_B$) | $1.854802\times10^{-23}$ J T⁻¹ |
| polarizability $\alpha$ | $e^2a_0^2/E_h$ | $1.648777\times10^{-41}$ C² m² J⁻¹ |
| first hyperpolarizability $\beta$ | $e^3a_0^3/E_h^2$ | $3.206361\times10^{-53}$ C³ m³ J⁻² |
| second hyperpolarizability $\gamma$ | $e^4a_0^4/E_h^3$ | $6.235380\times10^{-65}$ C⁴ m⁴ J⁻³ |
| magnetizability $\xi$ | $e^2a_0^2/m_e$ | $7.891037\times10^{-29}$ J T⁻² |

The pattern for response properties: a property $X$ defined by $\mu = XF^k$ has atomic unit $(ea_0)(ea_0/E_h)^k$. Each power of the field brings one factor $ea_0/E_h$.

**A slip in NRS.** NRS Sec. 3.5.6 writes the field unit as $\hbar/(ea_0)$. That combination has dimension T m, not T: its value is $1.244\times10^{-5}$ T m. The correct unit is $\hbar/(ea_0^2)$, which does give the quoted $2.3505\times10^5$ T.

**Magnitudes.** The field felt by the electron at the Bohr radius in hydrogen is the atomic unit. Compare (NRS Sec. 3.5.6):

| field | value | in atomic units |
|---|---|---:|
| near a power line | up to $10^4$ V m⁻¹ | $2\times10^{-8}$ |
| breakdown of air | $3.0\times10^6$ V m⁻¹ | $5.8\times10^{-6}$ |
| Earth's magnetic field | about 60 µT | $2.6\times10^{-10}$ |
| NMR magnet | about 10 T | $4.3\times10^{-5}$ |
| strongest nondestructive lab field | about 100 T | $4.3\times10^{-4}$ |
| magnetic white dwarfs | about $10^5$ T | about 1 |
| magnetars | $10^8$–$10^{11}$ T | $4\times10^2$–$4\times10^5$ |

**Intensities.** A light wave whose peak field is 1 au carries the intensity $\tfrac12\varepsilon_0cE_0^2 = 3.51\times10^{16}$ W cm⁻² (see [[electromagnetic-waves-and-polarization]]). Only strong-field lasers reach this. Ordinary spectroscopy is deep in the perturbative regime, which is why the response expansion of [[polarizabilities-and-dispersion-coefficients]] works.

## Conversion to Gaussian (esu) units

**Why it is needed.** Much of the nonlinear-optics literature reports $\alpha$, $\beta$, $\gamma$ in Gaussian "esu". The conversion follows from two factors:

- **Dipole.** 1 D = $10^{-18}$ statC cm = $10^{-21}/c$ C m (with $c$ in m s⁻¹), so 1 C m = $c\times10^{-18}\times10^{21}$ statC cm = $2.998\times10^{11}$ statC cm.
- **Field.** 1 statV cm⁻¹ = 29979.2458 V m⁻¹.

For $\mu = XF^k$:

$$
X_{\rm esu} = X_{\rm SI}\,\frac{2.99792458\times10^{11}}{(1/29979.2458)^k}.
\label{esu}
$$

**Values.** Applied to the atomic units:

| property | 1 au in esu | Gaussian dimension |
|---|---|---|
| $\alpha$ ($k = 1$) | $1.48185\times10^{-25}$ cm³ | volume |
| $\beta$ ($k = 2$) | $8.63922\times10^{-33}$ esu | cm⁵ statC⁻¹ |
| $\gamma$ ($k = 3$) | $5.03670\times10^{-40}$ esu | cm⁶ statC⁻² |

These are the values commonly quoted.

**Polarizability volume.** For $\alpha$ the conversion is just $\alpha_{\rm SI}/(4\pi\varepsilon_0)$ in cm³, the polarizability volume. In atomic units it is $a_0^3 = 0.148185$ Å³. This is why "α in Å³" and "α in au" differ by that factor, and why the Clausius–Mossotti formula of [[local-field-clausius-mossotti-and-reaction-field]] reads $\frac{\varepsilon - 1}{\varepsilon + 2} = \frac{4\pi}{3}\mathcal N\alpha'$ with the volume $\alpha'$.

**Expansion conventions.** Hyperpolarizabilities come with a second ambiguity: the expansion convention. $\mu = \alpha F + \tfrac12\beta F^2 + \tfrac16\gamma F^3$ (Taylor, used here and in [[polarizabilities-and-dispersion-coefficients]]) and $\mu = \alpha F + \beta F^2 + \gamma F^3$ (power series) differ by factors 2 and 6. Eq. [[#esu]] converts units only. A literature value must also be checked for its convention.

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Sec. 3.5.6. The table of atomic units, the esu factors, the expansion-convention remark and the intensity are standard material computed from CODATA 2022 constants (`scipy.constants`), not taken from NRS. NRS cite D. H. Whiffen, Pure Appl. Chem. 50, 75 (1978) for SI-based atomic units (to verify, not consulted). The calculations are in `Claude outputs/part1_fields_batchD.py`, section I.
