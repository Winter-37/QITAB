---
id: kohn-sham-dft
title: Hohenberg–Kohn theorems and the Kohn–Sham method
summary: The ground-state density determines the external potential and hence everything (Hohenberg–Kohn), and minimizes the energy functional (HK variational theorem). Kohn and Sham replace the unknown kinetic functional by that of a noninteracting reference system with the same density, which gives one-electron equations identical in form to Hartree–Fock with the exchange operator replaced by v_xc = δE_xc/δρ. Covers the energy decomposition, the functional derivative, the basis-set (Roothaan-like) form and numerical integration, and the meaning of KS orbitals and orbital energies. Worked example: the KS energy of H₂O at B3LYP/cc-pVTZ term by term (−76.4598 E_h, 22 mE_h below the exact energy).
status: in-progress
kind: theory
level: intermediate
tags: [dft, kohn-sham, hohenberg-kohn, exchange-correlation, functional-derivative, electron-density]
prerequisites: [hartree-fock-equations, variational-principle, free-electron-gas, rhf]
related: [exchange-correlation-functionals, dft-versus-hartree-fock, fock-operator, koopmans-theorem, one-particle-rdm]
order: 10
date: 2026-11-17
---

Atomic units throughout. $n$ electrons, nuclei of charge $Z_\alpha$ fixed; $\rho(\mathbf r)$ is the electron density, $\int\rho\,\mathrm d\mathbf r = n$.

## The Hohenberg–Kohn theorem

The electronic Hamiltonian is fixed by $n$ and the **external potential** $v(\mathbf r) = -\sum_\alpha Z_\alpha/|\mathbf r - \mathbf R_\alpha|$:

$$
\hat H = -\tfrac12\sum_i\nabla_i^2 + \sum_iv(\mathbf r_i) + \sum_{i<j}\frac1{r_{ij}} .
$$

**Theorem.** For a nondegenerate ground state, $\rho_0(\mathbf r)$ determines $v$ up to an additive constant, and it determines $n$ by integration. Hence it determines $\hat H$, and with it the ground-state wave function, the energy and every other property.

**Proof (by contradiction).** Suppose $v_a$ and $v_b$ differ by more than a constant but give the same ground-state density $\rho_0$. Their ground states $\Psi_a$, $\Psi_b$ differ. Use $\Psi_b$ as a trial function for $\hat H_a$; with $\hat H_a - \hat H_b = \sum_i[v_a(\mathbf r_i) - v_b(\mathbf r_i)]$ the strict variation theorem gives

$$
E_a < \langle\Psi_b|\hat H_a|\Psi_b\rangle = E_b + \int\rho_0(\mathbf r)\big[v_a(\mathbf r) - v_b(\mathbf r)\big]\mathrm d\mathbf r .
$$

Exchanging $a$ and $b$ gives $E_b < E_a + \int\rho_0[v_b - v_a]\,\mathrm d\mathbf r$. Adding the two inequalities gives $E_a + E_b < E_a + E_b$, a contradiction.

So the energy is a functional of the density:

$$
E_v[\rho] = \int\rho(\mathbf r)v(\mathbf r)\,\mathrm d\mathbf r + F[\rho],\qquad F[\rho] = T[\rho] + V_{ee}[\rho],
$$

where $F$ is the same for every molecule (it does not depend on $v$) but is unknown.

**HK variational theorem.** For any trial density $\rho_{\text{tr}}\ge0$ with $\int\rho_{\text{tr}} = n$, $E_v[\rho_{\text{tr}}]\ge E_0$. Proof: $\rho_{\text{tr}}$ determines a $v_{\text{tr}}$ and a wave function $\Psi_{\text{tr}}$; using $\Psi_{\text{tr}}$ as a trial function for $\hat H$ gives $T[\rho_{\text{tr}}] + V_{ee}[\rho_{\text{tr}}] + \int\rho_{\text{tr}}v\ge E_0$. This assumes $\rho_{\text{tr}}$ is **$v$-representable** (comes from the ground state of some external potential); Levy's constrained-search reformulation removes that assumption and also covers degenerate ground states.

