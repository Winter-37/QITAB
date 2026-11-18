---
id: spin-orbital-to-spatial-orbital
title: From spin orbitals to spatial orbitals (integrating out spin)
summary: How spin-orbital integrals reduce to spatial integrals for restricted orbitals, the closed-shell energy E0 = 2Σh_ii + ΣΣ(2J_ij − K_ij), exchange lowering of parallel-spin pairs, the pseudo-classical bookkeeping of determinant energies, and the closed-shell MP2 formula as a worked conversion.
status: in-progress
kind: derivation
level: intermediate
tags: [spin-integration, closed-shell, rhf-energy, coulomb, exchange, mp2]
prerequisites: [slater-condon-rules, integral-notation]
related: [minimal-basis-h2-model, spin-adapted-configurations]
conventions: [ia-letters, chemists-integrals, physicists-integrals, antisymmetrized-integrals]
order: 60
date: 2026-11-03
---

## Restricted spin orbitals and bar notation

Restricted spin orbitals share one spatial function for both spins:

$$
\chi_p(\mathbf x) = \psi_q(\mathbf r)\alpha(\omega)\equiv\psi_q,
\qquad
\chi_p(\mathbf x) = \psi_q(\mathbf r)\beta(\omega)\equiv\bar\psi_q .
$$

A bar marks $\beta$. Integrating over $\omega$ uses only $\langle\alpha|\alpha\rangle = \langle\beta|\beta\rangle = 1$ and $\langle\alpha|\beta\rangle = 0$.

**One-electron integrals.** $h$ is spin-free:

$$
[\psi_p|h|\psi_q] = [\bar\psi_p|h|\bar\psi_q] = (\psi_p|h|\psi_q) = h_{pq},
\qquad
[\psi_p|h|\bar\psi_q] = 0 .
$$

