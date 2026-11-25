---
id: multipolar-gauge-and-the-electric-dipole-approximation
title: The multipolar gauge and the electric dipole approximation - potentials written through the fields, the multipole interaction series, point dipoles, ordering by the wave vector, and electric dipole radiation
summary: A gauge transformation of the Taylor-expanded potentials expresses φ and A entirely through E, B and their derivatives at an expansion point. This is the multipolar gauge, with r·A = 0. Inserted into the interaction energy it gives a series in which electric multipoles couple to E and its gradients, and magnetic multipoles to B and its gradients. For a light wave the terms are ordered by k·(molecular size). The zeroth order is the electric dipole approximation; the first adds the electric quadrupole and magnetic dipole couplings that chiroptical and X-ray spectroscopies need. An oscillating dipole radiates with a sin²θ pattern and total power ω⁴μ²/12πε₀c³, the microscopic source of Rayleigh and Raman scattering. Checked: the multipolar potentials reproduce the fields (and NRS Eq. 3.178 has a sign misprint), the radiated power, and k·L for UV and soft X-rays.
status: in-progress
kind: theory
level: intermediate
tags: [multipolar-gauge, multipole-expansion, electric-dipole-approximation, electric-quadrupole, magnetic-dipole, point-dipole, dipole-radiation, near-field, far-field, power-zienau-woolley]
prerequisites: [electromagnetic-potentials-and-gauge-freedom, electromagnetic-waves-and-polarization]
related: [electric-and-magnetic-multipole-moments, charged-particle-in-an-electromagnetic-field, x-ray-absorption, optical-activity-ecd-and-mcd, raman-scattering, emission-absorption-and-spontaneous-emission]
conventions: [si-units]
key: hint
order: 50
date: 2026-11-25
---

SI units. Einstein summation over Cartesian indices. A superscript $[n]$ is an $n$th derivative at the expansion point $\mathbf r = \mathbf 0$: $\phi^{[2]}_{ij} = \partial_i\partial_j\phi|_0$, $E^{[1]}_{i;j} = \partial_jE_i|_0$ (the index before the semicolon is the field component). $\rho$ and $\mathbf j$ are the charge and current densities of the molecule.

## The multipolar gauge

**Taylor expansion.** Expand $\phi$ and $\mathbf A$ about the origin (NRS Eqs. 3.169–3.170). Use $\mathbf E = -\nabla\phi - \partial_t\mathbf A$ to replace the derivatives of $\phi$ by $\mathbf E$ and $\partial_t\mathbf A$ (NRS Eq. 3.171). Then remove the $\mathbf A$ terms with the gauge function (NRS Eqs. 3.172–3.175)

$$
\chi(\mathbf r,t) = -\int_0^1\mathbf r\cdot\mathbf A(u\mathbf r,t)\,du .
$$

**The resulting potentials.** They contain only the fields and their derivatives at the origin (NRS Eqs. 3.176–3.177):

$$
\phi(\mathbf r,t) = \phi^{[0]} - \sum_{n=0}^\infty\frac{1}{(n+1)!}r_{j_1}\cdots r_{j_n}\big(\mathbf r\cdot\mathbf E^{[n]}_{j_1\cdots j_n}\big),\qquad
\mathbf A(\mathbf r,t) = -\sum_{n=0}^\infty\frac{n+1}{(n+2)!}r_{j_1}\cdots r_{j_n}\big(\mathbf r\times\mathbf B^{[n]}_{j_1\cdots j_n}\big).
\label{multipolar}
$$

**Compact form.** In integral form:

$$
\phi(\mathbf r,t) = \phi^{[0]} - \int_0^1\mathbf r\cdot\mathbf E(u\mathbf r,t)\,du,\qquad
\mathbf A(\mathbf r,t) = \int_0^1u\,\mathbf B(u\mathbf r,t)\times\mathbf r\,du .
$$

NRS Eq. (3.178) prints the vector potential as $\int_0^1u\,\mathbf r\times\mathbf B(u\mathbf r,t)\,du$. That has the opposite sign: its curl is $-\mathbf B$, and it disagrees with their own Eqs. (3.177) and (3.180). The form above is consistent with both (checked below).

**Two simple cases** (NRS Eqs. 3.179–3.183):

