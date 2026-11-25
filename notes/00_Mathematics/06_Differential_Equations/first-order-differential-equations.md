---
id: first-order-differential-equations
title: First-order ordinary differential equations - classification, separable and exact equations, integrating factors, the linear equation, Bernoulli and logistic equations, existence and uniqueness, and rate laws
summary: An ordinary differential equation relates a function of one variable to its derivatives. Its order is the highest derivative, and it is linear if the unknown and its derivatives enter linearly. First-order equations y' = f(x, y) are solved by a few methods: separating variables; recognizing an exact differential P dx + Q dy = dφ; multiplying by an integrating factor, which always works for the linear equation y' + p(x)y = q(x) with factor e^{∫p}; and substitutions, such as the one that makes the Bernoulli and logistic equations linear. Under mild conditions (Picard–Lindelöf) a solution through each initial point exists and is unique. Chemical rate laws are the natural examples. Worked examples: first- and second-order kinetics and their half-lives, a linear equation by integrating factor, an exact equation, and the logistic curve.
status: in-progress
kind: theory
level: introductory
tags: [ordinary-differential-equation, first-order, separation-of-variables, exact-equation, integrating-factor, linear-ode, bernoulli-equation, logistic-equation, initial-value-problem, picard-lindelof, rate-law, kinetics]
prerequisites: [integral-calculus, differential-calculus]
related: [second-order-linear-differential-equations, partial-differential-equations-and-separation-of-variables, time-dependent-perturbation-theory]
key: linear1
order: 10
date: 2026-11-25
---

$y = y(x)$ (or $y(t)$), $y' = dy/dx$. $C$ denotes an integration constant fixed by an initial condition $y(x_0) = y_0$.

## Classification

**Order and linearity.** An ordinary differential equation (ODE) involves one independent variable; a partial differential equation (PDE) involves several ([[partial-differential-equations-and-separation-of-variables]]). The **order** is that of the highest derivative. An ODE is **linear** if it has the form

$$
a_n(x)y^{(n)} + \cdots + a_1(x)y' + a_0(x)y = f(x).
$$

It is **homogeneous** if $f = 0$. For linear homogeneous equations, any linear combination of solutions is a solution (superposition). The time-dependent Schrödinger equation is linear for this reason, and quantum states can be superposed.

**Counting constants.** The general solution of an $n$-th order ODE contains $n$ arbitrary constants, fixed by $n$ initial or boundary conditions.

## Methods for first-order equations

Arfken Sec. 9.2 treats these methods.

**Separable equations.** $y' = f(x)g(y)$. Divide and integrate:

$$
\int\frac{dy}{g(y)} = \int f(x)\,dx + C .
$$

Zeros of $g$ give constant solutions that division loses.

**Exact equations.** $P(x, y)\,dx + Q(x, y)\,dy = 0$ is exact if $\partial P/\partial y = \partial Q/\partial x$ ([[differential-calculus]]). Then $P\,dx + Q\,dy = d\varphi$ for a potential $\varphi$, and the solution is $\varphi(x, y) = C$. Find $\varphi$ by integrating $P$ in $x$ and fixing the remaining function of $y$ from $\partial\varphi/\partial y = Q$. This is the same construction as recovering a scalar potential from a curl-free field ([[scalar-and-vector-fields-and-the-gradient]]).

**Integrating factors.** If the equation is not exact, a function $\alpha(x, y)$ with $\alpha P\,dx + \alpha Q\,dy$ exact may exist. In general it is hard to find. For the linear equation it always exists.

**The linear first-order equation.** For $y' + p(x)y = q(x)$, choose $\alpha(x) = \exp\int p(x)\,dx$. Then $(\alpha y)' = \alpha q$, and

$$
y(x) = \frac1{\alpha(x)}\Big[\int\alpha(x)q(x)\,dx + C\Big],\qquad \alpha = e^{\int p\,dx} .
\label{linear1}
$$

The solution is a particular solution plus $C/\alpha$, the general solution of the homogeneous equation. That structure holds for every linear equation ([[second-order-linear-differential-equations]]). Arfken derives it as Eqs. 9.25–9.31 and applies it to an $RL$ circuit.

**Substitutions.**

