---
id: wigner-rotation-matrices
title: Wigner rotation matrices
summary: The matrix elements D^j_{m'm}(α,β,γ) = ⟨j m'|D(R)|j m⟩ = e^{−i(m'α + mγ)} d^j_{m'm}(β) of the rotation operator in a multiplet of angular momentum j. Gives d^{1/2} and d^1 explicitly, the general formula, the symmetry relations, unitarity and the group property, the orthogonality integral, the connection D^l_{m0} ∝ Y_l^m* to spherical harmonics, and the behaviour under a 2π rotation, all checked numerically up to j = 3.
status: in-progress
kind: theory
level: intermediate
tags: [wigner-d-matrix, rotation-matrices, euler-angles, irreducible-representation, spherical-harmonics, angular-momentum, sakurai]
prerequisites: [rotations-su2-so3-and-euler-angles, addition-of-angular-momenta, central-potentials-and-spherical-harmonics]
related: [schwinger-oscillator-model, spherical-tensor-operators, rotation-operator-and-rotational-symmetry, time-reversal-and-antiunitary-operators, spin-tensor-operators]
order: 34
date: 2026-11-15
---

## Definition

A rotation does not change $J^2$, since $J^2$ commutes with every component of $\mathbf J$. It therefore maps a state of definite $j$ into a combination of states with the same $j$:

$$
\mathcal D(R)\,|j,m\rangle = \sum_{m'}|j,m'\rangle\,\mathcal D^{(j)}_{m'm}(R) ,\qquad \mathcal D^{(j)}_{m'm}(R) = \langle j,m'|\exp\Big(-\frac{i\mathbf J\cdot\hat{\mathbf n}\,\phi}{\hbar}\Big)|j,m\rangle .
$$

The $(2j+1)\times(2j+1)$ matrices $\mathcal D^{(j)}(R)$ are the **Wigner functions** or rotation matrices. $|\mathcal D^{(j)}_{m'm}|^2$ is the probability that a system prepared in $|j,m\rangle$ and rotated by $R$ is found with $J_z = m'\hbar$. For each $j$ they form an irreducible representation of the rotation group: no basis change can split them into smaller blocks for all $R$ at once.

**Euler angles.** With $R = R_z(\alpha)R_y(\beta)R_z(\gamma)$ ([[rotations-su2-so3-and-euler-angles]]), the outer factors are diagonal in $|j,m\rangle$ and

$$
\boxed{\,\mathcal D^{(j)}_{m'm}(\alpha,\beta,\gamma) = e^{-i(m'\alpha + m\gamma)}\,d^{(j)}_{m'm}(\beta) ,\qquad d^{(j)}_{m'm}(\beta) = \langle j,m'|e^{-iJ_y\beta/\hbar}|j,m\rangle\,}
$$

All the work is in the reduced matrix $d^{(j)}(\beta)$. In the standard (Condon-Shortley) phase convention $J_y$ is purely imaginary, so $d^{(j)}$ is **real**.

## The simplest cases

**$j = \tfrac12$:**

$$
d^{(1/2)}(\beta) = \begin{pmatrix}\cos\frac\beta2&-\sin\frac\beta2\\ \sin\frac\beta2&\cos\frac\beta2\end{pmatrix} ,
$$

rows and columns ordered $m = +\tfrac12,-\tfrac12$.

**$j = 1$.** Here $(J_y/\hbar)^3 = J_y/\hbar$, so the exponential series collapses to $e^{-iJ_y\beta/\hbar} = 1 - (J_y/\hbar)^2(1 - \cos\beta) - i(J_y/\hbar)\sin\beta$ and

$$
d^{(1)}(\beta) = \begin{pmatrix}\frac12(1+\cos\beta)&-\frac{1}{\sqrt2}\sin\beta&\frac12(1-\cos\beta)\\ \frac{1}{\sqrt2}\sin\beta&\cos\beta&-\frac{1}{\sqrt2}\sin\beta\\ \frac12(1-\cos\beta)&\frac{1}{\sqrt2}\sin\beta&\frac12(1+\cos\beta)\end{pmatrix} ,
$$

rows and columns ordered $m = 1,0,-1$. For general $j$, Wigner's formula, derived in [[schwinger-oscillator-model]], is

$$
d^{(j)}_{m'm}(\beta) = \sum_k(-1)^{k-m+m'}\frac{\sqrt{(j+m)!\,(j-m)!\,(j+m')!\,(j-m')!}}{(j+m-k)!\;k!\;(j-k-m')!\;(k-m+m')!}\Big(\cos\frac\beta2\Big)^{2j-2k+m-m'}\Big(\sin\frac\beta2\Big)^{2k-m+m'} ,
$$

the sum running over the integers $k$ for which no factorial has a negative argument. For $j = \tfrac12, 1, \tfrac32, 2, \tfrac52, 3$ at $\beta = 0.83$ it agrees with the numerically exponentiated $\exp(-iJ_y\beta/\hbar)$ to $3\times10^{-16}$.

## Properties

All of the following were checked numerically for $j$ up to 3.

- **Unitarity.** $\mathcal D^{(j)}(R^{-1}) = \mathcal D^{(j)}(R)^\dagger$; for the real $d$ matrices, $d^{(j)}(\beta)^{\rm T}d^{(j)}(\beta) = \mathbb 1$ and $d^{(j)}(-\beta) = d^{(j)}(\beta)^{\rm T}$.
- **Symmetry.**

$$
d^{(j)}_{m'm}(\beta) = (-1)^{m-m'}\,d^{(j)}_{mm'}(\beta) = d^{(j)}_{-m,-m'}(\beta) .
$$

- **Group property.** $\mathcal D^{(j)}(R_1)\mathcal D^{(j)}(R_2) = \mathcal D^{(j)}(R_1R_2)$, the Euler angles of the product being those of the product rotation. For half-integer $j$ this holds up to the overall sign of the double cover.
- **Full turn.** $d^{(j)}(2\pi) = (-1)^{2j}\,\mathbb 1$: integer $j$ returns to itself, half-integer $j$ changes sign.
- **Orthogonality.** Integrated over the group,

$$
\int_0^{2\pi}\!d\alpha\int_0^\pi\!\sin\beta\,d\beta\int_0^{2\pi}\!d\gamma\;\mathcal D^{(j)*}_{m'm}(\alpha,\beta,\gamma)\,\mathcal D^{(j')}_{\mu'\mu}(\alpha,\beta,\gamma) = \frac{8\pi^2}{2j+1}\,\delta_{jj'}\delta_{m'\mu'}\delta_{m\mu} .
$$

  The $\beta$ part, $\int_0^\pi[d^{(j)}_{m'm}]^2\sin\beta\,d\beta = 2/(2j+1)$, was checked for $(j,m',m) = (1,1,0)$, $(\tfrac32,\tfrac12,-\tfrac32)$ and $(2,-1,2)$.
- **Coupling.** The product of two rotation matrices decomposes with Clebsch-Gordan coefficients ([[addition-of-angular-momenta]]), $\mathcal D^{(j_1)}_{m_1'm_1}\mathcal D^{(j_2)}_{m_2'm_2} = \sum_{j,m,m'}\langle j_1j_2;m_1m_2|jm\rangle\langle j_1j_2;m_1'm_2'|jm'\rangle\,\mathcal D^{(j)}_{m'm}$, which is the statement that the direct product of two irreducible representations is a sum of irreducible ones.

## Spherical harmonics as rotation matrices

The state $|\hat{\mathbf n}\rangle$, a direction eigenket pointing along $(\theta,\phi)$, is obtained from $|\hat{\mathbf z}\rangle$ by the rotation $R(\alpha = \phi,\beta = \theta,\gamma = 0)$. Since $\langle l,m|\hat{\mathbf z}\rangle$ is nonzero only for $m = 0$, where it equals $\sqrt{(2l+1)/4\pi}$, projecting $|\hat{\mathbf n}\rangle = \mathcal D(R)|\hat{\mathbf z}\rangle$ onto $\langle l,m|$ gives $Y_l^{m*}(\theta,\phi) = \sqrt{(2l+1)/4\pi}\,\mathcal D^{(l)}_{m0}(\phi,\theta,0)$, or

$$
\boxed{\,\mathcal D^{(l)}_{m0}(\alpha,\beta,0) = \sqrt{\frac{4\pi}{2l+1}}\;Y_l^{m*}(\theta,\phi)\Big|_{\theta=\beta,\ \phi=\alpha}\,}
$$

and in particular $d^{(l)}_{00}(\beta) = P_l(\cos\beta)$. This was checked for $l = 1,2,3$ against SciPy's spherical harmonics, which use the Condon-Shortley phase of [[central-potentials-and-spherical-harmonics]]. Integer $l$ is forced here: only integer-$j$ representations have an $m = 0$ column, which is another way of seeing why orbital angular momentum cannot be half-integer.

Combined with the group property, this relation gives the addition theorem for spherical harmonics, $P_l(\cos\gamma) = \frac{4\pi}{2l+1}\sum_mY_l^{m*}(\theta_1,\phi_1)Y_l^m(\theta_2,\phi_2)$, with $\gamma$ the angle between the two directions.

## Source

Sakurai and Napolitano, *Modern Quantum Mechanics* (3rd ed., Cambridge University Press, 2021), Sec. 3.5.4, pp. 185-188: Wigner functions (3.194), irreducibility and the group property, the meaning of $|\mathcal D_{m'm}|^2$ (3.200), $d^{(1/2)}$ (3.204), the $j = 1$ calculation (3.206)-(3.208) and $d^{(1)}$; Sec. 3.6.3, pp. 194-195, spherical harmonics as rotation matrices (3.258)-(3.261); Sec. 3.9.2, pp. 222-223, Wigner's formula (3.426).

The symmetry relations, the orthogonality integral, the coupling series and the addition theorem are standard results not proved in these sections of Sakurai; each was checked numerically rather than taken on trust. Computed in `sakurai/companions_ch2_ch4.py` (sections C and C2; the coupling series was checked for $1\otimes\tfrac12$, the addition theorem for $l = 1, 2, 4$).
