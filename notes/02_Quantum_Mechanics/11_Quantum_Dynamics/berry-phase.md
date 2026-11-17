---
id: berry-phase
title: Berry's phase
summary: The geometric phase acquired in adiabatic evolution. When the parameters of a Hamiltonian are carried slowly around a closed loop, an eigenstate returns with its dynamic phase plus a phase γ = i∮⟨ψ|∇ψ⟩·dR that depends only on the path, not on the time taken. Covers gauge invariance, the Berry connection and curvature, the spin-1/2 result γ = ∓Ω/2 (verified by integrating the Schrödinger equation), the sign change around a conical intersection, and the Aharonov-Bohm effect as a Berry phase.
status: in-progress
kind: theory
level: advanced
tags: [berry-phase, geometric-phase, adiabatic-theorem, berry-connection, berry-curvature, solid-angle, conical-intersection, aharonov-bohm, gauge-invariance, sakurai, griffiths]
prerequisites: [sudden-and-adiabatic-approximations, spin-one-half]
related: [minimal-coupling-and-aharonov-bohm, born-oppenheimer-approximation, nonadiabatic-couplings, rotation-operator-and-rotational-symmetry]
order: 70
date: 2026-11-15
---

## Where the phase comes from

In adiabatic evolution a system that starts in the $n$-th eigenstate of $H(t)$ stays in it ([[sudden-and-adiabatic-approximations]]):

$$
\Psi_n(t) = e^{i\theta_n(t)}\,e^{i\gamma_n(t)}\,\psi_n(t) ,\qquad \theta_n = -\frac1\hbar\int_0^tE_n\,dt' ,\qquad \gamma_n(t) = i\int_0^t\Big\langle\psi_n\Big|\frac{\partial\psi_n}{\partial t'}\Big\rangle\,dt' .
$$

Suppose $H$ depends on time only through a set of parameters $\mathbf R(t) = (R_1,R_2,\dots)$: a field direction, the positions of nuclei, the shape of a box. Then $\partial\psi_n/\partial t = \nabla_R\psi_n\cdot d\mathbf R/dt$ and the time drops out:

$$
\gamma_n = i\int_{\mathbf R_i}^{\mathbf R_f}\langle\psi_n|\nabla_R\psi_n\rangle\cdot d\mathbf R .
$$

The dynamic phase records how long the journey took. The **geometric phase** records only which path was followed in parameter space. If the parameters return to their starting values after a closed loop $C$,

$$
\boxed{\,\gamma_n(C) = i\oint_C\langle\psi_n|\nabla_R\psi_n\rangle\cdot d\mathbf R\,}
$$

This is **Berry's phase**.

## Is it real, or a matter of convention?

The eigenstates $\psi_n(\mathbf R)$ are defined only up to a phase at each $\mathbf R$. Under a change of convention $\psi_n\to e^{i\chi(\mathbf R)}\psi_n$, the integrand

$$
\mathbf A_n(\mathbf R)\equiv i\,\langle\psi_n|\nabla_R\psi_n\rangle
$$

(real, and called the Berry connection) changes to $\mathbf A_n - \nabla_R\chi$, exactly like a vector potential under a gauge transformation. Consequently:

- For an open path $\gamma_n$ can be changed at will, even to zero. It has no physical meaning.
- For a closed loop, with $\psi_n(\mathbf R)$ chosen single valued, $\oint\nabla\chi\cdot d\mathbf R = 0$ (or a multiple of $2\pi$), so $\gamma_n(C)$ is gauge invariant modulo $2\pi$. It is measurable by interference: split a beam, take one part around the loop, recombine.

For three parameters, Stokes' theorem turns the loop integral into a flux:

$$
\gamma_n(C) = \int_S\mathbf B_n\cdot d\mathbf a ,\qquad \mathbf B_n = \nabla_R\times\mathbf A_n = i\sum_{m\ne n}\frac{\langle\psi_n|\nabla_RH|\psi_m\rangle\times\langle\psi_m|\nabla_RH|\psi_n\rangle}{(E_m - E_n)^2} .
$$

