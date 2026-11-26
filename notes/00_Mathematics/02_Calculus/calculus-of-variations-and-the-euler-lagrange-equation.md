---
id: calculus-of-variations-and-the-euler-lagrange-equation
title: Calculus of variations - functionals, the first variation, the Euler-Lagrange equation and Beltrami identity, several functions and several variables, constraints with Lagrange multipliers, and the Rayleigh-Ritz method
summary: A functional J[y] = ∫ f(y, y', x) dx assigns a number to a whole function. It is stationary when its first variation vanishes for every admissible change δy. Integrating by parts turns that into the Euler–Lagrange equation ∂f/∂y − d/dx(∂f/∂y') = 0, and when f does not depend on x explicitly, into the first integral f − y'∂f/∂y' = constant (Beltrami). The same steps give one equation per unknown function (Hamilton's principle and Lagrange's equations of motion) and partial differential equations for several independent variables (Laplace's equation). Constraints of integral form, such as a fixed length or normalization, enter with a Lagrange multiplier. Normalization turns the stationary energy into the Schrödinger equation with the energy as the multiplier. Restricting y to a family of trial functions turns the problem back into ordinary minimization: the Rayleigh–Ritz method behind every variational calculation. Worked examples: the catenary, the brachistochrone, Ritz estimates for a vibrating string, and hydrogen with one Gaussian.
status: in-progress
kind: theory
level: intermediate
tags: [calculus-of-variations, functional, first-variation, euler-lagrange-equation, beltrami-identity, hamilton-principle, brachistochrone, catenary, isoperimetric-problem, rayleigh-ritz, variational-method, natural-boundary-conditions]
prerequisites: [integral-calculus, differential-calculus]
related: [functional-derivatives, lagrange-multipliers-and-kkt-conditions, variational-principle, sturm-liouville-theory, partial-differential-equations-and-separation-of-variables, envelope-theorem-and-the-lagrangian-method]
key: el
order: 70
date: 2026-11-26
---

$y(x)$ on $[x_1, x_2]$, $y' = dy/dx$, and $f(y, y', x)$ is a smooth integrand. $\delta y(x) = \epsilon\eta(x)$ is a small admissible change; $\eta$ vanishes at fixed endpoints. Notation follows Arfken Ch. 17, which writes $y_x$ for $y'$.

## Functionals and their variation

**Functionals.** A functional maps a function to a number (Arfken Eq. 17.1):

