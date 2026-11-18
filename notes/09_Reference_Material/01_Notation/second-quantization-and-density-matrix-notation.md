---
id: second-quantization-and-density-matrix-notation
title: Second-quantization and density-matrix notation
summary: Symbols for creation and annihilation operators, occupation-number vectors, excitation operators, normal ordering, cluster and rotation operators, and the one- and two-electron density matrices, with the book each comes from. Definitions and index orders of the densities are compared in density-matrix-conventions.
status: in-progress
kind: reference
level: intermediate
tags: [notation, second-quantization, excitation-operators, density-matrices, normal-ordering]
prerequisites: [index-and-orbital-notation]
related: [creation-and-annihilation-operators, second-quantized-operators, normal-ordering-and-wicks-theorem, density-matrix-conventions, excitation-operator-conventions]
order: 30
date: 2026-11-17
---

## Operators and states

| Symbol | Meaning | Defined in |
|---|---|---|
| $a_P^\dagger$, $a_P$ | create, annihilate an electron in spin orbital $P$ | [[creation-and-annihilation-operators]] |
| $a_{p\sigma}^\dagger$ | spin orbital with spatial part $p$ and spin $\sigma\in\{\alpha,\beta\}$ | [[second-quantized-operators]] |
| $\{a_P, a_Q^\dagger\} = \delta_{PQ}$ | anticommutation relations (orthonormal spin orbitals) | [[commutator-and-anticommutator-identities]] |
| $|\mathrm{vac}\rangle$ (HJO), $|\,\rangle$ (Szabo) | true vacuum, no electrons | [[creation-and-annihilation-operators]] |
| $|\mathbf k\rangle = |k_1k_2\cdots k_M\rangle$ | occupation-number (ON) vector, $k_P\in\{0,1\}$ | [[second-quantization-in-a-finite-basis]] |
| $\hat n_P = a_P^\dagger a_P$, $\hat N = \sum_P\hat n_P$ | occupation-number and number operators | |
| $|0\rangle$ | reference determinant used as Fermi vacuum (SB); the state of interest (HJO) | |
| $\hat\imath^\dagger$, $\hat a$ | SB shorthand for $a_i^\dagger$, $a_a$ with the letter fixing hole/particle | |
| $\{\cdots\}$ | normal product relative to the Fermi vacuum (SB); $:\cdots:$ in some other texts | [[normal-ordering-and-wicks-theorem]] |

Many-electron operators in second quantization ([[second-quantized-operators]]):

$$
\hat H = \sum_{PQ}h_{PQ}a_P^\dagger a_Q + \tfrac12\sum_{PQRS}g_{PQRS}\,a_P^\dagger a_R^\dagger a_S a_Q + h_{\text{nuc}},
\qquad g_{PQRS} = (PQ|RS) .
$$

## Excitation and rotation operators

| Symbol | Meaning |
|---|---|
| $\hat E_{pq} = \sum_\sigma a_{p\sigma}^\dagger a_{q\sigma}$ | singlet (spin-summed) excitation operator, HJO Eq. (2.2.7) |
| $\hat e_{pqrs} = \hat E_{pq}\hat E_{rs} - \delta_{qr}\hat E_{ps}$ | two-electron singlet operator |
| $\hat E^-_{pq} = \hat E_{pq} - \hat E_{qp}$ | anti-Hermitian combination used in orbital rotations |
| $\hat\kappa = \sum_{p>q}\kappa_{pq}\hat E^-_{pq}$ | anti-Hermitian orbital-rotation generator; its exponential is the unitary orbital rotation ([[orbital-rotations]]) |
| $\hat T = \hat T_1 + \hat T_2 + \cdots$ | cluster operator ([[excitation-operator-conventions]] for normalizations) |
| $\hat\tau_\mu$, $t_\mu$ | HJO's generic excitation operator and its amplitude, $\hat T = \sum_\mu t_\mu\hat\tau_\mu$ |
| $\hat S_\pm$, $\hat S_z$, $\hat S^2$ | total-spin operators ([[spin-operators]]) |
| $\hat T^{k,q}_{pq}$ | spin-tensor operators ([[spin-tensor-operators]]) |

## Density matrices

| Symbol | Meaning | Source |
|---|---|---|
| $\gamma(\mathbf x_1,\mathbf x_1')$ | one-electron reduced density matrix (kernel), trace $N$ | Szabo, SB |
| $\gamma_{ij}$ | its matrix in spin orbitals, $\gamma_{ij} = \langle a_j^\dagger a_i\rangle$ | Szabo |
| $\bar D_{PQ}$, $\bar d_{PQRS}$ | spin-orbital densities $\langle a_P^\dagger a_Q\rangle$, $\langle a_P^\dagger a_R^\dagger a_S a_Q\rangle$ | HJO |
| $D_{pq}$, $d_{pqrs}$ | spin-summed (orbital) densities $\langle\hat E_{pq}\rangle$, $\langle\hat e_{pqrs}\rangle$ | HJO |
| $\Gamma_{rspq}$ | SB two-body density $\langle a_p^\dagger a_q^\dagger a_s a_r\rangle$ | SB |
| $\mathbf P$ | closed-shell AO density, $2\mathbf C_{\text{occ}}\mathbf C_{\text{occ}}^\dagger$ | Szabo |
| $\rho(\mathbf r)$ | electron density, $\rho(\mathbf r) = \sum_\omega\gamma(\mathbf x,\mathbf x)$ | |
| $\omega_P$, $n_p$ | natural occupation numbers | |

The index order and normalization differ between these; [[density-matrix-conventions]] gives the dictionary and the energy formula in each.

## Source

- Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, 2000), Secs. 1.2-1.4 (ON vectors, operators), Sec. 1.7, pp. 19-23, Eqs. (1.7.4)-(1.7.6) (spin-orbital densities), Sec. 2.2, p. 36, Eq. (2.2.7) ($\hat E_{pq}$), Secs. 3.2-3.3, pp. 86-93 (orbital rotations); Sec. 13.1 ($\hat\tau_\mu$).
- Shavitt and Bartlett, *Many-Body Methods in Chemistry and Physics* (Cambridge University Press, 2009), Sec. 3.4, p. 72 (hole/particle letters, Fermi vacuum $|0\rangle$), Sec. 11.2, pp. 352-353, Eqs. (11.15)-(11.25) (densities).
- Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996), Sec. 4.4, pp. 252-254 ($\gamma$), as recorded in [[one-particle-rdm]].
