---
id: adapt-vqe
title: ADAPT-VQE - growing the ansatz one operator at a time by energy gradient
summary: ADAPT-VQE builds the circuit from a pool of anti-Hermitian generators. At each step it measures every pool gradient ∂E/∂θ = ⟨ψ|[H, A_m]|ψ⟩, appends the largest as e^{θA}, and re-optimizes all parameters. Statevector simulations here use a pool of spin-orbital singles and doubles. H₄ chain (1.5 Å): chemical accuracy after 10 operators, against 26 for single-step UCCSD. H₆ chain (1.5 Å): UCCSD stays 4.7–4.8 mEh above FCI with 117 parameters, while ADAPT reaches 0.15 mEh at the usual gradient threshold and chemical accuracy after 77 operators (59 distinct). LiH: ADAPT matches UCCSD's 0.011 mEh with 34 operators. CCSD and CCSD(T) fall 1.5–6.5 mEh below FCI for the stretched chains. Caveats: the standard stopping rule |g| < 10⁻³ left H₄ 1.44 mEh above FCI, and H₆ needed about 2×10⁴ measured pool gradients.
status: in-progress
kind: algorithm
level: advanced
tags: [VQE, ADAPT-VQE, ansatz, UCCSD, operator-pool, gradient, strong-correlation]
prerequisites: [vqe-ansatze, variational-quantum-eigensolver, coupled-cluster-second-quantization]
related: [pauli-measurement-and-grouping, error-mitigation-for-vqe, lucj-ansatz, sample-based-quantum-diagonalization, perturbative-triples-cc2-cc3]
order: 40
date: 2026-11-17
---

## Overview

A fixed ansatz such as UCCSD ([[vqe-ansatze]]) includes every excitation whether it matters or not, and a single Trotter step of it is not exact. ADAPT-VQE (Grimsley, Economou, Barnes and Mayhall 2019) lets the molecule choose: the circuit grows one operator at a time, each time adding the generator that lowers the energy fastest. This note states the algorithm, derives the selection gradient, and compares ADAPT with single-step UCCSD, CCSD and CCSD(T) on weakly and strongly correlated systems.

**Notation.**
- Spin orbitals in the interleaved order; occupied $i,j$; virtual $a,b$.
- Jordan–Wigner qubit operators.
- A pool generator $\hat A_m=\hat\tau_m-\hat\tau_m^\dagger$, with $\hat\tau_m=a_a^\dagger a_i$ (single) or $a_a^\dagger a_b^\dagger a_ja_i$ (double), spin-conserving. $\hat A_m$ is anti-Hermitian, so $e^{\theta\hat A_m}$ is unitary.

## The algorithm

Starting from $|\psi^{(0)}\rangle=|\text{HF}\rangle$ with no parameters:

1. **Gradients.** For every pool operator, measure

    $$
    g_m=\frac{\partial}{\partial\theta}\langle\psi^{(n)}|e^{-\theta\hat A_m}\hat He^{\theta\hat A_m}|\psi^{(n)}\rangle\Big|_{\theta=0}=\langle\psi^{(n)}|[\hat H,\hat A_m]|\psi^{(n)}\rangle .
    $$

    This is the derivative for appending $e^{\theta\hat A_m}$ as the last gate. It follows from $(e^{\theta\hat A})^\dagger=e^{-\theta\hat A}$. With real wave functions and a real antisymmetric $\hat A_m$, $g_m=2\langle\psi|\hat H\hat A_m|\psi\rangle$.
2. **Stop** if $\|\mathbf g\|<\varepsilon_g$.
3. **Grow.** Append $e^{\theta_{n+1}\hat A_{m^*}}$ with $m^*=\arg\max|g_m|$ and $\theta_{n+1}=0$. Operators may be chosen again.
4. **Re-optimize** all $n+1$ parameters (warm start from the previous values), then return to step 1.

**Exact exponentials.** For a fermionic excitation $\hat\tau^2=0$, and $\hat A=\hat\tau-\hat\tau^\dagger$ satisfies $\hat A^3=-\hat A$ (checked for every pool operator). Hence

$$
e^{\theta\hat A}=1+\sin\theta\,\hat A+(1-\cos\theta)\,\hat A^2 ,
$$

a rotation between a determinant and its excited partner. The simulations below use this form. On hardware, each $e^{\theta\hat A}$ becomes a short product of commuting Pauli exponentials: the 8 strings of a double excitation are found in [[error-mitigation-for-vqe]].

**Gradients of the whole circuit.** For $|\psi\rangle=U_n\cdots U_1|\text{HF}\rangle$, $\partial E/\partial\theta_k=2\langle\psi|\hat H\,U_n\cdots U_{k+1}\hat A_kU_k\cdots U_1|\text{HF}\rangle$. The script evaluates it in one forward and one backward sweep. On hardware it costs two energy evaluations per parameter with the parameter-shift rule ([[variational-quantum-eigensolver]]).

## Results

