---
id: tridiagonal-qr-iteration
title: QR iteration for symmetric tridiagonal matrices
summary: The classical Phase II solver. One shifted QR step T − σ1 = QR, T′ = RQ + σ1 = QᵀTQ is carried out implicitly as a chain of n − 1 rotations that chase a bulge down the band, at O(n) flop. With Wilkinson's shift the last off-diagonal element converges globally and ultimately cubically, about two sweeps per eigenvalue, so all eigenvalues cost O(n²) and accumulating eigenvectors about 6n³. Worked convergence tables, shifted and unshifted.
status: in-progress
kind: algorithm
level: intermediate
tags: [qr-algorithm, wilkinson-shift, implicit-shift, bulge-chasing, deflation, cubic-convergence, dsteqr, dsyev]
prerequisites: [householder-tridiagonalization, givens-rotations-and-householder-reflections]
related: [bisection-and-inverse-iteration, divide-and-conquer-eigensolver, jacobi-eigenvalue-method, choosing-a-symmetric-eigensolver]
key: qr-step
order: 40
date: 2026-11-21
---

## Overview

After Phase I ([[householder-tridiagonalization]]) the problem is to diagonalize a symmetric tridiagonal $\mathbf T$ with diagonal $\alpha_1,\dots,\alpha_n$ and off-diagonal $\beta_2,\dots,\beta_n$. Assume every $\beta_i\ne0$. If some $\beta_i = 0$, $\mathbf T$ is block diagonal and the blocks are treated separately; this is **deflation**:

$$
\mathbf Q^{\mathsf T}\mathbf A\mathbf Q = \begin{pmatrix}\mathbf A_1&\mathbf 0\\\mathbf 0&\mathbf A_2\end{pmatrix}
\ \Rightarrow\ \operatorname{spec}\mathbf A = \operatorname{spec}\mathbf A_1\cup\operatorname{spec}\mathbf A_2,
$$

and the eigenvectors are $\mathbf Q_i\tilde{\mathbf x}$ (Lang Sec. 2.5). The QR iteration drives the $\beta_i$ to zero by orthogonal similarity transformations. Since its invention in the 1960s it has been the standard way to compute all eigenvalues.

## One QR step

For a shift $\sigma\in\mathbb R$, factor and recombine:

$$
\mathbf T - \sigma\mathbf 1 = \mathbf Q\mathbf R,\qquad \mathbf T' = \mathbf R\mathbf Q + \sigma\mathbf 1 .
\label{qr-step}
$$

Here $\mathbf Q$ is orthogonal and $\mathbf R$ upper triangular. Since $\mathbf R = \mathbf Q^{\mathsf T}(\mathbf T-\sigma\mathbf 1)$,

$$
\mathbf T' = \mathbf Q^{\mathsf T}(\mathbf T-\sigma\mathbf 1)\mathbf Q + \sigma\mathbf 1 = \mathbf Q^{\mathsf T}\mathbf T\mathbf Q ,
$$

so $\mathbf T'$ is an orthogonal similarity transform of $\mathbf T$ with the same eigenvalues. It is also tridiagonal. $\mathbf Q$ is the product of $n-1$ adjacent-plane rotations, so it has upper Hessenberg form. Then $\mathbf R\mathbf Q$ is upper Hessenberg, and a symmetric upper Hessenberg matrix is tridiagonal.

## Implicit form: chasing the bulge (Lang Algorithm 8)

Forming $\mathbf Q$ and $\mathbf R$ is unnecessary. One **sweep** works directly on $\mathbf T$:

1. Choose the shift $\sigma$.
2. Determine the $(1,2)$ rotation $\mathbf G_1$ that zeroes the second entry of the first column of $\mathbf T-\sigma\mathbf 1$, namely $(\alpha_1-\sigma,\ \beta_2,\ 0,\dots)^{\mathsf T}$. Apply $\mathbf T\leftarrow\mathbf G_1^{\mathsf T}\mathbf T\mathbf G_1$. This creates a **bulge**: a nonzero at position $(3,1)$ and $(1,3)$.
3. For $i = 2,\dots,n-1$, apply the $(i,i{+}1)$ rotation that zeroes the bulge at $(i{+}1,i{-}1)$. That rotation pushes a new bulge to $(i{+}2,i)$.
4. After the last rotation the bulge has left the matrix and $\mathbf T$ is tridiagonal again.

Each rotation costs $O(1)$ on a tridiagonal matrix, so a sweep is $O(n)$ flop.

