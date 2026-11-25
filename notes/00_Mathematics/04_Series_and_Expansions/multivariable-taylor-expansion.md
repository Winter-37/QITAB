---
id: multivariable-taylor-expansion
title: Taylor expansion in several variables - gradient and Hessian, the operator form exp(a·∇), quadratic models, Newton steps, normal coordinates, and the expansion of 1/|r − a|
summary: For a function of several variables, f(x + a) = Σₙ (a·∇)ⁿ f/n! = e^{a·∇} f(x). To second order this is f + gᵀa + ½aᵀHa, with g the gradient and H the symmetric Hessian. This quadratic model is the basis of geometry optimization (the Newton step a = −H⁻¹g), of harmonic vibrational analysis (diagonalizing the mass-weighted Hessian gives normal coordinates), and of second-order SCF and orbital optimization. Expanding 1/|r − a| in a gives the monopole, dipole and quadrupole terms of the multipole expansion. Worked examples: linear and quadratic models of a 2D function, Newton iterations that converge quadratically to a saddle point rather than the minimum, and the first three orders of 1/|r − a|.
status: in-progress
kind: theory
level: intermediate
tags: [multivariable-taylor, gradient, hessian, quadratic-model, newton-step, normal-coordinates, potential-energy-surface, multipole-expansion, operator-exponential]
prerequisites: [taylor-and-maclaurin-expansions, scalar-and-vector-fields-and-the-gradient]
related: [differential-calculus, harmonic-vibrational-analysis, newton-and-broyden-methods-for-nonlinear-equations, electric-and-magnetic-multipole-moments, eigenfunction-expansions-and-generating-functions]
key: quad
order: 40
date: 2026-11-25
---

$\mathbf x\in\mathbb R^n$, $\mathbf g = \nabla f$ the gradient, $H_{ij} = \partial_i\partial_jf$ the Hessian, both at the expansion point. Repeated indices are summed.

## The expansion

**Derivation.** Restrict $f$ to the line $\mathbf x + t\mathbf a$ and apply the one-variable Taylor theorem in $t$ ([[taylor-and-maclaurin-expansions]]). By the chain rule $\frac{d}{dt} = \mathbf a\cdot\nabla$, so at $t = 1$

$$
f(\mathbf x + \mathbf a) = \sum_{n=0}^\infty\frac1{n!}(\mathbf a\cdot\nabla)^nf(\mathbf x) = e^{\mathbf a\cdot\nabla}f(\mathbf x)
\label{exp}
$$

(Arfken Sec. 5.6, for two and three variables). The exponential form is the three-dimensional translation operator $e^{-i\mathbf a\cdot\hat{\mathbf p}/\hbar}$.

**To second order.**

$$
f(\mathbf x + \mathbf a) = f + g_ia_i + \tfrac12a_iH_{ij}a_j + \tfrac16a_ia_ja_k\,\partial_i\partial_j\partial_kf + O(|\mathbf a|^4)
= f + \mathbf g^{\rm T}\mathbf a + \tfrac12\mathbf a^{\rm T}\mathbf H\mathbf a + O(|\mathbf a|^3).
\label{quad}
$$

The Hessian is symmetric when the second derivatives are continuous ([[differential-calculus]]). The remainder can be written with all third derivatives evaluated at an intermediate point on the segment, as in one variable.

## Quadratic models

