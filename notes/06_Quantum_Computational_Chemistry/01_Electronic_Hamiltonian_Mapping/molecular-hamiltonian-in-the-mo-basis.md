---
id: molecular-hamiltonian-in-the-mo-basis
title: The molecular Hamiltonian in the MO basis - integral transformation, spin orbitals and notation
summary: Every quantum algorithm for chemistry starts from H = E_nuc + Σ h_pq a†_p a_q + ½ Σ (pq|rs) a†_p a†_r a_s a_q in an orthonormal orbital basis. This note covers how to get there. AO integrals are transformed to MOs by four quarter transformations, O(n⁵) instead of O(n⁸), checked against PySCF for H₂O/6-31G. Real orbitals give 8-fold permutational symmetry, 4186 unique integrals instead of 28,561 for 13 MOs. The spatial integrals are expanded to interleaved spin orbitals, and the note converts between chemists', physicists' and antisymmetrized notation. Checks: the HF energy from MO integrals matches PySCF to 10⁻¹⁰ (H₂O/6-31G); Szabo's six minimal-basis H₂ integrals are reproduced at R = 1.4 bohr; the 12-qubit LiH Hamiltonian gives the FCI energy. The spectrum is orbital-invariant, but the qubit Hamiltonian is not. For an H₄ chain a rotation doubles the Pauli term count (185 → 361) and raises λ from 7.14 to 7.82–8.91 Eh; for N₂ even the arbitrary choice within the degenerate π pair shifts λ by about 2 Eh.
status: in-progress
kind: theory
level: intermediate
tags: [molecular-hamiltonian, integral-transformation, mo-integrals, second-quantization, spin-orbitals, integral-notation, permutational-symmetry, orbital-invariance, one-norm]
prerequisites: [second-quantized-operators, integral-notation, rhf, molecular-hamiltonian]
related: [jordan-wigner-mapping, frozen-core-and-active-space-hamiltonians, qpe-cost-and-resource-estimates, minimal-basis-h2-model, spin-orbital-to-spatial-orbital]
order: 10
date: 2026-11-17
---

## Overview

Quantum algorithms for chemistry (VQE, SQD, QPE) all take as input the second-quantized electronic Hamiltonian in a finite orthonormal orbital basis. This note goes from a Hartree–Fock calculation to that operator, ready for a fermion-to-qubit mapping ([[jordan-wigner-mapping]]). Each step is routine in a quantum chemistry code, and each hides a convention that has to match on the quantum side: integral ordering, spin-orbital ordering, factors of ½, and the constant term.

## The target operator

With orthonormal spin orbitals $\{\chi_p\}$, the clamped-nucleus Hamiltonian ([[molecular-hamiltonian]], [[second-quantized-operators]]) is

$$
\hat H=E_{\text{nuc}}+\sum_{pq}h_{pq}\,a_p^\dagger a_q+\frac12\sum_{pqrs}(pq|rs)\,a_p^\dagger a_r^\dagger a_s a_q ,
$$

with

$$
h_{pq}=\int\chi_p^*(\mathbf x)\Big(-\tfrac12\nabla^2-\sum_A\frac{Z_A}{r_A}\Big)\chi_q(\mathbf x)\,d\mathbf x,\qquad
(pq|rs)=\iint\frac{\chi_p^*(\mathbf x_1)\chi_q(\mathbf x_1)\,\chi_r^*(\mathbf x_2)\chi_s(\mathbf x_2)}{r_{12}}\,d\mathbf x_1d\mathbf x_2 ,
$$

in chemists' notation ([[integral-notation]]). $E_{\text{nuc}}=\sum_{A<B}Z_AZ_B/R_{AB}$ is a constant that must not be forgotten: it becomes the coefficient of the identity in the qubit Hamiltonian.

**Equivalent forms.**
- **Physicists' notation.** $\langle pr|qs\rangle=(pq|rs)$, so the two-body term is $\tfrac12\sum\langle pq|rs\rangle a_p^\dagger a_q^\dagger a_sa_r$.
- **Antisymmetrized.** $\langle pq||rs\rangle=\langle pq|rs\rangle-\langle pq|sr\rangle$, with term $\tfrac14\sum\langle pq||rs\rangle a_p^\dagger a_q^\dagger a_sa_r$.

