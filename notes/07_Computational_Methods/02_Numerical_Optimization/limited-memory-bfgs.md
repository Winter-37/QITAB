---
id: limited-memory-bfgs
title: Limited-memory BFGS (L-BFGS)
summary: For large n, store only the last m pairs (s_i, y_i) instead of the dense inverse Hessian. Unrolling the BFGS update gives H_k as a product formula, and the two-loop recursion computes H_k g in 4mn multiplications without ever forming a matrix. The initial matrix γ_k1 with γ_k = sᵀy/yᵀy is chosen afresh at every iteration, and m = 3–20 usually suffices. Checked against the explicit BFGS matrix, and on a coupled Rosenbrock function up to n = 10 000.
status: in-progress
kind: algorithm
level: intermediate
tags: [l-bfgs, limited-memory, two-loop-recursion, quasi-newton, large-scale-optimization, l-bfgs-b]
prerequisites: [bfgs-method]
related: [nonlinear-conjugate-gradient, inexact-newton-and-newton-cg, choosing-an-unconstrained-optimizer, geometry-optimization]
key: two-loop
order: 80
date: 2026-11-21
---

## Overview

BFGS stores an $n\times n$ matrix and spends $O(n^2)$ work per iteration. That is fine for the $3N$ Cartesian coordinates of a small molecule. It becomes the bottleneck for thousands of variables: large-molecule geometries, orbital-rotation parameters, or the many parameters of a variational circuit. L-BFGS keeps the curvature information of only the $m$ most recent steps, in $2mn$ numbers, and applies the implied inverse Hessian implicitly.

## Unrolling the update

Write the BFGS update of [[bfgs-method]] as

$$
\mathbf H_{k+1} = \mathbf V_k^{\mathsf T}\mathbf H_k\mathbf V_k+\rho_k\mathbf s_k\mathbf s_k^{\mathsf T},\qquad
\mathbf V_k = \mathbf 1-\rho_k\mathbf y_k\mathbf s_k^{\mathsf T},\quad \rho_k = \frac1{\mathbf y_k^{\mathsf T}\mathbf s_k}.
$$

Start each iteration from a simple $\mathbf H_k^0$ and apply only the last $m$ updates (N&W Eq. (9.5)):

$$
\begin{aligned}
\mathbf H_k = {}& (\mathbf V_{k-1}^{\mathsf T}\cdots\mathbf V_{k-m}^{\mathsf T})\,\mathbf H_k^0\,(\mathbf V_{k-m}\cdots\mathbf V_{k-1})\\
&+\rho_{k-m}(\mathbf V_{k-1}^{\mathsf T}\cdots\mathbf V_{k-m+1}^{\mathsf T})\,\mathbf s_{k-m}\mathbf s_{k-m}^{\mathsf T}\,(\mathbf V_{k-m+1}\cdots\mathbf V_{k-1})\\
&+\cdots+\rho_{k-1}\mathbf s_{k-1}\mathbf s_{k-1}^{\mathsf T}.
\end{aligned}
$$

## The two-loop recursion (Algorithm 9.1)

Products $\mathbf V_i\mathbf q = \mathbf q-\rho_i\mathbf y_i(\mathbf s_i^{\mathsf T}\mathbf q)$ cost one inner product and one vector update. Evaluating Eq. (9.5) applied to $\mathbf g_k$ from the inside out gives:

1. $\mathbf q\leftarrow\mathbf g_k$.
2. For $i = k-1,\dots,k-m$: $\ \alpha_i\leftarrow\rho_i\mathbf s_i^{\mathsf T}\mathbf q$, $\ \mathbf q\leftarrow\mathbf q-\alpha_i\mathbf y_i$.
3. $\mathbf r\leftarrow\mathbf H_k^0\mathbf q$.
4. For $i = k-m,\dots,k-1$: $\ \beta\leftarrow\rho_i\mathbf y_i^{\mathsf T}\mathbf r$, $\ \mathbf r\leftarrow\mathbf r+\mathbf s_i(\alpha_i-\beta)$.
5. Return $\mathbf r = \mathbf H_k\mathbf g_k$.

The first loop applies the $\mathbf V_i$ from the right; the $\alpha_i$ it stores are exactly the coefficients of the $\mathbf s_i\mathbf s_i^{\mathsf T}$ terms. The second loop applies the $\mathbf V_i^{\mathsf T}$ and adds those terms back.

The cost is $4mn$ multiplications, plus $n$ if $\mathbf H_k^0$ is diagonal. Because $\mathbf H_k^0$ enters only in step 3, it can be any matrix that is cheap to apply. It can even be given implicitly, through a solve with a cheap $\mathbf B_k^0$, such as a model Hessian built from force constants.

**Initial matrix** (Eq. (9.6)):

$$
\mathbf H_k^0 = \gamma_k\mathbf 1,\qquad \gamma_k = \frac{\mathbf s_{k-1}^{\mathsf T}\mathbf y_{k-1}}{\mathbf y_{k-1}^{\mathsf T}\mathbf y_{k-1}} .
\label{two-loop}
$$

