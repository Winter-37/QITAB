---
id: lithium-ground-state
title: The lithium ground state - Pauli principle, perturbation theory and screened orbitals
summary: Why lithium's ground configuration is 1s²2s, a 3×3 Slater determinant, and not 1s³. Covers the zeroth-order energy (−275.5 eV) and the first-order correction E⁽¹⁾ = 2J₁ₛ₂ₛ + J₁ₛ₁ₛ − K₁ₛ₂ₛ (exact fraction 5965/1944 E_h), giving −192.0 eV against the exact −203.5 eV. Then a variational determinant with separate effective charges for 1s and 2s (Wilson's function). Minimizing it gives b₁ = 2.680, b₂ = 1.868 and W = −201.19 eV (Levine: 2.686, 1.776, −201.2 eV). W is flat along b₂, and a nodeless Slater 2s does better (−201.85 eV). Hartree–Fock limit −202.3 eV, so the correlation energy is 1.25 eV.
status: needs-revision
kind: derivation
level: intermediate
tags: [lithium, slater-determinants, pauli-principle, perturbation-theory, variation-method, screening, effective-nuclear-charge, many-electron-atoms]
prerequisites: [helium-excited-states-perturbation, helium-ground-state-variational, slater-determinants, exchange-symmetry-spin-and-symmetrization-principle]
related: [periodic-table-and-term-symbols, helium-atom-independent-particle-model, hartree-fock-equations, spin-orbitals-and-antisymmetry]
conventions: [atomic-units]
order: 10
date: 2026-11-20
---

Atomic units, infinite nuclear mass, $Z = 3$:

