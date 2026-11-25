---
id: functions
title: Functions - domain, range, composition and inverses, parity, periodicity, and the elementary functions
summary: A function assigns to every element of its domain exactly one value. This note fixes the vocabulary used throughout the notebook. It covers domain and range; injective, surjective and bijective maps; composition and inverses (restricting the domain to make an inverse exist); and even, odd and periodic functions, with the even–odd decomposition. It then surveys the elementary functions (polynomials, rational functions, exponential and logarithm, trigonometric and hyperbolic functions and their inverses) and functions of several variables. Worked example: inverse functions, principal branches and the parity decomposition of e^x.
status: in-progress
kind: theory
level: introductory
tags: [function, domain, range, inverse-function, composition, even-function, odd-function, periodic-function, elementary-functions, exponential, logarithm, hyperbolic-functions]
prerequisites: []
related: [limits-and-continuity, differential-calculus, complex-numbers, power-series-and-radius-of-convergence]
order: 10
date: 2026-11-25
---

Real variables unless stated otherwise. $\mathbb R$ is the real line; $f: A\to B$ means $f$ takes values in $B$ for arguments in $A$.

## Definition and vocabulary

**Function.** A function $f: A\to B$ assigns to each $x$ in the **domain** $A$ exactly one value $f(x)\in B$. The **range** (image) is $f(A) = \{f(x): x\in A\}\subseteq B$. A formula alone does not define a function; the domain is part of the definition. $f(x) = \sqrt x$ has domain $[0,\infty)$ over the reals.

**Graph.** The set of pairs $(x, f(x))$. A curve in the plane is the graph of a function of $x$ exactly when every vertical line meets it at most once. The circle $x^2 + y^2 = 1$ is not; it is the union of the graphs of $\pm\sqrt{1 - x^2}$.

**Injective, surjective, bijective.**

- **Injective** (one-to-one): $f(x_1) = f(x_2)\Rightarrow x_1 = x_2$.
- **Surjective** (onto): $f(A) = B$.
- **Bijective**: both. Exactly the bijections have an inverse $f^{-1}: B\to A$ with $f^{-1}(f(x)) = x$ and $f(f^{-1}(y)) = y$.

A strictly monotonic function on an interval is injective, so it has an inverse on its range. The graph of $f^{-1}$ is the reflection of the graph of $f$ in the line $y = x$.

**Composition.** $(g\circ f)(x) = g(f(x))$, defined where $f(x)$ lies in the domain of $g$. Composition is associative but not commutative: $\sin(x^2)\ne\sin^2x$. The inverse of a composition reverses the order, $(g\circ f)^{-1} = f^{-1}\circ g^{-1}$, as for matrices.

## Symmetry: parity and periodicity

**Parity.** $f$ is **even** if $f(-x) = f(x)$ and **odd** if $f(-x) = -f(x)$, on a domain symmetric about 0. Every such $f$ splits uniquely into an even and an odd part:

$$
f(x) = \underbrace{\tfrac12[f(x) + f(-x)]}_{f_{\rm e}} + \underbrace{\tfrac12[f(x) - f(-x)]}_{f_{\rm o}}.
\label{evenodd}
$$

- **Products.** even × even and odd × odd are even; even × odd is odd.
- **Integrals.** $\int_{-a}^af_{\rm o}\,dx = 0$ and $\int_{-a}^af_{\rm e}\,dx = 2\int_0^af_{\rm e}\,dx$.

This is the one-dimensional form of the parity selection rules used throughout quantum mechanics: an integral over all space of an odd integrand vanishes.

**Periodicity.** $f$ is periodic with period $T$ if $f(x + T) = f(x)$ for all $x$; the smallest such $T > 0$ is the fundamental period. $\sin$ and $\cos$ have period $2\pi$, $\tan$ has $\pi$. Periodic functions are what Fourier series expand ([[fourier-series]]).

**Bounded and monotonic.** $f$ is bounded if $|f(x)|\le M$ on its domain. It is increasing if $x_1 < x_2\Rightarrow f(x_1)\le f(x_2)$, strictly increasing with $<$.

## The elementary functions

**Polynomials** $p(x) = \sum_{k=0}^na_kx^k$ of degree $n$ (with $a_n\ne0$). A real polynomial of degree $n$ has exactly $n$ complex roots counted with multiplicity (fundamental theorem of algebra), and complex roots come in conjugate pairs. **Rational functions** $p(x)/q(x)$ are defined except at the roots of $q$, and are integrated by partial fractions ([[integral-calculus]]).

