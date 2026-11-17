---
id: iterative-phase-estimation
title: Iterative (single-ancilla) phase estimation
summary: Phase estimation with one ancilla, reused t times, reading the bits of φ from least to most significant. Round k applies H, controlled-U^{2^{k−1}}, a feedback rotation R_z(ω_k) built from the bits already measured, then H, and measures. The feedback is the inverse QFT done semiclassically, so the output distribution is identical to textbook QPE (verified: total-variation distance ≤ 0.008 over 6 phases, 40,000 samples each). It needs one ancilla instead of t and no multi-qubit QFT, but requires mid-circuit measurement with feed-forward and t sequential rounds. For H₂ at 2.0 Å with an HF input, 400 simulated runs with t = 10 return the ground-state energy in 67% of runs (|c₀|² = 0.71), the rest returning the excited state. This was the scheme used in the 2005 simulated computation of H₂O and LiH energies.
status: in-progress
kind: algorithm
level: intermediate
tags: [iterative-phase-estimation, ipea, kitaev, single-ancilla, semiclassical-qft, feed-forward, mid-circuit-measurement]
prerequisites: [quantum-phase-estimation, measurement-in-quantum-circuits, qpe-for-molecular-energies]
related: [quantum-fourier-transform, trotter-error-in-qpe-energies, qpe-cost-and-resource-estimates]
order: 20
date: 2026-11-17
---

## Overview

Textbook phase estimation uses $t$ ancilla qubits and an inverse QFT. Early fault-tolerant devices will have few logical qubits, so the ancilla register matters. Iterative phase estimation (IPEA) needs **one** ancilla. It measures one bit per round and uses the bits already found to choose a phase correction for the next round.

Its origins are Kitaev's single-qubit eigenvalue-measurement procedure (1995) and the observation that the inverse QFT followed by measurement can be done "semiclassically", with classically controlled single-qubit rotations instead of controlled two-qubit gates. Dobšíček et al. (2007) gave the arbitrary-precision iterative form used here.

## The algorithm

Write the phase as $\varphi=0.\varphi_1\varphi_2\cdots\varphi_t$ in binary. With $|u\rangle$ an eigenstate of $U$, start the system in $|u\rangle$ and repeat for $k=t,t-1,\dots,1$:

1. Prepare the ancilla in $|0\rangle$ and apply $H$.
2. Apply controlled-$U^{2^{k-1}}$. Phase kickback puts $e^{2\pi i\,2^{k-1}\varphi}$ on the ancilla's $|1\rangle$. Since $2^{k-1}\varphi=\varphi_1\cdots\varphi_{k-1}.\varphi_k\varphi_{k+1}\cdots$, only the fractional part $0.\varphi_k\varphi_{k+1}\cdots\varphi_t$ matters.
3. Apply $R_z(\omega_k)$, or equivalently a phase $e^{i\omega_k}$ on $|1\rangle$, with
$$
\omega_k=-2\pi\,(0.0\varphi_{k+1}\varphi_{k+2}\cdots\varphi_t),
$$
built from the bits already measured. This removes their contribution, leaving the phase $e^{i\pi\varphi_k}=\pm1$ when $\varphi$ is exact.
4. Apply $H$ and measure. The result is $\varphi_k$ with certainty if $\varphi$ has exactly $t$ bits. Otherwise $P(0)=\cos^2(\theta_k/2)$ with $\theta_k=2\pi2^{k-1}\varphi+\omega_k$.

The system register is never measured. It stays in $|u\rangle$ throughout, because every controlled power acts diagonally on it.

**Why it equals textbook QPE.** The inverse QFT ([[quantum-fourier-transform]]) is a sequence of Hadamards and controlled phases. Every controlled phase acts on a qubit whose value is about to be measured, and measurement commutes with control ([[measurement-in-quantum-circuits]]). So each controlled phase can be replaced by a classically controlled one after the controlling qubit is measured. Processing bits from least significant to most significant then lets one ancilla be reused. The output distribution is unchanged. Checked numerically: for 6 random phases and $t=6$, the empirical IPEA distribution (40,000 samples each) differs from the exact textbook line shape by total-variation distance at most 0.008, consistent with sampling noise. Exact $t$-bit phases are returned with certainty.

## Non-eigenstate input

With $|\Phi\rangle=\sum_uc_u|u\rangle$, every round acts diagonally on the system, so the statistics are again those of choosing $u$ with probability $|c_u|^2$ first. The first controlled power and ancilla measurement start to collapse the system onto eigenstates whose phases are consistent with the bits found so far.

!!! example "H₂/STO-3G at 2.0 Å, HF input, $t=10$, 1-norm window"
    400 simulated runs:

    - 67.2% returned an energy within two grid steps of $E_0$. The expected value is $|c_0|^2=0.712$; the difference is sampling noise plus the $\pm2$-bin cut.
    - The ground-state readouts cluster at $-0.949152$, compared with $E_{\text{FCI}}=-0.948641$. The grid step is 2.07 m$E_h$.
    - The remaining runs returned the doubly excited state.

## Trade-offs

| | textbook QPE | iterative PE |
|---|---|---|
| ancillas | $t$ | 1 |
| inverse QFT | $O(t^2)$ gates | single-qubit feedback rotations |
| circuit structure | one coherent circuit | $t$ rounds with mid-circuit measurement and classical feed-forward |
| total evolution time | $\approx(2^t-1)\tau$ | same |
| errors | spread over the register | an error in one bit corrupts all later feedback; rounds can be repeated and majority-voted |

The evolution cost is identical, because every power $U^{2^j}$ is still applied once. IPEA saves qubits, not time.

## Beyond IPEA

Single-ancilla schemes that estimate $\langle\Phi|e^{-iHt}|\Phi\rangle$ at many times $t$ with the Hadamard test, and then fit or Fourier-analyse the signal classically, are the basis of "early fault-tolerant" phase estimation. They tolerate shallower circuits at the cost of more repetitions. This is mentioned for orientation only; no specific method is derived or checked here.

## Source

- A. Yu. Kitaev, "Quantum measurements and the Abelian Stabilizer Problem", arXiv:quant-ph/9511026 (1995): the eigenvalue-measurement procedure on which iterative phase estimation is based.
- M. Dobšíček, G. Johansson, V. Shumeiko and G. Wendin, "Arbitrary accuracy iterative quantum phase estimation algorithm using a single ancillary qubit: A two-qubit benchmark", *Phys. Rev. A* **76**, 030306(R) (2007), doi:10.1103/PhysRevA.76.030306.
- A. Aspuru-Guzik, A. D. Dutoi, P. J. Love and M. Head-Gordon, *Science* **309**, 1704 (2005), doi:10.1126/science.1113479. Their recursive phase-estimation algorithm reduced the readout register from about 20 qubits to 4 for H₂O and LiH.
- Measurement commuting with control: Nielsen and Chuang (2010), Sec. 4.4, Exercise 4.35, p. 188.

All numbers are computed in `qcchem/part6_ch4_qpe.py` (section B).
