---
id: floating-point-and-eigenvalue-perturbation
title: Floating point, backward stability and eigenvalue perturbation
summary: What accuracy an eigensolver can deliver in IEEE double precision. A backward-stable algorithm returns the exact eigensystem of A + ΔA with ‖ΔA‖₂ = O(ε)‖A‖₂; perturbation bounds then give eigenvalue errors of O(ε‖A‖₂) and eigenvector errors of O(ε‖A‖₂/gap). Consequences for tiny and near-degenerate eigenvalues, and why the characteristic polynomial is never used.
status: in-progress
kind: theory
level: intermediate
tags: [floating-point, machine-epsilon, backward-error, perturbation-theory, weyl, wielandt-hoffman, eigenvector-sensitivity, conditioning]
prerequisites: [matrix-eigenvalue-problem, spectral-decomposition-and-normal-operators]
related: [upper-bounds-and-interlacing, basis-orthogonalization, givens-rotations-and-householder-reflections]
key: weyl
order: 10
date: 2026-11-21
---

## Overview

An eigensolver cannot return the exact eigenvalues of a matrix stored in floating point. There are two reasons. Every eigensolver has an iterative part that must be stopped, and every intermediate number is rounded. This note fixes what "accurate" can mean for the real symmetric problem $\mathbf A\mathbf q_i = \mathbf q_i\lambda_i$, $\lambda_1\le\dots\le\lambda_n$. Every later note in this chapter is measured against this standard.

## Notation

- $\|\mathbf x\|_2 = (\mathbf x^{\mathsf T}\mathbf x)^{1/2}$ is the Euclidean norm.
- $\|\mathbf A\|_2 = \max_{\mathbf x\ne0}\|\mathbf A\mathbf x\|_2/\|\mathbf x\|_2$ is the spectral norm, equal to $\max(|\lambda_1|,|\lambda_n|)$ for symmetric $\mathbf A$.
- $\|\mathbf A\|_F = (\sum_{ij}A_{ij}^2)^{1/2}$ is the Frobenius norm, cheaper than $\|\mathbf A\|_2$ and within a factor $\sqrt n$ of it.
- Tilded quantities belong to the perturbed matrix $\tilde{\mathbf A} = \mathbf A + \mathbf E$.

## Floating-point model

An IEEE 754 double has 64 bits: 1 sign bit, 11 exponent bits and a 52-bit fraction. With the implicit leading bit there are 53 significant binary digits, about 16 decimal digits. The arithmetic model behind all error analysis is that each operation $\circ\in\{+,-,\times,/\}$ (and $\sqrt{\ }$) returns the exact result rounded:

$$
\mathrm{fl}(\alpha\circ\beta) = (\alpha\circ\beta)(1+\epsilon), \qquad |\epsilon|\le u .
\label{fl}
$$

Two constants are both called "machine epsilon", and they differ by a factor of 2:

- **Lang's ε (NumPy's eps).** Lang quotes the bound as $\varepsilon\approx2.22\times10^{-16}$. That is $2^{-52}$, the gap between 1 and the next larger double, which is also what `numpy.finfo(float).eps` returns.
- **Unit roundoff u.** Round-to-nearest gives the sharper bound $u = 2^{-53}\approx1.11\times10^{-16}$.

