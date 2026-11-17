---
id: frozen-core-and-active-space-hamiltonians
title: Frozen-core and active-space Hamiltonians - the core energy, the effective one-electron operator and qubit savings
summary: Splitting the orbitals into doubly occupied core, active and discarded virtual sets gives an active-space Hamiltonian of the same form, with a constant E_core = E_nuc + Σ_i(h_ii + f^core_ii) and h^eff_tu = h_tu + Σ_i[2(tu|ii) − (ti|iu)]. Verified against PySCF CASCI for LiH, H₂O and N₂. Freezing the 1s cores costs under 0.3 mEh in STO-3G (LiH 0.23, H₂O 0.08, N₂ 0.30 mEh), saves 2 qubits per frozen orbital, and cuts the 1-norm λ sharply: H₂O 72.0 → 27.7 and N₂ about 115–118 → 36–38 Eh, since the core integrals are the largest. Small valence active spaces such as CAS(4e,4o) for H₂O and CAS(6e,6o) for N₂ cut qubits further (14 → 8 and 20 → 12) and λ to 6.9 and about 14 Eh, but lose 42 and 31 mEh of correlation energy. QPE on such a Hamiltonian returns the CASCI energy, not the full-space FCI energy.
status: in-progress
kind: theory
level: intermediate
tags: [frozen-core, active-space, casci, core-energy, effective-hamiltonian, qubit-reduction, one-norm, embedding]
prerequisites: [molecular-hamiltonian-in-the-mo-basis, fock-operator, mcscf-and-gvb]
related: [qpe-cost-and-resource-estimates, dmet-embedding-hamiltonian, sample-based-quantum-diagonalization, variational-quantum-eigensolver, jordan-wigner-mapping]
order: 20
date: 2026-11-17
---

## Overview

Qubit counts are tight. Every spatial orbital costs two qubits under Jordan–Wigner, and the Hamiltonian's 1-norm grows quickly with the number of orbitals ([[qpe-cost-and-resource-estimates]]). Almost every quantum chemistry calculation on quantum hardware therefore works in an **active space**:

- **core** orbitals, kept doubly occupied ("frozen");
- **virtual** orbitals, kept empty;
- the **active** orbitals in between, which are treated exactly on the quantum device.

This note derives the Hamiltonian that acts on the active space, verifies it against CASCI, and quantifies what freezing costs in energy and saves in qubits and $\lambda$. The same construction, with a different choice of orbitals, gives the DMET embedding Hamiltonian ([[dmet-embedding-hamiltonian]]).

**Notation.** $i,j$ are core spatial orbitals, $t,u,v,w$ active, and $p,q$ general. $h_{pq}$ and $(pq|rs)$ are MO integrals ([[molecular-hamiltonian-in-the-mo-basis]]).

## The active-space Hamiltonian

Restrict the wave function to determinants with every core orbital doubly occupied and every discarded virtual empty. Taking the expectation value of $\hat H$ over the core part leaves an operator on the active orbitals of exactly the original form:

$$
\hat H_{\text{act}}=E_{\text{core}}+\sum_{tu}h^{\text{eff}}_{tu}\,\hat E_{tu}+\frac12\sum_{tuvw}(tu|vw)\,\big(\hat E_{tu}\hat E_{vw}-\delta_{uv}\hat E_{tw}\big),
$$

with $\hat E_{tu}=\sum_\sigma a_{t\sigma}^\dagger a_{u\sigma}$. The constant and the one-body operator are

$$
E_{\text{core}}=E_{\text{nuc}}+\sum_i\big(h_{ii}+f^{\text{core}}_{ii}\big)
=E_{\text{nuc}}+2\sum_ih_{ii}+\sum_{ij}\big[2(ii|jj)-(ij|ji)\big],
$$

$$
h^{\text{eff}}_{tu}=h_{tu}+\sum_i\big[2(tu|ii)-(ti|iu)\big]\equiv f^{\text{core}}_{tu}.
$$

That is, $E_{\text{core}}$ is the energy of the frozen closed shell plus nuclear repulsion. The **core Fock operator** $h^{\text{eff}}$ is the bare one-electron operator plus the Coulomb and exchange potential of the frozen electrons ([[fock-operator]]). The two-electron integrals keep only active indices.

**Derivation sketch.**
1. Split each sum over orbitals into core and active parts.
2. Normal-order the core operators with respect to the closed-shell core.
3. Collect terms. Core–core terms give $E_{\text{core}}$. Terms with two core and two active indices give the Coulomb ($2(tu|ii)$) and exchange ($-(ti|iu)$) contributions to $h^{\text{eff}}$. Terms with one or three core indices vanish, because they change the core occupation.

