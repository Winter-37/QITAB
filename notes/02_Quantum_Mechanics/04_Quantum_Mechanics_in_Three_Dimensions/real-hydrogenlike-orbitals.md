---
id: real-hydrogenlike-orbitals
title: Real hydrogenlike orbitals, radial distribution functions and orbital shapes
summary: Chemists use real orbitals (2p_x, 3d_xy, …), built from the complex ψ_nlm with ±m. They are eigenfunctions of H and L² but not of L_z, and their angular parts are polynomials in x, y, z. Covers radial and angular nodes, the radial distribution function r²R² against the density |ψ|², most probable radius against ⟨r⟩, the nuclear cusp, and what the familiar orbital pictures do and do not show. Real 2p orbitals are two separated distorted ellipsoids, not tangent spheres, and the complex 2p±1 are doughnuts. Checked symbolically - orthonormality of all 14 real orbitals with n ≤ 3, the Cartesian forms, nodes, P(r < a₀) = 1 − 5e⁻² for 1s, the 95% surfaces, and ⟨T⟩(2p) = Z²/8.
status: in-progress
kind: theory
level: introductory
tags: [hydrogen-atom, atomic-orbitals, real-orbitals, radial-distribution, nodes, orbital-shapes, cusp]
prerequisites: [hydrogen-atom, central-potentials-and-spherical-harmonics]
related: [orbital-angular-momentum, molecular-orbitals-of-polyatomic-molecules, homonuclear-diatomic-molecular-orbitals]
conventions: [atomic-units, condon-shortley, real-harmonics]
order: 35
date: 2026-11-20
---

Atomic units with an infinitely heavy nucleus of charge $Z$; lengths are in bohr. For hydrogen with the true reduced mass, multiply lengths by $m_e/\mu = 1.000545$. $\psi_{n\ell m} = R_{n\ell}(r)Y_\ell^m(\theta,\phi)$ are the complex eigenfunctions of [[hydrogen-atom]].

## From complex to real orbitals

The energy depends only on $n$, so any combination of degenerate $\psi_{n\ell m}$ is again an eigenfunction of $\hat H$ with the same energy. Combinations with fixed $\ell$ are also eigenfunctions of $\hat L^2$. Combining $m$ and $-m$ removes the factor $e^{\pm i|m|\phi}$. With Condon–Shortley phases,

$$
p_x = \frac{Y_1^{-1} - Y_1^{1}}{\sqrt2} = \sqrt{\frac{3}{4\pi}}\,\frac{x}{r},\qquad
p_y = i\,\frac{Y_1^{-1} + Y_1^{1}}{\sqrt2} = \sqrt{\frac{3}{4\pi}}\,\frac{y}{r},\qquad
p_z = Y_1^0 = \sqrt{\frac{3}{4\pi}}\,\frac{z}{r} .
$$

In general one replaces $e^{im\phi}/\sqrt{2\pi}$ by $\pi^{-1/2}\cos|m|\phi$ or $\pi^{-1/2}\sin|m|\phi$; for $m = 0$ nothing changes. Levine drops the Condon–Shortley sign in his complex functions, so his combination for $2p_x$ reads $(2p_{-1} + 2p_1)/\sqrt2$; the result is the same real function.

| Orbital | angular factor × $\sqrt{4\pi}$ | Cartesian form of $\psi$ |
|---|---|---|
| $2p_x, 2p_y, 2p_z$ | $\sqrt3\,(x, y, z)/r$ | $\dfrac{Z^{5/2}}{4\sqrt{2\pi}}\,(x, y, z)\,e^{-Zr/2}$ |
| $3d_{xy}, 3d_{xz}, 3d_{yz}$ | $\sqrt{15}\,(xy, xz, yz)/r^2$ | $\dfrac{\sqrt2 Z^{7/2}}{81\sqrt\pi}\,(xy, xz, yz)\,e^{-Zr/3}$ |
| $3d_{x^2-y^2}$ | $\tfrac{\sqrt{15}}2(x^2-y^2)/r^2$ | $\dfrac{\sqrt2 Z^{7/2}}{162\sqrt\pi}(x^2-y^2)e^{-Zr/3}$ |
| $3d_{z^2}$ | $\tfrac{\sqrt5}2(3z^2-r^2)/r^2$ | $\dfrac{\sqrt6 Z^{7/2}}{486\sqrt\pi}(3z^2-r^2)e^{-Zr/3}$ |

The subscripts are the Cartesian polynomials themselves, which is why real orbitals transform simply under molecular symmetry operations ([[molecular-orbitals-of-polyatomic-molecules]]).

- **Not $\hat L_z$ eigenfunctions.** $\hat L^2\,2p_x = 2\,2p_x$, but $\hat L_z 2p_x / 2p_x = i\tan\phi$ is not a constant, so $2p_x$ is not an eigenfunction of $\hat L_z$. The complex orbitals are the right choice when $\hat L_z$ matters, as in atoms in a magnetic field and in linear molecules.

!!! example "Symbolic checks"
    - **Orthonormality.** All 14 real orbitals with $n \le 3$ ($1s$ to $3d$) are orthonormal: the overlap matrix is exactly the identity.
    - **Cartesian forms.** Each ratio $\psi/[\text{polynomial}\times e^{-Zr/n}]$ reduces to the constant in the table above.

## Nodes

$R_{n\ell}$ is $r^\ell$ times a polynomial of degree $n - \ell - 1$ (with real positive roots) times $e^{-Zr/n}$. Every orbital therefore has

- $n - \ell - 1$ **radial nodes** (spheres), and
- $\ell$ **angular nodes** (planes or cones), for $n - 1$ nodal surfaces in all.