This is the same curvature estimate as the BFGS initial scaling, renewed at every step. It keeps $\mathbf p_k$ well scaled, so that $\alpha = 1$ is usually accepted. As for BFGS, the line search must satisfy the Wolfe conditions, so that $\mathbf y^{\mathsf T}\mathbf s>0$ ([[line-searches-and-wolfe-conditions]]).

## The algorithm (Algorithm 9.2) and practice

Each iteration:

- computes $\mathbf p_k = -\mathbf H_k\mathbf g_k$ by the two-loop recursion;
- takes a Wolfe step;
- stores the new pair $(\mathbf s_k,\mathbf y_k)$, discarding the oldest once more than $m$ are held.

For the first $m$ iterations it is identical to BFGS started from the same $\mathbf H_0$.

- **Memory.** N&W report that $m$ between 3 and 20 usually works. Larger $m$ reduces evaluations, but each iteration costs more, so the fastest wall time is often at small $m$ (their Table 9.1). The best $m$ is problem dependent.
- **When to use it.** It is the method of choice for large problems whose Hessian is not sparse. It can beat Hessian-free Newton–CG ([[inexact-newton-and-newton-cg]]). Its weakness is slow convergence on ill-conditioned problems, where $m$ pairs cannot capture the spread of curvatures.
- **Relation to CG** (Sec. 9.1). The memoryless BFGS method resets $\mathbf H_k = \mathbf 1$ before every update. With exact line searches its direction is
  $$\mathbf p_{k+1} = -\mathbf g_{k+1}+\frac{\mathbf g_{k+1}^{\mathsf T}\mathbf y_k}{\mathbf y_k^{\mathsf T}\mathbf p_k}\mathbf p_k ,$$
  which is the Hestenes–Stiefel conjugate-gradient method. That reduces to Polak–Ribière when $\mathbf g_{k+1}^{\mathsf T}\mathbf p_k = 0$ ([[nonlinear-conjugate-gradient]]). L-BFGS extends this with $m$ stored pairs. Storage is $2mn+4n$ numbers, against $3n$ for Fletcher–Reeves and $4n$ for Polak–Ribière.
- **Compact representation.** N&W Sec. 9.2 writes the limited-memory matrices as $\mathbf B_k = \gamma\mathbf 1-[\ldots]\mathbf M_k^{-1}[\ldots]^{\mathsf T}$, with $n\times2m$ factors. This is what bound-constrained variants (L-BFGS-B, SciPy's `method="L-BFGS-B"`) and trust-region versions need.

!!! example "Worked examples"
    **Exactness.** With $m = 4$ stored pairs in $n = 6$ and $\mathbf H^0 = 0.7\,\mathbf 1$, the two-loop result equals the explicitly updated BFGS matrix times $\mathbf g$ to $5\times10^{-16}$. The cost is $4mn = 96$ multiplications instead of the 36 of a dense product, plus the $O(n^2)$ updates that are no longer needed.

    **A coupled test problem.** The chained Rosenbrock function $f = \sum_{i=1}^{n-1}[100(x_{i+1}-x_i^2)^2+(1-x_i)^2]$ has a tridiagonal Hessian and minimizer $\mathbf x^* = \mathbf 1$. Its gradient and Hessian-vector product were checked against finite differences to $3\times10^{-8}$. Start from $x_i = 1+0.5\sin i$ and stop at $\|\mathbf g\|\le10^{-5}$:

    | $n$ | $m = 3$ | $m = 5$ | $m = 17$ |
    |---:|---:|---:|---:|
    | 100 | 57 it / 64 evals | 51 / 56 | 45 / 47 |
    | 1000 | 55 / 60 | 57 / 65 | 45 / 51 |
    | 10000 | 70 / 78 | 59 / 66 | 46 / 51 |

    The iteration count hardly grows with $n$, and each run takes at most 0.03 s. SciPy's L-BFGS-B ($m = 10$, $n = 1000$) needs 38 iterations and 43 evaluations.

    Dense BFGS at $n = 1000$ needed 125 iterations, 140 evaluations and 8.9 s. In this run it was both slower per iteration ($O(n^2)$) and not better in iteration count than the limited-memory version.

    **A start where nothing helps.** From $(-1.2,1,-1.2,1,\dots)$ the chained function must be resolved roughly one coordinate at a time along its curved valley. L-BFGS ($m = 5$) then needs 546 iterations for $n = 100$ and 5020 for $n = 1000$. Memory does not cure a problem whose difficulty grows with $n$.

## Source

Nocedal and Wright, *Numerical Optimization* (Springer, New York, 1999), Ch. 9, Secs. 9.1-9.2, pp. 222-233, Algorithms 9.1-9.2, Table 9.1, Eqs. (9.1)-(9.6).

Numbers: `Claude outputs/part7_ch2_numerical_optimization.py`, section H.
