---
id: excitation-operator-conventions
title: Excitation-operator and amplitude conventions
summary: Spin-orbital versus singlet excitation operators, the operator strings that produce Szabo's excited determinants with the right sign, and the normalizations of cluster operators - spin-orbital T₂ = ¼Σt a†b†ji (Shavitt–Bartlett) versus closed-shell T₂ = ½Σt E_ai E_bj (HJO, PySCF) - with the exact relation between the two sets of amplitudes and the matching energy formulas, checked on water CCSD.
status: in-progress
kind: comparison
level: intermediate
tags: [excitation-operators, coupled-cluster, amplitudes, conventions, spin-adaptation, pyscf, comparison]
prerequisites: [second-quantization-and-density-matrix-notation, excited-determinants]
related: [full-ci, index-and-orbital-notation, density-matrix-conventions, commutator-and-anticommutator-identities, ccsd-spin-orbital-equations, closed-shell-ccsd-t1-transformation, coupled-cluster-hierarchy-and-size-extensivity]
order: 20
date: 2026-11-17
---

Index letters here: $i,j$ occupied, $a,b$ virtual, $p,q$ general ([[index-and-orbital-notation]]). In Szabo's letters the same objects are $a,b$ occupied and $r,s$ virtual.

## One-electron excitation operators

| Operator | Definition | Acts on | Where |
|---|---|---|---|
| spin-orbital | $a_P^\dagger a_Q$ | spin orbitals | all books |
| singlet | $\hat E_{pq} = a_{p\alpha}^\dagger a_{q\alpha} + a_{p\beta}^\dagger a_{q\beta}$ | spatial orbitals | HJO Eq. (2.2.7) |
| anti-Hermitian | $\hat E^-_{pq} = \hat E_{pq} - \hat E_{qp}$ | spatial orbitals | orbital rotations |
| normal product | $\{a_a^\dagger a_i\}$ | relative to Fermi vacuum $|0\rangle$ | Shavitt–Bartlett |

For $a\ne i$ the normal product and the plain product are equal, $\{a_a^\dagger a_i\} = a_a^\dagger a_i$; the distinction matters only for $p = q$.

**Szabo's determinants as operator strings.** Szabo writes $|\Psi_a^r\rangle$ for the determinant with $\chi_r$ placed in the slot of $\chi_a$ (occupied $a$, virtual $r$ in Szabo's letters). With $|\chi_i\chi_j\cdots\rangle = a_i^\dagger a_j^\dagger\cdots|\,\rangle$:

$$
|\Psi_a^r\rangle = a_r^\dagger a_a|\Psi_0\rangle,
\qquad
|\Psi_{ab}^{rs}\rangle = a_r^\dagger a_s^\dagger a_ba_a|\Psi_0\rangle = a_r^\dagger a_a\,a_s^\dagger a_b|\Psi_0\rangle .
$$

The order of the annihilators ($a_b a_a$, i.e. reversed) is what keeps the sign $+1$. Writing $a_r^\dagger a_s^\dagger a_a a_b$ instead flips the sign of every double, which changes no energy but changes the sign of every CI coefficient and amplitude.

## Cluster operators

**Spin orbitals (Shavitt–Bartlett; [[ccsd-spin-orbital-equations]]).**

$$
\hat T_1 = \sum_{ia}t_i^a\{a_a^\dagger a_i\},\qquad
\hat T_2 = \frac1{(2!)^2}\sum_{ijab}t_{ij}^{ab}\{a_a^\dagger a_b^\dagger a_ja_i\} = \frac14\sum_{ijab}t_{ij}^{ab}\{a_a^\dagger a_b^\dagger a_ja_i\},
\qquad
\hat T_3 = \frac1{36}\sum t_{ijk}^{abc}\{\cdots\},
$$

with amplitudes antisymmetric in $ij$ and in $ab$: $t_{ij}^{ab} = -t_{ji}^{ab} = -t_{ij}^{ba} = t_{ji}^{ba}$. The prefactor $1/(n!)^2$ cancels the $(n!)^2$ equivalent orderings, so each distinct excitation appears once with coefficient $t$.

