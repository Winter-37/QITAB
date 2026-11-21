---
id: molecular-symmetry-and-point-groups
title: Molecular symmetry - symmetry elements, operations and point groups
summary: The four kinds of symmetry element (Cₙ, σ, i, Sₙ) and their operations, with Sₙ¹ = σ, Sₙ² = i and Cₙⁿ = E. Covers products and non-commutation, 3×3 matrix representatives, and the function operators Ô_R that commute with the molecular Hamiltonian (Ô_i is parity; Ô_C₄ turns 2p_x into 2p_y). Also the classification of point groups (C₁, C_s, C_i; Cₙ, Cₙₕ, Cₙᵥ, S₂ₙ; Dₙ, Dₙₕ, Dₙd; T_d, Oₕ, Iₕ; C∞ᵥ, D∞ₕ), a practical procedure for assigning one, and the symmetry rules for dipole moments and optical activity. Checked on 17 molecules from C₁ to Oₕ - a brute-force search finds every symmetry operation, the group orders and PySCF's assignments agree, and computed dipoles vanish exactly where the rule says.
status: in-progress
kind: theory
level: introductory
tags: [symmetry, point-groups, symmetry-operations, group-theory, dipole-moment, chirality, molecular-structure]
prerequisites: [groups-representations-and-characters, parity-and-parity-selection-rules]
related: [molecular-orbitals-of-polyatomic-molecules, symmetry-conservation-and-degeneracy, rotation-operator-and-rotational-symmetry, real-hydrogenlike-orbitals]
order: 10
date: 2026-11-20
---

The symmetry of a molecule means the symmetry of its nuclear framework at the equilibrium geometry of a given electronic state. It can change between states: HCN is linear in its ground state but bent in some excited states.

## Elements and operations

A **symmetry operation** moves the molecule into a configuration physically indistinguishable from the original, preserving all interparticle distances. A **symmetry element** is the point, line or plane with respect to which it acts.

| Element | Symbol | Operation |
|---|---|---|
| $n$-fold proper axis | $C_n$ | $\hat C_n$: rotation by $360°/n$ (counterclockwise); $\hat C_n^k$ by $k\cdot 360°/n$ |
| plane | $\sigma$ ($\sigma_v$ containing the principal axis, $\sigma_h$ perpendicular to it, $\sigma_d$ bisecting two $C_2$ axes) | $\hat\sigma$: reflection |
| centre | $i$ | $\hat\imath$: $(x, y, z) \to (-x, -y, -z)$ |
| $n$-fold improper axis | $S_n$ | $\hat S_n = \hat\sigma_h\hat C_n$: rotation, then reflection in the perpendicular plane |

Identities that reduce the list:

- $\hat C_n^n = \hat E$, the identity.
- $\hat S_1 = \hat\sigma$ and $\hat S_2 = \hat\imath$.
- $\hat C_6^2 = \hat C_3$ and $\hat C_6^3 = \hat C_2$, so a $C_6$ axis is also a $C_3$ and a $C_2$ axis.
- $\hat\sigma^2 = \hat\imath^2 = \hat E$.

**Improper axes need not be proper.** A $C_n$ axis with a perpendicular plane is automatically an $S_n$ axis (the $C_3$ of BF₃ is an $S_3$). But an $S_n$ axis need not be a $C_n$ axis: CH₄ has three $S_4$ axes that are only $C_2$ axes. All elements pass through the centre of mass, the only point every operation leaves fixed. That is why the groups are **point groups**.

**Products.** $\hat R\hat S$ means "do $\hat S$, then $\hat R$", with the axes fixed in space. Products of symmetry operations are symmetry operations, but they need not commute. In SF₆, $\hat C_4(z)\hat C_2(x) \ne \hat C_2(x)\hat C_4(z)$. The latter is a $C_2$ rotation about the axis $(1, -1, 0)/\sqrt2$.

**Matrices.** Each operation is a linear map of $(x, y, z)$, so it has a 3×3 orthogonal matrix, and products of operations multiply as matrices:

$$
\hat C_4(z) \to \begin{pmatrix}0 & -1 & 0\\ 1 & 0 & 0\\ 0 & 0 & 1\end{pmatrix},\qquad
\hat\imath \to -\mathbf 1,\qquad \hat\sigma(\mathbf n) \to \mathbf 1 - 2\mathbf n\mathbf n^{\mathsf T} .
$$

