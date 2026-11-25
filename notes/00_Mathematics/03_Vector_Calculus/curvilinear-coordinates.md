---
id: curvilinear-coordinates
title: Orthogonal curvilinear coordinates - scale factors, line, area and volume elements, and the gradient, divergence, curl and Laplacian in cylindrical and spherical coordinates
summary: In orthogonal coordinates (q₁, q₂, q₃) the line element is ds² = Σ hᵢ² dqᵢ², and the scale factors hᵢ fix everything else. The volume element is h₁h₂h₃ dq₁dq₂dq₃; the gradient has components (1/hᵢ)∂ψ/∂qᵢ; the divergence, curl and Laplacian follow from the flux and circulation definitions applied to a curvilinear box. For cylindrical coordinates (h = 1, ρ, 1) and spherical coordinates (h = 1, r, r sin θ) the general formulas give the standard operators, including the spherical Laplacian whose angular part is −L̂²/(ħ²r²). The unit vectors depend on position, which is why the vector Laplacian is not the Laplacian of the components. Worked examples: scale factors from the metric, the spherical Laplacian checked against Cartesian, and ⟨T⟩ = 1/2 hartree for hydrogen 1s.
status: in-progress
kind: theory
level: intermediate
tags: [curvilinear-coordinates, scale-factors, metric, spherical-coordinates, cylindrical-coordinates, laplacian, volume-element, unit-vectors, angular-momentum]
prerequisites: [vector-identities-and-the-laplacian]
related: [integral-calculus, partial-differential-equations-and-separation-of-variables, classical-orthogonal-polynomials, hydrogen-atom]
key: lapsph
order: 60
date: 2026-11-25
---

Spherical coordinates in the physics convention: $\theta\in[0,\pi]$ is the polar angle from $z$, $\phi\in[0, 2\pi)$ the azimuth. Cylindrical coordinates $(\rho,\phi,z)$. Indices are not summed in this note unless a $\sum$ is written.

## Orthogonal coordinates

**Scale factors.** Let $\mathbf r = \mathbf r(q_1, q_2, q_3)$. The coordinate system is **orthogonal** when the curves along which only one $q_i$ varies meet at right angles everywhere. Then

$$
ds^2 = |d\mathbf r|^2 = h_1^2dq_1^2 + h_2^2dq_2^2 + h_3^2dq_3^2,\qquad h_i = \Big|\frac{\partial\mathbf r}{\partial q_i}\Big|
\label{metric}
$$

(Arfken Sec. 2.1). The unit vectors are $\hat{\mathbf q}_i = h_i^{-1}\,\partial\mathbf r/\partial q_i$. They form a right-handed orthonormal set at each point, but their directions change from point to point.

**Elements.** A step $dq_i$ moves a distance $h_i\,dq_i$. So:

- the line element is $d\mathbf r = \sum_ih_i\,dq_i\,\hat{\mathbf q}_i$;
- the area element on a surface $q_1 = $ const is $h_2h_3\,dq_2\,dq_3$;
- the volume element is $d\tau = h_1h_2h_3\,dq_1\,dq_2\,dq_3$, the Jacobian determinant of [[integral-calculus]].

## The differential operators