**Closed shell (HJO Sec. 13.7; PySCF `cc.CCSD`; [[closed-shell-ccsd-t1-transformation]]).**

$$
\hat T_1 = \sum_{ai}t_i^a\hat E_{ai},\qquad
\hat T_2 = \frac12\sum_{aibj}t_{ij}^{ab}\hat E_{ai}\hat E_{bj},\qquad t_{ij}^{ab} = t_{ji}^{ba},
$$

over spatial orbitals. These amplitudes are **not** antisymmetric; PySCF stores them as `t1[i,a]`, `t2[i,j,a,b]`.

**Relation between the two.** Writing $i\alpha$ for spatial orbital $i$ with spin $\alpha$,

$$
t_{i\alpha j\beta}^{a\alpha b\beta}(\text{spin orbitals}) = t_{ij}^{ab}(\text{closed shell}),
\qquad
t_{i\alpha j\alpha}^{a\alpha b\alpha} = t_{i\beta j\beta}^{a\beta b\beta} = t_{ij}^{ab} - t_{ji}^{ab},
$$

and $t_{i\alpha}^{a\alpha} = t_{i\beta}^{a\beta} = t_i^a$. PySCF's `cc.addons.spatial2spin` performs exactly this map.

**Energies.** The same correlation energy in both forms:

$$
E_{\text{corr}} = \frac14\sum_{ijab}\langle ij||ab\rangle\big(t_{ij}^{ab} + t_i^at_j^b - t_i^bt_j^a\big)\quad\text{(spin orbitals, canonical HF)},
$$

$$
E_{\text{corr}} = \sum_{ijab}\big[2(ia|jb) - (ib|ja)\big]\big(t_{ij}^{ab} + t_i^at_j^b\big)\quad\text{(closed shell)} .
$$

!!! example "Water, STO-3G"
    Converged RHF ($10^{-13}$) and CCSD ($10^{-12}$) at the geometry in `part9_reference.py` give $E_{\text{corr}} = -0.049\,438\,563\,E_h$. Both formulas above reproduce PySCF's value to $10^{-12}$, and the spin-orbital amplitudes from `spatial2spin` satisfy the two relations exactly. With the default SCF threshold the formulas miss PySCF by $1.3\times10^{-8}\,E_h$: a not-quite-converged reference leaves $f_{ia}\ne0$, and PySCF's energy includes the term $2\sum f_{ia}t_i^a$ that the canonical formulas drop.

## Other places the normalization differs

- **CI coefficients.** Szabo's CISD expansion $|\Psi\rangle = c_0|\Psi_0\rangle + \sum_{ar}c_a^r|\Psi_a^r\rangle + \sum_{a<b,\,r<s}c_{ab}^{rs}|\Psi_{ab}^{rs}\rangle$ uses restricted sums, equivalent to $\tfrac14\sum$ over unrestricted antisymmetric coefficients ([[full-ci]]).
- **Two-electron excitation operators.** HJO's $\hat e_{pqrs} = \hat E_{pq}\hat E_{rs} - \delta_{qr}\hat E_{ps}$ appears with $\tfrac12$ in $\hat H$; SB's normal-ordered $\hat V_N$ appears with $\tfrac14$ and antisymmetrized integrals. The factors match the density conventions of [[density-matrix-conventions]].

## Source

- Shavitt and Bartlett, *Many-Body Methods in Chemistry and Physics* (Cambridge University Press, 2009), Sec. 9.2, pp. 255-256, Eqs. (9.25)-(9.28); Eq. (9.83) (antisymmetric amplitudes).
- Helgaker, Jørgensen and Olsen, *Molecular Electronic-Structure Theory* (Wiley, 2000), Sec. 2.2, Eq. (2.2.7) ($\hat E_{pq}$); Secs. 13.7.3-13.7.4 (closed-shell CCSD), as recorded in [[closed-shell-ccsd-t1-transformation]].
- Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996), Secs. 2.2.6-2.2.7 (excited determinants) and Sec. 4.1, pp. 233-242 (CI expansion), as recorded in [[excited-determinants]] and [[full-ci]].
- Numerical checks: `part9_reference.py`, sections D (operator strings) and I (water CCSD with PySCF 2.15.1).
