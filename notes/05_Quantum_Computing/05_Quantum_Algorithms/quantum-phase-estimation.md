---
id: quantum-phase-estimation
title: Quantum phase estimation
summary: Given controlled-U^{2^j} gates and an eigenstate U|u⟩ = e^{2πiφ}|u⟩, phase estimation writes φ into a t-qubit register in four steps. Hadamards; controlled powers that kick back e^{2πiφk} onto |k⟩; the inverse QFT; measurement. If φ has an exact t-bit expansion the result is exact. Otherwise the nearest t-bit value occurs with probability ≥ 4/π² ≈ 0.405 (verified; my addition), and P(|m−b| > e) ≤ 1/(2(e−1)) (N&C 5.34, verified). An n-bit estimate with success probability 1−ε needs t = n + ⌈log₂(2 + 1/(2ε))⌉ qubits, e.g. t = 7 for n = 4, ε = 0.1, where the worst observed success was 0.975. A non-eigenstate input returns eigenphase φ_u with probability ≈ |⟨u|ψ⟩|². With U = e^{iHτ} this is an energy measurement; for a random 4×4 Hamiltonian all four energies are recovered to within one grid step. This is the route to chemistry energies on fault-tolerant hardware.
status: in-progress
kind: algorithm
level: intermediate
tags: [phase-estimation, qpe, eigenvalue, inverse-qft, phase-kickback, energy-estimation, hamiltonian-simulation, nielsen-chuang]
prerequisites: [quantum-fourier-transform, measurement-in-quantum-circuits, controlled-operations]
related: [simulation-of-quantum-systems, deutsch-jozsa-and-quantum-parallelism, full-ci, sample-based-quantum-diagonalization, variational-quantum-eigensolver]
order: 30
date: 2026-11-17
---

## Overview

Phase estimation answers: given a unitary $U$ and one of its eigenvectors $|u\rangle$, what is the eigenvalue $e^{2\pi i\varphi}$? For chemistry, take $U=e^{iH\tau}$ for an electronic Hamiltonian $H$. The eigenphases are then energies, and phase estimation becomes a projective measurement of the energy. It returns an eigenvalue of the exact Hamiltonian in the chosen orbital space, i.e. a full-CI energy ([[full-ci]]), with probability set by the overlap of the input state with that eigenstate. This is the main fault-tolerant algorithm for electronic structure, and the benchmark that near-term methods such as VQE and SQD approximate.

## The algorithm

**Inputs.**
- A black box that performs controlled-$U^{2^j}$ for $j=0,\dots,t-1$.
- An eigenstate $|u\rangle$ with $U|u\rangle=e^{2\pi i\varphi}|u\rangle$, where $0\le\varphi<1$.
- A $t$-qubit register in $|0\rangle$.

**Steps.**

1. **Superpose.** Apply $H^{\otimes t}$ to the register: $2^{-t/2}\sum_{k=0}^{2^t-1}|k\rangle|u\rangle$.
2. **Kick back.** Register qubit $j$ controls $U^{2^{t-j}}$. Each control picks up the phase $e^{2\pi i\varphi2^{t-j}}$, because $|u\rangle$ is an eigenvector (phase kickback, [[controlled-operations]]). Together,
$$
\frac1{2^{t/2}}\sum_{k=0}^{2^t-1}e^{2\pi i\varphi k}|k\rangle\,|u\rangle
=\frac1{2^{t/2}}\big(|0\rangle+e^{2\pi i2^{t-1}\varphi}|1\rangle\big)\cdots\big(|0\rangle+e^{2\pi i2^0\varphi}|1\rangle\big)|u\rangle .
$$
3. **Inverse QFT** on the register.
4. **Measure** the register. The result $m$ gives the estimate $\tilde\varphi=m/2^t$.

Step 2 is a Hadamard test with $t$ ancillas and doubling powers ([[measurement-in-quantum-circuits]]). Step 3 turns the phase pattern into bits: if $\varphi=0.\varphi_1\cdots\varphi_t$ exactly, the register state is precisely the product form of $\mathrm{QFT}|\varphi_1\cdots\varphi_t\rangle$ ([[quantum-fourier-transform]]). The inverse QFT then gives $|\varphi_1\cdots\varphi_t\rangle$ with certainty, as checked for several exact phases with $t=5$.

**Cost.** $O(t^2)$ gates for the inverse QFT, plus the controlled powers. These dominate: $U^{2^{t-1}}$ means evolving for time $2^{t-1}\tau$. Unless $U$ has special structure, $t$ bits of precision cost $\sim2^t$ applications of $U$. This is the Heisenberg limit: precision $\epsilon$ for total evolution time $\sim1/\epsilon$.

