---
id: maxwell-equations-in-matter
title: Maxwell's equations in matter - spatial averaging, polarization and magnetization from molecular multipoles, the auxiliary fields D and H, constitutive relations, boundary conditions, and a dielectric sphere in a field
summary: Macroscopic fields are spatial averages of microscopic ones, so Maxwell's equations hold for them unchanged. Splitting the sources into free and bound parts and expanding the bound densities in molecular multipoles gives ρ_bound = −∇·P and j_bound = ∂P/∂t + ∇×M. Here P is the dipole (plus quadrupole-gradient) density and M the magnetic dipole density. The equations then read ∇·D = ρ_free and ∇×H − ∂D/∂t = j_free, with D = ε₀E + P and H = B/μ₀ − M. Constitutive relations close them: in general nonlocal in space and time, for linear isotropic media D = ε₀ε_rE. Boundary conditions follow from pillboxes and loops across interfaces. The dielectric sphere in a uniform field is the model problem behind local fields and continuum solvation. Checked: the sphere solution satisfies both boundary conditions.
status: in-progress
kind: theory
level: intermediate
tags: [macroscopic-maxwell-equations, polarization, magnetization, electric-displacement, auxiliary-field, constitutive-relations, linear-media, boundary-conditions, dielectric-sphere, susceptibility, spatial-dispersion]
prerequisites: [maxwell-equations-and-helmholtz-decomposition, electric-and-magnetic-multipole-moments]
related: [local-field-clausius-mossotti-and-reaction-field, electromagnetic-waves-in-linear-media, magnetizability-and-gauge-origin]
conventions: [si-units]
key: sphere
order: 70
date: 2026-11-25
---

SI units. Overbars denote spatially averaged (macroscopic) quantities. They are dropped once the averaging is understood. Molecule $M$ sits at $\mathbf R_M$ with internal coordinates $\mathbf r_M$ and moments $Q^{[n]}_M$, $\mathbf m_M$.

## Spatial averaging

**The averaging.** A measuring probe is much larger than a molecule, so it sees smoothed fields. With an isotropic, positive weight function normalized to one (NRS Eqs. 3.269–3.270),

$$
\bar{\mathbf F}(\mathbf r,t) = \int w(\mathbf r' - \mathbf r)\mathbf F(\mathbf r',t)\,d^3r' = \int w(\mathbf u)\mathbf F(\mathbf u + \mathbf r,t)\,d^3u .
$$

**Consequences.** Averaging commutes with time and space derivatives, so the averaged fields and sources obey the microscopic equations of [[maxwell-equations-and-helmholtz-decomposition]]. Because averaging treats space and time differently, Lorentz covariance of the macroscopic equations is not guaranteed.

## Polarization and magnetization

**The capacitor.** A parallel-plate capacitor with surface charge $\sigma$ has $E = \sigma/\varepsilon_0$ inside. Filling it with a dielectric lowers the field to $\sigma/\varepsilon$ with $\varepsilon = \varepsilon_0\varepsilon_r$. The medium has reorganized its charge so that it partly cancels the plates' field. The apparent loss of surface charge defines the polarization and the displacement (NRS Eqs. 3.271–3.278):

$$
\mathbf P = \sigma\Big(1 - \frac1{\varepsilon_r}\Big)\mathbf n = \varepsilon_0(\varepsilon_r - 1)\mathbf E = \varepsilon_0\chi_e\mathbf E,\qquad \mathbf D = \varepsilon_0\mathbf E + \mathbf P .
$$

**The magnetic case.** A toroidal coil with $N$ windings gives $B = \mu_0NI/2\pi r$ inside. An iron core raises this by $\mu_r$. Splitting the field into an applied part and a response defines (NRS Eqs. 3.279–3.283)

$$
\mathbf B = \mu_0(\mathbf H + \mathbf M),\qquad \mathbf M = \chi\mathbf H,\quad \chi = \mu_r - 1 .
$$

**The analogy is not complete.** $\mathbf E = (\mathbf D - \mathbf P)/\varepsilon_0$: polarization reduces the applied field, while magnetization usually adds to it (NRS Eq. 3.284).

- **Molecular materials.** $|\chi|\lesssim10^{-3}$, positive for paramagnets and negative for diamagnets. For a dilute medium the volume susceptibility is $\chi\approx\mu_0\mathcal N\xi$ (number density $\mathcal N$), with the molecular magnetizability $\xi$ of [[magnetizability-and-gauge-origin]].
- **Ferromagnets.** For iron $\chi\approx3000$.

## Maxwell's equations in matter

