---
id: nonlinear-conjugate-gradient
title: Nonlinear conjugate gradient methods
summary: Generalize linear CG to a nonlinear f by replacing the residual with the gradient and the exact step with a line search. Search directions p_{k+1} = −g_{k+1} + β_{k+1}p_k with the Fletcher–Reeves, Polak–Ribière (PR, PR+) or Hestenes–Stiefel choice of β. Why FR needs the strong Wolfe conditions with c₂ < ½ to stay a descent method, FR's tendency to stall, global convergence results (FR yes, PR only with modifications), restarts and n-step quadratic convergence. O(n) memory; compared on Rosenbrock and a coupled n = 1000 problem.
status: in-progress
kind: algorithm
level: intermediate
tags: [conjugate-gradient, nonlinear-cg, fletcher-reeves, polak-ribiere, hestenes-stiefel, restart, large-scale-optimization]
prerequisites: [line-searches-and-wolfe-conditions]
related: [limited-memory-bfgs, inexact-newton-and-newton-cg, Linear conjugate gradient method, density-based-hartree-fock]
key: fr
order: 90
date: 2026-11-21
---

## Overview

Linear CG minimizes a convex quadratic $\tfrac12\mathbf x^{\mathsf T}\mathbf A\mathbf x-\mathbf b^{\mathsf T}\mathbf x$, i.e. solves $\mathbf A\mathbf x = \mathbf b$, in at most $n$ steps. It uses mutually $\mathbf A$-conjugate directions built from the residuals, and needs only a few vectors of storage. That algorithm, its expanding-subspace theory and preconditioning belong to Chapter 3 (iterative solvers, planned: [[Linear conjugate gradient method]]). This note treats the extension to general smooth $f$. Levine describes it as the gradient-only alternative to quasi-Newton geometry optimization for large molecules.

## The Fletcher–Reeves method (Algorithm 5.4)

Start from $\mathbf p_0 = -\mathbf g_0$. Each iteration:

1. Find $\alpha_k$ by a line search and set $\mathbf x_{k+1} = \mathbf x_k+\alpha_k\mathbf p_k$.
2. Evaluate $\mathbf g_{k+1}$ and set
   $$
   \beta_{k+1}^{\mathrm{FR}} = \frac{\mathbf g_{k+1}^{\mathsf T}\mathbf g_{k+1}}{\mathbf g_k^{\mathsf T}\mathbf g_k},\qquad
   \mathbf p_{k+1} = -\mathbf g_{k+1}+\beta_{k+1}\mathbf p_k .
   \label{fr}
   $$

On a convex quadratic with exact line searches this is linear CG. There are no matrix operations at all.

**Descent requires a careful line search.** Taking the inner product of the direction with $\mathbf g_k$ gives

$$
\mathbf g_k^{\mathsf T}\mathbf p_k = -\|\mathbf g_k\|^2+\beta_k\,\mathbf g_k^{\mathsf T}\mathbf p_{k-1}.
$$

An exact line search makes the second term vanish. An inexact one can make it dominate, giving an ascent direction. N&W therefore impose the strong Wolfe conditions with

$$
0<c_1<c_2<\tfrac12 \qquad(\text{instead of } c_2<1).
$$

Lemma 5.6 then shows that every FR direction is a descent direction, with

$$
-\frac1{1-c_2}\le\frac{\mathbf g_k^{\mathsf T}\mathbf p_k}{\|\mathbf g_k\|^2}\le\frac{2c_2-1}{1-c_2} .
$$

**Global convergence** (Thm. 5.8). Assume a bounded level set and Lipschitz gradient, and strong Wolfe steps with $c_2<\tfrac12$. Then FR satisfies $\liminf\|\mathbf g_k\| = 0$. The proof combines Lemma 5.6 with the Zoutendijk condition ([[line-searches-and-wolfe-conditions]]).

**Weakness.** Lemma 5.6 also implies that if FR produces a bad direction, nearly orthogonal to $-\mathbf g_k$, with a tiny step, then $\mathbf g_{k+1}\approx\mathbf g_k$ and $\beta_{k+1}\approx1$. The next direction is then nearly as bad. FR can therefore crawl for many iterations unless it is restarted.

## Other choices of β

**Polak–Ribière** (Eq. (5.43)):

$$
\beta_{k+1}^{\mathrm{PR}} = \frac{\mathbf g_{k+1}^{\mathsf T}(\mathbf g_{k+1}-\mathbf g_k)}{\mathbf g_k^{\mathsf T}\mathbf g_k}.
$$

