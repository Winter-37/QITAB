---
id: bisection-and-inverse-iteration
title: Bisection with Sturm counts, power and inverse iteration
summary: For selected eigenpairs of a symmetric tridiagonal T. The signs of the pivots of T − μ1 = LDLᵀ count the eigenvalues below μ (Sylvester's law of inertia), so bisection locates any chosen eigenvalue, one bit per O(n) step. Inverse iteration then gives its eigenvector in one or two O(n) solves. Clustered eigenvalues spoil orthogonality and need explicit Gram–Schmidt. Worked Sturm table, convergence numbers and a near-degenerate example (Wilkinson W21+).
status: in-progress
kind: algorithm
level: intermediate
tags: [bisection, sturm-sequence, sylvester-inertia, gershgorin, power-iteration, inverse-iteration, eigenvalue-clusters, gram-schmidt, dsyevx]
prerequisites: [householder-tridiagonalization, floating-point-and-eigenvalue-perturbation]
related: [tridiagonal-qr-iteration, divide-and-conquer-eigensolver, choosing-a-symmetric-eigensolver, ci-optimization-newton-and-davidson]
key: sturm
order: 50
date: 2026-11-21
---

## Overview

When only some eigenvalues are needed, for example the lowest few or all in a window, the QR iteration does too much work. **Bisection** finds any chosen eigenvalue by counting. **Inverse iteration** then supplies its eigenvector. Both work on the tridiagonal $\mathbf T$ (diagonal $\alpha_i$, off-diagonal $\beta_i\ne0$) produced by [[householder-tridiagonalization]].

## Counting eigenvalues below μ

For $\mu\in\mathbb R$ define (Lang Eq. (21))

$$
\delta_1 = \alpha_1-\mu,\qquad
\delta_i = (\alpha_i-\mu) - \frac{\beta_i^2}{\delta_{i-1}}\quad(i = 2,\dots,n),
\label{sturm}
$$

and let $\nu(\mu)$ be the number of negative $\delta_i$. **Claim:** $\nu(\mu)$ equals the number of eigenvalues of $\mathbf T$ smaller than $\mu$.

*Proof.* Write $\mathbf T-\mu\mathbf 1 = \mathbf L\mathbf D\mathbf L^{\mathsf T}$ with $\mathbf L$ unit lower bidiagonal ($L_{i,i-1} = \ell_i$) and $\mathbf D = \operatorname{diag}(\delta_i)$. Comparing entries:

- the $(1,1)$ entry gives $\delta_1 = \alpha_1-\mu$;
- the $(i,i-1)$ entry gives $\ell_i\delta_{i-1} = \beta_i$;
- the $(i,i)$ entry gives $\delta_i + \ell_i^2\delta_{i-1} = \alpha_i-\mu$.

Together these are Eq. [[#sturm]]. By Sylvester's law of inertia, $\mathbf T-\mu\mathbf 1$ and $\mathbf D$ are congruent and so have the same number of negative eigenvalues. Those of $\mathbf T-\mu\mathbf 1$ are $\lambda_i-\mu$. $\square$

If some $\delta_{i-1} = 0$ exactly, replace it by a tiny number. The count is unaffected.

**A starting interval** comes from Gershgorin's theorem. All eigenvalues lie in

$$
\Big[\min_i(\alpha_i-\rho_i),\ \max_i(\alpha_i+\rho_i)\Big],\qquad \rho_i = |\beta_i|+|\beta_{i+1}|\quad(\beta_1 = \beta_{n+1} := 0).
$$

## Bisection (Lang Algorithm 9)

Suppose $\nu(a) < k\le\nu(b)$, so that $\lambda_k\in[a,b)$. Evaluate $\nu$ at the midpoint $c$:

- if $\nu(c)\ge k$, keep $[a,c)$;
- otherwise keep $[c,b)$.

Each step costs one $O(n)$ evaluation of Eq. [[#sturm]] and gains exactly one bit, so reaching width $w$ from width $W$ takes $\log_2(W/w)$ steps. The method extends directly to a run of consecutive eigenvalues or to all eigenvalues in a window.

Bisection uses no orthogonal transformations; it is related to Gaussian elimination without pivoting, which is unstable in general. It is nevertheless a stable algorithm with a very small backward error. Disjoint sets of eigenvalues can be computed on different processors.

Its weakness is linear convergence. In practice bisection is used only to **isolate** each eigenvalue in its own interval, and a superlinear root finder (Newton, or Brent's zeroin) finishes the job. If more than about a third of the spectrum is wanted, Lang finds QR-type methods faster on a serial machine.

## Power iteration and inverse iteration

**Power iteration** (Lang Algorithm 10) repeats $\tilde{\mathbf v} = \mathbf T\mathbf v$, $\mathbf v = \tilde{\mathbf v}/\|\tilde{\mathbf v}\|$. The normalization prevents overflow. If one eigenvalue $\lambda_{\max}$ dominates in modulus, $\pm\mathbf v$ tends to its eigenvector. The error shrinks linearly with factor $|\lambda_{\max,2}/\lambda_{\max}|$, where $\lambda_{\max,2}$ is the eigenvalue of second-largest modulus.

**Inverse iteration** is power iteration on $(\mathbf T-\mu\mathbf 1)^{-1}$. That matrix has the same eigenvectors as $\mathbf T$, with eigenvalues $1/(\lambda_i-\mu)$. If $\mu$ is a good approximation to $\lambda_i$, then $1/(\lambda_i-\mu)$ dominates by the factor $\min_{j\ne i}|\lambda_j-\mu|/|\lambda_i-\mu|$, which is very large. One step is

$$
(\mathbf T-\mu\mathbf 1)\,\tilde{\mathbf v} = \mathbf v,\qquad \mathbf v\leftarrow\tilde{\mathbf v}/\|\tilde{\mathbf v}\| .
\label{invit}
$$

For tridiagonal $\mathbf T$ the solve costs $O(n)$. With $\mu$ from bisection or QR, experience shows one or two steps are enough. That gives an eigenvector for $O(n)$ flop, against $O(n^2)$ per vector for QR with accumulation. Different eigenvectors can be computed in parallel. The near-singularity of $\mathbf T-\mu\mathbf 1$ is harmless: the solve error lies almost entirely along the wanted eigenvector, which is then normalized away.

## Clusters

If $\lambda_i\approx\lambda_{i+1}\approx\dots\approx\lambda_j$, the shifted systems for different eigenvalues in the cluster are almost identical, so they return almost identical vectors. Orthogonality is lost; this matches the sensitivity bound $\theta\lesssim\|\mathbf E\|/\mathrm{gap}$ of [[floating-point-and-eigenvalue-perturbation]]. Two partial remedies:

- Start each eigenvalue from a fresh random vector.
- In every step for $\mathbf v_{\ell+1}$, orthogonalize $\tilde{\mathbf v}$ against the vectors $\mathbf v_i,\dots,\mathbf v_\ell$ already accepted in the cluster (modified Gram–Schmidt, $\tilde{\mathbf v}\leftarrow\tilde{\mathbf v}-(\mathbf v_r^{\mathsf T}\tilde{\mathbf v})\mathbf v_r$ one $r$ at a time) before normalizing.

The explicit orthogonalization costs up to $O(n^3)$ for large clusters. Neither remedy rules out the rarer failure of matching a vector to the wrong eigenvalue.

When Lang wrote, a variant of inverse iteration that gives orthogonal vectors without explicit orthogonalization was being developed (Dhillon's thesis, Lang ref. 12). This became the MRRR algorithm behind LAPACK's `dsyevr`, which is SciPy's default `eigh` driver *(link to MRRR from LAPACK documentation; to verify against the LAPACK Users' Guide)*. LAPACK's `dsyevx` (SciPy `driver="evx"`) is bisection plus inverse iteration.

!!! example "Worked example: the 4×4 T of [[householder-tridiagonalization]]"
    The matrix is $\boldsymbol\alpha = (4, \tfrac{10}3, -\tfrac{33}{25}, \tfrac{149}{75})$, $\boldsymbol\beta = (-3, -\tfrac53, \tfrac{68}{75})$, with eigenvalues $-2.197517$, $1.084364$, $2.268531$, $6.844621$. Gershgorin gives the interval $[-3.893333,\ 8.000000]$.

    | $\mu$ | $\delta_1$ | $\delta_2$ | $\delta_3$ | $\delta_4$ | $\nu(\mu)$ |
    |---:|---:|---:|---:|---:|---:|
    | $-3$ | 7 | 5.0476 | 1.1297 | 4.2590 | 0 |
    | $-2$ | 6 | 3.8333 | $-0.0446$ | 22.403 | 1 |
    | 1 | 3 | $-0.6667$ | 1.8467 | 0.5415 | 1 |
    | 2 | 2 | $-3.1667$ | $-2.4428$ | 0.3232 | 2 |
    | 3 | 1 | $-8.6667$ | $-3.9995$ | $-0.8078$ | 3 |
    | 7 | $-3$ | $-0.6667$ | $-4.1533$ | $-4.8154$ | 4 |

    Every count agrees with the true number of eigenvalues below $\mu$. Which $\delta_i$ is negative changes, but not how many.

    **Bisection for $\lambda_2$** from the Gershgorin interval (width 11.89) to a relative width of $10^{-12}$: 43 halvings, against $\log_2$ of the width ratio $= 42.3$. The result is $\lambda_2 = 1.084364463773$, all digits correct.

    **Power iteration** from $(1,1,1,1)/2$ converges to $\lambda = 6.844621$. $\sin\angle(\mathbf v,\mathbf q_{\max})$ is $2.7\times10^{-2}$ after 5 steps and $9.9\times10^{-5}$ after 10, a factor $0.33$ per step. The predicted factor is $|2.268531/6.844621| = 0.331$.

    **Inverse iteration** at $\mu = \lambda_2(\text{bisection})$: the residual $\|\mathbf T\mathbf v-\mu\mathbf v\|$ is $3.5\times10^{-13}$ after one step and $2.2\times10^{-13}$ after two. The floor is set by $|\mu-\lambda_2|$, that is, by the bisection tolerance.

    **A near-degenerate pair: Wilkinson's $W_{21}^+$** ($\alpha_i = |11-i|$ for $i = 1..21$, all $\beta_i = 1$). Its two largest eigenvalues are $10.746194182903395$ and $10.746194182903324$, a gap of $7.1\times10^{-14}$.

    - Three inverse-iteration steps for each, from the same random start vector, give residuals of $1.4\times10^{-15}$ (both excellent), but $|\mathbf v_1^{\mathsf T}\mathbf v_2| = 6.6\times10^{-4}$.
    - With modified Gram–Schmidt against $\mathbf v_1$ inside the iteration for $\mathbf v_2$: $|\mathbf v_1^{\mathsf T}\mathbf v_2| = 1.1\times10^{-16}$, and the residual stays at $1.8\times10^{-15}$.
    - Both vectors lie in the exact two-dimensional invariant subspace to all 15 digits. Only the split within the subspace was ill determined.

## Source

Grotendorst, *Modern Methods and Algorithms of Quantum Chemistry* (NIC Series Vol. 3, 2nd ed., John von Neumann Institute for Computing, Jülich, 2000): chapter by B. Lang, "Direct Solvers for Symmetric Eigenvalue Problems", pp. 231-257, Secs. 5.2, 5.3, pp. 249-251, Eq. (21), Algorithms 9-10.

The $\mathbf L\mathbf D\mathbf L^{\mathsf T}$ derivation of Eq. [[#sturm]] is mine (Lang states the result). The remark that the near-singular solve is harmless is the standard argument, not in Lang. Numbers: `Claude outputs/part7_ch1_numerical_linear_algebra.py`, section E.
