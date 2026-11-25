---
id: infrared-intensities
title: Infrared intensities - IR absorption as a residue of the vibrational polarizability, the double-harmonic approximation, dipole derivatives as mixed field-geometry derivatives, km/mol intensities, and anharmonic effects
summary: IR absorption is the electric-dipole absorption of Part 4, Ch. 17 applied to vibrational transitions within the electronic ground state. In the double-harmonic approximation (harmonic oscillator states, dipole linear in the normal coordinates), only fundamentals are allowed, with ⟨0|μ|1_a⟩ = (ħ/2ω_a)^{1/2}∂μ/∂Q_a. The integrated band intensity is A = (N_A π/3c²)|∂μ/∂Q_a|² (Gaussian units), i.e. 974.88 km/mol per (a.u. per amu^{1/2} bohr)². A mode is IR active when Γ(Q_a)⊗Γ(μ) contains the totally symmetric representation. Dipole derivatives are mixed second derivatives ∂²E/∂F∂x, computed with the same response machinery as the Hessian. Electrical anharmonicity gives overtones and combination bands; mechanical anharmonicity shifts frequencies and gives Fermi resonances. Recomputed: NRS's water B3LYP/cc-pVTZ table (1639, 3800, 3901 cm⁻¹; derivatives 6.26, 1.35, 4.80 × 10⁻³ a.u.), plus intensities of 69.6, 3.2 and 40.9 km/mol.
status: in-progress
kind: theory
level: intermediate
tags: [infrared, ir-intensities, double-harmonic, dipole-derivatives, atomic-polar-tensor, normal-modes, selection-rules, anharmonicity, fermi-resonance]
prerequisites: [harmonic-vibrational-analysis, damped-response-and-absorption-cross-sections, analytic-gradients-and-force-constants]
related: [rhf-analytic-hessian, cphf-closed-shell, variational-perturbation-theory-and-the-2n-plus-1-rule, raman-scattering, diatomic-vibration-and-anharmonicity, groups-representations-and-characters, zero-point-energy-and-thermochemistry]
conventions: [atomic-units, si-units]
key: kmmol
order: 60
date: 2026-11-24
---

$Q_a$ are mass-weighted normal coordinates with harmonic frequencies $\omega_a$ ([[harmonic-vibrational-analysis]]). $\boldsymbol\mu(\mathbf Q)$ is the total (electronic plus nuclear) dipole moment of the electronic ground state, a function of geometry. Formulas are given in SI or Gaussian units where noted, numbers in atomic units.

## IR absorption as linear response

**Vibrational states.** Within the Born-Oppenheimer approximation the states $|k\rangle$ that the field connects at IR frequencies are vibrational levels of the ground electronic state. The relevant property is the *pure vibrational* polarizability: the sum over states restricted to vibrational excitations, with $\boldsymbol\mu(\mathbf Q)$ as the operator. Its residues at the vibrational frequencies give the transition moments $\langle0|\mu_\alpha|k\rangle$. The absorption cross section is the one of [[damped-response-and-absorption-cross-sections]]:

$$
\sigma(\omega) = \frac{\pi\omega}{3\varepsilon_0c\hbar}\sum_\alpha|\langle0|\mu_\alpha|k\rangle|^2\,L(\omega;\omega_{k0},\gamma_{k0}),
$$

with $\gamma_{k0}$ the inverse lifetime of the vibrational level. Equivalently, $\sigma = (\omega/\varepsilon_0c)\,\mathrm{Im}\,\bar\alpha^{\rm v}(-\omega;\omega)$ from the damped vibrational polarizability. The electronic contribution is excluded on the assumption that IR photons are far below every electronic excitation. That needs checking for molecules with near-degenerate frontier orbitals.

## The double-harmonic approximation

**Two approximations.**

1. **Mechanical harmonicity.** Vibrational states are products of harmonic oscillator functions.
2. **Electrical harmonicity.** The dipole is linear in the normal coordinates, $\boldsymbol\mu(\mathbf Q) = \boldsymbol\mu_0 + \sum_a(\partial\boldsymbol\mu/\partial Q_a)_0Q_a$.

