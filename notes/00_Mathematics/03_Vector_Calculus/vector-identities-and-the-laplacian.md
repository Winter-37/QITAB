---
id: vector-identities-and-the-laplacian
title: Second derivatives, the Laplacian and vector identities - div grad, curl grad = 0, div curl = 0, curl curl, product rules, scalar and vector potentials, and the Laplacian of 1/r
summary: Applying ∇ twice gives five combinations. Two vanish identically: curl grad φ = 0 and div curl V = 0. One is the Laplacian ∇²φ = ∇·∇φ, the operator of the Schrödinger, Poisson, diffusion and wave equations. The last, curl curl V = ∇(∇·V) − ∇²V, defines the vector Laplacian. The vanishing identities have converses on simply connected regions: an irrotational field has a scalar potential, and a solenoidal field has a vector potential. With the product rules and ∇²(1/r) = −4πδ(r), they solve Poisson's equation and lead to the Helmholtz decomposition. Worked examples: symbolic checks of every identity, ∇²rⁿ = n(n + 1)r^{n−2}, and the screened Coulomb function e^{−r}/r.
status: in-progress
kind: theory
level: intermediate
tags: [laplacian, vector-identities, curl-grad, div-curl, curl-curl, scalar-potential, vector-potential, poisson-equation, green-function, harmonic-function, helmholtz-theorem]
prerequisites: [curl-and-stokes-theorem]
related: [curvilinear-coordinates, maxwell-equations-and-helmholtz-decomposition, electromagnetic-potentials-and-gauge-freedom, partial-differential-equations-and-separation-of-variables, divergence-and-gauss-theorem]
key: poisson
order: 50
date: 2026-11-25
---

Cartesian coordinates, $\partial_i = \partial/\partial x_i$, summation over repeated indices. All fields have continuous second derivatives unless a singularity is stated.

## Successive applications of ∇

**The five combinations.** $\nabla$ can act on a gradient (a vector) by div or curl, and on a curl (a vector) by div or curl, and on a divergence (a scalar) by grad (Arfken Sec. 1.9):

| combination | result |
|---|---|
| $\nabla\cdot\nabla\varphi$ | $\nabla^2\varphi$, the Laplacian |
| $\nabla\times\nabla\varphi$ | $0$ |
| $\nabla\cdot(\nabla\times\mathbf V)$ | $0$ |
| $\nabla\times(\nabla\times\mathbf V)$ | $\nabla(\nabla\cdot\mathbf V) - \nabla^2\mathbf V$ |
| $\nabla(\nabla\cdot\mathbf V)$ | (no simpler form) |

**Why two vanish.** In index form, $(\nabla\times\nabla\varphi)_i = \epsilon_{ijk}\partial_j\partial_k\varphi$, and $\nabla\cdot(\nabla\times\mathbf V) = \epsilon_{ijk}\partial_i\partial_jV_k$. In both, $\epsilon$ is antisymmetric in a pair of indices that is contracted with symmetric second derivatives, so the sum is zero.

