---
id: matrix-differentiation-identities
title: Matrix differentiation identities
summary: Derivatives of the inverse, determinant, log-determinant and powers of a matrix; first-order perturbation formulas for eigenvalues and eigenvectors of symmetric and generalized eigenproblems; the Fréchet derivative of the matrix exponential; and the derivative of S^{1/2}, S^{-1/2} and S^{-1} in the eigenbasis of S (Daleckii–Krein). All checked against central finite differences.
status: in-progress
kind: reference
level: intermediate
tags: [matrix-calculus, derivatives, eigenvalues, perturbation, lowdin, matrix-exponential, gradients]
prerequisites: [matrix-and-tensor-identities]
related: [functions-of-matrices, unitary-matrices-exponential-logarithm, hellmann-feynman-and-virial-theorems, derivative-integrals-and-u-matrices, basis-orthogonalization, rayleigh-schrodinger-perturbation-theory]
order: 30
date: 2026-11-17
---

$\mathbf A(x)$ depends smoothly on a real parameter $x$ (a nuclear coordinate, a field strength), and $\mathbf A' = \mathrm d\mathbf A/\mathrm dx$. Analytic-gradient theory is built from these rules.

## Inverse, determinant, powers

$$
(\mathbf A^{-1})' = -\mathbf A^{-1}\mathbf A'\mathbf A^{-1},
$$

$$
(\ln|\det\mathbf A|)' = \operatorname{tr}(\mathbf A^{-1}\mathbf A'),\qquad
(\det\mathbf A)' = \det\mathbf A\,\operatorname{tr}(\mathbf A^{-1}\mathbf A')\quad\text{(Jacobi's formula)},
$$

$$
\big(\operatorname{tr}\mathbf A^k\big)' = k\operatorname{tr}(\mathbf A^{k-1}\mathbf A') .
$$

The first follows from differentiating $\mathbf A\mathbf A^{-1} = \mathbf 1$. Applied to the overlap matrix it gives the derivative of $\mathbf S^{-1}$ that appears in every gradient with a non-orthogonal basis.

## Eigenvalues and eigenvectors

**Symmetric (Hermitian) matrix**, $\mathbf H\mathbf v_k = \lambda_k\mathbf v_k$, orthonormal $\mathbf v_k$, $\lambda_k$ nondegenerate:

$$
\lambda_k' = \mathbf v_k^{\mathsf T}\mathbf H'\mathbf v_k,
\qquad
\mathbf v_k' = \sum_{j\ne k}\mathbf v_j\,\frac{\mathbf v_j^{\mathsf T}\mathbf H'\mathbf v_k}{\lambda_k - \lambda_j} .
$$

The first is the matrix form of the Hellmann–Feynman theorem ([[hellmann-feynman-and-virial-theorems]]); the second is first-order perturbation theory for the state, with the phase fixed so that $\mathbf v_k^{\mathsf T}\mathbf v_k' = 0$. A degenerate level needs degenerate perturbation theory first.

**Generalized problem** $\mathbf F\mathbf c_k = \lambda_k\mathbf S\mathbf c_k$, normalized $\mathbf c_k^{\mathsf T}\mathbf S\mathbf c_k = 1$:

$$
\lambda_k' = \mathbf c_k^{\mathsf T}\big(\mathbf F' - \lambda_k\mathbf S'\big)\mathbf c_k .
$$

This is the origin of the energy-weighted density term $-\sum\varepsilon_i\,\mathbf c_i^{\mathsf T}\mathbf S'\mathbf c_i$ in the Hartree–Fock gradient ([[rhf-analytic-gradient]]).

## Matrix exponential

The derivative of $e^{\mathbf A}$ is not $e^{\mathbf A}\mathbf A'$ unless $\mathbf A$ and $\mathbf A'$ commute. In general (Fréchet derivative)

$$
\big(e^{\mathbf A}\big)' = \int_0^1 e^{s\mathbf A}\,\mathbf A'\,e^{(1-s)\mathbf A}\,\mathrm ds
= e^{\mathbf A}\Big(\mathbf A' - \tfrac1{2!}[\mathbf A,\mathbf A'] + \tfrac1{3!}[\mathbf A,[\mathbf A,\mathbf A']] - \cdots\Big).
$$

At $\mathbf A = 0$ it reduces to $\mathbf A'$, which is why orbital-rotation gradients are simple at $\boldsymbol\kappa = 0$ but second derivatives pick up commutator terms ([[orbital-rotations]]). SciPy provides it as `scipy.linalg.expm_frechet`.

## Functions of a symmetric matrix (Löwdin orthogonalization)

Let $\mathbf S = \mathbf U\operatorname{diag}(s_i)\mathbf U^{\mathsf T}$ with $s_i > 0$, and write $\tilde{\mathbf S}' = \mathbf U^{\mathsf T}\mathbf S'\mathbf U$ (the perturbation in the eigenbasis). For $f(\mathbf S) = \mathbf U\operatorname{diag}(f(s_i))\mathbf U^{\mathsf T}$ the **Daleckii–Krein formula** gives

$$
\big[\mathbf U^{\mathsf T}f(\mathbf S)'\,\mathbf U\big]_{ij} = \tilde S'_{ij}\;\frac{f(s_i) - f(s_j)}{s_i - s_j},
\qquad\text{with}\ \frac{f(s_i) - f(s_j)}{s_i - s_j}\to f'(s_i)\ \text{when}\ s_i = s_j .
$$

For the three powers that occur in practice the divided difference simplifies:

| $f(\mathbf S)$ | factor multiplying $\tilde S'_{ij}$ |
|---|---|
| $\mathbf S^{1/2}$ | $\dfrac{1}{\sqrt{s_i} + \sqrt{s_j}}$ |
| $\mathbf S^{-1/2}$ | $-\dfrac{1}{\sqrt{s_is_j}\,(\sqrt{s_i} + \sqrt{s_j})}$ |
| $\mathbf S^{-1}$ | $-\dfrac{1}{s_is_j}$ |

The $\mathbf S^{-1/2}$ entry is the derivative of the symmetric (Löwdin) orthogonalizer $\mathbf X = \mathbf S^{-1/2}$ of [[basis-orthogonalization]]; the $\mathbf S^{1/2}$ entry is equivalent to solving the Sylvester equation $\mathbf S^{1/2}\mathbf Y + \mathbf Y\mathbf S^{1/2} = \mathbf S'$ for $\mathbf Y = (\mathbf S^{1/2})'$. Small eigenvalues of $\mathbf S$ (near-linear dependence) make all three factors large, so derivatives of orthogonalized quantities become ill-conditioned before the energy does.

## Checks

`part9_reference.py`, section E, compares every formula with a central finite difference (step $10^{-6}$) on random $5\times5$ matrices: inverse, log-determinant, determinant, $\operatorname{tr}\mathbf A^3$, eigenvalue and eigenvector derivatives (symmetric and generalized), the exponential (Gauss–Legendre quadrature of the integral, 30 points, and `expm_frechet`), and the three Daleckii–Krein factors. Agreement is $10^{-7}$ or better, the accuracy of the finite differences.

## Source

Standard matrix calculus, collected here and verified numerically. The eigenvalue formulas are first-order Rayleigh–Schrödinger perturbation theory in matrix form ([[rayleigh-schrodinger-perturbation-theory]]). The Daleckii–Krein divided-difference formula is the standard result for Fréchet derivatives of spectral functions of Hermitian matrices (reference to verify; the formula itself is checked numerically here).