**Two-electron integrals (chemists').** Each charge distribution $\chi^*\chi$ must have matching spins, or the integral vanishes:

$$
[pq|rs] \text{ (spin orbitals)} = (pq|rs) \text{ (spatial)}\times\delta_{\sigma_i\sigma_j}\,\delta_{\sigma_k\sigma_l}.
$$

So $[\psi_p\psi_q|\bar\psi_r\bar\psi_s] = (pq|rs)$, but $[\psi_p\bar\psi_q|\psi_r\bar\psi_s] = 0$. In physicists' notation, spins must match between positions 1 and 3 and between 2 and 4.

## Closed-shell determinant energy

A closed shell has $N/2$ spatial orbitals each doubly occupied:

$$
|\Psi_0\rangle = |\psi_1\bar\psi_1\cdots\psi_i\bar\psi_i\cdots\psi_{N/2}\bar\psi_{N/2}\rangle .
$$

Split the spin-orbital sums of [[slater-condon-rules]] into $\alpha$ and $\beta$ parts:

$$
\sum_i^N\chi_i = \sum_i^{N/2}\psi_i + \sum_i^{N/2}\bar\psi_i .
$$

- **One-electron part.** $\sum_i^N\langle i|h|i\rangle = 2\sum_i^{N/2}h_{ii}$.
- **Two-electron part.** In $\tfrac12\sum_{i,j}^N\big([ii|jj] - [ij|ji]\big)$ the Coulomb term survives for all four spin pairs, giving $4\cdot\tfrac12(ii|jj)$. The exchange term survives only for same-spin pairs, giving $2\cdot\tfrac12(ij|ji)$.

Hence

$$
E_0 = 2\sum_i^{N/2}h_{ii} + \sum_i^{N/2}\sum_j^{N/2}\big[2(ii|jj) - (ij|ji)\big]
= 2\sum_i^{N/2}h_{ii} + \sum_i^{N/2}\sum_j^{N/2}\big(2J_{ij} - K_{ij}\big),
$$

or in physicists' notation, $E_0 = 2\sum_i\langle i|h|i\rangle + \sum_{ij}\big(2\langle ij|ij\rangle - \langle ij|ji\rangle\big)$.

**Physical reading.** $h_{ii}$ is the mean kinetic plus nuclear-attraction energy of an electron in $\psi_i$. $J_{ij}$ is the Coulomb repulsion of charge clouds, and $K_{ij}$ is the exchange correction for same-spin pairs. Terms with $i=j$ give $2J_{ii} - K_{ii} = J_{ii}$, the repulsion of the two electrons sharing $\psi_i$. For minimal-basis H$_2$, $E_0 = 2h_{11} + J_{11}$ ([[minimal-basis-h2-model]]).

## Rules for any determinant (pseudo-classical bookkeeping)

The energy of any single determinant of restricted orbitals is:

1. $h_{pp}$ for each electron in $\psi_p$, whatever its spin.
2. $J_{pq}$ for **every** pair of electrons, one in $\psi_p$ and one in $\psi_q$ (including two electrons in the same $\psi_p$, which gives $J_{pp}$).
3. $-K_{pq}$ for every pair of electrons with **parallel** spins in different spatial orbitals.

!!! example "Parallel versus antiparallel spins (Szabo Eqs. 2.186-2.187, Ex. 2.22)"
    Two electrons in $\psi_1$ and $\psi_2$:
    $$
    E(\uparrow\downarrow) = \langle\psi_1\bar\psi_2|\hat H|\psi_1\bar\psi_2\rangle = h_{11} + h_{22} + J_{12},
    $$
    $$
    E(\uparrow\uparrow) = \langle\psi_1\psi_2|\hat H|\psi_1\psi_2\rangle = h_{11} + h_{22} + J_{12} - K_{12}.
    $$
    Since $K_{12}>0$, the parallel-spin determinant is lower. The Fermi hole keeps same-spin electrons apart and reduces their repulsion ([[slater-determinants]]).

    For contrast, the Hartree products $\psi_1(\mathbf r_1)\alpha(\omega_1)\psi_2(\mathbf r_2)\beta(\omega_2)$ and $\psi_1(\mathbf r_1)\beta(\omega_1)\psi_2(\mathbf r_2)\beta(\omega_2)$ both have energy $h_{11}+h_{22}+J_{12}$. A product has no exchange term, so its energy does not depend on the spins.

    With the minimal-basis H$_2$ numbers ($R = 1.4$ bohr, STO-3G): $h_{11}+h_{22}+J_{12} = -1.064835$ and $h_{11}+h_{22}+J_{12}-K_{12} = -1.246093$ hartree (electronic).

## Full CI of minimal-basis H2 in spatial form (Szabo Ex. 2.17, 2.21)

$$
\mathbf H = \begin{pmatrix} 2h_{11} + J_{11} & K_{12}\\ K_{12} & 2h_{22} + J_{22}\end{pmatrix}.
$$

The off-diagonal element is $\langle1\bar1||2\bar2\rangle = \langle1\bar1|2\bar2\rangle - \langle1\bar1|\bar22\rangle = (12|12) - 0$. For real orbitals $(12|12) = (12|21) = K_{12}$.

## Worked conversion: closed-shell MP2 (Szabo Ex. 2.18)

The second-order energy over spin orbitals is

$$
E_0^{(2)} = \frac14\sum_{ijab}\frac{|\langle ij||ab\rangle|^2}{\varepsilon_i + \varepsilon_j - \varepsilon_a - \varepsilon_b}.
$$

**Expand.** Write $|\langle ij||ab\rangle|^2 = |\langle ij|ab\rangle|^2 + |\langle ij|ba\rangle|^2 - 2\,\mathrm{Re}\,\langle ij|ab\rangle\langle ab|ji\rangle$. The two squared terms give equal sums after relabelling $a\leftrightarrow b$, so

$$
E_0^{(2)} = \frac12\sum_{ijab}\frac{|\langle ij|ab\rangle|^2 - \langle ij|ab\rangle\langle ab|ji\rangle}{\varepsilon_i+\varepsilon_j-\varepsilon_a-\varepsilon_b}.
$$

**Count spin cases.** Restricted orbitals have $\varepsilon_i = \varepsilon_{\bar i}$, and each spatial label carries a spin.

- $\langle ij|ab\rangle$ needs $\sigma_a = \sigma_r$ and $\sigma_b = \sigma_s$: 4 spin assignments.
- The product $\langle ij|ab\rangle\langle ab|ji\rangle$ needs all four spins equal: 2 assignments.

This gives

$$
E_0^{(2)} = \sum_{ij}^{N/2}\sum_{ab}^{K}{}'\ \frac{(ia|jb)\big[2(ai|bj) - (aj|bi)\big]}{\varepsilon_i+\varepsilon_j-\varepsilon_a-\varepsilon_b}.
$$

Here $i,j$ run over the occupied spatial orbitals $1..N/2$, $a,b$ over the virtual spatial orbitals $N/2+1..K$, and the integrals are chemists' notation. In physicists' notation the numerator is $\langle ij|ab\rangle\big(2\langle ab|ij\rangle - \langle ab|ji\rangle\big)$, the form printed in Szabo (p. 85). For real orbitals the two forms are identical term by term.

**Numerical check.** H$_2$O/STO-3G (O at the origin, H at $(0,\pm0.757,0.587)$ Å). The spin-orbital formula and the closed-shell formula both give $E^{(2)} = -0.035566818$ hartree, identical to PySCF `mp.MP2(mf).e_corr`.

## Source

Szabo and Ostlund, *Modern Quantum Chemistry* (Dover, 1996; reprint of the revised first edition, McGraw-Hill, 1989), Sec. 2.3.5-2.3.7, pp. 81-89, Eqs. (2.159)-(2.189), Ex. 2.17-2.23. Numbers computed with PySCF 2.14 for this note.