Proper operations have determinant +1 and improper ones −1.

## Operations on functions

For an operation $\hat R$ taking the point $\mathbf r$ to $\mathbf r'$, define the function operator $\hat O_R$ by $(\hat O_Rf)(\mathbf r') = f(\mathbf r)$, i.e. $(\hat O_Rf)(\mathbf r) = f(R^{-1}\mathbf r)$.

- **Examples.** $\hat O_{C_4(z)}\,2p_x = 2p_y$, checked numerically on random points. $\hat O_i$ is the parity operator ([[parity-and-parity-selection-rules]]).
- **Many particles.** For many particles $\hat O_R$ acts on every particle's spatial coordinates and leaves spins alone.
- **Commutation with $\hat H$.** If $\hat R$ is a symmetry operation of the nuclear framework, $\hat O_R$ commutes with the electronic Hamiltonian. Electronic states can then be classified by symmetry, as eigenfunctions of a commuting subset or, in general, by irreducible representation ([[groups-representations-and-characters]]).
- **Conservation.** Continuous symmetries give conservation laws ([[symmetry-conservation-and-degeneracy]]). An atom (spherical symmetry) conserves $\mathbf L$; a linear molecule conserves only $L_z$.

The set of all symmetry operations of a molecule forms a **group** under successive application: it has closure, an identity, inverses ($\hat C_3^{-1} = \hat C_3^2$) and associativity. The number of operations is the **order** of the group.

## The point groups

| Class | Group | Elements (besides $E$) | Order | Example |
|---|---|---|---:|---|
| no $C_n$ | $C_1$ | none | 1 | CHFClBr |
| | $C_s$ | $\sigma$ | 2 | HOCl |
| | $C_i$ | $i$ | 2 | anti-CHFCl–CHFCl (meso) |
| one $C_n$ | $C_n$ | $C_n$ | $n$ | H₂O₂ ($C_2$) |
| | $C_{nh}$ | $C_n$, $\sigma_h$ (so $S_n$; $i$ if $n$ even) | $2n$ | trans-CHCl=CHCl ($C_{2h}$), B(OH)₃ ($C_{3h}$) |
| | $C_{nv}$ | $C_n$, $n\,\sigma_v$ | $2n$ | H₂O ($C_{2v}$), NH₃ ($C_{3v}$) |
| | $S_{2n}$ | $S_{2n}$ only ($n \ge 2$) | $2n$ | |
| $C_n$ + $n\,C_2\perp$ | $D_n$ | | $2n$ | |
| | $D_{nh}$ | + $\sigma_h$ | $4n$ | C₂H₄ ($D_{2h}$), BF₃ ($D_{3h}$), C₆H₆ ($D_{6h}$) |
| | $D_{nd}$ | + $n\,\sigma_d$ | $4n$ | staggered C₂H₆ ($D_{3d}$), allene ($D_{2d}$) |
| several $C_n$, $n > 2$ | $T_d$ | | 24 | CH₄ |
| | $O_h$ | | 48 | SF₆ |
| | $I_h$ | | 120 | C₆₀ |
| linear | $C_{\infty v}$ | $C_\infty$, $\infty\,\sigma_v$ | ∞ | HCN |
| | $D_{\infty h}$ | + $i$, $\sigma_h$, $\infty\,C_2$ | ∞ | CO₂ |

$S_n$ with odd $n$ is the same as $C_{nh}$, and $S_2$ is $C_i$, so the only new $S$ groups are $S_4, S_6, \ldots$.

**Assigning a group:**

1. Linear? Then $D_{\infty h}$ if it has a centre, else $C_{\infty v}$.
2. Two or more $C_n$ with $n > 2$? Then a cubic or icosahedral group ($T_d$, $O_h$, $I_h$, …).
3. Otherwise find the highest-order $C_n$. If there is none: $C_s$ with a plane, $C_i$ with a centre, $C_1$ otherwise.
4. Are there $n$ $C_2$ axes perpendicular to $C_n$?
    - **Yes:** $D_{nh}$ with $\sigma_h$, $D_{nd}$ with $n$ dihedral planes, $D_n$ otherwise.
    - **No:** $C_{nh}$ with $\sigma_h$, $C_{nv}$ with $n$ vertical planes, $S_{2n}$ with an $S_{2n}$ axis, $C_n$ otherwise.

