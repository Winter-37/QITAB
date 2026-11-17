---
id: scattering-cross-sections-and-amplitude
title: Cross sections and the scattering amplitude
summary: The language of scattering. Classical definitions of impact parameter, differential cross section dσ/dΩ = (b/sin θ)|db/dθ| and total cross section, with the hard sphere and Rutherford scattering as examples. In quantum mechanics a stationary scattering state behaves at large r as an incident plane wave plus an outgoing spherical wave f(θ) exp(ikr)/r, and dσ/dΩ = |f(θ)|². The rest of the chapter is about calculating f.
status: in-progress
kind: theory
level: intermediate
tags: [scattering, cross-section, differential-cross-section, scattering-amplitude, impact-parameter, rutherford-scattering, hard-sphere, probability-current, griffiths]
prerequisites: [schrodinger-equation-in-three-dimensions, free-particle-and-wave-packets, one-dimensional-scattering-and-transfer-matrix]
related: [partial-wave-analysis-and-phase-shifts, born-approximation-and-lippmann-schwinger, low-energy-scattering-and-resonances]
order: 10
date: 2026-11-15
---

## Classical scattering

A particle of energy $E$ approaches a fixed scattering centre along a line that would miss it by the **impact parameter** $b$, and leaves at the **scattering angle** $\theta$ measured from the incident direction. For a central force the motion is in a plane and the whole problem is the function $b(\theta)$.

Particles that arrive through an element of area $d\sigma = b\,db\,d\phi$ leave into the solid angle $d\Omega = \sin\theta\,d\theta\,d\phi$. Their ratio is the **differential cross section**

$$
D(\theta) \equiv \frac{d\sigma}{d\Omega} = \frac{b}{\sin\theta}\Big|\frac{db}{d\theta}\Big| ,
$$

and the **total cross section** is $\sigma = \int D(\theta)\,d\Omega$: the area of incident beam that is scattered at all.

For a beam of **luminosity** $\mathcal L$ (particles per unit area per unit time) the number scattered into $d\Omega$ per unit time is $dN = \mathcal L\,D(\theta)\,d\Omega$. This is the operational definition: $D = (1/\mathcal L)\,dN/d\Omega$ is what a detector measures.

!!! example "Hard sphere"

    A particle bouncing elastically off a sphere of radius $R$ has $b = R\cos(\theta/2)$, so

    $$
    D(\theta) = \frac{R\cos(\theta/2)}{\sin\theta}\cdot\frac R2\sin(\theta/2) = \frac{R^2}{4} ,\qquad \sigma = \pi R^2 .
    $$

    The scattering is isotropic and the total cross section is the geometrical area.

!!! example "Rutherford scattering"

    For the Coulomb repulsion of charges $q_1$ and $q_2$,

    $$
    b = \frac{q_1q_2}{8\pi\epsilon_0E}\cot(\theta/2) ,\qquad D(\theta) = \Big[\frac{q_1q_2}{16\pi\epsilon_0E\,\sin^2(\theta/2)}\Big]^2 .
    $$

    The total cross section is infinite, because the Coulomb force has infinite range and every impact parameter gives some deflection.

    Numbers for a 5 MeV alpha particle on gold ($q_1q_2/4\pi\epsilon_0 = 2\times79\times1.440$ MeV fm): the length $q_1q_2/(4\pi\epsilon_0E)$ is 45.5 fm, $D(90^\circ) = 518\ \text{fm}^2 = 5.18$ b/sr, and the cross section for deflection by more than $90^\circ$ is $\pi b(90^\circ)^2 = \pi(22.75\ \text{fm})^2 = 16.3$ b. In a foil 1 μm thick with $5.90\times10^{28}$ atoms per m$^3$, the fraction of particles turned back is $n\sigma t = 9.6\times10^{-5}$: about one in ten thousand, from single collisions with a point charge. (Target recoil is neglected.)

## Quantum scattering

There are no trajectories, so no impact parameter. Instead one looks for a solution of the time-independent Schrödinger equation that describes a steady incident beam and a steady scattered flux. For a potential that falls off faster than $1/r$, at large $r$

$$
\boxed{\,\psi(r,\theta) \approx A\Big[e^{ikz} + f(\theta)\,\frac{e^{ikr}}{r}\Big] ,\qquad k = \frac{\sqrt{2mE}}{\hbar}\,}
$$

The first term is the incident plane wave travelling along $z$. The second is an outgoing spherical wave: the factor $1/r$ conserves probability, and $f(\theta)$, the **scattering amplitude**, has the dimension of length. For a potential without axial symmetry $f$ depends on $\phi$ as well.

**Cross section.** The incident wave carries the probability current $\mathbf j_{\rm inc} = |A|^2(\hbar k/m)\,\hat{\mathbf z}$. For the scattered wave the radial current at large $r$ is

$$
j_r = \frac{\hbar}{m}\,\mathrm{Im}\Big(\psi_{\rm sc}^*\frac{\partial\psi_{\rm sc}}{\partial r}\Big) = |A|^2\frac{\hbar k}{m}\frac{|f(\theta)|^2}{r^2} ,
$$

up to terms that fall off faster. The probability per unit time crossing the area $r^2d\Omega$ is $j_rr^2d\Omega$, and dividing by the incident current gives

$$
\boxed{\,\frac{d\sigma}{d\Omega} = |f(\theta)|^2\,}
$$

The interference between the incident and scattered waves was ignored. It averages to zero away from the forward direction for any beam of finite width; at $\theta = 0$ it does not, and it accounts for the removal of flux from the beam (the optical theorem, [[partial-wave-analysis-and-phase-shifts]]).

**What remains.** Everything is contained in $f(\theta)$. Two methods of calculating it follow: [[partial-wave-analysis-and-phase-shifts]], which is exact and most useful at low energy, and [[born-approximation-and-lippmann-schwinger]], which is perturbative and most useful at high energy or for weak potentials.

## Two-body scattering

For two particles interacting through $V(\mathbf r_1 - \mathbf r_2)$ the centre of mass moves freely and the relative coordinate obeys the one-body equation with the reduced mass $\mu = m_1m_2/(m_1 + m_2)$. All formulas of this chapter then apply in the centre-of-mass frame with $m\to\mu$, and the angles must be transformed to the laboratory frame if the target is not heavy.

## Source

Griffiths and Schroeter, *Introduction to Quantum Mechanics* (3rd ed., Cambridge University Press, 2018), Sec. 10.1, Eqs. (10.1)-(10.14), Examples 10.1 and 10.2 (hard sphere); Problem 10.1 (Rutherford scattering). Page numbers are not given because the PDF used is an e-book rendering without print pagination.

Sakurai and Napolitano, *Modern Quantum Mechanics* (3rd ed., Cambridge University Press, 2021), Sec. 6.2, pp. 376-381, for the asymptotic wave function and the cross section from a formal point of view.

The derivation of the cross section from the probability current is written out here in my own steps; Griffiths argues with the probability passing through an area in time $dt$. The gold-foil numbers are my own example (gold density 19.3 g/cm$^3$ and molar mass 196.97 g/mol entered from memory), computed in `griffiths/ch10_scattering.py` (section E).