**Exponential and logarithm.** $e^x$ maps $\mathbb R$ bijectively onto $(0,\infty)$, with $e^{a + b} = e^ae^b$. Its inverse is the natural logarithm $\ln: (0,\infty)\to\mathbb R$, with $\ln(ab) = \ln a + \ln b$. General powers are defined through them: $a^x = e^{x\ln a}$ for $a > 0$.

**Trigonometric functions.** $\sin$, $\cos$, $\tan = \sin/\cos$ and their reciprocals. They are not injective, so each inverse is defined on a restricted principal branch:

| function | restricted to | inverse | range of the inverse |
|---|---|---|---|
| $\sin x$ | $[-\pi/2, \pi/2]$ | $\arcsin y$, $y\in[-1, 1]$ | $[-\pi/2, \pi/2]$ |
| $\cos x$ | $[0, \pi]$ | $\arccos y$, $y\in[-1, 1]$ | $[0, \pi]$ |
| $\tan x$ | $(-\pi/2, \pi/2)$ | $\arctan y$, $y\in\mathbb R$ | $(-\pi/2, \pi/2)$ |

Two traps follow. $\arcsin(\sin x) = x$ only for $x\in[-\pi/2,\pi/2]$; $\arcsin(\sin 2) = \pi - 2$. And the polar angle of a point $(x, y)$ is not $\arctan(y/x)$ in general, because that loses the quadrant; numerical codes use the two-argument $\mathrm{atan2}(y, x)\in(-\pi,\pi]$.

**Hyperbolic functions.** $\cosh x = \tfrac12(e^x + e^{-x})$ and $\sinh x = \tfrac12(e^x - e^{-x})$ are the even and odd parts of $e^x$ (Eq. [[#evenodd]]). They satisfy $\cosh^2x - \sinh^2x = 1$. Their inverses are logarithms, for example $\operatorname{arsinh}y = \ln(y + \sqrt{y^2 + 1})$. Through $e^{ix} = \cos x + i\sin x$ ([[complex-numbers]]) they are the trigonometric functions of an imaginary argument: $\cosh x = \cos(ix)$.

## Functions of several variables

**Definition.** $f:\mathbb R^n\to\mathbb R$ assigns a number to each point $\mathbf x = (x_1,\dots,x_n)$: a scalar field when $n = 3$ ([[scalar-and-vector-fields-and-the-gradient]]). A potential energy surface $E(\mathbf R)$ is a function of $3N$ nuclear coordinates. A map $\mathbf f:\mathbb R^n\to\mathbb R^m$ has $m$ component functions; a vector field is the case $n = m = 3$.

**Level sets.** The set where $f(\mathbf x) = c$ is a level curve ($n = 2$) or surface ($n = 3$): contour lines, isodensity surfaces of an orbital.

**Separable functions.** $f(x, y) = g(x)h(y)$. Products like this are what separation of variables looks for ([[partial-differential-equations-and-separation-of-variables]]), and what makes a Gaussian $e^{-a(x^2 + y^2 + z^2)}$ factorize into three one-dimensional integrals.

## Worked example

!!! example "Inverses, branches and parity (computed for this note)"
    **An inverse by restriction.** $f(x) = x^2 - 4x + 7 = (x - 2)^2 + 3$ is not injective on $\mathbb R$. Restricted to $[2,\infty)$ it is strictly increasing with range $[3,\infty)$, and solving $y = (x - 2)^2 + 3$ for $x\ge2$ gives $f^{-1}(y) = 2 + \sqrt{y - 3}$. On $(-\infty, 2]$ the inverse is $2 - \sqrt{y - 3}$ instead. Both branches are correct; the domain decides.

    **A principal branch.** $\arcsin(\sin2) = \pi - 2 = 1.1416$, not 2, because 2 lies outside $[-\pi/2,\pi/2] = [-1.5708, 1.5708]$ and $\sin(\pi - 2) = \sin2$.

    **Parity of $e^x$.** Eq. [[#evenodd]] gives $f_{\rm e} = \cosh x$ and $f_{\rm o} = \sinh x$. So $\int_{-1}^1e^x\,dx = 2\int_0^1\cosh x\,dx = 2\sinh1 = 2.3504$, which equals $e - e^{-1}$ as it must.

    **Composition order.** With $f(x) = x + 1$ and $g(x) = x^2$: $(g\circ f)(x) = (x + 1)^2$ but $(f\circ g)(x) = x^2 + 1$. At $x = 2$ these are 9 and 5.

## Source

The vocabulary and the elementary functions are standard; Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005), Sec. 6.1 treats the elementary functions of a complex argument. The numbers are elementary arithmetic.
