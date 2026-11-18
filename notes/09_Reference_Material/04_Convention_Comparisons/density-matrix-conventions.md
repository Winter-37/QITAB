---
id: density-matrix-conventions
title: Density-matrix conventions across books and codes
summary: How Szabo, Helgaker–Jørgensen–Olsen, Shavitt–Bartlett, Yamaguchi et al. and PySCF define the one- and two-electron density matrices - which index is created and which annihilated, whether spin is summed, and whether the 2-RDM is normalized to N(N−1) or N(N−1)/2 - with the energy expression that goes with each. Verified on full-CI LiH in the full Fock space.
status: in-progress
kind: comparison
level: intermediate
tags: [density-matrices, rdm, conventions, normalization, pyscf, comparison]
prerequisites: [one-particle-rdm, density-matrices-second-quantization]
related: [second-quantization-and-density-matrix-notation, integral-notation, derivative-integrals-and-u-matrices, excitation-operator-conventions]
order: 10
date: 2026-11-17
---

## The two choices that differ

1. **Index order of the 1-RDM.** Is the first index the created or the annihilated orbital? For real wave functions the 1-RDM is symmetric and the choice is invisible; for transition densities, complex orbitals or response densities it matters.
2. **Normalization of the 2-RDM.** The trace is $N(N-1)$ (sum over ordered pairs) or $N(N-1)/2$ (unordered pairs), and the energy formula carries $\tfrac12$ or $\tfrac14$ or nothing to compensate.

