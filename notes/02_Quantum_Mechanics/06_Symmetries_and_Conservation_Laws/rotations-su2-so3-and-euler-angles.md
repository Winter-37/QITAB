---
id: rotations-su2-so3-and-euler-angles
title: Finite rotations, SU(2), SO(3) and Euler angles
summary: Rotations as a non-commuting group. Shows that two small rotations about x and y fail to commute by a rotation about z, which is why the generators obey the angular momentum algebra. For spin 1/2 the rotation operator is exp(−iσ·nφ/2) = cos(φ/2) − i σ·n sin(φ/2), a unitary unimodular 2×2 matrix; these matrices form SU(2), which covers the rotation group SO(3) twice. Covers the 2π sign change and its detection by neutron interferometry, the Cayley-Klein parameters, and the Euler-angle parametrization in its body-fixed and space-fixed forms.
status: in-progress
kind: derivation
level: intermediate
tags: [rotation-group, so3, su2, spin-one-half, euler-angles, cayley-klein, double-cover, neutron-interferometry, non-abelian, sakurai]
prerequisites: [rotation-operator-and-rotational-symmetry, spin-one-half]
related: [wigner-rotation-matrices, schwinger-oscillator-model, berry-phase, unitary-matrices-exponential-logarithm, two-level-systems-and-rabi-oscillations]
order: 32
date: 2026-11-15
---

## Rotations do not commute

A rotation of a vector in three dimensions is a real $3\times3$ orthogonal matrix of determinant one, $R^{\rm T}R = \mathbb 1$; these form the group SO(3). About the $z$ axis,

$$
R_z(\phi) = \begin{pmatrix}\cos\phi&-\sin\phi&0\\ \sin\phi&\cos\phi&0\\ 0&0&1\end{pmatrix} ,
$$

and similarly for $x$ and $y$. Rotations about different axes do not commute. Expanding each to second order in a small angle $\varepsilon$, $R_x(\varepsilon) = \mathbb 1 + \varepsilon K_x + \tfrac12\varepsilon^2K_x^2 + \cdots$, gives

$$
R_x(\varepsilon)R_y(\varepsilon) - R_y(\varepsilon)R_x(\varepsilon) = R_z(\varepsilon^2) - \mathbb 1 + O(\varepsilon^3) .
$$

(Numerically the remainder is $5.0\times10^{-4}$ at $\varepsilon = 0.1$ and $5.0\times10^{-7}$ at $\varepsilon = 0.01$.) The group is **non-Abelian**.

In quantum mechanics a rotation $R$ is represented by a unitary operator $\mathcal D(R)$ on kets, $|\alpha\rangle_R = \mathcal D(R)|\alpha\rangle$. For an infinitesimal rotation $\mathcal D = 1 - i(\mathbf J\cdot\hat{\mathbf n})\,d\phi/\hbar$, which defines the angular momentum $\mathbf J$ as the generator of rotations, and a finite rotation is $\mathcal D_{\hat{\mathbf n}}(\phi) = \exp(-i\mathbf J\cdot\hat{\mathbf n}\,\phi/\hbar)$ ([[rotation-operator-and-rotational-symmetry]]). Requiring that $\mathcal D$ obey the same multiplication law as $R$, the relation above becomes

$$
[J_x,J_y] = i\hbar J_z\quad\text{and cyclic} .
$$

The commutation relations of angular momentum are therefore not an extra postulate: they express the non-commutativity of rotations. Everything in the theory of angular momentum follows from them.

## Spin one-half

With $\mathbf S = \tfrac\hbar2\boldsymbol\sigma$ and the Pauli identity $(\boldsymbol\sigma\cdot\mathbf a)(\boldsymbol\sigma\cdot\mathbf b) = \mathbf a\cdot\mathbf b + i\boldsymbol\sigma\cdot(\mathbf a\times\mathbf b)$, the series for the exponential sums to

$$
\boxed{\,\mathcal D^{(1/2)}(\hat{\mathbf n},\phi) = \exp\Big(-\frac{i\boldsymbol\sigma\cdot\hat{\mathbf n}\,\phi}{2}\Big) = \mathbb 1\cos\frac\phi2 - i\,\boldsymbol\sigma\cdot\hat{\mathbf n}\,\sin\frac\phi2\,}
$$

Under this operator the expectation value of $\mathbf S$ rotates as a classical vector, $\langle S_k\rangle\to\sum_lR_{kl}\langle S_l\rangle$. Equivalently, $\mathcal D^\dagger\sigma_k\mathcal D = \sum_lR_{kl}\sigma_l$, so the rotation matrix can be read off from the $2\times2$ one:

$$
R_{kl} = \tfrac12\,\mathrm{tr}\big(\sigma_k\,\mathcal D\,\sigma_l\,\mathcal D^\dagger\big) .
$$

**The $2\pi$ sign.** At $\phi = 2\pi$ the formula gives $\mathcal D = -\mathbb 1$: a full turn multiplies every spinor by $-1$, and $4\pi$ is needed to return to the identity. Expectation values, being quadratic in the state, are unaffected. The sign becomes visible when one part of a coherent beam is rotated and the other is not. In a spin precessing at angular velocity $\omega$ the state vector has period $4\pi/\omega$, twice the precession period.

