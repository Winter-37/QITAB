---
id: qpe-for-molecular-energies
title: Phase estimation for molecular energies - energy window, readout resolution and success probability
summary: To measure a molecular energy, run phase estimation on U = e^{−i(H−E_ref)τ}. Choose E_ref and τ so the relevant spectrum maps one-to-one onto phases in [0,1). A safe a-priori window uses the Pauli 1-norm, E ∈ [c_I − λ, c_I + λ], so τ = π/λ and the readout grid is 2λ/2^t. The run returns eigenvalue E_u with probability |⟨u|Φ⟩|² for input |Φ⟩; it is an energy measurement in the Hamiltonian's eigenbasis, not a variational estimate. Worked for H₂/STO-3G with the HF input. At 0.735 Å, λ = 1.8945 Eh and |⟨HF|FCI⟩|² = 0.9876; t = 12 bits give a 0.925 mEh grid, the most likely readout lies 0.42 mEh from FCI, and 0.964 of the probability sits within ±8 bins. At 2.0 Å the overlap is 0.712, so the ground state is found only about 71% of the time. Only the ground state and the doubly excited singlet carry weight, as symmetry dictates.
status: in-progress
kind: algorithm
level: intermediate
tags: [phase-estimation, qpe, molecular-energy, energy-window, one-norm, readout-resolution, overlap, h2, jordan-wigner]
prerequisites: [quantum-phase-estimation, jordan-wigner-mapping, full-ci]
related: [iterative-phase-estimation, trotter-error-in-qpe-energies, qpe-state-preparation-and-overlap, qpe-cost-and-resource-estimates, molecular-hamiltonian-in-the-mo-basis, variational-quantum-eigensolver]
order: 10
date: 2026-11-17
---

## Overview

[[quantum-phase-estimation]] measures an eigenphase of a unitary. For chemistry the unitary is time evolution under the qubit Hamiltonian of a molecule ([[jordan-wigner-mapping]]), and the eigenphases encode energies. This note covers the set-up that turns the generic algorithm into an energy measurement:

- how to choose the evolution time $\tau$ and a reference energy;
- what the readout grid is;
- what the output distribution looks like for a realistic, non-eigenstate input.

The worked example is a full classical simulation for H₂/STO-3G.

**Conventions.** Atomic units, $\hbar=1$. $H=\sum_kc_kP_k$ is the Jordan–Wigner Hamiltonian, with identity coefficient $c_I$ and Pauli 1-norm $\lambda=\sum_{P_k\ne I}|c_k|$. $|u\rangle$, $E_u$ are its eigenpairs in the $N$-electron sector, $E_0$ the ground state. $|\Phi\rangle$ is the input state, with $c_u=\langle u|\Phi\rangle$.

## From energies to phases

Run phase estimation on

$$
U=e^{-i(H-E_{\text{ref}})\tau},\qquad U|u\rangle=e^{2\pi i\varphi_u}|u\rangle,\qquad
\varphi_u=\frac{(E_{\text{ref}}-E_u)\,\tau}{2\pi}\ \bmod 1 .
$$

A $t$-bit readout $m$ gives the energy estimate

$$
\tilde E=E_{\text{ref}}-\frac{2\pi m}{2^t\tau}.
$$

Two requirements fix $E_{\text{ref}}$ and $\tau$:

1. **No wrapping.** Every eigenvalue that can appear must map into one period, $0\le(E_{\text{ref}}-E_u)\tau<2\pi$. Otherwise a high-lying state could alias onto the ground-state phase.
2. **Resolution.** The grid spacing $\Delta E=2\pi/(2^t\tau)$ must be below the target precision.

**A safe window without prior knowledge.** Since $\|H-c_I\|\le\lambda$, all eigenvalues lie in $[c_I-\lambda,\,c_I+\lambda]$. Choosing

$$
E_{\text{ref}}=c_I+\lambda,\qquad \tau=\frac{2\pi}{2\lambda}=\frac\pi\lambda,\qquad \Delta E=\frac{2\lambda}{2^t}
$$

maps the whole window onto $[0,1)$. This is wasteful, since the window is much wider than the physically relevant range. Narrowing it with a classical estimate, such as HF or CCSD energies and an estimate of the gap, increases $\tau$ and improves resolution for the same $t$, but must be done safely.

**What each controlled power costs.** The $j$th register qubit controls $U^{2^j}$, which is evolution for time $2^j\tau$. Total simulated time is about $(2^t-1)\tau$, so halving $\Delta E$ doubles the time. This Heisenberg-limited scaling (cost $\propto1/\epsilon$) is the defining advantage of QPE over sampling expectation values, whose cost scales as $1/\epsilon^2$ ([[concentration-inequalities-and-sampling]]).

## What the output means

Because $U$ is diagonal in the eigenbasis of $H$, a run on $|\Phi\rangle=\sum_uc_u|u\rangle$ is equivalent to:

1. choosing eigenstate $u$ with probability $|c_u|^2$;
2. running phase estimation on that eigenstate.

So:

- **The readout is an eigenvalue, not an average.** Each run returns an estimate of a single $E_u$, never the expectation value $\langle\Phi|H|\Phi\rangle$. The ground-state energy is obtained exactly, to grid precision, in the fraction $|c_0|^2$ of runs. There is no variational bias.
- **The system collapses** to approximately $|u\rangle$, so a successful run also prepares the ground state for later measurements of properties.
- **Repetitions** needed to see the ground state at least once scale as $1/|c_0|^2$. The lowest frequently observed peak is taken as $E_0$. Overlap is therefore the central question ([[qpe-state-preparation-and-overlap]]).
- **Symmetry selects the sector.** $H$ conserves electron number and $S_z$, and spatial symmetries too. An input with definite quantum numbers can only return states in the same sector. HF has the ground state's symmetry by construction, which removes most of the spectrum from the output.

