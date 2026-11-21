---
id: preconditioned-conjugate-gradient
title: Preconditioned conjugate gradients, and CPHF as the example
summary: CG converges according to the spectrum of A, so solve an equivalent system whose matrix C⁻ᵀAC⁻¹ has a smaller condition number or tighter clusters. Algorithm 5.3 needs only solves with M = CᵀC, and its residuals are M⁻¹-orthogonal. For orbital-response equations the orbital-energy-difference diagonal is the natural M. Water RHF/cc-pVDZ CPHF: κ drops from 69.4 to 3.3, CG iterations from 24-34 to 11-12, and the polarizability matches finite field to all five printed decimals. N&W's Algorithm 5.3 as printed starts with p₀ = −r₀; the correct start is p₀ = −y₀, and the printed version needs 42-64 iterations on the same problem.
status: in-progress
kind: algorithm
level: advanced
tags: [preconditioning, pcg, cphf, polarizability, incomplete-cholesky, jacobi-preconditioner, orbital-energy-denominators, response-equations]
prerequisites: [linear-conjugate-gradient-method, cphf-closed-shell]
related: [z-vector-method, davidson-and-jacobi-davidson-methods, diis-extrapolation, inexact-newton-and-newton-cg, molecular-properties-and-response, cholesky-and-generalized-eigenproblem]
conventions: [ia-letters, spatial-orbitals, chemists-integrals]
key: pcg
order: 50
date: 2026-11-21
---

## Overview

The CG error after $k$ steps is set by how well a degree-$k$ polynomial with $Q(0) = 1$ can be made small on the spectrum of $\mathbf A$ ([[linear-conjugate-gradient-method]]). **Preconditioning** changes the spectrum: solve an equivalent system whose matrix has a smaller condition number, or eigenvalues in a few tight clusters.

## Change of variables

**Transformation (N&W Eqs. (5.36)-(5.37)).** With a nonsingular $\mathbf C$ set $\hat{\mathbf x} = \mathbf C\mathbf x$. Then $\phi(\mathbf x) = \frac12\mathbf x^{\mathsf T}\mathbf A\mathbf x-\mathbf b^{\mathsf T}\mathbf x$ becomes

$$
\hat\phi(\hat{\mathbf x}) = \tfrac12\hat{\mathbf x}^{\mathsf T}(\mathbf C^{-\mathsf T}\mathbf A\mathbf C^{-1})\hat{\mathbf x}-(\mathbf C^{-\mathsf T}\mathbf b)^{\mathsf T}\hat{\mathbf x},
$$

and CG on $\hat\phi$ converges according to the eigenvalues of $\mathbf C^{-\mathsf T}\mathbf A\mathbf C^{-1}$. These are the eigenvalues of $\mathbf M^{-1}\mathbf A$ with $\mathbf M = \mathbf C^{\mathsf T}\mathbf C$, since the two matrices are similar.

**Back in the original variables.** Rewriting CG on $\hat\phi$ in terms of $\mathbf x$, every occurrence of $\mathbf C$ combines into $\mathbf M$. With $\mathbf r_k = \mathbf A\mathbf x_k-\mathbf b$ and $\mathbf y_k = \mathbf M^{-1}\mathbf r_k$ (the preconditioned residual):

$$
\begin{aligned}
&\mathbf r_0 = \mathbf A\mathbf x_0-\mathbf b,\quad \mathbf M\mathbf y_0 = \mathbf r_0,\quad \mathbf p_0 = -\mathbf y_0;\\
&\alpha_k = \frac{\mathbf r_k^{\mathsf T}\mathbf y_k}{\mathbf p_k^{\mathsf T}\mathbf A\mathbf p_k},\quad
\mathbf x_{k+1} = \mathbf x_k+\alpha_k\mathbf p_k,\quad
\mathbf r_{k+1} = \mathbf r_k+\alpha_k\mathbf A\mathbf p_k,\quad
\mathbf M\mathbf y_{k+1} = \mathbf r_{k+1},\\
&\beta_{k+1} = \frac{\mathbf r_{k+1}^{\mathsf T}\mathbf y_{k+1}}{\mathbf r_k^{\mathsf T}\mathbf y_k},\quad
\mathbf p_{k+1} = -\mathbf y_{k+1}+\beta_{k+1}\mathbf p_k .
\end{aligned}
\label{pcg}
$$

