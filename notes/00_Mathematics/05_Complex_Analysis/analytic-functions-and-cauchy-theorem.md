---
id: analytic-functions-and-cauchy-theorem
title: Analytic functions and Cauchy's theorem - complex differentiability, the Cauchy-Riemann equations, harmonic functions, contour integrals, Cauchy's integral theorem and formula, and their consequences
summary: A function of a complex variable is analytic where its derivative exists, independent of the direction of approach. Writing f = u + iv, that requires the Cauchy–Riemann equations u_x = v_y, u_y = −v_x, which make u and v harmonic. Contour integrals of analytic functions around closed curves vanish (Cauchy's integral theorem), so integrals depend only on the endpoints and contours can be deformed freely through regions of analyticity. Cauchy's integral formula recovers f and all its derivatives inside a contour from its values on the boundary. Hence an analytic function is infinitely differentiable, equals its Taylor series in the largest disc free of singularities, and is constant if bounded on the whole plane (Liouville). Worked examples: Cauchy–Riemann checks, ∮ zⁿ dz, and Cauchy's formula evaluated numerically.
status: in-progress
kind: theory
level: intermediate
tags: [analytic-function, holomorphic, cauchy-riemann, harmonic-function, contour-integral, cauchy-integral-theorem, cauchy-integral-formula, liouville-theorem, morera-theorem, deformation-of-contours]
prerequisites: [complex-numbers, curl-and-stokes-theorem, power-series-and-radius-of-convergence]
related: [laurent-series-singularities-and-residues, vector-identities-and-the-laplacian, limits-and-continuity]
key: cauchyformula
order: 20
date: 2026-11-25
---

$z = x + iy$, $f(z) = u(x, y) + iv(x, y)$ with $u, v$ real. Contours are piecewise smooth closed curves traversed counterclockwise (positive sense) unless stated.

## Complex differentiability

**Definition.** $f$ is differentiable at $z_0$ if

$$
f'(z_0) = \lim_{\delta z\to0}\frac{f(z_0 + \delta z) - f(z_0)}{\delta z}
$$

exists and is the same for every direction in which $\delta z\to0$ in the plane. $f$ is **analytic** (holomorphic, regular) at $z_0$ if it is differentiable in a neighbourhood of $z_0$ (Arfken Sec. 6.2). The differentiation rules of real calculus carry over ([[differential-calculus]]). Polynomials, $e^z$, $\sin z$ and $\cos z$ are analytic everywhere (entire); rational functions are analytic except at the zeros of the denominator.

**Cauchy–Riemann equations.** Approach along the real axis ($\delta z = \delta x$) and along the imaginary axis ($\delta z = i\delta y$):

$$
f' = u_x + iv_x = -iu_y + v_y\qquad\Rightarrow\qquad u_x = v_y,\quad u_y = -v_x .
\label{cr}
$$

These are necessary. With continuous partial derivatives they are also sufficient.

**Non-analytic examples.** $f = z^* = x - iy$ has $u_x = 1\ne v_y = -1$, so it is nowhere analytic. $|z|^2$ satisfies Eq. [[#cr]] only at $z = 0$. In general, a function of $z$ alone is analytic and one that depends on $z^*$ is not. This is the starting point of Wirtinger derivatives for optimizing over complex orbitals, which treat $z$ and $z^*$ as independent.

**Harmonic functions.** Differentiating Eq. [[#cr]] gives $\nabla^2u = u_{xx} + u_{yy} = v_{yx} - v_{xy} = 0$, and likewise $\nabla^2v = 0$. The real and imaginary parts of an analytic function are harmonic conjugates. Their level curves cross at right angles. Two-dimensional electrostatics and potential flow are therefore complex analysis ([[vector-identities-and-the-laplacian]]); conformal mapping (Arfken Secs. 6.7–6.8) solves Laplace's equation by changing variables.

## Contour integrals

**Definition.** For a curve $C$ parametrized by $z(t)$, $\int_Cf(z)\,dz = \int f(z(t))\,z'(t)\,dt$. The basic estimate is $|\int_Cf\,dz|\le\max_C|f|\cdot\mathrm{length}(C)$.

**The key integral.** On the circle $|z - z_0| = R$:

$$
\oint(z - z_0)^n\,dz = \begin{cases}2\pi i,&n = -1\\0,&\text{every other integer }n.\end{cases}
\label{zn}
$$

For $n\ne-1$ the integrand has an antiderivative $(z - z_0)^{n+1}/(n + 1)$, which is single valued, so the closed integral vanishes. For $n = -1$ the antiderivative $\log(z - z_0)$ increases by $2\pi i$ around the circle.

## Cauchy's integral theorem

**Statement.** If $f$ is analytic on and inside a closed contour $C$ in a simply connected region (Arfken Sec. 6.3),

$$
\oint_Cf(z)\,dz = 0 .
$$

**Proof idea.** Write $f\,dz = (u + iv)(dx + i\,dy)$ and apply Stokes's theorem in the plane ([[curl-and-stokes-theorem]]). The real and imaginary parts of the resulting surface integrand are exactly the two Cauchy–Riemann combinations, which vanish.

**Consequences.**

- **Path independence.** $\int_{z_1}^{z_2}f\,dz$ is independent of the path within a region of analyticity, and $f$ has an antiderivative there.
- **Deformation.** A contour can be deformed freely, without changing the integral, as long as it does not cross a singularity. A contour around several singularities equals the sum of small circles around each. That reduces every closed integral to local information at the singularities ([[laurent-series-singularities-and-residues]]).
- **Morera's theorem.** The converse: if $f$ is continuous and $\oint f\,dz = 0$ around every closed curve, $f$ is analytic.

## Cauchy's integral formula

**Statement.** If $f$ is analytic on and inside $C$ and $z_0$ is inside (Arfken Sec. 6.4),

$$
f(z_0) = \frac1{2\pi i}\oint_C\frac{f(z)}{z - z_0}dz,\qquad f^{(n)}(z_0) = \frac{n!}{2\pi i}\oint_C\frac{f(z)}{(z - z_0)^{n+1}}dz .
\label{cauchyformula}
$$

**Proof idea.** Shrink $C$ to a small circle around $z_0$ (allowed by the theorem), where $f(z)\approx f(z_0)$, and use Eq. [[#zn]]. Differentiating under the integral gives the second formula.

**What follows.**

- **Infinitely differentiable.** An analytic function has derivatives of all orders. Real differentiable functions need not.
- **Taylor series.** Expanding $1/(z - z_0)$ in the formula as a geometric series shows that $f$ equals its Taylor series in the largest disc around $z_0$ free of singularities. Complex differentiability and analyticity in the power-series sense are the same thing. The radius of convergence is the distance to the nearest singularity ([[power-series-and-radius-of-convergence]]).
- **Mean value property.** $f(z_0)$ is the average of $f$ on any circle around $z_0$.
- **Maximum modulus.** $|f|$ has no interior maximum unless $f$ is constant.
- **Liouville's theorem.** A function analytic and bounded on the whole plane is constant. With it one proves the fundamental theorem of algebra: if a polynomial had no root, $1/p$ would be bounded and entire.
- **Identity theorem.** Two functions analytic in a region that agree on a segment agree everywhere. This makes analytic continuation unique: $\Gamma(z)$ and $\zeta(z)$ extend from their defining regions in exactly one way.

## Worked examples

!!! example "Cauchy–Riemann, the key integral and Cauchy's formula (computed for this note)"
    **Cauchy–Riemann** (sympy), reporting $u_x - v_y$, $u_y + v_x$ and $\nabla^2u$:

    | $f$ | $u_x - v_y$ | $u_y + v_x$ | $\nabla^2u$ |
    |---|---|---|---|
    | $z^3$ | 0 | 0 | 0 |
    | $e^z$ | 0 | 0 | 0 |
    | $z^*$ | 2 | 0 | 0 |
    | $|z|^2$ (taken as $u$, $v = 0$) | $2x$ | $2y$ | 4 |

    $z^*$ fails the first condition everywhere, though its real part $x$ is harmonic; $|z|^2$ satisfies Eq. [[#cr]] only at the origin.

    **Eq. [[#zn]] by quadrature.** On the unit circle with $2\times10^5$ points, $\oint z^n\,dz$ for $n = -3,\dots,2$ is zero to $10^{-10}$ except $n = -1$, which gives $6.2831853072i = 2\pi i$.

    **Cauchy's formula.** $\frac1{2\pi i}\oint\frac{\cos w}{w - 0.3}dw = 0.9553364891 = \cos0.3$. And $\oint e^z/z^3\,dz = 3.1415926536i$, which is $2\pi i\cdot f''(0)/2! = \pi i$ for $f = e^z$, from the second form of Eq. [[#cauchyformula]].

## Source

Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005), Sec. 6.2 (Cauchy–Riemann conditions, analytic functions, harmonic conjugates), Sec. 6.3 (Cauchy's integral theorem, by Stokes's theorem; multiply connected regions), Sec. 6.4 (Cauchy's integral formula, derivatives, Morera's theorem, Liouville's theorem), Secs. 6.7–6.8 (mapping). The Wirtinger-derivative remark is general knowledge. Calculations in `Claude outputs/part0_math_batchE.py`, section D.
