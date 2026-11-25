---
id: scalar-and-vector-fields-and-the-gradient
title: Scalar and vector fields and the gradient - the del operator, directional derivatives, normals to level surfaces, line integrals and conservative fields
summary: A scalar field assigns a number to every point of space, a vector field a vector. The gradient ∇φ = (∂φ/∂x, ∂φ/∂y, ∂φ/∂z) is the vector whose dot product with a displacement gives the change of φ, dφ = ∇φ·dr. It points in the direction of fastest increase, its length is that rate, and it is normal to the level surfaces of φ. Its line integral depends only on the endpoints, which is why a force F = −∇V is conservative and its work is a potential-energy difference. Worked examples: ∇(1/r) = −r/r³ (the Coulomb field), ∇rⁿ, a directional derivative, and a path-independence check.
status: in-progress
kind: theory
level: introductory
tags: [scalar-field, vector-field, gradient, del-operator, nabla, directional-derivative, level-surface, line-integral, conservative-field, potential]
prerequisites: [scalars-and-vectors, differential-calculus]
related: [divergence-and-gauss-theorem, curl-and-stokes-theorem, vector-identities-and-the-laplacian, curvilinear-coordinates, multivariable-taylor-expansion]
key: grad
order: 20
date: 2026-11-25
---

Cartesian coordinates; $r = |\mathbf r|$ and $\hat{\mathbf r} = \mathbf r/r$. Curvilinear forms are in [[curvilinear-coordinates]].

## Fields

**Definitions.** A **scalar field** $\varphi(\mathbf r)$ assigns a number to each point: temperature, electrostatic potential, electron density $\rho(\mathbf r)$, a wave function. A **vector field** $\mathbf V(\mathbf r)$ assigns a vector: the electric field, a fluid velocity, a current density $\mathbf j(\mathbf r)$. A field is a scalar or vector field when its value at each point transforms as a scalar or vector under rotation ([[scalars-and-vectors]]).

**Pictures.** Scalar fields are drawn as level (iso-) surfaces $\varphi = $ const. Vector fields are drawn as arrows or as field lines tangent to $\mathbf V$ everywhere.

## The gradient

**Definition.** The vector differential operator del (nabla) is

$$
\nabla = \hat{\mathbf x}\frac{\partial}{\partial x} + \hat{\mathbf y}\frac{\partial}{\partial y} + \hat{\mathbf z}\frac{\partial}{\partial z}.
$$

Acting on a scalar field it gives the gradient $\nabla\varphi = (\partial_x\varphi, \partial_y\varphi, \partial_z\varphi)$ (Arfken Sec. 1.6). Its defining property is the total differential of [[differential-calculus]]:

$$
d\varphi = \nabla\varphi\cdot d\mathbf r .
\label{grad}
$$

$\nabla\varphi$ is a vector: by the chain rule, $\partial/\partial x'_i = a_{ij}\,\partial/\partial x_j$, which is the rotation rule of [[scalars-and-vectors]].

**Directional derivative.** The rate of change of $\varphi$ along a unit vector $\hat{\mathbf u}$ is $D_{\hat{\mathbf u}}\varphi = \nabla\varphi\cdot\hat{\mathbf u} = |\nabla\varphi|\cos\theta$. It is largest along $\nabla\varphi$ itself, so:

- **direction.** The gradient points in the direction of steepest ascent; $-\nabla\varphi$ points downhill. Steepest descent and every gradient-based geometry optimizer use this.
- **magnitude.** $|\nabla\varphi|$ is the largest rate of increase.
- **normal.** Along a level surface $d\varphi = 0$, so $\nabla\varphi\cdot d\mathbf r = 0$ for every tangent displacement. The gradient is normal to the level surfaces. A molecular surface defined by $\rho(\mathbf r) = $ const has normal $\nabla\rho/|\nabla\rho|$.

**Rules.** $\nabla$ is linear and obeys the product rule, $\nabla(fg) = f\nabla g + g\nabla f$, and the chain rule, $\nabla f(\varphi) = f'(\varphi)\nabla\varphi$.

**Radial functions.** For $\varphi = f(r)$, $\nabla f(r) = f'(r)\,\hat{\mathbf r}$, since $\nabla r = \mathbf r/r$. In particular

