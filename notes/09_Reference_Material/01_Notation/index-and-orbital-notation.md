---
id: index-and-orbital-notation
title: Index letters and orbital symbols
summary: Which letters mean occupied, virtual, active and general orbitals in each part of the notebook, and which symbols denote spin orbitals, spatial orbitals and basis functions. The letter a is occupied in the Szabo-based chapters and virtual in the HJO- and Shavitt–Bartlett-based chapters; χ is a spin orbital in Szabo and an atomic orbital in HJO.
status: in-progress
kind: reference
level: introductory
tags: [notation, indices, orbitals, spin-orbitals, basis-functions, conventions]
prerequisites: []
related: [operator-and-matrix-notation, second-quantization-and-density-matrix-notation, integral-notation, excited-determinants, derivative-integrals-and-u-matrices]
order: 10
date: 2026-11-17
---

## Why this note exists

The electronic-structure chapters follow their main source closely, so the notation changes with the source. Two collisions matter most:

- **The letter $a$.** In the Szabo–Ostlund chapters $a,b,c$ are **occupied** orbitals and $r,s,t$ are virtual. In the chapters that follow Helgaker–Jørgensen–Olsen (HJO), Shavitt–Bartlett (SB) or Yamaguchi et al. (YOGS), $a,b,c$ are **virtual** and $i,j,k$ are occupied.
- **The letter $\chi$.** In Szabo, $\chi$ is a **spin orbital**. In HJO, $\chi_\mu$ is an **atomic orbital** (basis function), and orbitals are $\phi$.

Each note states its convention near the top. Use this table to find which one applies.

## Index letters

| Role | Szabo–Ostlund | HJO, spatial orbitals | HJO, spin orbitals | Shavitt–Bartlett |
|---|---|---|---|---|
| occupied (hole) | $a,b,c,\dots$ | $i,j,k,l$ (inactive) | $I,J,K,L$ | $i,j,k,\dots$ |
| virtual (particle) | $r,s,t,\dots$ | $a,b,c,d,e$ | $A,B,C,D$ | $a,b,c,\dots$ |
| active (partially occupied) | — | $v,w,x,y,z$ | — | — |
| general | $i,j,k,l$ | $m,n,o,p,q,r,s,t,u$ | $P,Q,R,S$ | $p,q,r,s$ |
| basis functions (AOs) | $\mu,\nu,\lambda,\sigma$ | $\mu,\nu,\dots$ | — | — |

The gradient notes (from Yamaguchi et al., YOGS) use the Shavitt–Bartlett letters for MOs, $m$ as an extra general index, and $\mu,\nu,\lambda,\sigma$ for AOs. In YOGS itself the general MO indices are $i,j,k,l$ and occupied/virtual are named "d.o." and "virt."; the gradient notes translate this to the HJO-style letters above ([[derivative-integrals-and-u-matrices]]).

**Where each convention is used in this notebook (Part 4).**

| Chapters | Convention |
|---|---|
| 2 Many-electron wave functions, 3 Hartree–Fock, 9 CI (Szabo notes), 10 MBPT, the coupled-pair and IEPA notes of Ch. 11, [[one-particle-hamiltonian-models]] | Szabo: $a$ occupied, $r$ virtual |
| 5 Second quantization, 6 RDMs, 7 Orbital optimization, 9 CI (HJO notes), 12 Beyond CCSD, 13 MCSCF | HJO: lowercase spatial, uppercase spin orbitals |
| 11 Coupled cluster (spin-orbital and closed-shell CCSD, diagrams), 15 Analytic derivatives | $i$ occupied, $a$ virtual |

Part 6 (quantum computational chemistry) uses $i,j$ occupied, $a,b$ virtual and $p,q,r,s$ general.

!!! warning "Translating between chapters"
    A Szabo formula such as $E_0^{(2)} = \sum_{a<b,\,r<s}|\langle ab||rs\rangle|^2/(\varepsilon_a+\varepsilon_b-\varepsilon_r-\varepsilon_s)$ becomes, in the other convention, $\sum_{i<j,\,a<b}|\langle ij||ab\rangle|^2/(\varepsilon_i+\varepsilon_j-\varepsilon_a-\varepsilon_b)$. Rename **all** indices at once; renaming $r\to a$ before $a\to i$ produces nonsense.

## Orbital and function symbols

