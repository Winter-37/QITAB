---
id: neumann-series-and-operator-expansions
title: Neumann series and operator expansions - the geometric series of a matrix or operator, the resolvent and Dyson equation, the Born series, expansion of an inverse, and the exponential series
summary: The geometric series carries over to matrices and operators: (1 − A)⁻¹ = Σ Aᵏ converges when the spectral radius of A is below 1. This Neumann series solves integral equations by iteration (Arfken Sec. 16.3). It also expands a resolvent G = (E − H₀ − V)⁻¹ in powers of V, which is the Dyson equation G = G₀ + G₀VG. In scattering the same expansion is the Born series of the Lippmann–Schwinger equation. Expanding an inverse in a perturbation, (A + δA)⁻¹ = A⁻¹ − A⁻¹δA A⁻¹ + …, gives first-order response formulas. The exponential series e^A = Σ Aᵏ/k! always converges and defines rotations, time evolution and orbital rotations. Worked examples: a Neumann series checked against a matrix inverse, a Dyson series, and the exponential of a rotation generator.
status: in-progress
kind: theory
level: intermediate
tags: [neumann-series, operator-series, spectral-radius, resolvent, dyson-equation, born-series, lippmann-schwinger, matrix-inverse-expansion, matrix-exponential, integral-equation]
prerequisites: [sequences-series-and-convergence, functions-of-matrices]
related: [baker-campbell-hausdorff, unitary-matrices-exponential-logarithm, interaction-picture-and-dyson-series, born-approximation-and-lippmann-schwinger, one-particle-greens-function, rayleigh-schrodinger-perturbation-theory]
key: neumann
order: 80
date: 2026-11-25
---

$\mathbf A$ is a square matrix (or a bounded operator); $\rho(\mathbf A) = \max|\lambda_i|$ is its spectral radius and $\|\mathbf A\|$ any submultiplicative norm. $\mathbf 1$ is the identity.

## The Neumann series

**Statement.** The geometric series of [[sequences-series-and-convergence]] carries over unchanged:

$$
(\mathbf 1 - \mathbf A)^{-1} = \sum_{k=0}^\infty\mathbf A^k = \mathbf 1 + \mathbf A + \mathbf A^2 + \cdots\qquad\text{if }\rho(\mathbf A) < 1 .
\label{neumann}
$$

**Proof.** The partial sums satisfy $(\mathbf 1 - \mathbf A)S_N = \mathbf 1 - \mathbf A^{N+1}$. And $\mathbf A^N\to0$ exactly when $\rho(\mathbf A) < 1$. A sufficient test is $\|\mathbf A\| < 1$ in any norm, since $\rho\le\|\mathbf A\|$. The error after $N$ terms falls as $\rho^{N+1}$.

**Divergence.** If $\rho(\mathbf A)\ge1$ the series diverges, but $(\mathbf 1 - \mathbf A)^{-1}$ may still exist. Convergence of the series proves the inverse exists; its failure proves nothing (Arfken Sec. 16.3).

**Integral equations.** Arfken introduces the series for the Fredholm equation $\varphi(x) = f(x) + \lambda\int K(x, t)\varphi(t)\,dt$, written $\varphi = f + \lambda K\varphi$. Iterating gives

$$
\varphi = f + \lambda Kf + \lambda^2K^2f + \cdots = (1 - \lambda K)^{-1}f .
$$

It converges for $|\lambda|$ small enough (Arfken Sec. 16.3, Eqs. 16.56–16.59). Arfken gives a sufficient condition in terms of the maximum of $|K|$; the sharp condition is $|\lambda|\rho(K) < 1$. The same iteration applies to Volterra equations, where it always converges. Iterative solvers built on this series are Jacobi iteration and the simplest SCF iteration; acceleration methods (DIIS, Krylov) exist because $\rho$ is often close to 1.

## Resolvents and the Dyson equation

