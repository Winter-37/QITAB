---
id: physical-constants
title: Physical constants (CODATA 2022)
summary: The SI defining constants (exact since 2019) and the measured constants that enter quantum chemistry, with their atomic-unit meaning and relative uncertainty, as provided by scipy.constants (CODATA 2022). Includes the identities E_h = α²m_ec² and a_0 = ħ/(m_ecα) as consistency checks.
status: in-progress
kind: reference
level: introductory
tags: [constants, codata, si-units, atomic-units]
prerequisites: []
related: [atomic-units, energy-and-unit-conversions]
order: 10
date: 2026-11-17
---

## Defining constants of the SI (exact)

Since the 2019 redefinition of the SI these have fixed numerical values, so they carry no uncertainty.

| Constant | Symbol | Value |
|---|---|---|
| speed of light in vacuum | $c$ | 299 792 458 m s$^{-1}$ |
| Planck constant | $h$ | $6.626\,070\,15\times10^{-34}$ J s |
| elementary charge | $e$ | $1.602\,176\,634\times10^{-19}$ C |
| Boltzmann constant | $k_B$ | $1.380\,649\times10^{-23}$ J K$^{-1}$ |
| Avogadro constant | $N_A$ | $6.022\,140\,76\times10^{23}$ mol$^{-1}$ |

Derived and also exact: $\hbar = h/2\pi = 1.054\,571\,817\ldots\times10^{-34}$ J s, the gas constant $R = N_Ak_B = 8.314\,462\,618\ldots$ J mol$^{-1}$ K$^{-1}$, and the Faraday constant $F = N_Ae$.

## Measured constants

Values rounded from `scipy.constants` (SciPy 1.18, CODATA 2022). "Atomic unit" says which constant is set to 1 in atomic units ([[atomic-units]]).

| Constant | Symbol | Value | Rel. unc. | Atomic unit |
|---|---|---|---|---|
| electron mass | $m_e$ | $9.109\,383\,714\times10^{-31}$ kg | $3\times10^{-10}$ | mass |
| proton mass | $m_p$ | $1.672\,621\,926\times10^{-27}$ kg | $3\times10^{-10}$ | $1836.152\,673\,4\,m_e$ |
| atomic mass constant (dalton) | $m_u$ | $1.660\,539\,069\times10^{-27}$ kg | $3\times10^{-10}$ | $1822.888\,486\,m_e$ |
| fine-structure constant | $\alpha$ | $7.297\,352\,564\times10^{-3}$, $1/\alpha = 137.035\,999\,18$ | $1.5\times10^{-10}$ | $1/c$ in a.u. |
| vacuum permittivity | $\varepsilon_0$ | $8.854\,187\,819\times10^{-12}$ F m$^{-1}$ | $1.6\times10^{-10}$ | $4\pi\varepsilon_0 = 1$ |
| Bohr radius | $a_0$ | $5.291\,772\,105\times10^{-11}$ m | $1.6\times10^{-10}$ | length |
| Hartree energy | $E_h$ | $4.359\,744\,722\times10^{-18}$ J | $1.1\times10^{-12}$ | energy |
| Rydberg constant | $R_\infty$ | $10\,973\,731.568$ m$^{-1}$ | $1.1\times10^{-12}$ | $\tfrac12E_h/(hc)$ |
| Bohr magneton | $\mu_B$ | $9.274\,010\,066\times10^{-24}$ J T$^{-1}$ | $3\times10^{-10}$ | $\tfrac12$ a.u. |
| nuclear magneton | $\mu_N$ | $5.050\,783\,739\times10^{-27}$ J T$^{-1}$ | $3\times10^{-10}$ | |
| electron $g$ factor | $g_e$ | $-2.002\,319\,304\,36$ | $1.8\times10^{-13}$ | |
| atomic unit of time | $\hbar/E_h$ | $2.418\,884\,326\,6\times10^{-17}$ s | $1.1\times10^{-12}$ | time |
| atomic unit of force | $E_h/a_0$ | $8.238\,723\,504\times10^{-8}$ N | $1.6\times10^{-10}$ | force |
| atomic unit of electric field | $E_h/(ea_0)$ | $5.142\,206\,751\times10^{11}$ V m$^{-1}$ | $1.6\times10^{-10}$ | field |
| atomic unit of dipole moment | $ea_0$ | $8.478\,353\,620\times10^{-30}$ C m | $1.6\times10^{-10}$ | dipole |

The relative uncertainties are the CODATA standard uncertainties divided by the value, rounded.

## Relations among them

The atomic units are not independent constants. With $\hbar = m_e = e = 4\pi\varepsilon_0 = 1$:

$$
E_h = \alpha^2m_ec^2 = \frac{m_ee^4}{(4\pi\varepsilon_0)^2\hbar^2},\qquad
a_0 = \frac{\hbar}{m_ec\alpha} = \frac{4\pi\varepsilon_0\hbar^2}{m_ee^2},\qquad
\alpha = \frac{e^2}{4\pi\varepsilon_0\hbar c},\qquad R_\infty = \frac{\alpha^2m_ec}{2h} .
$$

So the speed of light in atomic units is $c = 1/\alpha \approx 137.036$, the number that appears in relativistic corrections such as the fine structure ([[hydrogen-fine-structure]]).

Both $E_h = \alpha^2m_ec^2$ and $a_0 = \hbar/(m_ec\alpha)$ reproduce the tabulated values to $10^{-11}$ (relative), the precision of the rounded inputs (`part9_reference.py`, section A).

!!! warning "Old tables"
    Szabo's Table 2.1 and many program manuals use older CODATA sets. Differences are in the sixth or seventh digit for $E_h$ in eV or kcal/mol. When reproducing a published number to all printed digits, use the constants that the authors used. PySCF takes its values from its own `pyscf.data.nist` module, which in PySCF 2.15 holds an older set: `HARTREE2EV = 27.21138602` and `BOHR = 0.52917721092` Å, against 27.211386246 eV and 0.529177211 Å from CODATA 2022. The difference ($10^{-8}$ relative) only matters when matching printed digits.

## Source

CODATA 2022 recommended values as distributed in `scipy.constants` (SciPy 1.18.1), read and checked in `part9_reference.py`, section A. PySCF values read from `pyscf.data.nist` (PySCF 2.15.1). The SI defining constants are those of the 2019 SI. Relations are standard; compare Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996), Sec. 2.1.1, Table 2.1, as summarized in [[atomic-units]].