**Free and bound sources.** Split them, $\rho = \rho_{\rm free} + \rho_{\rm bound}$ and $\mathbf j = \mathbf j_{\rm free} + \mathbf j_{\rm bound}$. Write the bound density as a sum of molecular densities $\rho_M(\mathbf r - \mathbf R_M)$, average it, and Taylor-expand the weight function about each molecular origin (NRS Eqs. 3.285–3.294):

$$
\bar\rho_{\rm bound} = \rho_{\rm ion} - \nabla\cdot\mathbf P,\qquad P_i = \sum_M\bar Q^{[1]}_{M;i} + \tfrac12\nabla_j\sum_M\bar Q^{[2]}_{M;ij} + \cdots
$$

The macroscopic polarization is the dipole density plus gradients of the higher multipole densities, usually negligible. $\bar Q^{[n]}_M = \langle Q^{[n]}_M\delta(\mathbf r - \mathbf R_M)\rangle$ are the averaged point multipoles.

**Bound currents.** The bound current must also include the motion of each molecular origin, $\mathbf V_M = \partial_t\mathbf R_M$. Using the continuity equation (NRS Eqs. 3.296–3.300):

$$
\bar{\mathbf j}_{\rm bound} = \partial_t\mathbf P + \nabla\times\mathbf M + \mathbf j_{\rm ion} + \mathbf j_{\rm Röntgen},\qquad \mathbf M = \Big\langle\sum_M\mathbf m_M\delta(\mathbf R_M - \mathbf r)\Big\rangle + \cdots
$$

The ion current vanishes for neutral molecules. The Röntgen current couples polarization to the overall motion of the molecules and vanishes for a sample at rest.

**The macroscopic equations.** Inserting these gives (NRS Eqs. 3.295, 3.301–3.302)

$$
\nabla\cdot\mathbf B = 0,\qquad \nabla\times\mathbf E + \partial_t\mathbf B = \mathbf 0,\qquad \nabla\cdot\mathbf D = \rho_{\rm free},\qquad \nabla\times\mathbf H - \partial_t\mathbf D = \mathbf j_{\rm free}.
\label{macro}
$$

**Ambiguities.** The split into $\mathbf P$ and $\mathbf M$ is not unique. Only the irrotational part of $\mathbf P$ and the solenoidal part of $\mathbf M$ enter the bound sources. The free/bound division is also a choice: conduction electrons are free, electrons bound to molecules are not.

## Constitutive relations