$$
\hat H = \underbrace{\sum_{i=1}^3\Big(-\tfrac12\nabla_i^2 - \frac Z{r_i}\Big)}_{\hat H^0} + \underbrace{\frac1{r_{12}} + \frac1{r_{13}} + \frac1{r_{23}}}_{\hat H'} .
$$

## Why not 1s³

$\hat H^0$ is a sum of hydrogenlike Hamiltonians, so a product of three 1s orbitals would be its lowest eigenfunction. But the wave function must be antisymmetric in all coordinates, spin included ([[exchange-symmetry-spin-and-symmetrization-principle]]). The antisymmetrized product of the spin orbitals $1s\alpha$, $1s\beta$ and $1s\alpha$ is a determinant with two identical columns, which vanishes. At most two electrons fit in an orbital, so the third goes into $n = 2$.

The ground configuration is 1s²2s, a single [[slater-determinants|Slater determinant]] $|1s\,\overline{1s}\,2s|$ (bar = $\beta$ spin). In the unperturbed problem, 2s and 2p are degenerate; the $1/r_{ij}$ terms put 2s lower, by the same penetration argument as for helium ([[helium-excited-states-perturbation]]).

## Perturbation theory

Each of the six terms of the determinant is an eigenfunction of $\hat H^0$ with eigenvalue $E_{1s} + E_{1s} + E_{2s}$, so

$$
E^{(0)} = -\frac{Z^2}{2}\Big(1 + 1 + \frac14\Big) = -\frac{81}{8}\,E_h = -275.5\ \text{eV}.
$$

**First order.** Average $\hat H'$ over the determinant. For each pair of spin orbitals there is a Coulomb term, minus an exchange term if their spins are equal:

$$
E^{(1)} = \langle\psi^{(0)}|\hat H'|\psi^{(0)}\rangle = 2J_{1s2s} + J_{1s1s} - K_{1s2s} ,
$$

The terms count as follows:

- **$J_{1s1s}$:** the $1s\alpha$–$1s\beta$ pair (no exchange, opposite spins).
- **$2J_{1s2s}$:** the two 1s–2s pairs.
- **$-K_{1s2s}$:** exchange for the same-spin pair $1s\alpha$–$2s\alpha$ only.

With $J_{1s1s} = 5Z/8$, $J_{1s2s} = 17Z/81$ and $K_{1s2s} = 16Z/729$ (derived in [[helium-excited-states-perturbation]]),

$$
E^{(1)} = Z\Big(\frac58 + \frac{34}{81} - \frac{16}{729}\Big) = \frac{5965}{1944}\,E_h = 83.5\ \text{eV},\qquad
E^{(0)} + E^{(1)} = -7.0566\,E_h = -192.0\ \text{eV}.
$$

The exact ground-state energy is −203.5 eV. Higher orders would bring in other configurations (configuration interaction).

## Variation with screened orbitals

The 2s electron is largely shielded from the nucleus by the 1s pair, and the 1s electrons partly shield each other. So give each shell its own effective charge:

$$
f = \Big(\frac{b_1^3}{\pi}\Big)^{1/2}e^{-b_1r},\qquad g = N\,(2 - b_2r)\,e^{-b_2r/2},\qquad
\phi = |f\,\bar f\,g| .
$$

**The determinant is easy to evaluate.** With $b_1 \ne b_2$, $f$ and $g$ are not orthogonal. But $f$ and $g$ appear only with $\alpha$ spin, so replacing $g$ by $g' = (g - Sf)/\sqrt{1 - S^2}$, with $S = \langle f|g\rangle$, adds a multiple of one column to another. That leaves the determinant unchanged apart from normalization. The energy is then the orthonormal-orbital expression

$$
W = 2h_{ff} + h_{g'g'} + J_{ff} + 2J_{fg'} - K_{fg'} .
$$

!!! example "Minimizing W for lithium"
    **Method.** All integrals are of spherically symmetric functions, so only the $k = 0$ term of $1/r_{12}$ survives. They are done on a radial grid; at $b_1 = b_2 = 3$ this reproduces $E^{(0)} + E^{(1)}$ to $2\times10^{-5}\,E_h$.

    | Trial function | $b_1$ | $b_2$ | $W$ ($E_h$) | $W$ (eV) |
    |---|---:|---:|---:|---:|
    | $Z = 3$ hydrogenlike ($E^{(0)} + E^{(1)}$) | 3 | 3 | −7.0566 | −192.0 |
    | 2s form above, optimized | 2.680 | 1.868 | −7.39358 | −201.19 |
    | same, $b_2$ fixed at Wilson's 1.776 | 2.676 | 1.776 | −7.39226 | −201.15 |
    | nodeless Slater 2s, $r\,e^{-b_2r/2}$, optimized | 2.686 | 1.275 | −7.41790 | −201.85 |
    | Hartree–Fock limit (ROHF/cc-pV5Z) | | | −7.43272 | −202.26 |
    | exact (Levine) | | | −7.4785 | −203.5 |

    - **Comparison with Levine.** Levine quotes Wilson (1933): $b_1 = 2.686$, $b_2 = 1.776$, $W = -201.2$ eV. The minimum energy agrees, and so does $b_1$ (to 0.006), but the minimizing $b_2$ here is 1.868. The surface is very flat along $b_2$: fixing $b_2 = 1.776$ costs only 1.3 m$E_h$ (0.04 eV), less than the rounding of −201.2 eV. Whether Wilson's 2s function had exactly this form is **to verify** against the original paper.
    - **Screening.** $b_1 \approx 2.68$ is close to the helium-like $Z - 5/16 = 2.6875$. $b_2$ shows strong, but not complete, screening of the 2s electron by the 1s pair.
    - **A nodeless 2s helps.** The Slater-type 2s does better by 0.66 eV. The radial node is not lost: after orthogonalization to $f$, $g'$ has one, placed where the energy wants it rather than fixed by $b_2$.
    - **Limits of one determinant.** No choice of orbitals in a single determinant can go below the Hartree–Fock limit. The remaining 0.046 $E_h$ (1.25 eV) is the correlation energy, which needs $r_{ij}$-dependent terms or several determinants.

## Source

Levine, *Quantum Chemistry* (7th ed., Pearson, 2014), Sec. 10.5, pp. 273-277 (Pauli principle, why 1s³ is forbidden); Sec. 10.6, pp. 277-278 (Slater determinants, Eqs. (10.40)-(10.47)); Sec. 10.7, pp. 278-279 (perturbation treatment, Eqs. (10.48)-(10.51), −275.5 and −192.0 eV against −203.5 eV); Sec. 10.8, pp. 279-280 (two-parameter variation function, Eqs. (10.52)-(10.54), and Wilson's results as quoted: E. B. Wilson Jr., *J. Chem. Phys.* **1**, 210 (1933)). Calculations in `part2_levine_gaps.py`, section C (SymPy for the integrals, NumPy radial grid for W; PySCF ROHF/cc-pV5Z for the HF limit).
