---
id: qpe-cost-and-resource-estimates
title: The cost of phase estimation for chemistry - the 1-norm λ, Trotter versus qubitization, and resource estimates
summary: QPE cost is (repetitions ≈ 1/|c₀|²) × (cost per run). In the qubitization framework, a run needs O(λ/ε) applications of a block encoding of H, where λ is the 1-norm of the Hamiltonian's coefficients and ε the target precision. λ is therefore the key figure of merit. Computed Pauli 1-norms (STO-3G unless noted): H₂ 1.89, LiH 12.3, H₂O 72.0 and N₂ 117.7 Eh. For H₂, λ rises from 1.89 (STO-3G) to 11.5 (6-31G) and 104.4 Eh (cc-pVDZ), so λ/ε at chemical accuracy runs from about 10³ to 10⁵. The number of Pauli terms grows as O(N⁴), from 15 to about 3000 for 20 qubits. Factorized representations (double factorization, THC) reduce the effective λ and the per-step cost. Lee et al. (2021) estimate that FeMoco needs about four million physical qubits and under four days on a surface-code machine with 1 µs cycles and 0.1% gate errors. Trotter costs grow faster and depend on commutator structure.
status: in-progress
kind: comparison
level: advanced
tags: [resource-estimation, one-norm, qubitization, block-encoding, linear-combination-of-unitaries, trotter, t-count, toffoli, femoco, tensor-hypercontraction, fault-tolerance]
prerequisites: [qpe-for-molecular-energies, trotter-error-in-qpe-energies, universal-gate-sets]
related: [qpe-state-preparation-and-overlap, molecular-hamiltonian-in-the-mo-basis, frozen-core-and-active-space-hamiltonians, jordan-wigner-mapping]
order: 50
date: 2026-11-17
---

## Overview

How long would phase estimation for a real molecule take on a fault-tolerant computer? The answer factorizes into:

- **repetitions:** about $1/|c_0|^2$, set by the input overlap ([[qpe-state-preparation-and-overlap]]);
- **cost per run:** the number of applications of the time-evolution primitive, times the gate cost of each.

On error-corrected hardware, Clifford gates are cheap and non-Clifford gates ($T$ or Toffoli) dominate ([[universal-gate-sets]]). Resource estimates therefore quote **$T$ or Toffoli counts** and **logical qubits**, then translate them into physical qubits and wall-clock time for a given error-correcting code. This note explains the central quantity, the 1-norm $\lambda$, computes it for small molecules, and summarizes how published estimates are structured.

## Two ways to implement the evolution

**Trotterization** ([[trotter-error-in-qpe-energies]]). The cost per run is (number of steps) × (number of terms) × (gates per Pauli exponential). The number of steps for fixed accuracy depends on nested commutators of the terms. Tight estimates need commutator bounds or numerical extrapolation (Childs et al. 2021). Each Pauli rotation by an arbitrary angle must itself be synthesized from many $T$ gates.

**Qubitization.** Write $H=\sum_kc_kU_k$ as a linear combination of unitaries (for example Pauli strings), with $\lambda=\sum_k|c_k|$. Two oracles are needed:

- PREPARE: $|0\rangle\mapsto\sum_k\sqrt{|c_k|/\lambda}\,|k\rangle$;
- SELECT: $|k\rangle|\psi\rangle\mapsto|k\rangle U_k|\psi\rangle$.

Together they block-encode $H/\lambda$. Low and Chuang showed that a "qubitized" walk operator built from them has eigenphases $\pm\arccos(E_u/\lambda)$. Phase estimation on the walk, rather than on $e^{-iH\tau}$, then gives the energies directly, with no Trotter error. Babbush et al. (2018) showed that sampling the eigenbasis this way takes $O(\lambda/\epsilon)$ walk steps. The full cost is

$$
\text{cost per run}\ \sim\ \frac{\lambda}{\epsilon}\times(\text{cost of one PREPARE + SELECT}).
$$

Two levers follow: make $\lambda$ small, and make the oracles cheap. The orbital count $N$ enters through both.

## λ for small molecules

Pauli 1-norms of the Jordan–Wigner Hamiltonian, excluding the identity term, in RHF canonical orbitals with all electrons:

| system | qubits | Pauli terms | $\lambda$ ($E_h$) | $\lambda/\epsilon$ at $\epsilon=1.6$ m$E_h$ |
|---|---:|---:|---:|---:|
| H₂ 0.735 Å, STO-3G | 4 | 15 | 1.894 | $1.2\times10^3$ |
| H₂ 0.735 Å, 6-31G | 8 | 185 | 11.46 | $7.2\times10^3$ |
| H₂ 0.735 Å, cc-pVDZ | 20 | 2951 | 104.4 | $6.5\times10^4$ |
| LiH 1.6 Å, STO-3G | 12 | 631 | 12.34 | $7.7\times10^3$ |
| H₂O (experimental geometry), STO-3G | 14 | 1086 | 72.00 | $4.5\times10^4$ |
| N₂ 1.098 Å, STO-3G | 20 | 2959 | 117.7 | $7.4\times10^4$ |