The same algebra underlies CASCI and CASSCF ([[mcscf-and-gvb]]).

**Check against CASCI.** In the script, $E_{\text{core}}$ and $h^{\text{eff}}$ are built in the AO basis, as $D^{\text{core}}=2C_{\text{core}}C_{\text{core}}^T$ and $v^{\text{core}}=J[D^{\text{core}}]-\tfrac12K[D^{\text{core}}]$, then transformed to the active MOs. Both agree with PySCF's `CASCI.get_h1eff` to $10^{-8}$. Diagonalizing $\hat H_{\text{act}}$ reproduces the CASCI energy to $10^{-8}$ in all five cases below.

## Frozen core

Freezing the 1s cores (all other orbitals active), STO-3G, RHF orbitals:

| system | qubits | $E_{\text{core}}$ ($E_h$) | $E_{\text{FC}}-E_{\text{FCI}}$ (m$E_h$) | $\lambda$ full → frozen core ($E_h$) |
|---|---|---:|---:|---|
| LiH, 1.6 Å | 12 → 10 | −6.804012 | +0.228 | 12.34 → 8.89 |
| H₂O | 14 → 12 | −51.471170 | +0.078 | 72.00 → 27.73 |
| N₂, 1.098 Å | 20 → 16 | −76.412431 | +0.296 | ≈115–118 → ≈36–38 |

The N₂ ranges reflect the arbitrary choice within the degenerate $\pi$ orbitals ([[molecular-hamiltonian-in-the-mo-basis]]).

- **The energy cost is small and positive.** Freezing removes core and core–valence correlation, raising the energy by less than 0.3 m$E_h$ here. It is variational: freezing restricts the space. In larger, more flexible bases with core-correlating functions, core correlation is larger. It matters for absolute energies but largely cancels in valence energy differences.
- **The $\lambda$ savings are large.** Core orbitals are compact, so their one- and two-electron integrals, with nuclear attraction near $Z/r$ and self-repulsion of order $Z$, dominate $\lambda$. Freezing them moves that weight into the constant $E_{\text{core}}$, which costs nothing in phase estimation. For H₂O, $\lambda$ falls by a factor of 2.6 for a 0.08 m$E_h$ energy change.

## Valence active spaces

| system | active space | qubits | $E_{\text{CASCI}}-E_{\text{FCI}}$ (m$E_h$) | $\lambda$ ($E_h$) |
|---|---|---:|---:|---:|
| H₂O | CAS(4e, 4o): 3 core, 4 active | 8 | +42.12 | 6.91 |
| N₂ | CAS(6e, 6o): 4 core, 6 active | 12 | +30.99 | ≈14 (13.7–14.3) |

A small active space with fixed RHF orbitals (CASCI) captures static correlation in the chosen orbitals but loses tens of m$E_h$ of dynamic correlation. That is far beyond chemical accuracy in absolute terms. Whether it matters depends on the quantity: energy differences along a reaction coordinate often benefit from error cancellation. Two common remedies:

- **Optimize the orbitals** (CASSCF), so the active space is the best one of its size. Quantum versions alternate a quantum CI step with classical orbital rotations.
- **Add dynamic correlation afterwards** with perturbation theory (CASPT2- or NEVPT2-type) using RDMs measured on the device.

## What the quantum computer then solves

All the quantum methods of this part (VQE, SQD, QPE, DMET with quantum solvers) act on $\hat H_{\text{act}}$:

- **The energy reported is CASCI (or CASSCF) quality**, $E_{\text{core}}$ plus the active-space eigenvalue, not the full-space FCI energy. "Exact" QPE in an active space is exact only for the active-space problem.
- **Qubits:** $2n_{\text{act}}$ under Jordan–Wigner, fewer with symmetry tapering (Chapter 2, planned).
- **Electron count in the active space:** $N_{\text{act}}=N-2n_{\text{core}}$. The quantum calculation must be restricted to that sector, which is automatic if the input state has the right number of electrons.
- **Embedding is the same construction.** DMET's "core" is the unentangled environment and its "active space" is fragment plus bath. The embedding Hamiltonian has exactly the form above, with an extra chemical-potential term ([[dmet-embedding-hamiltonian]]).

## Source

- The frozen-core / CASCI Hamiltonian is standard: Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, 2000), Ch. 10 (inactive Fock matrix) (to verify the exact equation numbers). In this notebook: [[generalized-fock-matrix-and-orbital-hessian]] (inactive and active Fock matrices).
- PySCF CASCI (`mcscf.CASCI`, `get_h1eff`) is used as the reference implementation.
- All numbers are computed in `qcchem/part6_ch1_hamiltonian.py` (section D).
