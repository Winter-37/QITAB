---
id: electromagnetic-potentials-and-gauge-freedom
title: Electromagnetic potentials and gauge freedom - scalar and vector potentials, gauge transformations, the Lorenz and Coulomb gauges, and the covariant formulation with the field tensor
summary: Because B has no divergence it is the curl of a vector potential, and Faraday's law then makes E + ∂A/∂t the gradient of a scalar potential. The potentials solve the homogeneous Maxwell pair identically. They are fixed only up to a gauge transformation A → A + ∇χ, φ → φ − ∂χ/∂t, which leaves E and B unchanged. The Lorenz gauge gives retarded wave equations for both potentials. The Coulomb gauge gives an instantaneous scalar potential and puts all retardation in the transverse vector potential. Gauge conditions define classes, not single potentials. In four-vector form the whole theory is one equation, derived from the Lagrangian density with the field tensor F. Checked symbolically: gauge invariance of E and B, the gauge classes, and the field-tensor invariant.
status: in-progress
kind: theory
level: intermediate
tags: [vector-potential, scalar-potential, gauge-transformation, lorenz-gauge, coulomb-gauge, gauge-invariance, four-vector, field-tensor, lagrangian-density, lorentz-covariance]
prerequisites: [maxwell-equations-and-helmholtz-decomposition]
related: [charged-particle-in-an-electromagnetic-field, multipolar-gauge-and-the-electric-dipole-approximation, minimal-coupling-and-aharonov-bohm, magnetizability-and-gauge-origin]
conventions: [si-units]
key: gauge
order: 20
date: 2026-11-25
---

SI units, notation of [[maxwell-equations-and-helmholtz-decomposition]]: $\Box^2 = \nabla^2 - c^{-2}\partial_t^2$, and $\parallel$/$\perp$ denote irrotational and solenoidal parts. In the four-vector part, Greek indices run over 1–4 and repeated indices are summed. NRS use an imaginary fourth component instead of a metric.

## Potentials

**Definition.** $\nabla\cdot\mathbf B = 0$ means $\mathbf B$ is solenoidal, so it is the curl of a vector potential. Inserting this into Faraday's law gives $\nabla\times(\mathbf E + \partial_t\mathbf A) = \mathbf 0$, so $\mathbf E + \partial_t\mathbf A$ is a gradient (NRS Eqs. 3.49–3.51):

$$
\mathbf B = \nabla\times\mathbf A,\qquad \mathbf E = -\nabla\phi - \partial_t\mathbf A,\qquad
\mathbf E_\parallel = -\nabla\phi - \partial_t\mathbf A_\parallel,\quad \mathbf E_\perp = -\partial_t\mathbf A_\perp .
$$

**What the potentials buy.** The homogeneous Maxwell pair is then satisfied identically, and only the inhomogeneous pair remains (NRS Eqs. 3.52–3.53):

$$
\nabla^2\phi + \partial_t(\nabla\cdot\mathbf A) = -\rho/\varepsilon_0,\qquad
\Box^2\mathbf A - \nabla\Big[\nabla\cdot\mathbf A + \frac1{c^2}\partial_t\phi\Big] = -\mu_0\mathbf j .
$$

## Gauge freedom

**Gauge transformation.** Only $\nabla\times\mathbf A$ is fixed by $\mathbf B$, so the irrotational part of $\mathbf A$ can be changed by a gradient. Since $\mathbf A_\parallel$ also enters $\mathbf E_\parallel$, the scalar potential must change with it. For any gauge function $\chi(\mathbf r,t)$ (NRS Eqs. 3.54–3.55):

$$
\mathbf A\to\mathbf A' = \mathbf A + \nabla\chi,\qquad \phi\to\phi' = \phi - \partial_t\chi
\qquad\Rightarrow\qquad \mathbf E' = \mathbf E,\quad \mathbf B' = \mathbf B .
\label{gauge}
$$

**Lorenz gauge.** NRS call it the Lorentz gauge. It is Lorentz invariant, and it decouples the potentials into retarded wave equations (NRS Eqs. 3.56–3.58):

$$
\nabla\cdot\mathbf A + \frac1{c^2}\partial_t\phi = 0:\qquad
\Box^2\mathbf A = -\mu_0\mathbf j,\quad \Box^2\phi = -\rho/\varepsilon_0,\qquad
\phi(\mathbf r_1,t) = \frac{1}{4\pi\varepsilon_0}\int\frac{\rho(\mathbf r_2,t_r)}{r_{12}}d^3r_2,\quad
\mathbf A(\mathbf r_1,t) = \frac{\mu_0}{4\pi}\int\frac{\mathbf j(\mathbf r_2,t_r)}{r_{12}}d^3r_2 .
$$

**Coulomb gauge.** It removes the irrotational part of $\mathbf A$ (NRS Eqs. 3.59–3.64):

$$
\nabla\cdot\mathbf A = 0:\qquad \nabla^2\phi = -\rho/\varepsilon_0,\quad \phi(\mathbf r_1,t) = \frac{1}{4\pi\varepsilon_0}\int\frac{\rho(\mathbf r_2,t)}{r_{12}}d^3r_2,\qquad
\Box^2\mathbf A_\perp = -\mu_0\mathbf j_\perp .
$$