## Performance when φ is not a t-bit number

Let $b$ be the integer with $b/2^t$ the best $t$-bit approximation below $\varphi$, and $\delta=\varphi-b/2^t\in[0,2^{-t})$. Applying the inverse QFT gives amplitudes

$$
\alpha_l=\frac1{2^t}\,\frac{1-e^{2\pi i(2^t\delta-l)}}{1-e^{2\pi i(\delta-l/2^t)}}
$$

for outcome $m=b+l\pmod{2^t}$ (N&C Eq. 5.26), a sinc-like peak around $\varphi$. Two bounds:

- **Nearest value.** The closest $t$-bit value is obtained with probability at least $4/\pi^2\approx0.405$. The worst case found numerically over 2000 phases with $t=6$ was 0.4058, at phases halfway between grid points. This bound is my addition; Nielsen and Chuang work with the tail bound below.
- **Tails (N&C Eqs. 5.27–5.34).** Using $|1-e^{i\theta}|\ge2|\theta|/\pi$ on $[-\pi,\pi]$,
$$
P\big(|m-b|>e\big)\le\frac{1}{2(e-1)} .
$$
Verified for 300 random phases with $t=8$ and $e=2,3,5,10$.

**How many qubits.** For accuracy $2^{-n}$ choose $e=2^{t-n}-1$. Success probability $1-\epsilon$ then requires

$$
t=n+\Big\lceil\log_2\Big(2+\frac1{2\epsilon}\Big)\Big\rceil .
$$

For $n=4$ and $\epsilon=0.1$ this gives $t=7$. Over 300 random phases the worst success probability was 0.975, above the required 0.9. The extra $\log(1/\epsilon)$ qubits buy confidence, not resolution.

## Inputs that are not eigenstates

In practice the eigenstate is unknown, which is the whole point for chemistry. Expand the input as $|\psi\rangle=\sum_uc_u|u\rangle$. By linearity the algorithm produces $\sum_uc_u|\tilde\varphi_u\rangle|u\rangle$. Measuring the register returns an estimate of $\varphi_u$ with probability $|c_u|^2$, up to the error above (Exercise 5.8), and leaves the system approximately in $|u\rangle$. Phase estimation is a projective measurement of $U$ in its eigenbasis.

!!! example "Energies of a random 4×4 Hamiltonian"
    Use $U=e^{iH\tau}$, with $\tau$ chosen so that all phases $E_u\tau/2\pi$ fit in one period, $t=9$ register qubits, and a random input state.

    | | $u=1$ | $u=2$ | $u=3$ | $u=4$ |
    |---|---:|---:|---:|---:|
    | exact $E_u$ | −3.5600 | −1.8813 | 0.0593 | 2.6765 |
    | read from peak | −3.5617 | −1.8798 | 0.0565 | 2.6713 |
    | $\lvert c_u\rvert^2$ | 0.1216 | 0.1426 | 0.1971 | 0.5387 |
    | weight within ±1 bin | 0.1194 | 0.1407 | 0.1883 | 0.4761 |

    The energy grid spacing is $2\pi/(\tau2^t)=0.0141$, and every energy is recovered to within one grid step. The weight near each peak tracks $|c_u|^2$; the rest sits in the sinc tails.

**For electronic structure.** To obtain the ground-state energy:

- **Prepare a state with large overlap $|c_0|^2$.** Hartree–Fock, a CASSCF state or a VQE state is typical. The expected number of repetitions to land in the ground state is $1/|c_0|^2$. Overlap shrinks with system size in general, which is the main open problem for QPE in chemistry.
- **Implement $e^{iH\tau}$.** This uses Trotterization of the Jordan–Wigner Hamiltonian ([[simulation-of-quantum-systems]], [[jordan-wigner-mapping]]) or more advanced block-encoding methods (planned, Part 6).
- **Choose $\tau$ and $t$.** These are set by the energy range and the precision wanted. Chemical accuracy, about 1.6 m$E_h$, needs total evolution time of order $10^3\,E_h^{-1}$ (my order-of-magnitude estimate).

## Source

Nielsen and Chuang, *Quantum Computation and Quantum Information* (10th anniversary ed., Cambridge University Press, 2010):

- Sec. 5.2, pp. 221–223: the procedure, Figures 5.2–5.3, Eqs. (5.20)–(5.21); Exercise 5.7.
- Sec. 5.2.1, pp. 223–225: performance, Eqs. (5.22)–(5.35); non-eigenstate inputs; the algorithm box; Exercises 5.8–5.9.

Page numbers are those printed in the book. The $4/\pi^2$ bound, the Hamiltonian example and the chemistry remarks are my additions. All checks are in `nielsen_chuang/part5_batch7.py` (section F).