$\mathbf M = \mathbf1$ recovers plain CG. The residuals now satisfy $\mathbf r_i^{\mathsf T}\mathbf M^{-1}\mathbf r_j = 0$ for $i\ne j$ (N&W Eq. (5.39)), and $\mathbf x_k$ minimizes $\|\mathbf x-\mathbf x^*\|_{\mathbf A}$ over $\mathbf x_0+\mathcal K_k(\mathbf M^{-1}\mathbf A,\mathbf M^{-1}\mathbf r_0)$. The extra cost per step is one solve $\mathbf M\mathbf y = \mathbf r$. $\mathbf M$ must be SPD.

**Printed start.** N&W's Algorithm 5.3 (1st ed., p. 118) sets $\mathbf p_0 = -\mathbf r_0$. The transformed CG starts with $\hat{\mathbf p}_0 = -\hat{\mathbf r}_0 = -\mathbf C^{-\mathsf T}\mathbf r_0$, i.e. $\mathbf p_0 = \mathbf C^{-1}\hat{\mathbf p}_0 = -\mathbf M^{-1}\mathbf r_0 = -\mathbf y_0$. With $\mathbf p_0 = -\mathbf r_0$ the later directions are no longer conjugate to the first, and the iteration degrades badly (example below).

## Choosing M

**Requirements (N&W p. 119).** $\mathbf M^{-1}\mathbf A$ should have a favorable spectrum; $\mathbf M$ should be cheap to build and store; $\mathbf M\mathbf y = \mathbf r$ should be cheap to solve. No preconditioner is best for all matrices: the good ones use the structure and origin of the problem.

**General-purpose choices (N&W pp. 119-120).**

- **Diagonal (Jacobi).** $\mathbf M = \mathrm{diag}(\mathbf A)$.
- **Symmetric successive overrelaxation (SSOR)** and **banded** preconditioners.
- **Incomplete Cholesky**, probably the most effective general choice. Run the Cholesky factorization but keep a factor $\tilde{\mathbf L}$ no denser (or not much denser) than the lower triangle of $\mathbf A$; then $\mathbf M = \tilde{\mathbf L}\tilde{\mathbf L}^{\mathsf T}$, $\mathbf C = \tilde{\mathbf L}^{\mathsf T}$, and $\mathbf C^{-\mathsf T}\mathbf A\mathbf C^{-1}\approx\mathbf1$. The factorization can break down (a negative pivot); a shift of the diagonal is then added. Cholesky itself is in [[cholesky-and-generalized-eigenproblem]].

**In electronic structure.** Orbital-response matrices are diagonally dominant in the canonical MO basis, with diagonal close to orbital-energy differences. $\mathbf M = \mathrm{diag}(\varepsilon_a-\varepsilon_i)$ is free, positive for a closed-shell RHF reference, and usually very good. The same denominators precondition CC amplitude equations and Davidson eigenvalue problems ([[davidson-and-jacobi-davidson-methods]]).

## Example: CPHF for the polarizability of water

