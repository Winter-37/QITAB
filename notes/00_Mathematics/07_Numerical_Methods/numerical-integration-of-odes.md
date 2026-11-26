---
id: numerical-integration-of-odes
title: Numerical integration of ordinary differential equations - Euler and Runge-Kutta methods, local and global error, order, adaptive step control, stability regions, stiffness and implicit methods
summary: A one-step method advances y' = f(t, y) by approximating the Taylor series of y(t + h). Euler keeps the first-order term and has global error O(h). Runge–Kutta methods combine several evaluations of f per step to match more Taylor terms without derivatives of f: RK2 is O(h²), the classical RK4 O(h⁴). Embedded pairs estimate the local error and adapt the step to a tolerance. Accuracy is not the only constraint. For y' = λy, an explicit method is stable only if hλ lies in a bounded region, so a fast decay forces tiny steps long after it has died out: stiffness. Implicit methods (backward Euler, BDF, Radau) are stable for any step on decaying modes, at the price of a linear solve per step. General-purpose integrators also slowly drift in the energy of a Hamiltonian system. That motivates the symplectic integrators used in molecular dynamics. Worked examples: measured orders, adaptive steps, a stiff consecutive reaction, the explicit stability limit, and RK4 energy drift.
status: in-progress
kind: theory
level: intermediate
tags: [ode-integration, euler-method, runge-kutta, rk4, local-error, global-error, order-of-accuracy, adaptive-step-size, embedded-runge-kutta, stability-region, stiffness, implicit-euler, bdf, kinetics]
prerequisites: [first-order-differential-equations, taylor-and-maclaurin-expansions, floating-point-and-numerical-error]
related: [velocity-verlet-and-symplectic-integration, second-order-linear-differential-equations, laplace-transform, gaussian-quadrature]
key: rk4
order: 40
date: 2026-11-26
---

Initial value problem $y' = f(t, y)$, $y(t_0) = y_0$, with $y$ a scalar or a vector; step $h$, $t_n = t_0 + nh$, $y_n\approx y(t_n)$. A higher-order equation is first written as a first-order system, as in $q'' = F(q)/m$ with $(q, p)$ ([[first-order-differential-equations]]).

## One-step methods and their error

**Euler's method.** Keep the first two terms of the Taylor series $y(t + h) = y + hy' + \tfrac12h^2y'' + \cdots$ ([[taylor-and-maclaurin-expansions]]):

$$
y_{n+1} = y_n + hf(t_n, y_n) .
$$

**Local and global error.**

- **Local error.** The error made in one step from exact data is $O(h^{p+1})$ for a method of order $p$; for Euler it is $\tfrac12h^2y''$.
- **Global error.** Over a fixed interval, $T/h$ local errors accumulate, propagated by the equation's own stability, so the global error is $O(h^p)$. Euler is first order: halving $h$ halves the error.
- **Round-off.** It adds an error growing like $\varepsilon/h$ per step, so very small steps do not help ([[floating-point-and-numerical-error]]).

**Runge–Kutta methods.** Evaluate $f$ at several points inside the step and combine the slopes so that the result matches the Taylor series to higher order, without derivatives of $f$. The classical fourth-order method:

$$
\begin{aligned}
k_1 &= f(t_n, y_n), & k_2 &= f\big(t_n + \tfrac h2, y_n + \tfrac h2k_1\big),\\
k_3 &= f\big(t_n + \tfrac h2, y_n + \tfrac h2k_2\big), & k_4 &= f(t_n + h, y_n + hk_3),\\
y_{n+1} &= y_n + \tfrac h6(k_1 + 2k_2 + 2k_3 + k_4) .
\end{aligned}
\label{rk4}
$$

**Related schemes.**

