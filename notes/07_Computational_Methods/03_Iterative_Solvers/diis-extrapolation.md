---
id: diis-extrapolation
title: DIIS - direct inversion in the iterative subspace
summary: DIIS accelerates a fixed-point iteration by replacing the newest iterate with the affine combination of recent iterates whose combined error vector is smallest. The weights solve a bordered linear system of dimension m + 1, whose multiplier equals the minimal squared error norm. Linearity between iterates and errors is assumed; it is exact for affine iterations and approximate for SCF and CC. On the CPHF system, DIIS on the orbital-energy-denominator iteration cuts 28-41 iterations to 11-14, close to preconditioned CG. For water SCF and CCSD, history length, conditioning of B and the definition of the error vector are examined; PySCF's CCSD reproduces HJO Table 13.2 (13 iterations with DIIS against 48-49 without at 2R_ref).
status: in-progress
kind: algorithm
level: advanced
tags: [diis, pulay, convergence-acceleration, extrapolation, fixed-point-iteration, scf-convergence, coupled-cluster-convergence, error-vector]
prerequisites: [newton-and-broyden-methods-for-nonlinear-equations, preconditioned-conjugate-gradient, scf-convergence-diis-and-newton]
related: [coupled-cluster-optimization-and-lagrangian, scf-second-order-and-stability, scf-procedure, linear-conjugate-gradient-method]
conventions: [ia-letters]
key: diis-system
order: 70
date: 2026-11-21
---

## Overview

Many electronic-structure iterations are fixed-point iterations $\mathbf x\leftarrow\mathbf g(\mathbf x)$ that converge slowly, oscillate or diverge:

- **SCF:** $\mathbf x$ is the Fock matrix; $\mathbf g$ diagonalizes it, occupies orbitals, and rebuilds the Fock matrix ([[scf-convergence-diis-and-newton]]).
- **Coupled cluster:** $\mathbf x$ is the amplitude vector; $\mathbf g(\mathbf t) = \mathbf t+\Delta\mathbf t$ with the quasi-Newton step $\Delta t_\mu = -\Omega_\mu(\mathbf t)/\varepsilon_\mu$, $\varepsilon_\mu$ the orbital-energy difference of excitation $\mu$ ([[coupled-cluster-optimization-and-lagrangian]]).
- **Linear response:** $\mathbf x\leftarrow\mathbf x-\mathbf D^{-1}(\mathbf A\mathbf x-\mathbf b)$ with $\mathbf D$ the orbital-energy diagonal of $\mathbf A$.

Pulay's DIIS ("direct inversion in the iterative subspace", HJO Sec. 10.6.2) uses the history of the iteration instead of only its last step. It needs one **error vector** $\mathbf e$ per iterate, which vanishes at the solution and measures how far the iterate is from it.

## The extrapolation

**Ansatz.** After $m$ iterations with iterates $\mathbf x_1,\dots,\mathbf x_m$ and error vectors $\mathbf e_1,\dots,\mathbf e_m$, form

$$
\bar{\mathbf x} = \sum_{i=1}^mw_i\mathbf x_i,\qquad \sum_{i=1}^mw_i = 1 .
\label{affine}
$$

**Assumption: linearity.** If $\mathbf e$ depends linearly (affinely) on $\mathbf x$, the error of $\bar{\mathbf x}$ is

$$
\bar{\mathbf e} = \sum_iw_i\mathbf e_i ,
$$

and the constraint $\sum_iw_i = 1$ is exactly what makes this hold for an affine map. Choose the weights to make $\bar{\mathbf e}$ as small as possible.

**Weights (HJO Eqs. (10.6.25)-(10.6.28)).** Minimize $\|\bar{\mathbf e}\|^2 = \sum_{ij}w_iB_{ij}w_j$ with $B_{ij} = \mathbf e_i^{\mathsf T}\mathbf e_j$, subject to the constraint. With the Lagrangian $L = \mathbf w^{\mathsf T}\mathbf B\mathbf w-2\lambda(\sum_iw_i-1)$, stationarity gives $\mathbf B\mathbf w = \lambda\mathbf 1$, and with the constraint

$$
\begin{pmatrix}\mathbf B&-\mathbf 1\\-\mathbf 1^{\mathsf T}&0\end{pmatrix}\begin{pmatrix}\mathbf w\\\lambda\end{pmatrix} = \begin{pmatrix}\mathbf 0\\-1\end{pmatrix}.
\label{diis-system}
$$