After a tiny unproductive step, $\mathbf g_{k+1}\approx\mathbf g_k$ gives $\beta\approx0$, an automatic restart along $-\mathbf g_{k+1}$. This is why PR usually beats FR in practice. Its theory is weaker. The strong Wolfe conditions do not guarantee descent for PR. Thm. 5.9 gives a smooth $f$ on $\mathbb R^3$ on which PR with an *ideal* line search cycles with $\|\mathbf g_k\|$ bounded away from zero.

**PR+** (Eq. (5.44)): $\beta_{k+1}^+ = \max(\beta_{k+1}^{\mathrm{PR}},0)$. With a suitably adapted strong-Wolfe line search, this choice gives descent directions and global convergence.

**Hestenes–Stiefel** (Eq. (5.45)): $\beta_{k+1}^{\mathrm{HS}} = \mathbf g_{k+1}^{\mathsf T}(\mathbf g_{k+1}-\mathbf g_k)/[(\mathbf g_{k+1}-\mathbf g_k)^{\mathsf T}\mathbf p_k]$. It equals PR under exact line searches. It is also the memoryless BFGS direction ([[limited-memory-bfgs]]).

All choices coincide on a convex quadratic with exact line searches.

## Restarts and rate

**Periodic restart.** Setting $\beta = 0$ every $n$ steps gives **$n$-step quadratic convergence**:

$$
\|\mathbf x_{k+n}-\mathbf x^*\| = O(\|\mathbf x_k-\mathbf x^*\|^2).
$$

Near $\mathbf x^*$ the function is almost quadratic, and a restart begins a fresh CG cycle on it. For large $n$ this is rarely useful, since the solution is often reached in fewer than $n$ steps.

**Orthogonality test** (Eq. (5.47)). Successive gradients of a quadratic are orthogonal. Restart whenever

$$
\frac{|\mathbf g_k^{\mathsf T}\mathbf g_{k-1}|}{\|\mathbf g_k\|^2}\ge\nu,\qquad \nu\approx0.1 .
$$

PR+ restarts automatically whenever $\beta^{\mathrm{PR}}<0$.

## Practice

The line search must be more accurate than for quasi-Newton methods: $c_2 = 0.1$ is typical, against 0.9. The first trial step should be taken from the previous decrease, since the direction has no natural scale. In memory and per-iteration cost (a few vectors, $O(n)$ work), nonlinear CG is the cheapest gradient method. It is usually beaten in evaluations by L-BFGS with modest $m$, for little more storage. CG-based searches also appear in electronic structure, for example the conjugate-gradient density-matrix searches mentioned in [[density-based-hartree-fock]].

!!! example "Worked example"
    Strong Wolfe line search with $c_1 = 10^{-4}$, $c_2 = 0.1$, stop at $\|\mathbf g\|\le10^{-6}$. "Evals" counts line-search evaluations.

    | problem | variant | restart test $\nu = 0.1$ | no restart test |
    |---|---|---|---|
    | Rosenbrock, $n = 2$, from $(-1.2,1)$ | FR | 31 it, 129 evals (13 restarts) | 62 it, 194 evals |
    | | PR | 30 it, 114 evals | 25 it, 107 evals |
    | | PR+ | 30 it, 114 evals | 22 it, 86 evals |
    | chained Rosenbrock, $n = 1000$, $x_i = 1+0.5\sin i$ | FR | 120 it, 303 evals (11 restarts) | 192 it, 430 evals |
    | | PR = PR+ | 95 it, 247 evals | 246 it, 561 evals |

    - FR without restarts needs about twice as many iterations as with them: the stalling described above.
    - PR with the orthogonality test was best on the large problem.
    - In both problems $\beta^{\mathrm{PR}}$ never became negative, so PR and PR+ coincide there.

    For comparison:

    - SciPy's `method="CG"` (a Polak–Ribière variant) needs 289 iterations and 458 evaluations on the $n = 1000$ problem;
    - L-BFGS ($m = 5$) needs 57 iterations and 65 evaluations ([[limited-memory-bfgs]]).

    **Quadratic termination:** FR with exact line searches on a random SPD quadratic in $n = 8$ reaches $\|\mathbf g_8\| = 1.2\times10^{-12}$ after exactly 8 steps.

## Source

Nocedal and Wright, *Numerical Optimization* (Springer, New York, 1999), Ch. 5, Sec. 5.2, pp. 120-131, Algorithm 5.4, Lemma 5.6, Thms. 5.7-5.9, Eqs. (5.40)-(5.47). Levine, *Quantum Chemistry* (7th ed., Pearson, 2014), Sec. 15.10, pp. 489-490 (steepest descent and conjugate gradients for large molecules).

The descriptions of PR+ convergence follow N&W, who state them without proof. Numbers: `Claude outputs/part7_ch2_numerical_optimization.py`, section I.