Either one serves in bounds such as Eq. [[#backward]], where only the order of magnitude matters.

Rounding makes floating-point addition non-associative: $(0.1+0.2)+0.3$ evaluates to `0.6000000000000001`, but $0.1+(0.2+0.3)$ evaluates to `0.6`. A mathematically correct algorithm can therefore still return a useless result, if its sequence of operations amplifies these relative errors.

## Forward error, backward error, stability

The **forward error** is the distance of the computed result from the exact one, for example $|\mathrm{fl}(\lambda_i)-\lambda_i|$. It is usually hard to bound directly.

Wilkinson's **backward error analysis** asks a different question: for which nearby matrix are the computed results *exact*? An eigensolver is **backward stable** if its computed eigenvalues (and eigenvectors) are the exact ones of a perturbed matrix $\mathbf A+\Delta\mathbf A$ with

$$
\|\Delta\mathbf A\|_2 = O(\varepsilon)\,\|\mathbf A\|_2 ,
\label{backward}
$$

where $O(\varepsilon)$ allows a modest polynomial in $n$ (for example $4n\varepsilon$ or $2n^2\varepsilon$). The forward error then follows from **perturbation theory**, which says how far the eigensystem can move when the matrix moves by $\Delta\mathbf A$:

$$
\text{forward error} \;\lesssim\; \text{(condition of the problem)}\times\text{(backward error)} .
$$

Orthogonal similarity transformations are backward stable. Every rotation or reflection adds a backward error of order $\varepsilon\|\mathbf A\|_F$, and orthogonal matrices do not amplify errors made earlier. This is why the direct eigensolvers of this chapter are built from them ([[givens-rotations-and-householder-reflections]]).

## Perturbation bounds for symmetric matrices

Let $\mathbf A$ and $\tilde{\mathbf A} = \mathbf A+\mathbf E$ be symmetric, with eigenvalues ordered ascending in both.

**Eigenvalues, one at a time.** This bound is often named after Weyl:

$$
|\tilde\lambda_i - \lambda_i| \le \|\mathbf E\|_2 \qquad (i = 1,\dots,n).
\label{weyl}
$$

*Proof.* The min–max (Courant–Fischer) characterization is $\lambda_i(\mathbf A) = \min_{\dim V = i}\ \max_{\mathbf x\in V,\ \|\mathbf x\|=1}\mathbf x^{\mathsf T}\mathbf A\mathbf x$. The same variational idea gives the interlacing results of [[upper-bounds-and-interlacing]]. For every unit $\mathbf x$, $\mathbf x^{\mathsf T}\tilde{\mathbf A}\mathbf x\le\mathbf x^{\mathsf T}\mathbf A\mathbf x+\|\mathbf E\|_2$. Taking the max over $V$ and then the min over all $V$ gives $\tilde\lambda_i\le\lambda_i+\|\mathbf E\|_2$. Exchanging the roles of $\mathbf A$ and $\tilde{\mathbf A}$ gives the other side. $\square$

**Eigenvalues, all together (Wielandt–Hoffman).**

$$
\Big(\sum_{i=1}^n(\tilde\lambda_i-\lambda_i)^2\Big)^{1/2} \le \|\mathbf E\|_F .
\label{wh}
$$

**Eigenvectors.** Let $\lambda_i$ be simple, with gap $\mathrm{gap}_i = \min_{j\ne i}|\lambda_j-\lambda_i|$. Let $\theta_i$ be the acute angle between $\mathbf q_i$ and $\tilde{\mathbf q}_i$. Then

$$
\tfrac12\sin2\theta_i \le \frac{\|\mathbf E\|_2}{\mathrm{gap}_i},
\qquad
\theta_i\approx\frac{\|\mathbf E\|_2}{\mathrm{gap}_i}\ \text{ when small}.
\label{evec}
$$

Lang states Eqs. [[#wh]] and [[#evec]] without proof, citing the literature. The $2\times2$ case shows where the gap comes from. For $\mathbf A = \mathrm{diag}(\lambda,\lambda+g)$ and $\mathbf E = \eta\begin{pmatrix}0&1\\1&0\end{pmatrix}$, the rotation that diagonalizes $\tilde{\mathbf A}$ ([[matrix-eigenvalue-problem]]) has $\tan2\theta = 2\eta/g$. So $\tfrac12\sin2\theta = \eta/\sqrt{g^2+4\eta^2}\le\eta/g$, which is Eq. [[#evec]] with near-equality when $\eta\ll g$.

## What a stable solver therefore delivers

Combine Eq. [[#backward]] with Eqs. [[#weyl]] and [[#evec]]:

1. **Eigenvalues** carry an *absolute* error of $O(\varepsilon)\|\mathbf A\|_2$. For $|\lambda_i|\approx\|\mathbf A\|_2$ only the last digit or two are wrong.
2. **Tiny eigenvalues** ($|\lambda_i|\sim\varepsilon\|\mathbf A\|_2$) may have no correct digit. Even their sign can be wrong. The overlap matrix of a nearly linearly dependent basis is the chemical example. Its smallest eigenvalues are the ones canonical orthogonalization divides by ([[basis-orthogonalization]]), which is why they are discarded below a threshold rather than trusted.
3. **Eigenvectors** of well-separated eigenvalues carry an error of $O(\varepsilon)\|\mathbf A\|_2/\mathrm{gap}_i$.
4. **Near-degenerate eigenvalues** ($\mathrm{gap}_i\lesssim\|\mathbf E\|$) have individually meaningless eigenvectors. Only the invariant subspace they span is determined. Any rotation inside it is an equally valid answer. Comparing individual eigenvectors across nearby matrices, for example orbitals along a scan, is then not well posed. Compare the projector onto the subspace instead.

For special classes of matrices (for example graded or diagonally dominant ones), relative perturbations of the entries cause only relative perturbations of the eigenvalues. Suitable algorithms then get even tiny eigenvalues to high relative accuracy (Lang, ref. 4: Barlow and Demmel). Lang notes that a carefully implemented Jacobi method can, in some cases, deliver much more accurate eigensystems than the reduction-based solvers ([[jacobi-eigenvalue-method]]).

## Why the characteristic polynomial is never used

Finding the roots of $\det(\mathbf A-\lambda\mathbf 1)$ is the textbook route ([[matrix-eigenvalue-problem]]). Numerically it is a poor route, for two reasons:

- the coefficients of the polynomial are computed with rounding errors;
- the roots of a high-degree polynomial are extremely sensitive to its coefficients.

The problem "eigenvalues of a symmetric $\mathbf A$" is well conditioned (Eq. [[#weyl]]). The detour through coefficients replaces it with an ill-conditioned one.

!!! example "Worked examples (all numbers from the script named in the Source)"
    **1. Characteristic polynomial against an orthogonal solver.** Take $\mathbf A = \mathbf Q\,\mathrm{diag}(1,2,\dots,20)\,\mathbf Q^{\mathsf T}$ with a random orthogonal $\mathbf Q$, so $\|\mathbf A\|_2 = 20$.

    | Route | max $\lvert\mathrm{fl}(\lambda_i)-\lambda_i\rvert$ |
    |---|---:|
    | `numpy.linalg.eigvalsh` (orthogonal transformations) | $1.4\times10^{-14}$ |
    | `numpy.poly` then `numpy.roots` | $9.0\times10^{-2}$ (at $\lambda = 14$) |

    The relative residual of `eigh` is $\|\mathbf A\mathbf Q'-\mathbf Q'\mathbf\Lambda'\|_2/\|\mathbf A\|_2 = 1.7\times10^{-15}$. That is a backward error of a few $\varepsilon$, as Eq. [[#backward]] promises. The forward error $1.4\times10^{-14}$ matches $\varepsilon\|\mathbf A\|_2\approx4.4\times10^{-15}$ times a small factor.

    **2. Weyl and Wielandt–Hoffman.** A random symmetric $6\times6$ $\mathbf A$ plus a random symmetric $\mathbf E$ scaled to $\|\mathbf E\|_2 = 10^{-3}$:

    - $\max_i|\tilde\lambda_i-\lambda_i| = 6.14\times10^{-4}\le10^{-3}$;
    - $(\sum_i(\tilde\lambda_i-\lambda_i)^2)^{1/2} = 7.48\times10^{-4}\le\|\mathbf E\|_F = 1.57\times10^{-3}$.

    **3. Eigenvector sensitivity.** $\mathbf A = \mathrm{diag}(1,1+g)$, $\mathbf E = \eta\begin{pmatrix}0&1\\1&0\end{pmatrix}$, $\eta = 10^{-10}$:

    | gap $g$ | rotation $\theta$ (rad) | $\tfrac12\sin2\theta$ | bound $\eta/g$ | $\lvert\tilde\lambda_1-\lambda_1\rvert$ |
    |---:|---:|---:|---:|---:|
    | $10^{-6}$ | $1.0\times10^{-4}$ | $1.0\times10^{-4}$ | $1.0\times10^{-4}$ | $\approx10^{-14}$ |
    | $10^{-8}$ | $1.0\times10^{-2}$ | $1.0\times10^{-2}$ | $1.0\times10^{-2}$ | $1.0\times10^{-12}$ |
    | $10^{-10}$ | $0.554$ | $0.447$ | $1$ | $6.2\times10^{-11}$ |
    | $10^{-12}$ | $0.783\approx\pi/4$ | $0.500$ | $100$ | $9.9\times10^{-11}$ |

    The eigenvalues never move by more than $\eta$. The eigenvectors rotate by $\approx\eta/g$, until for $g\ll\eta$ they are fully mixed ($\theta\to\pi/4$).

    **4. Tiny eigenvalues: Hilbert matrices** $H_{ij} = 1/(i+j-1)$. The exact eigenvalues of the *float64* matrices were computed with `mpmath` at 60 digits.

    | $n$ | $\lambda_{\min}$ (exact) | `eigvalsh` | rel. error | $\max_i\lvert\Delta\lambda_i\rvert$ | $\varepsilon\|\mathbf H\|_2$ |
    |---:|---:|---:|---:|---:|---:|
    | 10 | $1.093252\times10^{-13}$ | $1.093270\times10^{-13}$ | $1.6\times10^{-5}$ | $8.9\times10^{-16}$ | $3.9\times10^{-16}$ |
    | 12 | $1.067490\times10^{-16}$ | $1.088673\times10^{-16}$ | $2.0\times10^{-2}$ | $2.2\times10^{-16}$ | $4.0\times10^{-16}$ |
    | 14 | $-6.32\times10^{-18}$ | $-7.60\times10^{-18}$ | $0.20$ | $1.7\times10^{-16}$ | $4.1\times10^{-16}$ |

    Every eigenvalue is correct to an absolute $\sim\varepsilon\|\mathbf H\|_2$. The largest one is correct to all digits; the smallest loses all of them. For $n=14$, rounding the entries to float64 has already made the stored matrix indefinite: its exact smallest eigenvalue is negative, although the exact Hilbert matrix is positive definite.

## Source

Grotendorst, *Modern Methods and Algorithms of Quantum Chemistry* (NIC Series Vol. 3, 2nd ed., John von Neumann Institute for Computing, Jülich, 2000): chapter by B. Lang, "Direct Solvers for Symmetric Eigenvalue Problems", pp. 231-257, Secs. 1.2, 2.1, 2.2, pp. 232-236, Eqs. (1)-(6).

The proof of Eq. [[#weyl]] from the min–max principle and the $2\times2$ illustration of Eq. [[#evec]] are mine, not Lang's. Numbers: `Claude outputs/part7_ch1_numerical_linear_algebra.py`, section A.
