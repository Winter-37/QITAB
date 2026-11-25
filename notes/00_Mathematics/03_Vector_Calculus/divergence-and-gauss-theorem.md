---
id: divergence-and-gauss-theorem
title: Divergence and Gauss's theorem - flux, the divergence as outflow per unit volume, the continuity equation, the divergence of r/r³, and Green's theorems
summary: The divergence ∇·V = ∂V_x/∂x + ∂V_y/∂y + ∂V_z/∂z is the net outward flux of V per unit volume at a point: a source where it is positive, a sink where it is negative. Gauss's (divergence) theorem says the flux of V out of a closed surface equals the volume integral of ∇·V inside. With it come the continuity equation for any conserved density and Green's theorems, the three-dimensional integration by parts. The field r/r³ has zero divergence everywhere except the origin, yet a flux of 4π through every sphere: ∇·(r/r³) = 4πδ(r). Worked examples: ∇·r = 3, ∇·(rⁿr) = (n + 3)rⁿ, and Gauss's theorem on a cube.
status: in-progress
kind: theory
level: introductory
tags: [divergence, flux, gauss-theorem, divergence-theorem, continuity-equation, green-theorem, source, sink, dirac-delta, solenoidal]
prerequisites: [scalar-and-vector-fields-and-the-gradient, integral-calculus]
related: [curl-and-stokes-theorem, vector-identities-and-the-laplacian, curvilinear-coordinates, maxwell-equations-and-helmholtz-decomposition, fourier-transforms-and-the-dirac-delta]
key: gauss
order: 30
date: 2026-11-25
---

Cartesian coordinates. $d\boldsymbol\sigma = \hat{\mathbf n}\,d\sigma$ is the outward-pointing surface element, $d\tau$ the volume element, $\partial V$ the closed surface bounding the volume $V$.

## Flux

**Definition.** The flux of $\mathbf V$ through a surface $S$ is $\int_S\mathbf V\cdot d\boldsymbol\sigma$: the amount of $\mathbf V$ crossing it, counting only the normal component. For a fluid with density $\rho$ and velocity $\mathbf v$, the flux of $\rho\mathbf v$ is the mass crossing $S$ per unit time.

## The divergence

**Definition.** Acting on a vector field with $\nabla\cdot$ gives a scalar field (Arfken Sec. 1.7):

$$
\nabla\cdot\mathbf V = \frac{\partial V_x}{\partial x} + \frac{\partial V_y}{\partial y} + \frac{\partial V_z}{\partial z} = \partial_iV_i .
$$

**Meaning.** Arfken counts the flow through the six faces of a small box $dx\,dy\,dz$. The net outflow is $\nabla\cdot(\rho\mathbf v)\,dx\,dy\,dz$ (Arfken Eq. 1.66). The divergence is therefore the outflow per unit volume:

$$
\nabla\cdot\mathbf V = \lim_{\Delta V\to0}\frac1{\Delta V}\oint_{\partial(\Delta V)}\mathbf V\cdot d\boldsymbol\sigma .
\label{divdef}
$$

