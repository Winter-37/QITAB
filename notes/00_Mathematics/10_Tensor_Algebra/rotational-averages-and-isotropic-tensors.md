---
id: rotational-averages-and-isotropic-tensors
title: Rotational averages of Cartesian tensors - transformation by direction cosines, isotropic tensors, and the averages of rank 1 to 4
summary: A Cartesian tensor of rank n transforms with one direction-cosine matrix per index. For freely rotating molecules, what an experiment sees is the average over all orientations, ⟨l_{i'i}⋯l_{n'n}⟩T. That average is itself an isotropic tensor, so it can be expanded in the basic isotropic tensors of that rank: 1 for rank 0, none for rank 1, δ for rank 2, ε for rank 3, and the three δδ products for rank 4. The coefficients follow by contraction. The number of independent isotropic tensors of rank n is the Motzkin sum sequence 1, 0, 1, 1, 3, 6, 15, 36, 91, …. These averages turn molecular polarizabilities and transition moments into the isotropic invariants of refractive indices, Raman and ROA intensities and multiphoton cross sections. Checked: the rank-4 coefficient matrix, Monte Carlo averages, the Motzkin numbers from a character integral, and the isotropic α and G′ of CHFClBr (NRS Table 3.1).
status: in-progress
kind: theory
level: intermediate
tags: [rotational-average, isotropic-tensor, cartesian-tensor, direction-cosines, levi-civita, kronecker-delta, orientational-average, motzkin-numbers, invariants]
prerequisites: [change-of-basis]
related: [tensor-products-and-partial-trace, multiphoton-absorption, raman-scattering, vibrational-optical-activity, local-field-clausius-mossotti-and-reaction-field, optical-activity-ecd-and-mcd, rotations-su2-so3-and-euler-angles]
key: rank4
order: 30
date: 2026-11-25
---