Multiplying $\mathbf B\mathbf w = \lambda\mathbf 1$ by $\mathbf w^{\mathsf T}$ shows $\lambda = \mathbf w^{\mathsf T}\mathbf B\mathbf w = \|\bar{\mathbf e}\|^2$: the multiplier is the predicted squared error of the extrapolated iterate, a free convergence estimate.

**Then iterate.** Continue the fixed-point iteration from $\bar{\mathbf x}$: in SCF, diagonalize the averaged Fock matrix; in CC, take $\mathbf t^{(n+1)} = \sum_kw_k(\mathbf t^{(k)}+\Delta\mathbf t^{(k)})$ with $\Delta\mathbf t^{(k)}$ as error vectors (HJO Eqs. (13.4.11)-(13.4.13)).

## Why the constraint matters, and what DIIS is not

- **SCF.** The Fock matrix is $\mathbf f = \mathbf h+\mathbf G(\mathbf D)$, linear in the density. With $\sum w_i = 1$, $\sum_iw_i\mathbf f_i = \mathbf h+\mathbf G(\sum_iw_i\mathbf D_i)$: the one-electron part is kept exactly, and DIIS amounts to building the Fock matrix from an averaged density (HJO Eqs. (10.6.21)-(10.6.22)). This damps oscillations between two potentials.
- **Not an optimizer.** DIIS never produces a vector outside the span of the iterates it is given (HJO Sec. 13.4.3). It only makes better use of the steps that the underlying iteration (Roothaan step, quasi-Newton step) supplies. If those steps are poor, DIIS cannot invent good ones.
- **Linearity is approximate.** In SCF the error vectors are computed in orbitals that change every iteration, so the linear relation between $\mathbf f$ and $\mathbf e$ holds only approximately. Far from convergence DIIS can extrapolate to a worse point.

## Choosing the error vector

- **SCF:** the occupied–virtual block of the MO Fock matrix, $f_{ia}$, which vanishes by Brillouin's theorem at convergence; or equivalently the AO commutator $\mathbf{fDS}-\mathbf{SDf}$. Written in a fixed orthonormal basis $\mathbf X$ ($\mathbf X^{\mathsf T}\mathbf S\mathbf X = \mathbf1$), $\mathbf X^{\mathsf T}(\mathbf{fDS}-\mathbf{SDf})\mathbf X$ has the elements $\pm2f_{ia}$ of the current MO basis rotated into that fixed basis. Inner products between error vectors of different iterations are then taken in one basis, which is what the linearity assumption needs. Inner products of MO blocks from different iterations would mix bases.
- **CC:** the quasi-Newton step $\Delta\mathbf t$ (the residual scaled by the denominators) or the residual $\boldsymbol\Omega$ itself (HJO Sec. 13.4.3).
- **Linear problems:** the step $-\mathbf D^{-1}\mathbf r$. Here $\mathbf e$ is an affine function of $\mathbf x$, linearity is exact, and DIIS minimizes the $\mathbf D^{-1}$-scaled residual over the affine hull of the iterates.

## Practical details