**The closure problem.** Eq. [[#macro]] needs $\mathbf D$ and $\mathbf H$ in terms of $\mathbf E$ and $\mathbf B$. The induced moments respond to the total fields, not to the applied ones, so in general $\mathbf D = \varepsilon_0\mathbf E + \mathbf P[\mathbf E,\mathbf B]$ and $\mathbf H = \mathbf B/\mu_0 - \mathbf M[\mathbf E,\mathbf B]$ are functionals (NRS Eqs. 3.303–3.304). Magnetic hysteresis in iron is the extreme case: $\mathbf B$ is a multivalued function of $\mu_0\mathbf H$, depending on history (NRS Fig. 3.15).

**Linear media.** For weak fields and a weak response, the relations are linear but possibly nonlocal (NRS Eqs. 3.305–3.310). For a time-invariant, homogeneous medium they are convolutions, and in Fourier space

$$
D_i(\mathbf k,\omega) = A_{ij}(\mathbf k,\omega)E_j + T_{ij}(\mathbf k,\omega)B_j,\qquad H_i(\mathbf k,\omega) = U_{ij}(\mathbf k,\omega)E_j + X_{ij}(\mathbf k,\omega)B_j .
$$

The two kinds of dispersion:

- **Spatial dispersion.** The dependence on $\mathbf k$ scales with (molecular size)/(wavelength) and can be ignored when the electric dipole approximation holds.
- **Temporal dispersion.** The dependence on $\omega$ cannot be ignored, because molecular resonances span microwaves to X-rays ([[electromagnetic-waves-in-linear-media]]).
- **Complex and tensorial constants.** Phase lags make the constants complex, and anisotropy makes them $3\times3$ tensors: birefringence and dichroism.

**Simple linear dielectrics.** Most of what follows uses the simplest case, $\mathbf D = \varepsilon_0\varepsilon_r\mathbf E$, $\mathbf P = \varepsilon_0(\varepsilon_r - 1)\mathbf E$ (NRS Eq. 3.311).

## Boundary conditions

At an interface with normal $\mathbf n_{AB}$ pointing from $B$ into $A$, a flat pillbox and a thin loop give (NRS Eqs. 3.312–3.322):

$$
\mathbf n_{AB}\cdot(\mathbf D_A - \mathbf D_B) = \sigma_f,\qquad \mathbf n_{AB}\cdot(\mathbf B_A - \mathbf B_B) = 0,\qquad
\mathbf n_{AB}\times(\mathbf E_A - \mathbf E_B) = \mathbf 0,\qquad \mathbf n_{AB}\times(\mathbf H_A - \mathbf H_B) = \mathbf K_f .
$$

- **Interpretation.** The normal $\mathbf D$ jumps by the free surface charge, and the tangential $\mathbf H$ by the free surface current. The normal $\mathbf B$ and the tangential $\mathbf E$ are continuous.
- **Bound surface charges and currents.** In terms of the total fields, $\mathbf n\cdot(\mathbf P_A - \mathbf P_B) = -\sigma_b$ and $\mathbf n\times(\mathbf M_A - \mathbf M_B) = \mathbf K_b$.

## A dielectric sphere in a dielectric

**The problem.** A sphere of radius $a$ and permittivity $\varepsilon_A$ sits in a medium $\varepsilon_B$ with a uniform applied field $E_0\mathbf e_z$ far away. There are no free charges, so $\nabla^2\phi = 0$ everywhere. Axial symmetry gives $\phi = \sum_\ell(A_\ell r^\ell + B_\ell r^{-\ell-1})P_\ell(\cos\theta)$. Only $\ell = 1$ survives, and the conditions $\phi_A = \phi_B$ and $\varepsilon_A\partial_r\phi_A = \varepsilon_B\partial_r\phi_B$ at $r = a$ give (NRS Eqs. 3.323–3.335)

$$
\phi_A = -\frac{3\varepsilon_B}{\varepsilon_A + 2\varepsilon_B}E_0r\cos\theta,\qquad
\phi_B = -\Big[1 - \frac{\varepsilon_A - \varepsilon_B}{\varepsilon_A + 2\varepsilon_B}\frac{a^3}{r^3}\Big]E_0r\cos\theta .
\label{sphere}
$$

**Two special cases.**

- **A dielectric sphere in vacuum** ($\varepsilon_A = \varepsilon_r$, $\varepsilon_B = 1$). The inside field is uniform and reduced, $\mathbf E_{\rm in} = \frac{3}{\varepsilon_r + 2}\mathbf E_0$, with $\mathbf P_{\rm in} = 3\varepsilon_0\frac{\varepsilon_r - 1}{\varepsilon_r + 2}\mathbf E_0$. Outside, the applied field is joined by a point dipole $\frac{\varepsilon_r - 1}{\varepsilon_r + 2}a^3E_0$. The only bound charge is on the surface, $\sigma_b = 3\varepsilon_0\frac{\varepsilon_r - 1}{\varepsilon_r + 2}E_0\cos\theta$ (NRS Eqs. 3.336–3.343). Treating that surface charge explicitly, without $\mathbf D$, gives the same potentials.
- **A cavity in a dielectric** ($\varepsilon_A = 1$, $\varepsilon_B = \varepsilon_r$). The field inside is $\frac{3\varepsilon_r}{2\varepsilon_r + 1}\mathbf E$. This is the starting point of the reaction field and of the Onsager model of solvation ([[local-field-clausius-mossotti-and-reaction-field]]).

## Worked example

!!! example "Boundary conditions of the sphere solution (computed for this note)"
    For $\varepsilon_A = 5$, $\varepsilon_B = 2$, $a = 1$, $E_0 = 1$ and $\cos\theta = 0.3$, Eq. [[#sphere]] gives:

    - $\phi_A - \phi_B = 3\times10^{-17}$ at $r = a$;
    - $\varepsilon_A\partial_r\phi_A - \varepsilon_B\partial_r\phi_B = -3\times10^{-11}$ by central differences with step $10^{-6}$, the finite-difference error.

    Both interface conditions hold, as they must for the unique solution. The inside field is $3\varepsilon_B/(\varepsilon_A + 2\varepsilon_B) = 0.667$ of the applied one, and uniform.

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Sec. 3.4.1, Eqs. (3.269)–(3.270), Fig. 3.10 (described); Sec. 3.4.2, Eqs. (3.271)–(3.284), Figs. 3.11–3.13 (described); Sec. 3.4.3, Eqs. (3.285)–(3.302), Fig. 3.14 (described); Sec. 3.4.4, Eqs. (3.303)–(3.304), Fig. 3.15 (described); Sec. 3.5, Eqs. (3.305)–(3.311); Sec. 3.5.1, Eqs. (3.312)–(3.343), Figs. 3.16–3.17 (described). The check is in `Claude outputs/part1_fields_batchD.py`, section F.