- **Bernoulli equation.** $y' + p(x)y = q(x)y^n$ ($n\ne0, 1$) becomes linear in $v = y^{1-n}$.
- **Logistic equation.** $y' = ry(1 - y/K)$ is the case $n = 2$; it describes autocatalysis and population growth.
- **Homogeneous form.** $y' = F(y/x)$ separates in $v = y/x$.

## Existence and uniqueness

**Picard–Lindelöf theorem.** If $f(x, y)$ is continuous and Lipschitz in $y$ near $(x_0, y_0)$ (for example, $\partial f/\partial y$ continuous), the initial value problem $y' = f(x, y)$, $y(x_0) = y_0$, has exactly one solution near $x_0$. Two solution curves never cross.

**When the conditions fail.** Uniqueness can fail: $y' = \sqrt{|y|}$ with $y(0) = 0$ has the solutions $y = 0$ and $y = x^2/4$ (for $x\ge0$). Solutions can also blow up in finite time: $y' = y^2$ gives $y = 1/(C - x)$.

**Numerical integration.** Every numerical integrator (Euler, Runge–Kutta, the Verlet algorithm of molecular dynamics, which treats a second-order equation) steps along this unique solution. The errors come from truncating the Taylor expansion of $y(x + h)$ ([[taylor-and-maclaurin-expansions]]).

## Rate laws

**First order.** $A\to P$ with rate $k[A]$: $d[A]/dt = -k[A]$ separates to $[A] = [A]_0e^{-kt}$. The half-life $t_{1/2} = \ln2/k$ is independent of $[A]_0$. Radioactive decay and unimolecular reactions follow this law.

**Second order.** $2A\to P$ with $d[A]/dt = -k[A]^2$ separates to $1/[A] = 1/[A]_0 + kt$. The half-life $t_{1/2} = 1/(k[A]_0)$ depends on the starting concentration. This is how the order is diagnosed experimentally.

**Coupled first-order equations.** A reaction network $d\mathbf c/dt = \mathbf K\mathbf c$ is a linear system. It is solved by diagonalizing $\mathbf K$, or by the matrix exponential $\mathbf c(t) = e^{\mathbf Kt}\mathbf c(0)$ ([[neumann-series-and-operator-expansions]]). The time-dependent Schrödinger equation $i\hbar\dot{\mathbf c} = \mathbf H\mathbf c$ in a finite basis has the same form.

## Worked examples

!!! example "Rate laws, an integrating factor, an exact equation (computed for this note)"
    **Kinetics** (sympy `dsolve`):

    - $y' = -ky$ gives $y = Ce^{-kt}$.
    - $y' = -ky^2$ with $y(0) = y_0$ gives $y = 1/(kt + 1/y_0)$.

    With $k = 0.1$ and $y_0 = 1$, both start at the same rate. At $t = 10$ the first-order case has $e^{-1} = 0.368$ left and the second-order case $1/2$. The second-order law starts at the same slope and decays more slowly later.

    **Integrating factor.** $y' + 2y/t = t$: $p = 2/t$ and $\alpha = t^2$. Then $(t^2y)' = t^3$, so $y = t^2/4 + C/t^2$. sympy gives the same: $y = (C_1 + t^4/4)/t^2$.

    **Exact equation.** $(2xy + 1)\,dx + (x^2 + 2y)\,dy = 0$ has $\partial_y(2xy + 1) = 2x = \partial_x(x^2 + 2y)$. Integrating gives $\varphi = x^2y + x + y^2$; its partials reproduce $2xy + 1$ and $x^2 + 2y$. The solutions are the level curves $x^2y + x + y^2 = C$.

    **Logistic equation.** $y' = 2y(1 - y)$ gives $y = 1/(1 + C_1e^{-2t})$: a sigmoid that rises from near 0 to the carrying capacity 1.

## Source

Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005), Sec. 9.2 (first-order ODEs: separable variables, exact differential equations, integrating factors, the linear first-order equation with the circuit example, Eqs. 9.16–9.31). The Bernoulli substitution, the Picard–Lindelöf statement and the rate laws are standard material not taken from Arfken. Calculations in `Claude outputs/part0_math_batchE.py`, section E.
