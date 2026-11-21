---
id: helium-excited-states-perturbation
title: The first excited states of helium by degenerate perturbation theory
summary: The 1s2s and 1s2p configurations of helium form an eightfold-degenerate unperturbed level at −68.03 eV. Parity and reflection make the 8×8 secular determinant block-diagonal (four 2×2 blocks), giving the levels J ± K. Exchange degeneracy and ℓ degeneracy are lifted, but m degeneracy is not. All five Coulomb and exchange integrals are derived and checked exactly (J₁ₛ₂ₛ = 17Z/81, K₁ₛ₂ₛ = 16Z/729, J₁ₛ₂ₚ = 59Z/243, K₁ₛ₂ₚ = 112Z/6561). First-order energies are −57.8, −55.4, −55.75 and −53.9 eV, which put 2³P below 2¹S. A 96-function two-electron CI gives −59.19, −58.39, −58.04 and −57.79 eV (2³S < 2¹S < 2³P < 2¹P), within 0.06 eV of Levine's third-order values.
status: in-progress
kind: derivation
level: intermediate
tags: [helium, degenerate-perturbation-theory, coulomb-integral, exchange-integral, excited-states, secular-equation, symmetry, parity]
prerequisites: [degenerate-perturbation-theory, helium-atom-independent-particle-model, real-hydrogenlike-orbitals, parity-and-parity-selection-rules]
related: [helium-ground-state-variational, exchange-symmetry-spin-and-symmetrization-principle, bosons-fermions-and-exchange-forces, periodic-table-and-term-symbols, full-ci]
conventions: [atomic-units, real-harmonics]
order: 13
date: 2026-11-20
---

Atomic units, infinite nuclear mass. $\hat H^0 = \sum_{i=1,2}(-\tfrac12\nabla_i^2 - Z/r_i)$ and $\hat H' = 1/r_{12}$, with $Z = 2$. Orbitals are the real hydrogenlike functions of [[real-hydrogenlike-orbitals]]. Spin is ignored until the end: $\hat H$ contains no spin, so the spatial and spin problems separate.

## Using symmetry to simplify a secular equation

Suppose an operator $\hat A$ commutes with both $\hat H^0$ and $\hat H'$. Choose the degenerate unperturbed functions as eigenfunctions of $\hat A$. Then $H'_{ij} = 0$ whenever $\psi_i^{(0)}$ and $\psi_j^{(0)}$ have different eigenvalues of $\hat A$ (the theorem behind [[degenerate-perturbation-theory]]).

- **Diagonal case.** If all the eigenvalues differ, the secular determinant is diagonal, the chosen functions are already the correct zeroth-order functions, and $E_n^{(1)} = \langle\psi_n^{(0)}|\hat H'|\psi_n^{(0)}\rangle$.
- **Block case.** If some eigenvalues coincide, the determinant is block-diagonal, and each correct zeroth-order function is a combination of functions with the same eigenvalue only.
- **Converse.** If the starting functions are the correct zeroth-order functions, the secular determinant is diagonal.

## The eightfold-degenerate level

Promoting one electron to $n = 2$ gives

$$
E^{(0)} = -\frac{Z^2}{2}\Big(1 + \frac14\Big) = -2.5\,E_h = -68.03\ \text{eV}.
$$

The level is eightfold degenerate:

$$
\psi_{1,2}^{(0)} = 1s(1)2s(2),\ 2s(1)1s(2);\qquad
\psi_{3,4}^{(0)} = 1s(1)2p_x(2),\ 2p_x(1)1s(2);\qquad
\psi_{5,6}^{(0)},\ \psi_{7,8}^{(0)}\ \text{the same with } 2p_y,\ 2p_z .
$$

**Most of the 64 elements vanish by symmetry.** $r_{12}$ is unchanged by inverting all six coordinates and by reflecting $x_1, x_2$ (or $y_1, y_2$, or $z_1, z_2$) together.

- **Inversion.** $1s$ and $2s$ are even and $2p$ is odd, so every element between an $s$ pair ($\psi_1, \psi_2$) and an $sp$ pair ($\psi_3, \ldots, \psi_8$) changes sign under inversion and vanishes.
- **Reflections.** Reflecting the $x$ coordinates changes the sign of $2p_x$ but not of $2p_y$ or $2p_z$. This kills every element between the $p_x$, $p_y$ and $p_z$ pairs.

What remains is four 2×2 blocks, each of the form

$$
\begin{vmatrix} J - E^{(1)} & K\\ K & J - E^{(1)}\end{vmatrix} = 0
\quad\Longrightarrow\quad E^{(1)} = J \mp K,\qquad \psi^{(0)} = 2^{-1/2}\,[a(1)b(2) \mp b(1)a(2)] .
$$

The diagonal element is a **Coulomb integral** and the off-diagonal one an **exchange integral**:

$$
J_{ab} = \Big\langle a(1)b(2)\Big|\frac1{r_{12}}\Big|a(1)b(2)\Big\rangle,\qquad
K_{ab} = \Big\langle a(1)b(2)\Big|\frac1{r_{12}}\Big|b(1)a(2)\Big\rangle .
$$