For $Z = 1$ the radial nodes are at $r = 2$ (2s), $r = (9 \mp 3\sqrt3)/2 = 1.902, 7.098$ (3s) and $r = 6$ (3p). The angular nodes are:

- $2p_z$ and $3p_z$: the $xy$ plane.
- $3d_{x^2-y^2}$: the planes $x = \pm y$.
- $3d_{xy}$: the $xz$ and $yz$ planes.
- $3d_{z^2}$: two cones at $\theta = 54.74°$ and $125.26°$, where $\cos^2\theta = 1/3$.

## Probability density against radial distribution

The probability of finding the electron in a thin shell between $r$ and $r + \mathrm dr$, at any angle, is

$$
\int|\psi_{n\ell m}|^2\,r^2\sin\theta\,\mathrm d\theta\,\mathrm d\phi\;\mathrm dr = R_{n\ell}^2(r)\,r^2\,\mathrm dr ,
$$

because the spherical harmonics are normalized. $R_{n\ell}^2r^2$ is the **radial distribution function**. For 1s the density $|\psi|^2 \propto e^{-2Zr}$ is largest at the nucleus, but $R^2r^2$ vanishes there and peaks at $r = 1/Z$ (one Bohr radius for H). The two statements are not in conflict: the density falls as $r$ grows while the shell volume $4\pi r^2\mathrm dr$ grows, and their product peaks at $a_0/Z$.

!!! example "Most probable and mean radii (Z = 1)"
    | | 1s | 2s | 2p | 3s | 3p | 3d |
    |---|---:|---:|---:|---:|---:|---:|
    | maximum of $r^2R^2$ | 1 | 5.236 | 4 | 13.074 | 12 | 9 |
    | $\langle r\rangle = \tfrac12[3n^2 - \ell(\ell+1)]$ | 1.5 | 6 | 5 | 13.5 | 12.5 | 10.5 |

    - **Most probable radius.** For $\ell = n-1$ there is one maximum, at $n^2$ (the Bohr-model radius). Orbitals with radial nodes have their largest peak further out (2s: $3 + \sqrt5$).
    - **Inside one Bohr radius.** $P(r < a_0)$ is $1 - 5e^{-2} = 0.3233$ for 1s and $1 - \tfrac{65}{24}e^{-1} = 0.00366$ for 2p.
    - **95% sphere.** A sphere of radius $3.148\,a_0$ contains 95% of the 1s probability.
    - **Penetration.** The 2s distribution has an inner hump inside 2 bohr, where 2p has almost no probability. This is the penetration that makes 2s lie below 2p in many-electron atoms ([[helium-excited-states-perturbation]]).

## The cusp

For every $s$ state,

$$
\Big(\frac{1}{R}\frac{\mathrm dR}{\mathrm dr}\Big)_{r=0} = -Z ,
$$

checked symbolically for 1s, 2s and 3s. Along a line through the nucleus, $\psi$ has a kink: its slope jumps from $+Z\psi(0)$ to $-Z\psi(0)$. The kink is forced by the $-Z/r$ singularity of the potential. Gaussian basis functions have zero slope at the nucleus and cannot reproduce it.

## What orbital pictures show

There are two different kinds of picture:

1. **Graphs of the angular factor**, $|Y(\theta,\phi)|$ plotted as a distance from the origin. For $p_z$ this gives two spheres tangent at the origin. It is a graph of a function, **not** the shape of the orbital.
2. **Contour surfaces of constant $|\psi|$**, usually chosen to enclose 90% or 95% of the probability. These are the orbital shapes.

For $2p_y$ in the $yz$ plane, $|\psi| \propto r e^{-kr}|\sin\theta|$ with $k = Z/2$. The function depends only on $y$ and $x^2 + z^2$, so the contour surface is a cross section rotated about the $y$ axis: **two separated, distorted ellipsoids**. The complex $2p_{\pm1}$ have $|\psi| \propto re^{-kr}\sin\theta$, a function of $z$ and $x^2 + y^2$, so their surface is the same cross section rotated about $z$: a **doughnut**.

!!! example "The 95% surface of 2p_z (Z = 1)"
    **Method.** Grid integration in cylindrical coordinates finds the contour value $|\psi|^2 = 3.59\times10^{-5}$ bohr⁻³ such that the region with larger $|\psi|^2$ holds 95% of the probability.

    **Result.** Each lobe extends from $|z| = 0.06$ to $|z| = 10.27$ bohr and reaches 7.4 bohr from the axis. The lobes never touch, because $\psi$ vanishes on the whole $xy$ plane. Near the origin the contour is $|z| \approx 0.06\,e^{r/2}$.

**Kinetic energy.** For $2p_0$, direct integration gives $\langle T\rangle = Z^2/8\,E_h$, equal to $-E_2$, as the virial theorem requires.

## Source

Levine, *Quantum Chemistry* (7th ed., Pearson, 2014), Sec. 6.6, pp. 135-143 (radial factors and nodes, Eqs. (6.100)-(6.104); reduced mass and Bohr radius, Eqs. (6.105)-(6.108); cusp, Eq. (6.109); s, p, d labels; radial distribution function, Eqs. (6.115)-(6.117) and Figs. 6.8-6.9; $P(r < a)$ example). Sec. 6.7, pp. 143-147 (real orbitals, Eqs. (6.118)-(6.122) and Table 6.2; graphs against contour surfaces, Eqs. (6.123)-(6.124), Figs. 6.10-6.14). Calculations in `part2_levine_gaps.py`, section A (SymPy; NumPy for the contour).
