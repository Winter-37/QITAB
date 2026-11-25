---
id: electric-and-magnetic-multipole-moments
title: Electric and magnetic multipole moments - origin dependence, general versus traceless forms, spherical multipoles, counting, and what symmetry allows
summary: Only the lowest nonvanishing multipole of a charge or current distribution is independent of the origin. A dipole is origin independent only for a neutral system, a quadrupole only if the dipole also vanishes. The Cartesian moments Q^[n] (all (n+1)(n+2)/2 of them) can be reduced to traceless moments Θ^[n] (2n+1 of them), equivalent to spherical multipoles r^ℓY*_ℓm. The traceless forms are complete for static fields from external sources, but time-dependent fields also couple to the traces, so the general moments are the safer definition. Parity makes odd electric and even magnetic moments vanish for states of definite parity, and a state of angular momentum L carries electric multipoles up to order 2L. Magnetic multipoles are traceless by construction. Computed: the water dipole and quadrupole and their origin dependence, checked against the shift rule and against the measured quadrupole.
status: in-progress
kind: theory
level: intermediate
tags: [multipole-moments, electric-quadrupole, traceless-quadrupole, buckingham, spherical-multipoles, origin-dependence, parity, magnetic-multipoles, unsold-theorem, addition-theorem]
prerequisites: [multipolar-gauge-and-the-electric-dipole-approximation]
related: [central-potentials-and-spherical-harmonics, parity-and-parity-selection-rules, hyperfine-coupling-and-epr, magnetizability-and-gauge-origin, rotational-averages-and-isotropic-tensors]
conventions: [si-units]
key: shift
order: 60
date: 2026-11-25
---

SI units in the formulas; atomic units ($e a_0$, $e a_0^2$) in the worked example. $Q^{[n]}$ are the Cartesian electric moments and $m^{[n]}$ the magnetic moments of [[multipolar-gauge-and-the-electric-dipole-approximation]]. $\Theta^{[n]}$ are traceless moments, $Q = Q^{[0]}$ the total charge.

## Origin dependence

**Dipoles.** Moving the origin to $\mathbf G$ (NRS Eqs. 3.210–3.211):

$$
\boldsymbol\mu_G = \boldsymbol\mu_0 - \mathbf G\,Q^{[0]},\qquad \mathbf m_G = \mathbf m_0 - \mathbf G\times\tfrac12\int\mathbf j\,d^3r .
$$

The dipole of an ion depends on the origin; that of a neutral molecule does not. The magnetic dipole is origin independent if the total current vanishes, which it does for stationary bound states.

**Quadrupoles.** In the same way,

$$
Q^{[2]}_G = Q^{[2]}_0 - \mathbf G\boldsymbol\mu - \boldsymbol\mu\mathbf G + \mathbf G\mathbf G\,Q^{[0]},\qquad
\Theta_G = \Theta_0 - \tfrac32\big(\mathbf G\boldsymbol\mu + \boldsymbol\mu\mathbf G - \tfrac23(\mathbf G\cdot\boldsymbol\mu)\mathbf 1\big)\quad(Q^{[0]} = 0).
\label{shift}
$$

**The general rule.** The general statement is the rule: only the lowest nonvanishing multipole is an observable independent of the origin. Polar molecules (water) report quadrupoles at a stated origin, usually the centre of mass. Nonpolar ones (CO₂, N₂, benzene) have origin-independent quadrupoles.

**Gauge interpretation.** A change of multipole origin is a change of expansion point of the fields, hence a gauge transformation. For a uniform $\mathbf B(t)$, moving the origin to $\mathbf G$ gives $\mathbf A_G = \mathbf A_0 - \mathbf A_0(\mathbf G)$, a gauge transformation with $\chi = \mathbf r\cdot\mathbf A_0(\mathbf G)$ and a compensating $\phi_G = \tfrac12\mathbf r\cdot(\partial_t\mathbf B\times\mathbf G)$. The fields are unchanged (NRS Eqs. 3.212–3.216). This is the gauge-origin problem of [[magnetizability-and-gauge-origin]] in classical form.

## General and traceless electric multipoles

**Counting.** The moments of order $n$, $\int x^iy^jz^k\rho$ with $i + j + k = n$, are symmetric in all indices. There are $(n+1)(n+2)/2$ of them, as many as Cartesian Gaussians of angular momentum $n$ (NRS Eqs. 3.217–3.218).

