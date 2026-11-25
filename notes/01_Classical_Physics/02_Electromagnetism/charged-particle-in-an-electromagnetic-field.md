---
id: charged-particle-in-an-electromagnetic-field
title: A charged particle in an electromagnetic field - Lagrangian and Hamiltonian, canonical and mechanical momentum, the Lorentz force, Poynting's theorem, and the quantum Hamiltonian with its spin term
summary: The interaction Lagrangian qv·A − qφ makes the canonical momentum p = π + qA differ from the mechanical momentum π. The Hamiltonian follows by the minimal substitution p → p − qA, H = (p − qA)²/2m + qφ. Its equations of motion give the Lorentz force, whose magnetic part does no work. Poynting's theorem balances mechanical work, field energy and the energy flux S = ε₀c²E × B, which defines the intensity ½ε₀cE₀² of a wave. In quantum mechanics the same substitution gives the paramagnetic A·p and diamagnetic A² terms, and the spin–Zeeman term appears if the kinetic energy is written (σ·π)²/2m. The charge and current densities follow as functional derivatives of the interaction energy. Checked: cyclotron and E × B motion, the Pauli identity (sympy), and the intensity of a field of one atomic unit.
status: in-progress
kind: theory
level: intermediate
tags: [lorentz-force, canonical-momentum, mechanical-momentum, minimal-substitution, poynting-theorem, intensity, pauli-hamiltonian, spin-zeeman, current-density, dirac-equation, breit-interaction]
prerequisites: [electromagnetic-potentials-and-gauge-freedom]
related: [minimal-coupling-and-aharonov-bohm, spin-one-half, electromagnetic-waves-and-polarization, magnetizability-and-gauge-origin, nmr-shielding-and-spin-spin-coupling]
conventions: [si-units]
key: hclass
order: 30
date: 2026-11-25
---

SI units. One particle of charge $q$ and mass $m$ at $\mathbf r(t)$ with velocity $\mathbf v$; for the electron $q = -e$. Potentials $\phi(\mathbf r,t)$ and $\mathbf A(\mathbf r,t)$ as in [[electromagnetic-potentials-and-gauge-freedom]].

## Classical mechanics of a charge in a field

**Canonical and mechanical momentum.** For a point charge the interaction Lagrangian of [[electromagnetic-potentials-and-gauge-freedom]] reduces to $L_{\rm int} = q\mathbf v\cdot\mathbf A(\mathbf r,t) - q\phi(\mathbf r,t)$ (NRS Eq. 3.115). The canonical momentum then differs from the mechanical one (NRS Eqs. 3.116–3.117):

$$
\mathbf p = \frac{\partial L}{\partial\mathbf v} = \boldsymbol\pi + q\mathbf A,\qquad \boldsymbol\pi = \frac{\partial L_p}{\partial\mathbf v},\qquad
H = \mathbf p\cdot\mathbf v - L = (\boldsymbol\pi\cdot\mathbf v - L_p) + q\phi .
$$

**Minimal substitution.** Fields therefore enter through $p_\mu\to p_\mu - qA_\mu$, the minimal substitution, whether the free-particle Lagrangian is relativistic or not (NRS Eq. 3.118). The only property of the particle that enters is its charge. Nonrelativistically, $L_p = \tfrac12mv^2$ and (NRS Eqs. 3.119–3.120)

$$
H = \frac{(\mathbf p - q\mathbf A)^2}{2m} + q\phi .
\label{hclass}
$$

**The Lorentz force.** From the Euler–Lagrange equation, with the total time derivative of $\mathbf A$ along the trajectory, $d\mathbf A/dt = \partial_t\mathbf A + (\mathbf v\cdot\nabla)\mathbf A$ (NRS Eqs. 3.121–3.123):

$$
\frac{d\boldsymbol\pi}{dt} = q\big[-\nabla\phi - \partial_t\mathbf A\big] + q\,\mathbf v\times(\nabla\times\mathbf A) = q\mathbf E + q\,\mathbf v\times\mathbf B .
$$

**Magnetic forces do no work.** The magnetic force is perpendicular to $\mathbf v$, so the work $W = \int\mathbf F\cdot\mathbf v\,dt = \int q\mathbf E\cdot\mathbf v\,dt$ comes from the electric field alone (NRS Eqs. 3.124–3.125). Only $q\phi$ survives in $H$ once $\boldsymbol\pi$ is used.