**The resolvent.** For a Hamiltonian $H = H_0 + V$ and a complex energy $E$ off the spectrum, define $G(E) = (E - H)^{-1}$ and $G_0 = (E - H_0)^{-1}$. Then $E - H = G_0^{-1}(\mathbf 1 - G_0V)$, and Eq. [[#neumann]] gives

$$
G = G_0 + G_0VG_0 + G_0VG_0VG_0 + \cdots,\qquad G = G_0 + G_0VG .
\label{dyson}
$$

**Meaning.** The second form is the Dyson equation: exact, whether or not the series converges. The series converges when $\rho(G_0V) < 1$. Near an eigenvalue of $H$ it fails, because $G$ has a pole there that no finite order of $G_0$ reproduces. Summing selected terms to infinite order is how many-body Green's functions are built ([[one-particle-greens-function]]).

**The Born series.** In scattering, the Lippmann–Schwinger equation $|\psi\rangle = |\phi\rangle + G_0V|\psi\rangle$ has the same form. Its Neumann series is the Born series; its first term is the Born approximation ([[born-approximation-and-lippmann-schwinger]]).

**Time-dependent version.** The time-ordered exponential of the interaction picture is a Neumann series of a Volterra integral equation, and it always converges ([[interaction-picture-and-dyson-series]]).

**Perturbation theory.** Expanding the resolvent's poles in powers of $V$ gives the Rayleigh–Schrödinger series ([[rayleigh-schrodinger-perturbation-theory]]). Its convergence is limited by the same spectral condition.

## Expanding an inverse

**First-order response.** For invertible $\mathbf A$ and a small change $\delta\mathbf A$, factor $\mathbf A + \delta\mathbf A = \mathbf A(\mathbf 1 + \mathbf A^{-1}\delta\mathbf A)$ and apply Eq. [[#neumann]]:

$$
(\mathbf A + \delta\mathbf A)^{-1} = \mathbf A^{-1} - \mathbf A^{-1}\delta\mathbf A\,\mathbf A^{-1} + \mathbf A^{-1}\delta\mathbf A\,\mathbf A^{-1}\delta\mathbf A\,\mathbf A^{-1} - \cdots
$$

The first-order term gives $\partial(\mathbf A^{-1})/\partial x = -\mathbf A^{-1}(\partial\mathbf A/\partial x)\mathbf A^{-1}$. This formula differentiates the overlap-inverse and the orbital Hessian inverse in analytic gradients and response theory.

**Löwdin orthogonalization.** The same idea with the binomial series gives $\mathbf S^{-1/2} = (\mathbf 1 + \boldsymbol\Delta)^{-1/2} = \mathbf 1 - \tfrac12\boldsymbol\Delta + \tfrac38\boldsymbol\Delta^2 - \cdots$ for an overlap matrix $\mathbf S = \mathbf 1 + \boldsymbol\Delta$ with small off-diagonal $\boldsymbol\Delta$ ([[taylor-and-maclaurin-expansions]]).

## The exponential series

**Definition.** For every square matrix the series

$$
e^{\mathbf A} = \sum_{k=0}^\infty\frac{\mathbf A^k}{k!}
$$

converges absolutely, since $\|\mathbf A^k\|/k!\le\|\mathbf A\|^k/k!$.

**Uses.**

- Rotations are $e^{\theta\mathbf K}$ for an antisymmetric generator $\mathbf K$.
- Time evolution is $e^{-iHt/\hbar}$.
- Orbital rotations are $e^{\boldsymbol\kappa}$ with anti-Hermitian $\boldsymbol\kappa$ ([[unitary-matrices-exponential-logarithm]]).

**Commutators.** $e^{\mathbf A}e^{\mathbf B}\ne e^{\mathbf A + \mathbf B}$ unless the matrices commute. The correction is the Baker–Campbell–Hausdorff series ([[baker-campbell-hausdorff]]), and the Trotter product $(e^{\mathbf A/n}e^{\mathbf B/n})^n\to e^{\mathbf A + \mathbf B}$ is its practical consequence in quantum simulation.

**In practice.** The bare series is a poor numerical method for large $\|\mathbf A\|$, because of cancellation. Libraries use scaling and squaring with Padé approximants ([[asymptotic-expansions]]).

## Worked examples

!!! example "Neumann, Dyson and exponential series (computed for this note)"
    **Neumann series.** A random $5\times5$ matrix scaled to $\rho(\mathbf A) = 0.6$: 60 terms of Eq. [[#neumann]] reproduce $(\mathbf 1 - \mathbf A)^{-1}$ to $3.6\times10^{-14}$ in Frobenius norm. That is consistent with $0.6^{60}\approx5\times10^{-14}$.

    **Dyson series.** $H_0 = \mathrm{diag}(0, 1, 2.5)$, $V = 0.2\begin{pmatrix}0&1&0.5\\1&0&1\\0.5&1&0\end{pmatrix}$, $E = 0.4$. Here $\rho(G_0V) = 0.328$, and 40 orders of Eq. [[#dyson]] match $(E - H)^{-1}$ to $5\times10^{-16}$. Near $E = 0$, an eigenvalue of $H_0$, $\rho(G_0V)$ grows without bound and the series fails.

    **Exponential.** The generator $\mathbf K = \begin{pmatrix}0&-1\\1&0\end{pmatrix}$ times 0.8: 25 terms give $\begin{pmatrix}0.696707&-0.717356\\0.717356&0.696707\end{pmatrix}$, the rotation by 0.8 rad, with $\cos0.8 = 0.696707$. The even powers of $\mathbf K$ build the cosine and the odd powers the sine, because $\mathbf K^2 = -\mathbf 1$.

## Source

Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005), Sec. 16.3 (Neumann series, Eqs. 16.56–16.59, the operator form and the convergence criterion), Sec. 3.4 (matrix exponentials of Hermitian and unitary matrices). The resolvent, Dyson-equation, Löwdin and Trotter remarks are standard material not taken from Arfken. Calculations in `Claude outputs/part0_math_batchE.py`, section C.