$$
\nabla r^n = n\,r^{n-2}\,\mathbf r,\qquad \nabla\frac1r = -\frac{\mathbf r}{r^3} = -\frac{\hat{\mathbf r}}{r^2}.
\label{gradr}
$$

The second is the Coulomb field: $\mathbf E = -\nabla\phi$ with $\phi = q/(4\pi\varepsilon_0r)$ gives $\mathbf E = q\hat{\mathbf r}/(4\pi\varepsilon_0r^2)$.

## Line integrals and conservative fields

**Line integral.** Along a curve $C$ parametrized by $\mathbf r(t)$, $\int_C\mathbf V\cdot d\mathbf r = \int\mathbf V(\mathbf r(t))\cdot\mathbf r'(t)\,dt$. It depends on the path in general (Arfken Sec. 1.10).

**Gradient theorem.** For a gradient field, Eq. [[#grad]] integrates directly:

$$
\int_{\mathbf a}^{\mathbf b}\nabla\varphi\cdot d\mathbf r = \varphi(\mathbf b) - \varphi(\mathbf a),\qquad \oint\nabla\varphi\cdot d\mathbf r = 0 .
\label{gradthm}
$$

The integral depends only on the endpoints. This is the multidimensional fundamental theorem of calculus.

**Conservative fields.** For a field $\mathbf F$ on a simply connected region, the following are equivalent:

1. $\mathbf F = -\nabla V$ for some scalar potential $V$;
2. $\oint\mathbf F\cdot d\mathbf r = 0$ for every closed loop;
3. $\int\mathbf F\cdot d\mathbf r$ is path independent;
4. $\nabla\times\mathbf F = 0$ ([[curl-and-stokes-theorem]]).

The potential is then recovered by integrating along any path, $V(\mathbf r) = -\int_{\mathbf r_0}^{\mathbf r}\mathbf F\cdot d\mathbf r$. For a conservative force the work done is $-\Delta V$, so kinetic plus potential energy is conserved. The forces on nuclei in the Born–Oppenheimer approximation are $-\nabla_{\mathbf R}E(\mathbf R)$, gradients of the potential energy surface.

**Gradients in many dimensions.** Nothing here depends on three dimensions. The gradient of $E(\mathbf R)$ with respect to $3N$ nuclear coordinates is the nuclear gradient; its second derivatives form the Hessian ([[multivariable-taylor-expansion]]).

## Worked examples

!!! example "Coulomb field, a directional derivative, path independence (computed for this note)"
    **Radial gradients.** sympy confirms $\nabla(1/r) + \mathbf r/r^3 = 0$ and $\nabla r^n - n r^{n-2}\mathbf r = 0$, Eq. [[#gradr]].

    **Directional derivative.** $\varphi = x^2y + z^3$ has $\nabla\varphi = (2xy, x^2, 3z^2) = (2, 1, 3)$ at $(1, 1, 1)$. Along $\hat{\mathbf u} = (1, 2, 2)/3$, $D_{\hat{\mathbf u}}\varphi = (2 + 2 + 6)/3 = 10/3$. The steepest rate there is $|\nabla\varphi| = \sqrt{14} = 3.742$.

    **Path independence.** Take $\mathbf F = \nabla\varphi$ for the same $\varphi$ and go from $(0, 0, 0)$ to $(1, 1, 1)$. Along the straight line $\mathbf r = t(1, 1, 1)$: $\int_0^1(2t^2 + t^2 + 3t^2)\,dt = 2$. Along the three axis-parallel legs $x$, then $y$, then $z$: $0 + 1 + 1 = 2$. Both equal $\varphi(1,1,1) - \varphi(0,0,0) = 2$, as Eq. [[#gradthm]] requires.

## Source

Arfken and Weber, *Mathematical Methods for Physicists* (Elsevier, 2005), Sec. 1.6 (gradient, Example 1.6.1 for radial functions), Sec. 1.10 (line integrals), Sec. 1.13 (scalar potential and conservative forces). Calculations in `Claude outputs/part0_math_batchE.py`, section B; the path-independence integrals are elementary.
