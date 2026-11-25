---
id: local-field-clausius-mossotti-and-reaction-field
title: From molecular polarizability to permittivity - the internal field, the Clausius-Mossotti and Lorentz-Lorenz relations, the reaction field, and orientational polarization of polar molecules
summary: A molecule in a dielectric feels the internal field E_i, the total macroscopic field minus its own contribution. For a molecule in a spherical cavity of frozen polarization this is E_i = (ε_r + 2)E/3, which gives the Clausius–Mossotti relation 𝒩α/3ε₀ = (ε_r − 1)/(ε_r + 2) and, at optical frequencies, the Lorentz–Lorenz relation with n². NRS derive it three ways: by the cavity, by a dielectric sphere, and by the reaction field. The reaction field f μ is the field returned by the polarized surroundings. For polar molecules the directing field aligns permanent dipoles with a Boltzmann average given by the Langevin function, which adds 𝒩μ₀²/3kT for weak fields. That is the origin of the large static permittivity of polar liquids, and of temperature series in nonlinear optics. Computed: argon gas permittivity and the refractive index of liquid water from computed polarizabilities; the polarization catastrophe of the Clausius–Mossotti–Debye equation for water and Onsager's ε.
status: in-progress
kind: theory
level: intermediate
tags: [clausius-mossotti, lorentz-lorenz, internal-field, local-field, reaction-field, onsager, debye-equation, langevin-function, orientational-polarization, refractive-index, permittivity, continuum-solvation]
prerequisites: [maxwell-equations-in-matter, polarizabilities-and-dispersion-coefficients]
related: [electromagnetic-waves-in-linear-media, rotational-averages-and-isotropic-tensors, kramers-kronig-debye-and-lorentz-models, pure-vibrational-contributions-and-nuclear-relaxation]
conventions: [si-units, atomic-units]
key: cm
order: 80
date: 2026-11-25
---

SI units with polarizabilities $\alpha$ in C m² V⁻¹ (so $\boldsymbol\mu = \alpha\mathbf E$). An atomic-unit polarizability converts as $\alpha_{\rm SI} = 4\pi\varepsilon_0a_0^3\,\alpha_{\rm au}$. $\mathcal N$ is the number density, $\mathbf E$ the macroscopic field in the medium, $\mathbf E_0$ the field in vacuum, $\varepsilon_r$ the relative permittivity. Each molecule is imagined in a sphere of radius $R$ with $\tfrac{4\pi}{3}R^3\mathcal N = 1$ (NRS Eq. 3.345).

## The internal field

**The problem.** A nonpolar medium has $\mathbf P = \mathcal N\alpha\mathbf E_i$ (NRS Eq. 3.344). The field $\mathbf E_i$ that polarizes a molecule is not $\mathbf E$: from the total field one must remove the field the molecule's own share of the polarization creates.

**Derivation 1: the frozen plug.** Cut out the molecule's sphere while keeping the polarization of the rest frozen. The removed plug is a uniformly polarized sphere, two overlapping uniformly charged spheres displaced by $\boldsymbol\delta$ with $\mathbf P = \rho\boldsymbol\delta$. Inside it creates a uniform field $\mathbf E_{\rm plug} = -\mathbf P/3\varepsilon_0$ (NRS Eqs. 3.346–3.352). Therefore

$$
\mathbf E_i = \mathbf E - \mathbf E_{\rm plug} = \mathbf E + \frac{\mathbf P}{3\varepsilon_0} = \frac{\varepsilon_r + 2}{3}\mathbf E
\quad\Rightarrow\quad
\frac{\mathcal N\alpha}{3\varepsilon_0} = \frac{\varepsilon_r - 1}{\varepsilon_r + 2}.
\label{cm}
$$

This is the **Clausius–Mossotti relation** (NRS Eqs. 3.353–3.355).