Einstein summation over repeated indices. Unprimed indices refer to the molecular frame, primed ones to the laboratory frame. $l_{i'i} = \mathbf e_{i'}^{\rm T}\cdot\mathbf e_i = \cos\theta_{i'i}$ are the direction cosines, the elements of the rotation matrix between the frames. $\langle\cdots\rangle_{\rm iso}$ is the average over all orientations, uniform on SO(3).

## Cartesian tensors

**Transformation.** Components of a vector in two frames are related by projection, $T_{i'} = \mathbf e^{\rm T}_{i'}\cdot T_j\mathbf e_j = l_{i'j}T_j$ (NRS Eqs. 3.463–3.467). A polarizability links two vectors, $\mu_{i'} = \alpha_{i'j'}E_{j'}$. Transforming both gives $\alpha_{i'j'} = l_{i'i}l_{j'j}\alpha_{ij}$ (NRS Eqs. 3.468–3.469). In general

$$
T_{i'_1\cdots i'_n} = l_{i'_1i_1}\cdots l_{i'_ni_n}T_{i_1\cdots i_n},\qquad
\langle T_{i'_1\cdots i'_n}\rangle_{\rm iso} = \langle l_{i'_1i_1}\cdots l_{i'_ni_n}\rangle\,T_{i_1\cdots i_n}
\label{avg}
$$

(NRS Eqs. 3.470–3.471).

## Isotropic tensors

**The method.** The average in Eq. [[#avg]] is unchanged by any further rotation, so it is an isotropic tensor. It can be expanded in a basis of **basic isotropic tensors** of the same rank, and the coefficients found by contracting both sides with each basis tensor. The decisive step: a full contraction is a scalar, hence rotation invariant, so the average of the contraction is the contraction itself (NRS Eq. 3.474).

**Rank 0.** A scalar is its own average.

**Rank 1.** There is no isotropic vector, so $\langle T_{i'}\rangle_{\rm iso} = \langle\cos\theta_{i'i}\rangle T_i = 0$. A freely rotating molecule has no average dipole (NRS Eq. 3.472).

**Rank 2.** The basis is $\delta_{ij}$. Contracting with $\delta$ gives $3a = T_{ii}$ (NRS Eqs. 3.473–3.474):

$$
\langle T\rangle_{ij} = \tfrac13T_{kk}\,\delta_{ij} .
$$

**Rank 3.** The basis is $\epsilon_{ijk}$, and $\epsilon_{ijk}\epsilon_{ijk} = 6$ (NRS Eqs. 3.475–3.476):

$$
\langle T\rangle_{ijk} = \tfrac16\epsilon_{lmn}T_{lmn}\,\epsilon_{ijk} .
$$

The average picks out the totally antisymmetric part. That is why an isotropic sample has no $\beta$-type response for any second-order process with symmetric tensors, such as SHG. Only chiral contributions to sum-frequency generation survive.

**Rank 4.** There are three basis tensors. Contracting with each gives the Gram matrix with entries 9 on the diagonal and 3 elsewhere, whose inverse yields (NRS Eqs. 3.477–3.479)

$$
\langle T\rangle_{ijkl} = a\,\delta_{ij}\delta_{kl} + b\,\delta_{ik}\delta_{jl} + c\,\delta_{il}\delta_{jk},\qquad
\begin{pmatrix}a\\b\\c\end{pmatrix} = \frac1{30}\begin{pmatrix}4&-1&-1\\-1&4&-1\\-1&-1&4\end{pmatrix}\begin{pmatrix}T_{iijj}\\T_{ijij}\\T_{ijji}\end{pmatrix}.
\label{rank4}
$$

**Where rank 4 appears.** It gives the isotropic averages of products of two second-rank tensors: Raman invariants $a^2$, $\beta^2$ ([[raman-scattering]]), the two-photon invariant of [[multiphoton-absorption]], and the ROA invariants with $G'$ and $A$ ([[vibrational-optical-activity]]). For example, $\langle|\mathbf e\cdot\mathbf M\cdot\mathbf e|^2\rangle$ for a lab polarization $\mathbf e$ is a rank-4 average of $M_{ij}M^*_{kl}$.

**Higher ranks.** The basic isotropic tensors are products of Kronecker deltas and Levi-Civita symbols, and their number follows the Motzkin sum sequence (NRS Eq. 3.480):

$$
a_n = \frac{n-1}{n+1}(2a_{n-1} + 3a_{n-2}):\qquad 1, 0, 1, 1, 3, 6, 15, 36, 91, 232,\dots
$$

For $n\ge4$ the products are not linearly independent in three dimensions: rank 6 has 15 independent tensors among more products. Independent ones must be selected, as in the tables used for multiphoton averages.

## Physical meaning

**A sample calculation.** Take R-CHFClBr. Its permanent dipole (4.46 D, nearly along C–F) averages to zero in a gas or solution. Its polarizability tensor has nonzero off-diagonal components, so in an oriented sample the induced dipole would not be parallel to the field. Averaging keeps only $\bar\alpha = \tfrac13\alpha_{kk}$, and the polarization becomes parallel to $\mathbf E$ (NRS Eq. 3.481, Table 3.1).

**Chirality.** The mixed polarizability $G'$ averages to $\tfrac13G'_{kk}$ as well. That trace is a pseudoscalar: it changes sign with the enantiomer and gives a dipole along the time derivative of $\mathbf B$ rather than $\mathbf E$. This is the molecular origin of optical rotation in isotropic media (NRS Eq. 3.482; [[optical-activity-ecd-and-mcd]]).

## Worked example

!!! example "Checks of the averaging formulas (computed for this note)"
    **Rank-4 coefficients.** $30\times$ the inverse of $\begin{pmatrix}9&3&3\\3&9&3\\3&3&9\end{pmatrix}$ is $\begin{pmatrix}4&-1&-1\\-1&4&-1\\-1&-1&4\end{pmatrix}$, as in Eq. [[#rank4]].

    **Monte Carlo.** For a random (nonsymmetric) rank-4 tensor, averaging $l_{i'i}l_{j'j}l_{k'k}l_{l'l}T_{ijkl}$ over $2\times10^4$ uniform random rotations reproduces Eq. [[#rank4]] within the sampling error. The largest deviation over all 81 components is 0.011, against an estimated error of 0.06.

    **Rank 3.** For a random rank-3 tensor, $2\times10^5$ rotations give $\langle T_{xyz}\rangle = -0.2759$, equal to $\tfrac16\epsilon_{lmn}T_{lmn} = -0.2759$.

    **Counting.** The number of linearly independent isotropic tensors of rank $n$ is the multiplicity of the trivial representation in $(\mathbb R^3)^{\otimes n}$. It equals $\frac1\pi\int_0^\pi(1 + 2\cos w)^n(1 - \cos w)\,dw$, with $1 + 2\cos w$ the character of a rotation by $w$. For $n = 0,\dots,9$ the integral gives 1, 0, 1, 1, 3, 6, 15, 36, 91, 232, identical to the recurrence above.

    **CHFClBr** (B3LYP/aug-cc-pVDZ tensors at 589 nm, NRS Table 3.1): $\bar\alpha = \tfrac13(78.2270 + 50.1867 + 45.9111) = 58.1083$ au and $\bar G' = \tfrac13(-0.1015 + 0.1137 - 0.0075) = 0.00157$ au. These match the 58.1083 and 0.0016 quoted by NRS. The isotropic $G'$ is three orders of magnitude smaller than its largest components.

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Sec. 3.5.5, Eqs. (3.463)–(3.482), Table 3.1, Fig. 3.29 (described). The character-integral count and the SHG remark are general knowledge, not from NRS. The checks are in `Claude outputs/part1_fields_batchD.py`, sections E and H.