Further values for frozen-core active spaces (Chapter 6.1): H₄ chain at 1.0 Å, 8 qubits, $\lambda=7.14$; LiH with frozen 1s, 10 qubits, $\lambda=8.89$, down from 12.34 with the core included.

Observations:

- **$\lambda$ grows quickly with basis size.** It rises by a factor of 55 for H₂ from STO-3G to cc-pVDZ. Adding diffuse and polarization functions adds many two-electron integrals of similar size.
- **Core electrons are expensive.** $\lambda$ grows with nuclear charge (LiH < H₂O < N₂), largely through core-orbital integrals. Freezing cores and using active spaces lower it ([[frozen-core-and-active-space-hamiltonians]]).
- **$\lambda$ depends on the representation.** Orbital rotations, localization, and factorized forms change it, without changing the spectrum. Even the arbitrary choice within N₂'s degenerate $\pi$ orbitals moves $\lambda$ between about 115 and 119 $E_h$ in separate runs (symmetry-adapted orbitals give 114.71), so the N₂ entry above is one representative value ([[molecular-hamiltonian-in-the-mo-basis]]). The Pauli 1-norm here is an upper reference point, not the value used in state-of-the-art estimates.
- **Term count is $O(N^4)$**, from 15 to about 3000 for 20 qubits. The SELECT cost scales accordingly unless the Hamiltonian is factorized.

## Factorized Hamiltonians and published estimates

Modern estimates do not block-encode the raw Pauli sum. They factorize the two-electron tensor and encode the factors:

- **Low-rank factorizations.** The Coulomb operator is written as a sum of squares of one-body operators. Single and double factorization are the standard variants.
- **Tensor hypercontraction (THC).** Lee et al. (2021) block-encode quantum chemistry Hamiltonians in an arbitrary basis of $N$ orbitals with $\tilde O(N)$ Toffoli complexity per oracle call. They need $O(\lambda/\epsilon)$ calls, with $\lambda$ the 1-norm of the factorized representation. For the FeMoco active space they estimate **about four million physical qubits and under four days of runtime**, assuming 1 µs surface-code cycle times and physical error rates no worse than 0.1%.
- **History.** Reiher et al. (2017) gave the first detailed fault-tolerant estimate for FeMoco, using Trotterization. That study is what made nitrogenase the standard benchmark. Its specific gate counts are not reproduced here because I could not check them against the paper.

The estimates have fallen by orders of magnitude since 2017. This came from better encodings and algorithms, not better hardware, and the cost is dominated by $\lambda$ and the oracle cost.

## Putting the pieces together

For a target precision $\epsilon$, total cost is roughly

$$
\underbrace{\frac{1}{|c_0|^2}}_{\text{repetitions}}\times\underbrace{\frac{\lambda}{\epsilon}}_{\text{walk steps}}\times\underbrace{C_{\text{oracle}}(N)}_{\text{Toffolis per step}} .
$$

Two caveats belong next to every estimate:

1. **Overlap.** Published estimates usually assume a good input state. Without one, the first factor can dominate ([[qpe-state-preparation-and-overlap]]).
2. **Basis.** The energy is FCI in the chosen active space and basis. Basis-set incompleteness, often tens of m$E_h$ in total energies, is not reduced by QPE. Larger bases raise $\lambda$ and $N$ together.

## Source

- G. H. Low and I. L. Chuang, "Hamiltonian simulation by qubitization", *Quantum* **3**, 163 (2019), doi:10.22331/q-2019-07-12-163.
- R. Babbush, C. Gidney, D. W. Berry, N. Wiebe, J. McClean, A. Paler, A. Fowler and H. Neven, "Encoding electronic spectra in quantum circuits with linear T complexity", *Phys. Rev. X* **8**, 041015 (2018), doi:10.1103/PhysRevX.8.041015. Qubitized phase estimation with $O(\lambda/\epsilon)$ queries.
- J. Lee, D. W. Berry, C. Gidney, W. J. Huggins, J. R. McClean, N. Wiebe and R. Babbush, "Even more efficient quantum computations of chemistry through tensor hypercontraction", *PRX Quantum* **2**, 030305 (2021), doi:10.1103/PRXQuantum.2.030305. The FeMoco physical-qubit and runtime figures are quoted from the abstract.
- M. Reiher, N. Wiebe, K. M. Svore, D. Wecker and M. Troyer, "Elucidating reaction mechanisms on quantum computers", *PNAS* **114**, 7555 (2017), doi:10.1073/pnas.1619152114.
- A. M. Childs, Y. Su, M. C. Tran, N. Wiebe and S. Zhu, *Phys. Rev. X* **11**, 011020 (2021), doi:10.1103/PhysRevX.11.011020.

The statement that the walk eigenphases are $\pm\arccos(E/\lambda)$ is standard in the qubitization literature; I did not derive it here. All $\lambda$ values and term counts are computed in `qcchem/part6_ch4_qpe.py` (section E).