- **Order 2.** The two-stage methods (Heun's, the midpoint rule) are second order.
- **Relation to quadrature.** For $f$ depending on $t$ only, RK4 reduces to Simpson's rule ([[gaussian-quadrature]]).
- **Multistep methods** (Adams–Bashforth, Adams–Moulton) reuse past values of $f$ instead of extra stages.

**Adaptive steps.** An embedded pair, such as the Dormand–Prince 5(4) behind `RK45`, computes two estimates of different order from the same stages. Their difference estimates the local error, and the step is enlarged where the solution is smooth and shrunk where it changes fast. The user sets a tolerance, not a step size.

## Stability and stiffness

**The test equation.** Apply a method to $y' = \lambda y$ with $\mathrm{Re}\,\lambda < 0$, whose exact solution decays. Each step multiplies $y$ by an amplification factor $R(h\lambda)$. For Euler, $R = 1 + h\lambda$. The numerical solution decays only if $|R(h\lambda)| < 1$, which defines the method's **stability region** in the complex $h\lambda$ plane. For explicit Euler it is the disc $|1 + h\lambda| < 1$: on the real axis, $h < 2/|\lambda|$. For RK4 the real interval is $h|\lambda| < 2.785$. Every explicit method has a bounded stability region.

**Stiffness.** A system is stiff when it contains decay rates much faster than the time scale of interest. The fast modes die out almost at once, but an explicit method must still keep $h|\lambda_{\rm max}|$ inside its stability region for the entire run. The step is then set by stability, not accuracy, and the integration costs about $|\lambda_{\rm max}|/|\lambda_{\rm min}|$ times more than accuracy alone would require. Examples:

- chemical kinetics with fast pre-equilibria;
- radical chain mechanisms;
- the electronic and nuclear time scales in Ehrenfest dynamics;
- diffusion equations on fine grids, where the fastest mode scales as $1/\Delta x^2$.

**Implicit methods.** Backward Euler evaluates $f$ at the new point:

$$
y_{n+1} = y_n + hf(t_{n+1}, y_{n+1}),\qquad R(h\lambda) = \frac1{1 - h\lambda} .
$$

$|R| < 1$ for every $h > 0$ when $\mathrm{Re}\,\lambda < 0$ (A-stability). Each step needs the solution of a (nonlinear) system, with a Newton iteration using the Jacobian $\partial f/\partial y$. Production stiff solvers use higher-order implicit families: backward differentiation formulas (BDF, as in Gear's method) and implicit Runge–Kutta (Radau IIA). Backward Euler itself is only first order.

## Long-time behaviour of Hamiltonian systems

**Energy drift.** A general-purpose integrator has no reason to respect the structure of Hamilton's equations. For an oscillator, RK4 damps the motion slightly at every step. The energy drifts steadily downward, by an amount that grows linearly in time. Over the millions of steps of a molecular-dynamics run this is unacceptable, even though each step is very accurate. Symplectic integrators, whose energy error stays bounded for exponentially long times, are the subject of [[velocity-verlet-and-symplectic-integration]].

## Worked examples

!!! example "Orders, adaptivity, stiffness and drift (computed for this note)"
    **Observed orders.** For $y' = -y + \sin t$, $y(0) = 1$, the global error at $t = 1$ for $h = 0.1$, 0.05, 0.025:

    | method | errors | observed order |
    |---|---|---|
    | Euler | $3.35\times10^{-2}$, $1.63\times10^{-2}$, $8.07\times10^{-3}$ | 1.04, 1.02 |
    | RK2 (Heun) | $8.70\times10^{-4}$, $2.06\times10^{-4}$, $5.03\times10^{-5}$ | 2.07, 2.04 |
    | RK4, Eq. [[#rk4]] | $4.56\times10^{-7}$, $2.68\times10^{-8}$, $1.62\times10^{-9}$ | 4.09, 4.04 |

    At $t = 2$ the RK4 orders come out between 2.8 and 3.8. There the leading error coefficient happens to pass through zero. Measured orders should always be checked at more than one time.

    **Adaptive steps.** `RK45` with relative tolerance $10^{-8}$ covers $t\in[0, 20]$ in 197 steps, between 0.009 and 0.148 long, with final error $6\times10^{-10}$.

    **A stiff consecutive reaction.** $A\to B$ ($k_1 = 10^4$), $B\to C$ ($k_2 = 1$), integrated to $t = 5$ with tolerance $10^{-6}$:

    | method | steps | evaluations of $f$ | error in $[B](5)$ |
    |---|---:|---:|---:|
    | RK45 (explicit) | 15 157 | 106 034 | $7\times10^{-11}$ |
    | Radau (implicit) | 181 | 1 281 | $2\times10^{-12}$ |
    | BDF (implicit) | 235 | 511 | $7\times10^{-8}$ |

    The explicit method spends nearly all its steps resolving a decay that ended at $t\approx10^{-3}$.

    **The stability limit.** Explicit Euler with $h = 1.9\times10^{-4}$, just under $2/k_1$, gives $[A](0.02)\approx-2\times10^{-5}$ (oscillating, but bounded). With $h = 2.1\times10^{-4}$ it gives $-8.6\times10^3$. Backward Euler with $h = 0.1$, 500 times the explicit limit, is stable and gives $[B](5) = 0.00852$ against the exact 0.00674: stable, but first-order accurate.

    **RK4 energy drift.** Harmonic oscillator, $\omega = 1$, $h = 0.2$: the energy falls from 0.5 to 0.497794 after 5000 steps ($t = 1000$) and to 0.478371 after 50 000 steps. The drift is steady and grows linearly in time.

## Source

Standard numerical analysis of ODEs (Runge–Kutta methods, embedded pairs, stability regions, stiffness, BDF and Radau methods), written and checked here. Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005), Sec. 9.2, covers the analytic methods for first-order equations, not their numerical integration. The solvers used are `scipy.integrate.solve_ivp` (RK45 = Dormand–Prince, Radau IIA order 5, variable-order BDF) and hand-written Euler, RK2 and RK4. Calculations in `Claude outputs/part0_math_batchG.py`, section C.
