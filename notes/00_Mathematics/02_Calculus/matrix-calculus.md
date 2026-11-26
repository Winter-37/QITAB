---
id: matrix-calculus
title: Matrix calculus - differentials of traces, products, inverses, determinants, square roots and exponentials, derivatives of matrix functions, and gradients with respect to a matrix
summary: Matrix derivatives are easiest to get from differentials. Write d(f) to first order in a small change dX, using the product rule while keeping the order of noncommuting factors, then read off the gradient from d f = tr(Gᵀ dX). The rules used throughout analytic-derivative theory: d(X⁻¹) = −X⁻¹ dX X⁻¹, d det X = det X tr(X⁻¹ dX), d ln det X = tr(X⁻¹ dX), and ∂ tr(AXB)/∂X = AᵀBᵀ. The square root and S^{−1/2} have derivatives given by a Sylvester equation, solved elementwise in the eigenbasis of S. The exponential has d e^K = ∫₀¹ e^{sK} dK e^{(1−s)K} ds, which reduces to e^K dK only if K and dK commute. Every function of a symmetric matrix differentiates by divided differences of f at pairs of eigenvalues (Daleckii–Krein). Worked examples: all rules checked against finite differences, and a chain rule through Löwdin orthogonalization.
status: in-progress
kind: theory
level: intermediate
tags: [matrix-calculus, matrix-differential, derivative-of-inverse, jacobi-formula, log-determinant, matrix-square-root, lowdin-orthogonalization, sylvester-equation, matrix-exponential-derivative, daleckii-krein, divided-differences, trace-gradient]
prerequisites: [differential-calculus, functions-of-matrices]
related: [eigenvalue-and-eigenvector-derivatives, unitary-matrices-exponential-logarithm, baker-campbell-hausdorff, derivative-integrals-and-u-matrices, rhf-analytic-gradient, lagrange-multipliers-and-kkt-conditions, matrix-differentiation-identities]
key: inv
order: 50
date: 2026-11-26
---

$\mathbf X$, $\mathbf A$, $\mathbf B$ are square matrices (real unless stated); $d\mathbf X$ is an arbitrary small change and $d(\cdot)$ the first-order change it causes. $\mathbf S$ is symmetric positive definite with eigenvalues $s_i$ and eigenvectors in $\mathbf U$. A tilde marks a matrix in that eigenbasis, $\tilde{\mathbf M} = \mathbf U^{\rm T}\mathbf M\mathbf U$. The gradient of a scalar $f(\mathbf X)$ is the matrix $\partial f/\partial\mathbf X$ with elements $\partial f/\partial X_{ij}$.

The formulas are collected as a lookup table in [[matrix-differentiation-identities]] (Part 9).

## Differentials, not index-by-index derivatives

**The method.** The cleanest route to a matrix derivative is the differential. Expand $f(\mathbf X + d\mathbf X)$ to first order, using the ordinary product rule ([[differential-calculus]]) but never commuting factors:

$$
d(\mathbf{XY}) = d\mathbf X\,\mathbf Y + \mathbf X\,d\mathbf Y,\qquad d(\mathbf X^{\rm T}) = (d\mathbf X)^{\rm T},\qquad d\,\mathrm{tr}\,\mathbf X = \mathrm{tr}\,d\mathbf X .
$$

**Reading off a gradient.** For a scalar $f$, write the result as $df = \mathrm{tr}(\mathbf G^{\rm T}d\mathbf X) = \sum_{ij}G_{ij}dX_{ij}$. Then $\partial f/\partial\mathbf X = \mathbf G$. The cyclic property $\mathrm{tr}(\mathbf{ABC}) = \mathrm{tr}(\mathbf{CAB})$ is what brings $d\mathbf X$ to the end.

**Constraints on the change.** If $\mathbf X$ is constrained, the admissible $d\mathbf X$ are restricted, and $\mathbf G$ is defined only up to terms orthogonal to them:

- symmetric $\mathbf X$: use $d\mathbf X = d\mathbf X^{\rm T}$, and symmetrize $\mathbf G$;
- orthonormal columns: the tangent space of [[lagrange-multipliers-and-kkt-conditions]].

## Traces, inverses and determinants

**Traces of products.**

$$
d\,\mathrm{tr}(\mathbf{AXB}) = \mathrm{tr}(\mathbf{BA}\,d\mathbf X)\ \Rightarrow\ \frac{\partial\,\mathrm{tr}(\mathbf{AXB})}{\partial\mathbf X} = \mathbf A^{\rm T}\mathbf B^{\rm T},\qquad
\frac{\partial\,\mathrm{tr}(\mathbf X^{\rm T}\mathbf A\mathbf X)}{\partial\mathbf X} = (\mathbf A + \mathbf A^{\rm T})\mathbf X .
$$