**Curl curl.** From Eq. [[scalars-and-vectors#epsdelta]],

$$
[\nabla\times(\nabla\times\mathbf V)]_i = \epsilon_{ijk}\epsilon_{klm}\partial_j\partial_lV_m = (\delta_{il}\delta_{jm} - \delta_{im}\delta_{jl})\partial_j\partial_lV_m = \partial_i(\partial_jV_j) - \partial_j\partial_jV_i .
\label{curlcurl}
$$

In Cartesian components $\nabla^2\mathbf V$ is the Laplacian of each component. In curvilinear coordinates it is not, and Eq. [[#curlcurl]] serves as its definition ([[curvilinear-coordinates]]). This identity turns Maxwell's equations into wave equations (Arfken Example 1.9.2).

## The Laplacian

**Definition.** $\nabla^2\varphi = \partial_x^2\varphi + \partial_y^2\varphi + \partial_z^2\varphi$. By Eq. [[divergence-and-gauss-theorem#divdef]], it is the flux of $\nabla\varphi$ out of a small volume per unit volume. Equivalently, $\nabla^2\varphi$ at a point is proportional to how much the average of $\varphi$ over a small sphere exceeds the value at the centre. It appears in:

- the kinetic energy operator $-\frac{\hbar^2}{2m}\nabla^2$;
- Poisson's equation $\nabla^2\phi = -\rho/\varepsilon_0$;
- the diffusion equation $\partial_tu = D\nabla^2u$;
- the wave equation $\nabla^2u = c^{-2}\partial_t^2u$.

**Harmonic functions.** Solutions of Laplace's equation $\nabla^2\varphi = 0$ have no local maxima or minima inside their domain: the average over any sphere equals the value at the centre. Examples: $1/r$ (for $r\ne0$), $x^2 - y^2$, $r^lY_{lm}$. This is the origin of Earnshaw's theorem: no electrostatic field holds a charge in stable equilibrium.

**Radial functions.** $\nabla^2f(r) = f'' + \frac2rf' = \frac1r\frac{d^2}{dr^2}(rf)$. In particular (Arfken Example 1.9.1),

$$
\nabla^2r^n = n(n + 1)\,r^{n-2},\qquad \nabla^2\frac1r = -4\pi\,\delta(\mathbf r).
\label{lapr}
$$

The first vanishes for $n = 0$ and $n = -1$, the two radial harmonic functions. The delta function in the second comes from the flux argument of [[divergence-and-gauss-theorem]] (Arfken Eq. 1.170).

## Product rules

Each follows from the Leibniz rule in index form (Arfken Secs. 1.7–1.9):

| identity | |
|---|---|
| $\nabla(fg) = f\nabla g + g\nabla f$ | |
| $\nabla\cdot(f\mathbf A) = \nabla f\cdot\mathbf A + f\nabla\cdot\mathbf A$ | |
| $\nabla\times(f\mathbf A) = \nabla f\times\mathbf A + f\nabla\times\mathbf A$ | Eq. 1.70 |
| $\nabla\cdot(\mathbf A\times\mathbf B) = \mathbf B\cdot(\nabla\times\mathbf A) - \mathbf A\cdot(\nabla\times\mathbf B)$ | |
| $\nabla\times(\mathbf A\times\mathbf B) = \mathbf A(\nabla\cdot\mathbf B) - \mathbf B(\nabla\cdot\mathbf A) + (\mathbf B\cdot\nabla)\mathbf A - (\mathbf A\cdot\nabla)\mathbf B$ | |
| $\nabla(\mathbf A\cdot\mathbf B) = (\mathbf B\cdot\nabla)\mathbf A + (\mathbf A\cdot\nabla)\mathbf B + \mathbf B\times(\nabla\times\mathbf A) + \mathbf A\times(\nabla\times\mathbf B)$ | Eq. 1.80 |
| $\nabla^2(fg) = f\nabla^2g + 2\nabla f\cdot\nabla g + g\nabla^2f$ | |

## Potentials

**Scalar potential.** On a simply connected region, $\nabla\times\mathbf F = 0$ if and only if $\mathbf F = -\nabla\varphi$ ([[curl-and-stokes-theorem]]). The potential is unique up to a constant.

**Vector potential.** On a region where every closed surface can shrink to a point, $\nabla\cdot\mathbf B = 0$ if and only if $\mathbf B = \nabla\times\mathbf A$ (Arfken Sec. 1.13). $\mathbf A$ is unique only up to a gradient, $\mathbf A\to\mathbf A + \nabla\chi$, since $\nabla\times\nabla\chi = 0$. That is gauge freedom ([[electromagnetic-potentials-and-gauge-freedom]]).

**Poisson's equation and its Green's function.** Eq. [[#lapr]] says that $G(\mathbf r,\mathbf r') = 1/(4\pi|\mathbf r - \mathbf r'|)$ solves $\nabla^2G = -\delta(\mathbf r - \mathbf r')$. Superposing point sources gives the solution that vanishes at infinity:

$$
\nabla^2\phi = -\frac{\rho}{\varepsilon_0}\quad\Rightarrow\quad\phi(\mathbf r) = \frac1{4\pi\varepsilon_0}\int\frac{\rho(\mathbf r')}{|\mathbf r - \mathbf r'|}d\tau' .
\label{poisson}
$$

This integral is the Hartree (Coulomb) potential of an electron density. Expanding $1/|\mathbf r - \mathbf r'|$ in Legendre polynomials gives the multipole expansion ([[eigenfunction-expansions-and-generating-functions]]).

**Helmholtz's theorem.** A field that vanishes fast enough at infinity is fixed by its divergence and curl. It splits uniquely into an irrotational and a solenoidal part, $\mathbf V = -\nabla\varphi + \nabla\times\mathbf A$ (Arfken Sec. 1.16; worked out for electromagnetism in [[maxwell-equations-and-helmholtz-decomposition]]).

## Worked examples

!!! example "Identities, radial Laplacians and the screened Coulomb function (computed for this note)"
    **Identities for arbitrary functions** (sympy, with $f$ and $G_i$ undefined functions of $x, y, z$):

    - $\nabla\times\nabla f = 0$;
    - $\nabla\cdot\nabla\times\mathbf G = 0$;
    - $\nabla\times\nabla\times\mathbf G - [\nabla(\nabla\cdot\mathbf G) - \nabla^2\mathbf G] = 0$;
    - $\nabla\cdot(f\mathbf G) - (\nabla f\cdot\mathbf G + f\nabla\cdot\mathbf G) = 0$.

    **Radial Laplacians.** $\nabla^2(1/r) = 0$ for $r\ne0$. $\nabla^2(e^{-r}/r) = e^{-r}/r$ for $r\ne0$, so $e^{-\kappa r}/(4\pi r)$ is the Green's function of $\nabla^2 - \kappa^2$: the screened (Yukawa, Debye–Hückel) potential. The radial formula $\frac1r(rf)''$ gives the same: $(e^{-r})''/r = e^{-r}/r$.

    **A harmonic function.** $x^2 - y^2 = r^2\sin^2\theta\cos2\phi$ has $\nabla^2 = 2 - 2 = 0$; it is $r^2$ times a combination of $Y_{2,\pm2}$.

## Source

Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005), Sec. 1.9 (successive applications of ∇, Examples 1.9.1–1.9.2), Secs. 1.7–1.8 (product rules, Eqs. 1.70 and 1.80), Sec. 1.13 (potential theory), Sec. 1.15 (Eq. 1.170), Sec. 1.16 (Helmholtz's theorem). Calculations in `Claude outputs/part0_math_batchE.py`, section B.