**Transition moments.** With the oscillator matrix element $\langle0_a|Q_a|1_a\rangle = \sqrt{\hbar/2\omega_a}$, only fundamentals $0\to1_a$ are allowed:

$$
\langle0|\mu_\alpha|1_a\rangle = \sqrt{\frac{\hbar}{2\omega_a}}\,\frac{\partial\mu_\alpha}{\partial Q_a}.
\label{tm}
$$

**Integrated intensity.** Inserting Eq. [[#tm]] into $\sigma(\omega)$ and integrating over the line shape gives $\int\sigma\,d\omega = \pi|\partial\boldsymbol\mu/\partial Q_a|^2/(6\varepsilon_0c)$ (SI). Per wavenumber ($\omega = 2\pi c\tilde\nu$) and per mole:

$$
A_a = N_A\!\int\sigma\,d\tilde\nu = \frac{N_A}{12\varepsilon_0c^2}\Big|\frac{\partial\boldsymbol\mu}{\partial Q_a}\Big|^2\ \ (\text{SI}) = \frac{N_A\pi}{3c^2}\Big|\frac{\partial\boldsymbol\mu}{\partial Q_a}\Big|^2\ \ (\text{Gaussian}),\qquad A_a[\mathrm{km/mol}] = 974.88\,\Big|\frac{\partial\boldsymbol\mu}{\partial Q_a}\Big|^2_{\rm a.u./(amu^{1/2}\,bohr)}.
\label{kmmol}
$$

This is the quantity quantum chemistry programs print as IR intensity, a Naperian integrated molar absorption coefficient. NRS's Eq. (8.237) writes $\pi/(3\varepsilon_0c)|\partial\mu/\partial Q|^2$ for the integrated cross section. That is larger by 2 than the result of inserting $\langle0|Q|1\rangle^2 = \hbar/2\omega$ into their own Eq. (5.321), which in turn agrees with the standard formula above.

**Selection rule.** The ground vibrational state is totally symmetric and $|1_a\rangle$ transforms as $Q_a$. So the mode is IR active only if

$$
\Gamma(Q_a)\otimes\Gamma(\hat\mu_\alpha)\ni\Gamma_{\rm tot.sym.}
$$

for some $\alpha$, i.e. $Q_a$ transforms like $x$, $y$ or $z$. In water ($C_{2v}$, molecule in the $yz$ plane), $z\in A_1$ and $y\in B_2$. The bend and the symmetric stretch ($A_1$) absorb $z$-polarized light, the antisymmetric stretch ($B_2$) $y$-polarized light. In molecules with an inversion centre, IR-active modes are $u$ and Raman-active modes are $g$: the mutual exclusion rule ([[raman-scattering]]).

## Dipole derivatives are mixed second derivatives

**Atomic polar tensor.** Since $\mu_\alpha = -\partial E/\partial F_\alpha$, the geometric derivative of the dipole is a mixed second derivative of the energy:

$$
\frac{\partial\mu_\alpha}{\partial x_{K\beta}} = -\frac{\partial^2E}{\partial F_\alpha\,\partial x_{K\beta}},\qquad \frac{\partial\mu_\alpha}{\partial Q_a} = \sum_{K\beta}\frac{\partial\mu_\alpha}{\partial x_{K\beta}}\frac{L_{K\beta,a}}{\sqrt{M_K}}.
$$

$\partial\mu_\alpha/\partial x_{K\beta}$ is the atomic polar tensor of nucleus $K$, and $\mathbf L$ is the normal-mode matrix of mass-weighted displacements.

**How it is computed.** For SCF energies the mixed derivative needs the response of the wave function to only *one* of the two perturbations, by the $2n+1$ rule ([[variational-perturbation-theory-and-the-2n-plus-1-rule]]). Either the three field responses (CPHF with the dipole right-hand side, [[cphf-closed-shell]]) or the $3N$ nuclear responses already computed for the Hessian ([[rhf-analytic-hessian]]) suffice. That is why programs print IR intensities with frequencies at almost no extra cost.

**For correlated methods** the same Lagrangian technique applies ([[lagrangian-for-nonvariational-energies]]).

## Anharmonicity

**Electrical anharmonicity.** Quadratic terms $\tfrac12\sum\partial^2\mu/\partial Q_a\partial Q_b\,Q_aQ_b$ make overtones ($\langle2_a|Q_a^2|0\rangle\ne0$) and combination bands ($\langle1_a1_b|Q_aQ_b|0\rangle\ne0$) weakly allowed.

**Mechanical anharmonicity.** Cubic and quartic force constants lower fundamental frequencies, typically by 3-5% for X-H stretches. They also couple a fundamental to a nearly degenerate overtone or combination level through matrix elements such as $\langle1_a0_b|Q_aQ_b^2|0_a2_b\rangle$. The two levels then mix and share intensity, giving two bands of comparable strength instead of one strong and one weak: a **Fermi resonance**. The classic example is CO₂: the symmetric stretch and the bending overtone $2\nu_2$, seen in the Raman spectrum (Fermi 1931).

**Second-order vibrational perturbation theory.** It corrects the harmonic frequencies. NRS's water example at B3LYP/cc-pVTZ:

| Mode | harmonic | VPT2 | experiment (fundamental) |
|---|---:|---:|---:|
| bend ($A_1$) | 1640 | 1575 | 1595 |
| symmetric stretch ($A_1$) | 3800 | 3630 | 3657 |
| antisymmetric stretch ($B_2$) | 3900 | 3703 | 3756 |

The harmonic values are 2.8-3.9% too high. The anharmonic ones fall 20-53 cm⁻¹ below experiment, the remaining error being the B3LYP surface itself (NRS Table 8.11, not recomputed here).

## Worked example

!!! example "Water, B3LYP/cc-pVTZ: frequencies, dipole derivatives and intensities (NRS Table 8.10; recomputed for this note)"
    The geometry is optimized with PySCF 2.15.1 and geomeTRIC, the analytic Hessian diagonalized, and $\partial\boldsymbol\mu/\partial Q_a$ obtained by central differences of the SCF dipole ($\pm0.01$ amu$^{1/2}$ bohr along each mode). Molecule in the $yz$ plane; equilibrium dipole $\mu_z = -0.7550$ a.u. (O at $+z$).

    | Mode | $\omega_a$ (cm⁻¹) | NRS | $\partial\mu/\partial Q_a$ ($10^{-3}$ a.u., $Q$ in $m_e^{1/2}a_0$) | NRS | IR intensity (km/mol) |
    |---|---:|---:|---|---|---:|
    | bend, $A_1$ | 1639.3 | 1640 | $z$: 6.256 | $-6.25$ | 69.6 |
    | sym. stretch, $A_1$ | 3800.4 | 3800 | $z$: 1.349 | $-1.35$ | 3.2 |
    | antisym. stretch, $B_2$ | 3900.8 | 3900 | $y$: 4.798 | $-4.78$ | 40.9 |

    - **Signs.** The signs of $\partial\mu/\partial Q$ depend on the arbitrary sign of each normal mode; intensities do not.
    - **Units.** NRS's "$10^{-3}$ a.u." refers to $Q$ in units of $m_e^{1/2}a_0$. In units per amu$^{1/2}$ bohr the derivatives are 0.2671, 0.0576 and 0.2048, which give the intensities through Eq. [[#kmmol]].
    - **Spectrum.** The weak symmetric stretch next to a strong antisymmetric one is the familiar water gas-phase spectrum.

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Sec. 8.7.1, Eqs. (8.235)–(8.238), Tables 8.10–8.11, Fig. 8.37 (described); Sec. 5.10.7, Eq. (5.321); Sec. 6.6 for the pure vibrational polarizability (not yet in this notebook). The km/mol conversion and the factor-2 remark on Eq. (8.237) were derived here; the constant 974.88 was computed from CODATA constants. The calculations are in `Claude outputs/part4_response_batchB1.py`, section B.