**Equations (spatial orbitals, chemists' notation; [[cphf-closed-shell]]).** For a static field $F_c$ along $c\in\{x,y,z\}$, the first-order orbital response $U^c_{ai}$ solves

$$
\sum_{bj}M_{ai,bj}\,U^c_{bj} = b^c_{ai},\qquad
M_{ai,bj} = (\varepsilon_a-\varepsilon_i)\delta_{ab}\delta_{ij}+4(ai|bj)-(ab|ij)-(aj|ib),\qquad
b^c_{ai} = -\langle a|r_c|i\rangle ,
$$

and the polarizability is $\alpha_{cd} = 4\sum_{ai}b^c_{ai}\,(\mathbf M^{-1}\mathbf b^d)_{ai}$. $\mathbf M$ is SPD at a stable RHF solution. The products $\mathbf M\mathbf u$ are built from AO Fock-like contractions (PySCF `gen_response`); $\mathbf M$ itself is never needed, but here it was also formed to inspect its spectrum.

!!! example "Water RHF/cc-pVDZ at the HJO reference geometry (computed for this note)"

    5 occupied, 19 virtual orbitals: 95 unknowns. The molecule lies in the $xz$ plane with the $C_2$ axis along $z$.

    - **Spectrum.** $\mathbf M$ has eigenvalues in $[0.3426, 23.769]$, $\kappa = 69.4$. With $\mathbf D = \mathrm{diag}(\varepsilon_a-\varepsilon_i)$, $\kappa(\mathbf D^{-1/2}\mathbf M\mathbf D^{-1/2}) = 3.34$. The diagonal of $\mathbf M$ differs from $\varepsilon_a-\varepsilon_i$ by up to 47%, yet $\mathbf D$ is an excellent preconditioner.
    - **Iterations** to $\|\mathbf r\|/\|\mathbf b\|<10^{-10}$:

    | field | CG | PCG, $\mathbf M = \mathbf D$ | Alg. 5.3 as printed ($\mathbf p_0 = -\mathbf r_0$) |
    |---|---|---|---|
    | $x$ | 33 | 11 | 42 |
    | $y$ | 24 | 11 | 64 |
    | $z$ | 34 | 12 | 51 |

    - **Polarizability** (a.u.): $\alpha_{xx} = 7.44967$, $\alpha_{yy} = 3.02862$, $\alpha_{zz} = 4.97004$, off-diagonal elements zero by symmetry. Finite field ($F = \pm10^{-4}$ a.u., central difference of the SCF dipole): 7.44967, 3.02862, 4.97004. This needs the field SCF converged to an orbital gradient of $10^{-10}$: with only the energy converged to $10^{-13}$, the density error ($\sim\sqrt{10^{-13}}$) divided by $2F$ left the finite-field values scattered by up to $7\times10^{-4}$ from run to run.

    For a rough comparison, the bound $2q^k$ of [[linear-conjugate-gradient-method]] with $q = (\sqrt\kappa-1)/(\sqrt\kappa+1)$ falls below $10^{-10}$ after 99 steps for $\kappa = 69.4$ and 20 steps for $\kappa = 3.34$. (It bounds the $\mathbf A$-norm error, not the residual, so this is only indicative.) CG does much better than both because it adapts to the actual eigenvalue distribution.

**Several right-hand sides.** The three field directions share $\mathbf M$. They can be solved together (block CG, or simply in one loop that batches the products). For nuclear perturbations ($3N$ right-hand sides) the Z-vector method replaces all of them by one solve with $\mathbf M^{\mathsf T}$ ([[z-vector-method]]).

## Checks

`Claude outputs/part7_ch3_iterative_solvers.py`, section D: symmetry and spectrum of $\mathbf M$, iteration counts with and without the preconditioner, the printed Algorithm 5.3, the polarizability against finite field. The same system solved by a diagonal fixed-point iteration with DIIS is compared in [[diis-extrapolation]].

## Source

Nocedal and Wright, *Numerical Optimization* (Springer, New York, 1999), Ch. 5, Sec. 5.1 (Preconditioning; Practical Preconditioners), pp. 117-120, Eqs. (5.36)-(5.39), Algorithm 5.3. The CPHF equations are those of [[cphf-closed-shell]]; the calculations (PySCF 2.15 for integrals and response products, my own PCG) were done for this note.