## The Kohn–Sham reference system

The theorems give no recipe for $F[\rho]$. Kohn and Sham introduce a fictitious system of $n$ **noninteracting** electrons in a potential $v_s(\mathbf r)$ chosen so that its ground-state density equals the true one, $\rho_s = \rho_0$ (by HK applied to noninteracting systems, $v_s$ is unique). Its ground state is a single determinant of **Kohn–Sham spin orbitals** $u_i^{\text{KS}}$, and

$$
\rho(\mathbf r) = \sum_{i=1}^n|u_i^{\text{KS}}(\mathbf r)|^2 ,\qquad
T_s[\rho] = -\tfrac12\sum_{i=1}^n\langle u_i^{\text{KS}}|\nabla^2|u_i^{\text{KS}}\rangle .
$$

Define $\Delta T = T - T_s$, $\Delta V_{ee} = V_{ee} - J[\rho]$ with the classical Coulomb (Hartree) energy $J[\rho] = \tfrac12\iint\rho(\mathbf r_1)\rho(\mathbf r_2)/r_{12}$, and the **exchange–correlation energy**

$$
E_{xc}[\rho] = \Delta T[\rho] + \Delta V_{ee}[\rho] .
$$

Then, exactly,

$$
E_0 = \underbrace{\int\rho v\,\mathrm d\mathbf r}_{V_{Ne}} + \underbrace{T_s[\rho]}_{\text{noninteracting KE}} + \underbrace{J[\rho]}_{\text{Hartree}} + E_{xc}[\rho] .
$$

The first three terms are large and computable from the orbitals; $E_{xc}$ is small and contains everything hard: exchange, Coulomb correlation, the kinetic correlation $\Delta T$, and the correction for the self-interaction that $J[\rho]$ wrongly includes.

**Kohn–Sham equations.** Minimizing $E_0$ with respect to orthonormal orbitals gives

