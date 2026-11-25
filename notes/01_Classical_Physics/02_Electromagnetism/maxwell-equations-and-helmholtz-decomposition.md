---
id: maxwell-equations-and-helmholtz-decomposition
title: Microscopic Maxwell equations - sources, charge conservation, the Helmholtz decomposition, static and retarded solutions, and the nonrelativistic limit
summary: Maxwell's equations fix the divergence and curl of E and B in terms of the charge and current densities. The continuity equation (charge conservation) follows from them. The Helmholtz theorem splits any field that vanishes fast enough at infinity into an irrotational and a solenoidal part, and gives the unique static solutions: Coulomb's law for E, Biot–Savart for B. Time-dependent solutions involve the retarded time (Jefimenko's equations). Eliminating μ₀ = 1/ε₀c² and letting c → ∞ removes all magnetism and retardation, which is why chemistry starts from the instantaneous Coulomb interaction and treats magnetic effects as corrections in 1/c². Checked: the Biot–Savart field of a current loop against the point magnetic dipole.
status: in-progress
kind: theory
level: intermediate
tags: [maxwell-equations, continuity-equation, helmholtz-theorem, coulomb-law, biot-savart, retarded-time, jefimenko, magnetic-dipole, nonrelativistic-limit]
prerequisites: []
related: [electromagnetic-potentials-and-gauge-freedom, multipolar-gauge-and-the-electric-dipole-approximation, maxwell-equations-in-matter]
conventions: [si-units]
key: maxwell
order: 10
date: 2026-11-25
---

SI units. $\rho(\mathbf r,t)$ is the charge density and $\mathbf j(\mathbf r,t)$ the current density, $\varepsilon_0$ and $\mu_0$ the electric and magnetic constants, and $\mathbf r_{12} = \mathbf r_1 - \mathbf r_2$. For a classical point charge $q$ on the trajectory $\mathbf r(t)$, $\rho = q\,\delta(\mathbf r' - \mathbf r(t))$ and $\mathbf j = q\dot{\mathbf r}(t)\,\delta(\mathbf r' - \mathbf r(t))$ (NRS Eq. 3.8).

## The equations

**Two pairs.** A homogeneous pair contains only the fields, and an inhomogeneous pair adds the sources (NRS Eqs. 3.2–3.7):

$$
\nabla\cdot\mathbf B = 0,\qquad \nabla\times\mathbf E + \partial_t\mathbf B = \mathbf 0,\qquad
\nabla\cdot\mathbf E = \rho/\varepsilon_0,\qquad \nabla\times\mathbf B - \frac{1}{c^2}\partial_t\mathbf E = \mu_0\mathbf j,\qquad \mu_0\varepsilon_0 = \frac1{c^2}.
\label{maxwell}
$$

In order: Gauss's law for magnetism, Faraday's law of induction, Gauss's law, and the Ampère–Maxwell law.

**Charge conservation.** Taking the divergence of the Ampère–Maxwell law, with $\nabla\cdot(\nabla\times\mathbf F) = 0$, and inserting Gauss's law gives the continuity equation (NRS Eqs. 3.9–3.13):

$$
\nabla\cdot\mathbf j + \partial_t\rho = 0
\quad\Longleftrightarrow\quad
\oint_S\mathbf j\cdot\mathbf n\,dS = -\frac{dQ_V}{dt}.
$$

Without Maxwell's displacement term $\partial_t\mathbf E/c^2$ the equations would force $\nabla\cdot\mathbf j = 0$ everywhere and could not describe a charging capacitor.

**Integral theorems.** The divergence theorem $\int_V\nabla\cdot\mathbf F\,dV = \oint_S\mathbf F\cdot\mathbf n\,dS$ and the curl (Stokes) theorem $\int_S(\nabla\times\mathbf F)\cdot\mathbf n\,dS = \oint_C\mathbf F\cdot d\mathbf l$ turn Maxwell's equations into flux and circulation laws. Their limiting forms define divergence and curl at a point, independent of the shape of the shrinking volume or loop (NRS Eqs. 3.12–3.20). A useful corollary for integration by parts is $\int_V\nabla f\,dV = \oint_Sf\,\mathbf n\,dS$ (NRS Eq. 3.17).

## The stationary case and the Helmholtz theorem

**Static equations.** With time-independent fields, $\nabla\cdot\mathbf B = 0$, $\nabla\cdot\mathbf E = \rho/\varepsilon_0$, $\nabla\times\mathbf E = \mathbf 0$ and $\nabla\times\mathbf B = \mu_0\mathbf j$. These require steady currents, $\nabla\cdot\mathbf j = 0$ (NRS Eq. 3.21).

**Uniqueness needs boundary conditions.** Divergence and curl alone do not fix a field: $\mathbf F = (yz, zx, xy)$ has zero divergence and curl, like $\mathbf F = \mathbf 0$. If both vanish, each Cartesian component obeys Laplace's equation $\nabla^2F_i = 0$, by $\nabla^2\mathbf F = \nabla(\nabla\cdot\mathbf F) - \nabla\times(\nabla\times\mathbf F)$. Integrating over a small sphere shows that a harmonic function has no interior maxima or minima. With $\mathbf F\to0$ at infinity the only solution is $\mathbf F = \mathbf 0$ (NRS Eqs. 3.22–3.24).

**Helmholtz theorem.** Let the divergence and curl of $\mathbf F$ fall off faster than $r^{-2}$. Then solving Poisson's equation component by component and integrating by parts gives (NRS Eqs. 3.25–3.32)

$$
\mathbf F(\mathbf r) = -\nabla s(\mathbf r) + \nabla\times\mathbf v(\mathbf r),\qquad
s(\mathbf r_1) = \frac{1}{4\pi}\int\frac{\nabla_2\cdot\mathbf F(\mathbf r_2)}{r_{12}}d^3r_2,\qquad
\mathbf v(\mathbf r_1) = \frac{1}{4\pi}\int\frac{\nabla_2\times\mathbf F(\mathbf r_2)}{r_{12}}d^3r_2 .
\label{helmholtz}
$$

The two terms are the **irrotational** part $\mathbf F_\parallel = -\nabla s$ (zero curl, "flux") and the **solenoidal** part $\mathbf F_\perp = \nabla\times\mathbf v$ (zero divergence, "circulation"). For a field $F_r(r)\mathbf e_r + F_\phi(r)\mathbf e_\phi$, the radial component carries the flux and the azimuthal one the circulation (NRS Fig. 3.2). In statics, $\mathbf E$ is purely irrotational and $\mathbf B$ purely solenoidal. $\mathbf B$ stays solenoidal in general, since $\nabla\cdot\mathbf B = 0$ always.

**Coulomb and Biot–Savart.** Applied to the static equations, Eq. [[#helmholtz]] gives the two laws of statics (NRS Eqs. 3.33–3.34):

$$
\mathbf E(\mathbf r_1) = \frac{1}{4\pi\varepsilon_0}\int\frac{\mathbf r_{12}\,\rho(\mathbf r_2)}{r_{12}^3}d^3r_2,\qquad
\mathbf B(\mathbf r_1) = -\frac{\mu_0}{4\pi}\int\frac{\mathbf r_{12}\times\mathbf j(\mathbf r_2)}{r_{12}^3}d^3r_2 .
$$

## The general case: retardation

**Wave equations.** Taking the curl of Faraday's law and of the Ampère–Maxwell law gives inhomogeneous wave equations with the d'Alembertian $\Box^2 = \nabla^2 - c^{-2}\partial_t^2$ (NRS Eqs. 3.39–3.42):

$$
\Box^2\mathbf E = \nabla\rho/\varepsilon_0 + \mu_0\partial_t\mathbf j,\qquad \Box^2\mathbf B = -\mu_0\nabla\times\mathbf j .
$$

**Retarded solutions.** The solution of $\Box^2\Psi = f$ is $\Psi(\mathbf r_1,t) = -\frac{1}{4\pi}\int f(\mathbf r_2,t_r)/r_{12}\,d^3r_2$, with the retarded time $t_r = t - r_{12}/c$ (NRS Eqs. 3.43–3.44). The field at $\mathbf r_1$ now depends on what the sources did a light-travel time earlier.

**Jefimenko's equations.** Integrating by parts, taking care that the gradient acts before $t\to t_r$ is substituted (NRS Eq. 3.46), gives

$$
\mathbf E = \frac{1}{4\pi\varepsilon_0}\int\Big[\frac{\mathbf r_{12}\rho(t_r)}{r_{12}^3} + \frac{\mathbf r_{12}\,\partial_t\rho(t_r)}{c\,r_{12}^2} - \frac{\partial_t\mathbf j(t_r)}{c^2r_{12}}\Big]d^3r_2,\qquad
\mathbf B = -\frac{\mu_0}{4\pi}\int\Big[\frac{\mathbf r_{12}\times\mathbf j(t_r)}{r_{12}^3} + \frac{\mathbf r_{12}\times\partial_t\mathbf j(t_r)}{c\,r_{12}^2}\Big]d^3r_2
$$

(NRS Eqs. 3.47–3.48). Without retardation and time dependence they reduce to Coulomb and Biot–Savart. To any solution one can add source-free waves, the subject of [[electromagnetic-waves-and-polarization]].

**In practice.** These integrals are rarely useful in practice. The potentials of [[electromagnetic-potentials-and-gauge-freedom]] are the working route.

## The nonrelativistic limit

**Taking the limit.** Maxwell's equations are Lorentz covariant from the start (see [[electromagnetic-potentials-and-gauge-freedom]]). The nonrelativistic limit is $c\to\infty$, but the result depends on how $c$ enters the unit system. Eliminating $\mu_0$ with $\mu_0 = 1/\varepsilon_0c^2$ and then letting $c\to\infty$ gives (NRS Eqs. 3.103–3.106)

$$
\nabla\cdot\mathbf B = 0,\qquad \nabla\times\mathbf E + \partial_t\mathbf B = \mathbf 0,\qquad \nabla\cdot\mathbf E = \rho/\varepsilon_0,\qquad \nabla\times\mathbf B = \mathbf 0 .
$$

**Consequences.**

- **No magnetism.** With zero divergence and zero curl, and the boundary condition at infinity, $\mathbf B = \mathbf 0$ everywhere.
- **Electrostatics only.** $\mathbf E$ is then irrotational and the scalar potential suffices: electrodynamics becomes electrostatics, with instantaneous Coulomb interactions.
- **Consequence for chemistry.** The molecular Hamiltonian starts from the Coulomb interaction (the Coulomb gauge singles it out). Magnetic interactions and retardation (spin–orbit, spin–spin, Breit) are relativistic corrections of order $1/c^2$.

## Worked example

!!! example "A current loop becomes a point magnetic dipole (computed for this note)"
    **Setup.** A loop of radius $R = 1$ m in the $xy$ plane carries $I = 1$ A counterclockwise. Its dipole moment is $\mathbf m = I\pi R^2\mathbf e_z$ (NRS Eq. 3.197). I compared the Biot–Savart field (20 000 line elements) with the point-dipole field $\frac{\mu_0}{4\pi}\frac{3\mathbf r(\mathbf r\cdot\mathbf m) - \mathbf mr^2}{r^5}$ (NRS Eq. 3.204 without the contact term):

    | observation point (units of $R$) | $|\mathbf B_{\rm loop} - \mathbf B_{\rm dip}|/|\mathbf B_{\rm dip}|$ |
    |---|---:|
    | $(0, 0, 3)$ | $1.5\times10^{-1}$ |
    | $(4, 0, 3)$ | $3.6\times10^{-2}$ |
    | $(10, 5, -7)$ | $5.6\times10^{-3}$ |
    | $(30, 0, 30)$ | $4.6\times10^{-4}$ |

    **What the table shows.**

    - **Decay of the error.** The relative error falls as $(R/r)^2$. The next term of a symmetric loop is a magnetic octupole, whose field falls two powers of $r$ faster.
    - **The loop centre.** There the numerical field is $\mu_0I/2R = 6.283185\times10^{-7}$ T, exactly the textbook value.

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Sec. 3.1.1, Eqs. (3.2)–(3.20); Sec. 3.1.2, Eqs. (3.21)–(3.38), Fig. 3.2 (described); Sec. 3.1.3, Eqs. (3.39)–(3.48); Sec. 3.1.6, Eqs. (3.103)–(3.106); Sec. 3.3.2, Eqs. (3.194)–(3.204). The capacitor argument for the displacement term is general knowledge, not from NRS. The check is in `Claude outputs/part1_fields_batchD.py`, section A.