$$
J[y] = \int_{x_1}^{x_2}f\big(y(x), y'(x), x\big)\,dx .
$$

Examples:

- the length of a curve, $\int\sqrt{1 + y'^2}\,dx$;
- the time to slide down it;
- the action $\int L\,dt$ of a trajectory;
- the energy $\langle\psi|\hat H|\psi\rangle$ of a wave function;
- the energy $E[\rho]$ of a density.

**The first variation.** Replace $y$ by $y + \epsilon\eta$ and expand $J(\epsilon)$ in $\epsilon$:

$$
\frac{dJ}{d\epsilon}\Big|_{\epsilon=0} = \int_{x_1}^{x_2}\Big(\frac{\partial f}{\partial y}\eta + \frac{\partial f}{\partial y'}\eta'\Big)dx
= \Big[\frac{\partial f}{\partial y'}\eta\Big]_{x_1}^{x_2} + \int_{x_1}^{x_2}\Big(\frac{\partial f}{\partial y} - \frac{d}{dx}\frac{\partial f}{\partial y'}\Big)\eta\,dx
$$

(Arfken Eqs. 17.6–17.13). The second form comes from integrating the $\eta'$ term by parts.

**Stationarity.** $y$ makes $J$ stationary if this vanishes for every admissible $\eta$. That is the function-space version of $\nabla f = 0$. With fixed endpoints the boundary term is zero.

## The Euler–Lagrange equation

**Statement.** Since $\eta$ is arbitrary inside the interval, the bracket must vanish pointwise (the fundamental lemma of the calculus of variations). That gives the Euler–Lagrange equation (Arfken Eq. 17.15):

$$
\frac{\partial f}{\partial y} - \frac{d}{dx}\frac{\partial f}{\partial y'} = 0 .
\label{el}
$$

It is a second-order ODE for $y$, with the two endpoint values as boundary conditions ([[second-order-linear-differential-equations]]).

**What it does and does not guarantee.** Eq. [[#el]] is necessary for a smooth stationary path. It does not by itself say whether the path is a minimum, a maximum or a saddle, and solutions that are not twice differentiable can be missed. Arfken's examples include a great circle that is a saddle and Goldschmidt's discontinuous soap-film solution.

**The Beltrami identity.** If $f$ does not depend explicitly on $x$, multiply Eq. [[#el]] by $y'$ to get a first integral (Arfken Eqs. 17.16–17.18):

$$
f - y'\frac{\partial f}{\partial y'} = \text{constant} .
\label{beltrami}
$$

It is the analogue of energy conservation when the Lagrangian has no explicit time dependence.

**Natural boundary conditions.** If $y(x_2)$ is free, the boundary term must vanish on its own, giving $\partial f/\partial y' = 0$ at $x_2$. Free-end problems in mechanics and Neumann conditions in field theory come from this.

**Standard examples** (Arfken Sec. 17.2):

| problem | integrand $f$ | solution |
|---|---|---|
| shortest path in the plane | $\sqrt{1 + y'^2}$ | straight line ($y'' = 0$) |
| soap film between two rings (minimal surface of revolution) | $y\sqrt{1 + y'^2}$ | catenary $y = a\cosh\frac{x - b}{a}$ |
| fastest slide under gravity (brachistochrone) | $\sqrt{(1 + y'^2)/(2g\,|y|)}$ | cycloid |

## More functions, more variables

**Several dependent variables** (Arfken Sec. 17.3). For $J = \int f(y_1,\dots,y_n, y_1',\dots,y_n', x)\,dx$ one gets an Euler–Lagrange equation for each $y_i$.

**Hamilton's principle.** With $x\to t$, $y_i\to q_i$ and $f\to L = T - V$, these are Lagrange's equations of motion, $\partial L/\partial q_i - \frac{d}{dt}\partial L/\partial\dot q_i = 0$. For $L = \tfrac12m\dot q^2 - \tfrac12kq^2$ this gives $m\ddot q = -kq$. Classical mechanics, the time-dependent variational principle of quantum dynamics, and Hartree–Fock's derivation from $\langle\Phi|\hat H|\Phi\rangle$ all have this form.

**Several independent variables** (Arfken Sec. 17.4). For $J = \int f(u, \partial_xu, \partial_yu, \partial_zu, x, y, z)\,d\tau$ the Euler–Lagrange equation becomes a PDE:

$$
\frac{\partial f}{\partial u} - \sum_k\frac{\partial}{\partial x_k}\frac{\partial f}{\partial(\partial_ku)} = 0 .
$$

The Dirichlet integral $\int|\nabla u|^2d\tau$ gives Laplace's equation (Arfken Example 17.4.1). Gradient-dependent density functionals give the functional derivative $\partial f/\partial\rho - \nabla\cdot\partial f/\partial\nabla\rho$ ([[functional-derivatives]]).

## Constraints

**Integral constraints.** To make $J[y]$ stationary subject to $K[y] = \int g(y, y', x)\,dx = $ const (fixed length, fixed area, normalization), make $J - \lambda K$ stationary and determine the constant $\lambda$ from the constraint (Arfken Secs. 17.6–17.7). The Euler–Lagrange equation applies to $f - \lambda g$. The multiplier is the sensitivity $dJ^*/dK$, as in finite dimensions ([[lagrange-multipliers-and-kkt-conditions]]).

**The Schrödinger equation as a constrained variation.** Make $\int\big(\frac{\hbar^2}{2m}|\nabla\psi|^2 + V|\psi|^2\big)d\tau$ stationary subject to $\int|\psi|^2d\tau = 1$ (Arfken Example 17.7.3). The Euler–Lagrange equation of the integrand minus $E|\psi|^2$ is

$$
-\frac{\hbar^2}{2m}\nabla^2\psi + V\psi = E\psi .
$$

The multiplier is the energy eigenvalue, and the stationary functions are the eigenfunctions ([[variational-principle]]). The same argument for $\int(p|y'|^2 - q|y|^2)$ with weight $w$ gives the Sturm–Liouville equation ([[sturm-liouville-theory]]).

**Pointwise constraints.** A constraint at every point, $g(y_1, y_2, x) = 0$, needs a multiplier function $\lambda(x)$. In mechanics, $\lambda(t)$ is the constraint force (Arfken Sec. 17.7).

## The Rayleigh–Ritz method

**The method.** Restrict $y$ to a family of trial functions $y(x;\mathbf c)$ with a finite number of parameters. The functional becomes an ordinary function $J(\mathbf c)$, which is minimized by setting $\partial J/\partial c_i = 0$ (Arfken Sec. 17.8).

**Why it works well.** For an eigenvalue problem the minimum of the Rayleigh quotient is an upper bound to the lowest eigenvalue. Because the quotient is stationary, an error $\delta y$ in the trial function gives an error $O(\delta y^2)$ in the eigenvalue.

**Linear parameters.** For trial functions linear in their parameters, $y = \sum_ic_i\phi_i$, the stationarity conditions are the matrix eigenvalue problem $\mathbf{Hc} = E\mathbf{Sc}$: every basis-set calculation in quantum chemistry. Nonlinear parameters (Gaussian exponents, geometries) are optimized as ordinary functions.

## Worked examples

!!! example "Euler–Lagrange solutions and Ritz estimates (computed for this note)"
    **Euler–Lagrange equations by sympy.**

    - $\sqrt{1 + y'^2}$ gives $-y''/(1 + y'^2)^{3/2} = 0$, a straight line.
    - $y\sqrt{1 + y'^2}$ is solved exactly by $y = a\cosh((x - b)/a)$ (residual 0).
    - For that catenary the Beltrami expression, Eq. [[#beltrami]], is the constant $a$.
    - $L = \tfrac12m\dot q^2 - \tfrac12kq^2$ gives $-kq - m\ddot q = 0$.

    **Brachistochrone** from $(0, 0)$ to $(\pi, -2)$ m, with $g = 9.81$ m s⁻². The cycloid through these points has radius 1 m.

    | path | time (s) |
    |---|---:|
    | straight line | 1.18904 |
    | parabola $x = (\pi/4)y^2$ | 1.01287 |
    | cycloid | 1.00303 |
    | best 60-segment polygon (numerically optimized) | 1.00441 |

    The optimized polygon lies within 0.024 m of the cycloid everywhere, although nothing told the optimizer about cycloids.

    **Ritz, vibrating string or particle in a box** (Arfken Example 17.8.1). The lowest eigenvalue of $-y'' = \lambda y$ on $[0, 1]$ is $\pi^2 = 9.869604$.

    - The trial $x(1 - x)$ gives $\int y'^2/\int y^2 = 10$, 1.3% high.
    - Adding a parameter, $x(1 - x)[1 + c\,x(1 - x)]$, gives $c = 1.1331$ and $\lambda = 9.869750$, a relative error of $1.5\times10^{-5}$.

    **Hydrogen with one Gaussian.** $\phi = e^{-\alpha r^2}$ gives $E(\alpha) = \tfrac32\alpha - 2\sqrt{2\alpha/\pi}$ hartree. Minimizing over the one nonlinear parameter gives $\alpha^* = 8/(9\pi) = 0.282942$ and $E^* = -4/(3\pi) = -0.424413$ hartree, against the exact $-0.5$. At the optimum $-V/T = 2.000000$: the virial theorem holds for an optimized scale parameter, as stationarity requires.

## Source

Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005), Sec. 17.1 (one dependent and one independent variable, Eqs. 17.1–17.18), Sec. 17.2 (applications: straight line, soap film), Sec. 17.3 (several dependent variables, Hamilton's principle), Sec. 17.4 (several independent variables, Example 17.4.1), Secs. 17.6–17.7 (Lagrangian multipliers, variation with constraints, Example 17.7.3), Sec. 17.8 (Rayleigh–Ritz technique, Example 17.8.1). The brachistochrone and Gaussian-hydrogen numbers are computed here. Calculations in `Claude outputs/part0_math_batchF.py`, section E.
