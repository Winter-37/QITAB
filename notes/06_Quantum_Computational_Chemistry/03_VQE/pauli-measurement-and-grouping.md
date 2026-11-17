---
id: pauli-measurement-and-grouping
title: Measuring the energy in VQE - estimator variance, shot allocation and commuting groups
summary: VQE estimates ⟨H⟩ = Σ c_k⟨P_k⟩ from repeated projective measurements, so its cost is set by the estimator variance. With N_G shots on each simultaneously measured group G, Var = Σ σ_G²/N_G; the optimal allocation N_G ∝ σ_G gives N = (Σ σ_G)²/ε², below the worst case (λ/ε)². Exact variances in the FCI state, for ε = 1.6 mEh, in STO-3G. LiH: 5.9×10⁷ (worst case), 6.0×10⁶ (each term separately), 5.0×10⁵ (177 qubit-wise commuting groups), 2.5×10⁵ (35 fully commuting groups). H₂O: 2.0×10⁹, 1.9×10⁸, 8.3×10⁶, 3.0×10⁶. For H₂ all three strategies cost the same 4.9×10⁴. Hartree–Fock variances underestimate these by 1.3–3.8×. A sampling simulation reproduces the predicted standard error to within 7%. Greedy grouping is sensitive to tie-breaking: equal coefficients ordered differently changed the LiH shot count by 1.5×. All counts are per energy evaluation; an optimization needs many.
status: in-progress
kind: algorithm
level: intermediate
tags: [VQE, measurement, shot-noise, variance, qubit-wise-commuting, commuting-groups, shot-allocation, clique-cover]
prerequisites: [variational-quantum-eigensolver, jordan-wigner-mapping]
related: [qubit-tapering, parity-and-bravyi-kitaev-mappings, adapt-vqe, error-mitigation-for-vqe, sample-based-quantum-diagonalization, projective-and-povm-measurements]
order: 30
date: 2026-11-17
---

## Overview

A quantum computer does not return $\langle\psi|\hat H|\psi\rangle$. It returns bit strings. Each run of the circuit ends with a projective measurement ([[projective-and-povm-measurements]]), and the energy is an average over many runs ("shots"). The number of shots for a target statistical error $\epsilon$ is the dominant cost of VQE ([[variational-quantum-eigensolver]]). This note derives the shot count, shows how simultaneous measurement of commuting terms reduces it, and computes it exactly for H₂, LiH and H₂O.

**Notation.**
- $\hat H=c_0I+\sum_kc_kP_k$, with Pauli strings $P_k$ from the Jordan–Wigner mapping ([[jordan-wigner-mapping]]).
- $\lambda=\sum_{k}|c_k|$ excludes the identity.
- $\epsilon$ is the target standard error; 1.6 m$E_h$ is used throughout.

## One term at a time

Measuring $P_k$ (after rotating each qubit so that its Pauli factor becomes $Z$) gives an outcome $\pm1$ with mean $\langle P_k\rangle$ and variance $1-\langle P_k\rangle^2$. With $N_k$ shots on term $k$, the estimator $\hat E=c_0+\sum_kc_k\bar P_k$ is unbiased and

$$
\operatorname{Var}\hat E=\sum_k\frac{\sigma_k^2}{N_k},\qquad \sigma_k=|c_k|\sqrt{1-\langle P_k\rangle^2}.
$$

**Optimal allocation.** Minimizing this variance at fixed total $N=\sum_kN_k$ with a Lagrange multiplier gives $N_k\propto\sigma_k$ (Wecker, Hastings and Troyer 2015). Then

$$
\operatorname{Var}\hat E=\frac{\big(\sum_k\sigma_k\big)^2}{N}\quad\Longrightarrow\quad N=\frac{\big(\sum_k\sigma_k\big)^2}{\epsilon^2}\le\Big(\frac{\lambda}{\epsilon}\Big)^2 ,
$$

since $\sigma_k\le|c_k|$. The worst-case bound $(\lambda/\epsilon)^2$ is the one quoted in [[variational-quantum-eigensolver]]. It ignores that many $\langle P_k\rangle$ are close to $\pm1$ in a good state.

## Measuring commuting terms together

Terms that commute can be measured on the same shots.

- **Qubit-wise commuting (QWC).** On every qubit the two strings have the same Pauli or one has $I$. One layer of single-qubit rotations diagonalizes all of them at once, so no extra entangling gates are needed.
- **Fully commuting (FC).** The strings commute as operators, which also allows an even number of positions with different non-identity Paulis (for example $XX$ and $YY$). A Clifford circuit diagonalizes the group, at the cost of additional two-qubit gates (Yen, Verteletskyi and Izmaylov 2020).

Each shot on group $G$ samples the operator $\hat O_G=\sum_{k\in G}c_kP_k$, whose variance includes the covariances:

$$
\sigma_G^2=\langle\hat O_G^2\rangle-\langle\hat O_G\rangle^2=\sum_{k,l\in G}c_kc_l\big(\langle P_kP_l\rangle-\langle P_k\rangle\langle P_l\rangle\big),
\qquad N=\frac{\big(\sum_G\sigma_G\big)^2}{\epsilon^2}.
$$

Since the standard deviation of a sum is at most the sum of standard deviations, $\sigma_G\le\sum_{k\in G}\sigma_k$. Grouping therefore never costs more shots than measuring the same terms separately, and it needs far fewer distinct circuits.

