---
id: laurent-series-singularities-and-residues
title: Laurent series, singularities and residues - expansion in an annulus, poles, essential singularities and branch points, the residue theorem, real integrals by contour integration, Jordan's lemma, principal values and the Sokhotski-Plemelj formula
summary: Around an isolated singularity an analytic function has a Laurent expansion in positive and negative powers of (z − z₀). The negative powers classify the singularity: none (removable), finitely many (a pole), infinitely many (an essential singularity). Branch points are not isolated singularities and need cuts. The coefficient a₋₁ is the residue, and the residue theorem says ∮ f dz = 2πi Σ residues inside. Closing the contour in the upper half plane turns many real integrals into residue sums; Jordan's lemma makes the arc vanish for e^{ikx} integrands, and indenting around a pole on the axis gives a principal value. The Sokhotski–Plemelj formula, 1/(x − x₀ ∓ iη) → P(1/(x − x₀)) ± iπδ(x − x₀), is the source of the Kramers–Kronig relations and of damped response functions. Worked examples: Laurent series in two annuli, four residues, three real integrals, and Sokhotski–Plemelj checked numerically.
status: in-progress
kind: theory
level: intermediate
tags: [laurent-series, singularity, pole, essential-singularity, branch-point, residue, residue-theorem, contour-integration, jordan-lemma, principal-value, sokhotski-plemelj, dispersion-relation]
prerequisites: [analytic-functions-and-cauchy-theorem]
related: [kramers-kronig-debye-and-lorentz-models, damped-response-and-absorption-cross-sections, power-series-and-radius-of-convergence, integral-calculus, fourier-transforms-and-the-dirac-delta, one-particle-greens-function]
key: residuethm
order: 30
date: 2026-11-25
---

Contours are counterclockwise. $P\int$ is the Cauchy principal value. $\eta\to0^+$ is a positive infinitesimal.

## The Laurent expansion

**Statement.** If $f$ is analytic in the annulus $r_1 < |z - z_0| < r_2$, then there (Arfken Sec. 6.5)

$$
f(z) = \sum_{n=-\infty}^{\infty}a_n(z - z_0)^n,\qquad a_n = \frac1{2\pi i}\oint\frac{f(z')}{(z' - z_0)^{n+1}}dz' ,
\label{laurent}
$$

with the contour any circle inside the annulus.

**Proof idea.** Apply Cauchy's formula to the region between two circles. Expand $1/(z' - z)$ as a geometric series in $(z - z_0)/(z' - z_0)$ on the outer circle (giving positive powers) and in $(z' - z_0)/(z - z_0)$ on the inner one (giving negative powers).

**Properties.**

