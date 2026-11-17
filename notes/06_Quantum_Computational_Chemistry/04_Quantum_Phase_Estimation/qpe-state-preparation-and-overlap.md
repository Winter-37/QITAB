---
id: qpe-state-preparation-and-overlap
title: State preparation for phase estimation - the HF overlap and why it decays with system size
summary: QPE returns the ground-state energy with probability |⟨Ψ₀|Φ⟩|², so the input state sets the number of repetitions. For H₂/STO-3G the HF overlap is 0.988 at 0.735 Å and falls to 0.537 at 3.0 Å, approaching ½ on dissociation; a two-determinant state is exact at every distance. For linear H_n chains the overlap decays geometrically. At 1.0 Å spacing it goes from 0.969 (H₂) to 0.834 (H₁₀), about 0.965 per H₂ unit; at 1.5 Å from 0.874 to 0.450, about 0.853 per unit. Two non-interacting H₂ molecules give exactly the square of one molecule's overlap. This is the orthogonality catastrophe: for N weakly coupled fragments |c₀|² ≈ f^N, so any fixed-form input loses overlap exponentially. The determinants needed for 90% of the FCI weight grow from 2 to 283 along the 1.5 Å chain. Remedies are better references (multireference, VQE, MPS, adiabatic preparation), which raise the question of what classical methods can already do with the same state.
status: in-progress
kind: comparison
level: intermediate
tags: [state-preparation, overlap, orthogonality-catastrophe, hartree-fock, hydrogen-chain, multireference, adiabatic-state-preparation, quantum-advantage]
prerequisites: [qpe-for-molecular-energies, electron-correlation, full-ci]
related: [h2-dissociation-rhf-uhf, mcscf-and-gvb, variational-quantum-eigensolver, sample-based-quantum-diagonalization, size-consistency]
order: 40
date: 2026-11-17
---

## Overview

Every QPE run returns the ground-state energy with probability $|c_0|^2=|\langle\Psi_0|\Phi\rangle|^2$ ([[qpe-for-molecular-energies]]). About $1/|c_0|^2$ repetitions are needed before the ground state is seen with reasonable confidence, and a small overlap can make the algorithm useless whatever its circuit cost. This note measures the overlap of the most common input, the Hartree–Fock determinant, and shows why it decays exponentially with system size.

**Notation.** $|c_0|^2$ is the squared overlap of the RHF determinant with the FCI ground state in the same orbitals. It equals the squared HF coefficient of the FCI vector, the weight of the reference determinant in intermediate normalization ([[full-ci]]). All calculations are FCI in STO-3G.

## Bond stretching: H₂

| $R$ (Å) | 0.5 | 0.735 | 1.0 | 1.5 | 2.0 | 2.5 | 3.0 |
|---|---:|---:|---:|---:|---:|---:|---:|
| $\lvert c_0\rvert^2$ | 0.9948 | 0.9876 | 0.9693 | 0.8737 | 0.7119 | 0.5944 | 0.5374 |

As the bond breaks, the FCI state tends to $(|\sigma_g^2\rangle-|\sigma_u^2\rangle)/\sqrt2$, the covalent combination. The RHF determinant $|\sigma_g^2\rangle$ then has overlap $\to\tfrac12$ ([[h2-dissociation-rhf-uhf]]). For QPE this is still workable: about two repetitions per success. The deeper problem is size.

**Better references help.** In a minimal basis the two-determinant (GVB / CASSCF(2,2)) state $c_1|\sigma_g^2\rangle-c_2|\sigma_u^2\rangle$ *is* the FCI state at every $R$, so its overlap is 1 ([[mcscf-and-gvb]]). Preparing two determinants on a quantum computer is cheap: a single Givens rotation in the $\sigma_g$/$\sigma_u$ pair space.

## System size: hydrogen chains

Linear, equally spaced H$_n$ chains, with $|c_0|^2$, the "per-H₂-unit" factor $|c_0|^{4/n}$, and the number of determinants needed to collect 90% of the FCI weight:

| $n$ | spacing 1.0 Å: $\lvert c_0\rvert^2$ | per unit | dets for 90% | spacing 1.5 Å: $\lvert c_0\rvert^2$ | per unit | dets for 90% (of total) |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 0.9693 | 0.9693 | 1 | 0.8737 | 0.8737 | 2 (of 4) |
| 4 | 0.9365 | 0.9677 | 1 | 0.7496 | 0.8658 | 4 (of 36) |
| 6 | 0.9026 | 0.9664 | 1 | 0.6366 | 0.8603 | 15 (of 400) |
| 8 | 0.8684 | 0.9654 | 2 | 0.5368 | 0.8560 | 66 (of 4900) |
| 10 | 0.8344 | 0.9644 | 5 | 0.4503 | 0.8525 | 283 (of 63,504) |

The per-unit factor is nearly constant, so the overlap decays **geometrically**, $|c_0|^2\approx f^{n/2}$, with $f\approx0.965$ at 1.0 Å and $f\approx0.853$ at 1.5 Å. Extrapolated, a stretched chain of 100 hydrogens would have $|c_0|^2\sim0.853^{50}\approx4\times10^{-4}$. That is the geometric fit, not a computed number.

**Independent fragments multiply exactly.** For two H₂ molecules (1.5 Å bonds) 50 Å apart, the FCI calculation on the combined system gives $|c_0|^2=0.763332$, equal to the square of the single-molecule value. For $N$ non-interacting fragments the ground state is a product, and so is HF, so $|c_0|^2=f^N$ exactly. Weak interaction modifies $f$ but not the exponential form.

## The orthogonality catastrophe

This is general. Any input built from local pieces of fixed accuracy (a determinant, a low-depth circuit, a truncated expansion) has overlap per fragment $f<1$. Its total overlap therefore vanishes as $f^N$ with system size, even when the energy per fragment is excellent. Two consequences:

- **The cost of QPE grows exponentially** in system size through the repetition count, unless the input improves with size.
- **Energy and overlap are different questions.** A state with error 1 m$E_h$ per fragment can have overlap far below any useful threshold for a large system. Size-extensive energies are not enough ([[size-consistency]]).

Lee et al. (2023) examined this in detail. They argue that the features that let a quantum computer prepare a high-overlap state efficiently tend also to make classical heuristics accurate. They conclude that evidence for a *generic exponential* quantum advantage in ground-state chemistry has not been found, while polynomial speed-ups remain possible.

## What to use as the input

| input | how it is prepared | comment |
|---|---|---|
| HF determinant | $X$ gates only | adequate for small, weakly correlated molecules |
| few-determinant / CASSCF | Givens rotations or controlled preparation | fixes bond breaking and diradicals |
| VQE or LUCJ state | variational circuit ([[variational-quantum-eigensolver]]) | QPE then "refines" a near-term state |
| matrix product state | sequential circuit from a classical DMRG solution | high overlap for 1D-like systems |
| adiabatic state preparation | slow interpolation from a solvable Hamiltonian | overlap set by the minimum gap; used by Aspuru-Guzik et al. (2005) |

These states can sometimes be checked cheaply. For example, the overlap of a candidate with the output of a short QPE run can be estimated by repeated runs. Sampling-based approaches such as [[sample-based-quantum-diagonalization]] face the same issue in a different form: they need the important determinants to appear in the samples.

## Source

- S. Lee, J. Lee, H. Zhai, Y. Tong, A. M. Dalzell, A. Kumar, P. Helms, J. Gray, Z.-H. Cui, W. Liu, M. Kastoryano, R. Babbush, J. Preskill, D. R. Reichman, E. T. Campbell, E. F. Valeev, L. Lin and G. K.-L. Chan, "Evaluating the evidence for exponential quantum advantage in ground-state quantum chemistry", *Nat. Commun.* **14**, 1952 (2023), doi:10.1038/s41467-023-37587-6.
- A. Aspuru-Guzik et al., *Science* **309**, 1704 (2005), doi:10.1126/science.1113479 (adiabatic state preparation for QPE).

All overlaps, determinant counts and the two-fragment check are computed with PySCF FCI in `qcchem/part6_ch4_qpe.py` (section D). The extrapolation to H₁₀₀ is illustrative only.