Finding the fewest groups is a minimum clique cover problem on the compatibility graph, which is NP-hard. Verteletskyi, Yen and Izmaylov (2020) compare heuristics for it. Here a greedy rule is used: take terms in order of decreasing $|c_k|$ and put each into the first group it is compatible with. The result depends on how equal coefficients are ordered. In a first run, ties broken by round-off gave 179 QWC groups and $3.3\times10^5$ shots for LiH, against 177 groups and $5.0\times10^5$ shots with the deterministic order used for the table. Better clique-cover heuristics remove much of this arbitrariness.

## Numbers

Exact variances evaluated in the FCI and HF states (STO-3G, Jordan–Wigner, symmetry-adapted RHF orbitals). Shots per energy evaluation for $\epsilon=1.6$ m$E_h$:

| system | qubits | terms | $\lambda$ | QWC / FC groups | state | $(\lambda/\epsilon)^2$ | per term, optimal | QWC groups | FC groups |
|---|---:|---:|---:|---|---|---:|---:|---:|---:|
| H₂, 0.735 Å | 4 | 14 | 1.894 | 5 / 2 | FCI | $1.40\times10^6$ | $4.86\times10^4$ | $4.86\times10^4$ | $4.86\times10^4$ |
| | | | | | HF | | $1.28\times10^4$ | $1.28\times10^4$ | $1.28\times10^4$ |
| LiH, 1.6 Å | 12 | 630 | 12.341 | 177 / 35 | FCI | $5.95\times10^7$ | $6.01\times10^6$ | $5.02\times10^5$ | $2.52\times10^5$ |
| | | | | | HF | | $2.57\times10^6$ | $3.92\times10^5$ | $1.51\times10^5$ |
| H₂O | 14 | 1085 | 71.998 | 344 / 53 | FCI | $2.03\times10^9$ | $1.86\times10^8$ | $8.35\times10^6$ | $2.98\times10^6$ |
| | | | | | HF | | $1.05\times10^8$ | $7.28\times10^6$ | $2.29\times10^6$ |

**Reading the table.**
- **The worst-case bound is pessimistic.** It overestimates the optimally allocated per-term cost by about a factor of 10 for LiH and H₂O, and by 29 for H₂.
- **Grouping helps a lot for real molecules.** For H₂O, QWC grouping saves a factor of 22 in shots over measuring terms separately, and FC grouping a factor of 62; for LiH the factors are 12 and 24. FC needs 5–6.5 times fewer circuit settings than QWC (35 against 177 for LiH, 53 against 344 for H₂O), but each needs a diagonalizing Clifford circuit.
- **H₂ gains nothing from grouping.** In its two-determinant ground state the outcomes of the terms in each group are perfectly correlated, so $\sigma_G=\sum_{k\in G}\sigma_k$ holds with equality.
- **The variances must come from somewhere.** The optimal allocation needs $\sigma_G$, which depends on the unknown state. HF is a convenient proxy but underestimates: by 3.8× for H₂, 1.7× for LiH with FC groups, and 1.3× for H₂O. In practice $\sigma_G$ is estimated from a first batch of shots.
- **These are costs per energy evaluation.** An optimization needs hundreds to thousands of energies. The parameter-shift rule costs two per parameter per gradient. Molecules beyond a few dozen qubits quickly reach $10^{9}$–$10^{12}$ shots, which motivated measuring determinants instead ([[sample-based-quantum-diagonalization]]).

!!! example "Checking the variance formula by sampling"
    The script simulates each shot. It rotates the exact FCI state into each group's QWC basis, samples bit strings, and evaluates every Pauli string from the bits. Shots are allocated as $N_G\propto\sigma_G$.

    | system | shots per estimate | repeats | mean | spread | predicted $\big(\sum_G\sigma_G^2/N_G\big)^{1/2}$ |
    |---|---:|---:|---|---:|---:|
    | H₂ | 20,000 | 2000 | $-1.137286$ (FCI $-1.137306$) | 2.43 m$E_h$ | 2.50 m$E_h$ |
    | LiH | 200,010 | 400 | $-7.882155$ (FCI $-7.882324$) | 2.71 m$E_h$ | 2.54 m$E_h$ |

    The estimator is unbiased within its statistical error (the LiH mean is 1.3 standard errors of the mean from FCI), and its spread matches the formula within 7%. With 400 repeats the spread itself is only known to about 4%.

## Beyond grouping

- **Classical shadows.** Measure in random single-qubit bases and reconstruct many observables afterwards. The variance for one Pauli string grows as $3^{w}$ with its weight $w$, so the low weights of [[parity-and-bravyi-kitaev-mappings|Bravyi–Kitaev]] matter here (planned section).
- **Fewer qubits** from [[qubit-tapering]] give fewer, shorter strings. As shown there, $\lambda$ barely changes, so the shot count barely changes either.
- **Factorized Hamiltonians** (double factorization, measuring in rotated orbital bases) reduce the number of settings to $O(M)$ basis rotations and lower the variance further. They are not computed here.

## Source

- D. Wecker, M. B. Hastings and M. Troyer, "Progress towards practical quantum variational algorithms", *Phys. Rev. A* **92**, 042303 (2015): measurement cost and allocation by variance.
- V. Verteletskyi, T.-C. Yen and A. F. Izmaylov, "Measurement optimization in the variational quantum eigensolver using a minimum clique cover", *J. Chem. Phys.* **152** (12) (2020), doi:10.1063/1.5141458 (article number to verify).
- T.-C. Yen, V. Verteletskyi and A. F. Izmaylov, "Measuring all compatible operators in one series of single-qubit measurements using unitary transformations", *J. Chem. Theory Comput.* (2020), arXiv:1907.09386.
- J. Tilly et al., *Phys. Rep.* **986**, 1 (2022), Sec. 5 (measurement strategies).
- All numbers are computed in `qcchem/part6_ch3_vqe.py` (section A).