## Two consequences

**Dipole moments.** The dipole vector must be unchanged by every symmetry operation, so it lies along every proper axis and in every plane, and vanishes with a centre of symmetry or with two noncoincident axes. Only $C_1$, $C_s$, $C_n$, $C_{nv}$ and $C_{\infty v}$ molecules can be polar.

**Optical activity.** The mirror image of a molecule has the opposite optical rotation. If the molecule has any $S_n$ axis (including $\sigma = S_1$ and $i = S_2$), then $\hat S_n$ maps it into its mirror image and $\hat C_n$ superimposes the two, so it is optically inactive. Only molecules without improper axes ($C_1$, $C_n$, $D_n$, and the rotational subgroups $T$, $O$, $I$) can be chiral. A molecule with a $C_n$ axis can still be chiral, H₂O₂ for example. Conformations that interconvert by low-barrier internal rotation are not resolvable even if each is chiral.

!!! example "Seventeen molecules, checked by brute force"
    **Method.** For idealized geometries, every candidate operation was tested on the atoms: rotations by $2\pi k/n$ ($n \le 8$), reflections and improper rotations about axes built from atom positions and their sums, cross products and differences, plus $\pm\mathbf 1$. An operation counts if it maps every atom onto an atom of the same element within $10^{-4}$ Å.

    | Molecule | Operations found | Of which improper | PySCF | $\mu$, HF/STO-3G (D) |
    |---|---:|---:|---|---:|
    | CHFClBr | 1 | 0 | $C_1$ | 1.61 |
    | HOCl | 2 | 1 | $C_s$ | 1.94 |
    | anti-CHFCl–CHFCl | 2 | 1 | $C_i$ | 0 |
    | H₂O₂ | 2 | 0 | $C_2$ | 0.50 |
    | trans-CHCl=CHCl | 4 | 2 | $C_{2h}$ | 0 |
    | B(OH)₃ | 6 | 3 | $C_{3h}$ | 0 |
    | H₂O | 4 | 2 | $C_{2v}$ | 1.73 |
    | NH₃ | 6 | 3 | $C_{3v}$ | 1.76 |
    | C₂H₄ | 8 | 4 | $D_{2h}$ | 0 |
    | BF₃ | 12 | 6 | $D_{3h}$ | 0 |
    | C₆H₆ | 24 | 12 | $D_{6h}$ | 0 |
    | staggered C₂H₆ | 12 | 6 | $D_{3d}$ | 0 |
    | allene | 8 | 4 | $D_{2d}$ | 0 |
    | CH₄ | 24 | 12 | $T_d$ | 0 |
    | SF₆ | 48 | 24 | $O_h$ | 0 |
    | HCN | (∞) | | $C_{\infty v}$ | 2.45 |
    | CO₂ | (∞) | | $D_{\infty h}$ | 0 |

    - **Assignments.** Every order matches the table above and every PySCF assignment matches. Exactly half of each group's operations are improper unless it has none.
    - **Dipoles.** The dipole is zero (to $10^{-3}$ D) exactly for the groups the rule forbids.
    - **Chirality.** CHFClBr and H₂O₂ are the only ones without an improper operation: the only candidates for optical activity.

## Source

Levine, *Quantum Chemistry* (7th ed., Pearson, 2014), Sec. 12.1, pp. 328-335 (symmetry elements and operations, Figs. 12.1-12.6; products, non-commutation in SF₆, Fig. 12.7; dipole moments; optical activity; the operators $\hat O_R$, Eqs. (12.1)-(12.6), and their commutation with $\hat H$). Sec. 12.2, pp. 335-341 (matrix representatives; the group axioms; the four classes of point groups with examples, Figs. 12.11-12.13). Summary, p. 341. The assignment procedure above is a standard condensation of that classification. Calculations in `part2_levine_gaps.py`, section D (NumPy operation search; PySCF `symm.geom.detect_symm` and RHF dipoles).