| Object | Szabo–Ostlund | HJO | This notebook (Part 6, gradients) |
|---|---|---|---|
| spin orbital | $\chi_i(\mathbf x)$, $\mathbf x = (\mathbf r,\omega)$ | $\phi_P(\mathbf x)$ | $\chi$ or $\phi_{p\sigma}$, stated per note |
| spatial MO | $\psi_i(\mathbf r)$ | $\phi_p(\mathbf r)$ | $\phi_p$ |
| basis function (AO) | $\phi_\mu(\mathbf r)$ | $\chi_\mu(\mathbf r)$ | $\phi_\mu$ or $\chi_\mu$, stated per note |
| number of basis functions / spin orbitals | $K$ spatial, $2K$ spin orbitals | $M$ spin orbitals | stated per note |
| spin functions | $\alpha(\omega),\beta(\omega)$ | $\alpha,\beta$; $\sigma,\tau\in\{\alpha,\beta\}$ | same |
| MO coefficients | $\psi_i = \sum_\mu C_{\mu i}\phi_\mu$ | $\phi_p = \sum_\mu C_{\mu p}\chi_\mu$ | MO $p$ in column $p$ of $\mathbf C$ |
| reference determinant | $|\Psi_0\rangle$ | $|\mathrm{HF}\rangle$, $|0\rangle$ | $|\Phi_0\rangle$ or $|\mathrm{HF}\rangle$ |
| excited determinants | $|\Psi_a^r\rangle$, $|\Psi_{ab}^{rs}\rangle$ | $\hat E_{ai}|\mathrm{HF}\rangle$, $a_A^\dagger a_I|\mathrm{HF}\rangle$ | $|\Phi_i^a\rangle$, $|\Phi_{ij}^{ab}\rangle$ |

In every convention $\mathbf C$ has one column per MO, so $\mathbf C^\dagger\mathbf S\mathbf C = \mathbf 1$ for orthonormal MOs.

## Matrices over basis functions

| Quantity | Szabo | Notebook gradient notes | YOGS | PySCF |
|---|---|---|---|---|
| overlap | $S_{\mu\nu}$ | $S_{\mu\nu}$ | $S_{\mu\nu}$ | `mol.intor("int1e_ovlp")` |
| core Hamiltonian | $H^{\text{core}}_{\mu\nu}$ | $h_{\mu\nu}$ | $h_{\mu\nu}$ | `mf.get_hcore()` |
| Fock matrix | $F_{\mu\nu}$ | $F_{\mu\nu}$ | $F_{\mu\nu}$ | `mf.get_fock()` |
| closed-shell density | $P_{\mu\nu} = 2\sum_a^{N/2}C_{\mu a}C_{\nu a}^*$ | $P_{\mu\nu}$ (same) | $D_{\mu\nu} = P_{\mu\nu}/2$ | `mf.make_rdm1()` $= P$ |

With these definitions $\operatorname{tr}(\mathbf P\mathbf S) = N$ and $E_{\text{RHF}} = \tfrac12\operatorname{tr}[\mathbf P(\mathbf h + \mathbf F)] + E_{\text{nuc}}$ (both checked for LiH/STO-3G in `part9_reference.py`, section H).

## Other recurring symbols

| Symbol | Meaning |
|---|---|
| $N$ | number of electrons |
| $Z_A$, $\mathbf R_A$, $M_A$ | charge, position, mass of nucleus $A$ |
| $\varepsilon_p$ | orbital energy (canonical Fock eigenvalue) |
| $E_0$, $E_{\text{HF}}$, $E_{\text{corr}}$ | reference, Hartree–Fock and correlation energies |
| $h_{pq}$, $g_{pqrs}$ | one-electron integrals and chemists' two-electron integrals $(pq|rs)$ ([[integral-notation]]) |
| $\langle pq|rs\rangle$, $\langle pq||rs\rangle$ | physicists' and antisymmetrized integrals |
| $f_{pq}$ / $F_{pq}$ | Fock matrix elements (lowercase in SB and CC notes, uppercase in HJO and Szabo) |
| $x, y$ | perturbations (nuclear coordinates, field components) in Part 4, Ch. 15 |
| $\kappa_{pq}$ | orbital-rotation parameters, $\hat\kappa = \sum_{p>q}\kappa_{pq}\hat E^-_{pq}$ (HJO) |
| $t_i^a$, $t_{ij}^{ab}$ | coupled-cluster amplitudes ([[excitation-operator-conventions]]) |

## Source

- Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996), Secs. 2.2.6-2.2.7, pp. 58-64 (index letters, as recorded in [[excited-determinants]]); Sec. 3.4, pp. 131-142 (basis functions, $\mathbf C$, $\mathbf P$, as recorded in [[rhf]]).
- Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, 2000), Sec. 5.1, p. 143, Eq. (5.1.5) (AOs $\chi_\mu$, MOs $\phi_p$); Sec. 10.1.1, p. 434 (inactive $i,j,k,l$; active $v,w,x,y,z$; virtual $a,b,c,d,e$; general $m,\dots,u$); Sec. 14.2, p. 740 (spin-orbital $P,Q,R,S$; $I,J,K,L$; $A,B,C,D$).
- Shavitt and Bartlett, *Many-Body Methods in Chemistry and Physics: MBPT and Coupled-Cluster Theory* (Cambridge University Press, 2009), Sec. 3.4, p. 72 (holes $i,j,k$; particles $a,b,c$; general $p,q,r$).
- Yamaguchi, Osamura, Goddard and Schaefer, *A New Dimension to Quantum Chemistry* (Oxford University Press, 1994): translation table in [[derivative-integrals-and-u-matrices]].
- Checks: `part9_reference.py` (section H).
