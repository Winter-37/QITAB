---
id: hyperfine-splitting-hydrogen
title: Hyperfine splitting of the hydrogen ground state
summary: The magnetic interaction between the proton and electron spins splits the 1s level into a singlet (F = 0) and a triplet (F = 1). For l = 0 only the contact term of the dipole field contributes, the good states are eigenstates of the total spin, and the gap is (4/3) g_p (m/m_p) α⁴mc² = 5.88 × 10⁻⁶ eV, the 21 cm line. Numbers are recomputed, with the reduced-mass and electron g-factor corrections that bring 1421.2 MHz to within 0.006 percent of the measured 1420.4 MHz.
status: in-progress
kind: derivation
level: intermediate
tags: [hyperfine-structure, hydrogen-atom, spin-spin-coupling, 21-cm-line, proton-magnetic-moment, contact-interaction, singlet-triplet, degenerate-perturbation-theory, griffiths]
prerequisites: [hydrogen-fine-structure, degenerate-perturbation-theory, addition-of-angular-momenta]
related: [spin-one-half, zeeman-effect, exchange-symmetry-spin-and-symmetrization-principle]
order: 18
date: 2026-11-14
---

## The interaction

The proton is a magnetic dipole,

$$
\boldsymbol\mu_p = \frac{g_pe}{2m_p}\,\mathbf S_p ,\qquad g_p = 5.5857 ,
$$

weaker than the electron's moment $\boldsymbol\mu_e = -(e/m_e)\mathbf S_e$ by the mass ratio. A point dipole $\boldsymbol\mu$ at the origin produces the field

$$
\mathbf B = \frac{\mu_0}{4\pi r^3}\,\big[3(\boldsymbol\mu\cdot\hat{\mathbf r})\hat{\mathbf r} - \boldsymbol\mu\big] + \frac{2\mu_0}{3}\,\boldsymbol\mu\,\delta^3(\mathbf r) .
$$

The delta-function term is the field inside the dipole and is easy to overlook. The energy of the electron's moment in the proton's field, $H'_{hf} = -\boldsymbol\mu_e\cdot\mathbf B$, is

$$
H'_{hf} = \frac{\mu_0g_pe^2}{8\pi m_pm_e}\,\frac{3(\mathbf S_p\cdot\hat{\mathbf r})(\mathbf S_e\cdot\hat{\mathbf r}) - \mathbf S_p\cdot\mathbf S_e}{r^3}
+ \frac{\mu_0g_pe^2}{3m_pm_e}\,\mathbf S_p\cdot\mathbf S_e\,\delta^3(\mathbf r) .
$$

## First-order energy for l = 0

In a state with $l = 0$ the spatial wave function is spherically symmetric. The first term then averages to zero, because the angular average of $3\hat r_i\hat r_j$ is $\delta_{ij}$:

$$
\int\big[3(\mathbf a\cdot\hat{\mathbf r})(\mathbf b\cdot\hat{\mathbf r}) - \mathbf a\cdot\mathbf b\big]\sin\theta\,d\theta\,d\phi = 0 .
$$

Only the contact term survives. With $|\psi_{100}(0)|^2 = 1/(\pi a^3)$,

$$
E^1_{hf} = \frac{\mu_0g_pe^2}{3\pi m_pm_ea^3}\,\langle\mathbf S_p\cdot\mathbf S_e\rangle .
$$

This is spin-spin coupling: the energy depends on the relative orientation of the two spins. Only $s$ states feel the contact term, since $\psi(0) = 0$ for $l>0$; there the dipole-dipole term and the coupling of the proton moment to the orbital motion take over.

## Good states and the splitting

The $1s$ level is four-fold degenerate in the spin space of the two particles. $\mathbf S_p\cdot\mathbf S_e$ does not commute with the individual spins, but it commutes with the total spin

$$
\mathbf F = \mathbf S_e + \mathbf S_p ,
$$

so the good states are the eigenstates of $F^2$ and $F_z$: the triplet and the singlet ([[addition-of-angular-momenta]]). Squaring $\mathbf F$,