- **The current-carrying wire.** A wire in a magnetic field still moves, because the magnetic force displaces the conduction electrons, and the resulting electric field drags the lattice along (NRS Fig. 3.5).
- **Cyclotron motion.** In a uniform $\mathbf B$ a charge circles at $\omega_c = |q|B/m$ with constant kinetic energy.
- **Crossed fields.** With crossed $\mathbf E$ and $\mathbf B$ its guiding centre drifts at $\mathbf E\times\mathbf B/B^2$, independent of charge and mass.

## Poynting's theorem and intensity

**Energy balance.** The rate of work on the charges is $dW/dt = \int\mathbf E\cdot\mathbf j\,d^3r$. Replacing $\mathbf j$ with Ampère–Maxwell and using Faraday's law gives an energy balance (NRS Eqs. 3.126–3.132):

$$
\frac{dW}{dt} + \frac{d}{dt}\int_V\tfrac12\varepsilon_0(E^2 + c^2B^2)\,d^3r = -\oint_S\mathbf S\cdot\mathbf n\,dS,\qquad \mathbf S = \varepsilon_0c^2\,\mathbf E\times\mathbf B .
$$

The field carries energy density $\tfrac12\varepsilon_0(E^2 + c^2B^2)$, and $\mathbf S$ (the Poynting vector) is the energy flux.

**Intensity.** For a plane wave $\mathbf S = \varepsilon_0cE^2\mathbf e_k$. The intensity is its average over one period (NRS Eqs. 3.133–3.135):

$$
I = \langle S\rangle_T = \tfrac12\varepsilon_0cE_0^2,\qquad \langle\mathbf S\rangle_T = \tfrac12\varepsilon_0c^2\,\mathrm{Re}(\mathbf E\times\mathbf B^*)\ \text{for complex fields}.
\label{intensity}
$$

## The quantum Hamiltonian

**Starting point.** The electronic Hamiltonian has the generic form $\hat H = \sum_i\hat h(i) + \tfrac12\sum_{i\neq j}\hat g(i,j) + V_{NN}$ (NRS Eqs. 3.136–3.138). Fields enter $\hat h$ by minimal substitution.

**Dirac Hamiltonian.** For the four-component Dirac Hamiltonian, the substitution gives (NRS Eqs. 3.139–3.142, 3.151)

$$
\hat h_D = \beta m_ec^2 + c\,\boldsymbol\alpha\cdot\hat{\boldsymbol\pi} - e\phi,\qquad \hat{\boldsymbol\pi} = \hat{\mathbf p} + e\mathbf A,\qquad \boldsymbol\alpha = \begin{pmatrix}0&\boldsymbol\sigma\\\boldsymbol\sigma&0\end{pmatrix},\quad \beta = \begin{pmatrix}I_2&0\\0&-I_2\end{pmatrix}.
$$

Its features:

- **Linear in momentum.** It is linear in $\hat{\mathbf p}$, as Lorentz covariance requires.
- **Negative-energy continuum.** It has a continuum of negative-energy solutions about $2m_ec^2$ below the positive ones. Dirac's filled sea fixes this, and positrons follow from it.
- **Two-component approximations.** X2C, DKH and ZORA keep only the positive-energy spectrum, exactly or approximately (NRS Sec. 3.2.2).

**The Lévy-Leblond equation.** It follows from a metric change $\psi^S\to\psi^S/c$ and the limit $c\to\infty$. It is a four-component nonrelativistic equation, convenient for magnetic properties (NRS Eqs. 3.143–3.148). Eliminating the small component gives

$$
\Big[\frac{(\boldsymbol\sigma\cdot\hat{\mathbf p})(\boldsymbol\sigma\cdot\hat{\mathbf p})}{2m_e} + \hat V\Big]\psi^L = E\psi^L,\qquad (\boldsymbol\sigma\cdot\hat{\mathbf p})^2 = \hat p^2 .
$$

**Where spin enters.** Without fields the two forms are identical. With fields they differ: $\hat{\boldsymbol\pi}$ has noncommuting components, so $\hat{\boldsymbol\pi}\times\hat{\boldsymbol\pi}\neq\mathbf 0$ and (NRS Eqs. 3.155–3.158)

$$
(\boldsymbol\sigma\cdot\hat{\boldsymbol\pi})^2 = \hat\pi^2 + e\hbar\,\boldsymbol\sigma\cdot\mathbf B
\quad\Rightarrow\quad
\hat h = \frac{\hat p^2}{2m_e} + \frac{e}{2m_e}(\hat{\mathbf p}\cdot\mathbf A + \mathbf A\cdot\hat{\mathbf p}) + \frac{e^2A^2}{2m_e} + \frac{e\hbar}{2m_e}\boldsymbol\sigma\cdot\mathbf B - e\phi .
\label{pauli}
$$

