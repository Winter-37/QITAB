---
id: scalars-and-vectors
title: Scalars and vectors - definition by behaviour under rotation, components, the scalar and vector products, triple products, the Levi-Civita symbol, and pseudovectors
summary: A scalar is a quantity unchanged by a rotation of the coordinate axes; a vector is a triple of components that transforms like the coordinates themselves, V'_i = Σ_j a_ij V_j. The scalar (dot) product A·B = AB cos θ is invariant. The vector (cross) product A × B has magnitude AB sin θ and points along the normal. Both are written compactly with the Kronecker delta and the Levi-Civita symbol, and the identity εε = δδ − δδ generates the triple-product rules (BAC–CAB, Lagrange's identity). Under inversion a cross product does not change sign, so angular momentum, torque and B are pseudovectors. Worked examples: the tetrahedral angle, numerical checks of the identities, and the inversion test.
status: in-progress
kind: theory
level: introductory
tags: [scalar, vector, dot-product, cross-product, triple-product, levi-civita, kronecker-delta, rotation-matrix, pseudovector, direction-cosines]
prerequisites: [matrices-and-determinants]
related: [scalar-and-vector-fields-and-the-gradient, change-of-basis, rotational-averages-and-isotropic-tensors, rotations-su2-so3-and-euler-angles]
key: epsdelta
order: 10
date: 2026-11-25
---

Cartesian components in a right-handed frame with unit vectors $\hat{\mathbf x}, \hat{\mathbf y}, \hat{\mathbf z}$ (or $\hat{\mathbf e}_i$). Repeated indices are summed. $\delta_{ij}$ is the Kronecker delta and $\epsilon_{ijk}$ the Levi-Civita symbol: $+1$ for even permutations of $(1,2,3)$, $-1$ for odd ones, 0 if an index repeats.

## Scalars and vectors

**Elementary picture.** A scalar has magnitude only: mass, temperature, energy, charge. A vector has magnitude and direction and adds by the parallelogram rule: displacement, velocity, force, the electric field. Writing $\mathbf A = A_x\hat{\mathbf x} + A_y\hat{\mathbf y} + A_z\hat{\mathbf z}$, addition and multiplication by a number act on the components, and the length is $A = |\mathbf A| = (A_x^2 + A_y^2 + A_z^2)^{1/2}$ (Arfken Sec. 1.1).

**Definition by rotation.** Rotate the axes. Coordinates transform as $x'_i = a_{ij}x_j$, where $a_{ij} = \hat{\mathbf e}'_i\cdot\hat{\mathbf e}_j$ are the direction cosines. The matrix $\mathbf a$ is orthogonal, $\mathbf a\mathbf a^{\rm T} = \mathbf 1$, with determinant $+1$ for a proper rotation. Arfken Sec. 1.2 then defines:

- a **scalar** as a quantity with the same value in both frames, $\varphi' = \varphi$;
- a **vector** as a set of three components that transforms like the coordinates,

$$
V'_i = a_{ij}V_j .
\label{vec}
$$

Not every triple of numbers is a vector. $(T, P, V)$ of a gas is not, because the three entries do not mix under rotation. This definition is what extends to tensors ([[rotational-averages-and-isotropic-tensors]]).

## The scalar product

**Definition.** $\mathbf A\cdot\mathbf B = A_iB_i = AB\cos\theta$, with $\theta$ the angle between the vectors (Arfken Sec. 1.3).

**Invariance.** $A'_iB'_i = a_{ij}a_{ik}A_jB_k = \delta_{jk}A_jB_k = A_jB_j$, using orthogonality. So the scalar product is a scalar.

**Uses.**

- **Projection.** $\mathbf A\cdot\hat{\mathbf n}$ is the component of $\mathbf A$ along the unit vector $\hat{\mathbf n}$; $A_i = \mathbf A\cdot\hat{\mathbf e}_i$.
- **Orthogonality.** $\mathbf A\cdot\mathbf B = 0$ for perpendicular vectors; $\hat{\mathbf e}_i\cdot\hat{\mathbf e}_j = \delta_{ij}$.
- **Law of cosines.** $|\mathbf A - \mathbf B|^2 = A^2 + B^2 - 2AB\cos\theta$.
- **Work.** $W = \int\mathbf F\cdot d\mathbf r$.
- **Angles between bonds.** $\cos\theta = \mathbf r_1\cdot\mathbf r_2/(r_1r_2)$.

## The vector product

**Definition.** $\mathbf C = \mathbf A\times\mathbf B$ has magnitude $AB\sin\theta$, the area of the parallelogram spanned by $\mathbf A$ and $\mathbf B$. Its direction is perpendicular to both, by the right-hand rule (Arfken Sec. 1.4). In components,

$$
(\mathbf A\times\mathbf B)_i = \epsilon_{ijk}A_jB_k,\qquad
\mathbf A\times\mathbf B = \begin{vmatrix}\hat{\mathbf x}&\hat{\mathbf y}&\hat{\mathbf z}\\A_x&A_y&A_z\\B_x&B_y&B_z\end{vmatrix}.
$$

