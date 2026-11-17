---
id: trotter-error-in-qpe-energies
title: Trotter error in phase-estimation energies - the effective Hamiltonian and step size for chemical accuracy
summary: When U = e^{−iHτ} is replaced by a product of Pauli-string exponentials, phase estimation measures the eigenvalues of the Trotter unitary, i.e. of an effective Hamiltonian H_eff = H + O(Δt). The energy error is not the operator-norm error. For a real molecular Hamiltonian, the first-order correction (i/2)Σ_{j<k}[H_j,H_k] has zero expectation in the real ground state, so even first-order Trotter gives an energy error ∝ Δt². Measured orders are 2.00 for H₂, an H₄ chain and frozen-core LiH. When the terms fall into two commuting groups, as for H₂, the first-order and Strang products are similar matrices and give identical energies. Step sizes for a 1.6 mEh Trotter error are Δt ≈ 0.6 (H₂), 0.33–0.54 (H₄) and 0.34–0.44 (LiH) Eh⁻¹. With t = 12 readout bits, H₂ needs about 12,300 Trotter steps, or 1.7 × 10⁵ Pauli exponentials.
status: in-progress
kind: comparison
level: advanced
tags: [trotter, product-formula, effective-hamiltonian, baker-campbell-hausdorff, phase-estimation, chemical-accuracy, pauli-exponentials, lih, h4]
prerequisites: [qpe-for-molecular-energies, simulation-of-quantum-systems, baker-campbell-hausdorff]
related: [qpe-cost-and-resource-estimates, jordan-wigner-mapping, iterative-phase-estimation]
order: 30
date: 2026-11-17
---

## Overview

Phase estimation needs controlled $e^{-iH\tau}$. The simplest implementation splits $H=\sum_kc_kP_k$ into Pauli strings, each exponentiated by a CNOT ladder and one $R_z$ ([[simulation-of-quantum-systems]]), and multiplies them in a product formula. The product is not $e^{-iH\Delta t}$, so the energy that QPE returns is shifted. This note asks how large the shift is, how it scales with the step $\Delta t$, and what step size chemical accuracy requires. The answers differ from the generic operator-norm analysis in instructive ways.

## What QPE measures with a Trotter unitary

Let $S(\Delta t)$ be one Trotter step and apply $S^n$ for total time $n\Delta t$. Phase estimation returns eigenphases of $S(\Delta t)$, which are exact eigenvalues of the **effective Hamiltonian** defined by

$$
S(\Delta t)=e^{-iH_{\text{eff}}\Delta t}.
$$

Long evolution does not accumulate Trotter error in the eigenvalues. The error is a fixed shift $E_{\text{eff}}-E_0$ that depends only on $\Delta t$. By Baker–Campbell–Hausdorff ([[baker-campbell-hausdorff]]):

- **First order**, $S_1=\prod_ke^{-ic_kP_k\Delta t}$:
$$
H_{\text{eff}}=H+\frac{i\Delta t}{2}\sum_{j<k}[H_k,H_j]+O(\Delta t^2),\qquad H_k=c_kP_k .
$$
The sign of the commutator depends on the multiplication order; the conclusion below does not.
- **Second order (Strang)**, the palindromic product: $H_{\text{eff}}=H+O(\Delta t^2)$.

## Why first order gives an O(Δt²) energy error here

The leading energy shift from first-order Trotter is $\langle\Psi_0|\tfrac{i}{2}\sum_{j<k}[H_k,H_j]|\Psi_0\rangle$. For a molecular Hamiltonian with real integrals, the Jordan–Wigner matrix is **real symmetric**, since every Pauli string that appears has an even number of $Y$s. Its ground state can be chosen real. Each $H_k$ is real symmetric, so $[H_k,H_j]$ is real antisymmetric and has zero expectation in any real state. The first-order energy shift therefore vanishes, and

$$
E_{\text{eff}}-E_0=O(\Delta t^2)\quad\text{for both the first-order and the Strang formula.}
$$

The operator-norm error of $S_1$ is still $O(\Delta t^2)$ per step, i.e. first-order globally ([[simulation-of-quantum-systems]]). It affects eigenvectors and dynamics, not this eigenvalue. Checked for H₂: the first-order correction operator has expectation below $10^{-12}$ in the FCI ground state.

**When the two formulas coincide.** If the terms form two groups $A$ and $B$, each internally commuting, then $S_1\simeq e^{-iA\Delta t}e^{-iB\Delta t}$ and $S_2=e^{-iA\Delta t/2}e^{-iB\Delta t}e^{-iA\Delta t/2}=e^{iA\Delta t/2}S_1e^{-iA\Delta t/2}$. The two are similar matrices with the same eigenvalues, so QPE gives the same energy. H₂/STO-3G is such a case:

