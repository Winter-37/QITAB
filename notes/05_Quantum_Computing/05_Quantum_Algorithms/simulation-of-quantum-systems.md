---
id: simulation-of-quantum-systems
title: Simulation of quantum systems - Trotter formulas and Pauli-string exponentials
summary: Simulating e^{−iHt} classically needs 2ⁿ amplitudes, while a quantum computer needs n qubits. For a local Hamiltonian H = Σ_k H_k, the Trotter formula (e^{−iAt/n}e^{−iBt/n})ⁿ → e^{−i(A+B)t}, Theorem 4.3, builds the evolution from simple pieces. The first-order step has error O(Δt²) per step, O(t²/n) overall, and the symmetric step O(Δt³) and O(t³/n²). Measured on a 3-qubit transverse-field Ising chain, the convergence orders are 1.00 and 2.00. Each term e^{−iΔt P} for a Pauli string P becomes single-qubit basis changes plus a CNOT parity ladder around one R_z. The ancilla circuit of Fig. 4.19 and the ancilla-free ladder are both verified, and Ex. 4.51 is solved for X₁Y₂Z₃. This is how Jordan–Wigner molecular Hamiltonians are simulated, and how U = e^{iHτ} is supplied to phase estimation.
status: in-progress
kind: algorithm
level: intermediate
tags: [hamiltonian-simulation, trotter, suzuki-trotter, strang-splitting, baker-campbell-hausdorff, pauli-strings, cnot-ladder, quantum-simulation, nielsen-chuang]
prerequisites: [controlled-operations, baker-campbell-hausdorff, functions-of-matrices]
related: [quantum-phase-estimation, jordan-wigner-mapping, universal-gate-sets, heisenberg-picture-and-time-translation, coupled-cluster-second-quantization]
order: 40
date: 2026-11-17
---

## Overview

Feynman's original motivation for quantum computers was that classical computers cannot efficiently simulate quantum mechanics: $n$ qubits need $2^n$ complex amplitudes, and an $n$-qubit density matrix needs $4^n-1$ real numbers (Exercise 4.46). A quantum computer represents the state natively. What remains is to apply $e^{-iHt}$ with a polynomial number of gates. For Hamiltonians that are sums of local terms, which include the qubit form of every molecular Hamiltonian, the **Trotter formula** does this. The resulting circuits supply the time evolution that phase estimation needs ([[quantum-phase-estimation]]).

## Local Hamiltonians and the Trotter formula

Let $H=\sum_{k=1}^LH_k$, with each $H_k$ acting on a few qubits and $L$ polynomial in $n$. Examples are the Ising model, the Hubbard model, and the Jordan–Wigner molecular Hamiltonian, which has $O(N^4)$ Pauli strings for $N$ spin orbitals ([[jordan-wigner-mapping]]). If the terms commuted, $e^{-iHt}=\prod_ke^{-iH_kt}$ (Exercise 4.47). They do not, but:

**Theorem 4.3 (Trotter).** For Hermitian $A,B$ and real $t$,

$$
\lim_{n\to\infty}\big(e^{iAt/n}e^{iBt/n}\big)^n=e^{i(A+B)t}.
$$

*Proof sketch.* $e^{iAt/n}e^{iBt/n}=I+i(A+B)t/n+O(1/n^2)$. Raising to the $n$th power and expanding binomially, the $O(1/n^2)$ terms contribute $O(1/n)$ in total, which vanishes in the limit.

**Error per step.** From Baker–Campbell–Hausdorff ([[baker-campbell-hausdorff]]),

$$
e^{(A+B)\Delta t}=e^{A\Delta t}e^{B\Delta t}e^{-\frac12[A,B]\Delta t^2}+O(\Delta t^3)\qquad\text{(N\&C Eq. 4.105, verified at }\Delta t=0.01),
$$

so the **first-order** step $e^{-iA\Delta t}e^{-iB\Delta t}$ has error $O(\Delta t^2)$, set by the commutator. The **symmetric (Strang)** step

$$
e^{-i(A+B)\Delta t}=e^{-iA\Delta t/2}e^{-iB\Delta t}e^{-iA\Delta t/2}+O(\Delta t^3)
$$

cancels the commutator term. For many terms, the palindromic product $e^{-iH_1\Delta t}\cdots e^{-iH_L\Delta t}e^{-iH_L\Delta t}\cdots e^{-iH_1\Delta t}=e^{-2iH\Delta t}+O(\Delta t^3)$ (Exercise 4.50). Its error divided by $\Delta t^3$ was 2.98 at both $\Delta t=0.01$ and $0.005$, as expected for third order.

**Global error.** Over total time $t$ in $n=t/\Delta t$ steps, local errors add (Box 4.1, [[universal-gate-sets]]). The first-order product has total error $O(t^2/n)$, approximately bounded by $t^2\|[A,B]\|/(2n)$, and the symmetric one $O(t^3/n^2)$.

