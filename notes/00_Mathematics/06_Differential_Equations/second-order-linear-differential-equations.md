---
id: second-order-linear-differential-equations
title: Second-order linear ODEs - superposition and the Wronskian, constant coefficients and the characteristic equation, damped and driven oscillators, particular solutions by undetermined coefficients and variation of parameters, and Green's functions
summary: The general solution of y'' + p(x)y' + q(x)y = f(x) is a particular solution plus any combination of two independent solutions of the homogeneous equation; independence is tested by the Wronskian W = y₁y₂' − y₁'y₂, which obeys Abel's formula. With constant coefficients, trying e^{λx} gives the characteristic equation: distinct real roots, a repeated root (with an extra factor x), or complex roots (oscillation). The damped oscillator is underdamped, critically damped or overdamped accordingly. A sinusoidal drive gives a steady-state amplitude that peaks near resonance, with a phase lag. Particular solutions come from undetermined coefficients, from variation of parameters, or from a Green's function that solves the equation for a point source. Worked examples: the three root cases, variation of parameters for sec t, a numerically integrated driven oscillator against the resonance formula, and a Green's function solution.
status: in-progress
kind: theory
level: introductory
tags: [second-order-ode, linear-ode, wronskian, abel-formula, characteristic-equation, damped-oscillator, driven-oscillator, resonance, undetermined-coefficients, variation-of-parameters, green-function, boundary-value-problem]
prerequisites: [first-order-differential-equations, complex-numbers]
related: [partial-differential-equations-and-separation-of-variables, series-solutions-and-the-frobenius-method, sturm-liouville-theory, harmonic-oscillator-analytic-solution, kramers-kronig-debye-and-lorentz-models]
key: amp
order: 20
date: 2026-11-25
---

$y'' + p(x)y' + q(x)y = f(x)$ is the standard form (leading coefficient divided out). For the oscillator, $t$ is time, $\omega_0$ the natural frequency and $\gamma$ the damping rate, with the equation $\ddot y + 2\gamma\dot y + \omega_0^2y = F_0\cos\omega t$.

## General theory

**Superposition.** Solutions of the homogeneous equation ($f = 0$) form a two-dimensional vector space. If $y_1$ and $y_2$ are linearly independent solutions, every solution is $c_1y_1 + c_2y_2$. The nonhomogeneous equation has general solution

$$
y = y_p + c_1y_1 + c_2y_2 ,
$$

with $y_p$ any one particular solution: two solutions of the full equation differ by a homogeneous solution.

**The Wronskian.** $W(y_1, y_2) = y_1y_2' - y_1'y_2$. If $W\ne0$ at a point, the solutions are independent (Arfken Sec. 9.6). For two solutions of the same equation, Abel's formula gives

$$
W(x) = W(x_0)\exp\Big(-\int_{x_0}^xp(t)\,dt\Big),
$$

so $W$ is either never zero or always zero. Abel's formula also gives a second solution from a first one, $y_2 = y_1\int W/y_1^2\,dx$ (Arfken Sec. 9.6).

**Initial and boundary conditions.** An initial value problem fixes $y$ and $y'$ at one point; its solution is unique. A boundary value problem fixes conditions at two points, such as $y(0) = y(L) = 0$. It may have no solution, one, or infinitely many. In the homogeneous case it has nonzero solutions only for special parameter values: the eigenvalue problems of [[sturm-liouville-theory]], where energy quantization comes from.

## Constant coefficients

**The characteristic equation.** For $ay'' + by' + cy = 0$, try $y = e^{\lambda x}$: $a\lambda^2 + b\lambda + c = 0$.

| roots | solutions |
|---|---|
| real, distinct $\lambda_1\ne\lambda_2$ | $e^{\lambda_1x}$, $e^{\lambda_2x}$ |
| repeated $\lambda$ | $e^{\lambda x}$, $x\,e^{\lambda x}$ |
| complex $\alpha\pm i\beta$ | $e^{\alpha x}\cos\beta x$, $e^{\alpha x}\sin\beta x$ |

The real forms in the last row are combinations of $e^{(\alpha\pm i\beta)x}$, by Euler's formula ([[complex-numbers]]). The same method works for any order: an $n$-th order equation gives a degree-$n$ polynomial.

**The damped oscillator.** For $\ddot y + 2\gamma\dot y + \omega_0^2y = 0$, the roots are $\lambda = -\gamma\pm\sqrt{\gamma^2 - \omega_0^2}$:

- **underdamped** ($\gamma < \omega_0$): $y = e^{-\gamma t}(A\cos\omega_dt + B\sin\omega_dt)$ with $\omega_d = \sqrt{\omega_0^2 - \gamma^2}$;
- **critically damped** ($\gamma = \omega_0$): $(A + Bt)e^{-\gamma t}$, the fastest return without oscillation;
- **overdamped** ($\gamma > \omega_0$): two decaying exponentials.

