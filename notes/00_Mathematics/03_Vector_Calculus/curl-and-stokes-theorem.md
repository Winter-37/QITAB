---
id: curl-and-stokes-theorem
title: Curl and Stokes's theorem - circulation, the curl as circulation per unit area, rigid rotation, irrotational fields and scalar potentials, and why topology matters
summary: The curl ∇ × V is the vector whose component along a unit normal n is the circulation of V around a small loop perpendicular to n, per unit area. In Cartesian components it is the determinant with rows (x̂, ŷ, ẑ), ∇ and V, or (∇ × V)_i = ε_ijk ∂_j V_k. For a rigid rotation v = ω × r it is 2ω, which is why it measures local rotation. Stokes's theorem equates the circulation around a closed curve to the flux of the curl through any surface it bounds. An irrotational field on a simply connected region is a gradient. The field (−y, x)/(x² + y²) is a counterexample when the region has a hole: zero curl, circulation 2π. Worked examples: the curl of ω × r, a Stokes check, the wire field, and A = ½B × r.
status: in-progress
kind: theory
level: introductory
tags: [curl, rotation, circulation, stokes-theorem, irrotational, vorticity, levi-civita, vector-potential, simply-connected, aharonov-bohm]
prerequisites: [divergence-and-gauss-theorem]
related: [scalar-and-vector-fields-and-the-gradient, vector-identities-and-the-laplacian, curvilinear-coordinates, electromagnetic-potentials-and-gauge-freedom, berry-phase]
key: stokes
order: 40
date: 2026-11-25
---

Cartesian coordinates in a right-handed frame. $d\boldsymbol\lambda$ (or $d\mathbf r$) is the line element of a curve. The orientation of a surface and of its boundary curve are tied by the right-hand rule: with the thumb along $\hat{\mathbf n}$, the fingers follow the boundary.

## Circulation and the curl

**Circulation.** The circulation of $\mathbf V$ around a closed curve $C$ is $\oint_C\mathbf V\cdot d\boldsymbol\lambda$. For a fluid it measures how much the flow goes around the loop.

**Definition of the curl.** Take a small loop of area $\Delta\sigma$ with normal $\hat{\mathbf n}$. Then (Arfken Sec. 1.8)

$$
\hat{\mathbf n}\cdot(\nabla\times\mathbf V) = \lim_{\Delta\sigma\to0}\frac1{\Delta\sigma}\oint_C\mathbf V\cdot d\boldsymbol\lambda .
\label{curldef}
$$

For a small rectangle in the $xy$ plane, Arfken's count of the four sides gives $(\partial V_y/\partial x - \partial V_x/\partial y)\,dx\,dy$ (Eq. 1.76). In full:

$$
\nabla\times\mathbf V = \begin{vmatrix}\hat{\mathbf x}&\hat{\mathbf y}&\hat{\mathbf z}\\\partial_x&\partial_y&\partial_z\\V_x&V_y&V_z\end{vmatrix},\qquad (\nabla\times\mathbf V)_i = \epsilon_{ijk}\,\partial_jV_k .
$$

The determinant is mnemonic only: the second row acts on the third. The Levi-Civita form is the one to calculate with ([[scalars-and-vectors]]).

**Properties.**

- **Type.** The curl of a polar vector field is a pseudovector field. The magnetic field $\mathbf B = \nabla\times\mathbf A$ is the standard example.
- **Product rule.** $\nabla\times(f\mathbf V) = f\,\nabla\times\mathbf V + \nabla f\times\mathbf V$ (Arfken Eq. 1.70).
- **Radial fields.** Every central field $f(r)\mathbf r$ has zero curl (Arfken Example 1.8.2).

**Rigid rotation.** For $\mathbf v = \boldsymbol\omega\times\mathbf r$ with constant $\boldsymbol\omega$, BAC–CAB with $\nabla$ in place of the first vector gives

$$
\nabla\times(\boldsymbol\omega\times\mathbf r) = \boldsymbol\omega(\nabla\cdot\mathbf r) - (\boldsymbol\omega\cdot\nabla)\mathbf r = 3\boldsymbol\omega - \boldsymbol\omega = 2\boldsymbol\omega .
\label{rigid}
$$

The curl is twice the local angular velocity. The same calculation shows that $\mathbf A = \tfrac12\mathbf B\times\mathbf r$ is a vector potential of a uniform field: $\nabla\times\mathbf A = \mathbf B$ (Arfken Example 1.8.1). This is the symmetric gauge of molecular magnetic properties, and $\mathbf r$ is measured from the gauge origin.