This was observed with neutrons. A beam is split in a single-crystal interferometer, one path passes through a magnetic field region of length $l$ where the spin precesses, and the beams are recombined. The intensity oscillates with the field, and the field change between successive maxima corresponds to a precession angle of $4\pi$, not $2\pi$. Sakurai gives the period as $\Delta B = 4\pi\hbar c/(eg_n\lambda l)$ in Gaussian units ($g_n$ the neutron $g$ factor, $\lambda$ the neutron wavelength).

## SU(2) and its relation to SO(3)

Writing $\mathcal D^{(1/2)}$ out, with $\hat{\mathbf n} = (n_x,n_y,n_z)$,

$$
\mathcal D^{(1/2)} = \begin{pmatrix}\cos\frac\phi2 - in_z\sin\frac\phi2 & (-in_x - n_y)\sin\frac\phi2\\ (-in_x + n_y)\sin\frac\phi2 & \cos\frac\phi2 + in_z\sin\frac\phi2\end{pmatrix}
$$

is unitary with determinant one. Conversely, every such matrix has the form

$$
U(a,b) = \begin{pmatrix}a&b\\ -b^*&a^*\end{pmatrix} ,\qquad |a|^2 + |b|^2 = 1 ,
$$

with complex **Cayley-Klein parameters** $a$, $b$, and corresponds to a rotation. These matrices form the group SU(2) (special unitary, $2\times2$). Three real numbers fix an element, as for SO(3).

The map $U\mapsto R(U)$, with $R_{kl}$ as above, preserves multiplication, $R(U_1U_2) = R(U_1)R(U_2)$, and it is two-to-one: $U$ and $-U$ give the same rotation. Thus SU(2) is a **double cover** of SO(3). The two groups have the same Lie algebra and are identical near the identity (locally isomorphic), but SU(2) distinguishes a rotation by $\phi$ from one by $\phi + 2\pi$ while SO(3) does not. Integer $j$ gives genuine representations of SO(3). Half-integer $j$ gives representations of SU(2) only, which are double valued as representations of the rotations. All three properties of the map (equality with the rotation matrix, the product rule and $R(-U) = R(U)$) were checked numerically for random axes and angles.

Topologically, SU(2) is the unit sphere $S^3$ in four dimensions ($|a|^2 + |b|^2 = 1$) and SO(3) is that sphere with opposite points identified.

## Euler angles

Any rotation can be built from three rotations about coordinate axes. In the convention used by Sakurai (and by most of quantum mechanics):

1. Rotate the body by $\alpha$ about the space $z$ axis. Its $y$ axis moves to $y'$.
2. Rotate by $\beta$ about $y'$. Its $z$ axis moves to $z'$.
3. Rotate by $\gamma$ about $z'$.

The intermediate axes are inconvenient. They can be removed with the identities $R_{y'}(\beta) = R_z(\alpha)R_y(\beta)R_z^{-1}(\alpha)$ and $R_{z'}(\gamma) = R_{y'}(\beta)R_z(\gamma)R_{y'}^{-1}(\beta)$, which turn the sequence into rotations about the fixed space axes, applied in the opposite order:

$$
R(\alpha,\beta,\gamma) = R_{z'}(\gamma)R_{y'}(\beta)R_z(\alpha) = R_z(\alpha)\,R_y(\beta)\,R_z(\gamma) .
$$

The equality was confirmed numerically. The ranges $0\le\alpha,\gamma<2\pi$, $0\le\beta\le\pi$ cover all rotations. The same factorization holds for the operators, $\mathcal D(\alpha,\beta,\gamma) = \mathcal D_z(\alpha)\mathcal D_y(\beta)\mathcal D_z(\gamma)$, and for spin $\tfrac12$:

$$
\mathcal D^{(1/2)}(\alpha,\beta,\gamma) = \begin{pmatrix}e^{-i(\alpha+\gamma)/2}\cos\frac\beta2 & -e^{-i(\alpha-\gamma)/2}\sin\frac\beta2\\ e^{i(\alpha-\gamma)/2}\sin\frac\beta2 & e^{i(\alpha+\gamma)/2}\cos\frac\beta2\end{pmatrix} .
$$

This is a matrix of the Cayley-Klein form, and every element of SU(2) can be written this way. The middle rotation is chosen about $y$ so that its matrix, $\exp(-i\sigma_y\beta/2)$, is real; this choice makes the $d$ matrices of [[wigner-rotation-matrices]] real for every $j$.

## Source

Sakurai and Napolitano, *Modern Quantum Mechanics* (3rd ed., Cambridge University Press, 2021), Sec. 3.1, pp. 151-155 (finite versus infinitesimal rotations, the commutator of small rotations, Eqs. (3.1)-(3.21)); Sec. 3.2, pp. 155-162 (spin-$\tfrac12$ rotation operator, the $2\pi$ sign (3.33), spin precession (3.38)-(3.39), neutron interferometry (3.40)-(3.43), the two-component closed form (3.62)); Sec. 3.3, pp. 163-168 (SO(3), SU(2) and the Cayley-Klein form (3.77), the double covering, Euler rotations (3.85)-(3.91)). The neutron experiments, as cited by Sakurai: H. Rauch et al., Phys. Lett. A 54, 425 (1975); S. A. Werner et al., Phys. Rev. Lett. 35, 1053 (1975).

The trace formula for $R_{kl}$ and the remark on the topology of the two groups are my additions. Checks are in `sakurai/companions_ch2_ch4.py` (section B).