- **Uniform electric field.** $\phi = -\mathbf r\cdot\mathbf E^{[0]}$ and $\mathbf A = \mathbf 0$.
- **Uniform magnetic field.** $\phi = 0$ and $\mathbf A = \tfrac12\mathbf B^{[0]}\times\mathbf r$, the familiar symmetric gauge. If $\mathbf B$ depends on time, this $\mathbf A$ implies an electric field $\mathbf E = \tfrac12\mathbf r\times\partial_t\mathbf B$ (Faraday's law). That field vanishes at the origin but has an antisymmetric gradient $E^{[1]}_{i;j} = -\tfrac12\epsilon_{ijk}\partial_tB_k$.

**Properties of the gauge.** It satisfies $\mathbf r\cdot\mathbf A = 0$ (NRS Eq. 3.185). It coincides with the Coulomb gauge only for static electric fields without external currents (NRS Eq. 3.184). The remaining gauge freedom is the choice of expansion point.

## The multipole interaction series

**The series.** Insert Eq. [[#multipolar]] into $\langle\hat H_{\rm int}\rangle = \int(\rho\phi - \mathbf j\cdot\mathbf A)\,d^3r$ (NRS Eqs. 3.186–3.191):

$$
\langle\hat H_{\rm int}\rangle = Q^{[0]}\phi^{[0]} - \sum_{n=1}^\infty\frac{1}{n!}Q^{[n]}_{j_1\cdots j_n}E^{[n-1]}_{j_1;j_2\cdots j_n} - \sum_{n=1}^\infty\frac{1}{n!}m^{[n]}_{i;j_1\cdots j_{n-1}}B^{[n-1]}_{i;j_1\cdots j_{n-1}},
\label{hint}
$$

**The moments.**

$$
Q^{[n]}_{j_1\cdots j_n} = \int r_{j_1}\cdots r_{j_n}\rho\,d^3r,\qquad
m^{[n]}_{i;j_1\cdots j_{n-1}} = \frac{n}{n+1}\int r_{j_1}\cdots r_{j_{n-1}}(\mathbf r\times\mathbf j)_i\,d^3r .
$$

- **Lowest orders.** The total charge couples to $\phi$. The dipole $\boldsymbol\mu = \int\mathbf r\rho\,d^3r$ couples to $\mathbf E$. The quadrupole $Q^{[2]}_{ij}$ couples to the field gradient. The magnetic dipole $\mathbf m = \tfrac12\int\mathbf r\times\mathbf j\,d^3r$ couples to $\mathbf B$.
- **No magnetic monopole.** There is none, because $\nabla\cdot\mathbf B = 0$.
- **Interpretation.** Most molecular properties can be read as the change of these multipoles in response to fields.

## Point dipoles

**Electric dipole.** Two charges $\pm q$ separated by $\boldsymbol\delta$, in the limit $\delta\to0$ with $\boldsymbol\mu = q\boldsymbol\delta$ fixed, give the potential $\phi = \boldsymbol\mu\cdot\mathbf r/4\pi\varepsilon_0r^3$ (NRS Eqs. 3.192–3.193).

**Magnetic dipole.** A current loop of radius $R$ has $\mathbf m = I\pi R^2\mathbf e_z$. In the limit $R\to0$ it gives $\mathbf A = \frac{\mu_0}{4\pi}\mathbf m\times\mathbf r/r^3$ (NRS Eqs. 3.194–3.202; the loop check is in [[maxwell-equations-and-helmholtz-decomposition]]).

**Their fields** (NRS Eqs. 3.203–3.205):

$$
\mathbf E_{\rm pE1} = -\frac{\boldsymbol\mu}{3\varepsilon_0}\delta(\mathbf r) + \frac{1}{4\pi\varepsilon_0}\frac{3\mathbf r(\mathbf r\cdot\boldsymbol\mu) - \boldsymbol\mu r^2}{r^5},\qquad
\mathbf B_{\rm pM1} = \frac{1}{c^2}\Big[\frac{2\mathbf m}{3\varepsilon_0}\delta(\mathbf r) + \frac{1}{4\pi\varepsilon_0}\frac{3\mathbf r(\mathbf r\cdot\mathbf m) - \mathbf mr^2}{r^5}\Big].
$$

The two fields are identical outside the origin, with angular form $(2\cos\theta\,\mathbf e_r + \sin\theta\,\mathbf e_\theta)/r^3$. The contact terms differ, in sign and by a factor 2, because the two limits are different. The magnetic contact term is the origin of the Fermi-contact hyperfine interaction ([[hyperfine-coupling-and-epr]]).

## Ordering by the wave vector

**The expansion parameter.** For a plane wave, $kE = \omega B$, so each further spatial derivative brings a factor $k$. A truncation at order $n$ in $\mathbf E$ must be matched by order $n-1$ in $\mathbf B$ (NRS Eqs. 3.206–3.209):

$$
k^0:\ -\boldsymbol\mu\cdot\mathbf E^{[0]}\quad\text{(electric dipole approximation)},\qquad
k^1:\ -\tfrac12Q^{[2]}_{ij}E^{[1]}_{i;j} - \mathbf m\cdot\mathbf B^{[0]}\quad\text{(electric quadrupole + magnetic dipole)}.
$$

**Validity.** The electric dipole approximation holds when the molecule is small compared with the wavelength, $kL\ll1$.

- **UV light.** It is excellent for small and medium molecules in UV light.
- **Short wavelengths.** It degrades for nanoscale systems and short wavelengths (NRS Fig. 3.9).
- **The $k^1$ terms.** These are essential whenever the $k^0$ term vanishes or cancels in an orientational average: optical rotation, circular dichroism and ROA, and quadrupole-allowed pre-edge X-ray features of transition metals.

## Electric dipole radiation

**Fields of an oscillating dipole.** A point dipole $\mathbf p = \boldsymbol\mu e^{-i\omega t}\delta(\mathbf r)$ has current $\mathbf j = -i\omega\boldsymbol\mu e^{-i\omega t}\delta(\mathbf r)$. The retarded Lorenz-gauge potentials then give (NRS Eqs. 3.251–3.263)

$$
\mathbf E = \frac{\omega^2}{4\pi\varepsilon_0c^2r}\Big(\boldsymbol\mu - \frac{(\mathbf r\cdot\boldsymbol\mu)\mathbf r}{r^2}\Big)e^{-i\omega(t-r/c)} + \frac{1}{4\pi\varepsilon_0}\Big(\frac1{r^3} - \frac{i\omega}{cr^2}\Big)\Big(\frac{3(\mathbf r\cdot\boldsymbol\mu)\mathbf r}{r^2} - \boldsymbol\mu\Big)e^{-i\omega(t-r/c)} .
$$

**Far field** ($r\gg c/\omega$). Only the $1/r$ terms survive (NRS Eqs. 3.264–3.266):

$$
\langle\mathbf S\rangle_T = \frac{\omega^4\mu^2}{32\pi^2\varepsilon_0c^3}\frac{\mathbf r}{r^3}\sin^2\theta,\qquad P = \oint\langle\mathbf S\rangle_T\cdot d\mathbf a = \frac{\omega^4\mu^2}{12\pi\varepsilon_0c^3},
\label{power}
$$

with $\theta$ the angle between $\boldsymbol\mu$ and the direction of observation.

- **No emission along the dipole.** Nothing is emitted along the dipole axis.
- **Scattering.** The $\omega^4$ law is why the sky is blue. The same expression, with $\boldsymbol\mu$ the induced dipole, gives Rayleigh and Raman scattered intensities ([[raman-scattering]]).

**Near field** ($r\ll c/\omega$). The electric field is the static dipole field times $e^{-i\omega t}$. The magnetic field is $\pi/2$ out of phase and smaller by a factor $\omega r/c$ (NRS Eqs. 3.267–3.268). For 200 nm light, $c/\omega\approx600\,a_0$. Every molecule of a typical embedding model lies in the near field, so instantaneous electrostatics is enough for intermolecular interactions.

## Worked example

!!! example "Checks of the multipolar gauge and of radiation (computed for this note)"
    **Multipolar potentials (sympy).** For $\mathbf E(\mathbf r) = \mathbf E_0 + g(x, y, -2z)$ (uniform plus a traceless, curl-free gradient) and a uniform $\mathbf B_0$:

    - $\phi = -\int_0^1\mathbf r\cdot\mathbf E(u\mathbf r)du$ gives back $-\nabla\phi = \mathbf E$. For the gradient part it is $\phi = -\tfrac g2(x^2 + y^2 - 2z^2)$.
    - $\mathbf A = \int_0^1u\,\mathbf B_0\times\mathbf r\,du$ gives $\nabla\times\mathbf A = \mathbf B_0$ and $\mathbf r\cdot\mathbf A = 0$.
    - The form printed in NRS Eq. (3.178), $\int_0^1u\,\mathbf r\times\mathbf B\,du$, gives $\nabla\times\mathbf A = -\mathbf B_0$.

    **Radiated power.** For $\mu = 10^{-29}$ C m oscillating at 500 nm, integrating Eq. [[#power]] over a sphere gives $2.239651\times10^{-12}$ W, equal to $\omega^4\mu^2/12\pi\varepsilon_0c^3$.

    **Electric dipole parameter.** For a molecule of size $L = 1$ nm (about C₆₀):

    - at 200 nm, $kL = 0.031$;
    - at 290 eV, the carbon K-edge with $\lambda = 4.28$ nm, $kL = 1.47$.

    In the UV the dipole approximation is safe. At the carbon K-edge it is not safe in general, and NRS note that K-edge spectra of second-row elements are nonetheless treated in it.

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Sec. 3.3.1, Eqs. (3.169)–(3.185); Sec. 3.3.2, Eqs. (3.186)–(3.205), Figs. 3.6–3.8 (described); Sec. 3.3.3, Eqs. (3.206)–(3.209), Fig. 3.9 (described); Sec. 3.3.7, Eqs. (3.251)–(3.268). The total-power integral, the blue-sky remark and the transition-metal pre-edge example are general knowledge, not from NRS. The checks are in `Claude outputs/part1_fields_batchD.py`, sections B and E.