This is the Pauli Hamiltonian with $g_e = 2$.

- **Economy of the free-particle Hamiltonian.** Only the mass is needed to specify the free-particle Hamiltonian. Charge appears when fields are present, and spin only when there is a magnetic field.
- **In the Coulomb gauge.** $\tfrac{e}{2m_e}(\hat{\mathbf p}\cdot\mathbf A + \mathbf A\cdot\hat{\mathbf p}) = \tfrac{e}{m_e}\mathbf A\cdot\hat{\mathbf p}$ (NRS Eq. 3.154). These are the paramagnetic and diamagnetic operators used in [[magnetizability-and-gauge-origin]].

**Two-electron interaction.** In the Coulomb gauge, the nonrelativistic interaction is the instantaneous $e^2/4\pi\varepsilon_0r_{12}$. Relativistically, dropping retardation and using the velocity operator $c\boldsymbol\alpha$ adds the Breit term, which subtracts the irrotational current (NRS Eqs. 3.159–3.161):

$$
\hat g_B = -\frac{e^2}{8\pi\varepsilon_0c^2}\Big[\frac{c\boldsymbol\alpha_1\cdot c\boldsymbol\alpha_2}{r_{12}} + \frac{(c\boldsymbol\alpha_1\cdot\mathbf r_{12})(c\boldsymbol\alpha_2\cdot\mathbf r_{12})}{r_{12}^3}\Big].
$$

**Charge and current densities.** These are functional derivatives of the interaction energy, $\rho = \delta\langle\hat h_{\rm int}\rangle/\delta\phi$ and $\mathbf j = -\delta\langle\hat h_{\rm int}\rangle/\delta\mathbf A$ (NRS Eqs. 3.162–3.168).

- **Relativistic.** $\rho = -e\psi^\dagger\psi$ and $\mathbf j = -e\psi^\dagger c\boldsymbol\alpha\psi$.
- **Nonrelativistic.** The same $\rho$, but the current splits into three parts:

$$
\mathbf j^{\rm NR} = \underbrace{-\frac{e}{2m_e}\big[\psi^\dagger\hat{\mathbf p}\psi - \psi^{\rm T}\hat{\mathbf p}\psi^*\big]}_{\text{paramagnetic}}\;\underbrace{-\;\frac{e^2}{m_e}\psi^\dagger\mathbf A\psi}_{\text{diamagnetic}}\;\underbrace{-\;\frac{e}{2m_e}\nabla\times(\psi^\dagger\boldsymbol\sigma\psi)}_{\text{spin}} .
$$

## Worked example

!!! example "Trajectories, the Pauli identity and atomic field strengths (computed for this note)"
    **An electron in B = 1 T along z.** Starting velocity $(0, 10^5, 2\times10^4)$ m s⁻¹, integrated for 20 cyclotron periods (RK45, relative tolerance $10^{-11}$).

    - $\omega_c = eB/m_e = 1.758820\times10^{11}$ s⁻¹.
    - The kinetic energy stays constant to $5\times10^{-10}$ relative.

    **Crossed fields.** Adding $\mathbf E = 10^3\,\mathbf e_x$ V m⁻¹, the average velocity over 20 periods is $(0, -1000)$ m s⁻¹. This equals $\mathbf E\times\mathbf B/B^2$.

    **Pauli identity.** For a two-spinor $\psi = (\psi_\uparrow, 0)$ and a general $\mathbf A(x,y,z)$, sympy confirms the identity in Eq. [[#pauli]], $(\boldsymbol\sigma\cdot\hat{\boldsymbol\pi})^2\psi = [\hat\pi^2 + e\hbar\,\boldsymbol\sigma\cdot(\nabla\times\mathbf A)]\psi$.

    **Atomic unit of field.** One atomic unit of electric field is $E_h/ea_0 = 5.1422\times10^{11}$ V m⁻¹. By Eq. [[#intensity]], a wave of that amplitude has $I = 3.5094\times10^{16}$ W cm⁻². This is the intensity scale at which perturbation theory in the field breaks down: strong-field ionization and high-harmonic generation.

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Sec. 3.2.1, Eqs. (3.115)–(3.135), Fig. 3.5 (described); Sec. 3.2.2, Eqs. (3.136)–(3.168). The cyclotron and drift examples and the strong-field remark are general knowledge, not from NRS. The checks are in `Claude outputs/part1_fields_batchD.py`, section C.