Spin-orbital indices are uppercase or $p,q$ with spin implied; spin-summed (orbital) indices are lowercase. $g_{pqrs} = (pq|rs)$ (chemists'), $\langle pq||rs\rangle = \langle pq|rs\rangle - \langle pq|sr\rangle$ ([[integral-notation]]).

## Dictionary

| Source | 1-RDM | 2-RDM | Trace of 2-RDM |
|---|---|---|---|
| Szabo | $\gamma_{ij} = \langle a_j^\dagger a_i\rangle$ | — (not used) | — |
| HJO, spin orbitals | $\bar D_{PQ} = \langle a_P^\dagger a_Q\rangle$ | $\bar d_{PQRS} = \langle a_P^\dagger a_R^\dagger a_Sa_Q\rangle$ | $\sum_{PR}\bar d_{PPRR} = N(N-1)$ |
| HJO, orbitals | $D_{pq} = \langle\hat E_{pq}\rangle$ | $d_{pqrs} = \langle\hat e_{pqrs}\rangle$ | $\sum_{pr}d_{pprr} = N(N-1)$ |
| Shavitt–Bartlett | $\gamma_{qp} = \langle a_p^\dagger a_q\rangle$ | $\Gamma_{rspq} = \langle a_p^\dagger a_q^\dagger a_sa_r\rangle$ | $\sum_{pq}\Gamma_{pqpq} = N(N-1)$ |
| YOGS (gradient notes) | $Q_{pq} = D_{pq}$ | $G_{pqrs} = \tfrac12d_{pqrs}$ | $N(N-1)/2$ |
| PySCF `fci` | `dm1[p,q]` $=\langle a_q^\dagger a_p\rangle$ | `dm2[p,q,r,s]` $=\langle a_p^\dagger a_r^\dagger a_sa_q\rangle$ | $N(N-1)$ |

PySCF's `dm1`, `dm2` are spin-summed. The energy (electronic part) in each convention:

| Source | Energy |
|---|---|
| Szabo | $\sum_{ij}h_{ji}\gamma_{ij}$ (one-electron part) |
| HJO, spin orbitals | $\sum_{PQ}h_{PQ}\bar D_{PQ} + \tfrac12\sum_{PQRS}g_{PQRS}\bar d_{PQRS}$ |
| HJO, orbitals | $\sum_{pq}h_{pq}D_{pq} + \tfrac12\sum_{pqrs}g_{pqrs}d_{pqrs}$ |
| Shavitt–Bartlett | $\sum_{pq}o_{pq}\gamma_{qp} + \tfrac14\sum_{pqrs}\langle pq||rs\rangle\Gamma_{rspq}$ |
| YOGS | $\sum_{pq}h_{pq}Q_{pq} + \sum_{pqrs}g_{pqrs}G_{pqrs}$ |
| PySCF | `einsum('pq,qp', h, dm1) + 0.5*einsum('pqrs,pqrs', eri, dm2)` |

Relations that follow:

- **Szabo, SB and PySCF agree on the 1-RDM**: the first index is the annihilated orbital. **HJO is the transpose**: $\bar D_{PQ} = \gamma_{QP}$. For a real ground state they coincide numerically.
- **HJO and PySCF agree on the 2-RDM**: `dm2[p,q,r,s]` $= d_{pqrs}$, paired with chemists' integrals `eri[p,q,r,s]` $= (pq|rs)$. The order $p,q$ is electron 1 (create $p$, annihilate $q$), $r,s$ electron 2.
- **SB's $\Gamma$ is HJO's $d$ with indices regrouped**: $\Gamma_{rspq} = \bar d_{prqs}$, paired with physicists' antisymmetrized integrals; the $\tfrac14$ compensates for summing over all orderings of an antisymmetric pair twice.
- **Pair normalization.** Halving $d$ gives a 2-RDM with trace $N(N-1)/2$, the number of electron pairs. YOGS uses this ($G = \tfrac12d$), and so does the classic coordinate-space definition of the pair density in many older texts (to verify per source before use).
- **AO density.** The closed-shell AO density $P_{\mu\nu} = 2\sum_iC_{\mu i}C_{\nu i}$ of Szabo, PySCF `mf.make_rdm1()` and the notebook's gradient notes is the AO transform of $D$; YOGS uses $D_{\mu\nu} = P_{\mu\nu}/2$ ([[derivative-integrals-and-u-matrices]]).

!!! warning "Transition and response densities"
    For $\langle\Psi_A|\cdots|\Psi_B\rangle$ with $A\ne B$ the 1-RDM is not symmetric, and the two index orders give transposed matrices. PySCF's `trans_rdm1(bra, ket)[p,q]` is $\langle\mathrm{bra}|a_q^\dagger a_p|\mathrm{ket}\rangle$. A transition dipole or a Lagrangian (relaxed) density built in HJO's order must be transposed before it is contracted with PySCF's arrays, and vice versa.

## How this was checked

`part9_reference.py`, section H:

1. LiH/STO-3G (6 spatial, 12 spin orbitals, 4 electrons) was solved by building the full second-quantized Hamiltonian as Jordan–Wigner matrices in the $2^{12}$-dimensional Fock space and diagonalizing in the $N = 4$, $M_S = 0$ block. The ground-state energy agrees with PySCF's FCI to $4\times10^{-15}\,E_h$.
2. $\bar D$, $\bar d$, $\gamma$ and $\Gamma$ were evaluated element by element from their defining operator strings. Each energy formula in the table reproduces $E_{\text{FCI}} = -8.874\,531\,649\,E_h$ (electronic) to $10^{-14}$, and each trace is as tabulated.
3. PySCF's spin-free `dm1`, `dm2` equal the spin sums of $\bar D$ and $\bar d$, and its energy formula reproduces $E_{\text{FCI}}$.
4. For the index order of PySCF's transition density, the operators $a_q^\dagger a_p$ were applied with PySCF's own string routines (`fci.addons.des_a/cre_a/des_b/cre_b`) to the third singlet root and projected on the ground state. The result equals `trans_rdm1[p,q]` to $2\times10^{-16}$, while its transpose differs by up to 1.35.

## Source

- Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996), Sec. 4.4, pp. 252-254, Eqs. (4.33)-(4.40), Ex. 4.7, as recorded in [[one-particle-rdm]].
- Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, 2000), Sec. 1.7, pp. 19-23, Eqs. (1.7.4)-(1.7.6), (1.7.21)-(1.7.24); Sec. 2.7.1, pp. 61-63 (orbital densities), as recorded in [[density-matrices-second-quantization]].
- Shavitt and Bartlett, *Many-Body Methods in Chemistry and Physics* (Cambridge University Press, 2009), Sec. 11.2, pp. 352-354, Eqs. (11.15)-(11.26).
- Yamaguchi, Osamura, Goddard and Schaefer, *A New Dimension to Quantum Chemistry* (Oxford University Press, 1994): $Q$, $G$ as recorded in [[derivative-integrals-and-u-matrices]].
- PySCF 2.15.1, docstrings of `pyscf.fci.direct_spin1.make_rdm1`, `make_rdm12` and `pyscf/fci/rdm.py`, and the numerical checks above.