Here the scalar potential is instantaneous, with no retarded time. This does not violate relativity, because $\phi$ is an auxiliary quantity and the fields stay causal: the retardation sits in $\mathbf A_\perp$. The Coulomb gauge is the natural one for molecules. It separates the instantaneous Coulomb interaction, the dominant interaction in chemistry, from the transverse photon field.

**Gauge conditions define classes.** A further transformation with $\nabla^2\chi = 0$ keeps the Coulomb condition. One with $\Box^2\chi = 0$ keeps the Lorenz condition (NRS Eqs. 3.65–3.66). "The" Coulomb or Lorenz gauge is therefore a family of potentials.

**In quantum mechanics.** A gauge transformation of the potentials must be accompanied by a local phase change of the wave function, $\psi\to e^{iq\chi/\hbar}\psi$ ([[minimal-coupling-and-aharonov-bohm]]). In molecular property calculations, the choice of gauge origin for a uniform magnetic field is such a transformation. Approximate wave functions that do not carry the compensating phase give origin-dependent results ([[magnetizability-and-gauge-origin]]).

## Covariant form

**Four-vectors.** Write four-vectors with an imaginary time component (NRS Eqs. 3.92–3.98):

$$
r_\mu = (\mathbf r, ict),\quad p_\mu = (\mathbf p, iE/c),\quad A_\mu = (\mathbf A, i\phi/c),\quad j_\mu = (\mathbf j, ic\rho),\quad \partial_\mu = (\nabla, -i\partial_t/c).
$$

Lorentz transformations preserve $r_\mu r_\mu = r^2 - c^2t^2$.

**The theory in four-vector form.**

- **Continuity.** $\partial_\mu j_\mu = 0$.
- **D'Alembertian.** $\Box^2 = \partial_\mu\partial_\mu$.
- **Gauge transformation.** $A_\mu\to A_\mu + \partial_\mu\chi$.
- **Lorenz condition.** $\partial_\mu A_\mu = 0$.
- **Inhomogeneous Maxwell pair.** One equation (NRS Eqs. 3.99–3.102):

$$
\Box^2A_\mu - \partial_\mu(\partial_\nu A_\nu) = -\frac{1}{\varepsilon_0c^2}j_\mu .
\label{covariant}
$$

- **Magnetic induction is relativistic.** $\phi/c^2$ transforms like $t$. So a purely electrostatic potential in one frame acquires a vector-potential part in a moving frame: magnetism is a relativistic effect.

**Lagrangian density.** The field equations follow from (NRS Eqs. 3.108–3.114)

$$
\mathcal L(A_\alpha,\partial_\beta A_\alpha) = j_\alpha A_\alpha - \frac{\varepsilon_0c^2}{4}F_{\alpha\beta}F_{\alpha\beta},\qquad F_{\alpha\beta} = \partial_\alpha A_\beta - \partial_\beta A_\alpha,
$$

through the Euler–Lagrange equations for fields, $\partial\mathcal L/\partial A_\alpha - \partial_\beta[\partial\mathcal L/\partial(\partial_\beta A_\alpha)] = 0$.

- **The field tensor.** It is antisymmetric, with $F_{12} = B_z$, $F_{23} = B_x$, $F_{31} = B_y$ and $F_{k4} = -iE_k/c$ (NRS Eq. 3.112).
- **Field part.** For the free field, $\mathcal L_f = \tfrac12\varepsilon_0(E^2 - c^2B^2)$, since $F_{\alpha\beta}F_{\alpha\beta} = 2(B^2 - E^2/c^2)$.
- **Interaction part.** $L_{\rm int} = \int(\mathbf j\cdot\mathbf A - \rho\phi)\,d^3r$: currents couple to $\mathbf A$, charges to $\phi$. This is the starting point of [[charged-particle-in-an-electromagnetic-field]].

## Worked example

!!! example "Symbolic checks (sympy, computed for this note)"
    **Gauge invariance.** For arbitrary test potentials $\phi = \sin(xy)e^{-t} + z^2t$, $\mathbf A = (yzt, t^2\cos x, xyz)$ and gauge function $\chi = e^{x-t}\sin y + xyzt^3$, the transformed potentials of Eq. [[#gauge]] give identical $\mathbf E$ and $\mathbf B$ component by component.

    **Classes.** $\chi = xy + e^x\cos y$ is harmonic ($\nabla^2\chi = 0$), so it preserves any Coulomb-gauge $\mathbf A$. $\chi = \cos(kx - ckt)$ satisfies $\Box^2\chi = 0$, so it preserves the Lorenz condition.

    **Field-tensor invariant.** From the explicit matrix of NRS Eq. (3.112), $\sum_{\alpha\beta}F_{\alpha\beta}^2 = 2(B^2 - E^2/c^2)$. With the prefactor $\varepsilon_0c^2/4 = 1/4\mu_0$, the field Lagrangian density is therefore $-\tfrac14\varepsilon_0c^2F_{\alpha\beta}F_{\alpha\beta} = \tfrac12\varepsilon_0(E^2 - c^2B^2)$, NRS Eq. (3.113).

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Sec. 3.1.4, Eqs. (3.49)–(3.66); Sec. 3.1.6, Eqs. (3.91)–(3.102); Sec. 3.2.1, Eqs. (3.107)–(3.114). The quantum-mechanical phase of a gauge transformation is from [[minimal-coupling-and-aharonov-bohm]]. The checks are in `Claude outputs/part1_fields_batchD.py`, section B.