**Irrotational fields.** $\nabla\times\mathbf V = 0$. Every gradient is irrotational, since $\nabla\times\nabla\varphi = 0$ ([[vector-identities-and-the-laplacian]]). The converse requires a simply connected region (below).

## Stokes's theorem

**Statement.** For a surface $S$ bounded by the closed curve $\partial S$, oriented by the right-hand rule (Arfken Eq. 1.111 and Sec. 1.12),

$$
\oint_{\partial S}\mathbf V\cdot d\boldsymbol\lambda = \int_S(\nabla\times\mathbf V)\cdot d\boldsymbol\sigma .
\label{stokes}
$$

**Proof idea.** Divide $S$ into small cells and apply Eq. [[#curldef]] to each. Interior edges are traversed twice in opposite directions and cancel, leaving the outer boundary.

**Any surface will do.** The right side is the same for every surface with the same boundary. This follows from $\nabla\cdot(\nabla\times\mathbf V) = 0$ and Gauss's theorem applied to the volume between two such surfaces.

**Other forms.** With a constant vector one finds $\oint\varphi\,d\boldsymbol\lambda = \int d\boldsymbol\sigma\times\nabla\varphi$ (Arfken Eq. 1.113).

**Gauss and Stokes together.** Both say that the integral of a derivative over a region equals the integral of the function over its boundary. In one dimension this is the fundamental theorem of calculus ([[integral-calculus]]). In two, with $\mathbf V = (P, Q, 0)$, Stokes reduces to Green's theorem in the plane, $\oint(P\,dx + Q\,dy) = \iint(\partial_xQ - \partial_yP)\,dx\,dy$.

## Irrotational fields and topology

**On a simply connected region** (every loop can shrink to a point inside it), $\nabla\times\mathbf F = 0$ implies $\oint\mathbf F\cdot d\boldsymbol\lambda = 0$ for every loop, by Eq. [[#stokes]]. So $\mathbf F = -\nabla V$, and line integrals are path independent ([[scalar-and-vector-fields-and-the-gradient]]).

**When there is a hole.** $\mathbf V = (-y, x, 0)/(x^2 + y^2)$ is the magnetic field around a straight wire, up to constants. It has zero curl everywhere off the $z$ axis, but its circulation around any loop enclosing the axis is $2\pi$. No surface bounded by such a loop avoids the axis, so Stokes's theorem cannot be applied in the region where the curl vanishes. The field is locally $\nabla\phi$ with $\phi$ the azimuthal angle, but $\phi$ is multivalued, so the field is not globally a gradient.

**In quantum mechanics.** The same topology underlies the Aharonov–Bohm effect, where an electron encircles a field-free region with $\oint\mathbf A\cdot d\boldsymbol\lambda\ne0$. It also underlies geometric phases around conical intersections ([[berry-phase]]).

## Worked examples

!!! example "Rotation, Stokes, and the wire (computed for this note)"
    **Rigid rotation.** sympy: $\nabla\times(\mathbf w\times\mathbf r) = (2w_1, 2w_2, 2w_3)$, Eq. [[#rigid]].

    **Stokes on a disc.** For $\mathbf V = (-y^3, x^3, z)$ and the unit circle in the $xy$ plane:

    - The circulation is $\int_0^{2\pi}(\sin^4t + \cos^4t)\,dt = 3\pi/2$.
    - $(\nabla\times\mathbf V)_z = 3x^2 + 3y^2 = 3\rho^2$, and its flux through the unit disc is $\int_0^{2\pi}\int_0^13\rho^2\,\rho\,d\rho\,d\phi = 3\pi/2$.

    Both agree.

    **The wire field.** For $\mathbf V = (-y, x, 0)/(x^2 + y^2)$: $\nabla\times\mathbf V = 0$ away from the axis, and $\oint\mathbf V\cdot d\boldsymbol\lambda$ around the unit circle is $2\pi$. The nonzero circulation is carried by the axis, where the field is singular.

## Source

Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005), Sec. 1.8 (curl, Eqs. 1.70 and 1.76, Examples 1.8.1–1.8.2), Sec. 1.12 (Stokes's theorem, Eqs. 1.111 and 1.113), Sec. 1.13 (potential theory). The Aharonov–Bohm remark is general knowledge. Calculations in `Claude outputs/part0_math_batchE.py`, section B.