**Properties.** It is antisymmetric ($\mathbf A\times\mathbf B = -\mathbf B\times\mathbf A$, so $\mathbf A\times\mathbf A = 0$), distributive, and not associative. The unit vectors satisfy $\hat{\mathbf x}\times\hat{\mathbf y} = \hat{\mathbf z}$ cyclically.

**Physical examples.** Angular momentum $\mathbf L = \mathbf r\times\mathbf p$, torque $\mathbf r\times\mathbf F$, the velocity of a rigid rotation $\mathbf v = \boldsymbol\omega\times\mathbf r$, and the magnetic force $q\mathbf v\times\mathbf B$.

## The Levi-Civita identity and triple products

**The key identity.** Every product of two Levi-Civita symbols reduces to Kronecker deltas. Contracted on one index:

$$
\epsilon_{ijk}\epsilon_{imn} = \delta_{jm}\delta_{kn} - \delta_{jn}\delta_{km}.
\label{epsdelta}
$$

Further contractions give $\epsilon_{ijk}\epsilon_{ijn} = 2\delta_{kn}$ and $\epsilon_{ijk}\epsilon_{ijk} = 6$. Eq. [[#epsdelta]] proves the triple-product rules in one line each.

**Triple scalar product** (Arfken Sec. 1.5):

$$
\mathbf A\cdot(\mathbf B\times\mathbf C) = \epsilon_{ijk}A_iB_jC_k = \det\begin{pmatrix}A_x&A_y&A_z\\B_x&B_y&B_z\\C_x&C_y&C_z\end{pmatrix}.
$$

It is the signed volume of the parallelepiped spanned by the three vectors. It is unchanged under cyclic permutation and changes sign under exchange, and it vanishes exactly when the three vectors are coplanar.

**Triple vector product ("BAC–CAB"):**

$$
\mathbf A\times(\mathbf B\times\mathbf C) = \mathbf B(\mathbf A\cdot\mathbf C) - \mathbf C(\mathbf A\cdot\mathbf B).
$$

**Lagrange's identity:** $(\mathbf A\times\mathbf B)\cdot(\mathbf C\times\mathbf D) = (\mathbf A\cdot\mathbf C)(\mathbf B\cdot\mathbf D) - (\mathbf A\cdot\mathbf D)(\mathbf B\cdot\mathbf C)$. With $\mathbf C = \mathbf A$, $\mathbf D = \mathbf B$ it gives $|\mathbf A\times\mathbf B|^2 = A^2B^2 - (\mathbf A\cdot\mathbf B)^2$, i.e. $\sin^2 + \cos^2 = 1$.

## Pseudovectors and pseudoscalars

**Inversion.** Under $\mathbf r\to-\mathbf r$ (the matrix $-\mathbf 1$, determinant $-1$) a true (polar) vector changes sign. A cross product of two polar vectors does not: $(-\mathbf A)\times(-\mathbf B) = \mathbf A\times\mathbf B$. Such a quantity is an **axial vector** or **pseudovector**: it obeys Eq. [[#vec]] with an extra factor $\det\mathbf a$. Angular momentum, torque, $\boldsymbol\omega$ and the magnetic field are pseudovectors.

**Pseudoscalars.** A triple product of three polar vectors changes sign under inversion. This parity bookkeeping decides which molecular properties survive in isotropic or achiral media: optical rotation is a pseudoscalar property ([[rotational-averages-and-isotropic-tensors]]).

## Worked example

!!! example "Angles, identities and parity (computed for this note)"
    **Tetrahedral angle.** Bonds from the centre of a cube to opposite corners, $(1, 1, 1)$ and $(1, -1, -1)$: $\cos\theta = (1 - 1 - 1)/3 = -\tfrac13$, so $\theta = 109.4712°$, the angle in CH₄.

    **The identities, numerically.** For four random vectors, the BAC–CAB residual is $6\times10^{-17}$ and the Lagrange residual $9\times10^{-18}$. The triple product $\mathbf A\cdot(\mathbf B\times\mathbf C) = 0.17284634$ equals $\det[\mathbf A;\mathbf B;\mathbf C]$. Eq. [[#epsdelta]] holds for all 81 index combinations.

    **Rotation and inversion.** Under a random rotation $\mathbf R$, $(\mathbf R\mathbf A)\cdot(\mathbf R\mathbf B) = \mathbf A\cdot\mathbf B$ and $(\mathbf R\mathbf A)\times(\mathbf R\mathbf B) = \mathbf R(\mathbf A\times\mathbf B)$. Under inversion, $(-\mathbf A)\times(-\mathbf B) = +\mathbf A\times\mathbf B$: the pseudovector does not flip.

## Source

Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005), Secs. 1.1–1.5 (vectors, rotation of the axes, scalar and vector products, triple products), Sec. 2.9 (pseudovectors). Calculations in `Claude outputs/part0_math_batchE.py`, section B.