$$
\mathbf S_p\cdot\mathbf S_e = \tfrac12\big(F^2 - S_e^2 - S_p^2\big)
= \begin{cases}\ \ \tfrac14\hbar^2 & \text{triplet, } F = 1\\[2pt] -\tfrac34\hbar^2 & \text{singlet, } F = 0 .\end{cases}
$$

Eliminating $\mu_0 = 1/(\varepsilon_0c^2)$ and $e^2/(4\pi\varepsilon_0) = \hbar^2/(m_ea)$,

$$
E^1_{hf} = \frac{4g_p\hbar^4}{3m_pm_e^2c^2a^4}\times
\begin{cases} +\tfrac14 & \text{triplet}\\[2pt] -\tfrac34 & \text{singlet} .\end{cases}
$$

The coupling raises the triplet and lowers the singlet, so the ground state of hydrogen is the singlet, with antiparallel spins. The gap is

$$
\boxed{\,\Delta E = \frac{4g_p\hbar^4}{3m_pm_e^2c^2a^4} = \frac43\,g_p\,\frac{m_e}{m_p}\,\alpha^4m_ec^2\,}
$$

It is of the same order in $\alpha$ as fine structure and smaller by $m_e/m_p$. The trace of the perturbation over the four states vanishes, $3\times\tfrac14 - \tfrac34 = 0$, so the centre of gravity of the level does not move.

!!! example "The 21 cm line"

    With CODATA constants:

    | Quantity | Value |
    |---|---|
    | $\Delta E$ (formula above) | $5.877\times10^{-6}$ eV |
    | Frequency $\Delta E/h$ | 1421.16 MHz |
    | Wavelength $c/\nu$ | 21.09 cm |
    | Ratio to the $n = 2$ fine-structure splitting | 0.13 |

    The measured frequency is 1420.406 MHz. Two corrections close most of the gap.

    | Step | Frequency (MHz) |
    |---|---|
    | lowest order, infinite proton mass | 1421.160 |
    | $|\psi(0)|^2$ with the reduced mass, factor $(1 + m_e/m_p)^{-3}$ | 1418.840 |
    | electron $g$-factor, factor $g_e/2 = 1.00116$ | 1420.485 |
    | measured | 1420.406 |

    The remaining 0.08 MHz (0.006 percent) comes from higher-order relativistic, radiative and proton-structure effects that this treatment does not include. The measured value is quoted from memory and was not checked against a database here.

!!! example "Other two-body systems"

    The same contact formula applies to any $1s$ bound state of two spin-$\tfrac12$ particles after replacing $g_p$, $m_p$ and the reduced mass: $\Delta E = \tfrac43\,g_N(m_e/m_N)\,\alpha^4m_ec^2\,(\mu/m_e)^3$.

    | System | $\Delta E$ (eV) | Frequency |
    |---|---|---|
    | hydrogen ($e^-p$) | $5.868\times10^{-6}$ | 1418.8 MHz |
    | muonium ($e^-\mu^+$) | $1.842\times10^{-5}$ | 4453.8 MHz |
    | positronium ($e^-e^+$) | $4.830\times10^{-4}$ | 116.8 GHz |

    These are lowest-order values with $g = 2$ for the muon and positron. For positronium the result is known to be far from experiment, because virtual pair annihilation adds a contribution of the same order that the formula does not contain (Griffiths makes this point in the corresponding problem).

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 7.5, Eqs. (7.89)-(7.98), Fig. 7.12 (described); Problems 7.31-7.36. Page numbers are not given because the PDF used is an e-book rendering without print pagination. Griffiths quotes $5.88\times10^{-6}$ eV, 1420 MHz and 21 cm.

Sakurai's Sec. 5.3 treats fine structure and the Zeeman effect; the hyperfine splitting is not derived there, so this note rests on Griffiths alone.

All numbers, including the reduced-mass and $g$-factor steps and the muonium and positronium values, are computed in `griffiths/ch07_perturbation.py` (sections D and D2) with SciPy CODATA constants; the correction steps are my own bookkeeping, not taken from the book.