Each follows from a definition that does not mention axes: Eq. [[scalar-and-vector-fields-and-the-gradient#grad]] for the gradient, the flux limit for the divergence, the circulation limit for the curl. Applied to a box with edges $h_i\,dq_i$ they give (Arfken Eqs. 2.18, 2.21, 2.22, 2.27):

$$
\nabla\psi = \sum_i\frac{\hat{\mathbf q}_i}{h_i}\frac{\partial\psi}{\partial q_i},\qquad
\nabla\cdot\mathbf V = \frac1{h_1h_2h_3}\Big[\frac{\partial}{\partial q_1}(V_1h_2h_3) + \frac{\partial}{\partial q_2}(V_2h_3h_1) + \frac{\partial}{\partial q_3}(V_3h_1h_2)\Big],
$$

$$
\nabla^2\psi = \frac1{h_1h_2h_3}\sum_i\frac{\partial}{\partial q_i}\Big(\frac{h_1h_2h_3}{h_i^2}\frac{\partial\psi}{\partial q_i}\Big),\qquad
\nabla\times\mathbf V = \frac1{h_1h_2h_3}\begin{vmatrix}h_1\hat{\mathbf q}_1&h_2\hat{\mathbf q}_2&h_3\hat{\mathbf q}_3\\\partial_1&\partial_2&\partial_3\\h_1V_1&h_2V_2&h_3V_3\end{vmatrix}.
$$

Here $V_i = \hat{\mathbf q}_i\cdot\mathbf V$ are the physical components.

**Why not differentiate components naively.** In curvilinear coordinates $\partial\hat{\mathbf q}_i/\partial q_j\ne0$. Taking $\nabla\cdot\mathbf V$ as $\sum\partial V_i/\partial q_i$ is wrong: it misses the derivatives of the unit vectors. The factors $h_i$ above account for them. For the same reason the vector Laplacian $\nabla^2\mathbf V$ has extra terms beyond $\nabla^2$ of each component (Arfken Eqs. 2.37 and 2.50–2.52). Use $\nabla^2\mathbf V = \nabla(\nabla\cdot\mathbf V) - \nabla\times\nabla\times\mathbf V$.

## Cylindrical coordinates

**Definition.** $x = \rho\cos\phi$, $y = \rho\sin\phi$, $z = z$. Scale factors $h_\rho = 1$, $h_\phi = \rho$, $h_z = 1$; $d\tau = \rho\,d\rho\,d\phi\,dz$ (Arfken Sec. 2.4, Eqs. 2.28–2.29).

**Operators** (Arfken Eqs. 2.33–2.36):

$$
\nabla\psi = \hat{\boldsymbol\rho}\,\partial_\rho\psi + \frac{\hat{\boldsymbol\phi}}{\rho}\,\partial_\phi\psi + \hat{\mathbf z}\,\partial_z\psi,\qquad
\nabla\cdot\mathbf V = \frac1\rho\partial_\rho(\rho V_\rho) + \frac1\rho\partial_\phi V_\phi + \partial_zV_z,
$$

$$
\nabla^2\psi = \frac1\rho\partial_\rho(\rho\,\partial_\rho\psi) + \frac1{\rho^2}\partial_\phi^2\psi + \partial_z^2\psi .
$$

Used for linear molecules about their axis, the field of a wire, and the $\Lambda$ quantum number.

## Spherical coordinates

**Definition.** $x = r\sin\theta\cos\phi$, $y = r\sin\theta\sin\phi$, $z = r\cos\theta$. Scale factors $h_r = 1$, $h_\theta = r$, $h_\phi = r\sin\theta$; $d\tau = r^2\sin\theta\,dr\,d\theta\,d\phi$ and $d\Omega = \sin\theta\,d\theta\,d\phi$ (Arfken Sec. 2.5, Eqs. 2.38–2.40).

**Operators** (Arfken Eqs. 2.46–2.49):

$$
\nabla\psi = \hat{\mathbf r}\,\partial_r\psi + \frac{\hat{\boldsymbol\theta}}{r}\partial_\theta\psi + \frac{\hat{\boldsymbol\phi}}{r\sin\theta}\partial_\phi\psi,\qquad
\nabla\cdot\mathbf V = \frac1{r^2}\partial_r(r^2V_r) + \frac1{r\sin\theta}\partial_\theta(\sin\theta\,V_\theta) + \frac1{r\sin\theta}\partial_\phi V_\phi,
$$

$$
\nabla^2\psi = \frac1{r^2}\frac{\partial}{\partial r}\Big(r^2\frac{\partial\psi}{\partial r}\Big) + \frac1{r^2}\Big[\frac1{\sin\theta}\frac{\partial}{\partial\theta}\Big(\sin\theta\frac{\partial\psi}{\partial\theta}\Big) + \frac1{\sin^2\theta}\frac{\partial^2\psi}{\partial\phi^2}\Big].
\label{lapsph}
$$

**The angular part.** The bracket in Eq. [[#lapsph]] is $-\hat L^2/\hbar^2$, so

$$
\nabla^2 = \frac1{r^2}\partial_r(r^2\partial_r) - \frac{\hat L^2}{\hbar^2r^2},\qquad \frac1{r^2}\partial_r(r^2\partial_r) = \frac1r\partial_r^2\,r .
$$

This splitting is why a central-field Schrödinger equation separates into a radial equation and spherical harmonics ([[partial-differential-equations-and-separation-of-variables]], [[hydrogen-atom]]). The eigenvalues $l(l + 1)$ of the bracket's negative are those of the Legendre equation ([[classical-orthogonal-polynomials]]).

**Unit-vector derivatives.** $\partial\hat{\mathbf r}/\partial\theta = \hat{\boldsymbol\theta}$ and $\partial\hat{\mathbf r}/\partial\phi = \sin\theta\,\hat{\boldsymbol\phi}$ (Arfken Eq. 2.44 and the lines that follow). These are the terms missed by naive differentiation.

**Radial fields.** For $\mathbf V = f(r)\hat{\mathbf r}$: $\nabla\cdot\mathbf V = r^{-2}(r^2f)'$ and $\nabla\times\mathbf V = 0$ (Arfken Eq. 2.57). With $f = r^n$ the divergence is $(n + 2)r^{n-1}$, which vanishes for the inverse-square field.

## Worked examples

!!! example "Scale factors, the spherical Laplacian, and hydrogen 1s (computed for this note)"
    **Scale factors from the metric.** Differentiating $\mathbf r(r,\theta,\phi)$ and taking lengths, Eq. [[#metric]] gives $(1, r, r|\sin\theta|)$ for spherical and $(1, \rho, 1)$ for cylindrical coordinates (sympy).

    **Laplacian, two ways.** $\psi = (x^2 - y^2)e^{-r} = r^2\sin^2\theta\cos2\phi\,e^{-r}$. At $r = 1.3$, $\theta = 0.7$, $\phi = 0.4$, Eq. [[#lapsph]] gives $-0.4814749152$. The Cartesian $\partial_x^2 + \partial_y^2 + \partial_z^2$ at the same point gives $-0.4814749152$.

    **Radial divergence.** $r^{-2}\partial_r(r^2r^n) = (n + 2)r^{n-1}$ (sympy).

    **Kinetic energy of hydrogen 1s.** $\psi = e^{-r}/\sqrt\pi$ (atomic units). With the radial part of Eq. [[#lapsph]], $\langle-\tfrac12\nabla^2\rangle = 4\pi\int_0^\infty\psi\,(-\tfrac12)\,r^{-2}(r^2\psi')'\,r^2\,dr = \tfrac12$ hartree. The Green's-theorem form $\tfrac12\int|\nabla\psi|^2d\tau$ gives the same $\tfrac12$ ([[divergence-and-gauss-theorem]]).

## Source

Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005), Sec. 2.1 (orthogonal coordinates), Sec. 2.2 (differential operators, Eqs. 2.18–2.27), Sec. 2.4 (cylindrical coordinates, Eqs. 2.28–2.37), Sec. 2.5 (spherical coordinates, Eqs. 2.38–2.57). Calculations in `Claude outputs/part0_math_batchE.py`, section B.