- **History length.** Keep the last $m_{\max}$ (typically 6-10) vectors. Besides saving storage, the oldest vectors carry little information and their inclusion can degrade performance (HJO p. 462). They also make $\mathbf B$ more ill-conditioned.
- **Conditioning.** Near convergence the error vectors become nearly linearly dependent. In the water SCF runs below, the condition number of $\mathbf B$ reached $5\times10^{12}$ without harm, since Eq. [[#diis-system]] is solved directly and the bordering keeps it nonsingular. If the solve fails, drop the oldest vector.
- **When to start.** DIIS is usually switched on after one or two plain iterations, once a few error vectors exist. HJO apply it from the third CC iteration, so their first two iterations are identical with and without DIIS; PySCF's CCSD starts one iteration later (first three identical).
- **Cost.** Storage of $m_{\max}$ iterates and error vectors, and $m$ new inner products per iteration; negligible compared with a Fock build or a CC residual.

## Numerical tests

!!! example "Linear response: DIIS against preconditioned CG (computed for this note)"

    The CPHF system for water RHF/cc-pVDZ (95 unknowns, [[preconditioned-conjugate-gradient]]). Fixed-point iteration $\mathbf x\leftarrow\mathbf x-\mathbf D^{-1}(\mathbf M\mathbf x-\mathbf b)$, $\mathbf D = \mathrm{diag}(\varepsilon_a-\varepsilon_i)$; the spectral radius of $\mathbf1-\mathbf D^{-1}\mathbf M$ is 0.584, so the plain iteration converges linearly. Iterations to $\|\mathbf r\|/\|\mathbf b\|<10^{-10}$:

    | field | plain | DIIS, 4 vectors | DIIS, 8 | DIIS, all | PCG with the same $\mathbf D$ |
    |---|---|---|---|---|---|
    | $x$ | 28 | 14 | 12 | 12 | 11 |
    | $y$ | 34 | 15 | 12 | 11 | 11 |
    | $z$ | 41 | 17 | 14 | 13 | 12 |

    With the full history, DIIS needs almost exactly as many iterations as PCG. For an SPD linear system PCG is still preferable (no history to store), but DIIS needs neither symmetry nor linearity.

!!! example "SCF: water cc-pVQZ from the core Hamiltonian (computed for this note)"

    Symmetry-fixed occupation $3a_1^2\,1b_1^2\,1b_2^2$ (with which the plain SCF column of HJO Table 10.4 is reproduced; see [[scf-convergence-diis-and-newton]]). Error vector $\mathbf X^{\mathsf T}(\mathbf{fDS}-\mathbf{SDf})\mathbf X$, DIIS from the first iteration. Fock builds until $\|\mathbf{fDS}-\mathbf{SDf}\|<10^{-10}$:

    | history $m_{\max}$ | $R_{\text{ref}}$ | $2R_{\text{ref}}$ |
    |---|---|---|
    | 4 | 21 | 29 |
    | 6 | 18 | 25 |
    | 8 | 17 | 22 |
    | 20 | 17 | 22 |

    Plain SCF does not reach the threshold in 40 iterations at either geometry (factor 0.43 per iteration at $R_{\text{ref}}$; a two-cycle between $+6.3955$ and $+12.2826$ $E_h$ at $2R_{\text{ref}}$). With 8 vectors, the energy error rounds to 0.00000 $E_h$ from iteration 8 at $R_{\text{ref}}$ and from iteration 10 at $2R_{\text{ref}}$ (HJO: 8 and 15). The first two energies equal HJO's (16.00647, 9.58984 at $R_{\text{ref}}$); from the third on they differ (3.04024 against HJO's 4.64733), because HJO do not state their error-vector inner products or when DIIS starts. An earlier implementation in [[scf-convergence-diis-and-newton]] needed 15 iterations at $2R_{\text{ref}}$: the count depends on such details.

    **Occupation matters.** With aufbau occupation instead, plain SCF at $R_{\text{ref}}$ follows a different and slower path (9.99945 at iteration 2, still $2\times10^{-3}$ $E_h$ off at iteration 20, against $6\times10^{-5}$ with fixed occupation).

!!! example "CCSD: water cc-pVDZ, all electrons (PySCF; HJO Table 13.2)"

    PySCF's CCSD update is the orbital-energy quasi-Newton step, HJO Eq. (13.4.10). Energy errors per iteration:

    | geometry | without DIIS | with DIIS (PySCF default, 6 vectors) |
    |---|---|---|
    | $R_{\text{ref}}$ | 0.009388, 0.004537, 0.001233, 0.000488, 0.000188, … ; error $<5\times10^{-7}$ from iteration 13 (HJO: 12) | 0.009388, 0.004537, 0.001233, 0.000120, −0.000024, … ; from iteration 9 (HJO: 9) |
    | $2R_{\text{ref}}$ | 0.032697, 0.063687, 0.019485, 0.022513, 0.010350, … ; from iteration 48 (HJO: 49) | 0.032697, 0.063687, 0.019485, 0.022834, 0.006042, … ; from iteration 13 (HJO: 13) |

    Without DIIS the errors equal HJO's to the last printed digit. With DIIS the first iterations differ from HJO's (PySCF begins extrapolating one iteration later), but the iteration counts agree. Final energies −76.238116 and −75.929633 $E_h$, as in HJO. At $2R_{\text{ref}}$ the Jacobian is no longer diagonally dominant, the quasi-Newton step alone crawls, and DIIS cuts the work by a factor of almost four.

## Checks

`Claude outputs/part7_ch3_iterative_solvers.py`, sections D (linear-response comparison) and F (SCF and CCSD).

## Source

Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, Chichester, 2000), Sec. 10.6.2, pp. 460-463, Eqs. (10.6.20)-(10.6.28), Table 10.4; Secs. 13.4.1-13.4.4, pp. 670-674, Eqs. (13.4.10)-(13.4.13), Table 13.2. HJO cite Pulay for DIIS; the original papers were not consulted. The interpretation of $\lambda$, the linear-response comparison and all calculations were done for this note (PySCF 2.15).