- **No singularity inside.** If $f$ is analytic for $|z - z_0| < r_2$, all $a_n$ with $n < 0$ vanish and Eq. [[#laurent]] is the Taylor series.
- **Uniqueness.** The expansion is unique for a given annulus. Different annuli of the same function give different series, as the example below shows.
- **In practice.** Laurent series are rarely found from the integral. One uses known Taylor series instead, e.g. $e^{1/z} = \sum_{n\ge0}z^{-n}/n!$.

## Classification of singularities

**Isolated singularities.** $f$ is analytic in a punctured disc $0 < |z - z_0| < r$. Then (Arfken Sec. 6.6):

| type | Laurent series | example at $z_0 = 0$ | behaviour |
|---|---|---|---|
| removable | no negative powers | $\sin z/z$ | bounded; redefine $f(z_0)$ |
| pole of order $m$ | lowest power $(z - z_0)^{-m}$ | $1/z^2$ ($m = 2$) | $|f|\to\infty$ like $|z - z_0|^{-m}$ |
| essential | infinitely many negative powers | $e^{1/z}$ | takes nearly every value near $z_0$ (Picard) |

A function whose only singularities are poles is meromorphic. Response functions and Green's functions are meromorphic in the frequency, with poles at excitation energies.

**Branch points.** $\sqrt z$ and $\log z$ do not return to their value around a circle about 0. No Laurent series exists in any punctured disc there. One cuts the plane along a curve from the branch point (usually to infinity) and works on one branch ([[complex-numbers]]). Contour integrals must not cross the cut; integrals around cuts (keyhole contours) evaluate $\int_0^\infty x^{a-1}R(x)\,dx$.

**Singularities at infinity.** The behaviour at $z = \infty$ is that of $f(1/w)$ at $w = 0$. A polynomial of degree $n$ has a pole of order $n$ at infinity.

## Residues

**Definition.** The residue of $f$ at an isolated singularity is the coefficient $a_{-1}$ of its Laurent series. By Eq. [[analytic-functions-and-cauchy-theorem#zn]] it is the only coefficient that survives integration around $z_0$:

$$
\mathrm{Res}_{z_0}f = a_{-1} = \frac1{2\pi i}\oint f\,dz .
$$

**Computing residues.**

- **Simple pole.** $\mathrm{Res}_{z_0}f = \lim_{z\to z_0}(z - z_0)f(z)$. For $f = g/h$ with $h(z_0) = 0$, $h'(z_0)\ne0$: $g(z_0)/h'(z_0)$.
- **Pole of order $m$.** $\mathrm{Res}_{z_0}f = \frac1{(m - 1)!}\lim_{z\to z_0}\frac{d^{m-1}}{dz^{m-1}}\big[(z - z_0)^mf(z)\big]$.
- **Essential singularity.** Read $a_{-1}$ off the Laurent series.

**The residue theorem.** If $f$ is analytic on and inside $C$ except at isolated singularities $z_k$ inside (Arfken Sec. 7.1):

$$
\oint_Cf(z)\,dz = 2\pi i\sum_k\mathrm{Res}_{z_k}f .
\label{residuethm}
$$

It follows by deforming $C$ into small circles around each singularity ([[analytic-functions-and-cauchy-theorem]]).

## Real integrals by residues

**Rational functions.** For $\int_{-\infty}^\infty R(x)\,dx$ with $R = p/q$ and $\deg q\ge\deg p + 2$, close the contour with a large semicircle in the upper half plane. The arc vanishes like $1/R$, so the integral is $2\pi i\sum$(residues in the upper half plane).

**Trigonometric integrals.** For $\int_0^{2\pi}F(\cos\theta,\sin\theta)\,d\theta$, put $z = e^{i\theta}$, $\cos\theta = (z + z^{-1})/2$, $d\theta = dz/(iz)$. This gives a contour integral around the unit circle.

**Fourier-type integrals and Jordan's lemma.** For $\int_{-\infty}^\infty g(x)e^{ikx}dx$ with $k > 0$ and $g\to0$ at infinity, close in the upper half plane: $|e^{ikz}| = e^{-k\,\mathrm{Im}\,z}$ decays there. Jordan's lemma guarantees that the arc contributes nothing even when $g$ decays only like $1/|z|$. For $k < 0$, close below; the sign of the frequency decides the half plane. This is how causality becomes analyticity: a response vanishing for $t < 0$ has a Fourier transform analytic in the upper half of the frequency plane.

**Poles on the real axis.** Indent the contour around the pole with a small semicircle of radius $\varepsilon$. A semicircle around a simple pole contributes $\pm i\pi$ times its residue, half of a full circle. The remaining integral is a principal value. This gives $\int_0^\infty\frac{\sin x}xdx = \frac\pi2$ from $e^{iz}/z$.

## Principal values and the Sokhotski–Plemelj formula

**Statement.** For a smooth $f$ decaying at infinity,

$$
\lim_{\eta\to0^+}\int\frac{f(x)}{x - x_0\mp i\eta}dx = P\!\int\frac{f(x)}{x - x_0}dx \pm i\pi f(x_0),\qquad
\frac1{x - x_0\mp i\eta}\to P\frac1{x - x_0}\pm i\pi\delta(x - x_0).
\label{sp}
$$

**Proof.** Split $\frac1{x - x_0\mp i\eta} = \frac{x - x_0}{(x - x_0)^2 + \eta^2}\pm\frac{i\eta}{(x - x_0)^2 + \eta^2}$. The first part tends to the principal value; the second is $\pm i\pi$ times a Lorentzian of width $\eta$, a nascent delta function ([[fourier-transforms-and-the-dirac-delta]]).

**Where it appears.**

- **Response functions.** $\omega\to\omega + i\eta$ in a sum-over-states response function gives dispersion (the principal value) and absorption (the delta function, broadened to a Lorentzian at finite $\eta$) ([[damped-response-and-absorption-cross-sections]]).
- **Kramers–Kronig relations.** Applying Eq. [[#residuethm]] to a function analytic in the upper half plane, with a pole indented on the real axis, gives the Kramers–Kronig relations between real and imaginary parts (Arfken Sec. 7.2; [[kramers-kronig-debye-and-lorentz-models]]).
- **Green's functions.** The retarded and advanced Green's functions $(E - H\pm i\eta)^{-1}$ differ by the sign in Eq. [[#sp]] ([[one-particle-greens-function]]).

## Worked examples

!!! example "Laurent series, residues and three real integrals (computed for this note)"
    **Two Laurent series of one function.** $f = \frac1{z(z - 1)}$ has poles at 0 and 1.

    - In $0 < |z| < 1$: $f = -\frac1z\cdot\frac1{1 - z} = -\frac1z - 1 - z - z^2 - \cdots$, residue $-1$ at 0.
    - In $|z| > 1$: $f = \frac1{z^2}\cdot\frac1{1 - 1/z} = z^{-2} + z^{-3} + \cdots$, no $z^{-1}$ term. The sum of the residues at 0 and 1 is $-1 + 1 = 0$, so a large circle encloses zero total residue.

    **Residues** (sympy):

    - $1/(z^2 + 1)$ at $i$: $-i/2$;
    - $e^z/z^3$ at 0: $\tfrac12$;
    - $\cot z$ at 0: 1;
    - $1/\sin^2z$ at 0: 0 (a double pole with an even Laurent series).

    **Real integrals.**

    | integral | by residues | quadrature |
    |---|---|---|
    | $\int_{-\infty}^\infty\frac{\cos x}{x^2 + a^2}dx$, $a = 1.5$ | $\pi e^{-a}/a = 0.46732271$ | 0.46732271 |
    | $\int_0^\infty\frac{dx}{1 + x^4}$ | $\pi/(2\sqrt2) = 1.11072073$ | 1.11072073 |
    | $\int_0^{2\pi}\frac{d\theta}{2 + \cos\theta}$ | $2\pi/\sqrt3 = 3.62759873$ | 3.62759873 |

    For the first, the only pole in the upper half plane of $e^{iz}/(z^2 + a^2)$ is $ia$, with residue $e^{-a}/(2ia)$. For the third, $z = e^{i\theta}$ turns the integrand into $2/[i(z^2 + 4z + 1)]$, whose pole inside the unit circle is $z = -2 + \sqrt3$.

    **Sokhotski–Plemelj.** With $f = e^{-x^2}$ and $x_0 = 0.4$:

    - The Lorentzian part $\int f\,\eta/[(x - x_0)^2 + \eta^2]$ is 2.4419, 2.6520 and 2.6746 for $\eta = 0.1$, 0.01 and 0.001. It tends to $\pi f(x_0) = 2.6771$.
    - The principal value $P\int e^{-x^2}/(x - 0.4)\,dx = -1.275966$, which equals $-2\sqrt\pi\,F(0.4)$ with $F$ Dawson's integral.

## Source

Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005), Sec. 6.5 (Laurent expansion), Sec. 6.6 (singularities: poles, essential singularities, branch points and cuts), Sec. 7.1 (calculus of residues: the residue theorem, evaluation of definite integrals, Jordan's lemma, principal values, and moving poles off the axis by $\sigma\to\sigma + i\gamma$), Sec. 7.2 (dispersion relations, Kramers–Kronig). The Sokhotski–Plemelj formula as stated here, the Dawson-integral identity and the response-function remarks are general knowledge, not taken from Arfken. Calculations in `Claude outputs/part0_math_batchE.py`, section D.