$$
\Big[-\tfrac12\nabla^2 + v(\mathbf r) + \int\frac{\rho(\mathbf r')}{|\mathbf r - \mathbf r'|}\mathrm d\mathbf r' + v_{xc}(\mathbf r)\Big]u_i^{\text{KS}} = \varepsilon_i^{\text{KS}}u_i^{\text{KS}},\qquad
v_{xc}(\mathbf r) = \frac{\delta E_{xc}[\rho]}{\delta\rho(\mathbf r)} .
$$

The operator in brackets is $-\tfrac12\nabla^2 + v_s$. It is the Fock operator ([[fock-operator]]) with the nonlocal exchange operator $-\sum_j\hat K_j$ replaced by the **local, multiplicative** potential $v_{xc}$, which carries exchange and correlation together.

**Functional derivative.** For $F[\rho] = \int g(\rho,\rho_x,\rho_y,\rho_z)\,\mathrm d\mathbf r$, with $\rho_x = \partial\rho/\partial x$ etc.,

$$
\frac{\delta F}{\delta\rho} = \frac{\partial g}{\partial\rho} - \frac{\partial}{\partial x}\frac{\partial g}{\partial\rho_x} - \frac{\partial}{\partial y}\frac{\partial g}{\partial\rho_y} - \frac{\partial}{\partial z}\frac{\partial g}{\partial\rho_z} .
$$

It is defined by $\delta F = \int\frac{\delta F}{\delta\rho(\mathbf r)}\delta\rho(\mathbf r)\,\mathrm d\mathbf r$. For LDA exchange, $g = -\tfrac34(3/\pi)^{1/3}\rho^{4/3}$ gives $v_x = -(3\rho/\pi)^{1/3}$ ([[exchange-correlation-functionals]]).

## In a basis set

Expanding $u_i^{\text{KS}} = \sum_rc_{ri}\chi_r$ gives Roothaan-like equations

$$
\sum_s\big(h^{\text{KS}}_{rs} - \varepsilon_i^{\text{KS}}S_{rs}\big)c_{si} = 0,\qquad
h^{\text{KS}}_{rs} = \langle\chi_r|-\tfrac12\nabla^2 + v|\chi_s\rangle + J_{rs} + \langle\chi_r|v_{xc}|\chi_s\rangle ,
$$

solved self-consistently exactly like an SCF calculation ([[scf-procedure]]): guess $\rho$ (usually a superposition of atomic densities), build $v_{xc}$, diagonalize, rebuild $\rho$, iterate. Two practical differences from HF:

- $\langle\chi_r|v_{xc}|\chi_s\rangle$ cannot be done analytically and is computed by **numerical quadrature** on an atom-centred grid. This is the most expensive step with Gaussian basis functions, and too coarse a grid gives wrong energies and noisy gradients.
- Without exact exchange there is no $\hat K$, so density fitting (RI) of $J$ speeds the calculation up much more than for HF; hybrid functionals lose that advantage.

Analytic gradients and Hessians exist, so geometry optimization and frequencies work as for HF.

## What the orbitals mean

- The occupied KS orbitals belong to the fictitious system; the many-electron state has no DFT wave function. In practice they closely resemble HF orbitals and are used the same way in qualitative MO arguments.
- For the **exact** functional, the highest occupied KS orbital energy equals minus the first ionization energy. No other KS orbital energy has a Koopmans-like meaning, and with approximate functionals even $-\varepsilon_{\text{HOMO}}$ is far too small ([[dft-versus-hartree-fock]]).
- The spin-unrestricted generalization (spin-DFT, LSDA) treats $\rho^\alpha$ and $\rho^\beta$ separately, with $v_{xc}^\sigma = \delta E_{xc}[\rho^\alpha,\rho^\beta]/\delta\rho^\sigma$; it is needed for open shells and for bonds stretched toward dissociation.

## Worked example

!!! example "The Kohn–Sham energy of water, term by term (B3LYP/cc-pVTZ)"
    Optimized geometry $r(\text{OH}) = 0.9613$ Å, $\angle\text{HOH} = 104.53°$. Total energy $E = -76.459\,841\,E_h$, against Levine's $-76.460$.

    | Term | $E_h$ |
    |---|---:|
    | $T_s$ | 76.072 530 |
    | $V_{Ne}$ | −199.170 669 |
    | $J[\rho]$ | 46.830 629 |
    | $E_{xc}$ (B3LYP, total) | −9.347 600 |
    | of which 20% exact exchange | −1.787 527 |
    | $V_{NN}$ | 9.155 270 |
    | sum | −76.459 841 |

    - **Not variational.** The exact nonrelativistic energy is $-76.438\,E_h$ (Levine Table 16.1), so this DFT energy lies 22 m$E_h$ (14 kcal/mol) **below** it. An approximate functional gives no upper bound.
    - **KS versus HF.** At the same geometry, HF/cc-pVTZ gives $E = -76.056\,857\,E_h$ and $T = 75.989\,502\,E_h$. $T_s$ exceeds the HF kinetic energy by 0.083 $E_h$.
    - **Exchange.** The exact exchange energy evaluated with the KS orbitals is $-8.9376\,E_h$, against $-8.9546\,E_h$ with HF orbitals.
    - **Orbitals.** The occupied KS and HF spaces nearly coincide: the cosines of the five principal angles between them are 0.99981-0.99999.

## Source

Levine, *Quantum Chemistry* (7th ed., Pearson, 2014), Sec. 16.5, pp. 552-563: HK theorem and proof, Eqs. (16.33)-(16.36); HK variational theorem, Eq. (16.37), $v$-representability and Levy; KS reference system and energy, Eqs. (16.38)-(16.46); KS equations and functional derivative, Eqs. (16.47)-(16.51); basis-set form, Eq. (16.62), numerical integration, LSDA spin-DFT; meaning of KS orbitals and HOMO energy; the B3LYP/cc-pVTZ water energy (p. 571) and the exact nonrelativistic energy of Table 16.1 (p. 532). Original papers: Hohenberg and Kohn, *Phys. Rev.* **136**, B864 (1964); Kohn and Sham, *Phys. Rev.* **140**, A1133 (1965) (as cited by Levine). Calculations in `part4_dft.py`, sections A and B (PySCF 2.15.1, grid level 5).