The two diagonal elements of each block are equal, as one sees by relabelling the dummy integration variables 1 ↔ 2. The three $p$ blocks are identical, as one sees by relabelling $x \leftrightarrow y$ or $x \leftrightarrow z$.

## The integrals

**Method.** Expand $1/r_{12} = \sum_k (r_<^k/r_>^{k+1})P_k(\cos\gamma_{12})$ and integrate over angles. For $s$ orbitals only $k = 0$ survives. For the $1s$–$2p$ exchange integral only $k = 1$ survives, with angular factor $\tfrac13$. In terms of Slater radial integrals

$$
R^k(ab;cd) = \int_0^\infty\!\!\int_0^\infty R_a(r_1)R_c(r_1)R_b(r_2)R_d(r_2)\,\frac{r_<^k}{r_>^{k+1}}\,r_1^2r_2^2\,\mathrm dr_1\mathrm dr_2 ,
$$

this gives $J_{1s2s} = R^0(1s2s;1s2s)$, $K_{1s2s} = R^0(1s2s;2s1s)$, $J_{1s2p} = R^0(1s2p;1s2p)$ and $K_{1s2p} = \tfrac13R^1(1s2p;2p1s)$.

| Integral | exact (SymPy) | $Z = 2$ (eV) |
|---|---|---:|
| $J_{1s1s}$ | $5Z/8$ | 34.01 |
| $J_{1s2s}$ | $17Z/81$ | 11.42 |
| $K_{1s2s}$ | $16Z/729$ | 1.19 |
| $J_{1s2p}$ | $59Z/243$ | 13.21 |
| $K_{1s2p}$ | $112Z/6561$ | 0.93 |

All five agree exactly with Levine.

## First-order levels and what they get wrong

| Level | $E^{(0)} + E^{(1)}$ | Spatial function | First order (eV) | CI (eV) | Levine, through $E^{(3)}$ (eV) |
|---|---|---|---:|---:|---:|
| 2³S | $E^{(0)} + J_{1s2s} - K_{1s2s}$ | $2^{-1/2}[1s2s - 2s1s]$ | −57.80 | −59.19 | −59.2 |
| 2¹S | $E^{(0)} + J_{1s2s} + K_{1s2s}$ | $2^{-1/2}[1s2s + 2s1s]$ | −55.41 | −58.39 | −58.4 |
| 2³P | $E^{(0)} + J_{1s2p} - K_{1s2p}$ | $2^{-1/2}[1s2p - 2p1s]$ | −55.74 | −58.04 | −58.1 |
| 2¹P | $E^{(0)} + J_{1s2p} + K_{1s2p}$ | $2^{-1/2}[1s2p + 2p1s]$ | −53.89 | −57.79 | −57.8 |

**Method of the CI column.** A spin-adapted two-electron CI in an even-tempered basis (24 s, 14 p and 6 d shells; 96 functions), with each state found as the lowest root of its symmetry and spin. The same calculation gives the ground state at $-2.90268\,E_h$, 1.0 m$E_h$ above the exact $-2.903724\,E_h$ ([[helium-ground-state-variational]]), so the excited levels should be good to a few hundredths of an eV.

- **Exchange degeneracy is lifted.** The correct zeroth-order functions do not assign either electron to a definite orbital, which reflects the indistinguishability of electrons. The antisymmetric spatial function goes with the triplet spin functions ([[exchange-symmetry-spin-and-symmetrization-principle]]). Since $K > 0$ it lies lower, so each triplet is below its singlet.
- **$\ell$ degeneracy is lifted.** $J_{1s2s} < J_{1s2p}$. A 2s electron penetrates the 1s charge cloud more than a 2p electron ([[real-hydrogenlike-orbitals]]) and so feels less repulsion from it. In many-electron atoms, orbital energies with the same $n$ rise with $\ell$.
- **$m$ degeneracy survives.** Each 1s2p level stays triply degenerate (spatially). Only an external field removes it, and any combination of the $p_x$, $p_y$, $p_z$ functions (or $p_{1,0,-1}$) is an equally correct zeroth-order set.
- **First order gets the order wrong.** It puts 2³P (−55.74 eV) below 2¹S (−55.41 eV). With higher orders, or the CI, the order is 2³S < 2¹S < 2³P < 2¹P, as the spectrum shows. $1/r_{12}$ is not a small perturbation. The first-order wave-function correction already mixes in other configurations (configuration interaction).
- **The configuration label** (1s2s, 1s2p) names only the configuration that contributes most to the state.

## Source

Levine, *Quantum Chemistry* (7th ed., Pearson, 2014), Sec. 9.6, pp. 248-250 (diagonal and block-diagonal secular determinants, Eqs. (9.88)-(9.91); choosing unperturbed functions as eigenfunctions of an operator commuting with $\hat H^0$ and $\hat H'$). Sec. 9.7, pp. 250-256 (unperturbed level (9.92)-(9.93); parity and reflection arguments; Coulomb and exchange integrals (9.97)-(9.100); roots (9.102)-(9.109); integral values; Figs. 9.3-9.4 with the Knight–Scherr higher-order results; the three kinds of degeneracy; penetration). Calculations in `part2_levine_gaps.py`, section B (SymPy for the integrals; NumPy/PySCF integrals for the CI).
