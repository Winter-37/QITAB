---
id: helium-ground-state-variational
title: The ground state of helium by the variational method
summary: The simplest two-electron calculation. A product of two hydrogenic 1s functions gives −2.75 E_h in first order; letting the exponent vary gives the effective charge Z − 5/16 and E = −(Z − 5/16)², which for helium is −2.848 E_h (−77.5 eV) against −2.904 E_h. Covers the evaluation of ⟨1/r₁₂⟩ = 5Z/8, the screening interpretation, the virial check, the isoelectronic series from H⁻ to Be²⁺ (where the bound fails to bind H⁻), and what the remaining error means.
status: in-progress
kind: derivation
level: intermediate
tags: [helium-atom, variational-principle, effective-nuclear-charge, screening, electron-repulsion, two-electron-atoms, hydride-ion, correlation-energy, griffiths, sakurai]
prerequisites: [variational-principle, hydrogen-atom, helium-atom-independent-particle-model]
related: [coulomb-cusp-and-helium-expansions, hellmann-feynman-and-virial-theorems, atomic-units, rayleigh-schrodinger-perturbation-theory, hydrogen-molecule-ion-variational]
order: 50
date: 2026-11-14
---

## The problem

For a nucleus of charge $Z$ at rest, in atomic units ([[atomic-units]]),

$$
H = -\tfrac12\nabla_1^2 - \tfrac12\nabla_2^2 - \frac{Z}{r_1} - \frac{Z}{r_2} + \frac{1}{r_{12}} .
$$

The ground state is a spin singlet with a symmetric spatial function ([[helium-atom-independent-particle-model]]), so only the spatial part is needed. The electron repulsion $V_{ee} = 1/r_{12}$ prevents an exact solution. The accurate nonrelativistic energy for helium is $-2.903724\ E_h = -79.01$ eV; Griffiths quotes the measured $-78.975$ eV and Sakurai $-79.005$ eV.

## Zeroth and first order

Without $V_{ee}$ the ground state is a product of hydrogenic functions,

$$
\psi_0(\mathbf r_1,\mathbf r_2) = \frac{Z^3}{\pi}\,e^{-Z(r_1+r_2)} ,\qquad E_0 = -Z^2 ,
$$

which is $-4\ E_h = -108.8$ eV for helium, 38 percent too low. The expectation value of the full Hamiltonian in this state is

$$
\langle H\rangle = -Z^2 + \langle V_{ee}\rangle .
$$

This is both the first-order perturbation result and, by the variational principle ([[variational-principle]]), an upper bound.

**Evaluating the repulsion.** $\langle V_{ee}\rangle$ is the electrostatic energy of the charge density $\rho(r) = (Z^3/\pi)e^{-2Zr}$ of one electron in the potential of the other. A spherical density produces the potential

$$
\Phi(r) = \frac1r\int_0^r\rho\,4\pi r'^2dr' + \int_r^\infty\rho\,4\pi r'\,dr' = \frac1r - \Big(Z + \frac1r\Big)e^{-2Zr} ,
$$

and

$$
\langle V_{ee}\rangle = \int\rho(r)\,\Phi(r)\,d^3r
= 4Z^3\int_0^\infty\Big[r\,e^{-2Zr} - (Zr^2 + r)\,e^{-4Zr}\Big]dr
= 4Z^3\Big[\frac{1}{4Z^2} - \frac{1}{32Z^2} - \frac{1}{16Z^2}\Big] = \frac58\,Z .
$$

Griffiths obtains the same number by integrating over the angle between $\mathbf r_1$ and $\mathbf r_2$ with the law of cosines, and Sakurai by the Legendre expansion of $1/r_{12}$, of which only the $l = 0$ term survives. For helium

$$
\langle H\rangle = -4 + \tfrac54 = -2.75\ E_h = -74.83\ \text{eV} ,
$$

now 5 percent too high.

## Varying the exponent

Each electron partly shields the nucleus from the other, so the electrons should see a charge smaller than $Z$. Take the trial function

$$
\psi_\zeta(\mathbf r_1,\mathbf r_2) = \frac{\zeta^3}{\pi}\,e^{-\zeta(r_1+r_2)}
$$

with $\zeta$ as the variational parameter. Split the Hamiltonian so that $\psi_\zeta$ is an eigenfunction of the first part:

$$
H = \Big[-\tfrac12\nabla_1^2 - \tfrac12\nabla_2^2 - \frac{\zeta}{r_1} - \frac{\zeta}{r_2}\Big] + (\zeta - Z)\Big(\frac1{r_1} + \frac1{r_2}\Big) + \frac1{r_{12}} .
$$

The bracket gives $-\zeta^2$. For a hydrogenic 1s function $\langle1/r\rangle = \zeta$, and the repulsion is $\tfrac58\zeta$ by the result above. Therefore