- **group A:** 11 diagonal terms, the identity and the $Z$-type strings;
- **group B:** 4 off-diagonal $XXYY$-type terms, which commute with each other.

The term order used here (some $Z$ terms, then the four $XY$ terms, then the rest) reduces to the grouped form by a cyclic similarity. Verified: identical eigenvalues to $10^{-10}$.

## Measured Trotter energy errors

$E_{\text{eff}}-E_{\text{FCI}}$ is computed from the eigenvector of the Trotter unitary with largest overlap with the exact ground state. STO-3G, Pauli terms in the order produced by the Jordan–Wigner transform. Errors in m$E_h$:

| $\Delta t$ ($E_h^{-1}$) | H₂, 0.735 Å (4 qubits, 15 terms), 1st / 2nd | H₄ chain, 1.0 Å (8 qubits, 185 terms), 1st / 2nd | LiH, 1.6 Å, frozen 1s (10 qubits, 276 terms), 1st / 2nd |
|---:|---:|---:|---:|
| 0.40 | +0.683 / +0.683 | +0.904 / +2.309 | −2.057 / +1.304 |
| 0.20 | +0.170 / +0.170 | +0.222 / +0.576 | −0.541 / +0.329 |
| 0.10 | +0.0424 / +0.0424 | +0.0553 / +0.1440 | −0.137 / +0.0825 |
| 0.05 | +0.0106 / +0.0106 | +0.0138 / +0.0360 | −0.0344 / +0.0206 |
| observed order (0.1 → 0.05) | 2.00 / 2.00 | 2.00 / 2.00 | 2.00 / 2.00 |

Observations:

- **Both formulas are second order in the energy**, as argued. For H₄ the "higher-order" Strang formula is *worse* by a factor of about 2.6, and for LiH the two have opposite signs. Their prefactors differ, not their order. The second-order formula is not automatically the better choice for energies.
- **The sign varies.** Trotter error is not variational: it can push the energy above or below FCI.
- **Overlap of the Trotter eigenvector** with the exact ground state is at least 0.988 at $\Delta t=0.4$ and at least 0.9998 at $\Delta t=0.05$ in all cases. The state QPE prepares is close to the true one.
- **Symmetry.** Splitting a number-conserving operator into individual Pauli strings breaks particle-number conservation of each factor. The effect is $O(\Delta t^2)$ and is included in the numbers above. Grouping terms into number-conserving fermionic pairs avoids it.

**Step size for chemical accuracy.** Fitting $|E_{\text{eff}}-E_0|=C\Delta t^2$ at $\Delta t=0.05$ and solving for 1.6 m$E_h$:

| | first order | Strang |
|---|---:|---:|
| H₂ | 0.615 | 0.615 |
| H₄ | 0.538 | 0.333 |
| LiH (frozen core) | 0.341 | 0.440 |

All in $E_h^{-1}$. In practice the Trotter error should be a fraction of the total error budget, so steps of half these sizes or smaller would be used.

## What this costs

For H₂ with the 1-norm window of [[qpe-for-molecular-energies]], take $\tau=\pi/\lambda=1.658\,E_h^{-1}$ and $t=12$ readout bits, a grid of 0.925 m$E_h$:

1. The controlled powers apply $U$ a total of $2^{12}-1=4095$ times.
2. Total evolution time is $4095\tau\approx6790\,E_h^{-1}$.
3. With $\Delta t\le0.615$, each application of $U$ needs $\lceil\tau/\Delta t\rceil=3$ steps, so about 12,300 Trotter steps in all.
4. Each step has 14 non-identity Pauli exponentials, giving about $1.7\times10^5$ in total, each with its own CNOT ladder and controlled by the ancilla.

For larger molecules the number of terms grows as $O(N^4)$, and the step needed for a fixed energy error shrinks. The Trotter route therefore becomes expensive quickly. This is why the leading fault-tolerant estimates use qubitization instead ([[qpe-cost-and-resource-estimates]]).

**Tighter error bounds.** Generic norm bounds on Trotter error can overestimate the observed error by orders of magnitude. Childs et al. derived commutator-scaling bounds that are much closer to observed errors. Measured energy errors like those above, extrapolated from small cases, are commonly used to choose step sizes in practice.

## Source

- Product formulas and BCH: Nielsen and Chuang (2010), Sec. 4.7.2, Eqs. (4.103)–(4.106), pp. 207–209. In this notebook: [[simulation-of-quantum-systems]].
- A. M. Childs, Y. Su, M. C. Tran, N. Wiebe and S. Zhu, "Theory of Trotter error with commutator scaling", *Phys. Rev. X* **11**, 011020 (2021), doi:10.1103/PhysRevX.11.011020.
- The vanishing first-order energy shift for real Hamiltonians, the H₂ similarity argument, all tables and the cost arithmetic are my analysis, computed in `qcchem/part6_ch4_qpe.py` (section C).