Statevector simulation in the $(N_\alpha,N_\beta)$ sector, STO-3G, RHF orbitals. The pool is all spin-conserving occupied→virtual singles and doubles. BFGS optimization to gradient $10^{-8}$. UCCSD is one Trotter step containing every pool operator once, optimized from zero, with the operators in two orders (singles applied first, or doubles first). Errors are relative to FCI, in m$E_h$:

| system | qubits | pool | HF | CCSD | CCSD(T) | UCCSD (singles first / doubles first) | ADAPT at $\|\mathbf g\|<10^{-3}$ | ADAPT at $\|\mathbf g\|<10^{-4}$ |
|---|---:|---|---:|---:|---:|---|---|---|
| H₄ chain, 1.5 Å | 8 | 26 (8 S, 18 D) | 167.0 | −1.47 | −2.07 | 1.380 / 1.437 | 1.437 (12 ops) | $10^{-12}$ (20 ops, 14 distinct) |
| LiH, 1.6 Å | 12 | 92 (16 S, 76 D) | 20.46 | 0.011 | 0.002 | 0.0107 / 0.0106 | 0.0107 (33 ops) | 0.0107 (34 ops) |
| H₆ chain, 1.5 Å | 12 | 117 (18 S, 99 D) | 245.4 | −4.29 | −6.48 | 4.811 / 4.699 | 0.151 (124 ops) | 0.006 (168 ops, 59 distinct) |

ADAPT error, in m$E_h$, after a given number of operators:

| operators | 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| H₄ | 122.6 | 88.2 | 22.2 | 4.39 | 0.204 | | | |
| LiH | 5.89 | 3.98 | 2.12 | 0.559 | 0.064 | 0.011 | | |
| H₆ | 215.8 | 199.8 | 151.9 | 67.2 | 42.9 | 15.3 | 3.08 | 0.128 |

Chemical accuracy (1.6 m$E_h$) is reached after 10 operators for H₄, 5 for LiH, and 77 for H₆.

**Reading the results.**
- **Strong correlation separates the methods.** In the stretched H₆ chain, single-step UCCSD is stuck 4.7–4.8 m$E_h$ above FCI with all 117 parameters. ADAPT, which may reuse operators, goes below chemical accuracy and on to 0.006 m$E_h$. The repeated operators give it an effectively multi-step (and differently ordered) product. Of the 168 operators, only 59 are distinct.
- **Coupled cluster overshoots.** CCSD and CCSD(T) are not variational and land 1.5–6.5 m$E_h$ *below* FCI for both chains, the familiar breakdown for stretched bonds ([[perturbative-triples-cc2-cc3]]). VQE energies with any ansatz remain upper bounds.
- **Weak correlation is easy for everything.** For LiH at equilibrium, CCSD(T), UCCSD and ADAPT all agree with FCI to about 0.01 m$E_h$. ADAPT's advantage there is depth: 5 operators reach chemical accuracy.
- **Operator order matters a little.** Reordering the single Trotter step changes the UCCSD energy by 0.06–0.11 m$E_h$ in the chains.
- **The stopping rule is not an error bound.** At the commonly used $\|\mathbf g\|<10^{-3}$, ADAPT on H₄ stopped 1.44 m$E_h$ above FCI. Continuing to $10^{-4}$ reached FCI exactly with 8 more operators.

## Costs

- **Gradient measurements.** Every iteration measures all pool gradients. That is 546 for H₄ and about $2\times10^4$ for H₆ at $\|\mathbf g\|<10^{-4}$, each an expectation value with the measurement cost of [[pauli-measurement-and-grouping]]. The commutators $[\hat H,\hat A_m]$ can be grouped and measured together, but the pool scales as $O(M^4)$ for fermionic doubles.
- **Re-optimization.** Each step re-optimizes all parameters, with the full measurement cost of every energy and gradient evaluation.
- **Circuit depth.** ADAPT circuits are shorter than UCCSD for the same accuracy in the weakly correlated case, but grow long for strong correlation: H₆ needs 77 fermionic excitations for chemical accuracy. Each double excitation costs 8 Pauli exponentials, or fewer with dedicated circuits. Qubit pools (single Pauli strings) and qubit-excitation pools give shallower circuits per operator at the cost of more operators.
- **Noise.** None of this includes noise. Long ADAPT circuits accumulate gate errors exactly as in [[error-mitigation-for-vqe]].

## Source

- H. R. Grimsley, S. E. Economou, E. Barnes and N. J. Mayhall, "An adaptive variational algorithm for exact molecular simulations on a quantum computer", *Nat. Commun.* **10**, 3007 (2019), doi:10.1038/s41467-019-10988-2.
- J. Tilly et al., *Phys. Rep.* **986**, 1 (2022), Sec. 6.3.1 (ADAPT-VQE and variants).
- CCSD and CCSD(T) from PySCF; all numbers are computed in `qcchem/part6_ch3_vqe.py` (section B).