$$
\langle H\rangle(\zeta) = -\zeta^2 + 2(\zeta - Z)\zeta + \tfrac58\zeta = \zeta^2 - 2Z\zeta + \tfrac58\zeta .
$$

Setting $d\langle H\rangle/d\zeta = 0$,

$$
\boxed{\,\zeta = Z - \frac{5}{16} ,\qquad E_{var} = -\Big(Z - \frac{5}{16}\Big)^2\,}
$$

For helium $\zeta = 27/16 = 1.6875$ and $E_{var} = -2.84766\ E_h = -77.49$ eV, within 1.9 percent of the accurate value. The other electron screens $5/16$ of a nuclear charge.

**Virial check.** At the optimum $\langle T\rangle = \zeta^2$ and $\langle V\rangle = -2Z\zeta + \tfrac58\zeta = -2\zeta^2$, so $\langle V\rangle = -2\langle T\rangle$. Optimizing a scale parameter always enforces the virial theorem ([[hellmann-feynman-and-virial-theorems]]); the unscaled function with $\zeta = Z$ violates it.

## The isoelectronic series

!!! example "From the hydride ion to Be²⁺"

    All energies in $E_h$. The accurate nonrelativistic values are literature numbers quoted from memory, not recomputed here.

    | Ion | $Z$ | First order, $-Z^2 + \tfrac58Z$ | $\zeta$ | $E_{var}$ | Accurate | Error (m$E_h$) | One-electron threshold $-Z^2/2$ |
    |---|---|---|---|---|---|---|---|
    | H⁻ | 1 | $-0.37500$ | 0.6875 | $-0.47266$ | $-0.52775$ | 55.1 | $-0.5$ |
    | He | 2 | $-2.75000$ | 1.6875 | $-2.84766$ | $-2.90372$ | 56.1 | $-2.0$ |
    | Li⁺ | 3 | $-7.12500$ | 2.6875 | $-7.22266$ | $-7.27991$ | 57.3 | $-4.5$ |
    | Be²⁺ | 4 | $-13.50000$ | 3.6875 | $-13.59766$ | $-13.65557$ | 57.9 | $-8.0$ |

    Three things stand out.

    - The error is almost independent of $Z$, about 56 m$E_h$ (1.5 eV), while the total energy grows as $Z^2$. The relative error falls from 10 percent for H⁻ to 0.4 percent for Be²⁺.
    - For H⁻ the bound $-0.4727$ lies above the energy $-0.5$ of a hydrogen atom plus a free electron. The trial function fails to predict a bound ion, although H⁻ is bound by 0.0278 $E_h$ (0.76 eV). A variational energy above a threshold proves nothing; only an upper bound below the threshold proves binding.
    - The helium ionization energy, $E(\text{He}^+) - E(\text{He}) = -2 - E$, comes out as 23.07 eV against 24.59 eV.

## What the remaining error is

The trial function is a product of one-electron functions, so it cannot describe the correlation between the electrons.

- The best possible product function is the Hartree-Fock solution. In a large basis its energy is $-2.86163\ E_h$ (computed here; the Hartree-Fock limit is $-2.8617$), only 14 m$E_h$ below the single exponential. A single exponential with $\zeta = 27/16$ is already a fair orbital.
- The remaining 42 m$E_h$ is the correlation energy. It requires functions that depend on $r_{12}$ or a configuration expansion; see [[coulomb-cusp-and-helium-expansions]]. A full-CI calculation in the aug-cc-pV5Z basis gives $-2.90320\ E_h$, still 0.5 m$E_h$ short because of the slow convergence at the electron-electron cusp.

Griffiths notes that trial functions with more parameters, going back to Hylleraas, reach the measured value to many digits. Sakurai's treatment is identical in content and ends at the same $-77.5$ eV.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 8.2, Eqs. (8.15)-(8.35), Figs. 8.3 and 8.4 (described); Problems 8.7 and 8.8 (ionization energy, H⁻ and Li⁺). Page numbers are not given because the PDF used is an e-book rendering without print pagination.

Sakurai and Napolitano, *Modern Quantum Mechanics* (3rd ed., Cambridge University Press, 2021), Sec. 7.4, Eqs. (7.37)-(7.52), pp. 437-439, and Sec. 5.4, pp. 316-319, for the variational method in general.

The potential $\Phi(r)$ route to $\langle V_{ee}\rangle$ is my own; the value $5Z/8$ is confirmed symbolically. The series table and the PySCF Hartree-Fock and full-CI energies are computed in `griffiths/ch08_variational.py`. The accurate nonrelativistic energies and the Hartree-Fock limit are standard literature values quoted from memory (to verify against a tabulation).

Companion reading in Levine, *Quantum Chemistry* (7th ed., Pearson, 2014): Sec. 9.3, pp. 238-242 (perturbation treatment), and Sec. 9.4, pp. 242-245 (variation treatments of the helium ground state).