The first rotation is the same as in the explicit QR factorization of $\mathbf T-\sigma\mathbf 1$, and the rest only restore the tridiagonal form. The result therefore equals the explicit step Eq. [[#qr-step]] up to signs of the rows and columns. The standard justification is the implicit-Q theorem, which Lang does not state; the equality was checked numerically (worked example).

## Shifts and convergence

**No shift** ($\sigma = 0$). The iteration then converges linearly. Order the eigenvalues by modulus; the last off-diagonal element shrinks by roughly the ratio of the smallest $|\lambda|$ to the next one per sweep, and $\alpha_n$ tends to the eigenvalue of smallest modulus. Lang notes that QR tends to deliver the eigenvalues in order of increasing modulus, but not always.

**Wilkinson's shift.** Take $\sigma$ to be the eigenvalue of the trailing $2\times2$ block $\begin{pmatrix}\alpha_{n-1}&\beta_n\\\beta_n&\alpha_n\end{pmatrix}$ that is closer to $\alpha_n$. With $d = (\alpha_{n-1}-\alpha_n)/2$, the two eigenvalues are $\alpha_n + d\pm\sqrt{d^2+\beta_n^2}$. The one closer to $\alpha_n$, written so that nothing cancels, is

$$
\sigma_{\mathrm W} = \alpha_n - \frac{\beta_n^2}{d + \operatorname{sign}(d)\sqrt{d^2+\beta_n^2}} .
\label{wilkinson}
$$

This uses $d - \operatorname{sign}(d)\sqrt{d^2+\beta_n^2} = -\beta_n^2/(d+\operatorname{sign}(d)\sqrt{d^2+\beta_n^2})$. With this shift the iteration converges **globally** (the $\beta_i$ are guaranteed to go to zero) and, with rare exceptions, **ultimately cubically**. Each sweep then roughly triples the number of correct digits in $\beta_n$.

Once $|\beta_n|$ is negligible, set it to zero and read off $\lambda\approx\alpha_n$. Then continue with the leading $(n-1)\times(n-1)$ block, or split the matrix wherever another $\beta_i$ has become negligible. The usual test is $|\beta_i|\le\varepsilon(|\alpha_{i-1}|+|\alpha_i|)$. After a warm-up, about two sweeps per eigenvalue suffice.

## Cost

| Task | flop |
|---|---|
| one sweep on $\mathbf T$ | $O(n)$ |
| all eigenvalues of $\mathbf T$ | $O(n^2)$ (about two sweeps per eigenvalue) |
| accumulating eigenvectors, $\mathbf V\leftarrow\mathbf V\mathbf G$ for every rotation | $\approx6n^3$ |
| forming $\mathbf Q_1$ from Phase I first (for a full $\mathbf A$) | $\tfrac43n^3$ |

The work on $\mathbf T$ itself is inherently sequential. The accumulation of $\mathbf V$ parallelizes easily. Because the method uses only rotations, it is backward stable ([[floating-point-and-eigenvalue-perturbation]]).

The same idea works for banded or full matrices. But one sweep then costs $O(b^2n)$, so they are reduced to tridiagonal form first. Lang lists related variants:

- the LR iteration, built on LU factorizations;
- the QL iteration, which chases from the bottom up;
- the square-root-free Pal–Walker–Kahan QR for eigenvalues only;
- Parlett's qd algorithms on a factored form of $\mathbf T$.

!!! example "Worked example: convergence on the 4×4 T of [[householder-tridiagonalization]]"
    The matrix is $\mathbf T = \mathrm{tridiag}\big((-3,-\tfrac53,\tfrac{68}{75});\ (4,\tfrac{10}3,-\tfrac{33}{25},\tfrac{149}{75})\big)$, with eigenvalues $-2.197517$, $1.084364$, $2.268531$, $6.844621$.

    First Wilkinson shift: $\sigma_{\mathrm W} = 2.2189514165$. One implicit sweep and the explicit step Eq. [[#qr-step]] give the same matrix up to signs.

    **Wilkinson shift:**

    | sweep | $\lvert\beta_n\rvert$ | $\alpha_n$ |
    |---:|---:|---|
    | 1 | $2.05\times10^{-2}$ | 2.268246770959383 |
    | 2 | $1.14\times10^{-6}$ | 2.268531406430163 |
    | 3 | $2.0\times10^{-16}$ | 2.268531406431242 |

    The exact eigenvalue is $2.2685314064312423$. The step from $2\times10^{-2}$ to $10^{-6}$ is consistent with cubic convergence ($(2\times10^{-2})^3\approx10^{-5}$). Sweep 3 is limited by rounding, not by the iteration.

    **No shift:** $|\beta_n| = 0.886,\ 0.704,\ 0.418,\ 0.214,\ 0.105,\ 0.051,\ 0.025,\ 0.012$, while $\alpha_n\to1.0844$, the eigenvalue of smallest modulus. The ratio settles near $0.48$, compared with the predicted $|1.084364/2.197517| = 0.4934$.

    **All eigenvalues of a random $50\times50$ tridiagonal matrix**, with Wilkinson shifts and deflation (splitting at any negligible $\beta_i$): 146 sweeps in total, that is 2.9 per eigenvalue. The largest error against `eigvalsh` is $8.9\times10^{-15}$.

## Software

LAPACK `dsteqr` is the implicit QL/QR iteration for a tridiagonal matrix. `dsyev` (SciPy `eigh(driver="ev")`) combines it with `dsytrd`, the Householder reduction. In the timing of [[choosing-a-symmetric-eigensolver]] it is the slowest full-spectrum driver, mostly because of the $6n^3$ accumulation.

## Source

Grotendorst, *Modern Methods and Algorithms of Quantum Chemistry* (NIC Series Vol. 3, 2nd ed., John von Neumann Institute for Computing, Jülich, 2000): chapter by B. Lang, "Direct Solvers for Symmetric Eigenvalue Problems", pp. 231-257, Secs. 2.5, 5, 5.1, pp. 238, 247-249, Eq. (7), Algorithm 8.

The similarity and tridiagonality arguments for Eq. [[#qr-step]], the cancellation-free form Eq. [[#wilkinson]] and the unshifted convergence factor are standard but not in Lang; they were checked numerically. The routine names `dsteqr`/`dsyev` are LAPACK's (Lang Sec. 8 names `DSYEV`). Numbers: `Claude outputs/part7_ch1_numerical_linear_algebra.py`, section D.
