---
id: spherical-tensor-operators
title: Spherical tensor operators and the Wigner-Eckart theorem
summary: Operators classified by how they transform under rotations. A spherical tensor of rank k has 2k+1 components T_q that rotate like the states |k, q⟩, equivalently obey [J_z, T_q] = ħqT_q and [J_±, T_q] = ħ√((k∓q)(k±q+1)) T_{q±1}. Covers spherical components of a vector, the reduction of a Cartesian tensor into ranks 0, 1 and 2, products of tensors coupled with Clebsch-Gordan coefficients, the Wigner-Eckart theorem in general form with its selection rules, the projection theorem and the Landé g factor, all checked numerically.
status: in-progress
kind: theory
level: advanced
tags: [spherical-tensor, irreducible-tensor-operator, wigner-eckart-theorem, reduced-matrix-element, selection-rules, projection-theorem, lande-g-factor, clebsch-gordan, gaunt-coefficients, sakurai]
prerequisites: [rotational-selection-rules-and-wigner-eckart, addition-of-angular-momenta, wigner-rotation-matrices]
related: [emission-absorption-and-spontaneous-emission, zeeman-effect, time-reversal-and-antiunitary-operators, spin-tensor-operators, central-potentials-and-spherical-harmonics]
order: 55
date: 2026-11-15
---

## From vectors to tensors

A **vector operator** is a set of three operators $V_i$ whose expectation values rotate like a vector, $\langle V_i\rangle\to\sum_jR_{ij}\langle V_j\rangle$. In operator form, $\mathcal D^\dagger(R)V_i\mathcal D(R) = \sum_jR_{ij}V_j$, and for infinitesimal rotations

$$
[V_i,J_j] = i\hbar\,\epsilon_{ijk}V_k ,
$$

the relation used in [[rotational-selection-rules-and-wigner-eckart]]. The **spherical components**

$$
V_{\pm1} = \mp\frac{V_x\pm iV_y}{\sqrt2} ,\qquad V_0 = V_z
$$

transform among themselves exactly as the states $|1,q\rangle$, $q = \pm1,0$. For the position vector, $V_q = r\sqrt{4\pi/3}\,Y_1^q(\theta,\phi)$.

A Cartesian tensor $T_{ij}$ (nine components rotating as $V_iW_j$) is **reducible**: it splits into parts that do not mix under rotations,

$$
V_iW_j = \frac{\mathbf V\cdot\mathbf W}{3}\delta_{ij} + \frac{V_iW_j - V_jW_i}{2} + \Big(\frac{V_iW_j + V_jW_i}{2} - \frac{\mathbf V\cdot\mathbf W}{3}\delta_{ij}\Big) ,
$$

with $1 + 3 + 5$ independent components: a scalar, an antisymmetric part equivalent to the vector $\mathbf V\times\mathbf W$, and a traceless symmetric part. These are the counts $2k+1$ for $k = 0, 1, 2$, the same decomposition as $1\otimes1 = 0\oplus1\oplus2$ for angular momenta.

## Definition

A **spherical tensor of rank $k$** is a set of $2k+1$ operators $T^{(k)}_q$, $q = -k,\dots,k$, that transform under rotations like $|k,q\rangle$:

$$
\mathcal D^\dagger(R)\,T^{(k)}_q\,\mathcal D(R) = \sum_{q'}\mathcal D^{(k)*}_{qq'}(R)\,T^{(k)}_{q'} .
$$

The infinitesimal form is the working definition:

$$
\boxed{\,[J_z,T^{(k)}_q] = \hbar q\,T^{(k)}_q ,\qquad [J_\pm,T^{(k)}_q] = \hbar\sqrt{(k\mp q)(k\pm q+1)}\;T^{(k)}_{q\pm1}\,}
$$

These are the actions of $J_z$ and $J_\pm$ on $|k,q\rangle$, with the commutator in place of the operator acting on a ket. Examples: a scalar is rank 0; a vector in spherical components is rank 1; $r^kY_k^q(\theta,\phi)$ is rank $k$; the quadrupole moment is rank 2.

**Products.** If $X^{(k_1)}$ and $Z^{(k_2)}$ are spherical tensors, then

$$
T^{(k)}_q = \sum_{q_1,q_2}\langle k_1k_2;q_1q_2|k_1k_2;kq\rangle\,X^{(k_1)}_{q_1}Z^{(k_2)}_{q_2}
$$

is a spherical tensor of rank $k$: tensors are coupled exactly like angular momenta. For two vectors and $k = 2$,

$$
T^{(2)}_{\pm2} = V_{\pm1}W_{\pm1} ,\qquad T^{(2)}_{\pm1} = \frac{V_{\pm1}W_0 + V_0W_{\pm1}}{\sqrt2} ,\qquad T^{(2)}_0 = \frac{V_{+1}W_{-1} + 2V_0W_0 + V_{-1}W_{+1}}{\sqrt6} .
$$

!!! example "Checking the definition"

    With $\mathbf V = \mathbf J$ itself, in multiplets $j = 1, \tfrac32, 2$, the spherical components of $\mathbf J$ satisfy the rank-1 commutators, and the rank-2 product built from them by the formula above satisfies the rank-2 commutators for every $q$. (Because the components of $\mathbf J$ do not commute, the order in each product matters; the symmetric forms above are the ones the Clebsch-Gordan coupling produces.)

## The Wigner-Eckart theorem

**Theorem.** For states of definite angular momentum,

$$
\boxed{\,\langle\alpha',j'm'|T^{(k)}_q|\alpha,jm\rangle = \langle jk;mq|jk;j'm'\rangle\,\frac{\langle\alpha'j'\|T^{(k)}\|\alpha j\rangle}{\sqrt{2j+1}}\,}
$$

where the **reduced matrix element** $\langle\alpha'j'\|T^{(k)}\|\alpha j\rangle$ depends on $j$, $j'$, the other quantum numbers $\alpha$, $\alpha'$ and the operator, but not on $m$, $m'$ or $q$. All the dependence on orientation is a Clebsch-Gordan coefficient, fixed by geometry. The normalization $1/\sqrt{2j+1}$ is Sakurai's; other books use different factors, so reduced matrix elements from different sources must not be mixed without checking.

**Proof in outline.** Sandwich the commutator $[J_\pm,T^{(k)}_q]$ between $\langle\alpha'j'm'|$ and $|\alpha jm\rangle$. Moving $J_\pm$ onto the states gives a linear recursion relating matrix elements with neighbouring $m$, $m'$, $q$. It is the same recursion that the Clebsch-Gordan coefficients $\langle jk;mq|jk;j'm'\rangle$ satisfy. A linear homogeneous recursion fixes its solution up to one overall factor, which is the reduced matrix element.

**Selection rules.** The matrix element vanishes unless

$$
m' = m + q ,\qquad |j - k|\le j'\le j + k .
$$

The second is the triangle rule. For $k = 0$ it gives $j' = j$, $m' = m$ (a scalar cannot change angular momentum); for $k = 1$ it gives $\Delta j = 0,\pm1$, $\Delta m = 0,\pm1$, and $0\to0$ is forbidden because the Clebsch-Gordan coefficient for $0\otimes1\to0$ vanishes. These are the dipole selection rules of [[emission-absorption-and-spontaneous-emission]].

!!! example "Spherical harmonics between orbital states"

    For $T^{(k)}_q = Y_k^q$ between hydrogen-like angular states, the matrix elements are integrals of three spherical harmonics (Gaunt coefficients), computed exactly with SymPy. Their ratio to $\langle lk;mq|l'm'\rangle$ takes a single value for every allowed $m$, $q$, as the theorem requires, and that value is

    $$
    \frac{\langle l'm'|Y_k^q|lm\rangle}{\langle lk;mq|l'm'\rangle} = \frac{\langle l'\|Y_k\|l\rangle}{\sqrt{2l+1}} = \sqrt{\frac{(2l+1)(2k+1)}{4\pi(2l'+1)}}\;\langle lk;00|l'0\rangle .
    $$

    | $l\to l'$ | $k$ | ratio (all $m$, $q$) | formula |
    |---|---|---|---|
    | $1\to2$ | 1 | 0.309019 | 0.309019 |
    | $2\to2$ | 2 | $-0.337168$ | $-0.337168$ |
    | $1\to3$ | 2 | 0.319865 | 0.319865 |
    | $2\to1$ | 1 | $-0.398942$ | $-0.398942$ |

    The factor $\langle lk;00|l'0\rangle$ vanishes when $l + k + l'$ is odd, which is the parity selection rule ([[parity-and-parity-selection-rules]]) appearing automatically.

## The projection theorem

For a vector operator $\mathbf V$ within a single multiplet $j$, the Wigner-Eckart theorem applied to $\mathbf V$ and to $\mathbf J$ (also a vector) shows that their matrix elements are proportional. The constant is found from the scalar $\mathbf J\cdot\mathbf V$:

$$
\boxed{\,\langle\alpha,jm'|V_q|\alpha,jm\rangle = \frac{\langle\alpha,jm|\mathbf J\cdot\mathbf V|\alpha,jm\rangle}{\hbar^2j(j+1)}\,\langle jm'|J_q|jm\rangle\,}
$$

Within the multiplet, $\mathbf V$ acts like its projection on $\mathbf J$, as in the classical picture of a vector precessing rapidly about the total angular momentum.

!!! example "Landé g factor"

    For an electron with $l = 1$, $s = \tfrac12$, the magnetic moment is proportional to $\mathbf L + 2\mathbf S = \mathbf J + \mathbf S$. With $\mathbf J\cdot\mathbf S = \tfrac12[\mathbf J^2 + \mathbf S^2 - \mathbf L^2]$ the projection theorem gives $\langle L_z + 2S_z\rangle = g_Jm\hbar$ with

    $$
    g_J = 1 + \frac{j(j+1) + s(s+1) - l(l+1)}{2j(j+1)} ,
    $$

    so $g = \tfrac23$ for $j = \tfrac12$ and $\tfrac43$ for $j = \tfrac32$. Diagonalizing $\mathbf J^2$ in the six-dimensional product space and evaluating $\langle S_z\rangle$ and $\langle L_z + 2S_z\rangle$ directly reproduces these for all six states, for example $\langle S_z\rangle = +\hbar/6$ in $|j = \tfrac12, m = -\tfrac12\rangle$. This is the weak-field Zeeman result of [[zeeman-effect]].

## Source

Sakurai and Napolitano, *Modern Quantum Mechanics* (3rd ed., Cambridge University Press, 2021), Sec. 3.11, pp. 231-240: vector operators (3.11.1); Cartesian versus spherical tensors, the $1 + 3 + 5$ reduction and the definition (3.454)-(3.468) (3.11.2); products of tensors, Theorem (3.470) (3.11.3); the Wigner-Eckart theorem (3.474), the $m$ selection rule (3.471), the triangle rule (3.475), scalar and vector examples (3.481)-(3.482), and the projection theorem (3.483)-(3.488) (3.11.4).

The Gaunt-coefficient check, the explicit rank-2 product and the Landé example are my own, computed in `sakurai/companions_ch2_ch4.py` (section F).
