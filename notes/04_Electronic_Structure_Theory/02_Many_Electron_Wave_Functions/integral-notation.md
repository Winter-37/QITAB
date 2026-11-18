---
id: integral-notation
title: One- and two-electron integral notation
summary: Physicists' ⟨pq|rs⟩ versus chemists' [pq|rs] / (pq|rs) notation for spin and spatial orbitals, the antisymmetrized integral ⟨pq||rs⟩, permutational symmetries, and Coulomb and exchange integrals. Includes the PySCF index conventions.
status: in-progress
kind: reference
level: introductory
tags: [notation, integrals, eri, chemists-notation, physicists-notation, coulomb, exchange]
prerequisites: [spin-orbitals-and-antisymmetry]
related: [slater-condon-rules, spin-orbital-to-spatial-orbital, second-quantized-operators, electron-repulsion-integrals-md-os-rys]
conventions: [ia-letters, chemists-integrals, physicists-integrals, antisymmetrized-integrals]
order: 20
date: 2026-11-03
---

## Definitions (Szabo Table 2.2)

Spin orbitals are $\chi$ with coordinate $\mathbf x = \{\mathbf r,\omega\}$, and spatial orbitals are $\psi$ with coordinate $\mathbf r$. The one-electron operator $h$ and $r_{12}^{-1}$ act as written.

| | Spin orbitals $\chi$ | Spatial orbitals $\psi$ |
|---|---|---|
| one-electron | $[p|h|q] = \langle p|h|q\rangle = \int\mathrm d\mathbf x_1\,\chi_p^*(1)\,h(1)\,\chi_q(1)$ | $(p|h|q) = h_{pq} = \int\mathrm d\mathbf r_1\,\psi_p^*(1)\,h(1)\,\psi_q(1)$ |
| chemists' | $[pq|rs] = \int\mathrm d\mathbf x_1\mathrm d\mathbf x_2\,\chi_p^*(1)\chi_q(1)\,r_{12}^{-1}\,\chi_r^*(2)\chi_s(2)$ | $(pq|rs) = \int\mathrm d\mathbf r_1\mathrm d\mathbf r_2\,\psi_p^*(1)\psi_q(1)\,r_{12}^{-1}\,\psi_r^*(2)\psi_s(2)$ |
| physicists' | $\langle pq|rs\rangle = \int\mathrm d\mathbf x_1\mathrm d\mathbf x_2\,\chi_p^*(1)\chi_q^*(2)\,r_{12}^{-1}\,\chi_r(1)\chi_s(2)$ | written the same way with $\psi$ and $\mathbf r$ |
| antisymmetrized | $\langle pq||rs\rangle = \langle pq|rs\rangle - \langle pq|sr\rangle$ | |

## How to read them

- **Chemists' (Mulliken).** Group by electron: $(pq|$ is the "charge distribution" $\psi_p^*\psi_q$ of electron 1, and $|rs)$ that of electron 2. Complex-conjugated functions come first in each pair.
- **Physicists' (Dirac).** Group by bra and ket: $\langle pq|$ holds electron 1 then electron 2 (conjugated), and $|rs\rangle$ holds electron 1 then electron 2. The conversion is

$$
\langle pq|rs\rangle = [pr|qs],
\qquad
[pq|rs] = \langle pr|qs\rangle .
$$

- **Antisymmetrized.** The exchange term swaps the two ket labels:

$$
\langle pq||rs\rangle = \langle pq|rs\rangle - \langle pq|sr\rangle = [pr|qs] - [ps|qr].
$$

  It vanishes when $p = q$ or $r = s$, and satisfies $\langle pq||rs\rangle = -\langle qp||rs\rangle = -\langle pq||sr\rangle = \langle qp||sr\rangle$.

!!! warning "Same symbol, different meaning"
    $\langle pq|rs\rangle$ and $(pq|rs)$ with the same four labels are different integrals. Every expression must say which notation it uses. Szabo writes most general formulas in physicists' notation over spin orbitals and switches to chemists' notation over spatial orbitals for closed shells.

## Permutational symmetry

Both integrals are real for real orbitals. In general:

- **Interchange of electron labels.** $\langle pq|rs\rangle = \langle qp|sr\rangle$ and $[pq|rs] = [rs|pq]$.
- **Hermiticity.** $\langle pq|rs\rangle = \langle rs|pq\rangle^*$ and $[pq|rs] = [qp|sr]^*$.
- **Real orbitals.** Additionally $(pq|rs) = (qp|rs) = (pq|sr) = (qp|sr)$, giving the full **8-fold** symmetry of chemists' integrals:
$$
(pq|rs) = (qp|rs) = (pq|sr) = (qp|sr) = (rs|pq) = (sr|pq) = (rs|qp) = (sr|qp).
$$

## Coulomb and exchange integrals

For spatial orbitals,

$$
J_{pq} = (pp|qq) = \langle pq|pq\rangle,
\qquad
K_{pq} = (pq|qp) = \langle pq|qp\rangle .
$$

**Meaning.**

- $J_{pq}$ is the classical Coulomb repulsion between the charge clouds $|\psi_p(\mathbf r_1)|^2$ and $|\psi_q(\mathbf r_2)|^2$.
- $K_{pq}$ has no classical analogue. It arises only from antisymmetry.

**Properties (Szabo Ex. 2.19, 2.20).**

- $J_{pp} = K_{pp}$.
- $J_{pq}^* = J_{pq}$ and $K_{pq}^* = K_{pq}$: both are real.
- $J_{pq} = J_{qp}$ and $K_{pq} = K_{qp}$.
- $J_{pq} > 0$ and $K_{pq} > 0$: $K_{pq}$ is the self-repulsion of the charge distribution $\psi_p^*\psi_q$, and the Coulomb kernel is positive definite.
- For real orbitals, $K_{pq} = (pq|qp) = (pq|pq) = \langle pq|qp\rangle = \langle pp|qq\rangle$.

## In code (PySCF)

`mol.intor("int2e")` and `ao2mo` return **chemists'** integrals over spatial functions, `eri[p,q,r,s] = (pq|rs)`. Convert to physicists' order with `eri.transpose(0,2,1,3)`, which gives `g[p,q,r,s] = <pq|rs>`. Check the convention before contracting with an RDM, since $\Gamma$ in one notation pairs with integrals in the other.

```python
from pyscf import gto, ao2mo
mol = gto.M(atom="H 0 0 0; H 0 0 0.74", basis="sto-3g")
eri = ao2mo.restore(1, mol.intor("int2e", aosym="s8"), mol.nao)   # (pq|rs)
phys = eri.transpose(0, 2, 1, 3)                                   # <pq|rs>
assert abs(phys[0, 1, 0, 1] - eri[0, 0, 1, 1]) < 1e-14            # <01|01> = (00|11) = J
```

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 2.3.2 and 2.3.6, pp. 67-68 and 85-86, Table 2.2, Eqs. (2.179)-(2.185), Ex. 2.19-2.20. PySCF conventions from the PySCF documentation and checked in code.