The Berry curvature $\mathbf B_n$ is gauge invariant and needs no phase convention, only matrix elements of $\nabla_RH$. The denominator shows that its sources are the points of degeneracy in parameter space. The phase is determined by how the loop is placed relative to them.

## Spin one-half

Let $H = \tfrac12\hbar\omega_1\,\hat{\mathbf n}\cdot\boldsymbol\sigma$ with the direction $\hat{\mathbf n}(\theta,\phi)$ as parameter. The eigenstate with spin up along $\hat{\mathbf n}$ can be written

$$
\chi_+ = \begin{pmatrix}\cos(\theta/2)\\ e^{i\phi}\sin(\theta/2)\end{pmatrix} ,\qquad i\,\Big\langle\chi_+\Big|\frac{\partial\chi_+}{\partial\phi}\Big\rangle = -\sin^2(\theta/2) ,\qquad i\,\Big\langle\chi_+\Big|\frac{\partial\chi_+}{\partial\theta}\Big\rangle = 0 .
$$

Carrying $\hat{\mathbf n}$ once around a cone of half-angle $\alpha$ about the $z$ axis,

$$
\gamma_+ = -\sin^2(\alpha/2)\times2\pi = -\pi(1 - \cos\alpha) = -\tfrac12\Omega ,
$$

where $\Omega = 2\pi(1 - \cos\alpha)$ is the solid angle subtended by the loop. The general result, from the curvature formula, is $\mathbf B_\pm = \mp\hat{\mathbf R}/(2R^2)$, the field of a monopole of strength $\mp\tfrac12$ sitting at the degeneracy $\mathbf R = 0$, and for any loop

$$
\boxed{\,\gamma_\pm(C) = \mp\tfrac12\,\Omega(C)\,}
$$

For spin $s$ and magnetic quantum number $m$ along the field the result is $-m\Omega$.

!!! example "Check by solving the Schrödinger equation"

    The field sweeps a cone of half-angle $\alpha$ once, at angular velocity $\omega$, with $H = \tfrac12\hbar\omega_1\hat{\mathbf n}(t)\cdot\boldsymbol\sigma$. Start spin up along the field, integrate over one period $T = 2\pi/\omega$, take the phase of $\langle\chi_+(0)|\chi(T)\rangle$ and subtract the dynamic phase $-\omega_1T/2$. A second, independent evaluation uses the discrete gauge-invariant formula $\gamma = -\arg\prod_k\langle\psi_k|\psi_{k+1}\rangle$ over 2000 points on the loop, with eigenvectors from numerical diagonalization (whose phases are arbitrary).

    | $\alpha$ | $-\Omega/2$ | from dynamics, $\omega_1/\omega = 50$ | $\omega_1/\omega = 200$ | discrete formula |
    |---|---|---|---|---|
    | $30^\circ$ | $-0.4209$ | $-0.4289$ | $-0.4229$ | $-0.4209$ |
    | $60^\circ$ | $-1.5708$ | $-1.5946$ | $-1.5767$ | $-1.5708$ |
    | $90^\circ$ | $-3.1416$ | $-3.1730$ | $-3.1495$ | $-3.1416$ |
    | $120^\circ$ | $-4.7124$ | $-4.7357$ | $-4.7183$ | $-4.7124$ |

    (Phases are defined modulo $2\pi$; the dynamical values are shown on the branch nearest $-\Omega/2$.) The deviation falls in proportion to $\omega/\omega_1$, as expected for the leading non-adiabatic correction, while the dynamic phase being subtracted is as large as 628 rad.

Berry's phase for spin $\tfrac12$ has been measured with neutrons in a slowly rotating field, and its counterpart for photons in a helically wound optical fibre.

## Real Hamiltonians and conical intersections

If the eigenfunctions can be chosen real, $\langle\psi_n|\nabla\psi_n\rangle = \tfrac12\nabla\langle\psi_n|\psi_n\rangle = 0$, and one might conclude that the phase always vanishes. It does not, because a smooth real choice may fail to be single valued. Take the real symmetric two-parameter Hamiltonian