The second is the matrix form of $d(x^{\rm T}Ax)$. With $\mathbf X = \mathbf C_{\rm occ}$ it gives the orbital gradient of a one-electron energy $\mathrm{tr}(\mathbf C^{\rm T}\mathbf h\mathbf C)$.

**The inverse.** Differentiate $\mathbf X\mathbf X^{-1} = \mathbf 1$: $d\mathbf X\,\mathbf X^{-1} + \mathbf X\,d(\mathbf X^{-1}) = 0$, so

$$
d(\mathbf X^{-1}) = -\mathbf X^{-1}\,d\mathbf X\,\mathbf X^{-1} .
\label{inv}
$$

This is the matrix version of $d(1/x) = -dx/x^2$, with the order kept. It is the first term of the Neumann expansion of $(\mathbf X + d\mathbf X)^{-1}$ ([[neumann-series-and-operator-expansions]]). In analytic-gradient theory it gives the derivative of $\mathbf S^{-1}$ and of a resolvent, and it is why the $\mathbf S^x$ terms carry two factors of the density.

**The determinant (Jacobi's formula).** Expanding $\det(\mathbf X + d\mathbf X) = \det\mathbf X\det(\mathbf 1 + \mathbf X^{-1}d\mathbf X)$ and using $\det(\mathbf 1 + \boldsymbol\epsilon) = 1 + \mathrm{tr}\,\boldsymbol\epsilon + O(\epsilon^2)$:

$$
d\det\mathbf X = \det\mathbf X\;\mathrm{tr}(\mathbf X^{-1}d\mathbf X),\qquad d\ln\det\mathbf X = \mathrm{tr}(\mathbf X^{-1}d\mathbf X),\qquad \frac{\partial\ln|\det\mathbf X|}{\partial\mathbf X} = \mathbf X^{-\rm T} .
\label{jacobi}
$$

Since $\ln\det = \mathrm{tr}\ln$ for positive definite matrices, the second form is also $d\,\mathrm{tr}\ln\mathbf S = \mathrm{tr}(\mathbf S^{-1}d\mathbf S)$. Uses:

- the derivative of an overlap determinant of two Slater determinants (nonorthogonal CI, overlaps along a path);
- log-likelihoods of Gaussian distributions in fitting;
- the Jacobian of a change of variables.

## Square roots and Löwdin orthogonalization

**The square root.** $\mathbf Y = \mathbf S^{1/2}$ satisfies $\mathbf Y\mathbf Y = \mathbf S$. Differentiating gives a **Sylvester equation** for $d\mathbf Y$:

$$
\mathbf Y\,d\mathbf Y + d\mathbf Y\,\mathbf Y = d\mathbf S .
$$

In the eigenbasis of $\mathbf S$, $\mathbf Y$ is diagonal, and the equation decouples element by element: $d\tilde Y_{ij} = d\tilde S_{ij}/(\sqrt{s_i} + \sqrt{s_j})$.

**The inverse square root.** For $\mathbf Y = \mathbf S^{-1/2}$, differentiate $\mathbf Y\mathbf S\mathbf Y = \mathbf 1$ the same way:

$$
d\tilde Y_{ij} = -\frac{d\tilde S_{ij}}{\sqrt{s_is_j}\,\big(\sqrt{s_i} + \sqrt{s_j}\big)} .
\label{lowdin}
$$

The diagonal element reduces to $-\tfrac12s_i^{-3/2}d\tilde S_{ii}$, the scalar rule. Small eigenvalues of $\mathbf S$ (near-linear dependence) enter with $s^{-3/2}$: the derivative of a Löwdin-orthogonalized basis is ill-conditioned exactly when the basis is ([[floating-point-and-numerical-error]]).

**Uses.** Löwdin-orthogonalized AOs, symmetric orthogonalization in DMET and other embedding schemes, and Löwdin population analysis all depend on $\mathbf S$, which depends on the nuclear positions. Their nuclear derivatives need Eq. [[#lowdin]] with $d\mathbf S = \mathbf S^x\,dx$ ([[derivative-integrals-and-u-matrices]]).

## Exponentials and general matrix functions

**The exponential.** $e^{\mathbf K}$ does not differentiate to $e^{\mathbf K}d\mathbf K$ unless $\mathbf K$ and $d\mathbf K$ commute. The general result follows from $\frac{d}{dt}e^{t\mathbf K}$ and Duhamel's formula:

$$
d\,e^{\mathbf K} = \int_0^1e^{s\mathbf K}\,d\mathbf K\,e^{(1-s)\mathbf K}\,ds = e^{\mathbf K}\Big(d\mathbf K - \tfrac1{2!}[\mathbf K, d\mathbf K] + \tfrac1{3!}[\mathbf K,[\mathbf K, d\mathbf K]] - \cdots\Big).
\label{expderiv}
$$

The commutator series follows from the integral by Baker–Campbell–Hausdorff ([[baker-campbell-hausdorff]]).

**Orbital rotations.** In the exponential parametrization $\mathbf U = e^{-\boldsymbol\kappa}$ with antisymmetric $\boldsymbol\kappa$ ([[unitary-matrices-exponential-logarithm]]), derivatives are always taken at $\boldsymbol\kappa = 0$. There Eq. [[#expderiv]] collapses to $d\mathbf U = -d\boldsymbol\kappa$, and the second derivative is $\tfrac12(d\boldsymbol\kappa_1d\boldsymbol\kappa_2 + d\boldsymbol\kappa_2d\boldsymbol\kappa_1)$. This is why orbital gradients and Hessians come out as simple commutators, the strategy of HJO Ch. 3 and Sec. 10.8.

**General functions of a symmetric matrix (Daleckii–Krein).** For $f(\mathbf S) = \mathbf U f(\mathbf s)\mathbf U^{\rm T}$ ([[functions-of-matrices]]) and symmetric $d\mathbf S$:

$$
\widetilde{df(\mathbf S)}_{ij} = f^{[1]}(s_i, s_j)\,d\tilde S_{ij},\qquad
f^{[1]}(s_i, s_j) = \begin{cases}\dfrac{f(s_i) - f(s_j)}{s_i - s_j}, & s_i\ne s_j\\[1ex] f'(s_i), & s_i = s_j .\end{cases}
\label{dk}
$$

The first divided difference $f^{[1]}$ replaces $f'$:

- $f = \sqrt{\ }$ gives $1/(\sqrt{s_i} + \sqrt{s_j})$;
- $f = x^{-1/2}$ gives Eq. [[#lowdin]];
- $f = e^x$ gives the eigenbasis form of Eq. [[#expderiv]].

The trace needs only the diagonal: $d\,\mathrm{tr}f(\mathbf S) = \mathrm{tr}[f'(\mathbf S)\,d\mathbf S]$.

## Worked example

!!! example "Every rule against central finite differences (computed for this note)"
    Random $4\times4$ matrices; relative error between the analytic differential and the central difference $[f(\mathbf X + h\,d\mathbf X) - f(\mathbf X - h\,d\mathbf X)]/2h$ with $h = 10^{-6}$:

    | rule | relative error |
    |---|---:|
    | $d(\mathbf X^{-1})$, Eq. [[#inv]] | $1.3\times10^{-10}$ |
    | $d\det\mathbf X$ and $d\ln\det\mathbf X$, Eq. [[#jacobi]] | $2.7\times10^{-10}$, $1.5\times10^{-10}$ |
    | $\partial\ln|\det\mathbf X|/\partial\mathbf X = \mathbf X^{-\rm T}$ (all 16 elements) | $2.9\times10^{-9}$ |
    | $\partial\,\mathrm{tr}(\mathbf{AXB})/\partial\mathbf X = \mathbf A^{\rm T}\mathbf B^{\rm T}$ | $5.9\times10^{-11}$ |
    | $d\mathbf S^{1/2}$ (Sylvester, elementwise) | $6.1\times10^{-9}$ |
    | $d\mathbf S^{-1/2}$, Eq. [[#lowdin]] | $7.1\times10^{-9}$ |
    | $d\,e^{\mathbf K}$, Eq. [[#expderiv]], by quadrature of the integral and by divided differences | $6.3\times10^{-11}$, $6.3\times10^{-11}$ |
    | $d\log\mathbf S$ and $d\sqrt{\mathbf S}$ by Eq. [[#dk]] | $4.9\times10^{-9}$, $6.1\times10^{-9}$ |

    The naive $e^{\mathbf K}d\mathbf K$ is wrong by 35% for these noncommuting matrices.

    **A chain rule through Löwdin orthogonalization.** $E(\mathbf S) = \mathrm{tr}(\mathbf h\,\mathbf S^{-1/2}\mathbf P\,\mathbf S^{-1/2})$, with $\mathbf h$ and $\mathbf P$ fixed symmetric matrices, mimics a one-electron energy in a Löwdin basis. With $\mathbf Y = \mathbf S^{-1/2}$, the product rule gives $dE = \mathrm{tr}[d\mathbf Y(\mathbf{PYh} + \mathbf{hYP})]$, with $d\mathbf Y$ from Eq. [[#lowdin]]. For a random symmetric $d\mathbf S$ this gives 0.0101692788 against the finite difference 0.0101692777.

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, 2000), Sec. 3.1 (matrix exponentials and their evaluation), Sec. 10.8 (gradients and Hessians from the exponential parametrization at $\boldsymbol\kappa = 0$). The differential rules, Jacobi's formula, the Sylvester-equation solution and the Daleckii–Krein formula are standard matrix analysis; they are stated and proved here and checked numerically, not taken from a cited page. Calculations in `Claude outputs/part0_math_batchF.py`, section A.