**Derivation 2: a macroscopic sphere.** Put a sphere of the medium in a vacuum field $\mathbf E_0$. From [[maxwell-equations-in-matter]], $\mathbf E = \frac{3}{\varepsilon_r + 2}\mathbf E_0$ and $\mathbf P = 3\varepsilon_0\frac{\varepsilon_r - 1}{\varepsilon_r + 2}\mathbf E_0$. Then $\mathbf E_i = \mathbf E + \mathbf P/3\varepsilon_0 = \mathbf E_0$ (NRS Eqs. 3.356–3.358). The internal field is the field that would exist without the dielectric, and Eq. [[#cm]] follows again.

**Derivation 3: the reaction field.** Now let the surroundings respond to the molecule. For an empty cavity in the dielectric, the cavity field is $\mathbf E_{\rm cav} = \frac{3\varepsilon_r}{2\varepsilon_r + 1}\mathbf E$ (NRS Eq. 3.359). A dipole $\boldsymbol\mu$ at the centre polarizes the medium, which returns a uniform reaction field inside the cavity, while outside the dipole appears screened by $3/(2\varepsilon_r + 1)$ (NRS Eqs. 3.360–3.367):

$$
\mathbf R = f\boldsymbol\mu,\qquad f = \frac{2(\varepsilon_r - 1)}{2\varepsilon_r + 1}\frac{1}{4\pi\varepsilon_0R^3} = \frac{2(\varepsilon_r - 1)}{2\varepsilon_r + 1}\frac{\mathcal N}{3\varepsilon_0}.
$$

With $\mathbf E_i = \mathbf E_{\rm cav} + \mathbf R = \mathbf E_0$, this gives $\mathbf R$ and once more Clausius–Mossotti (NRS Eqs. 3.368–3.370). The reaction-field picture is the one that generalizes: it is Onsager's model and the basis of continuum solvation (PCM and its relatives), where $R$ becomes a cavity shaped by the molecule.

## Optical frequencies: Lorentz–Lorenz

**The relation.** At optical frequencies $\varepsilon_r = n^2$ for a nonmagnetic medium, and the same argument with the dynamic polarizability gives (NRS Eq. 3.461)

$$
\frac{\mathcal N\alpha(\omega)}{3\varepsilon_0} = \frac{n^2(\omega) - 1}{n^2(\omega) + 2}.
\label{ll}
$$

**Scope.** Clausius–Mossotti is a static relation and holds only for nonpolar media. Lorentz–Lorenz applies to polar liquids too, because at optical frequencies the permanent dipoles cannot follow the field and only the electronic polarizability responds. For a dilute gas, $n^2\approx1 + \mathcal N\alpha/\varepsilon_0$ (NRS Eq. 3.462).

## Polar molecules: orientational polarization

**The directing field.** A permanent dipole $\boldsymbol\mu_0$ in the field has orientation energy $U = -\boldsymbol\mu_0\cdot\mathbf E_d$. Only the part of the interaction that depends on orientation counts. With the reaction field the total dipole is $\boldsymbol\mu = (\boldsymbol\mu_0 + \alpha\mathbf E_{\rm cav})/(1 - f\alpha)$. The orientation-dependent energy then involves the **directing field** (NRS Eqs. 3.371–3.379)

$$
\mathbf E_d = \frac{1}{1 - f\alpha}\frac{3\varepsilon_r}{2\varepsilon_r + 1}\mathbf E .
$$

This is also the field component that exerts a torque, $\mathbf N = \boldsymbol\mu_0\times\mathbf E_i$.

**The Langevin function.** The Boltzmann average with $p(\theta)d\theta = \tfrac12\sin\theta\,d\theta$ gives (NRS Eqs. 3.380–3.388)

$$
\langle\cos\theta\rangle = L(x) = \coth x - \frac1x\approx\frac x3,\qquad x = \frac{\mu_0E_d}{kT},\qquad
\mathbf P_{\rm or} = \mathcal N\frac{\mu_0^2}{3kT}\mathbf E_d .
$$

**Linearity.** The response is linear only while $x\ll1$. For water ($\mu_0 = 1.85$ D, 298 K), $x = 0.1$ already needs $E\approx6.7\times10^7$ V m⁻¹, twenty times the breakdown field of air. Molecular media are therefore linear for orientation at any practical field, while the alignment remains tiny.

**Temperature series.** For nonlinear properties the orientational averages produce series $A_0 + A_1/T + A_2/T^2 + \cdots$ (NRS Eq. 3.389). Fitting measurements at several temperatures separates the electronic hyperpolarizability ($A_0$) from dipole-moment and polarizability-anisotropy contributions. This is the classical analysis of EFISHG and Kerr data.

**Debye's equation.** Adding orientational polarization to Clausius–Mossotti without the reaction field gives Debye's equation:

$$
\frac{\varepsilon_r - 1}{\varepsilon_r + 2} = \frac{\mathcal N}{3\varepsilon_0}\Big(\alpha + \frac{\mu_0^2}{3kT}\Big).
$$

It works for polar gases. For polar liquids its right-hand side exceeds 1, the polarization catastrophe (example below). Onsager's equation, in which the reaction field does not orient the dipole, removes the catastrophe. With $n^2$ for the electronic part:

$$
\frac{(\varepsilon_r - n^2)(2\varepsilon_r + n^2)}{\varepsilon_r(n^2 + 2)^2} = \frac{\mathcal N\mu_0^2}{9\varepsilon_0kT}.
$$

Kirkwood's correlation factor $g$, multiplying the right-hand side, accounts for the short-range orientational correlations that Onsager's continuum misses. (Debye's and Onsager's equations are standard results, not derived in NRS.)

## Worked example

!!! example "Gas, liquid and the catastrophe (computed for this note)"
    **Argon gas.** CCSD/aug-cc-pVTZ by finite field (±0.002 au) gives $\alpha = 10.779$ au. At 0 °C and 1 atm (Loschmidt number $2.6868\times10^{25}$ m⁻³):

    - $\varepsilon_r - 1 = \mathcal N\alpha/\varepsilon_0 = 5.393\times10^{-4}$; with Eq. [[#cm]] it is $5.394\times10^{-4}$, the difference being negligible in a gas.
    - $n - 1 = 2.70\times10^{-4}$.
    - With the reference polarizability of about 11.08 au (to verify), the same formula gives $5.54\times10^{-4}$. The 3% gap reflects the basis set and triples, not the Clausius–Mossotti relation.

    **Liquid water at 589 nm.** $\mathcal N = 3.334\times10^{28}$ m⁻³ at 25 °C. Eq. [[#ll]] with computed molecular polarizabilities (aug-cc-pVTZ, geometry of the gas):

    | $\alpha$ | value (au) | $n$ |
    |---|---:|---:|
    | HF, static | 8.428 | 1.278 |
    | TDHF, 589 nm | 8.567 | 1.283 |
    | CCSD, static | 9.235 | 1.307 |
    | CCSD × TDHF dispersion ratio, 589 nm | 9.387 | 1.313 |
    | gas-phase optical value, about 9.92 (to verify) | 9.92 | 1.332 |

    - **The relation holds.** With the experimental gas-phase polarizability, Lorentz–Lorenz reproduces the measured $n = 1.333$ of the liquid almost exactly. Treating each liquid molecule as a gas-phase molecule in a Lorentz cavity is a good approximation for the optical response.
    - **Where the error lies.** The computed values fall short through the remaining basis-set and correlation error in $\alpha$.

    **Static permittivity of water.** With $\mu_0 = 1.855$ D and the CCSD $\alpha$, the right-hand side of Debye's equation is 4.08. A ratio $(\varepsilon_r - 1)/(\varepsilon_r + 2)$ can never exceed 1, so the equation has no solution: the polarization catastrophe.

    **Onsager's equation.** With $n^2 = 1.333^2$ the right-hand side is 3.89, which gives $\varepsilon_r = 28.7$ against 78.4 measured. A Kirkwood factor $g = 2.79$ would be needed, the familiar signature of hydrogen-bonded orientational order.

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Sec. 3.5.2, Eqs. (3.344)–(3.389), Figs. 3.18–3.20 (described); Sec. 3.5.4.4, Eqs. (3.461)–(3.462). Debye's and Onsager's equations and the Kirkwood factor are general knowledge, not from NRS. The calculations are in `Claude outputs/part1_fields_batchD.py`, section F.