## Worked example: H₂/STO-3G

The qubit Hamiltonian is the 15-term operator of [[jordan-wigner-mapping]]: 4 qubits, spin orbitals in the order $(1\sigma_g\alpha,1\sigma_g\beta,1\sigma_u\alpha,1\sigma_u\beta)$, input $|\text{HF}\rangle=|1100\rangle$. The 1-norm window above is used; the evolution is exact, with no Trotter error. The outcome distribution is computed exactly from the eigen-decomposition and the phase-estimation line shape (N&C Eq. 5.26).

**Weights.** Only two of the six $N=2$ eigenstates have nonzero overlap with HF: the ground state and the doubly excited $^1\Sigma_g^+$ state. All other $N=2$ states differ in spin or spatial symmetry.

| | $R=0.735$ Å | $R=2.0$ Å |
|---|---:|---:|
| $E_{\text{FCI}}$ ($E_h$) | −1.137306 | −0.948641 |
| $\lambda$ ($E_h$) | 1.894493 | 1.057663 |
| $c_I$ ($E_h$) | −0.090579 | −0.533936 |
| $\lvert c_0\rvert^2=\lvert\langle\text{HF}\vert\text{FCI}\rangle\rvert^2$ | 0.987560 | 0.711909 |
| weight on the $1\sigma_u^2$-dominated state | 0.012440 | 0.288091 |

**Readout at equilibrium (0.735 Å).**

| $t$ | grid $2\lambda/2^t$ (m$E_h$) | most likely $\tilde E$ | error vs FCI (m$E_h$) | $P$(ground, ±1 bin) | $P$(ground, ±8 bins) |
|---:|---:|---:|---:|---:|---:|
| 6 | 59.20 | −1.156231 | 18.93 | 0.892 | 0.972 |
| 8 | 14.80 | −1.141431 | 4.13 | 0.909 | 0.974 |
| 10 | 3.70 | −1.137730 | 0.42 | 0.971 | 0.985 |
| 12 | 0.925 | −1.137730 | 0.42 | 0.850 | 0.964 |

**Readout when stretched (2.0 A), $t=12$.** The grid is 0.516 m$E_h$, the readout is $-0.948635$ (0.006 m$E_h$ from FCI), and $P$(ground) is 0.712 within both ±1 and ±8 bins.

What the numbers show:

- **The error is set by the grid.** With 12 bits the readout is within one grid step (0.925 m$E_h$) of FCI, i.e. within chemical accuracy. At $t=10$ and 12 the same readout appears because the $t=12$ grid refines the $t=10$ one and the phase sits close to a $t=10$ grid point.
- **The ±1-bin weight fluctuates with $t$.** When the true phase falls between grid points, the line shape spreads (the $4/\pi^2$ worst case of [[quantum-phase-estimation]]). Summed over ±8 bins, the ground-state weight recovers $|c_0|^2$ to within about 0.02.
- **Overlap controls success.** Stretching to 2.0 Å drops the success fraction from about 0.97–0.99 to about 0.71, exactly the HF overlap. The other 29% of runs return the doubly excited state. At this distance its energy is well separated, so the outcome is easily recognized as not the ground state.
- **The 1-norm window is loose.** For H₂ at 0.735 Å it spans $2\lambda=3.79\,E_h$, while the two relevant energies are only about $1.6\,E_h$ apart. A window matched to that range would be about 2.4 times narrower, giving the same resolution with about 2.4 times less total evolution time, a saving of a little over one bit.

## Relation to other chapters

- **VQE and SQD** ([[variational-quantum-eigensolver]], [[sample-based-quantum-diagonalization]]) give upper bounds from a state or subspace. QPE gives the exact eigenvalue in the chosen basis, but needs deep, fault-tolerant circuits.
- **The Hamiltonian it measures** is the second-quantized operator in a finite orbital basis, usually an active space. QPE returns FCI (or CASCI) energies, not the basis-set limit ([[molecular-hamiltonian-in-the-mo-basis]], [[frozen-core-and-active-space-hamiltonians]]).
- **In practice**, $e^{-iH\tau}$ is implemented approximately, by Trotterization ([[trotter-error-in-qpe-energies]]) or by qubitization ([[qpe-cost-and-resource-estimates]]). Ancilla count can be reduced to one ([[iterative-phase-estimation]]).

## Source

- Phase estimation and its output distribution: Nielsen and Chuang, *Quantum Computation and Quantum Information* (10th anniversary ed., 2010), Secs. 5.2–5.2.1, pp. 221–225, Eq. (5.26) and Exercise 5.8.
- First simulated application to molecular energies (H₂O and LiH, with a recursive phase-estimation scheme and adiabatic state preparation): A. Aspuru-Guzik, A. D. Dutoi, P. J. Love and M. Head-Gordon, *Science* **309**, 1704 (2005), doi:10.1126/science.1113479.
- The 1-norm energy window is a standard bound ($\|\sum c_kP_k\|\le\sum|c_k|$). All numbers are computed in `qcchem/part6_ch4_qpe.py` (section A), using PySCF integrals and the notebook's Jordan–Wigner conventions.