**Static fields from external sources.** In the stationary case $E^{[n-1]}_{j_1;j_2\cdots} = -\phi^{[n]}_{j_1\cdots j_n}$ is fully symmetric (NRS Eqs. 3.219–3.223). If the field is produced by charges away from the expansion point, $\phi$ also satisfies Laplace's equation there, so all its traces vanish (NRS Eqs. 3.224–3.225). The traces of $Q^{[n]}$ then do not couple, and they can be removed.

**Traceless quadrupole.** For the quadrupole (Buckingham's convention, NRS Eqs. 3.226–3.228):

$$
\Theta_{ij} = \tfrac32\Big(Q^{[2]}_{ij} - \tfrac13Q^{[2]}_{kk}\delta_{ij}\Big),\qquad
-\tfrac12Q^{[2]}_{ij}E^{[1]}_{i;j} = -\tfrac13\Theta_{ij}E^{[1]}_{i;j} - \tfrac16Q^{[2]}_{kk}E^{[1]}_{i;i} .
$$

The last term is the Poisson term, proportional to $\nabla\cdot\mathbf E = \rho/\varepsilon_0$ at the expansion point. It vanishes when no source charge is there, which is why the nuclear quadrupole interaction involves only $\Theta$ ([[hyperfine-coupling-and-epr]]).

**General order.** Traceless moments of any order follow from (NRS Eqs. 3.229–3.232)

$$
\Theta^{[n]}_{j_1\cdots j_n} = \int\rho(\mathbf r)\frac{(-1)^n}{n!}r^{2n+1}\Big(\prod_k\nabla_{j_k}\Big)\frac1r\,d^3r,
$$

for example $\Theta^{[3]}_{ijk} = \tfrac12(5Q_{ijk} - Q_{ill}\delta_{jk} - Q_{jll}\delta_{ik} - Q_{kll}\delta_{ij})$. Removing the $\tfrac12n(n-1)$ trace conditions leaves $2n + 1$ independent components. These are as many as spherical Gaussians, and as many as the spherical multipoles

$$
q_{\ell m} = \int r^\ell Y^*_{\ell m}(\theta,\phi)\rho(\mathbf r)\,d^3r
$$

from the addition theorem $\frac{1}{|\mathbf r - \mathbf r'|} = \sum_{\ell m}\frac{4\pi}{2\ell+1}\frac{r_<^\ell}{r_>^{\ell+1}}Y^*_{\ell m}Y_{\ell m}$ (NRS Eqs. 3.233–3.236; see [[central-potentials-and-spherical-harmonics]]).

**Static but not dynamic.** In time-dependent fields the gradients are not symmetric and not traceless. The octupole and hexadecapole couplings keep trace terms that do not vanish, even for external sources (NRS Eq. 3.237). The general Cartesian moments are therefore the safe definition when static and dynamic situations are treated together.

**Field of a distant source.** The potential of a distribution around $\mathbf R_A$, seen from far away, is (NRS Eqs. 3.238–3.240)

$$
\phi_A(\mathbf r) = \frac{1}{4\pi\varepsilon_0}\Big[\frac{Q^{[0]}_A}{|\mathbf r - \mathbf R_A|} + \frac{Q^{[1]}_{A;i}(\mathbf r - \mathbf R_A)_i}{|\mathbf r - \mathbf R_A|^3} + Q^{[2]}_{A;ij}\frac{3(\mathbf r - \mathbf R_A)_i(\mathbf r - \mathbf R_A)_j - \delta_{ij}|\mathbf r - \mathbf R_A|^2}{|\mathbf r - \mathbf R_A|^5} + \cdots\Big].
$$

General source moments multiply traceless observer factors. The quadrupole term here follows NRS; with the $\tfrac12$ of the Taylor series it reads $\tfrac12Q^{[2]}_{ij}(\cdots)$, equivalently $\Theta_{ij}(\cdots)/3$ (to verify against another text).

## What symmetry allows

**Parity.** For a Hamiltonian commuting with inversion, eigenstates have parity $\pm1$ and the density is even. Since $x^iy^jz^k$ has parity $(-1)^n$, every odd electric multipole vanishes: atoms and nuclei have no permanent dipole (NRS Eqs. 3.241–3.243; [[parity-and-parity-selection-rules]]). The current transforms like $\mathbf r$, so magnetic multipoles behave the opposite way: even ones vanish.

**Angular momentum.** For a state $|\eta LM\rangle$, the operator $\hat q_{\ell m}$ connects $L$ only to $L' = |\ell - L|,\dots,\ell + L$, with $M' = M + m$ (NRS Eqs. 3.244–3.247). The expectation value vanishes unless $\ell\le2L$.

- **Atoms.** An $S$ state ($L = 0$) has only the monopole. A $P$ state can have at most a quadrupole.
- **Nuclei.** A nucleus with $I = \tfrac12$ has no quadrupole moment, the rule used for NQR.

**Magnetic multipoles.** $m^{[n]}$ is symmetric in all indices but the first. $\nabla\cdot\mathbf B = 0$ holds at every point, so tracing the first index with any other gives zero. Magnetic multipoles are therefore traceless by construction, with $(3n^2 + n + 2)/2$ independent components. Away from the source currents $\nabla\times\mathbf B = \mathbf 0$ as well, so the antisymmetric part of the magnetic quadrupole is redundant there (NRS Eqs. 3.248–3.250). Time reversal removes further components (NRS Sec. 4.2).

## Worked example

!!! example "Water multipoles at the HF/aug-cc-pVTZ level (computed for this note)"
    **Setup.** Geometry $r_{\rm OH} = 0.9572$ Å, $\angle$HOH $= 104.5^\circ$. The $C_2$ axis is $z$, the molecular plane $yz$, and $x$ out of plane. Electronic plus nuclear moments, in au:

    | origin | $\mu_z$ | $\Theta_{xx}$ (out of plane) | $\Theta_{yy}$ (in plane, ⊥ $C_2$) | $\Theta_{zz}$ ($C_2$) | $Q^{[2]}_{zz}$ |
    |---|---:|---:|---:|---:|---:|
    | centre of mass | −0.78039 | −1.79775 | 1.89777 | −0.10003 | −4.4883 |
    | O nucleus | −0.78039 | −1.89385 | 1.80167 | 0.09218 | −4.2961 |
    | centre of mass + 1 bohr along $z$ | −0.78039 | −2.57813 | 1.11739 | 1.46075 | −2.9275 |

    The sign of $\mu_z$ reflects the axis orientation (H atoms at negative $z$).

    **What the table shows.**

    - **The dipole is origin independent.** It is $|\mu| = 1.9835$ D, against 1.855 D measured; HF overestimates it.
    - **The quadrupole is origin dependent.** A 1 bohr shift changes $\Theta_{zz}$ by 1.56 au, more than ten times its value at the centre of mass.
    - **The shift rule holds.** Eq. [[#shift]] with $\mathbf G = (0,0,1)$ and the computed $\boldsymbol\mu$ reproduces the shifted $\Theta$ exactly. The $xx$ and $yy$ components of $Q^{[2]}$ do not change, since $\boldsymbol\mu\parallel z$.

    **Against experiment.** At the centre of mass $\Theta = (-8.07, 8.51, -0.45)\times10^{-40}$ C m², i.e. $(-2.42, 2.55, -0.13)\times10^{-26}$ esu cm². This is close to the microwave values of Verhoeven and Dymanus, $(-2.50, 2.63, -0.13)\times10^{-26}$ esu cm² (to verify).

    **Counting** for $n = 1,\dots,5$:

    | $n$ | general | traceless | magnetic |
    |---:|---:|---:|---:|
    | 1 | 3 | 3 | 3 |
    | 2 | 6 | 5 | 8 |
    | 3 | 10 | 7 | 16 |
    | 4 | 15 | 9 | 27 |
    | 5 | 21 | 11 | 41 |

## Source

Norman, Ruud and Saue, *Principles and Practices of Molecular Properties: Theory, Modeling, and Simulations* (Wiley, 2018), Sec. 3.3.4, Eqs. (3.210)–(3.216); Sec. 3.3.5.1, Eqs. (3.217)–(3.240); Sec. 3.3.5.2, Eqs. (3.241)–(3.247); Sec. 3.3.6, Eqs. (3.248)–(3.250). The quadrupole shift rule and the nuclear-spin remark are general knowledge. J. Verhoeven and A. Dymanus, *J. Chem. Phys.* **52**, 3222 (1970), for the measured water quadrupole (recalled, not read; to verify). The calculations are in `Claude outputs/part1_fields_batchD.py`, section E.