## Particular solutions

**Undetermined coefficients.** For constant coefficients and a forcing that is a polynomial, exponential, sine or cosine (or products of these), guess $y_p$ of the same form with unknown coefficients. If the guess solves the homogeneous equation, multiply it by $x$.

**The driven oscillator.** With $F_0\cos\omega t$, write the force as $\mathrm{Re}\,F_0e^{-i\omega t}$ and try $y_p = \mathrm{Re}\,Ae^{-i\omega t}$:

$$
A(\omega) = \frac{F_0}{\omega_0^2 - \omega^2 - 2i\gamma\omega},\qquad |A| = \frac{F_0}{\sqrt{(\omega_0^2 - \omega^2)^2 + 4\gamma^2\omega^2}},\qquad \tan\delta = \frac{2\gamma\omega}{\omega_0^2 - \omega^2}.
\label{amp}
$$

The homogeneous part decays as $e^{-\gamma t}$, leaving the steady state. The amplitude peaks at $\omega = \sqrt{\omega_0^2 - 2\gamma^2}$, and the response lags the drive by $\delta$, which passes through $\pi/2$ at $\omega_0$.

**Response functions.** $A(\omega)/F_0$ is a response function. It has poles at $\omega = -i\gamma\pm\omega_d$ in the lower half plane, which is what causality requires. Its real and imaginary parts are a Kramers–Kronig pair. The Lorentz model of the permittivity is a sum of such oscillators ([[kramers-kronig-debye-and-lorentz-models]]).

**Variation of parameters.** For any $p$, $q$ and $f$, look for $y_p = u_1y_1 + u_2y_2$ with $u_1'y_1 + u_2'y_2 = 0$. Then

$$
u_1' = -\frac{y_2f}{W},\qquad u_2' = \frac{y_1f}{W} .
$$

It needs no guess, only the homogeneous solutions.

## Green's functions

**Definition.** The Green's function $G(x, s)$ solves the equation with a point source and the homogeneous boundary conditions: $\mathcal LG(x, s) = \delta(x - s)$. Superposing point sources then solves the equation for any source (Arfken Sec. 9.7):

$$
y(x) = \int G(x, s)\,f(s)\,ds .
$$

**Construction.** For $y'' = f$ on $[0, 1]$ with $y(0) = y(1) = 0$: $G$ is linear on each side of $s$, vanishes at the ends, is continuous at $x = s$, and its slope jumps by 1 there. That gives

$$
G(x, s) = \begin{cases}x(s - 1),& x < s\\ s(x - 1),& x > s.\end{cases}
$$

The same construction with the Laplacian gives $1/(4\pi|\mathbf r - \mathbf r'|)$ ([[vector-identities-and-the-laplacian]]). For the Schrödinger equation it gives the resolvent ([[neumann-series-and-operator-expansions]]).

## Worked examples

!!! example "Root cases, sec t, resonance and a Green's function (computed for this note)"
    **Characteristic roots** (sympy `dsolve`):

    - $y'' + 3y' + 2y = 0$: roots $-1, -2$, so $y = C_1e^{-t} + C_2e^{-2t}$. Its Wronskian is $-e^{-3t}$, never zero.
    - $y'' + 2y' + y = 0$: repeated root $-1$, so $y = (C_1 + C_2t)e^{-t}$.
    - $\cos t$, $\sin t$ have Wronskian 1.

    **Variation of parameters.** $y'' + y = \sec t$ with $y_1 = \cos t$, $y_2 = \sin t$, $W = 1$: $u_1' = -\tan t$ and $u_2' = 1$. So $y_p = \cos t\ln\cos t + t\sin t$, and sympy returns $(C_1 + t)\sin t + (C_2 + \ln\cos t)\cos t$. Undetermined coefficients cannot handle $\sec t$.

    **Driven oscillator.** $\omega_0 = 1$, $\gamma = 0.1$, drive $\cos1.2t$, integrated numerically from rest to $t = 300$. The amplitude after the transient ($t > 250$) is 1.99522. Eq. [[#amp]] gives $1/\sqrt{(1 - 1.44)^2 + 4(0.01)(1.44)} = 1.99522$. The peak would be at $\omega = \sqrt{1 - 0.02} = 0.990$.

    **Green's function.** $y'' = 1$, $y(0) = y(1) = 0$: $\int_0^1G(0.3, s)\,ds = -0.105$, equal to the exact solution $x(x - 1)/2$ at $x = 0.3$.

## Source

Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005), Sec. 9.6 (a second solution, the Wronskian, linear independence), Sec. 9.7 (nonhomogeneous equations, Green's function). The characteristic equation, undetermined coefficients, variation of parameters and the driven oscillator are standard material, written for this note. Calculations in `Claude outputs/part0_math_batchE.py`, section E.