- **Sources and sinks.** $\nabla\cdot\mathbf V > 0$ at a source, $< 0$ at a sink.
- **Solenoidal fields.** If $\nabla\cdot\mathbf V = 0$ everywhere, every bit of flux that enters a region also leaves it. Field lines neither begin nor end. The magnetic field is solenoidal; so is the velocity of an incompressible fluid.
- **Invariance.** Eq. [[#divdef]] makes no reference to axes, so $\nabla\cdot\mathbf V$ is a scalar. That is also why it can be written in any coordinate system ([[curvilinear-coordinates]]).

**Product rule.** $\nabla\cdot(f\mathbf V) = \nabla f\cdot\mathbf V + f\,\nabla\cdot\mathbf V$.

**Radial fields.** $\nabla\cdot\mathbf r = 3$, and for $\mathbf V = r^n\mathbf r$ (Arfken Examples 1.7.1–1.7.2):

$$
\nabla\cdot(r^n\mathbf r) = (n + 3)\,r^n .
\label{divrn}
$$

For $n = -3$ this vanishes: the inverse-square field $\mathbf r/r^3$ has zero divergence everywhere except the origin, where it is undefined.

## Gauss's theorem

**Statement.** For a volume $V$ bounded by a closed surface $\partial V$ and a field with continuous first derivatives (Arfken Eq. 1.101a),

$$
\oint_{\partial V}\mathbf V\cdot d\boldsymbol\sigma = \int_V\nabla\cdot\mathbf V\,d\tau .
\label{gauss}
$$

**Proof idea.** Divide $V$ into small boxes and apply Eq. [[#divdef]] to each. Fluxes through shared internal faces cancel in pairs, leaving only the outer surface.

**The continuity equation.** If a quantity with density $\rho$ and current density $\mathbf j$ is conserved, its decrease in a fixed volume equals its outflow: $-\frac{d}{dt}\int_V\rho\,d\tau = \oint\mathbf j\cdot d\boldsymbol\sigma$. Using Eq. [[#gauss]] and letting $V$ shrink,

$$
\frac{\partial\rho}{\partial t} + \nabla\cdot\mathbf j = 0 .
$$

This holds for charge, mass, and quantum-mechanical probability with $\mathbf j = \frac{\hbar}{2mi}(\psi^*\nabla\psi - \psi\nabla\psi^*)$.

**The point charge.** The flux of $\mathbf r/r^3$ through a sphere of radius $R$ is $\int(1/R^2)\,R^2\,d\Omega = 4\pi$, whatever $R$. Yet the divergence is zero away from the origin. By Eq. [[#gauss]], all the flux comes from the origin, which means

$$
\nabla\cdot\frac{\mathbf r}{r^3} = 4\pi\,\delta(\mathbf r),\qquad\text{equivalently}\qquad\nabla^2\frac1r = -4\pi\delta(\mathbf r)
\label{delta}
$$

(Arfken Sec. 1.14 and Eq. 1.170). This is Gauss's law for a point charge, $\nabla\cdot\mathbf E = \rho/\varepsilon_0$, and the reason $1/(4\pi r)$ is the Green's function of the Laplacian ([[vector-identities-and-the-laplacian]]).

**Other forms.** Applying Eq. [[#gauss]] to $\varphi\mathbf a$ and $\mathbf P\times\mathbf a$ with a constant $\mathbf a$ gives $\oint\varphi\,d\boldsymbol\sigma = \int\nabla\varphi\,d\tau$ and $\oint d\boldsymbol\sigma\times\mathbf P = \int\nabla\times\mathbf P\,d\tau$ (Arfken Eqs. 1.109–1.110).

## Green's theorems

**Integration by parts in 3D.** Apply Eq. [[#gauss]] to $u\nabla v$. Then

$$
\oint u\nabla v\cdot d\boldsymbol\sigma = \int\big(u\nabla^2v + \nabla u\cdot\nabla v\big)d\tau,
\qquad
\oint(u\nabla v - v\nabla u)\cdot d\boldsymbol\sigma = \int(u\nabla^2v - v\nabla^2u)\,d\tau
$$

(Arfken Eqs. 1.104–1.105). For functions that decay fast enough the surface terms vanish. Then $\int u\nabla^2v = -\int\nabla u\cdot\nabla v$, which is why the kinetic energy can be written as $\tfrac12\int|\nabla\psi|^2$. And $\int u\nabla^2v = \int v\nabla^2u$, which is why $\nabla^2$ is Hermitian.

## Worked examples

!!! example "Radial divergences, Gauss on a cube, and the 4π (computed for this note)"
    **Divergences.** sympy gives $\nabla\cdot\mathbf r = 3$, $\nabla\cdot(\mathbf r/r^3) = 0$ away from the origin, and $\nabla\cdot(r^n\mathbf r)/r^n = 5.5$ at $n = 2.5$, i.e. $n + 3$, Eq. [[#divrn]].

    **Gauss on the unit cube.** For $\mathbf V = (x^2y,\ yz,\ x\sin z)$, $\nabla\cdot\mathbf V = 2xy + z + x\cos z$. Its integral over $[0,1]^3$ is $\tfrac12 + \tfrac12 + \tfrac12\sin1 = 1 + \tfrac12\sin1 = 1.42074$. The fluxes through the three pairs of faces are $\tfrac12$ (the $x$ faces), $\tfrac12$ (the $y$ faces) and $\tfrac12\sin1$ (the $z$ faces), the same total.

    **The 4π.** The flux of $\mathbf r/r^3$ through a sphere is $4\pi$ for every radius, while the divergence is zero for $r > 0$, so the source sits at the origin, Eq. [[#delta]].

## Source

Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005), Sec. 1.7 (divergence, Eq. 1.66, Examples 1.7.1–1.7.2), Sec. 1.11 (Gauss's theorem, Eq. 1.101a; Green's theorem, Eqs. 1.104–1.105; alternate forms, Eqs. 1.109–1.110), Sec. 1.14 (Gauss's law), Sec. 1.15 (Eq. 1.170). Calculations in `Claude outputs/part0_math_batchE.py`, section B.