All three give the same operator; mixing them is the most common source of factor-of-2 and sign errors. Checked numerically: the antisymmetrized tensor is antisymmetric in both index pairs.

## Step 1: AO to MO integrals

The SCF gives MO coefficients $C_{\mu p}$, with $\phi_p=\sum_\mu C_{\mu p}\chi_\mu$ for $n$ basis functions. Then $h_{pq}=\sum_{\mu\nu}C_{\mu p}h_{\mu\nu}C_{\nu q}$, an $O(n^3)$ matrix product. The two-electron transformation

$$
(pq|rs)=\sum_{\mu\nu\lambda\sigma}C_{\mu p}C_{\nu q}C_{\lambda r}C_{\sigma s}\,(\mu\nu|\lambda\sigma)
$$

costs $O(n^8)$ done directly. Done as four **quarter transformations**, one index at a time, it costs $O(n^5)$:

$$
(p\nu|\lambda\sigma)=\sum_\mu C_{\mu p}(\mu\nu|\lambda\sigma),\quad\text{then }q,\ \text{then }r,\ \text{then }s .
$$

For H₂O/6-31G ($n=13$) that is about $1.5\times10^6$ multiply-adds against $8.2\times10^8$. The result matches PySCF's `ao2mo` to $10^{-10}$. For large $n$ this step, and storing $n^4$ numbers, becomes significant. Density fitting and Cholesky decomposition replace the four-index tensor by three-index factors. Those factorizations are also the basis of the low-rank Hamiltonian encodings used in QPE resource estimates ([[qpe-cost-and-resource-estimates]]).

**Permutational symmetry.** For real orbitals,

$$
(pq|rs)=(qp|rs)=(pq|sr)=(qp|sr)=(rs|pq)=(sr|pq)=(rs|qp)=(sr|qp),
$$

so only $P(P+1)/2$ integrals are unique, with $P=n(n+1)/2$. For $n=13$: 4186 unique against $n^4=28{,}561$, 6.8 times fewer.

**Check.** The closed-shell HF energy rebuilt from MO integrals,

$$
E_{\text{HF}}=E_{\text{nuc}}+2\sum_i^{\text{occ}}h_{ii}+\sum_{ij}^{\text{occ}}\big[2(ii|jj)-(ij|ji)\big],
$$

gives $-75.9839744727$ for H₂O/6-31G, equal to PySCF's RHF energy to $10^{-10}$ ([[spin-orbital-to-spatial-orbital]]).

## Step 2: spatial to spin orbitals

Quantum registers are indexed by spin orbitals. Following the notebook's convention, interleave them, so that spin orbital $2p+\sigma$ is spatial orbital $p$ with spin $\sigma\in\{\alpha,\beta\}$. Then

$$
h_{2p+\sigma,\,2q+\tau}=h_{pq}\,\delta_{\sigma\tau},\qquad
(2p+\sigma,\,2q+\sigma'|\,2r+\tau,\,2s+\tau')=(pq|rs)\,\delta_{\sigma\sigma'}\delta_{\tau\tau'} .
$$

Spin is integrated out, so integrals are nonzero only when each charge distribution $\chi_p^*\chi_q$ is spin-diagonal (verified). The spin-orbital count is $M=2n$, which is the qubit count under Jordan–Wigner.

Another common convention puts all $\alpha$ orbitals first, then all $\beta$. It gives the same physics with different qubit labels. Pauli-string weights and circuit layouts differ, so the convention must match between the integral code and the quantum code.

## Step 3: the qubit Hamiltonian and two checks

Mapping $a_p$ to Pauli strings ([[jordan-wigner-mapping]]) gives $\hat H=\sum_kc_kP_k$. For LiH/STO-3G at 1.6 Å (12 qubits) there are 631 Pauli terms including the identity; the identity coefficient is $-4.135867$ and $\lambda=12.34\,E_h$. Two checks catch almost every convention error:

1. **Hartree–Fock.** The basis state with the lowest $N_e$ spin orbitals occupied must give $\langle\text{HF}|\hat H|\text{HF}\rangle=E_{\text{RHF}}$. It does.
2. **FCI.** The lowest eigenvalue in the $N_e$-electron sector must equal the FCI energy. For LiH it is $-7.8823243789$, matching PySCF FCI to $10^{-10}$.

!!! example "Minimal-basis H₂ at $R=1.4$ bohr (Szabo–Ostlund)"
    The MO integrals in $E_h$, compared with Szabo–Ostlund's four-decimal values. $h_{11}$ and $h_{22}$ are confirmed in [[rhf]] (Ex. 3.23). The four Coulomb and exchange values are recalled from Szabo's minimal-basis H₂ treatment and still need checking against the book:

    | | value | Szabo |
    |---|---:|---:|
    | $h_{11}$ | −1.252797 | −1.2528 |
    | $h_{22}$ | −0.475602 | −0.4756 |
    | $J_{11}=(11\vert11)$ | 0.674594 | 0.6746 |
    | $J_{12}=(11\vert22)$ | 0.663564 | 0.6636 |
    | $J_{22}=(22\vert22)$ | 0.697495 | 0.6975 |
    | $K_{12}=(12\vert21)$ | 0.181258 | 0.1813 |

    All six agree to four decimals. $E_{\text{RHF}}=2h_{11}+J_{11}+1/R=-1.116714$, equal to PySCF. Integrals of the form $(11|12)$ and $(12|22)$ vanish by $g/u$ symmetry, which is why the H₂ qubit Hamiltonian has only 15 terms ([[minimal-basis-h2-model]]).

## The orbital basis matters for the qubit Hamiltonian

Rotating the orbitals by a unitary $U$ changes every integral but not the spectrum: FCI is orbital-invariant. It does change the qubit Hamiltonian.

!!! example "H₄ chain, 1.0 Å, STO-3G (8 qubits)"

    | orbitals | Pauli terms | $\lambda$ ($E_h$) | ground energy |
    |---|---:|---:|---:|
    | canonical RHF | 185 | 7.1449 | −2.1663874486 |
    | half-chain localized (45° rotations within occupied and within virtual pairs) | 361 | 7.8232 | −2.1663874486 |
    | random orthogonal rotation | 361 | 8.9132 | −2.1663874486 |

    Canonical orbitals of the symmetric chain have definite parity, which makes many integrals vanish. Rotating them breaks the symmetry, nearly doubles the number of terms, and raises $\lambda$. Here localization *increases* $\lambda$. For larger systems in larger bases, localized or specially optimized orbitals are often used to *reduce* it; the outcome depends on the system.

**Degenerate orbitals.** For N₂/STO-3G the occupied $\pi$ pair is degenerate ($\varepsilon=-0.572777\,E_h$), so the SCF returns an arbitrary rotation within it. Rotating within the pair changes $\lambda$ by about 2 $E_h$ (116.5, 117.6, 118.6 for three angles). Separate runs gave values from about 115 to 119 $E_h$. Any reported $\lambda$, term count or circuit depth therefore refers to a specific orbital choice. Reproducible workflows fix the orbitals, for example by symmetry adaptation.

**The input state changes too.** The HF determinant is a computational basis state only in the canonical (or any occupied/virtual-separated) basis. A generic rotation mixes occupied and virtual orbitals and turns HF into a superposition. Rotations within the occupied space and within the virtual space leave the HF state invariant up to a phase, and the energy unchanged.

## Source

- The Hamiltonian and notation: Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996), Chs. 2–3. In this notebook: [[second-quantized-operators]], [[integral-notation]], [[minimal-basis-h2-model]]. The $J$ and $K$ reference values for H₂ at 1.4 bohr are recalled, not read from the book: to verify (the computed values are authoritative here).
- Quarter transformations and the $O(n^5)$ cost are standard; see Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, 2000), Ch. 9 (to verify the exact section).
- All numbers are computed with PySCF in `qcchem/part6_ch1_hamiltonian.py` (sections A–C), using the Jordan–Wigner tools in `qcchem/qchem_qubit_tools.py`.