!!! example "Three-qubit transverse-field Ising chain"
    $H=A+B$ with $A=\sum_qX_q$ and $B=Z_1Z_2+Z_2Z_3$, simulated for $t=1$:

    | steps $n$ | first-order error | symmetric error |
    |---:|---:|---:|
    | 4 | 0.2867 | 0.04502 |
    | 8 | 0.1398 | 0.01105 |
    | 16 | 0.06926 | 0.002749 |
    | 32 | 0.03450 | 0.000687 |
    | 64 | 0.01722 | 0.000172 |

    Errors are operator norms of $U_{\text{Trotter}}-e^{-iHt}$. The observed orders, $\log_2$ of successive ratios, approach 1.00 and 2.00. Higher-order Suzuki formulas continue the pattern at the cost of more exponentials per step.

**The algorithm (N&C).** Represent the system in $n=\mathrm{poly}(\log N)$ qubits. Choose a product formula and $\Delta t$ so the total error is below $\delta$. Apply the step $U_{\Delta t}$ repeatedly, $t_f/\Delta t$ times, starting from $|\psi_0\rangle$. The cost is polynomial in $n$, $t$ and $1/\delta$.

## Exponentiating a Pauli string

Any qubit Hamiltonian term is a Pauli string $P=\sigma_{c(1)}\otimes\cdots\otimes\sigma_{c(n)}$ times a real coefficient. Qubits carrying $I$ are left alone, and $X$ and $Y$ factors are rotated to $Z$ by single-qubit basis changes ($HZH=X$ and $(SH)Z(SH)^\dagger=Y$). That leaves $e^{-i\Delta t\,Z_1Z_2\cdots Z_k}$, which multiplies each basis state by $e^{\mp i\Delta t}$ according to the **parity** of its bits. So:

- **With an ancilla (N&C Figure 4.19).** CNOT each qubit onto an ancilla in $|0\rangle$, so the ancilla holds the parity. Apply $e^{-i\Delta tZ}$ to the ancilla, then uncompute with the same CNOTs. Verified for $Z_1Z_2Z_3$; the ancilla returns to $|0\rangle$.
- **Without an ancilla.** Use a CNOT ladder $1\to2\to\cdots\to k$ to accumulate the parity on qubit $k$, apply $R_z(2\Delta t)$ there, and reverse the ladder. Verified for $k=3$. This costs $2(k-1)$ CNOTs per term, and is how VQE and QPE circuits implement Jordan–Wigner terms.
- **Mixed strings (Exercise 4.51).** $e^{-i\Delta t\,X_1Y_2Z_3}=W\,e^{-i\Delta t\,Z_1Z_2Z_3}\,W^\dagger$ with $W=H\otimes SH\otimes I$. Verified.

For a molecular Hamiltonian with $O(N^4)$ terms, a Trotter step therefore costs $O(N^4)$ such blocks, each with up to $O(N)$ CNOTs from Jordan–Wigner strings. Grouping commuting terms, ordering them so ladders cancel, and using better encodings reduce this considerably. This is one reason the planned Part 6 chapters discuss Hamiltonian representations at length.

## Connections

- **Unitary coupled cluster.** The UCC ansatz $e^{T-T^\dagger}$ is implemented exactly the same way: Trotterize the anti-Hermitian generator into Pauli-string exponentials ([[coupled-cluster-second-quantization]], [[vqe-ansatze]]).
- **Phase estimation.** Controlled-$e^{iH\tau2^j}$ is the Trotterized evolution with every gate controlled. The Trotter error shifts the measured energies, so it must be kept below the target precision.
- **Fermions.** Particle statistics must be built into the mapping. Jordan–Wigner does this with $Z$ strings, which the parity ladder handles naturally.
- **Beyond Trotter.** Methods such as qubitization and linear combinations of unitaries achieve better scaling in precision. They are the subject of the planned Part 6 chapter on phase estimation.

## Source

Nielsen and Chuang, *Quantum Computation and Quantum Information* (10th anniversary ed., Cambridge University Press, 2010), Sec. 4.7, pp. 204–211:

- motivation and Exercise 4.46, pp. 204–205;
- local Hamiltonians, Eqs. (4.94)–(4.97); Exercises 4.47–4.48;
- Theorem 4.3, Eqs. (4.98)–(4.102);
- higher-order formulas, Eqs. (4.103)–(4.105);
- the algorithm box; Exercises 4.49–4.50 (Eq. 4.106);
- Box 4.2 (the 1D Schrödinger equation);
- the Pauli-string example, Eqs. (4.113)–(4.115), Figure 4.19, Exercise 4.51.

Page numbers are those printed in the book. The Ising example, the error estimate $t^2\|[A,B]\|/(2n)$ and the chemistry remarks are my additions. All checks are in `nielsen_chuang/part5_batch7.py` (section G).