**Classification of stationary points.** At $\mathbf g = 0$, Eq. [[#quad]] is governed by the eigenvalues of $\mathbf H$. All positive means a minimum. One negative means a first-order saddle point (a transition state). The eigenvector of the negative eigenvalue is the direction of the reaction coordinate.

**The Newton step.** Minimizing the quadratic model over $\mathbf a$ gives

$$
\mathbf H\mathbf a = -\mathbf g\qquad\Rightarrow\qquad\mathbf a = -\mathbf H^{-1}\mathbf g .
\label{newton}
$$

Iterating converges quadratically near a stationary point: the error is roughly squared at each step. Newton's method does not prefer minima. It converges to whatever stationary point is nearby, and a step is downhill only when $\mathbf H$ is positive definite. Trust radii, line searches and Hessian updates (BFGS) make this robust ([[newton-and-broyden-methods-for-nonlinear-equations]]). Geometry optimizers, second-order SCF and MCSCF orbital optimizers all build Eq. [[#newton]] in their own variables.

**Normal coordinates.** For a molecule with nuclear masses $m_i$, the potential energy surface $E(\mathbf R)$ expanded about a minimum has kinetic energy $\tfrac12\sum m_i\dot R_i^2$ and potential $\tfrac12\Delta\mathbf R^{\rm T}\mathbf H\Delta\mathbf R$.

- **Mass weighting.** In the variables $q_i = \sqrt{m_i}\,\Delta R_i$, both forms become simple, and the potential has the mass-weighted Hessian $\mathbf H_{ij}/\sqrt{m_im_j}$.
- **Diagonalizing.** Its eigenvectors are the normal modes and its eigenvalues are $\omega_k^2$. Each normal coordinate is an independent harmonic oscillator ([[harmonic-vibrational-analysis]]).
- **Higher orders.** The cubic and quartic terms of Eq. [[#exp]] couple the modes (anharmonicity).

**Response properties.** The same expansion in field strengths, $E(\mathbf F) = E_0 - \mu_iF_i - \tfrac12\alpha_{ij}F_iF_j - \cdots$, defines dipole moments and polarizabilities as derivatives ([[polarizabilities-and-dispersion-coefficients]]).

## Expanding 1/|r − a|

**Setup.** For a source displaced by $\mathbf a$ from the origin and a field point $\mathbf r$ with $|\mathbf a| < r$, apply Eq. [[#exp]] to $f(\mathbf r) = 1/r$ with displacement $-\mathbf a$:

$$
\frac1{|\mathbf r - \mathbf a|} = \frac1r + \frac{\mathbf a\cdot\mathbf r}{r^3} + \frac{3(\mathbf a\cdot\mathbf r)^2 - a^2r^2}{2r^5} + O\Big(\frac{a^3}{r^4}\Big).
\label{multipole}
$$

**Multipoles.** The three terms are the monopole, dipole and quadrupole potentials. Summed over a charge distribution they give the multipole expansion of [[electric-and-magnetic-multipole-moments]]. With $\cos\gamma = \hat{\mathbf a}\cdot\hat{\mathbf r}$, the $n$-th term is $(a^n/r^{n+1})P_n(\cos\gamma)$. All orders at once come from the Legendre generating function ([[eigenfunction-expansions-and-generating-functions]]).

## Worked examples

!!! example "Quadratic model, Newton's method and the multipole series (computed for this note)"
    **Linear and quadratic models.** $f(x, y) = e^{x-1} + (y - 2)^2(1 + x^2) + \cos(xy)$ expanded at $(0.5, 1.5)$ with step $\mathbf a = (0.05, -0.03)$. Exact value 1.69408449. The linear model gives 1.69014774 (error $3.9\times10^{-3}$); adding $\tfrac12\mathbf a^{\rm T}\mathbf H\mathbf a$ gives 1.69386132 (error $2.2\times10^{-4}$). Each order gains roughly a factor $|\mathbf a|$.

    **Newton iterations** (Eq. [[#newton]]) from $(0.5, 1.5)$:

    | iteration | $(x, y)$ | $|\nabla f|$ |
    |---:|---|---:|
    | 1 | $(-0.132, 1.578)$ | 1.07 |
    | 2 | $(0.317, 1.876)$ | 0.70 |
    | 3 | $(0.059, 1.941)$ | 0.21 |
    | 4 | $(0.1046, 2.0089)$ | $1.1\times10^{-2}$ |
    | 5 | $(0.1015, 2.0102)$ | $3.1\times10^{-5}$ |

    The last two steps show quadratic convergence, with $|\nabla f|$ roughly squared. But the point reached is not a minimum. The Hessian there has eigenvalues $(-3.578, 2.039)$: it is a first-order saddle with $f = 1.38654$, higher than the value 1.35012 at step 2. The true minimum, found by BFGS, is at $(1.1774, 2.1430)$ with $f = 0.42811$ and Hessian eigenvalues $(3.241, 7.639)$.

    Eq. [[#newton]] looks for a zero of the gradient, and every stationary point is one. Started where $\mathbf H$ is indefinite, it can be attracted to a saddle. This is why minimizers check the Hessian, shift its negative eigenvalues or use a trust region, and why transition-state searches deliberately follow one negative eigenvalue.

    **$1/|\mathbf r - \mathbf a|$.** For $\mathbf r = (1, 2, 2)$ ($r = 3$) and $\mathbf a = (0.3, -0.1, 0.2)$: exact 0.35049982. Through orders 0, 1, 2 of Eq. [[#multipole]]: 0.33333333, 0.35185185, 0.35080247. Each order gains about a factor $a/r\approx0.12$.

## Source

Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005), Sec. 5.6 (Taylor expansion in more than one variable and the operator form), Sec. 12.1 (the generating function as the expansion of the potential of a displaced charge). Normal-coordinate and Newton-step remarks are standard. Calculations in `Claude outputs/part0_math_batchE.py`, section C.