$$
H(x,y) = \begin{pmatrix}x & y\\ y & -x\end{pmatrix} ,\qquad E_\pm = \pm\sqrt{x^2 + y^2} ,
$$

whose two levels touch at the origin in a double cone. With $x = r\cos\phi$, $y = r\sin\phi$ the upper eigenvector is $(\cos\tfrac\phi2,\ \sin\tfrac\phi2)$. It is real and smooth, but after one circuit of the origin, $\phi\to\phi + 2\pi$, it has changed sign. Making it single valued costs a complex factor $e^{i\phi/2}$, and then $\gamma = \pm\pi$. Either way the state returns multiplied by $-1$.

Numerically, with the discrete formula: a circle around the origin gives $|\gamma| = 3.1416$, an off-centre ellipse enclosing the origin gives $3.1416$, and a circle that does not enclose it gives $0$. The phase is topological: it counts whether the degeneracy is encircled. This agrees with the solid-angle rule, since $H = x\sigma_z + y\sigma_x$ confines $\hat{\mathbf n}$ to a great circle, which subtends $\Omega = 2\pi$.

This is the situation at a **conical intersection** of two electronic potential energy surfaces. The real electronic wave function of [[born-oppenheimer-approximation]] changes sign when the nuclei are carried around the intersection, and the nuclear wave function must compensate, which alters the nuclear dynamics even when the system never reaches the intersection.

## The Aharonov-Bohm effect

A charged particle confined in a small box that is carried around a line of magnetic flux $\Phi$, through a region where $\mathbf B = 0$ but $\mathbf A\ne0$, has box eigenfunctions of the form $e^{ig(\mathbf r)}\psi_n(\mathbf r - \mathbf R)$ with $g = (q/\hbar)\int_{\mathbf R}^{\mathbf r}\mathbf A\cdot d\mathbf r'$. Then $\langle\psi_n|\nabla_R\psi_n\rangle = -i(q/\hbar)\mathbf A(\mathbf R)$ and

$$
\gamma_n(C) = \frac q\hbar\oint\mathbf A\cdot d\mathbf R = \frac{q\Phi}{\hbar} ,
$$

the Aharonov-Bohm phase of [[minimal-coupling-and-aharonov-bohm]]. Here the Berry connection is the electromagnetic vector potential itself (times $q/\hbar$), and the analogy used above becomes an identity.

## Source

Sakurai and Napolitano, *Modern Quantum Mechanics* (3rd ed., Cambridge University Press, 2021), Sec. 5.6.3, pp. 331-333, Eqs. (5.230)-(5.242) (geometric phase as a loop integral, the generalized field $\mathbf B_n$ (5.236), its expression through $\nabla_RH$); Sec. 5.6.4, pp. 333-335, Eqs. (5.243)-(5.253) (spin $\tfrac12$: $\mathbf B_\pm$ (5.252), $\gamma_\pm = \mp\Omega/2$ (5.253), neutron data in Fig. 5.7); Sec. 5.6.5, pp. 335-337 (Aharonov-Bohm and the monopole quantization condition). Sakurai gives the references: M. V. Berry, Proc. R. Soc. London, Ser. A 392, 45 (1984); Richardson et al., Phys. Rev. Lett. 61, 2030 (1988) (neutrons); Tomita and Chiao, Phys. Rev. Lett. 57, 937 (1986) (optical fibre).

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 11.5.2, Eqs. (11.92)-(11.95) (dynamic and geometric phases), Example 11.4; Problems 11.21 (Berry's phase for the electron in a rotating field), 11.22 and 11.35. Page numbers are not given because the PDF used is an e-book rendering without print pagination.

The conical-intersection section is not from either book. The sign change was first pointed out, to my recollection, by Herzberg and Longuet-Higgins, Discuss. Faraday Soc. 35, 77 (1963); this reference is quoted from memory and is to be verified. The general-spin result $-m\Omega$ is from Berry's paper as I recall it, also to be verified. All numbers are computed in `griffiths/ch11_dynamics.py` (section F).
