---
id: partial-differential-equations-and-separation-of-variables
title: Partial differential equations and separation of variables - the Laplace, Poisson, diffusion, wave, Helmholtz and Schrödinger equations, boundary conditions, and separation in Cartesian, spherical and cylindrical coordinates
summary: The linear PDEs of physics are built from the Laplacian: Laplace and Poisson (elliptic: static fields), diffusion (parabolic: heat flow, Fick's law), and waves (hyperbolic). The Helmholtz and time-independent Schrödinger equations come from them by separating off time. Dirichlet, Neumann or periodic boundary conditions on a closed boundary make the elliptic problems well posed. Separation of variables writes the solution as a product of one-variable functions. Each separation constant turns the PDE into ODEs, and the boundary conditions turn those into eigenvalue problems. In Cartesian coordinates this gives sines and Fourier series, in spherical coordinates Legendre functions and spherical harmonics, in cylindrical coordinates Bessel functions. Worked examples: heat flow from a box profile, a harmonic function on a rectangle, and the degeneracies of a particle in a cube.
status: in-progress
kind: theory
level: intermediate
tags: [partial-differential-equation, separation-of-variables, laplace-equation, poisson-equation, diffusion-equation, heat-equation, wave-equation, helmholtz-equation, schrodinger-equation, boundary-conditions, dirichlet, neumann, separation-constant]
prerequisites: [second-order-linear-differential-equations, curvilinear-coordinates, fourier-series]
related: [series-solutions-and-the-frobenius-method, sturm-liouville-theory, classical-orthogonal-polynomials, spherical-bessel-functions, vector-identities-and-the-laplacian, hydrogen-atom]
key: heat
order: 30
date: 2026-11-25
---

$u(\mathbf r, t)$ is the unknown field; $\nabla^2$ the Laplacian ([[vector-identities-and-the-laplacian]], in curvilinear form in [[curvilinear-coordinates]]). $D$ is a diffusion constant, $c$ a wave speed.

## The equations of physics

Arfken Sec. 9.1 collects the standard linear PDEs:

| equation | form | type | describes |
|---|---|---|---|
| Laplace | $\nabla^2u = 0$ | elliptic | electrostatics without charge, steady heat flow, potential flow |
| Poisson | $\nabla^2u = -\rho/\varepsilon_0$ | elliptic | electrostatics with sources; the Hartree potential |
| diffusion (heat) | $\partial_tu = D\nabla^2u$ | parabolic | heat conduction, Fick diffusion, imaginary-time quantum dynamics |
| wave | $\nabla^2u = c^{-2}\partial_t^2u$ | hyperbolic | sound, light, strings |
| Helmholtz | $(\nabla^2 + k^2)u = 0$ | elliptic | wave or diffusion equation at a single frequency |
| Schrödinger | $i\hbar\partial_t\psi = [-\frac{\hbar^2}{2m}\nabla^2 + V]\psi$ | (parabolic in form, imaginary time step) | quantum dynamics |

**Classification.** For $Au_{xx} + 2Bu_{xy} + Cu_{yy} + \cdots = 0$ the type follows the discriminant $B^2 - AC$: negative is elliptic, zero parabolic, positive hyperbolic, as for conic sections. The type decides which conditions give a well-posed problem:

- **Elliptic:** boundary values on a closed surface.
- **Parabolic:** an initial state plus boundary values.
- **Hyperbolic:** an initial state and initial velocity (Arfken Sec. 9.1).

**Separating off time.** For a time-independent $V$, $\psi = \phi(\mathbf r)e^{-iEt/\hbar}$ reduces the Schrödinger equation to the eigenvalue problem $\hat H\phi = E\phi$. The same step reduces the wave equation to Helmholtz with $k = \omega/c$.

**Boundary conditions.**

- **Dirichlet:** $u$ given on the boundary, e.g. $\psi = 0$ at an infinite wall.
- **Neumann:** the normal derivative given.
- **Periodic**, as in crystals with Born–von Kármán conditions.
- **Decay at infinity**, for bound states.

The uniqueness of the elliptic problems follows from Green's theorem ([[divergence-and-gauss-theorem]]).

## Separation of variables

**The method.** Try $u = X(x)Y(y)Z(z)T(t)$, substitute, and divide by $u$ (Arfken Sec. 9.3). If the equation separates, each term depends on one variable only. A sum of functions of different variables can be constant only if each term is constant. Each term therefore equals a **separation constant**, and the PDE becomes a set of ODEs.

**Eigenvalue problems.** The boundary conditions on each ODE allow only certain values of the constants. Those are eigenvalue problems of Sturm–Liouville type ([[sturm-liouville-theory]]). The general solution is a sum over the allowed products. Its coefficients come from the initial or boundary data by orthogonality: a Fourier series or another eigenfunction expansion ([[eigenfunction-expansions-and-generating-functions]]).

**Which coordinates separate.** Separation works only for coordinates adapted to the boundary and the potential. Spherical coordinates suit central potentials; prolate spheroidal coordinates suit $\mathrm H_2^+$. The Helmholtz equation separates in at least eleven coordinate systems (Arfken Sec. 2.3).

### Cartesian coordinates

**The heat equation on an interval.** $\partial_tu = D\partial_x^2u$ on $(0, L)$ with $u(0) = u(L) = 0$. With $u = X(x)T(t)$,

$$
\frac{T'}{DT} = \frac{X''}{X} = -k^2\quad\Rightarrow\quad X_n = \sin\frac{n\pi x}L,\quad u = \sum_nb_n\sin\frac{n\pi x}L\,e^{-D(n\pi/L)^2t} .
\label{heat}
$$

The $b_n$ are the Fourier sine coefficients of $u(x, 0)$ ([[fourier-series]]). High modes decay fastest, so an initial profile smooths out: diffusion is a low-pass filter (Arfken Sec. 9.8).

**Laplace's equation on a rectangle.** $X''/X = -Y''/Y = -k^2$ gives $\sin kx\sinh ky$: oscillation in one direction forces exponential behaviour in the other.

**A particle in a box.** The three-dimensional box separates into three one-dimensional boxes, with $E = \frac{\pi^2\hbar^2}{2mL^2}(n_x^2 + n_y^2 + n_z^2)$. A cube has degeneracies from permutations of $(n_x, n_y, n_z)$, a symmetry consequence.

### Spherical coordinates

**Separation.** With $\nabla^2 = r^{-2}\partial_r(r^2\partial_r) - \hat L^2/(\hbar^2r^2)$ ([[curvilinear-coordinates]]), try $u = R(r)\Theta(\theta)\Phi(\phi)$ for a central potential:

- **$\phi$:** $\Phi'' = -m^2\Phi$, so $\Phi = e^{im\phi}$, with integer $m$ for single-valuedness.
- **$\theta$:** the associated Legendre equation, whose solutions regular at both poles exist only for $l(l + 1)$ with integer $l\ge|m|$. Together with $\Phi$ they form the spherical harmonics $Y_{lm}$ ([[classical-orthogonal-polynomials]]).
- **$r$:** the radial equation
  $$\frac1{r^2}\frac{d}{dr}\Big(r^2\frac{dR}{dr}\Big) - \frac{l(l + 1)}{r^2}R + \frac{2m_e}{\hbar^2}[E - V(r)]R = 0 .$$
  It gives powers $r^l$ and $r^{-l-1}$ for Laplace's equation, spherical Bessel functions for a free particle ([[spherical-bessel-functions]]), and Laguerre functions for hydrogen ([[hydrogen-atom]]).

**Laplace's equation.** $\nabla^2u = 0$ gives the solid harmonics $r^lY_{lm}$ and $r^{-l-1}Y_{lm}$. Their sums are the multipole expansions of electrostatics.

### Cylindrical coordinates

$u = R(\rho)\Phi(\phi)Z(z)$ with $Z = e^{\pm kz}$ (or $e^{\pm ikz}$) and $\Phi = e^{im\phi}$. The radial factor satisfies Bessel's equation $\rho^2R'' + \rho R' + (k^2\rho^2 - m^2)R = 0$, solved by $J_m(k\rho)$ and $Y_m(k\rho)$ (Arfken Ch. 11).

## Worked examples

!!! example "Heat flow, a harmonic function, and degeneracies (computed for this note)"
    **Heat flow from a box profile.** $u(x, 0) = 1$ on $(0, L)$ with ends held at 0. Its sine coefficients are $b_n = 4/(n\pi)$ for odd $n$ and 0 for even $n$ (the square wave of [[fourier-series]]). By Eq. [[#heat]], the $n = 3$ mode decays nine times faster than $n = 1$. After a time $L^2/(\pi^2D)$ it has fallen by $e^{-9}$ against $e^{-1}$, and the profile is essentially the single half-sine.

    **A harmonic function.** sympy: $\nabla^2[\sin\pi x\sinh\pi y] = 0$. It vanishes on $x = 0$ and $x = 1$ and on $y = 0$. So it solves Laplace's equation on the unit square with the top edge held at $\sinh\pi\,\sin\pi x$.

    **Particle in a cube.** Levels $n_x^2 + n_y^2 + n_z^2$ and their degeneracies:

    | $n_x^2 + n_y^2 + n_z^2$ | 3 | 6 | 9 | 11 | 12 | 14 |
    |---|---|---|---|---|---|---|
    | degeneracy | 1 | 3 | 3 | 3 | 1 | 6 |

    The 6-fold level is $(1, 2, 3)$ in all orders. The others are permutations of two equal and one different integer, or three equal ones.

## Source

Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005), Sec. 9.1 (partial differential equations of physics, classification, boundary conditions), Sec. 2.3 (separable coordinate systems), Sec. 9.3 (separation of variables in Cartesian, cylindrical and spherical coordinates), Sec. 9.8 (heat flow PDE), Ch. 11 (Bessel functions). Calculations in `Claude outputs/part0_math_batchE.py`, section E.
